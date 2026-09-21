import 'package:flutter/material.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:printing/printing.dart';

import '../models/board_model.dart';
import '../services/central_tendency_generator.dart';
import '../services/correlation_generator.dart';
import '../services/dispersion_generator.dart';
import '../services/index_number_generator.dart';
import '../services/paper_pdf_service.dart';
import '../services/regression_generator.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

enum _Topic { centralTendency, dispersion, correlation, indexNumbers, regression }

/// Teacher-facing screen: choose topic/board/class/question-count/
/// difficulty, then generate a worksheet PDF and a matching fully-worked
/// answer key PDF from the same underlying problems (so they never
/// disagree).
class TeacherPaperScreen extends StatefulWidget {
  const TeacherPaperScreen({super.key});

  @override
  State<TeacherPaperScreen> createState() => _TeacherPaperScreenState();
}

class _TeacherPaperScreenState extends State<TeacherPaperScreen> {
  Board _board = Board.gseb;
  int _schoolClass = 11;
  int _questionCount = 3;
  int _difficulty = 3;
  _Topic _topic = _Topic.centralTendency;
  final _titleController = TextEditingController(text: 'Measures of Central Tendency — Practice Worksheet');

  List<GeneratedCentralTendencyProblem>? _lastGeneratedCT;
  List<GeneratedCentralTendencyProblem>? _setBGeneratedCT;
  List<GeneratedDispersionProblem>? _lastGeneratedDisp;
  List<GeneratedDispersionProblem>? _setBGeneratedDisp;
  List<GeneratedCorrelationProblem>? _lastGeneratedCorr;
  List<GeneratedCorrelationProblem>? _setBGeneratedCorr;
  List<GeneratedIndexNumberProblem>? _lastGeneratedIdx;
  List<GeneratedIndexNumberProblem>? _setBGeneratedIdx;
  List<GeneratedRegressionProblem>? _lastGeneratedReg;
  List<GeneratedRegressionProblem>? _setBGeneratedReg;

  @override
  void dispose() {
    _titleController.dispose();
    super.dispose();
  }

  List<GeneratedCentralTendencyProblem> _rollNewCTSet() => List.generate(
        _questionCount,
        (_) => CentralTendencyGenerator.generate(board: _board, schoolClass: _schoolClass, difficulty: _difficulty),
      );

  List<GeneratedDispersionProblem> _rollNewDispSet() => List.generate(
        _questionCount,
        (_) => DispersionGenerator.generate(board: _board, schoolClass: _schoolClass, difficulty: _difficulty),
      );

  List<GeneratedCorrelationProblem> _rollNewCorrSet() => List.generate(
        _questionCount,
        (_) => CorrelationGenerator.generate(board: _board, schoolClass: _schoolClass, difficulty: _difficulty),
      );

  List<GeneratedIndexNumberProblem> _rollNewIdxSet() => List.generate(
        _questionCount,
        (_) => IndexNumberGenerator.generate(board: _board, schoolClass: _schoolClass, difficulty: _difficulty),
      );

  List<GeneratedRegressionProblem> _rollNewRegSet() => List.generate(
        _questionCount,
        (_) => RegressionGenerator.generate(board: _board, schoolClass: _schoolClass, difficulty: _difficulty),
      );

  void _clearAllGenerated() {
    _lastGeneratedCT = null;
    _setBGeneratedCT = null;
    _lastGeneratedDisp = null;
    _setBGeneratedDisp = null;
    _lastGeneratedCorr = null;
    _setBGeneratedCorr = null;
    _lastGeneratedIdx = null;
    _setBGeneratedIdx = null;
    _lastGeneratedReg = null;
    _setBGeneratedReg = null;
  }

  void _generateProblems() {
    setState(() {
      _clearAllGenerated();
      switch (_topic) {
        case _Topic.centralTendency:
          _lastGeneratedCT = _rollNewCTSet();
        case _Topic.dispersion:
          _lastGeneratedDisp = _rollNewDispSet();
        case _Topic.correlation:
          _lastGeneratedCorr = _rollNewCorrSet();
        case _Topic.indexNumbers:
          _lastGeneratedIdx = _rollNewIdxSet();
        case _Topic.regression:
          _lastGeneratedReg = _rollNewRegSet();
      }
    });
  }

  void _generateSetB() {
    setState(() {
      switch (_topic) {
        case _Topic.centralTendency:
          _setBGeneratedCT = _rollNewCTSet();
        case _Topic.dispersion:
          _setBGeneratedDisp = _rollNewDispSet();
        case _Topic.correlation:
          _setBGeneratedCorr = _rollNewCorrSet();
        case _Topic.indexNumbers:
          _setBGeneratedIdx = _rollNewIdxSet();
        case _Topic.regression:
          _setBGeneratedReg = _rollNewRegSet();
      }
    });
  }

  /// Every PDF preview call below builds a document then hands it to
  /// Printing.layoutPdf — both steps can throw (missing font asset, low
  /// storage, printing plugin failure on an older device). Wrapping here
  /// once avoids a crash with no feedback, which is especially bad for a
  /// teacher mid-class trying to print a worksheet.
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

  Future<void> _previewCTQuestionPaper({required List<GeneratedCentralTendencyProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildCentralTendencyQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
          ));

  Future<void> _previewCTAnswerKey({required List<GeneratedCentralTendencyProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildCentralTendencyAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
          ));

  Future<void> _previewDispQuestionPaper({required List<GeneratedDispersionProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildDispersionQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
          ));

  Future<void> _previewDispAnswerKey({required List<GeneratedDispersionProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildDispersionAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
          ));

  Future<void> _previewCorrQuestionPaper({required List<GeneratedCorrelationProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildCorrelationQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
          ));

  Future<void> _previewCorrAnswerKey({required List<GeneratedCorrelationProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildCorrelationAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
          ));

  Future<void> _previewIdxQuestionPaper({required List<GeneratedIndexNumberProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildIndexNumberQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
          ));

  Future<void> _previewIdxAnswerKey({required List<GeneratedIndexNumberProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildIndexNumberAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
          ));

  Future<void> _previewRegQuestionPaper({required List<GeneratedRegressionProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildRegressionQuestionPaper(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
          ));

  Future<void> _previewRegAnswerKey({required List<GeneratedRegressionProblem> problems, String setLabel = 'Set A'}) =>
      _showPdf(() => PaperPdfService.buildRegressionAnswerKey(
            problems: problems,
            board: _board,
            schoolClass: _schoolClass,
            paperTitle: _titleController.text,
            setLabel: setLabel,
          ));

  String _topicDescription(_Topic topic) => switch (topic) {
        _Topic.centralTendency => 'Class 11-12. Mean, Median & Mode — covers individual, discrete and continuous series.',
        _Topic.dispersion =>
          'Class 11-12. Range, Mean Deviation, Standard Deviation & Coefficient of Variation — covers individual, discrete and continuous series.',
        _Topic.correlation => "Class 11-12. Karl Pearson's Coefficient of Correlation between two variables.",
        _Topic.indexNumbers =>
          "Class 11-12. Simple Aggregative, Price Relatives, Laspeyres' & Paasche's methods.",
        _Topic.regression => 'Class 12. Regression lines of Y on X and X on Y using the deviation method.',
      };

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(TrilingualService.instance.getUIText('Teacher — Worksheet Generator'))),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          DropdownButtonFormField<_Topic>(
            decoration: const InputDecoration(labelText: 'Topic', border: OutlineInputBorder()),
            initialValue: _topic,
            items: [
              DropdownMenuItem(value: _Topic.centralTendency, child: Text(TrilingualService.instance.getUIText('Measures of Central Tendency'))),
              DropdownMenuItem(value: _Topic.dispersion, child: Text(TrilingualService.instance.getUIText('Measures of Dispersion'))),
              DropdownMenuItem(value: _Topic.correlation, child: Text(TrilingualService.instance.getUIText('Correlation'))),
              DropdownMenuItem(value: _Topic.indexNumbers, child: Text(TrilingualService.instance.getUIText('Index Numbers'))),
              DropdownMenuItem(value: _Topic.regression, child: Text(TrilingualService.instance.getUIText('Regression Analysis'))),
            ],
            onChanged: (v) {
              setState(() {
                _topic = v!;
                _titleController.text = switch (_topic) {
                  _Topic.centralTendency => 'Measures of Central Tendency — Practice Worksheet',
                  _Topic.dispersion => 'Measures of Dispersion — Practice Worksheet',
                  _Topic.correlation => 'Correlation — Practice Worksheet',
                  _Topic.indexNumbers => 'Index Numbers — Practice Worksheet',
                  _Topic.regression => 'Regression Analysis — Practice Worksheet',
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
            decoration: const InputDecoration(labelText: 'Worksheet Title', border: OutlineInputBorder()),
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
                  onChanged: (v) => setState(() => _schoolClass = v!),
                ),
              ),
            ],
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
          Text('Difficulty: $_difficulty / 5 (1-2: individual series, 3: discrete, 4-5: continuous)'),
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
          if (_lastGeneratedCT != null) ...[
            Text('${_lastGeneratedCT!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewCTQuestionPaper(problems: _lastGeneratedCT!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Worksheet (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewCTAnswerKey(problems: _lastGeneratedCT!, setLabel: 'Set A'),
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
            if (_setBGeneratedCT != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewCTQuestionPaper(problems: _setBGeneratedCT!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Worksheet (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewCTAnswerKey(problems: _setBGeneratedCT!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedDisp != null) ...[
            Text('${_lastGeneratedDisp!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewDispQuestionPaper(problems: _lastGeneratedDisp!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Worksheet (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewDispAnswerKey(problems: _lastGeneratedDisp!, setLabel: 'Set A'),
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
            if (_setBGeneratedDisp != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewDispQuestionPaper(problems: _setBGeneratedDisp!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Worksheet (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewDispAnswerKey(problems: _setBGeneratedDisp!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedCorr != null) ...[
            Text('${_lastGeneratedCorr!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewCorrQuestionPaper(problems: _lastGeneratedCorr!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Worksheet (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewCorrAnswerKey(problems: _lastGeneratedCorr!, setLabel: 'Set A'),
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
            if (_setBGeneratedCorr != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewCorrQuestionPaper(problems: _setBGeneratedCorr!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Worksheet (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewCorrAnswerKey(problems: _setBGeneratedCorr!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedIdx != null) ...[
            Text('${_lastGeneratedIdx!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewIdxQuestionPaper(problems: _lastGeneratedIdx!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Worksheet (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewIdxAnswerKey(problems: _lastGeneratedIdx!, setLabel: 'Set A'),
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
            if (_setBGeneratedIdx != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewIdxQuestionPaper(problems: _setBGeneratedIdx!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Worksheet (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewIdxAnswerKey(problems: _setBGeneratedIdx!, setLabel: 'Set B'),
                    icon: Icon(Icons.check_circle_outline),
                    label: Text(TrilingualService.instance.getUIText('Answer Key B (Full Working)')),
                  ),
                ],
              ),
            ],
          ],
          if (_lastGeneratedReg != null) ...[
            Text('${_lastGeneratedReg!.length} questions generated'),
            const SizedBox(height: 12),
            Wrap(
              spacing: 10,
              runSpacing: 10,
              children: [
                ElevatedButton.icon(
                  onPressed: () => _previewRegQuestionPaper(problems: _lastGeneratedReg!, setLabel: 'Set A'),
                  icon: Icon(Icons.description),
                  label: Text(TrilingualService.instance.getUIText('Worksheet (Set A)')),
                ),
                ElevatedButton.icon(
                  onPressed: () => _previewRegAnswerKey(problems: _lastGeneratedReg!, setLabel: 'Set A'),
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
            if (_setBGeneratedReg != null) ...[
              const SizedBox(height: 12),
              Wrap(
                spacing: 10,
                runSpacing: 10,
                children: [
                  ElevatedButton.icon(
                    onPressed: () => _previewRegQuestionPaper(problems: _setBGeneratedReg!, setLabel: 'Set B'),
                    icon: Icon(Icons.description),
                    label: Text(TrilingualService.instance.getUIText('Worksheet (Set B)')),
                  ),
                  ElevatedButton.icon(
                    onPressed: () => _previewRegAnswerKey(problems: _setBGeneratedReg!, setLabel: 'Set B'),
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
}
