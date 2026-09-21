import 'package:flutter/material.dart';
import '../models/chapter_model.dart';

/// Small, hand-drawn icon shown at the top of each revision note card.
/// Kept as vector art (not image assets) so it stays crisp at any size and
/// matches the rest of the app's illustrated-diagram style. Add a new
/// `case` here whenever a chapter's notes need a new picture; unmatched
/// keys just fall back to a plain bullet-list icon so nothing breaks.
class _NoteIconPainter extends CustomPainter {
  final String iconKey;
  final Color color;

  _NoteIconPainter({required this.iconKey, required this.color});

  @override
  void paint(Canvas canvas, Size size) {
    final w = size.width, h = size.height;
    final fill = Paint()..color = color.withValues(alpha: 0.85);
    final stroke = Paint()
      ..color = color
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.6
      ..strokeCap = StrokeCap.round;
    final faint = Paint()..color = color.withValues(alpha: 0.18);

    switch (iconKey) {
      case 'microscope':
        canvas.drawLine(Offset(w * 0.3, h * 0.85), Offset(w * 0.75, h * 0.85), stroke);
        canvas.drawLine(Offset(w * 0.55, h * 0.85), Offset(w * 0.4, h * 0.3), stroke);
        canvas.drawCircle(Offset(w * 0.4, h * 0.28), w * 0.08, fill);
        canvas.drawLine(Offset(w * 0.4, h * 0.36), Offset(w * 0.58, h * 0.5), stroke);
        canvas.drawCircle(Offset(w * 0.62, h * 0.55), w * 0.1, faint);
        canvas.drawCircle(Offset(w * 0.62, h * 0.55), w * 0.1, stroke);
        break;

      case 'membrane':
        for (int i = 0; i < 5; i++) {
          final cx = w * (0.15 + i * 0.18);
          canvas.drawOval(Rect.fromCenter(center: Offset(cx, h * 0.4), width: w * 0.12, height: h * 0.5), fill);
          canvas.drawOval(Rect.fromCenter(center: Offset(cx, h * 0.7), width: w * 0.12, height: h * 0.5), fill);
        }
        break;

      case 'organelles':
        canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.5, h * 0.5), width: w * 0.85, height: h * 0.75), faint);
        canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.5, h * 0.5), width: w * 0.85, height: h * 0.75), stroke);
        canvas.drawCircle(Offset(w * 0.42, h * 0.45), w * 0.14, fill);
        canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.68, h * 0.32), width: w * 0.2, height: h * 0.12), Paint()..color = color.withValues(alpha: 0.6));
        canvas.drawCircle(Offset(w * 0.62, h * 0.68), w * 0.08, Paint()..color = color.withValues(alpha: 0.5));
        break;

      case 'division':
        canvas.drawCircle(Offset(w * 0.5, h * 0.22), w * 0.13, fill);
        canvas.drawLine(Offset(w * 0.5, h * 0.35), Offset(w * 0.5, h * 0.52), stroke);
        canvas.drawCircle(Offset(w * 0.3, h * 0.75), w * 0.13, fill);
        canvas.drawCircle(Offset(w * 0.7, h * 0.75), w * 0.13, fill);
        canvas.drawLine(Offset(w * 0.5, h * 0.52), Offset(w * 0.3, h * 0.62), stroke);
        canvas.drawLine(Offset(w * 0.5, h * 0.52), Offset(w * 0.7, h * 0.62), stroke);
        break;

      case 'theory':
        canvas.drawRRect(RRect.fromRectAndRadius(Rect.fromLTWH(w * 0.15, h * 0.15, w * 0.7, h * 0.7), const Radius.circular(6)), faint);
        canvas.drawRRect(RRect.fromRectAndRadius(Rect.fromLTWH(w * 0.15, h * 0.15, w * 0.7, h * 0.7), const Radius.circular(6)), stroke);
        for (int i = 0; i < 3; i++) {
          final y = h * (0.32 + i * 0.18);
          canvas.drawLine(Offset(w * 0.28, y), Offset(w * 0.72, y), stroke..strokeWidth = 1.4);
        }
        break;

      case 'plant_growth':
        canvas.drawLine(Offset(w * 0.5, h * 0.9), Offset(w * 0.5, h * 0.35), stroke);
        canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.35, h * 0.3), width: w * 0.28, height: h * 0.2), fill);
        canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.65, h * 0.42), width: w * 0.28, height: h * 0.2), fill);
        canvas.drawCircle(Offset(w * 0.5, h * 0.9), w * 0.06, Paint()..color = color.withValues(alpha: 0.5));
        break;

      case 'stomata':
        canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.35, h * 0.5), width: w * 0.4, height: h * 0.35), fill);
        canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.65, h * 0.5), width: w * 0.4, height: h * 0.35), fill);
        canvas.drawOval(Rect.fromCenter(center: Offset(w * 0.5, h * 0.5), width: w * 0.14, height: h * 0.3), Paint()..color = Colors.white);
        break;

      case 'animal_tissues':
        canvas.drawRect(Rect.fromLTWH(w * 0.12, h * 0.15, w * 0.32, h * 0.32), fill);
        canvas.drawCircle(Offset(w * 0.72, h * 0.28), w * 0.16, Paint()..color = color.withValues(alpha: 0.55));
        for (int i = 0; i < 4; i++) {
          canvas.drawLine(Offset(w * 0.2, h * (0.6 + i * 0.02)), Offset(w * 0.5, h * (0.55 + i * 0.06)), stroke);
        }
        canvas.drawCircle(Offset(w * 0.75, h * 0.75), w * 0.1, faint);
        canvas.drawCircle(Offset(w * 0.75, h * 0.75), w * 0.1, stroke);
        break;

      case 'muscle':
        for (int i = 0; i < 4; i++) {
          final y = h * (0.2 + i * 0.2);
          canvas.drawLine(Offset(w * 0.15, y), Offset(w * 0.85, y), stroke..strokeWidth = 2.2);
        }
        break;

      case 'joints':
        canvas.drawCircle(Offset(w * 0.5, h * 0.35), w * 0.16, faint);
        canvas.drawCircle(Offset(w * 0.5, h * 0.35), w * 0.09, fill);
        canvas.drawLine(Offset(w * 0.5, h * 0.5), Offset(w * 0.5, h * 0.85), stroke..strokeWidth = 3);
        break;

      default:
        for (int i = 0; i < 3; i++) {
          canvas.drawCircle(Offset(w * 0.25, h * (0.3 + i * 0.22)), 3, fill);
          canvas.drawLine(Offset(w * 0.38, h * (0.3 + i * 0.22)), Offset(w * 0.82, h * (0.3 + i * 0.22)), stroke..strokeWidth = 1.6);
        }
    }
  }

  @override
  bool shouldRepaint(covariant _NoteIconPainter oldDelegate) => oldDelegate.iconKey != iconKey || oldDelegate.color != color;
}

/// A grid of "revision card" summaries — one per sub-topic of a chapter —
/// meant for quick pre-exam reading: a short illustration, a title, and a
/// handful of crisp bullet points instead of full prose. Tapping a card
/// expands it to fill the width so long point lists stay readable.
class RevisionNotesSection extends StatefulWidget {
  final List<RevisionNote> notes;
  final Color accent;

  const RevisionNotesSection({super.key, required this.notes, this.accent = Colors.teal});

  @override
  State<RevisionNotesSection> createState() => _RevisionNotesSectionState();
}

class _RevisionNotesSectionState extends State<RevisionNotesSection> {
  int? _expanded;

  static const _palette = [
    Color(0xFF2D7D5F),
    Color(0xFF3F6A9C),
    Color(0xFFD9622A),
    Color(0xFF7A5AA8),
    Color(0xFFC2455B),
    Color(0xFFC99A24),
  ];

  @override
  Widget build(BuildContext context) {
    if (widget.notes.isEmpty) return const SizedBox.shrink();

    return LayoutBuilder(
      builder: (context, constraints) {
        final isWide = constraints.maxWidth > 620;
        return Wrap(
          spacing: 12,
          runSpacing: 12,
          children: List.generate(widget.notes.length, (i) {
            final note = widget.notes[i];
            final color = _palette[i % _palette.length];
            final isExpanded = _expanded == i;
            final cardWidth = isExpanded || !isWide ? constraints.maxWidth : (constraints.maxWidth - 12) / 2;

            return SizedBox(
              width: cardWidth,
              child: _NoteCard(
                note: note,
                color: color,
                expanded: isExpanded,
                onTap: () => setState(() => _expanded = isExpanded ? null : i),
              ),
            );
          }),
        );
      },
    );
  }
}

class _NoteCard extends StatelessWidget {
  final RevisionNote note;
  final Color color;
  final bool expanded;
  final VoidCallback onTap;

  const _NoteCard({required this.note, required this.color, required this.expanded, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return Material(
      color: Colors.transparent,
      child: InkWell(
        borderRadius: BorderRadius.circular(14),
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(
            color: color.withValues(alpha: 0.06),
            borderRadius: BorderRadius.circular(14),
            border: Border.all(color: color.withValues(alpha: 0.25)),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    width: 40,
                    height: 40,
                    decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(10), border: Border.all(color: color.withValues(alpha: 0.3))),
                    child: CustomPaint(painter: _NoteIconPainter(iconKey: note.iconKey, color: color)),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text(note.title, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14, color: color)),
                  ),
                  Icon(expanded ? Icons.expand_less : Icons.expand_more, color: color, size: 20),
                ],
              ),
              const SizedBox(height: 10),
              ...note.points
                  .take(expanded ? note.points.length : 3)
                  .map((p) => Padding(
                        padding: const EdgeInsets.only(bottom: 5),
                        child: Row(
                          crossAxisAlignment: CrossAxisAlignment.start,
                          children: [
                            Padding(
                              padding: const EdgeInsets.only(top: 5, right: 6),
                              child: Container(width: 5, height: 5, decoration: BoxDecoration(color: color, shape: BoxShape.circle)),
                            ),
                            Expanded(child: Text(p, style: TextStyle(fontSize: 12.5, height: 1.35))),
                          ],
                        ),
                      )),
              if (!expanded && note.points.length > 3)
                Text('+${note.points.length - 3} more — tap to expand', style: TextStyle(fontSize: 11, color: color, fontWeight: FontWeight.w600)),
            ],
          ),
        ),
      ),
    );
  }
}
