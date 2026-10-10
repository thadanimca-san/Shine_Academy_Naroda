import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';

import '../../../../core/engine/block_registry.dart';
import '../../../../core/services/gamification_service.dart';
import '../../../../core/services/trilingual_service.dart';
import '../../../../foundation/theme/app_colors.dart';
import '../../../../foundation/theme/app_typography.dart';
import '../../../common/widgets/tts_interactive_text.dart';
import '../../../common/widgets/xp_popup.dart';

/// How a student did on one game question.
class QuizAnswerResult {
  final bool correct;
  final int attempts;
  final int xpEarned;
  const QuizAnswerResult({required this.correct, required this.attempts, required this.xpEarned});
}

/// A multiple-choice question played as a game: instant feedback, an
/// explanation for the exact option chosen, one retry, and XP.
///
/// The explanation for each option is what makes this teach rather than just
/// mark: a student who picks the LCM instead of the HCF is told precisely that.
class GameQuizCard extends StatefulWidget {
  final String question;
  final List<String> options;
  final int correctIndex;
  final String? explanation;

  /// One entry per option: why that option is right or wrong.
  final List<String>? optionFeedback;
  final Widget? figure;

  /// Correct answers in a row so far (from a quiz session), for bonus XP.
  final int answerStreak;
  final bool awardXp;

  /// When set, XP for this question is given only once per app session, so
  /// scrolling a lesson up and down cannot farm points.
  final String? xpOncePerSessionKey;
  final ValueChanged<QuizAnswerResult>? onAnswered;

  const GameQuizCard({
    super.key,
    required this.question,
    required this.options,
    required this.correctIndex,
    this.explanation,
    this.optionFeedback,
    this.figure,
    this.answerStreak = 0,
    this.awardXp = true,
    this.xpOncePerSessionKey,
    this.onAnswered,
  });

  @override
  State<GameQuizCard> createState() => _GameQuizCardState();
}

class _GameQuizCardState extends State<GameQuizCard> with SingleTickerProviderStateMixin {
  static final Set<String> _xpAwardedKeys = {};

  final List<int> _wrongPicks = [];
  bool _isFinished = false;
  bool _isCorrect = false;
  int _xpEarned = 0;
  int? _shakingIndex;

  late final AnimationController _shake =
      AnimationController(vsync: this, duration: const Duration(milliseconds: 450));

  /// Two options (true/false) get no retry: the second try would be a giveaway.
  int get _maxAttempts => widget.options.length > 2 ? 2 : 1;

  @override
  void dispose() {
    _shake.dispose();
    super.dispose();
  }

  Future<void> _pick(int index, Offset tapPosition) async {
    if (_isFinished || _wrongPicks.contains(index)) return;

    if (index == widget.correctIndex) {
      HapticFeedback.lightImpact();
      final attempt = _wrongPicks.length + 1;
      final bonus = widget.answerStreak >= GamificationService.answerStreakBonusFrom ? GamificationService.answerStreakBonusXp : 0;
      final key = widget.xpOncePerSessionKey;
      final earnsXp = widget.awardXp && (key == null || _xpAwardedKeys.add(key));
      setState(() {
        _isFinished = true;
        _isCorrect = true;
        _xpEarned = earnsXp ? GamificationService.quizAnswerXp(attempt: attempt) + bonus : 0;
      });
      if (earnsXp) {
        XpPopup.show(context, amount: _xpEarned, position: tapPosition);
        try {
          await GamificationService.instance.addQuizAnswerXp(attempt: attempt, answerStreak: widget.answerStreak);
        } catch (e) {
          debugPrint('GameQuizCard: could not save XP: $e');
        }
      }
    } else {
      HapticFeedback.mediumImpact();
      setState(() {
        _wrongPicks.add(index);
        _shakingIndex = index;
        _isFinished = _wrongPicks.length >= _maxAttempts;
      });
      _shake.forward(from: 0);
    }

    if (_isFinished) {
      widget.onAnswered?.call(QuizAnswerResult(correct: _isCorrect, attempts: _wrongPicks.length + (_isCorrect ? 1 : 0), xpEarned: _xpEarned));
    }
  }

  String? _feedbackFor(int index) {
    final feedback = widget.optionFeedback;
    if (feedback == null || index >= feedback.length || feedback[index].trim().isEmpty) return null;
    return feedback[index];
  }

  @override
  Widget build(BuildContext context) {
    final ui = TrilingualService.instance.getUIText;
    final onSurface = Theme.of(context).colorScheme.onSurface;

    return Card(
      margin: const EdgeInsets.symmetric(vertical: 8),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Row(
              children: [
                const Icon(Icons.sports_esports, color: AppColors.primary),
                const SizedBox(width: 8),
                Text(ui('Quiz time!'), style: AppTypography.bodySmall(context, color: AppColors.primary, fontWeight: FontWeight.bold)),
                const Spacer(),
                if (widget.answerStreak >= GamificationService.answerStreakBonusFrom)
                  Text('🔥 ${widget.answerStreak}', style: AppTypography.bodySmall(context, color: Colors.deepOrange, fontWeight: FontWeight.bold)),
              ],
            ),
            const SizedBox(height: 10),
            TtsInteractiveText(text: widget.question, style: AppTypography.body(context, color: onSurface, fontWeight: FontWeight.w600)),
            if (widget.figure != null) Padding(padding: const EdgeInsets.only(top: 8), child: widget.figure),
            const SizedBox(height: 12),
            for (var i = 0; i < widget.options.length; i++) _buildOption(context, i),
            _buildFeedback(context),
          ],
        ),
      ),
    );
  }

  Widget _buildOption(BuildContext context, int index) {
    final isWrongPick = _wrongPicks.contains(index);
    final showAsCorrect = _isFinished && index == widget.correctIndex;
    final background = showAsCorrect
        ? Colors.green.shade50
        : isWrongPick
            ? Colors.red.shade50
            : Theme.of(context).colorScheme.surface;
    final border = showAsCorrect
        ? Colors.green
        : isWrongPick
            ? Colors.red.shade300
            : Colors.grey.shade300;
    final icon = showAsCorrect
        ? const Icon(Icons.check_circle, color: Colors.green)
        : isWrongPick
            ? Icon(Icons.cancel, color: Colors.red.shade400)
            : null;

    final tile = Container(
      margin: const EdgeInsets.only(bottom: 10),
      padding: const EdgeInsets.symmetric(horizontal: 14, vertical: 12),
      decoration: BoxDecoration(
        color: background,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: border, width: showAsCorrect || isWrongPick ? 2 : 1),
      ),
      child: Row(
        children: [
          Text('(${String.fromCharCode(97 + index)})  ',
              style: AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface, fontWeight: FontWeight.bold)),
          Expanded(
            child: TtsInteractiveText(
              text: widget.options[index],
              enableWordTap: false,
              style: AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface),
            ),
          ),
          if (icon != null) icon,
        ],
      ),
    );

    return AnimatedBuilder(
      animation: _shake,
      builder: (context, child) {
        final offset = _shakingIndex == index ? math.sin(_shake.value * math.pi * 6) * 8 * (1 - _shake.value) : 0.0;
        return Transform.translate(offset: Offset(offset, 0), child: child);
      },
      child: Semantics(
        button: true,
        label: 'Option ${String.fromCharCode(97 + index)}',
        child: GestureDetector(
          behavior: HitTestBehavior.opaque,
          onTapUp: (details) => _pick(index, details.globalPosition),
          child: tile,
        ),
      ),
    );
  }

  Widget _buildFeedback(BuildContext context) {
    final ui = TrilingualService.instance.getUIText;
    if (_wrongPicks.isEmpty && !_isFinished) return const SizedBox.shrink();

    final lastWrong = _wrongPicks.isEmpty ? null : _wrongPicks.last;
    final wrongFeedback = lastWrong == null ? null : _feedbackFor(lastWrong);
    final correctFeedback = _feedbackFor(widget.correctIndex) ?? widget.explanation;

    late final String headline;
    late final Color color;
    late final IconData icon;
    if (_isCorrect) {
      headline = _wrongPicks.isEmpty ? ui('Excellent! You got it.') : ui('Well done! You found it on the second try.');
      color = Colors.green.shade700;
      icon = Icons.emoji_events;
    } else if (!_isFinished) {
      headline = ui('Good try! Read why, then pick again.');
      color = Colors.orange.shade800;
      icon = Icons.lightbulb;
    } else {
      headline = ui('No worries: now you know it. Here is why.');
      color = Colors.blue.shade800;
      icon = Icons.school;
    }

    final bodyStyle = AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface);
    return AnimatedContainer(
      duration: const Duration(milliseconds: 250),
      margin: const EdgeInsets.only(top: 6),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(color: color.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(icon, color: color),
              const SizedBox(width: 8),
              Expanded(child: Text(headline, style: AppTypography.body(context, color: color, fontWeight: FontWeight.bold))),
              if (_xpEarned > 0) Text('+$_xpEarned XP', style: AppTypography.body(context, color: Colors.amber.shade800, fontWeight: FontWeight.bold)),
            ],
          ),
          if (wrongFeedback != null && !_isCorrect) ...[
            const SizedBox(height: 8),
            TtsInteractiveText(text: wrongFeedback, style: bodyStyle),
          ],
          if (_isFinished && correctFeedback != null && correctFeedback.isNotEmpty) ...[
            const SizedBox(height: 8),
            if (!_isCorrect)
              Text('${ui('Answer')}: (${String.fromCharCode(97 + widget.correctIndex)})',
                  style: AppTypography.body(context, color: Colors.green.shade800, fontWeight: FontWeight.bold)),
            TtsInteractiveText(text: correctFeedback, style: bodyStyle),
          ],
        ],
      ),
    );
  }
}

/// Learn-screen block wrapper: reads a quiz block (in the chosen language) and
/// shows it as a [GameQuizCard].
class GameQuizBlock extends StatelessWidget {
  final Map<String, dynamic> block;
  const GameQuizBlock({super.key, required this.block});

  /// Blocks with plain-text options and a valid `correct_index` can be played
  /// as a game; older formats keep using QuizWidget.
  static bool canHandle(Map<String, dynamic> block) {
    final options = block['options'];
    final correct = block['correct_index'];
    return options is List && options.length >= 2 && options.every((o) => o is String) &&
        correct is int && correct >= 0 && correct < options.length;
  }

  List<String>? _localizedList(String key) {
    final lang = TrilingualService.instance.activeViewLanguage;
    final localized = block['${key}_$lang'];
    if (lang != 'en' && localized is List && localized.isNotEmpty) return localized.cast<String>();
    return (block[key] as List?)?.cast<String>();
  }

  @override
  Widget build(BuildContext context) {
    final figure = block['figure'];
    return GameQuizCard(
      question: TrilingualService.instance.getLocalizedText(block, 'question'),
      options: _localizedList('options')!,
      correctIndex: block['correct_index'] as int,
      explanation: TrilingualService.instance.getLocalizedText(block, 'explanation'),
      optionFeedback: _localizedList('option_feedback'),
      figure: figure is Map<String, dynamic> ? BlockRegistry.instance.build(figure) : null,
      xpOncePerSessionKey: block['id'] as String?,
    );
  }
}
