import 'package:flutter/material.dart';
import '../models/syllabus.dart';
import '../theme/tokens.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// One tappable topic row. Coming-soon topics stay visible (the student sees
/// the full journey) but are visually quiet and explain themselves on tap.
class TopicTile extends StatelessWidget {
  final Topic topic;
  final Color tint;
  final bool visited;
  final VoidCallback? onOpen;

  const TopicTile({
    super.key,
    required this.topic,
    required this.tint,
    required this.visited,
    this.onOpen,
  });

  @override
  Widget build(BuildContext context) {
    final available = topic.isAvailable;

    return InkWell(
      borderRadius: BorderRadius.circular(Corner.md),
      onTap: available
          ? onOpen
          : () => ScaffoldMessenger.of(context)
            ..hideCurrentSnackBar()
            ..showSnackBar(SnackBar(
              content: Text('“${topic.title}” is on its way — new labs land every update.'),
              duration: const Duration(seconds: 2),
            )),
      child: Padding(
        padding: const EdgeInsets.symmetric(horizontal: Gap.x2, vertical: Gap.x3),
        child: Row(
          children: [
            Container(
              width: 38,
              height: 38,
              decoration: BoxDecoration(
                color: available ? tint.withValues(alpha: 0.12) : Palette.surfaceAlt,
                borderRadius: BorderRadius.circular(Corner.sm + 2),
              ),
              child: Icon(topic.icon, size: 20, color: available ? tint : Palette.textFaint),
            ),
            const SizedBox(width: Gap.x3),
            Expanded(
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Row(
                    children: [
                      Flexible(
                        child: Text(
                          topic.title,
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: Type.bodyStrong.copyWith(
                            fontSize: 14,
                            color: available ? Palette.textStrong : Palette.textMuted,
                          ),
                        ),
                      ),
                      if (topic.highYield) ...[
                        const SizedBox(width: Gap.x2),
                        Container(
                          padding: const EdgeInsets.symmetric(horizontal: 6, vertical: 1.5),
                          decoration: BoxDecoration(
                            color: Palette.accentSoft,
                            borderRadius: BorderRadius.circular(Corner.pill),
                          ),
                          child: Text(TrilingualService.instance.getUIText('HIGH-YIELD'),
                              style: Type.label.copyWith(fontSize: 8.5, color: const Color(0xFF92400E))),
                        ),
                      ],
                    ],
                  ),
                  const SizedBox(height: 2),
                  Text(
                    topic.tagline,
                    maxLines: 1,
                    overflow: TextOverflow.ellipsis,
                    style: Type.caption.copyWith(
                        fontSize: 12, color: available ? Palette.textMuted : Palette.textFaint),
                  ),
                ],
              ),
            ),
            const SizedBox(width: Gap.x2),
            if (!available)
              Container(
                padding: const EdgeInsets.symmetric(horizontal: 8, vertical: 3),
                decoration: BoxDecoration(
                  color: Palette.surfaceAlt,
                  borderRadius: BorderRadius.circular(Corner.pill),
                ),
                child: Text(TrilingualService.instance.getUIText('SOON'), style: Type.label.copyWith(fontSize: 9, color: Palette.textFaint)),
              )
            else if (visited)
              Icon(Icons.check_circle_rounded, size: 18, color: Palette.success)
            else
              Icon(Icons.chevron_right_rounded, size: 20, color: Palette.textFaint),
          ],
        ),
      ),
    );
  }
}
