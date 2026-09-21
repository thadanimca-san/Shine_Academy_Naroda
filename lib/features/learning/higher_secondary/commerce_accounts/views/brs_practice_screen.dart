import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../services/brs_generator.dart';
import '../services/brs_solver.dart';
import '../services/localization_service.dart';
import '../services/progress_service.dart';
import '../widgets/solution_reveal_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for Bank Reconciliation Statement: shows the Cash
/// Book balance and reconciling items, lets the student compute the Pass
/// Book balance, then checks it and reveals the full step-by-step
/// statement.
class BrsPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;
  final Medium medium;

  const BrsPracticeScreen({
    super.key,
    required this.board,
    required this.schoolClass,
    this.difficulty = 3,
    this.medium = Medium.english,
  });

  @override
  State<BrsPracticeScreen> createState() => _BrsPracticeScreenState();
}

class _BrsPracticeScreenState extends State<BrsPracticeScreen> {
  late GeneratedBrsProblem _problem;
  final _answerController = TextEditingController();
  bool? _isCorrect;
  bool _revealed = false;

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
      _problem = BrsGenerator.generate(board: widget.board, schoolClass: widget.schoolClass, difficulty: widget.difficulty);
      _answerController.clear();
      _isCorrect = null;
      _revealed = false;
    });
  }

  void _check() {
    final entered = double.tryParse(_answerController.text);
    final correct = entered != null && (entered - _problem.passBookBalance).abs() < 0.5;
    setState(() {
      _isCorrect = correct;
    });
    ProgressService.recordAttempt(topicKey: ProgressService.topicBrs, wasCorrect: correct);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Bank Reconciliation — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text('${LocalizationService.t('Balance as per Cash Book', widget.medium)}: ₹${_problem.cashBookBalance.toStringAsFixed(0)}',
              style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15)),
          const SizedBox(height: 8),
          Text(LocalizationService.translatePhrase(
              'The following differences were found. Prepare a Bank Reconciliation Statement and find the Balance as per Pass Book:',
              widget.medium)),
          const SizedBox(height: 8),
          for (final item in _problem.items)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 2),
              child: Text('• ${LocalizationService.translatePhrase(item.description, widget.medium)}'),
            ),
          const SizedBox(height: 16),
          Row(
            children: [
              Expanded(
                child: TextField(
                  controller: _answerController,
                  enabled: _isCorrect == null,
                  keyboardType: TextInputType.number,
                  decoration: InputDecoration(
                      labelText: '${LocalizationService.t('Balance as per Pass Book', widget.medium)} ₹',
                      border: const OutlineInputBorder()),
                ),
              ),
              const SizedBox(width: 10),
              ElevatedButton(
                  onPressed: _isCorrect == null ? _check : null,
                  child: Text(LocalizationService.t('Check', widget.medium))),
            ],
          ),
          if (_isCorrect != null)
            Padding(
              padding: const EdgeInsets.only(top: 8),
              child: Text(
                _isCorrect!
                    ? '${LocalizationService.t('Correct', widget.medium)}!'
                    : '${LocalizationService.t('Not quite', widget.medium)} — expected ₹${_problem.passBookBalance.toStringAsFixed(0)}',
                style: TextStyle(color: _isCorrect! ? Colors.green.shade800 : Colors.red.shade800, fontWeight: FontWeight.bold),
              ),
            ),
          const SizedBox(height: 12),
          TextButton.icon(
            onPressed: () => setState(() => _revealed = !_revealed),
            icon: Icon(_revealed ? Icons.visibility_off : Icons.lightbulb_outline),
            label: Text(_revealed
                ? LocalizationService.t('Hide Full Solution', widget.medium)
                : LocalizationService.t('Show Full Solution', widget.medium)),
          ),
          if (_revealed)
            SolutionRevealWidget(
              steps: BrsSolver.explainStartingFromCashBook(_problem.cashBookBalance, _problem.items),
              medium: widget.medium,
            ),
        ],
      ),
    );
  }
}
