import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../services/depreciation_generator.dart';
import '../services/depreciation_solver.dart';
import '../services/localization_service.dart';
import '../services/progress_service.dart';
import '../widgets/depreciation_schedule_widget.dart';
import '../widgets/solution_reveal_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for Depreciation (SLM & WDV): shows asset details and
/// lets the student enter their computed depreciation figure for each
/// year, checked instantly against the solver's schedule.
class DepreciationPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;
  final Medium medium;

  const DepreciationPracticeScreen({
    super.key,
    required this.board,
    required this.schoolClass,
    this.difficulty = 2,
    this.medium = Medium.english,
  });

  @override
  State<DepreciationPracticeScreen> createState() => _DepreciationPracticeScreenState();
}

class _DepreciationPracticeScreenState extends State<DepreciationPracticeScreen> {
  late GeneratedDepreciationProblem _problem;
  List<TextEditingController> _controllers = [];
  List<bool?> _correctness = [];
  bool _checked = false;
  bool _revealed = false;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  @override
  void dispose() {
    for (final c in _controllers) {
      c.dispose();
    }
    super.dispose();
  }

  void _generateNewProblem() {
    for (final c in _controllers) {
      c.dispose();
    }
    setState(() {
      _problem = DepreciationGenerator.generate(
        board: widget.board,
        schoolClass: widget.schoolClass,
        difficulty: widget.difficulty,
      );
      _controllers = List.generate(_problem.schedule.rows.length, (_) => TextEditingController());
      _correctness = List.filled(_problem.schedule.rows.length, null);
      _checked = false;
      _revealed = false;
    });
  }

  void _check() {
    setState(() {
      _checked = true;
      _correctness = List.generate(_problem.schedule.rows.length, (i) {
        final entered = double.tryParse(_controllers[i].text);
        final correct = _problem.schedule.rows[i].depreciationAmount;
        return entered != null && (entered - correct).abs() < 0.5;
      });
    });
    for (final wasCorrect in _correctness) {
      ProgressService.recordAttempt(topicKey: ProgressService.topicDepreciation, wasCorrect: wasCorrect ?? false);
    }
  }

  @override
  Widget build(BuildContext context) {
    final schedule = _problem.schedule;
    final methodLabel = LocalizationService.t(
        schedule.method.toString().contains('straightLine') ? 'Straight Line Method (SLM)' : 'Written Down Value Method (WDV)',
        widget.medium);

    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Depreciation — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(
            'A ${schedule.assetName} was purchased for ₹${schedule.originalCost.toStringAsFixed(0)}. '
            '${LocalizationService.t('Calculate depreciation for', widget.medium)} ${schedule.years} '
            '${LocalizationService.t('years under the', widget.medium)} $methodLabel @ ${schedule.ratePercent}% p.a.',
            style: TextStyle(fontSize: 15),
          ),
          const SizedBox(height: 12),
          for (var i = 0; i < schedule.rows.length; i++) _buildYearRow(i, schedule.rows[i].openingBalance),
          const SizedBox(height: 12),
          if (!_checked)
            ElevatedButton(onPressed: _check, child: Text(LocalizationService.t('Check My Answers', widget.medium)))
          else
            Text(
              '${_correctness.where((c) => c == true).length} / ${_correctness.length} correct',
              style: TextStyle(fontWeight: FontWeight.bold),
            ),
          const SizedBox(height: 12),
          TextButton.icon(
            onPressed: () => setState(() => _revealed = !_revealed),
            icon: Icon(_revealed ? Icons.visibility_off : Icons.lightbulb_outline),
            label: Text(_revealed
                ? LocalizationService.t('Hide Full Solution', widget.medium)
                : LocalizationService.t('Show Full Solution', widget.medium)),
          ),
          if (_revealed) ...[
            DepreciationScheduleWidget(schedule: schedule, medium: widget.medium),
            for (var i = 0; i < schedule.rows.length; i++)
              SolutionRevealWidget(
                key: ValueKey('${_problem.id}-year-$i'),
                steps: DepreciationSolver.explainYear(schedule, i),
                medium: widget.medium,
              ),
          ],
        ],
      ),
    );
  }

  Widget _buildYearRow(int i, double opening) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        children: [
          Expanded(flex: 2, child: Text('${LocalizationService.t('Year', widget.medium)} ${i + 1} (${LocalizationService.t('Opening', widget.medium)} ₹${opening.toStringAsFixed(0)}):')),
          Expanded(
            flex: 2,
            child: TextField(
              controller: _controllers[i],
              enabled: !_checked,
              keyboardType: TextInputType.number,
              decoration: InputDecoration(labelText: '${LocalizationService.t('Depreciation', widget.medium)} ₹', isDense: true, border: const OutlineInputBorder()),
            ),
          ),
          if (_checked && _correctness[i] != null) ...[
            const SizedBox(width: 8),
            Icon(_correctness[i]! ? Icons.check_circle : Icons.cancel, color: _correctness[i]! ? Colors.green : Colors.red),
          ],
        ],
      ),
    );
  }
}
