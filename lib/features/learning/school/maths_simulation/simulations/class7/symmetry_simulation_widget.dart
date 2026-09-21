import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Pick a regular polygon and see all of its lines of symmetry draw in
/// one by one, plus a Play button that spins the polygon through a full
/// rotation so its rotational symmetry of order n is felt, not just
/// stated as a number.
class SymmetrySimulationWidget extends StatefulWidget {
  const SymmetrySimulationWidget({super.key});

  @override
  State<SymmetrySimulationWidget> createState() => _SymmetrySimulationWidgetState();
}

class _SymmetrySimulationWidgetState extends State<SymmetrySimulationWidget> with SingleTickerProviderStateMixin {
  int _sides = 5;
  late AnimationController _linesController;
  late AnimationController _spinController;

  @override
  void initState() {
    super.initState();
    _linesController = AnimationController(vsync: this, duration: const Duration(milliseconds: 900));
    _linesController.forward();
    _spinController = AnimationController(vsync: this, duration: const Duration(milliseconds: 1400));
  }

  @override
  void dispose() {
    _linesController.dispose();
    _spinController.dispose();
    super.dispose();
  }

  void _spin() => _spinController.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Lines of Symmetry',
      icon: Icons.auto_awesome_mosaic,
      accent: Colors.pink.shade600,
      description: 'A regular polygon with n sides has n lines of symmetry, and rotational symmetry of order n — press spin to feel it.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 200,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.pink.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: Listenable.merge([_linesController, _spinController]),
              builder: (context, _) {
                final linesT = Curves.easeOut.transform(_linesController.value);
                final spinAngle = Curves.easeInOut.transform(_spinController.value) * 2 * 3.141592653589793;
                return CustomPaint(size: Size.infinite, painter: _PolygonPainter(sides: _sides, linesT: linesT, spinAngle: spinAngle));
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: TextButton.icon(
              onPressed: _spin,
              icon: Icon(Icons.rotate_right, size: 18),
              label: Text(TrilingualService.instance.getUIText('Spin (rotational symmetry)')),
              style: TextButton.styleFrom(foregroundColor: Colors.pink.shade600),
            ),
          ),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Sides', value: '$_sides'),
            SimMetric(label: 'Lines of Symmetry', value: '$_sides', color: Colors.pink),
            SimMetric(label: 'Rotational Order', value: '$_sides', color: Colors.deepPurple),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Number of sides: $_sides',
            value: _sides.toDouble(),
            min: 3,
            max: 10,
            divisions: 7,
            activeColor: Colors.pink,
            onChanged: (val) => setState(() {
              _sides = val.round();
              _linesController.forward(from: 0);
            }),
          ),
        ],
      ),
    );
  }
}

class _PolygonPainter extends CustomPainter {
  final int sides;
  final double linesT; // 0..1, how many symmetry lines have drawn in so far
  final double spinAngle; // extra rotation applied to the whole polygon (radians)
  _PolygonPainter({required this.sides, this.linesT = 1, this.spinAngle = 0});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final radius = math.min(size.width, size.height) / 2 - 20;

    Offset vertex(int i) {
      final angle = -math.pi / 2 + (2 * math.pi * i / sides) + spinAngle;
      return center + Offset(math.cos(angle) * radius, math.sin(angle) * radius);
    }

    final points = List.generate(sides, vertex);
    final path = Path()..addPolygon(points, true);
    canvas.drawPath(path, Paint()..color = Colors.pink.shade200);
    canvas.drawPath(path, Paint()..color = Colors.pink.shade700..style = PaintingStyle.stroke..strokeWidth = 2);

    // Reveal the symmetry lines one at a time as linesT sweeps 0 -> 1.
    final linesToShow = (sides * linesT).ceil().clamp(0, sides);
    final symmetryPaint = Paint()
      ..color = Colors.deepPurple.withValues(alpha: 0.5)
      ..strokeWidth = 1;
    for (int i = 0; i < linesToShow; i++) {
      final frac = (sides * linesT - i).clamp(0.0, 1.0);
      final angle = -math.pi / 2 + (math.pi * i / sides);
      final full1 = center + Offset(math.cos(angle) * radius, math.sin(angle) * radius);
      final full2 = center - Offset(math.cos(angle) * radius, math.sin(angle) * radius);
      final p1 = Offset.lerp(center, full1, frac)!;
      final p2 = Offset.lerp(center, full2, frac)!;
      canvas.drawLine(p1, p2, symmetryPaint);
    }
  }

  @override
  bool shouldRepaint(covariant _PolygonPainter oldDelegate) =>
      oldDelegate.sides != sides || oldDelegate.linesT != linesT || oldDelegate.spinAngle != spinAngle;
}
