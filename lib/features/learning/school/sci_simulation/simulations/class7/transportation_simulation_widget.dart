import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/diagram_helpers.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

enum _View { heart, stem }

/// Real, labeled diagrams for transportation in animals (the heart, with
/// arteries and veins) and in plants (a stem cross-section showing the ring
/// of vascular bundles), replacing what used to be a scaling heart icon and
/// a plain rectangle with moving dots.
class TransportationSimulationWidget extends StatefulWidget {
  const TransportationSimulationWidget({super.key});

  @override
  State<TransportationSimulationWidget> createState() => _TransportationSimulationWidgetState();
}

class _TransportationSimulationWidgetState extends State<TransportationSimulationWidget> with SingleTickerProviderStateMixin {
  _View _view = _View.heart;
  DiagramPart? _selected;
  late AnimationController _controller;

  static const _heartParts = [
    DiagramPart(name: 'Heart', label: 'Heart', color: Color(0xFFC62828), function: 'A muscular, fist-sized organ that rhythmically contracts to pump blood through the whole body, non-stop.'),
    DiagramPart(name: 'Artery', label: 'Artery', color: Color(0xFFE53935), function: 'A thick-walled blood vessel that carries oxygen-rich blood away from the heart to the body.'),
    DiagramPart(name: 'Vein', label: 'Vein', color: Color(0xFF1E88E5), function: 'A blood vessel that carries oxygen-poor blood back from the body to the heart.'),
  ];

  static const _stemParts = [
    DiagramPart(name: 'Epidermis', label: 'Epidermis', color: Color(0xFF8D6E63), function: 'The outermost protective layer of the stem, often covered with a waxy cuticle to reduce water loss.'),
    DiagramPart(name: 'Cortex', label: 'Cortex', color: Color(0xFFA5D6A7), function: 'A layer of packing cells beneath the epidermis that provides support and stores food.'),
    DiagramPart(name: 'Xylem', label: 'Xylem', color: Color(0xFF1E88E5), function: 'Tube-like vessels that carry water and dissolved minerals upward from the roots to the leaves.'),
    DiagramPart(name: 'Phloem', label: 'Phloem', color: Color(0xFF43A047), function: 'Sieve tubes that carry the food made in the leaves down to other parts of the plant (translocation).'),
    DiagramPart(name: 'Pith', label: 'Pith', color: Color(0xFFFFF3C4), function: 'The soft, central tissue of the stem that stores food and water.'),
  ];

  List<DiagramPart> get _parts => _view == _View.heart ? _heartParts : _stemParts;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 2))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Transportation Systems',
      icon: Icons.favorite,
      accent: Colors.red.shade600,
      description: 'Tap a labeled part to learn its role. Compare animals and plants.',
      actions: [
        ToggleButtons(
          isSelected: [_view == _View.heart, _view == _View.stem],
          onPressed: (i) => setState(() {
            _view = i == 0 ? _View.heart : _View.stem;
            _selected = null;
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.red.shade600,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 56),
          children: [Text(TrilingualService.instance.getUIText('Heart')), Text(TrilingualService.instance.getUIText('Plant'))],
        ),
      ],
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              ResponsiveDiagram(
                aspectRatio: _view == _View.heart ? 1.1 : 1.0,
                maxWidth: 420,
                backgroundGradient: _view == _View.heart ? [Colors.red.shade50, Colors.pink.shade50] : [Colors.green.shade50, Colors.lightGreen.shade50],
                painter: _TransportPainter(view: _view, selectedName: _selected?.name, t: _controller.value),
                parts: _parts,
                hitRects: (size) => _hitRectsFor(_view, size),
                onSelect: (p) => setState(() => _selected = p),
              ),
              const SizedBox(height: 14),
              DiagramPartPicker(parts: _parts, selected: _selected, onSelect: (p) => setState(() => _selected = p)),
            ],
          );
        },
      ),
    );
  }
}

Map<String, Rect> _hitRectsFor(_View view, Size size) {
  final w = size.width, h = size.height;
  Rect f(double l, double t, double r, double b) => Rect.fromLTRB(l * w, t * h, r * w, b * h);

  if (view == _View.heart) {
    return {
      'Heart': f(0.20, 0.30, 0.80, 0.90),
      'Artery': f(0.42, 0.02, 0.62, 0.30),
      'Vein': f(0.58, 0.02, 0.78, 0.30),
    };
  }
  final center = Offset(w * 0.5, h * 0.5);
  final r = math.min(w, h) * 0.42;
  return {
    'Epidermis': Rect.fromCircle(center: center, radius: r).inflate(-2),
    'Cortex': Rect.fromCircle(center: center, radius: r * 0.82),
    'Xylem': Rect.fromCircle(center: center, radius: r * 0.55),
    'Phloem': Rect.fromCircle(center: center, radius: r * 0.62),
    'Pith': Rect.fromCircle(center: center, radius: r * 0.22),
  };
}

class _TransportPainter extends CustomPainter {
  final _View view;
  final String? selectedName;
  final double t;

  _TransportPainter({required this.view, required this.selectedName, required this.t});

  bool _sel(String name) => name == selectedName;

  @override
  void paint(Canvas canvas, Size size) {
    if (view == _View.heart) {
      _paintHeart(canvas, size);
    } else {
      _paintStem(canvas, size);
    }
  }

  void _label(Canvas canvas, Offset pos, String text, Color color) {
    final tp = TextPainter(
      text: TextSpan(text: text, style: TextStyle(fontSize: 9.5, fontWeight: FontWeight.w700, color: Colors.black87, height: 1.1)),
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
    )..layout(maxWidth: 74);
    final bg = Rect.fromLTWH(pos.dx - tp.width / 2 - 3, pos.dy - 1, tp.width + 6, tp.height + 2);
    canvas.drawRRect(RRect.fromRectAndRadius(bg, const Radius.circular(4)), Paint()..color = Colors.white.withValues(alpha: 0.82));
    tp.paint(canvas, Offset(pos.dx - tp.width / 2, pos.dy));
  }

  // ---------------- Heart ----------------
  void _paintHeart(Canvas canvas, Size size) {
    final w = size.width, h = size.height;
    final beat = 1.0 + math.sin(t * 2 * math.pi) * 0.03;

    canvas.save();
    canvas.translate(w / 2, h * 0.62);
    canvas.scale(beat);
    canvas.translate(-w / 2, -h * 0.62);

    // Vein (into the heart, blood returning — blue).
    final vein = Path()
      ..moveTo(w * 0.66, h * 0.02)
      ..quadraticBezierTo(w * 0.60, h * 0.14, w * 0.56, h * 0.28);
    final emphVein = _sel('Vein');
    if (emphVein) drawGlow(canvas, Offset(w * 0.6, h * 0.14), w * 0.14, const Color(0xFF1E88E5));
    canvas.drawPath(vein, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = w * 0.07
      ..strokeCap = StrokeCap.round
      ..color = const Color(0xFF1E88E5).withValues(alpha: emphVein ? 1.0 : 0.85));

    // Artery (out of the heart, blood leaving — red).
    final artery = Path()
      ..moveTo(w * 0.40, h * 0.02)
      ..quadraticBezierTo(w * 0.34, h * 0.10, w * 0.40, h * 0.26);
    final emphArtery = _sel('Artery');
    if (emphArtery) drawGlow(canvas, Offset(w * 0.37, h * 0.14), w * 0.14, const Color(0xFFE53935));
    canvas.drawPath(artery, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = w * 0.07
      ..strokeCap = StrokeCap.round
      ..color = const Color(0xFFE53935).withValues(alpha: emphArtery ? 1.0 : 0.85));

    // Heart body.
    final outline = Path()
      ..moveTo(w * 0.5, h * 0.32)
      ..cubicTo(w * 0.20, h * 0.22, w * 0.08, h * 0.55, w * 0.30, h * 0.76)
      ..cubicTo(w * 0.40, h * 0.86, w * 0.5, h * 0.92, w * 0.5, h * 0.92)
      ..cubicTo(w * 0.5, h * 0.92, w * 0.60, h * 0.86, w * 0.70, h * 0.76)
      ..cubicTo(w * 0.92, h * 0.55, w * 0.80, h * 0.22, w * 0.5, h * 0.32)
      ..close();
    final emphHeart = _sel('Heart');
    if (emphHeart) drawGlow(canvas, Offset(w * 0.5, h * 0.55), w * 0.4, const Color(0xFFC62828));
    canvas.drawPath(outline, Paint()..color = const Color(0xFFEF5350));
    canvas.drawPath(outline, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphHeart ? 3 : 1.8
      ..color = emphHeart ? Colors.black87 : const Color(0xFFB71C1C));
    // Central groove hinting at the septum.
    canvas.drawLine(Offset(w * 0.5, h * 0.36), Offset(w * 0.5, h * 0.88), Paint()
      ..strokeWidth = 2
      ..color = const Color(0xFFB71C1C).withValues(alpha: 0.4));

    canvas.restore();

    _label(canvas, Offset(w * 0.30, h * 0.0), 'Artery', const Color(0xFFE53935));
    _label(canvas, Offset(w * 0.78, h * 0.0), 'Vein', const Color(0xFF1E88E5));
    _label(canvas, Offset(w * 0.5, h * 0.95), 'Heart', const Color(0xFFC62828));
  }

  // ---------------- Stem cross-section ----------------
  void _paintStem(Canvas canvas, Size size) {
    final w = size.width, h = size.height;
    final center = Offset(w * 0.5, h * 0.5);
    final r = math.min(w, h) * 0.42;

    void ring(double radius, Color color, String name, {double alpha = 0.5}) {
      final emphasize = _sel(name);
      if (emphasize) drawGlow(canvas, center, radius * 1.1, color);
      canvas.drawCircle(center, radius, Paint()..color = color.withValues(alpha: alpha));
      canvas.drawCircle(center, radius, Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = emphasize ? 2.4 : 1.2
        ..color = emphasize ? Colors.black87 : color);
    }

    ring(r, const Color(0xFF8D6E63), 'Epidermis', alpha: 0.25);
    ring(r * 0.82, const Color(0xFFA5D6A7), 'Cortex', alpha: 0.55);

    // Ring of vascular bundles (xylem inner wedge + phloem outer arc).
    const bundles = 8;
    final emphXylem = _sel('Xylem');
    final emphPhloem = _sel('Phloem');
    if (emphXylem) drawGlow(canvas, center, r * 0.6, const Color(0xFF1E88E5));
    if (emphPhloem) drawGlow(canvas, center, r * 0.66, const Color(0xFF43A047));
    for (int i = 0; i < bundles; i++) {
      final angle = i / bundles * 2 * math.pi;
      final bundleCenter = center + Offset(math.cos(angle), math.sin(angle)) * r * 0.68;
      final xylemCenter = center + Offset(math.cos(angle), math.sin(angle)) * r * 0.55;

      // Phloem (outer arc of the bundle).
      canvas.drawCircle(bundleCenter, r * 0.10, Paint()..color = const Color(0xFF43A047).withValues(alpha: emphPhloem ? 1.0 : 0.85));
      canvas.drawCircle(bundleCenter, r * 0.10, Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = emphPhloem ? 2 : 1
        ..color = emphPhloem ? Colors.black87 : const Color(0xFF2E7D32));

      // Xylem (inner wedge of the bundle) — a few vessel dots.
      canvas.drawCircle(xylemCenter, r * 0.09, Paint()..color = const Color(0xFF1E88E5).withValues(alpha: emphXylem ? 1.0 : 0.85));
      canvas.drawCircle(xylemCenter, r * 0.09, Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = emphXylem ? 2 : 1
        ..color = emphXylem ? Colors.black87 : const Color(0xFF0D47A1));

      // Animated water droplet rising through xylem (visible on a couple of bundles).
      if (i % 3 == 0) {
        final travel = (t + i / bundles) % 1.0;
        final dropRadius = r * (0.55 - 0.02);
        final dropAngle = angle;
        final dropCenter = Offset.lerp(
          center + Offset(math.cos(dropAngle), math.sin(dropAngle)) * dropRadius * 0.3,
          center + Offset(math.cos(dropAngle), math.sin(dropAngle)) * dropRadius,
          travel,
        )!;
        canvas.drawCircle(dropCenter, 2, Paint()..color = Colors.white.withValues(alpha: 0.9));
      }
    }

    // Pith (centre).
    final emphPith = _sel('Pith');
    if (emphPith) drawGlow(canvas, center, r * 0.3, const Color(0xFFFFF3C4));
    canvas.drawCircle(center, r * 0.22, Paint()..color = const Color(0xFFFFF3C4).withValues(alpha: 0.9));
    canvas.drawCircle(center, r * 0.22, Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = emphPith ? 2.2 : 1
      ..color = emphPith ? Colors.black87 : const Color(0xFFFBC02D));

    _label(canvas, Offset(center.dx, center.dy - r - 14), 'Epidermis', const Color(0xFF8D6E63));
    _label(canvas, Offset(center.dx + r * 0.6, center.dy + r * 0.6 + 10), 'Cortex', const Color(0xFF2E7D32));
    _label(canvas, Offset(center.dx, center.dy), 'Pith', const Color(0xFFFBC02D));
    _label(canvas, Offset(center.dx - r * 0.75, center.dy - r * 0.55), 'Xylem', const Color(0xFF0D47A1));
    _label(canvas, Offset(center.dx - r * 0.95, center.dy - r * 0.15), 'Phloem', const Color(0xFF2E7D32));
  }

  @override
  bool shouldRepaint(covariant _TransportPainter oldDelegate) => true;
}
