import 'package:flutter/material.dart';

import '../models/board_model.dart';
import '../services/dispersion_generator.dart';
import '../services/progress_service.dart';
import '../widgets/data_series_widget.dart';
import '../widgets/solution_reveal_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for Measures of Dispersion: shows a data series,
/// lets the student enter their computed Range and Standard Deviation
/// (the two most commonly examined measures), checks instantly, then
/// reveals the full step-by-step working for all four measures.
class DispersionPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;

  const DispersionPracticeScreen({super.key, required this.board, required this.schoolClass, this.difficulty = 2});

  @override
  State<DispersionPracticeScreen> createState() => _DispersionPracticeScreenState();
}

class _DispersionPracticeScreenState extends State<DispersionPracticeScreen> {
  late GeneratedDispersionProblem _problem;
  final _rangeController = TextEditingController();
  final _sdController = TextEditingController();
  bool _checked = false;
  bool _revealed = false;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  @override
  void dispose() {
    _rangeController.dispose();
    _sdController.dispose();
    super.dispose();
  }

  void _generateNewProblem() {
    setState(() {
      _problem = DispersionGenerator.generate(
        board: widget.board,
        schoolClass: widget.schoolClass,
        difficulty: widget.difficulty,
      );
      _rangeController.clear();
      _sdController.clear();
      _checked = false;
      _revealed = false;
    });
  }

  bool _close(String text, double correct) {
    final entered = double.tryParse(text);
    return entered != null && (entered - correct).abs() < 0.5;
  }

  void _check() {
    final rangeOk = _close(_rangeController.text, _problem.result.range.range);
    final sdOk = _close(_sdController.text, _problem.result.standardDeviation.standardDeviation);
    setState(() => _checked = true);
    ProgressService.recordAttempt(topicKey: ProgressService.topicDispersion, wasCorrect: rangeOk && sdOk);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Dispersion — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(TrilingualService.instance.getUIText('Find the Range and Standard Deviation of the following data:'), style: TextStyle(fontSize: 15)),
          const SizedBox(height: 10),
          DataSeriesWidget(series: _problem.series),
          const SizedBox(height: 16),
          _answerField('Range', _rangeController),
          _answerField('Standard Deviation', _sdController),
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
            SolutionRevealWidget(title: 'Range', steps: _problem.result.range.steps, finalAnswer: _fmt(_problem.result.range.range)),
            SolutionRevealWidget(
                title: 'Mean Deviation', steps: _problem.result.meanDeviation.steps, finalAnswer: _fmt(_problem.result.meanDeviation.meanDeviation)),
            SolutionRevealWidget(
                title: 'Standard Deviation',
                steps: _problem.result.standardDeviation.steps,
                finalAnswer: _fmt(_problem.result.standardDeviation.standardDeviation)),
            SolutionRevealWidget(
                title: 'Coefficient of Variation',
                steps: _problem.result.coefficientOfVariation.steps,
                finalAnswer: '${_fmt(_problem.result.coefficientOfVariation.coefficientOfVariation)}%'),
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
    final rangeOk = _close(_rangeController.text, _problem.result.range.range);
    final sdOk = _close(_sdController.text, _problem.result.standardDeviation.standardDeviation);
    return Column(
      children: [
        _feedbackRow('Range', rangeOk),
        _feedbackRow('Standard Deviation', sdOk),
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
