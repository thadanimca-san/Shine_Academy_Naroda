import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// Slide an external point's distance from the centre and watch the
/// tangent line draw itself out from the point of contact, its length
/// updating live via the Pythagoras relation — tangent² = distance² − radius².
class Class10CirclesSimulationWidget extends StatefulWidget {
  const Class10CirclesSimulationWidget({super.key});

  @override
  State<Class10CirclesSimulationWidget> createState() => _Class10CirclesSimulationWidgetState();
}

class _Class10CirclesSimulationWidgetState extends State<Class10CirclesSimulationWidget> with SingleTickerProviderStateMixin {
  final double _radius = 3;
  double _distance = 6;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 700));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final tangentSq = _distance * _distance - _radius * _radius;
    final tangent = math.sqrt(tangentSq.clamp(0, double.infinity));

    return SimFrame(
      title: 'Tangent Length from an External Point',
      icon: Icons.circle_outlined,
      accent: Colors.indigo.shade600,
      description: 'The tangent, radius and the line to the centre always form a right triangle — slide the distance and watch the tangent draw itself out.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.indigo.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeOutCubic.transform(_controller.value);
                return CustomPaint(size: Size.infinite, painter: _TangentPainter(radius: _radius, distance: _distance, drawT: eased));
              },
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Radius', value: '${_radius.toStringAsFixed(0)} cm'),
            SimMetric(label: 'Distance to Centre', value: '${_distance.toStringAsFixed(1)} cm', color: Colors.blue),
            SimMetric(label: 'Tangent Length', value: '${tangent.toStringAsFixed(2)} cm', color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Distance from centre: ${_distance.toStringAsFixed(1)} cm',
            value: _distance,
            min: 3.1,
            max: 10,
            divisions: 30,
            activeColor: Colors.indigo,
            onChanged: (v) => setState(() {
              _distance = v;
              _controller.forward(from: 0);
            }),
          ),
        ],
      ),
    );
  }
}

class _TangentPainter extends CustomPainter {
  final double radius, distance, drawT;
  _TangentPainter({required this.radius, required this.distance, required this.drawT});

  @override
  void paint(Canvas canvas, Size size) {
    const scale = 12.0;
    final center = Offset(40, size.height / 2);
    canvas.drawCircle(center, radius * scale, Paint()..color = Colors.indigo.shade200..style = PaintingStyle.stroke..strokeWidth = 2);

    final point = center + Offset(distance * scale, 0);
    final angle = math.acos((radius / distance).clamp(-1.0, 1.0));
    final touchPoint = center + Offset(math.cos(angle) * radius, -math.sin(angle) * radius) * scale;
    final animatedPoint = Offset.lerp(touchPoint, point, drawT)!;

    canvas.drawLine(center, point, Paint()..color = Colors.blue..strokeWidth = 2);
    canvas.drawLine(center, touchPoint, Paint()..color = Colors.indigo..strokeWidth = 2);
    canvas.drawLine(touchPoint, animatedPoint, Paint()..color = Colors.deepOrange..strokeWidth = 2.5);

    canvas.drawCircle(center, 3, Paint()..color = Colors.black);
    canvas.drawCircle(point, 4, Paint()..color = Colors.blue.shade800.withValues(alpha: 0.4 + 0.6 * drawT));
    canvas.drawCircle(touchPoint, 4, Paint()..color = Colors.deepOrange);
  }

  @override
  bool shouldRepaint(covariant _TangentPainter oldDelegate) =>
      oldDelegate.radius != radius || oldDelegate.distance != distance || oldDelegate.drawT != drawT;
}
