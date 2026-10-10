import 'package:flutter/material.dart';
import 'package:shared_preferences/shared_preferences.dart';

import '../../../../core/services/gamification_service.dart';
import '../../../../core/services/trilingual_service.dart';
import '../../../../foundation/theme/app_typography.dart';

/// Shown at the end of a lesson: celebrates finishing, gives the chapter XP
/// once, and points to the next step.
class ChapterFinishCard extends StatefulWidget {
  final String moduleId;
  final VoidCallback onPlayQuiz;
  final VoidCallback onQuickRevision;

  const ChapterFinishCard({super.key, required this.moduleId, required this.onPlayQuiz, required this.onQuickRevision});

  @override
  State<ChapterFinishCard> createState() => _ChapterFinishCardState();
}

class _ChapterFinishCardState extends State<ChapterFinishCard> {
  bool? _alreadyCompleted;

  String get _key => 'chapter_completed_${widget.moduleId}';

  @override
  void initState() {
    super.initState();
    SharedPreferences.getInstance().then((prefs) {
      if (mounted) setState(() => _alreadyCompleted = prefs.getBool(_key) ?? false);
    });
  }

  Future<void> _complete() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setBool(_key, true);
      await GamificationService.instance.addChapterCompleteXp();
      if (mounted) setState(() => _alreadyCompleted = true);
    } catch (e) {
      debugPrint('ChapterFinishCard: could not save completion: $e');
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(SnackBar(content: Text(TrilingualService.instance.getUIText('Could not save your progress. Please try again.'))));
      }
    }
  }

  @override
  Widget build(BuildContext context) {
    final ui = TrilingualService.instance.getUIText;
    final done = _alreadyCompleted ?? false;
    final streak = GamificationService.instance.streakNotifier.value;
    final ink = Colors.indigo.shade900;

    return Container(
      margin: const EdgeInsets.only(top: 16, bottom: 32),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        gradient: LinearGradient(colors: [Colors.indigo.shade50, Colors.purple.shade50]),
        borderRadius: BorderRadius.circular(20),
      ),
      child: Column(
        children: [
          Text(done ? '🏆' : '🎯', style: AppTypography.h1(context)),
          const SizedBox(height: 8),
          Text(done ? ui('Chapter completed! Proud of you.') : ui('You reached the end of the lesson!'),
              textAlign: TextAlign.center, style: AppTypography.h3(context, color: ink)),
          const SizedBox(height: 8),
          Text(
            done
                ? ui('Keep the knowledge fresh: play the quiz or do a quick revision tomorrow.')
                : ui('Hard work today is success tomorrow. Mark this chapter complete and collect your reward.'),
            textAlign: TextAlign.center,
            style: AppTypography.body(context, color: Colors.indigo.shade700),
          ),
          if (streak > 0) ...[
            const SizedBox(height: 8),
            Text('🔥 $streak ${ui('day learning streak')}',
                style: AppTypography.body(context, color: Colors.deepOrange, fontWeight: FontWeight.bold)),
          ],
          const SizedBox(height: 16),
          if (_alreadyCompleted == false)
            FilledButton.icon(
              onPressed: _complete,
              icon: const Icon(Icons.emoji_events),
              label: Text(ui('Mark complete (+500 XP)')),
            ),
          const SizedBox(height: 8),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            alignment: WrapAlignment.center,
            children: [
              OutlinedButton.icon(onPressed: widget.onPlayQuiz, icon: const Icon(Icons.sports_esports), label: Text(ui('Play Quiz Game'))),
              OutlinedButton.icon(onPressed: widget.onQuickRevision, icon: const Icon(Icons.bolt), label: Text(ui('Quick revision'))),
            ],
          ),
        ],
      ),
    );
  }
}
