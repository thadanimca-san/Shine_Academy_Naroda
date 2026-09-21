import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../models/rectification_model.dart';
import '../models/solution_model.dart';
import '../services/localization_service.dart';
import '../services/progress_service.dart';
import '../services/rectification_generator.dart';
import '../widgets/journal_attempt_widget.dart';
import '../widgets/solution_reveal_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for Rectification of Errors: shows the error as it
/// would appear in an exam question, lets the student attempt the
/// rectifying journal entry, and explains whether Suspense A/c was
/// needed (one-sided error) or not (two-sided error).
class RectificationPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;
  final Medium medium;

  const RectificationPracticeScreen({
    super.key,
    required this.board,
    required this.schoolClass,
    this.difficulty = 3,
    this.medium = Medium.english,
  });

  @override
  State<RectificationPracticeScreen> createState() => _RectificationPracticeScreenState();
}

class _RectificationPracticeScreenState extends State<RectificationPracticeScreen> {
  late GeneratedRectificationProblem _problem;
  int _correctCount = 0;
  int _attemptedCount = 0;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  void _generateNewProblem() {
    setState(() {
      _problem = RectificationGenerator.generate(
        board: widget.board,
        schoolClass: widget.schoolClass,
        difficulty: widget.difficulty,
      );
      _correctCount = 0;
      _attemptedCount = 0;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Rectification of Errors — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(
            LocalizationService.translatePhrase(
                'The following errors were found in the books. Pass the rectifying journal entry for each '
                '(use the Suspense A/c where the error affects only one side of the trial balance):',
                widget.medium),
            style: TextStyle(fontSize: 15),
          ),
          const SizedBox(height: 8),
          Text('Score: $_correctCount / $_attemptedCount', style: TextStyle(color: Colors.grey)),
          const SizedBox(height: 8),
          for (final c in _problem.cases) ...[
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 4),
              child: Text(LocalizationService.translatePhrase(c.errorDescription, widget.medium),
                  style: TextStyle(fontStyle: FontStyle.italic)),
            ),
            JournalAttemptWidget(
              key: ValueKey('${_problem.id}-${c.errorDescription}'),
              correctEntry: c.rectifyingEntry,
              lineCount: c.rectifyingEntry.lines.length,
              medium: widget.medium,
              onSubmit: (correct) {
                setState(() {
                  _attemptedCount++;
                  if (correct) _correctCount++;
                });
                ProgressService.recordAttempt(topicKey: ProgressService.topicRectification, wasCorrect: correct);
              },
            ),
            _RectificationExplainTrigger(
              key: ValueKey('${_problem.id}-explain-${c.errorDescription}'),
              rectificationCase: c,
              medium: widget.medium,
            ),
          ],
        ],
      ),
    );
  }
}

class _RectificationExplainTrigger extends StatefulWidget {
  final RectificationCase rectificationCase;
  final Medium medium;

  const _RectificationExplainTrigger({super.key, required this.rectificationCase, this.medium = Medium.english});

  @override
  State<_RectificationExplainTrigger> createState() => _RectificationExplainTriggerState();
}

class _RectificationExplainTriggerState extends State<_RectificationExplainTrigger> {
  bool _open = false;

  @override
  Widget build(BuildContext context) {
    final c = widget.rectificationCase;
    final isOneSided = c.effect == ErrorEffect.oneSided;
    return Padding(
      padding: const EdgeInsets.only(left: 8, bottom: 16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TextButton.icon(
            onPressed: () => setState(() => _open = !_open),
            icon: Icon(_open ? Icons.visibility_off : Icons.lightbulb_outline),
            label: Text(_open
                ? LocalizationService.t('Hide Explanation', widget.medium)
                : LocalizationService.t('Show Explanation', widget.medium)),
          ),
          if (_open)
            SolutionRevealWidget(
              medium: widget.medium,
              steps: [
                SolutionStep(
                  title: isOneSided ? 'One-Sided Error' : 'Two-Sided Error',
                  reasoning: isOneSided
                      ? 'This error affects only one side of the trial balance, so the difference is routed through Suspense A/c.'
                      : 'This error affects both sides equally, so the rectifying entry balances directly without Suspense A/c.',
                ),
              ],
            ),
        ],
      ),
    );
  }
}
