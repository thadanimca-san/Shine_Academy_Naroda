import 'package:flutter/material.dart';

import '../models/board_model.dart';
import '../services/central_tendency_generator.dart';
import '../services/progress_service.dart';
import '../widgets/data_series_widget.dart';
import '../widgets/solution_reveal_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for Measures of Central Tendency: shows a data
/// series (individual/discrete/continuous, scaled by difficulty), lets
/// the student enter their computed Mean/Median/Mode, checks instantly,
/// then reveals the full step-by-step working for each measure.
class CentralTendencyPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;

  const CentralTendencyPracticeScreen({super.key, required this.board, required this.schoolClass, this.difficulty = 2});

  @override
  State<CentralTendencyPracticeScreen> createState() => _CentralTendencyPracticeScreenState();
}

class _CentralTendencyPracticeScreenState extends State<CentralTendencyPracticeScreen> {
  late GeneratedCentralTendencyProblem _problem;
  final _meanController = TextEditingController();
  final _medianController = TextEditingController();
  final _modeController = TextEditingController();
  bool _checked = false;
  bool _revealed = false;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  @override
  void dispose() {
    _meanController.dispose();
    _medianController.dispose();
    _modeController.dispose();
    super.dispose();
  }

  void _generateNewProblem() {
    setState(() {
      _problem = CentralTendencyGenerator.generate(
        board: widget.board,
        schoolClass: widget.schoolClass,
        difficulty: widget.difficulty,
      );
      _meanController.clear();
      _medianController.clear();
      _modeController.clear();
      _checked = false;
      _revealed = false;
    });
  }

  bool _close(String text, double? correct) {
    if (correct == null) return true; // no mode -> any/no answer is acceptable to not penalise
    final entered = double.tryParse(text);
    return entered != null && (entered - correct).abs() < 0.5;
  }

  void _check() {
    final meanOk = _close(_meanController.text, _problem.result.mean.mean);
    final medianOk = _close(_medianController.text, _problem.result.median.median);
    final modeOk = _problem.result.mode.mode == null || _close(_modeController.text, _problem.result.mode.mode);
    final allOk = meanOk && medianOk && modeOk;
    setState(() => _checked = true);
    ProgressService.recordAttempt(topicKey: ProgressService.topicCentralTendency, wasCorrect: allOk);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Central Tendency — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(TrilingualService.instance.getUIText('Find the Mean, Median and Mode of the following data:'), style: TextStyle(fontSize: 15)),
          const SizedBox(height: 10),
          DataSeriesWidget(series: _problem.series),
          const SizedBox(height: 16),
          _answerField('Mean', _meanController),
          _answerField('Median', _medianController),
          _answerField('Mode', _modeController),
          const SizedBox(height: 12),
          if (!_checked)
            Center(child: ElevatedButton(onPressed: _check, child: Text(TrilingualService.instance.getUIText('Check My Answers'))))
          else
            _buildFeedback(),
          const SizedBox(height: 16),
          Center(
            child: TextButton.icon(
              onPressed: () => setState(() => _revealed = !_revealed),
              icon: Icon(_revealed ? Icons.visibility_off : Icons.lightbulb_outline),
              label: Text(_revealed ? 'Hide Full Solution' : 'Show Full Solution'),
            ),
          ),
          if (_revealed) ...[
            SolutionRevealWidget(
              title: 'Mean',
              steps: _problem.result.mean.steps,
              finalAnswer: _fmt(_problem.result.mean.mean),
            ),
            SolutionRevealWidget(
              title: 'Median',
              steps: _problem.result.median.steps,
              finalAnswer: _fmt(_problem.result.median.median),
            ),
            SolutionRevealWidget(
              title: 'Mode',
              steps: _problem.result.mode.steps,
              finalAnswer: _problem.result.mode.mode != null ? _fmt(_problem.result.mode.mode!) : 'No mode',
            ),
          ],
        ],
      ),
    );
  }

  Widget _answerField(String label, TextEditingController controller) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: TextField(
        controller: controller,
        enabled: !_checked,
        keyboardType: const TextInputType.numberWithOptions(decimal: true),
        decoration: InputDecoration(labelText: label, border: const OutlineInputBorder(), isDense: true),
      ),
    );
  }

  Widget _buildFeedback() {
    final meanOk = _close(_meanController.text, _problem.result.mean.mean);
    final medianOk = _close(_medianController.text, _problem.result.median.median);
    final modeOk = _problem.result.mode.mode == null || _close(_modeController.text, _problem.result.mode.mode);
    return Column(
      children: [
        _feedbackRow('Mean', meanOk),
        _feedbackRow('Median', medianOk),
        _feedbackRow('Mode', modeOk),
      ],
    );
  }

  Widget _feedbackRow(String label, bool ok) {
    return Row(
      children: [
        Icon(ok ? Icons.check_circle : Icons.cancel, color: ok ? Colors.green : Colors.red, size: 18),
        const SizedBox(width: 6),
        Text('$label ${ok ? "correct" : "check again"}'),
      ],
    );
  }

  String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
