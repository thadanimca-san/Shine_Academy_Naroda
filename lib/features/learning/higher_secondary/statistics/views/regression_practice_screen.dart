import 'package:flutter/material.dart';

import '../models/board_model.dart';
import '../services/progress_service.dart';
import '../services/regression_generator.dart';
import '../widgets/solution_reveal_widget.dart';
import '../widgets/xy_pairs_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for Regression Analysis: shows paired (X, Y) data,
/// lets the student enter the regression coefficient byx (Y on X),
/// checks instantly, then reveals the full working for both regression
/// lines.
class RegressionPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;

  const RegressionPracticeScreen({super.key, required this.board, required this.schoolClass, this.difficulty = 2});

  @override
  State<RegressionPracticeScreen> createState() => _RegressionPracticeScreenState();
}

class _RegressionPracticeScreenState extends State<RegressionPracticeScreen> {
  late GeneratedRegressionProblem _problem;
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
      _problem = RegressionGenerator.generate(
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
    final correct = entered != null && (entered - _problem.result.yOnX.coefficient).abs() < 0.05;
    setState(() => _isCorrect = correct);
    ProgressService.recordAttempt(topicKey: ProgressService.topicRegression, wasCorrect: correct);
  }

  @override
  Widget build(BuildContext context) {
    final r = _problem.result;
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Regression — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(TrilingualService.instance.getUIText('Find the regression coefficient byx (Regression of Y on X):'), style: TextStyle(fontSize: 15)),
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
                  decoration: const InputDecoration(labelText: 'byx', border: OutlineInputBorder()),
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
                _isCorrect! ? 'Correct!' : 'Not quite — expected byx ≈ ${r.yOnX.coefficient.toStringAsFixed(3)}',
                style: TextStyle(color: _isCorrect! ? Colors.green.shade800 : Colors.red.shade800, fontWeight: FontWeight.bold),
              ),
            ),
          const SizedBox(height: 16),
          SolutionRevealWidget(title: 'Regression of Y on X', steps: r.yOnX.steps, finalAnswer: r.yOnX.equation),
          SolutionRevealWidget(title: 'Regression of X on Y', steps: r.xOnY.steps, finalAnswer: r.xOnY.equation),
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 8),
            child: Text(
              'Implied Coefficient of Correlation: r = √(byx × bxy) = ${r.impliedR.toStringAsFixed(3)}',
              style: TextStyle(fontStyle: FontStyle.italic, color: Colors.grey),
            ),
          ),
        ],
      ),
    );
  }
}
