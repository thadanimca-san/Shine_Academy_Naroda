import 'package:flutter/material.dart';

import '../models/account_model.dart';
import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../services/accounting_solver.dart';
import '../services/localization_service.dart';
import '../services/problem_generator.dart';
import '../services/progress_service.dart';
import '../widgets/journal_attempt_widget.dart';
import '../widgets/ledger_table_widget.dart';
import '../widgets/solution_reveal_widget.dart';
import '../widgets/trial_balance_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

enum _Stage { journal, ledger, trialBalance, done }

/// Full student practice flow for one generated problem: attempt each
/// journal entry step-by-step with instant feedback, then move on to
/// ledger posting and trial balance once journalising is complete.
class StudentPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;
  final Medium medium;

  const StudentPracticeScreen({
    super.key,
    required this.board,
    required this.schoolClass,
    this.difficulty = 2,
    this.medium = Medium.english,
  });

  @override
  State<StudentPracticeScreen> createState() => _StudentPracticeScreenState();
}

class _StudentPracticeScreenState extends State<StudentPracticeScreen> {
  late GeneratedProblem _problem;
  _Stage _stage = _Stage.journal;
  int _correctCount = 0;
  int _attemptedCount = 0;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  void _generateNewProblem() {
    setState(() {
      _problem = ProblemGenerator.generateJournalLedgerTrialBalance(
        board: widget.board,
        schoolClass: widget.schoolClass,
        difficulty: widget.difficulty,
      );
      _stage = _Stage.journal;
      _correctCount = 0;
      _attemptedCount = 0;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('${_problem.topic.chapter} — Practice'),
        actions: [
          IconButton(
            icon: Icon(Icons.refresh),
            tooltip: 'New Problem',
            onPressed: _generateNewProblem,
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(LocalizationService.translatePhrase(_problem.questionText, widget.medium), style: TextStyle(fontSize: 15)),
          const SizedBox(height: 8),
          if (_stage == _Stage.journal) ..._buildJournalStage(),
          if (_stage == _Stage.ledger) _buildLedgerStage(),
          if (_stage == _Stage.trialBalance) _buildTrialBalanceStage(),
          if (_stage == _Stage.done) _buildDoneStage(),
        ],
      ),
    );
  }

  List<Widget> _buildJournalStage() {
    return [
      Text('Score so far: $_correctCount / $_attemptedCount',
          style: TextStyle(color: Colors.grey)),
      const SizedBox(height: 8),
      for (final entry in _problem.transactions) ...[
        JournalAttemptWidget(
          key: ValueKey('${_problem.id}-${entry.transactionText}'),
          correctEntry: entry,
          lineCount: entry.lines.length,
          medium: widget.medium,
          onSubmit: (correct) {
            setState(() {
              _attemptedCount++;
              if (correct) _correctCount++;
            });
            ProgressService.recordAttempt(topicKey: ProgressService.topicJournalLedgerTB, wasCorrect: correct);
          },
        ),
        SolutionRevealTrigger(
          key: ValueKey('${_problem.id}-reveal-${entry.transactionText}'),
          entry: entry,
          board: widget.board,
          medium: widget.medium,
        ),
      ],
      const SizedBox(height: 16),
      Center(
        child: ElevatedButton(
          onPressed: () => setState(() => _stage = _Stage.ledger),
          child: Text(TrilingualService.instance.getUIText('Proceed to Ledger Posting')),
        ),
      ),
    ];
  }

  Widget _buildLedgerStage() {
    final ledgers = AccountingSolver.postToLedger(_problem.transactions);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(TrilingualService.instance.getUIText('Ledger Accounts (auto-posted from your journal for reference):'),
            style: TextStyle(fontWeight: FontWeight.bold)),
        const SizedBox(height: 8),
        for (final l in ledgers) LedgerTableWidget(ledger: l, medium: widget.medium),
        const SizedBox(height: 16),
        Center(
          child: ElevatedButton(
            onPressed: () => setState(() => _stage = _Stage.trialBalance),
            child: Text(TrilingualService.instance.getUIText('Proceed to Trial Balance')),
          ),
        ),
      ],
    );
  }

  Widget _buildTrialBalanceStage() {
    final ledgers = AccountingSolver.postToLedger(_problem.transactions);
    final tb = AccountingSolver.buildTrialBalance(ledgers);
    return Column(
      children: [
        TrialBalanceWidget(trialBalance: tb, medium: widget.medium),
        const SizedBox(height: 16),
        Center(
          child: ElevatedButton(
            onPressed: () => setState(() => _stage = _Stage.done),
            child: Text(TrilingualService.instance.getUIText('Finish')),
          ),
        ),
      ],
    );
  }

  Widget _buildDoneStage() {
    return Column(
      children: [
        Text('Journal Score: $_correctCount / $_attemptedCount',
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
        const SizedBox(height: 16),
        ElevatedButton(onPressed: _generateNewProblem, child: Text(TrilingualService.instance.getUIText('Try a New Problem'))),
      ],
    );
  }
}

/// Small collapsible trigger that shows the full step-by-step solution
/// for one journal entry, reusing the same solver output the answer key
/// PDF is built from.
class SolutionRevealTrigger extends StatefulWidget {
  final JournalEntry entry;
  final Board board;
  final Medium medium;

  const SolutionRevealTrigger({super.key, required this.entry, required this.board, this.medium = Medium.english});

  @override
  State<SolutionRevealTrigger> createState() => _SolutionRevealTriggerState();
}

class _SolutionRevealTriggerState extends State<SolutionRevealTrigger> {
  bool _open = false;

  @override
  Widget build(BuildContext context) {
    final solution = AccountingSolver.explainEntry(widget.entry, board: widget.board);
    return Padding(
      padding: const EdgeInsets.only(left: 8, bottom: 12),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TextButton.icon(
            onPressed: () => setState(() => _open = !_open),
            icon: Icon(_open ? Icons.visibility_off : Icons.lightbulb_outline),
            label: Text(_open
                ? LocalizationService.t('Hide Solution', widget.medium)
                : LocalizationService.t('Show Solution', widget.medium)),
          ),
          if (_open) SolutionRevealWidget(steps: solution.steps, medium: widget.medium),
        ],
      ),
    );
  }
}
