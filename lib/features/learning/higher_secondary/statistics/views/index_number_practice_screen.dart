import 'package:flutter/material.dart';

import '../models/board_model.dart';
import '../services/index_number_generator.dart';
import '../services/progress_service.dart';
import '../widgets/commodity_table_widget.dart';
import '../widgets/solution_reveal_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for Index Numbers: shows a commodity price (and
/// optionally quantity) table, lets the student enter the Simple
/// Aggregative index, checks instantly, then reveals the full working
/// for all applicable methods.
class IndexNumberPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;

  const IndexNumberPracticeScreen({super.key, required this.board, required this.schoolClass, this.difficulty = 2});

  @override
  State<IndexNumberPracticeScreen> createState() => _IndexNumberPracticeScreenState();
}

class _IndexNumberPracticeScreenState extends State<IndexNumberPracticeScreen> {
  late GeneratedIndexNumberProblem _problem;
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
      _problem = IndexNumberGenerator.generate(
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
    final correct = entered != null && (entered - _problem.result.simpleAggregativeIndex).abs() < 0.5;
    setState(() => _isCorrect = correct);
    ProgressService.recordAttempt(topicKey: ProgressService.topicIndexNumbers, wasCorrect: correct);
  }

  @override
  Widget build(BuildContext context) {
    final r = _problem.result;
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Index Numbers — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(TrilingualService.instance.getUIText('Construct the Price Index Number (base year = 100) from the following data:'), style: TextStyle(fontSize: 15)),
          const SizedBox(height: 10),
          CommodityTableWidget(commodities: _problem.commodities, includeQuantities: _problem.includeQuantities),
          const SizedBox(height: 16),
          Row(
            children: [
              Expanded(
                child: TextField(
                  controller: _answerController,
                  enabled: _isCorrect == null,
                  keyboardType: const TextInputType.numberWithOptions(decimal: true),
                  decoration: const InputDecoration(labelText: 'Simple Aggregative Index (P01)', border: OutlineInputBorder()),
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
                _isCorrect! ? 'Correct!' : 'Not quite — expected ${r.simpleAggregativeIndex.toStringAsFixed(2)}',
                style: TextStyle(color: _isCorrect! ? Colors.green.shade800 : Colors.red.shade800, fontWeight: FontWeight.bold),
              ),
            ),
          const SizedBox(height: 16),
          SolutionRevealWidget(
            title: 'Simple Aggregative Method',
            steps: r.simpleAggregativeSteps,
            finalAnswer: r.simpleAggregativeIndex.toStringAsFixed(2),
          ),
          SolutionRevealWidget(
            title: 'Simple Average of Price Relatives',
            steps: r.simpleAverageSteps,
            finalAnswer: r.simpleAveragePriceRelativeIndex.toStringAsFixed(2),
          ),
          if (r.laspeyresIndex != null)
            SolutionRevealWidget(
              title: "Laspeyres' Method",
              steps: r.laspeyresSteps,
              finalAnswer: r.laspeyresIndex!.toStringAsFixed(2),
            ),
          if (r.paascheIndex != null)
            SolutionRevealWidget(
              title: "Paasche's Method",
              steps: r.paascheSteps,
              finalAnswer: r.paascheIndex!.toStringAsFixed(2),
            ),
        ],
      ),
    );
  }
}
