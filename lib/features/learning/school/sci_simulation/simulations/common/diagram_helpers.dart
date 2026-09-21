import 'package:flutter/material.dart';

/// Shared drawing/interaction primitives for hand-illustrated biology
/// diagrams (see `organelle_diagram.dart` for the cell-diagram original).
/// Keeps every diagram — digestive system, neuron, leaf cross-section, etc.
/// — visually consistent and lets each one scale cleanly from a phone up to
/// a tablet or a classroom smart board.

/// Soft highlight glow drawn behind a selected/emphasised part.
void drawGlow(Canvas canvas, Offset center, double radius, Color color) {
  final glowPaint = Paint()
    ..color = color.withValues(alpha: 0.45)
    ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 10);
  canvas.drawCircle(center, radius, glowPaint);
}

/// A small pill-shaped text label anchored near a diagram part, matching
/// the look used across all illustrated diagrams in this app.
void drawDiagramLabel(Canvas canvas, Offset anchor, String text, Color color, {TextAlign align = TextAlign.left}) {
  final tp = TextPainter(
    text: TextSpan(text: text, style: TextStyle(fontSize: 9.5, fontWeight: FontWeight.w700, color: Colors.black87)),
    textDirection: TextDirection.ltr,
  )..layout();
  double dx = anchor.dx;
  if (align == TextAlign.center) dx -= tp.width / 2;
  if (align == TextAlign.right) dx -= tp.width;
  final pos = Offset(dx, anchor.dy);
  final bgRect = Rect.fromLTWH(pos.dx - 3, pos.dy - 1, tp.width + 6, tp.height + 2);
  canvas.drawRRect(RRect.fromRectAndRadius(bgRect, const Radius.circular(4)), Paint()..color = Colors.white.withValues(alpha: 0.82));
  canvas.drawRRect(RRect.fromRectAndRadius(bgRect, const Radius.circular(4)), Paint()
    ..style = PaintingStyle.stroke
    ..strokeWidth = 0.8
    ..color = color.withValues(alpha: 0.6));
  tp.paint(canvas, pos);
}

/// One tappable, labeled part of an illustrated diagram: a name for the
/// info panel, a short on-canvas tag, an explanation, a colour, and the
/// canvas-pixel hit box supplied by the painter's own geometry function so
/// what's drawn and what's tappable never drift apart.
class DiagramPart {
  final String name;
  final String label;
  final String function;
  final Color color;

  const DiagramPart({required this.name, required this.label, required this.function, required this.color});
}

/// Wraps an illustrated [CustomPainter] with: a fixed-aspect canvas capped
/// at [maxWidth] (so it stays sensible on a tablet or classroom smart
/// board instead of stretching edge to edge), a semi-transparent tap
/// overlay per part for hit-testing, and a light card background. Every
/// illustration in this app is vector-drawn, so it stays crisp at any
/// screen size or pixel density.
class ResponsiveDiagram extends StatelessWidget {
  final double aspectRatio;
  final double maxWidth;
  final List<Color> backgroundGradient;
  final CustomPainter painter;
  final List<DiagramPart> parts;
  final Map<String, Rect> Function(Size canvasSize) hitRects;
  final ValueChanged<DiagramPart> onSelect;

  const ResponsiveDiagram({
    super.key,
    required this.aspectRatio,
    required this.painter,
    required this.parts,
    required this.hitRects,
    required this.onSelect,
    this.maxWidth = 640,
    this.backgroundGradient = const [Color(0xFFF1F8F6), Color(0xFFEAF4FB)],
  });

  @override
  Widget build(BuildContext context) {
    return Center(
      child: ConstrainedBox(
        constraints: BoxConstraints(maxWidth: maxWidth),
        child: AspectRatio(
          aspectRatio: aspectRatio,
          child: Container(
            decoration: BoxDecoration(
              gradient: LinearGradient(begin: Alignment.topLeft, end: Alignment.bottomRight, colors: backgroundGradient),
              borderRadius: BorderRadius.circular(12),
            ),
            clipBehavior: Clip.antiAlias,
            child: LayoutBuilder(
              builder: (context, constraints) {
                final canvasSize = Size(constraints.maxWidth, constraints.maxHeight);
                final rects = hitRects(canvasSize);
                return Stack(
                  children: [
                    Positioned.fill(child: CustomPaint(painter: painter)),
                    for (final part in parts)
                      if (rects[part.name] != null)
                        Positioned.fromRect(
                          rect: rects[part.name]!,
                          child: GestureDetector(
                            behavior: HitTestBehavior.translucent,
                            onTap: () => onSelect(part),
                          ),
                        ),
                  ],
                );
              },
            ),
          ),
        ),
      ),
    );
  }
}

/// The chip row + description panel every illustrated-diagram simulation
/// shows below the canvas, so tapping a chip and tapping the diagram do the
/// same thing.
class DiagramPartPicker extends StatelessWidget {
  final List<DiagramPart> parts;
  final DiagramPart? selected;
  final ValueChanged<DiagramPart> onSelect;
  final String placeholder;

  const DiagramPartPicker({super.key, required this.parts, required this.selected, required this.onSelect, this.placeholder = 'Tap a labeled part above to see what it does.'});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Wrap(
          spacing: 6,
          runSpacing: 6,
          children: parts.map((p) {
            final isSelected = selected?.name == p.name;
            return ActionChip(
              label: Text(p.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
              backgroundColor: isSelected ? p.color : p.color.withValues(alpha: 0.25),
              onPressed: () => onSelect(p),
            );
          }).toList(),
        ),
        const SizedBox(height: 12),
        Container(
          width: double.infinity,
          padding: const EdgeInsets.all(12),
          decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
          child: selected == null
              ? Text(placeholder, style: TextStyle(color: Colors.black54, fontSize: 13))
              : Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(selected!.name, style: TextStyle(fontWeight: FontWeight.bold, color: selected!.color, fontSize: 14)),
                    const SizedBox(height: 4),
                    Text(selected!.function, style: TextStyle(fontSize: 13)),
                  ],
                ),
        ),
      ],
    );
  }
}
