import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// An arc subtends an angle at the centre and at a point on the
/// circumference: press play to watch the far point glide around the
/// circumference while the inscribed angle keeps re-forming, staying
/// exactly half the central angle; slide the arc size to explore any
/// single configuration.
class CirclesSimulationWidget extends StatefulWidget {
  const CirclesSimulationWidget({super.key});

  @override
  State<CirclesSimulationWidget> createState() => _CirclesSimulationWidgetState();
}

class _CirclesSimulationWidgetState extends State<CirclesSimulationWidget> with SingleTickerProviderStateMixin {
  double _arcAngle = 80; // degrees, the central angle
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 1800));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _play() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final circumAngle = _arcAngle / 2;

    return SimFrame(
      title: 'Central Angle = 2 × Circumference Angle',
      icon: Icons.circle_outlined,
      accent: Colors.deepPurple.shade400,
      description: 'Press play to watch the far point glide around the circumference — the angle an arc subtends at the centre stays double the angle at the circumference, wherever the point sits.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 200,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.deepPurple.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                // Sweep the far point from just past the arc, around the major
                // arc, without ever crossing p1 or p2.
                final farT = eased; // 0..1 maps to a safe range of the major arc
                return CustomPaint(size: Size.infinite, painter: _CircleAnglePainter(arcAngle: _arcAngle, farT: farT));
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: ElevatedButton.icon(
              onPressed: _play,
              icon: Icon(Icons.play_arrow),
              label: Text(TrilingualService.instance.getUIText('Glide point')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.deepPurple.shade400, foregroundColor: Colors.white),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Central Angle', value: '${_arcAngle.toStringAsFixed(0)}°', color: Colors.red),
            SimMetric(label: 'Circumference Angle', value: '${circumAngle.toStringAsFixed(0)}°', color: Colors.blue),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Arc size: ${_arcAngle.toStringAsFixed(0)}°', value: _arcAngle, min: 20, max: 160, divisions: 28, activeColor: Colors.deepPurple, onChanged: (v) => setState(() => _arcAngle = v)),
        ],
      ),
    );
  }
}

class _CircleAnglePainter extends CustomPainter {
  final double arcAngle;
  final double farT;
  _CircleAnglePainter({required this.arcAngle, this.farT = 0.5});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2 + 10);
    final radius = math.min(size.width, size.height) / 2 - 20;
    canvas.drawCircle(center, radius, Paint()..color = Colors.deepPurple.shade200..style = PaintingStyle.stroke..strokeWidth = 2);

    final halfRad = arcAngle * math.pi / 180 / 2;
    final startAngle = -math.pi / 2 - halfRad;
    final endAngle = -math.pi / 2 + halfRad;
    final p1 = center + Offset(math.cos(startAngle), math.sin(startAngle)) * radius;
    final p2 = center + Offset(math.cos(endAngle), math.sin(endAngle)) * radius;

    // Point on major arc, gliding between just past p2 and just before p1
    // (going the long way round), for the inscribed angle.
    final majorSpan = 2 * math.pi - arcAngle * math.pi / 180;
    final farAngle = endAngle + 0.15 * majorSpan / 2 + (majorSpan - 0.3 * majorSpan / 2 * 2) * farT;
    final p3 = center + Offset(math.cos(farAngle), math.sin(farAngle)) * radius;

    canvas.drawLine(center, p1, Paint()..color = Colors.red..strokeWidth = 2);
    canvas.drawLine(center, p2, Paint()..color = Colors.red..strokeWidth = 2);
    canvas.drawLine(p3, p1, Paint()..color = Colors.blue..strokeWidth = 2);
    canvas.drawLine(p3, p2, Paint()..color = Colors.blue..strokeWidth = 2);

    canvas.drawCircle(p1, 3, Paint()..color = Colors.black);
    canvas.drawCircle(p2, 3, Paint()..color = Colors.black);
    canvas.drawCircle(p3, 4, Paint()..color = Colors.blue.shade900);
    canvas.drawCircle(center, 3, Paint()..color = Colors.red.shade900);
  }

  @override
  bool shouldRepaint(covariant _CircleAnglePainter oldDelegate) => oldDelegate.arcAngle != arcAngle || oldDelegate.farT != farT;
}
