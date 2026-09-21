import 'package:flutter/material.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:printing/printing.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../services/brs_generator.dart';
import '../services/cash_book_generator.dart';
import '../services/cash_flow_generator.dart';
import '../services/company_accounts_generator.dart';
import '../services/depreciation_generator.dart';
import '../services/dissolution_generator.dart';
import '../services/final_accounts_generator.dart';
import '../services/paper_pdf_service.dart';
import '../services/partnership_generator.dart';
import '../services/problem_generator.dart';
import '../services/rectification_generator.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

enum _Topic {
  journalLedgerTB,
  cashBook,
  depreciation,
  rectification,
  brs,
  finalAccounts,
  partnershipAdmission,
  partnershipDeparture,
  partnershipDissolution,
  shareIssue,
  cashFlow,
}

/// The class each topic is first taught in (GSEB and CBSE agree on this
/// split) — used to hide Class-12-only topics from the dropdown when a
/// teacher has Class 11 selected, and vice versa is never restrictive
/// since Class 12 topics remain available alongside Class 11 ones.
int _minClassFor(_Topic topic) => switch (topic) {
      _Topic.journalLedgerTB ||
      _Topic.cashBook ||
      _Topic.depreciation ||
      _Topic.rectification ||
      _Topic.brs ||
      _Topic.finalAccounts =>
        11,
      _Topic.partnershipAdmission ||
      _Topic.partnershipDeparture ||
      _Topic.partnershipDissolution ||
      _Topic.shareIssue ||
      _Topic.cashFlow =>
        12,
    };

const _topicLabels = {
  _Topic.journalLedgerTB: 'Journal, Ledger & Trial Balance',
  _Topic.cashBook: 'Double Column Cash Book',
  _Topic.depreciation: 'Depreciation (SLM & WDV)',
  _Topic.rectification: 'Rectification of Errors',
  _Topic.brs: 'Bank Reconciliation Statement',
  _Topic.finalAccounts: 'Final Accounts',
  _Topic.partnershipAdmission: 'Partnership — Admission',
  _Topic.partnershipDeparture: 'Partnership — Retirement/Death',
  _Topic.partnershipDissolution: 'Partnership — Dissolution',
  _Topic.shareIssue: 'Company Accounts — Issue of Shares',
  _Topic.cashFlow: 'Cash Flow Statement',
};

/// Teacher-facing screen: choose board/class/topic/marks/set-count, then
/// generate a question paper PDF and a matching fully-worked answer key
/// PDF from the same underlying problems (so they never disagree).
class TeacherPaperScreen extends StatefulWidget {
  const TeacherPaperScreen({super.key});

  @override
  State<TeacherPaperScreen> createState() => _TeacherPaperScreenState();
}

class _TeacherPaperScreenState extends State<TeacherPaperScreen> {
  Board _board = Board.cbse;
  int _schoolClass = 11;
  Medium _medium = Medium.english;
  int _questionCount = 3;
  int _difficulty = 3;
  _Topic _topic = _Topic.journalLedgerTB;
  final _titleController = TextEditingController(text: 'Journal, Ledger & Trial Balance — Practice Test');

  List<GeneratedProblem>? _lastGenerated;
  List<GeneratedProblem>? _setBGenerated;
  List<GeneratedCashBookProblem>? _lastGeneratedCB;
  List<GeneratedCashBookProblem>? _setBGeneratedCB;
  List<GeneratedDepreciationProblem>? _lastGeneratedDep;
  List<GeneratedDepreciationProblem>? _setBGeneratedDep;
  List<GeneratedRectificationProblem>? _lastGeneratedRect;
  List<GeneratedRectificationProblem>? _setBGeneratedRect;
  List<GeneratedBrsProblem>? _lastGeneratedBrs;
  List<GeneratedBrsProblem>? _setBGeneratedBrs;
  List<GeneratedFinalAccountsProblem>? _lastGeneratedFA;
  List<GeneratedFinalAccountsProblem>? _setBGeneratedFA;
  List<GeneratedAdmissionProblem>? _lastGeneratedAdm;
  List<GeneratedAdmissionProblem>? _setBGeneratedAdm;
  List<GeneratedDepartureProblem>? _lastGeneratedDep2;
  List<GeneratedDepartureProblem>? _setBGeneratedDep2;
  List<GeneratedShareIssueProblem>? _lastGeneratedShare;
  List<GeneratedShareIssueProblem>? _setBGeneratedShare;
  List<GeneratedCashFlowProblem>? _lastGeneratedCF;
  List<GeneratedCashFlowProblem>? _setBGeneratedCF;
  List<GeneratedDissolutionProblem>? _lastGeneratedDiss;
  List<GeneratedDissolutionProblem>? _setBGeneratedDiss;

  @override
  void dispose() {
    _titleController.dispose();
    super.dispose();
  }

  List<GeneratedProblem> _rollNewSet() => List.generate(
        _questionCount,
        (_) => ProblemGenerator.generateJournalLedgerTrialBalance(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  List<GeneratedCashBookProblem> _rollNewCashBookSet() => List.generate(
        _questionCount,
        (_) => CashBookGenerator.generate(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  List<GeneratedDepreciationProblem> _rollNewDepreciationSet() => List.generate(
        _questionCount,
        (_) => DepreciationGenerator.generate(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  List<GeneratedRectificationProblem> _rollNewRectificationSet() => List.generate(
        _questionCount,
        (_) => RectificationGenerator.generate(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  List<GeneratedBrsProblem> _rollNewBrsSet() => List.generate(
        _questionCount,
        (_) => BrsGenerator.generate(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  List<GeneratedFinalAccountsProblem> _rollNewFinalAccountsSet() => List.generate(
        _questionCount,
        (_) => FinalAccountsGenerator.generate(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  List<GeneratedAdmissionProblem> _rollNewAdmissionSet() => List.generate(
        _questionCount,
        (_) => PartnershipGenerator.generateAdmission(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  List<GeneratedDepartureProblem> _rollNewDepartureSet() => List.generate(
        _questionCount,
        (_) => PartnershipGenerator.generateDeparture(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  List<GeneratedShareIssueProblem> _rollNewShareIssueSet() => List.generate(
        _questionCount,
        (_) => CompanyAccountsGenerator.generate(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  List<GeneratedCashFlowProblem> _rollNewCashFlowSet() => List.generate(
        _questionCount,
        (_) => CashFlowGenerator.generate(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  List<GeneratedDissolutionProblem> _rollNewDissolutionSet() => List.generate(
        _questionCount,
        (_) => DissolutionGenerator.generate(
          board: _board,
          schoolClass: _schoolClass,
          difficulty: _difficulty,
        ),
      );

  void _clearAllGenerated() {
    _lastGenerated = null;
    _setBGenerated = null;
    _lastGeneratedCB = null;
    _setBGeneratedCB = null;
    _lastGeneratedDep = null;
    _setBGeneratedDep = null;
    _lastGeneratedRect = null;
    _setBGeneratedRect = null;
    _lastGeneratedBrs = null;
    _setBGeneratedBrs = null;
    _lastGeneratedFA = null;
    _setBGeneratedFA = null;
    _lastGeneratedAdm = null;
    _setBGeneratedAdm = null;
    _lastGeneratedDep2 = null;
    _setBGeneratedDep2 = null;
    _lastGeneratedShare = null;
    _setBGeneratedShare = null;
    _lastGeneratedCF = null;
    _setBGeneratedCF = null;
    _lastGeneratedDiss = null;
    _setBGeneratedDiss = null;
  }

  void _generateProblems() {
    setState(() {
      _clearAllGenerated();
      switch (_topic) {
        case _Topic.journalLedgerTB:
          _lastGenerated = _rollNewSet();
        case _Topic.cashBook:
          _lastGeneratedCB = _rollNewCashBookSet();
        case _Topic.depreciation:
          _lastGeneratedDep = _rollNewDepreciationSet();
        case _Topic.rectification:
          _lastGeneratedRect = _rollNewRectificationSet();
        case _Topic.brs:
          _lastGeneratedBrs = _rollNewBrsSet();
        case _Topic.finalAccounts:
          _lastGeneratedFA = _rollNewFinalAccountsSet();
        case _Topic.partnershipAdmission:
          _lastGeneratedAdm = _rollNewAdmissionSet();
        case _Topic.partnershipDeparture:
          _lastGeneratedDep2 = _rollNewDepartureSet();
        case _Topic.partnershipDissolution:
          _lastGeneratedDiss = _rollNewDissolutionSet();
        case _Topic.shareIssue:
          _lastGeneratedShare = _rollNewShareIssueSet();
        case _Topic.cashFlow:
          _lastGeneratedCF = _rollNewCashFlowSet();
      }
    });
  }

  void _generateSetB() {
    setState(() {
      switch (_topic) {
        case _Topic.journalLedgerTB:
          _setBGenerated = _rollNewSet();
        case _Topic.cashBook:
          _setBGeneratedCB = _rollNewCashBookSet();
        case _Topic.depreciation:
          _setBGeneratedDep = _rollNewDepreciationSet();
        case _Topic.rectification:
          _setBGeneratedRect = _rollNewRectificationSet();
        case _Topic.brs:
          _setBGeneratedBrs = _rollNewBrsSet();
        case _Topic.finalAccounts:
          _setBGeneratedFA = _rollNewFinalAccountsSet();
        case _Topic.partnershipAdmission:
          _setBGeneratedAdm = _rollNewAdmissionSet();
        case _Topic.partnershipDeparture:
          _setBGeneratedDep2 = _rollNewDepartureSet();
        case _Topic.partnershipDissolution:
          _setBGeneratedDiss = _rollNewDissolutionSet();
        case _Topic.shareIssue:
          _setBGeneratedShare = _rollNewShareIssueSet();
        case _Topic.cashFlow:
          _setBGeneratedCF = _rollNewCashFlowSet();
      }
    });
  }

  /// Every _preview* method below builds a PDF and hands it to
  /// Printing.layoutPdf. Both steps can throw (missing font asset, low
  /// storage, printing plugin failure on an older device) — without this
  /// wrapper that would crash the app with no feedback, which is
  /// especially bad for a teacher mid-class trying to print a paper.
  Future<void> _showPdf(Future<pw.Document> Function() buildDoc) async {
    try {
      final doc = await buildDoc();
      await Printing.layoutPdf(onLayout: (_) => doc.save());
    } catch (e) {
      if (!mounted) return;
      ScaffoldMessenger.of(context).showSnackBar(
        SnackBar(content: Text('Could not generate the PDF: $e')),
      );
    }
  }

  Future<void> _previewQuestionPaper({required List<GeneratedProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewAnswerKey({required List<GeneratedProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewCashBookQuestionPaper({required List<GeneratedCashBookProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildCashBookQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewCashBookAnswerKey({required List<GeneratedCashBookProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildCashBookAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewDepreciationQuestionPaper({required List<GeneratedDepreciationProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildDepreciationQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewDepreciationAnswerKey({required List<GeneratedDepreciationProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildDepreciationAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewRectificationQuestionPaper({required List<GeneratedRectificationProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildRectificationQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewRectificationAnswerKey({required List<GeneratedRectificationProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildRectificationAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewBrsQuestionPaper({required List<GeneratedBrsProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildBrsQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewBrsAnswerKey({required List<GeneratedBrsProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildBrsAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewFinalAccountsQuestionPaper({required List<GeneratedFinalAccountsProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildFinalAccountsQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewFinalAccountsAnswerKey({required List<GeneratedFinalAccountsProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildFinalAccountsAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewAdmissionQuestionPaper({required List<GeneratedAdmissionProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildPartnershipAdmissionQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewAdmissionAnswerKey({required List<GeneratedAdmissionProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildPartnershipAdmissionAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewDepartureQuestionPaper({required List<GeneratedDepartureProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildPartnershipDepartureQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewDepartureAnswerKey({required List<GeneratedDepartureProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildPartnershipDepartureAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewShareIssueQuestionPaper({required List<GeneratedShareIssueProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildShareIssueQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewShareIssueAnswerKey({required List<GeneratedShareIssueProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildShareIssueAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewCashFlowQuestionPaper({required List<GeneratedCashFlowProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildCashFlowQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewCashFlowAnswerKey({required List<GeneratedCashFlowProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildCashFlowAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewDissolutionQuestionPaper({required List<GeneratedDissolutionProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildDissolutionQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  Future<void> _previewDissolutionAnswerKey({required List<GeneratedDissolutionProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildDissolutionAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
            medium: _medium,
          ));

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(TrilingualService.instance.getUIText('Teacher — Paper Generator'))),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          DropdownButtonFormField<_Topic>(
            decoration: InputDecoration(labelText: 'Topic (Class $_schoolClass)', border: const OutlineInputBorder()),
            initialValue: _topic,
            items: [
              for (final entry in _topicLabels.entries)
                if (_minClassFor(entry.key) <= _schoolClass)
                  DropdownMenuItem(value: entry.key, child: Text(entry.value)),
            ],
            onChanged: (v) {
              setState(() {
                _topic = v!;
                _titleController.text = switch (_topic) {
                  _Topic.journalLedgerTB => 'Journal, Ledger & Trial Balance — Practice Test',
                  _Topic.cashBook => 'Double Column Cash Book — Practice Test',
                  _Topic.depreciation => 'Depreciation — Practice Test',
                  _Topic.rectification => 'Rectification of Errors — Practice Test',
                  _Topic.brs => 'Bank Reconciliation Statement — Practice Test',
                  _Topic.finalAccounts => 'Final Accounts — Practice Test',
                  _Topic.partnershipAdmission => 'Partnership — Admission of a Partner — Practice Test',
                  _Topic.partnershipDeparture => 'Partnership — Retirement/Death of a Partner — Practice Test',
                  _Topic.partnershipDissolution => 'Partnership — Dissolution of Firm — Practice Test',
                  _Topic.shareIssue => 'Company Accounts — Issue of Shares — Practice Test',
                  _Topic.cashFlow => 'Cash Flow Statement — Practice Test',
                };
                _clearAllGenerated();
              });
            },
          ),
          const SizedBox(height: 8),
          Padding(
            padding: const EdgeInsets.symmetric(horizontal: 4),
            child: Text(
              _topicDescription(_topic),
              style: TextStyle(fontSize: 12, color: Colors.grey.shade700, fontStyle: FontStyle.italic),
            ),
          ),
          const SizedBox(height: 12),
          TextField(
            controller: _titleController,
            decoration: const InputDecoration(labelText: 'Paper Title', border: OutlineInputBorder()),
          ),
          const SizedBox(height: 12),
          Row(
            children: [
              Expanded(
                child: DropdownButtonFormField<Board>(
                  decoration: const InputDecoration(labelText: 'Board', border: OutlineInputBorder()),
                  initialValue: _board,
                  items: [
                    DropdownMenuItem(value: Board.gseb, child: Text(TrilingualService.instance.getUIText('GSEB'))),
                    DropdownMenuItem(value: Board.cbse, child: Text(TrilingualService.instance.getUIText('CBSE'))),
                  ],
                  onChanged: (v) => setState(() => _board = v!),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: DropdownButtonFormField<int>(
                  decoration: const InputDecoration(labelText: 'Class', border: OutlineInputBorder()),
                  initialValue: _schoolClass,
                  items: [
                    DropdownMenuItem(value: 11, child: Text(TrilingualService.instance.getUIText('Class 11'))),
                    DropdownMenuItem(value: 12, child: Text(TrilingualService.instance.getUIText('Class 12'))),
                  ],
                  onChanged: (v) {
                    setState(() {
                      _schoolClass = v!;
                      // If the currently selected topic isn't taught in the
                      // newly selected class, fall back to the first topic
                      // that is, rather than leaving an invalid selection.
                      if (_minClassFor(_topic) > _schoolClass) {
                        _topic = _topicLabels.keys.firstWhere((t) => _minClassFor(t) <= _schoolClass);
                        _titleController.text = '${_topicLabels[_topic]} — Practice Test';
                        _clearAllGenerated();
                      }
                    });
                  },
                ),
              ),
            ],
          ),
          const SizedBox(height: 12),
          DropdownButtonFormField<Medium>(
            decoration: const InputDecoration(labelText: 'Medium (Journal/Ledger/TB papers only)', border: OutlineInputBorder()),
            initialValue: _medium,
            items: [
              DropdownMenuItem(value: Medium.english, child: Text(TrilingualService.instance.getUIText('English'))),
              DropdownMenuItem(value: Medium.gujarati, child: Text(TrilingualService.instance.getUIText('ગુજરાતી (Gujarati)'))),
            ],
            onChanged: (v) => setState(() => _medium = v!),
          ),
          const SizedBox(height: 12),
          Text('Number of Questions: $_questionCount'),
          Slider(
            value: _questionCount.toDouble(),
            min: 1,
            max: 8,
            divisions: 7,
            label: '$_questionCount',
            onChanged: (v) => setState(() => _questionCount = v.round()),
          ),
          Text('Difficulty: $_difficulty / 5'),
          Slider(
            value: _difficulty.toDouble(),
            min: 1,
            max: 5,
            divisions: 4,
            label: '$_difficulty',
            onChanged: (v) => setState(() => _difficulty = v.round()),
          ),
          const SizedBox(height: 12),
          ElevatedButton.icon(
            onPressed: _generateProblems,
            icon: Icon(Icons.auto_awesome),
            label: Text(TrilingualService.instance.getUIText('Generate Problem Set')),
          ),
          const SizedBox(height: 16),
          if (_lastGenerated != null) ...[
            Text('${_lastGenerated!.length} questions generated, '
                '${_lastGenerated!.fold<double>(0, (s, p) => s + p.marks).round()} total marks'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewQuestionPaper(problems: _lastGenerated!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewAnswerKey(problems: _lastGenerated!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGenerated != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewQuestionPaper(problems: _setBGenerated!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewAnswerKey(problems: _setBGenerated!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedCB != null) ...[
            Text('${_lastGeneratedCB!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewCashBookQuestionPaper(problems: _lastGeneratedCB!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewCashBookAnswerKey(problems: _lastGeneratedCB!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGeneratedCB != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewCashBookQuestionPaper(problems: _setBGeneratedCB!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewCashBookAnswerKey(problems: _setBGeneratedCB!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedDep != null) ...[
            Text('${_lastGeneratedDep!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewDepreciationQuestionPaper(problems: _lastGeneratedDep!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewDepreciationAnswerKey(problems: _lastGeneratedDep!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGeneratedDep != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewDepreciationQuestionPaper(problems: _setBGeneratedDep!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewDepreciationAnswerKey(problems: _setBGeneratedDep!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedRect != null) ...[
            Text('${_lastGeneratedRect!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewRectificationQuestionPaper(problems: _lastGeneratedRect!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewRectificationAnswerKey(problems: _lastGeneratedRect!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGeneratedRect != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewRectificationQuestionPaper(problems: _setBGeneratedRect!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewRectificationAnswerKey(problems: _setBGeneratedRect!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedBrs != null) ...[
            Text('${_lastGeneratedBrs!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewBrsQuestionPaper(problems: _lastGeneratedBrs!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewBrsAnswerKey(problems: _lastGeneratedBrs!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGeneratedBrs != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewBrsQuestionPaper(problems: _setBGeneratedBrs!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewBrsAnswerKey(problems: _setBGeneratedBrs!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedFA != null) ...[
            Text('${_lastGeneratedFA!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewFinalAccountsQuestionPaper(problems: _lastGeneratedFA!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewFinalAccountsAnswerKey(problems: _lastGeneratedFA!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGeneratedFA != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewFinalAccountsQuestionPaper(problems: _setBGeneratedFA!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewFinalAccountsAnswerKey(problems: _setBGeneratedFA!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedAdm != null) ...[
            Text('${_lastGeneratedAdm!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewAdmissionQuestionPaper(problems: _lastGeneratedAdm!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewAdmissionAnswerKey(problems: _lastGeneratedAdm!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGeneratedAdm != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewAdmissionQuestionPaper(problems: _setBGeneratedAdm!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewAdmissionAnswerKey(problems: _setBGeneratedAdm!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedDep2 != null) ...[
            Text('${_lastGeneratedDep2!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewDepartureQuestionPaper(problems: _lastGeneratedDep2!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewDepartureAnswerKey(problems: _lastGeneratedDep2!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGeneratedDep2 != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewDepartureQuestionPaper(problems: _setBGeneratedDep2!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewDepartureAnswerKey(problems: _setBGeneratedDep2!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedShare != null) ...[
            Text('${_lastGeneratedShare!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewShareIssueQuestionPaper(problems: _lastGeneratedShare!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewShareIssueAnswerKey(problems: _lastGeneratedShare!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGeneratedShare != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewShareIssueQuestionPaper(problems: _setBGeneratedShare!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewShareIssueAnswerKey(problems: _setBGeneratedShare!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedCF != null) ...[
            Text('${_lastGeneratedCF!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewCashFlowQuestionPaper(problems: _lastGeneratedCF!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewCashFlowAnswerKey(problems: _lastGeneratedCF!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGeneratedCF != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewCashFlowQuestionPaper(problems: _setBGeneratedCF!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewCashFlowAnswerKey(problems: _setBGeneratedCF!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedDiss != null) ...[
            Text('${_lastGeneratedDiss!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewDissolutionQuestionPaper(problems: _lastGeneratedDiss!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Question Paper (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewDissolutionAnswerKey(problems: _lastGeneratedDiss!, setLabel: 'Set A'),
                  icon: Icon(Icons.check_circle_outline),
                  label: Text(TrilingualService.instance.getUIText('Answer Key A (Full Working)')),
                ),
                OutlinedButton.icon(
                  onPressed: _generateSetB,
                  icon: Icon(Icons.shuffle),
                  label: Text(TrilingualService.instance.getUIText('Generate Set B (same structure, new numbers)')),
                ),
              ],
            ),
            if (_setBGeneratedDiss != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewDissolutionQuestionPaper(problems: _setBGeneratedDiss!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Question Paper (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewDissolutionAnswerKey(problems: _setBGeneratedDiss!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
        ],
      ),
    );
  }

  String _topicDescription(_Topic topic) => switch (topic) {
        _Topic.journalLedgerTB =>
          'Class 11. Journalising transactions, posting to ledger, and preparing a trial balance — the foundational topic.',
        _Topic.cashBook => 'Class 11. Double Column Cash Book with Cash, Bank & Discount columns, including contra entries.',
        _Topic.depreciation => 'Class 11. Straight Line and Written Down Value depreciation methods, year-by-year schedule.',
        _Topic.rectification =>
          'Class 11. Finding and correcting errors of omission, commission, principle & compensating, using Suspense A/c where needed.',
        _Topic.brs => 'Class 11. Reconciling Cash Book and Pass Book balances.',
        _Topic.finalAccounts => 'Class 11-12. Trading A/c, Profit & Loss A/c and Balance Sheet with adjustments.',
        _Topic.partnershipAdmission => 'Class 12. Admission of a new partner — new ratio, sacrificing ratio, goodwill adjustment.',
        _Topic.partnershipDeparture =>
          'Class 12. Retirement or death of a partner — gaining ratio, goodwill adjustment, settlement.',
        _Topic.partnershipDissolution => 'Class 12. Dissolution of firm — Realisation Account, settling partners.',
        _Topic.shareIssue =>
          'Class 12. Issue of shares at par/premium, application/allotment/calls, forfeiture & reissue.',
        _Topic.cashFlow => 'Class 12. Cash Flow Statement (Indirect Method) — Operating, Investing & Financing activities.',
      };
}
