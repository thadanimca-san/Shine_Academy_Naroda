import 'dart:async';

import 'package:flutter/material.dart';

import '../models/account_model.dart';
import '../models/depreciation_model.dart';
import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../models/solution_model.dart';
import '../services/accounting_solver.dart';
import '../services/brs_generator.dart';
import '../services/brs_solver.dart';
import '../services/cash_flow_generator.dart';
import '../services/depreciation_generator.dart';
import '../services/final_accounts_generator.dart';
import '../services/localization_service.dart';
import '../services/partnership_generator.dart';
import '../services/problem_generator.dart';
import '../services/progress_service.dart';
import '../services/rectification_generator.dart';
import '../widgets/cash_flow_statement_widget.dart';
import '../widgets/capital_accounts_widget.dart';
import '../widgets/final_accounts_widget.dart';
import '../widgets/journal_attempt_widget.dart';
import '../widgets/self_check_widget.dart';
import '../widgets/solution_reveal_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A timed mock test spanning several topics at once, matching the mixed
/// nature of an actual board exam paper rather than single-topic drills.
/// Duration and question mix scale with [schoolClass]/[board] pattern —
/// kept simple (fixed mix, fixed duration) for the first version.
class MockTestScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final Medium medium;

  const MockTestScreen({super.key, required this.board, required this.schoolClass, this.medium = Medium.english});

  @override
  State<MockTestScreen> createState() => _MockTestScreenState();
}

class _MockTestScreenState extends State<MockTestScreen> {
  late final List<_MockQuestion> _questions;
  late final Duration _testDuration;
  Timer? _timer;
  late Duration _remaining;
  bool _submitted = false;
  int _correctCount = 0;
  int _attemptedCount = 0;

  @override
  void initState() {
    super.initState();
    _questions = _buildQuestionSet();
    // Class 12 mock includes extra long-answer topics on top of the
    // Class 11 core set, so it gets more time on the clock.
    _testDuration = Duration(minutes: widget.schoolClass == 12 ? 45 : 30);
    _remaining = _testDuration;
    _startTimer();
  }

  @override
  void dispose() {
    _timer?.cancel();
    super.dispose();
  }

  List<_MockQuestion> _buildQuestionSet() {
    final journalProblem = ProblemGenerator.generateJournalLedgerTrialBalance(
      board: widget.board,
      schoolClass: widget.schoolClass,
      difficulty: 3,
      transactionCount: 3,
    );
    final depProblem = DepreciationGenerator.generate(board: widget.board, schoolClass: widget.schoolClass, difficulty: 3);
    final rectProblem = RectificationGenerator.generate(board: widget.board, schoolClass: widget.schoolClass, difficulty: 3, caseCount: 2);
    final brsProblem = BrsGenerator.generate(board: widget.board, schoolClass: widget.schoolClass, difficulty: 3, itemCount: 3);

    final questions = [
      for (final e in journalProblem.transactions) _MockQuestion.journal(e, widget.medium),
      _MockQuestion.depreciation(depProblem, widget.medium),
      for (final c in rectProblem.cases) _MockQuestion.rectification(c.rectifyingEntry, c.errorDescription, widget.medium),
      _MockQuestion.brs(brsProblem, widget.medium),
    ];

    // Class 12 topics only make sense on a Class 12 mock test — a Class
    // 11 student sitting this test should never see Partnership/Company/
    // Cash Flow questions they haven't been taught yet.
    if (widget.schoolClass == 12) {
      final faProblem = FinalAccountsGenerator.generate(board: widget.board, schoolClass: widget.schoolClass, difficulty: 3);
      final admProblem = PartnershipGenerator.generateAdmission(board: widget.board, schoolClass: widget.schoolClass, difficulty: 3);
      final cfProblem = CashFlowGenerator.generate(board: widget.board, schoolClass: widget.schoolClass, difficulty: 3);
      questions.addAll([
        _MockQuestion.finalAccounts(faProblem, widget.medium),
        _MockQuestion.partnershipAdmission(admProblem, widget.medium),
        _MockQuestion.cashFlow(cfProblem, widget.medium),
      ]);
    }

    return questions;
  }

  void _startTimer() {
    _timer = Timer.periodic(const Duration(seconds: 1), (_) {
      setState(() {
        if (_remaining.inSeconds <= 1) {
          _remaining = Duration.zero;
          _timer?.cancel();
          _submitted = true;
        } else {
          _remaining -= const Duration(seconds: 1);
        }
      });
    });
  }

  String get _timeLabel {
    final m = _remaining.inMinutes.toString().padLeft(2, '0');
    final s = (_remaining.inSeconds % 60).toString().padLeft(2, '0');
    return '$m:$s';
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Mock Test')),
        actions: [
          Padding(
            padding: const EdgeInsets.only(right: 16),
            child: Center(
              child: Text(_timeLabel,
                  style: TextStyle(
                      fontWeight: FontWeight.bold, fontSize: 16, color: _remaining.inMinutes < 5 ? Colors.red : null)),
            ),
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          if (!_submitted) Text('Score so far: $_correctCount / $_attemptedCount', style: TextStyle(color: Colors.grey)),
          const SizedBox(height: 8),
          for (var i = 0; i < _questions.length; i++) _buildQuestion(i),
          if (!_submitted)
            Center(
              child: ElevatedButton(
                onPressed: () {
                  _timer?.cancel();
                  setState(() => _submitted = true);
                },
                child: Text(LocalizationService.t('Submit Test', widget.medium)),
              ),
            ),
          if (_submitted)
            Card(
              color: Colors.indigo.withValues(alpha: 0.08),
              child: Padding(
                padding: const EdgeInsets.all(16),
                child: Text('Test Submitted — Journal-style score: $_correctCount / $_attemptedCount\n'
                    'Review each question below for the full worked solution.'),
              ),
            ),
        ],
      ),
    );
  }

  Widget _buildQuestion(int index) {
    final q = _questions[index];
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 8),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text('Q${index + 1}. ${q.prompt}', style: TextStyle(fontWeight: FontWeight.bold)),
          const SizedBox(height: 6),
          if (q.journalEntry != null && !_submitted)
            JournalAttemptWidget(
              correctEntry: q.journalEntry!,
              lineCount: q.journalEntry!.lines.length,
              medium: widget.medium,
              onSubmit: (correct) {
                setState(() {
                  _attemptedCount++;
                  if (correct) _correctCount++;
                });
                ProgressService.recordAttempt(topicKey: q.topicKey, wasCorrect: correct);
              },
            ),
          if (_submitted && q.journalEntry != null)
            SolutionRevealWidget(
                steps: AccountingSolver.explainEntry(q.journalEntry!, board: widget.board).steps, medium: widget.medium),
          if (_submitted && q.brsSteps != null) SolutionRevealWidget(steps: q.brsSteps!, medium: widget.medium),
          if (_submitted && q.freeText != null) Text(q.freeText!),
          if (_submitted && q.solutionWidget != null) q.solutionWidget!,
          if (_submitted && q.journalEntry == null)
            SelfCheckWidget(key: ValueKey('mock-$index'), topicKey: q.topicKey),
        ],
      ),
    );
  }
}

class _MockQuestion {
  final String prompt;
  final String topicKey;
  final JournalEntry? journalEntry;
  final List<SolutionStep>? brsSteps;
  final String? freeText;
  final Widget? solutionWidget;

  const _MockQuestion({
    required this.prompt,
    required this.topicKey,
    this.journalEntry,
    this.brsSteps,
    this.freeText,
    this.solutionWidget,
  });

  factory _MockQuestion.journal(JournalEntry entry, Medium medium) => _MockQuestion(
        prompt: 'Journalise: ${LocalizationService.translatePhrase(entry.transactionText, medium)}',
        topicKey: ProgressService.topicJournalLedgerTB,
        journalEntry: entry,
      );

  factory _MockQuestion.rectification(JournalEntry entry, String description, Medium medium) => _MockQuestion(
        prompt: 'Rectify: ${LocalizationService.translatePhrase(description, medium)}',
        topicKey: ProgressService.topicRectification,
        journalEntry: entry,
      );

  factory _MockQuestion.depreciation(GeneratedDepreciationProblem depProblem, Medium medium) {
    final s = depProblem.schedule;
    final methodLabel = s.method == DepreciationMethod.straightLine ? 'SLM' : 'WDV';
    return _MockQuestion(
      prompt: 'A ${s.assetName} costing ₹${s.originalCost.toStringAsFixed(0)} depreciates at '
          '${s.ratePercent}% p.a. under $methodLabel. Find the depreciation for Year 1.',
      topicKey: ProgressService.topicDepreciation,
      freeText: 'Answer: ₹${s.rows[0].depreciationAmount.toStringAsFixed(0)}',
    );
  }

  factory _MockQuestion.brs(GeneratedBrsProblem brsProblem, Medium medium) {
    return _MockQuestion(
      prompt: 'Prepare a BRS. Cash Book balance: ₹${brsProblem.cashBookBalance.toStringAsFixed(0)}, '
          '${brsProblem.items.length} reconciling items given.',
      topicKey: ProgressService.topicBrs,
      brsSteps: BrsSolver.explainStartingFromCashBook(brsProblem.cashBookBalance, brsProblem.items),
    );
  }

  factory _MockQuestion.finalAccounts(GeneratedFinalAccountsProblem faProblem, Medium medium) {
    final i = faProblem.input;
    return _MockQuestion(
      prompt: 'Prepare Final Accounts. Opening Stock ₹${i.openingStock.toStringAsFixed(0)}, '
          'Purchases ₹${i.purchases.toStringAsFixed(0)}, Sales ₹${i.sales.toStringAsFixed(0)}, '
          '${faProblem.adjustments.length} adjustment(s) given.',
      topicKey: ProgressService.topicFinalAccounts,
      solutionWidget: FinalAccountsWidget(result: faProblem.result, medium: medium),
    );
  }

  factory _MockQuestion.partnershipAdmission(GeneratedAdmissionProblem admProblem, Medium medium) {
    final sharePercent = (admProblem.newPartnerShare * 100).round();
    return _MockQuestion(
      prompt: '${admProblem.existingPartners.map((p) => p.name).join(' and ')} admit '
          '${admProblem.newPartnerName} for a $sharePercent% share, bringing capital '
          '₹${admProblem.newPartnerCapital.toStringAsFixed(0)}. Goodwill '
          '₹${admProblem.goodwill.totalFirmGoodwill.toStringAsFixed(0)}. Prepare Capital Accounts.',
      topicKey: ProgressService.topicPartnership,
      solutionWidget: CapitalAccountsWidget(rows: admProblem.result.capitalAccounts, medium: medium),
    );
  }

  factory _MockQuestion.cashFlow(GeneratedCashFlowProblem cfProblem, Medium medium) {
    final d = cfProblem.data;
    return _MockQuestion(
      prompt: 'Prepare a Cash Flow Statement. Net Profit before Tax ₹${d.netProfitBeforeTax.toStringAsFixed(0)}, '
          'Depreciation ₹${d.depreciationForYear.toStringAsFixed(0)}.',
      topicKey: ProgressService.topicCashFlow,
      solutionWidget: CashFlowStatementWidget(result: cfProblem.result, medium: medium),
    );
  }
}
