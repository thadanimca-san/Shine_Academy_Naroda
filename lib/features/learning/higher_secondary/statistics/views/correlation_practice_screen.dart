import 'package:flutter/material.dart';

import '../models/board_model.dart';
import '../services/correlation_generator.dart';
import '../services/progress_service.dart';
import '../widgets/solution_reveal_widget.dart';
import '../widgets/xy_pairs_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for Karl Pearson's Coefficient of Correlation: shows
/// paired (X, Y) data, lets the student enter their computed
/// coefficient, checks instantly, then reveals the full step-by-step
/// working.
class CorrelationPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;

  const CorrelationPracticeScreen({super.key, required this.board, required this.schoolClass, this.difficulty = 2});

  @override
  State<CorrelationPracticeScreen> createState() => _CorrelationPracticeScreenState();
}

class _CorrelationPracticeScreenState extends State<CorrelationPracticeScreen> {
  late GeneratedCorrelationProblem _problem;
  final _answerController = TextEditingController();
  bool? _isCorrect;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  @override
  void dispose() {
    _answerController.dispose();
    super.dispose();
  }

  void _generateNewProblem() {
    setState(() {
      _problem = CorrelationGenerator.generate(
        board: widget.board,
        schoolClass: widget.schoolClass,
        difficulty: widget.difficulty,
      );
      _answerController.clear();
      _isCorrect = null;
    });
  }

  void _check() {
    final entered = double.tryParse(_answerController.text);
    final correct = entered != null && (entered - _problem.result.coefficient).abs() < 0.05;
    setState(() => _isCorrect = correct);
    ProgressService.recordAttempt(topicKey: ProgressService.topicCorrelation, wasCorrect: correct);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Correlation — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(TrilingualService.instance.getUIText("Calculate Karl Pearson's Coefficient of Correlation between X and Y:"),
            style: TextStyle(fontSize: 15),
          ),
          const SizedBox(height: 10),
          XyPairsWidget(pairs: _problem.pairs),
          const SizedBox(height: 16),
          Row(
            children: [
              Expanded(
                child: TextField(
                  controller: _answerController,
                  enabled: _isCorrect == null,
                  keyboardType: const TextInputType.numberWithOptions(decimal: true, signed: true),
                  decoration: const InputDecoration(labelText: 'r (between -1 and +1)', border: OutlineInputBorder()),
                ),
              ),
              const SizedBox(width: 10),
              ElevatedButton(onPressed: _isCorrect == null ? _check : null, child: Text(TrilingualService.instance.getUIText('Check'))),
            ],
          ),
          if (_isCorrect != null)
            Padding(
              padding: const EdgeInsets.only(top: 8),
              child: Text(
                _isCorrect!
                    ? 'Correct!'
                    : 'Not quite — expected r ≈ ${_problem.result.coefficient.toStringAsFixed(3)}',
                style: TextStyle(color: _isCorrect! ? Colors.green.shade800 : Colors.red.shade800, fontWeight: FontWeight.bold),
              ),
            ),
          const SizedBox(height: 16),
          SolutionRevealWidget(
            title: "Karl Pearson's Coefficient of Correlation",
            steps: _problem.result.steps,
            finalAnswer: '${_problem.result.coefficient.toStringAsFixed(3)} — ${_problem.result.interpretation}',
          ),
        ],
      ),
    );
  }
}
