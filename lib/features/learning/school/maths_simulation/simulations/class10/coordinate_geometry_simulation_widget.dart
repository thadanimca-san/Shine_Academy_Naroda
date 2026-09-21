import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// Two draggable-via-slider points on a grid, with the right-triangle
/// used to derive the distance formula drawing itself in — horizontal
/// leg, then vertical leg, then hypotenuse — showing the Pythagoras
/// Theorem doing the actual work whenever a point moves.
class Class10CoordinateGeometrySimulationWidget extends StatefulWidget {
  const Class10CoordinateGeometrySimulationWidget({super.key});

  @override
  State<Class10CoordinateGeometrySimulationWidget> createState() => _Class10CoordinateGeometrySimulationWidgetState();
}

class _Class10CoordinateGeometrySimulationWidgetState extends State<Class10CoordinateGeometrySimulationWidget> with SingleTickerProviderStateMixin {
  double _x1 = -3, _y1 = -2, _x2 = 4, _y2 = 3;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 900));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _replay() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final dx = _x2 - _x1;
    final dy = _y2 - _y1;
    final distance = math.sqrt(dx * dx + dy * dy);

    return SimFrame(
      title: 'The Distance Formula',
      icon: Icons.straighten,
      accent: Colors.deepPurple.shade400,
      description: 'The distance between two points is the hypotenuse of a right triangle formed by their horizontal and vertical separation — watch it draw in leg by leg.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 180,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.deepPurple.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                return CustomPaint(size: Size.infinite, painter: _DistancePainter(x1: _x1, y1: _y1, x2: _x2, y2: _y2, drawT: eased));
              },
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Δx', value: dx.toStringAsFixed(0), color: Colors.blue),
            SimMetric(label: 'Δy', value: dy.toStringAsFixed(0), color: Colors.teal),
            SimMetric(label: 'Distance', value: distance.toStringAsFixed(2), color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'x₁: ${_x1.toStringAsFixed(0)}', value: _x1, min: -8, max: 8, divisions: 16, activeColor: Colors.blue, onChanged: (v) => setState(() { _x1 = v; _replay(); })),
          SimSlider(label: 'y₁: ${_y1.toStringAsFixed(0)}', value: _y1, min: -8, max: 8, divisions: 16, activeColor: Colors.blue, onChanged: (v) => setState(() { _y1 = v; _replay(); })),
          SimSlider(label: 'x₂: ${_x2.toStringAsFixed(0)}', value: _x2, min: -8, max: 8, divisions: 16, activeColor: Colors.teal, onChanged: (v) => setState(() { _x2 = v; _replay(); })),
          SimSlider(label: 'y₂: ${_y2.toStringAsFixed(0)}', value: _y2, min: -8, max: 8, divisions: 16, activeColor: Colors.teal, onChanged: (v) => setState(() { _y2 = v; _replay(); })),
        ],
      ),
    );
  }
}

class _DistancePainter extends CustomPainter {
  final double x1, y1, x2, y2, drawT;
  _DistancePainter({required this.x1, required this.y1, required this.x2, required this.y2, required this.drawT});

  @override
  void paint(Canvas canvas, Size size) {
    Offset toScreen(double x, double y) => Offset((x + 10) / 20 * size.width, size.height - (y + 10) / 20 * size.height);
    final p1 = toScreen(x1, y1);
    final p2 = toScreen(x2, y2);
    final corner = toScreen(x2, y1);

    // Draw the horizontal leg first (0 -> 0.4), then vertical leg (0.4 -> 0.75),
    // then the hypotenuse (0.75 -> 1.0), tracing the Pythagoras construction in order.
    final horizT = (drawT / 0.4).clamp(0.0, 1.0);
    final vertT = ((drawT - 0.4) / 0.35).clamp(0.0, 1.0);
    final hypT = ((drawT - 0.75) / 0.25).clamp(0.0, 1.0);

    canvas.drawLine(p1, Offset.lerp(p1, corner, horizT)!, Paint()..color = Colors.blue..strokeWidth = 2);
    canvas.drawLine(corner, Offset.lerp(corner, p2, vertT)!, Paint()..color = Colors.teal..strokeWidth = 2);
    canvas.drawLine(p1, Offset.lerp(p1, p2, hypT)!, Paint()..color = Colors.deepOrange..strokeWidth = 2.5);

    canvas.drawCircle(p1, 5, Paint()..color = Colors.deepPurple);
    if (drawT > 0.75) {
      canvas.drawCircle(p2, 5, Paint()..color = Colors.deepPurple.withValues(alpha: hypT));
    }
  }

  @override
  bool shouldRepaint(covariant _DistancePainter oldDelegate) => true;
}
