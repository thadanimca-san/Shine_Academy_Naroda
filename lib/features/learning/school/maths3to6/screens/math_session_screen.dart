import 'package:flutter/material.dart';

import '../models/math_question.dart';
import '../models/math_session.dart';
import '../theme/app_theme.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Runs one practice set at a time (10 questions). Every question shows a
/// full step-by-step worked solution after answering — not a one-line
/// reason — since a maths mistake needs to be traced through the working,
/// not just told "wrong".
class MathSessionScreen extends StatefulWidget {
  final MathTopic topic;

  const MathSessionScreen({super.key, required this.topic});

  @override
  State<MathSessionScreen> createState() => _MathSessionScreenState();
}

class _MathSessionScreenState extends State<MathSessionScreen> {
  late final MathSession _session;
  late List<MathQuestion> _currentSet;
  int _questionIndex = 0;
  int? _selectedOption;
  bool _revealed = false;
  int _correctCount = 0;
  bool _setComplete = false;

  @override
  void initState() {
    super.initState();
    _session = MathSession(widget.topic);
    _currentSet = _session.nextSet();
  }

  void _selectOption(int index) {
    if (_revealed) return;
    setState(() {
      _selectedOption = index;
      _revealed = true;
      if (index == _currentSet[_questionIndex].correctIndex) _correctCount++;
    });
  }

  void _next() {
    if (_questionIndex + 1 < _currentSet.length) {
      setState(() {
        _questionIndex++;
        _selectedOption = null;
        _revealed = false;
      });
    } else {
      setState(() => _setComplete = true);
    }
  }

  void _startNextSet() {
    setState(() {
      _currentSet = _session.nextSet();
      _questionIndex = 0;
      _selectedOption = null;
      _revealed = false;
      _correctCount = 0;
      _setComplete = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: Text(widget.topic.title)),
      body: SafeArea(
        child: _setComplete ? _buildSetSummary(context) : _buildQuestion(context),
      ),
    );
  }

  Widget _buildQuestion(BuildContext context) {
    final question = _currentSet[_questionIndex];
    return SingleChildScrollView(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Text(
                'Question ${_questionIndex + 1} of ${_currentSet.length}',
                style: TextStyle(color: AppColors.inkFaint, fontSize: 13, fontWeight: FontWeight.w600),
              ),
              const Spacer(),
              _DifficultyBadge(difficulty: question.difficulty),
            ],
          ),
          const SizedBox(height: 6),
          ClipRRect(
            borderRadius: BorderRadius.circular(4),
            child: LinearProgressIndicator(
              value: (_questionIndex + (_revealed ? 1 : 0)) / _currentSet.length,
              minHeight: 6,
              backgroundColor: AppColors.paperRaised,
              valueColor: const AlwaysStoppedAnimation(AppColors.indigo),
            ),
          ),
          const SizedBox(height: 24),
          if (question.emoji != null) ...[
            Center(
              child: Container(
                width: 72,
                height: 72,
                alignment: Alignment.center,
                decoration: BoxDecoration(color: AppColors.indigoTint, borderRadius: BorderRadius.circular(14)),
                child: Text(question.emoji!, style: TextStyle(fontSize: 36)),
              ),
            ),
            const SizedBox(height: 16),
          ],
          Text(
            question.prompt,
            style: TextStyle(fontSize: 19, fontWeight: FontWeight.w700, color: AppColors.ink, height: 1.35),
          ),
          const SizedBox(height: 20),
          ...List.generate(question.options.length, (i) => Padding(
                padding: const EdgeInsets.only(bottom: 10),
                child: _OptionTile(
                  text: question.options[i],
                  state: _optionState(question, i),
                  onTap: () => _selectOption(i),
                ),
              )),
          if (_revealed) ...[
            _SolutionCard(correct: _selectedOption == question.correctIndex, steps: question.solutionSteps),
            const SizedBox(height: 14),
            SizedBox(
              width: double.infinity,
              child: FilledButton(
                onPressed: _next,
                style: FilledButton.styleFrom(
                  backgroundColor: AppColors.indigo,
                  padding: const EdgeInsets.symmetric(vertical: 14),
                ),
                child: Text(_questionIndex + 1 < _currentSet.length ? 'Next question' : 'Finish set'),
              ),
            ),
          ],
        ],
      ),
    );
  }

  _OptionState _optionState(MathQuestion question, int index) {
    if (!_revealed) return _OptionState.neutral;
    if (index == question.correctIndex) return _OptionState.correct;
    if (index == _selectedOption) return _OptionState.incorrect;
    return _OptionState.dimmed;
  }

  Widget _buildSetSummary(BuildContext context) {
    final remaining = _session.remainingInBank;
    final bankSize = _session.bankSize;
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(28),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(TrilingualService.instance.getUIText('🎯'), style: TextStyle(fontSize: 48)),
            const SizedBox(height: 12),
            Text(
              '$_correctCount / ${_currentSet.length} correct',
              style: TextStyle(fontSize: 24, fontWeight: FontWeight.w800, color: AppColors.ink),
            ),
            const SizedBox(height: 8),
            Text(
              remaining > 0
                  ? '$remaining more questions left in this topic\'s bank of $bankSize.'
                  : 'You\'ve been through all $bankSize questions in this bank — the next set reshuffles from the start.',
              textAlign: TextAlign.center,
              style: TextStyle(color: AppColors.inkFaint),
            ),
            const SizedBox(height: 28),
            SizedBox(
              width: double.infinity,
              child: FilledButton(
                onPressed: _startNextSet,
                style: FilledButton.styleFrom(
                  backgroundColor: AppColors.indigo,
                  padding: const EdgeInsets.symmetric(vertical: 14),
                ),
                child: Text(TrilingualService.instance.getUIText('Practice more')),
              ),
            ),
            const SizedBox(height: 10),
            SizedBox(
              width: double.infinity,
              child: OutlinedButton(
                onPressed: () => Navigator.of(context).pop(),
                style: OutlinedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  side: const BorderSide(color: AppColors.rule),
                ),
                child: Text(TrilingualService.instance.getUIText('Back to topics'), style: TextStyle(color: AppColors.inkSoft)),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

enum _OptionState { neutral, correct, incorrect, dimmed }

class _OptionTile extends StatelessWidget {
  final String text;
  final _OptionState state;
  final VoidCallback onTap;

  const _OptionTile({required this.text, required this.state, required this.onTap});

  @override
  Widget build(BuildContext context) {
    Color bg;
    Color border;
    Color fg;
    IconData? icon;

    switch (state) {
      case _OptionState.neutral:
        bg = AppColors.paperRaised;
        border = AppColors.rule;
        fg = AppColors.ink;
        icon = null;
      case _OptionState.correct:
        bg = AppColors.success.withValues(alpha: 0.12);
        border = AppColors.success;
        fg = AppColors.success;
        icon = Icons.check_circle;
      case _OptionState.incorrect:
        bg = AppColors.critical.withValues(alpha: 0.10);
        border = AppColors.critical;
        fg = AppColors.critical;
        icon = Icons.cancel;
      case _OptionState.dimmed:
        bg = AppColors.paperRaised.withValues(alpha: 0.5);
        border = AppColors.rule;
        fg = AppColors.inkFaint;
        icon = null;
    }

    return InkWell(
      borderRadius: BorderRadius.circular(10),
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
        decoration: BoxDecoration(color: bg, borderRadius: BorderRadius.circular(10), border: Border.all(color: border)),
        child: Row(
          children: [
            Expanded(child: Text(text, style: TextStyle(color: fg, fontSize: 15, fontWeight: FontWeight.w600))),
            if (icon != null) Icon(icon, color: fg, size: 20),
          ],
        ),
      ),
    );
  }
}

class _SolutionCard extends StatelessWidget {
  final bool correct;
  final List<SolutionStep> steps;

  const _SolutionCard({required this.correct, required this.steps});

  @override
  Widget build(BuildContext context) {
    final color = correct ? AppColors.success : AppColors.critical;
    return Container(
      margin: const EdgeInsets.only(top: 14),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.06),
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: color.withValues(alpha: 0.35)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(correct ? Icons.check_circle_outline : Icons.info_outline, color: color, size: 18),
              const SizedBox(width: 8),
              Text(
                correct ? 'Correct — here\'s the full working' : 'Not quite — here\'s the full working',
                style: TextStyle(color: color, fontWeight: FontWeight.w700, fontSize: 13),
              ),
            ],
          ),
          const SizedBox(height: 10),
          for (var i = 0; i < steps.length; i++) _StepRow(index: i + 1, step: steps[i]),
        ],
      ),
    );
  }
}

class _StepRow extends StatelessWidget {
  final int index;
  final SolutionStep step;

  const _StepRow({required this.index, required this.step});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: 20,
            height: 20,
            margin: const EdgeInsets.only(top: 1),
            alignment: Alignment.center,
            decoration: BoxDecoration(color: AppColors.indigoTint, shape: BoxShape.circle),
            child: Text('$index', style: TextStyle(fontSize: 10.5, fontWeight: FontWeight.w700, color: AppColors.indigoDeep)),
          ),
          const SizedBox(width: 8),
          if (step.emoji != null) ...[
            Text(step.emoji!, style: TextStyle(fontSize: 16)),
            const SizedBox(width: 6),
          ],
          Expanded(
            child: Text(step.text, style: TextStyle(fontSize: 13.5, color: AppColors.inkSoft, height: 1.4)),
          ),
        ],
      ),
    );
  }
}

class _DifficultyBadge extends StatelessWidget {
  final Difficulty difficulty;

  const _DifficultyBadge({required this.difficulty});

  @override
  Widget build(BuildContext context) {
    final (label, color) = switch (difficulty) {
      Difficulty.easy => ('Easy', AppColors.success),
      Difficulty.medium => ('Medium', AppColors.warning),
      Difficulty.hard => ('Hard', AppColors.critical),
    };
    return Container(
      padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
      decoration: BoxDecoration(color: color.withValues(alpha: 0.12), borderRadius: BorderRadius.circular(20)),
      child: Text(label, style: TextStyle(color: color, fontSize: 11, fontWeight: FontWeight.w700)),
    );
  }
}
