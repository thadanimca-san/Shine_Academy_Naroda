import 'package:flutter/material.dart';
import '../models/syllabus.dart';
import '../services/progress_service.dart';
import '../theme/tokens.dart';
import 'progress_ring.dart';
import 'soft_card.dart';
import 'topic_tile.dart';

/// Expandable chapter card: header shows identity + progress, body lists
/// every topic so students can learn in any order they like.
class ChapterCard extends StatefulWidget {
  final Chapter chapter;
  final void Function(Topic topic) onOpenTopic;
  final bool initiallyExpanded;

  const ChapterCard({
    super.key,
    required this.chapter,
    required this.onOpenTopic,
    this.initiallyExpanded = false,
  });

  @override
  State<ChapterCard> createState() => _ChapterCardState();
}

class _ChapterCardState extends State<ChapterCard> {
  late bool _expanded = widget.initiallyExpanded;

  @override
  Widget build(BuildContext context) {
    final c = widget.chapter;
    final progress = ProgressService.instance;
    final visited = progress.visitedInChapter(c.topics.map((t) => t.id));
    final ratio = c.topics.isEmpty ? 0.0 : visited / c.topics.length;

    return SoftCard(
      padding: EdgeInsets.zero,
      onTap: () => setState(() => _expanded = !_expanded),
      child: Column(
        children: [
          Padding(
            padding: const EdgeInsets.all(Gap.x4),
            child: Row(
              children: [
                Container(
                  width: 44,
                  height: 44,
                  decoration: BoxDecoration(
                    gradient: LinearGradient(
                      begin: Alignment.topLeft,
                      end: Alignment.bottomRight,
                      colors: [c.tint, c.tint.withValues(alpha: 0.72)],
                    ),
                    borderRadius: BorderRadius.circular(Corner.md),
                  ),
                  child: Icon(c.icon, color: Colors.white, size: 22),
                ),
                const SizedBox(width: Gap.x3),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(c.title, style: Type.heading),
                      const SizedBox(height: 2),
                      Text(
                        visited > 0
                            ? '$visited of ${c.topics.length} topics explored'
                            : '${c.topics.length} topics · ${c.availableCount} labs ready',
                        style: Type.caption,
                      ),
                    ],
                  ),
                ),
                const SizedBox(width: Gap.x2),
                ProgressRing(
                  progress: ratio,
                  size: 38,
                  color: c.tint,
                  center: ratio >= 1
                      ? Icon(Icons.check_rounded, size: 16, color: c.tint)
                      : AnimatedRotation(
                          turns: _expanded ? 0.5 : 0,
                          duration: Motion.base,
                          curve: Motion.ease,
                          child: Icon(Icons.keyboard_arrow_down_rounded,
                              size: 18, color: Palette.textMuted),
                        ),
                ),
              ],
            ),
          ),
          AnimatedSize(
            duration: Motion.base,
            curve: Motion.ease,
            alignment: Alignment.topCenter,
            child: _expanded
                ? Column(
                    children: [
                      const Divider(height: 1),
                      Padding(
                        padding: const EdgeInsets.fromLTRB(Gap.x2, Gap.x1, Gap.x2, Gap.x2),
                        child: Column(
                          children: [
                            for (final t in c.topics)
                              TopicTile(
                                topic: t,
                                tint: c.tint,
                                visited: progress.isVisited(t.id),
                                onOpen: () => widget.onOpenTopic(t),
                              ),
                          ],
                        ),
                      ),
                    ],
                  )
                : const SizedBox(width: double.infinity),
          ),
        ],
      ),
    );
  }
}
