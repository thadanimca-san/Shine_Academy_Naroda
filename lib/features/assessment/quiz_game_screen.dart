import 'dart:math';

import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:go_router/go_router.dart';

import '../../core/engine/assessment_engine.dart';
import '../../core/engine/block_registry.dart';
import '../../core/engine/content_repository.dart';
import '../../core/services/activation_service.dart';
import '../../core/services/trilingual_service.dart';
import '../../foundation/theme/app_colors.dart';
import '../../foundation/theme/app_typography.dart';
import '../../shared/widgets/activation_dialog.dart';
import '../learning/learning_engine/widgets/game_quiz_card.dart';
import 'widgets/paper_question_tile.dart';

/// Practice as a game: rounds of objective questions with instant
/// explanations, a streak counter and XP. Exam Mode stays available for
/// timed board-style practice.
class QuizGameScreen extends StatefulWidget {
  final String moduleId;
  const QuizGameScreen({super.key, required this.moduleId});

  @override
  State<QuizGameScreen> createState() => _QuizGameScreenState();
}

class _QuizGameScreenState extends State<QuizGameScreen> {
  static const int roundSize = 10;

  final _random = Random();
  List<AssessmentQuestion> _pool = [];
  List<AssessmentQuestion> _round = [];
  final Set<int> _playedPoolIndexes = {};

  bool _isLoading = true;
  String? _error;

  int _current = 0;
  bool _currentAnswered = false;
  int _streak = 0;
  int _bestStreak = 0;
  int _correct = 0;
  int _xp = 0;

  @override
  void initState() {
    super.initState();
    _load();
  }

  Future<void> _load() async {
    try {
      final bank = await ContentRepository.instance.loadQuestions(widget.moduleId);
      final questions = bank != null
          ? bank
              .where((q) => AssessmentQuestion.objectiveBankTypes.contains(q['type']))
              .map((q) => AssessmentQuestion.fromBankQuestion(q, widget.moduleId))
              .toList()
          : await AssessmentEngine.instance.extractQuestionsForModule(widget.moduleId, ['quiz', 'true_false']);
      _pool = questions
          .where((q) => q.type == 'quiz' && q.options.length >= 2 && q.correctIndexOrAnswer is int)
          .toList();
      if (_pool.isEmpty) throw Exception('No game questions for ${widget.moduleId}');
      _startRound();
      setState(() => _isLoading = false);
    } catch (e) {
      debugPrint('QuizGameScreen: $e');
      setState(() {
        _isLoading = false;
        _error = TrilingualService.instance.getUIText('No quiz questions are ready for this chapter yet.');
      });
    }
  }

  /// Picks questions not played yet in this session; starts over once all are used.
  void _startRound() {
    var unplayed = [for (var i = 0; i < _pool.length; i++) if (!_playedPoolIndexes.contains(i)) i];
    if (unplayed.isEmpty) {
      _playedPoolIndexes.clear();
      unplayed = List.generate(_pool.length, (i) => i);
    }
    unplayed.shuffle(_random);
    final picked = unplayed.take(roundSize).toList();
    _playedPoolIndexes.addAll(picked);
    _round = picked.map((i) => _pool[i]).toList();
    _current = 0;
    _currentAnswered = false;
    _streak = 0;
    _bestStreak = 0;
    _correct = 0;
    _xp = 0;
  }

  void _onAnswered(QuizAnswerResult result) {
    setState(() {
      _currentAnswered = true;
      _xp += result.xpEarned;
      if (result.correct) _correct++;
      _streak = result.correct && result.attempts == 1 ? _streak + 1 : 0;
      _bestStreak = max(_bestStreak, _streak);
    });
  }

  void _next() => setState(() {
        _current++;
        _currentAnswered = false;
      });

  bool get _isSkillupLocked {
    if ((appFlavor ?? 'default') != 'skillup') return false;
    if (ActivationService.isActivated) return false;
    final match = RegExp(r'govindsir_english_ch(\d+)').firstMatch(widget.moduleId);
    if (match != null) {
      final num = int.tryParse(match.group(1)!) ?? 1;
      return num > 2;
    }
    return false;
  }

  @override
  Widget build(BuildContext context) {
    if (_isSkillupLocked) {
      final scale = AppTypography.scaleFactor(context);
      return Scaffold(
        appBar: AppBar(title: Text(TrilingualService.instance.getUIText('🔒 Premium Quiz'))),
        body: Center(
          child: Padding(
            padding: EdgeInsets.all(24.0 * scale),
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Icon(Icons.lock_outline, size: 64 * scale, color: const Color(0xFFFF6F00)),
                SizedBox(height: 16 * scale),
                Text(
                  TrilingualService.instance.getUIText('This quiz requires activation.'),
                  style: AppTypography.h3(context, fontWeight: FontWeight.bold),
                  textAlign: TextAlign.center,
                ),
                SizedBox(height: 8 * scale),
                Text(
                  TrilingualService.instance.getUIText('Chapters 1 and 2 quizzes are fully free. Activate to play all chapter quizzes.'),
                  style: AppTypography.bodySmall(context),
                  textAlign: TextAlign.center,
                ),
                SizedBox(height: 24 * scale),
                ElevatedButton.icon(
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppColors.primary,
                    foregroundColor: Colors.white,
                    padding: EdgeInsets.symmetric(horizontal: 24 * scale, vertical: 12 * scale),
                  ),
                  onPressed: () => ActivationDialog.show(context, onActivated: () => setState(() {})),
                  icon: const Icon(Icons.key, color: Colors.white),
                  label: Text(TrilingualService.instance.getUIText('Enter Activation Code')),
                ),
              ],
            ),
          ),
        ),
      );
    }

    final ui = TrilingualService.instance.getUIText;
    return Scaffold(
      appBar: AppBar(
        title: Text(ui('Quiz Game')),
        actions: [
          Center(
            child: Padding(
              padding: const EdgeInsets.only(right: 16),
              child: Text('⭐ $_xp XP', style: AppTypography.body(context, color: Colors.amber.shade800, fontWeight: FontWeight.bold)),
            ),
          ),
        ],
      ),
      body: _isLoading
          ? const Center(child: CircularProgressIndicator())
          : _error != null
              ? Center(child: Padding(padding: const EdgeInsets.all(24), child: Text(_error!, textAlign: TextAlign.center)))
              : _current >= _round.length
                  ? _buildScoreCard(context)
                  : _buildQuestion(context),
    );
  }

  Widget _buildQuestion(BuildContext context) {
    final ui = TrilingualService.instance.getUIText;
    final q = _round[_current];
    final isLast = _current == _round.length - 1;
    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        Row(
          children: [
            Text('${ui('Question')} ${_current + 1} / ${_round.length}',
                style: AppTypography.bodySmall(context, color: Colors.grey.shade700, fontWeight: FontWeight.bold)),
            const Spacer(),
            if (_streak > 0) Text('🔥 $_streak', style: AppTypography.body(context, color: Colors.deepOrange, fontWeight: FontWeight.bold)),
          ],
        ),
        const SizedBox(height: 8),
        ClipRRect(
          borderRadius: BorderRadius.circular(8),
          child: LinearProgressIndicator(value: (_current + (_currentAnswered ? 1 : 0)) / _round.length, minHeight: 8),
        ),
        const SizedBox(height: 8),
        GameQuizCard(
          key: ValueKey('${q.question}-$_current'),
          question: q.localizedQuestion,
          options: q.localizedOptions,
          correctIndex: q.correctIndexOrAnswer as int,
          explanation: q.localizedExplanation,
          optionFeedback: q.localizedOptionFeedback,
          figure: q.figure == null ? null : BlockRegistry.instance.build(q.figure!),
          answerStreak: _streak,
          onAnswered: _onAnswered,
        ),
        if (_currentAnswered)
          Padding(
            padding: const EdgeInsets.only(top: 8),
            child: FilledButton.icon(
              onPressed: _next,
              icon: Icon(isLast ? Icons.flag : Icons.arrow_forward),
              label: Text(isLast ? ui('See my score') : ui('Next question')),
            ),
          ),
      ],
    );
  }

  Widget _buildScoreCard(BuildContext context) {
    final ui = TrilingualService.instance.getUIText;
    final total = _round.length;
    final percent = total == 0 ? 0 : (_correct * 100 / total).round();
    final stars = percent >= 90 ? 3 : percent >= 60 ? 2 : percent >= 30 ? 1 : 0;
    final message = switch (stars) {
      3 => ui('Outstanding! You are ready for the board exam on this topic.'),
      2 => ui('Great work! A little more practice and you will master it.'),
      1 => ui('Good effort! Read the lesson once more and play again: you will improve.'),
      _ => ui('Every expert was once a beginner. Revise the lesson and try again!'),
    };

    return ListView(
      padding: const EdgeInsets.all(24),
      children: [
        const SizedBox(height: 12),
        Center(child: Text('⭐' * stars + '☆' * (3 - stars), style: AppTypography.h1(context, color: Colors.amber.shade700))),
        const SizedBox(height: 12),
        Center(child: Text('$_correct / $total ${ui('correct')}', style: AppTypography.h2(context, color: AppColors.textPrimary))),
        const SizedBox(height: 8),
        Center(
          child: Text('+$_xp XP   •   🔥 ${ui('Best streak')}: $_bestStreak',
              style: AppTypography.body(context, color: Colors.amber.shade900, fontWeight: FontWeight.bold)),
        ),
        const SizedBox(height: 16),
        Text(message, textAlign: TextAlign.center, style: AppTypography.body(context, color: AppColors.textPrimary)),
        const SizedBox(height: 24),
        FilledButton.icon(
          onPressed: () => setState(_startRound),
          icon: const Icon(Icons.replay),
          label: Text(ui('Play another round')),
        ),
        const SizedBox(height: 8),
        OutlinedButton.icon(
          onPressed: () => context.pushReplacement('/assessment/engine/${widget.moduleId}'),
          icon: const Icon(Icons.timer),
          label: Text(ui('Try Exam Mode (timed)')),
        ),
      ],
    );
  }
}
