import 'package:flutter/material.dart';

import '../../../../../core/engine/local_content_manager.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';
import '../models/practice_question.dart';
import '../models/practice_session.dart';
import '../theme/app_theme.dart';
import '../widgets/admin_edit_button.dart';
import '../widgets/read_aloud_button.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Runs one practice set at a time (10 questions, per the blueprint's "large
/// bank, served in small sets" design). Every question is answered and
/// explained immediately — never a bare score at the end — and finishing a
/// set offers "Practice More" to keep pulling fresh sets from the bank.
class PracticeSessionScreen extends StatefulWidget {
  final PracticeTopic topic;

  const PracticeSessionScreen({super.key, required this.topic});

  @override
  State<PracticeSessionScreen> createState() => _PracticeSessionScreenState();
}

class _PracticeSessionScreenState extends State<PracticeSessionScreen> {
  late final PracticeSession _session;
  late List<PracticeQuestion> _currentSet;
  int _questionIndex = 0;
  int? _selectedOption;
  bool _revealed = false;
  int _correctCount = 0;
  bool _setComplete = false;
  late PracticeTopic _topic;

  @override
  void initState() {
    super.initState();
    _topic = widget.topic;
    _session = PracticeSession(widget.topic);
    _currentSet = _session.nextSet();
    _tryLoadLocalOverride();
    TrilingualService.instance.addListener(_onLangChange);
  }

  void _onLangChange() {
    if (mounted) setState(() {});
  }

  @override
  void dispose() {
    TrilingualService.instance.removeListener(_onLangChange);
    super.dispose();
  }

  String get _jsonPath => 'app_core/english/practice/${_topic.id}.json';

  Future<void> _tryLoadLocalOverride() async {
    try {
      await LocalContentManager.instance.init();
      final data = await LocalContentManager.instance.readLocalJson(_jsonPath);
      if (data != null && mounted && data.containsKey('bank')) {
        setState(() => _topic = PracticeTopic.fromJson(data));
      }
    } catch (e) {
      debugPrint('PracticeSessionScreen: could not load local override: $e');
    }
  }

  void _selectOption(int index) {
    if (_revealed) return;
    setState(() {
      _selectedOption = index;
      _revealed = true;
      if (index == _currentSet[_questionIndex].correctIndex) {
        _correctCount++;
      }
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
      appBar: BrandAppBar(
        title: _topic.title,
        actions: [
          AdminEditButton(
            jsonPath: _jsonPath,
            data: _topic.toJson(),
            onEditorClosed: _tryLoadLocalOverride,
          ),
        ],
      ),
      body: SafeArea(
        child: _setComplete ? _buildSetSummary(context) : _buildQuestion(context),
      ),
    );
  }

  Widget _buildQuestion(BuildContext context) {
    final question = _currentSet[_questionIndex];
    return Padding(
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
              valueColor: const AlwaysStoppedAnimation(AppColors.saffron),
            ),
          ),
          const SizedBox(height: 24),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                TrilingualService.instance.activeViewLanguage == 'hi' && question.promptHi != null
                    ? question.promptHi!
                    : TrilingualService.instance.activeViewLanguage == 'gu' && question.promptGu != null
                        ? question.promptGu!
                        : question.prompt,
                style: TextStyle(fontSize: 19, fontWeight: FontWeight.w700, color: AppColors.ink, height: 1.35),
              ),
              const SizedBox(height: 12),
              ReadAloudButton(
                  text: TrilingualService.instance.activeViewLanguage == 'hi' && question.promptHi != null
                      ? question.promptHi!
                      : TrilingualService.instance.activeViewLanguage == 'gu' && question.promptGu != null
                          ? question.promptGu!
                          : question.prompt,
                  label: 'Listen'),
            ],
          ),
          const SizedBox(height: 20),
          Expanded(
            child: ListView.separated(
              itemCount: question.options.length,
              separatorBuilder: (_, _) => const SizedBox(height: 10),
              itemBuilder: (context, i) => _OptionTile(
                text: TrilingualService.instance.activeViewLanguage == 'hi' && question.optionsHi != null
                    ? question.optionsHi![i]
                    : TrilingualService.instance.activeViewLanguage == 'gu' && question.optionsGu != null
                        ? question.optionsGu![i]
                        : question.options[i],
                state: _optionState(question, i),
                onTap: () => _selectOption(i),
              ),
            ),
          ),
          if (_revealed) ...[
            _ExplanationCard(
              correct: _selectedOption == question.correctIndex,
              explanation: TrilingualService.instance.activeViewLanguage == 'hi' && question.explanationHi != null
                  ? question.explanationHi!
                  : TrilingualService.instance.activeViewLanguage == 'gu' && question.explanationGu != null
                      ? question.explanationGu!
                      : question.explanation,
            ),
            const SizedBox(height: 14),
            SizedBox(
              width: double.infinity,
              child: FilledButton(
                onPressed: _next,
                style: FilledButton.styleFrom(
                  backgroundColor: AppColors.saffron,
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

  _OptionState _optionState(PracticeQuestion question, int index) {
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
                  backgroundColor: AppColors.saffron,
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
        decoration: BoxDecoration(
          color: bg,
          borderRadius: BorderRadius.circular(10),
          border: Border.all(color: border),
        ),
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

class _ExplanationCard extends StatelessWidget {
  final bool correct;
  final String explanation;

  const _ExplanationCard({required this.correct, required this.explanation});

  @override
  Widget build(BuildContext context) {
    final color = correct ? AppColors.success : AppColors.critical;
    return Container(
      margin: const EdgeInsets.only(top: 14),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.08),
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: color.withValues(alpha: 0.4)),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(correct ? Icons.lightbulb : Icons.info_outline, color: color, size: 20),
          const SizedBox(width: 10),
          Expanded(
            child: Text(
              explanation,
              style: TextStyle(color: AppColors.inkSoft, fontSize: 13.5, height: 1.4),
            ),
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
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.12),
        borderRadius: BorderRadius.circular(20),
      ),
      child: Text(label, style: TextStyle(color: color, fontSize: 11, fontWeight: FontWeight.w700)),
    );
  }
}
