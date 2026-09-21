import 'package:flutter/material.dart';
import '../../models/lesson.dart';
import '../../theme/tokens.dart';

/// Renders one [ContentBlock] in the lesson's visual language.
class BlockView extends StatelessWidget {
  final ContentBlock block;
  const BlockView({super.key, required this.block});

  @override
  Widget build(BuildContext context) {
    switch (block.kind) {
      case BlockKind.paragraph:
        return _plain();
      case BlockKind.bullets:
        return _bullets();
      case BlockKind.formula:
        return _formula();
      case BlockKind.realLife:
        return _callout('IN REAL LIFE', Icons.public_rounded, Palette.info, Palette.infoSoft);
      case BlockKind.example:
        return _callout('WORKED EXAMPLE', Icons.edit_note_rounded, Palette.primaryDeep, Palette.primarySoft);
      case BlockKind.mistake:
        return _callout('COMMON MISTAKE', Icons.error_outline_rounded, Palette.danger, Palette.dangerSoft);
      case BlockKind.jeeTip:
        return _callout('JEE TIP', Icons.emoji_events_outlined, Palette.jee, const Color(0xFFFFF3EB));
      case BlockKind.neetNote:
        return _callout('NEET NOTE', Icons.medical_services_outlined, Palette.neet, Palette.successSoft);
    }
  }

  Widget _plain() {
    return Padding(
      padding: const EdgeInsets.only(bottom: Gap.x4),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (block.title != null) ...[
            Text(block.title!, style: Type.heading),
            const SizedBox(height: Gap.x2),
          ],
          Text(block.text!, style: Type.body),
        ],
      ),
    );
  }

  Widget _bullets() {
    return Padding(
      padding: const EdgeInsets.only(bottom: Gap.x4),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (block.title != null) ...[
            Text(block.title!, style: Type.heading),
            const SizedBox(height: Gap.x2),
          ],
          for (final item in block.items)
            Padding(
              padding: const EdgeInsets.only(bottom: Gap.x2),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  const Padding(
                    padding: EdgeInsets.only(top: 7),
                    child: Icon(Icons.circle, size: 6, color: Palette.primary),
                  ),
                  const SizedBox(width: Gap.x3),
                  Expanded(child: Text(item, style: Type.body)),
                ],
              ),
            ),
        ],
      ),
    );
  }

  Widget _formula() {
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.only(bottom: Gap.x4),
      padding: const EdgeInsets.all(Gap.x4),
      decoration: BoxDecoration(
        color: Palette.stage,
        borderRadius: BorderRadius.circular(Corner.md),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          if (block.title != null) ...[
            Text(block.title!,
                style: Type.label.copyWith(color: const Color(0xFF9BA3FF), fontSize: 10)),
            const SizedBox(height: Gap.x2),
          ],
          Text(block.text!,
              style: Type.mono.copyWith(color: const Color(0xFF7EF5C1), fontSize: 15)),
        ],
      ),
    );
  }

  Widget _callout(String tag, IconData icon, Color color, Color bg) {
    return Container(
      width: double.infinity,
      margin: const EdgeInsets.only(bottom: Gap.x4),
      padding: const EdgeInsets.all(Gap.x4),
      decoration: BoxDecoration(
        color: bg,
        borderRadius: BorderRadius.circular(Corner.md),
        border: Border.all(color: color.withValues(alpha: 0.25)),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(icon, size: 15, color: color),
              const SizedBox(width: Gap.x2),
              Text(block.title ?? tag, style: Type.label.copyWith(color: color, fontSize: 10.5)),
            ],
          ),
          const SizedBox(height: Gap.x2),
          Text(block.text!, style: Type.body.copyWith(fontSize: 14)),
        ],
      ),
    );
  }
}
