import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A pie-slice sector whose angle you control: the sector sweeps open
/// from 0° to θ whenever you move the slider, and the sector area and
/// arc length scale as a fraction of the full circle.
class AreasRelatedCirclesSimulationWidget extends StatefulWidget {
  const AreasRelatedCirclesSimulationWidget({super.key});

  @override
  State<AreasRelatedCirclesSimulationWidget> createState() => _AreasRelatedCirclesSimulationWidgetState();
}

class _AreasRelatedCirclesSimulationWidgetState extends State<AreasRelatedCirclesSimulationWidget> with SingleTickerProviderStateMixin {
  final double _radius = 7;
  double _angle = 90;
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
    const pi = 3.14159265;
    final sectorArea = (_angle / 360) * pi * _radius * _radius;
    final arcLength = (_angle / 360) * 2 * pi * _radius;

    return SimFrame(
      title: 'Sector Area & Arc Length',
      icon: Icons.pie_chart_outline,
      accent: Colors.pink.shade600,
      description: 'Slide the central angle and watch the sector sweep open — its area and arc length scale as a fraction of the full circle.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.pink.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeOutCubic.transform(_controller.value);
                return CustomPaint(size: Size.infinite, painter: _SectorPainter(angle: _angle * eased));
              },
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Angle θ', value: '${_angle.toStringAsFixed(0)}°'),
            SimMetric(label: 'Sector Area', value: '${sectorArea.toStringAsFixed(1)} u²', color: Colors.deepOrange),
            SimMetric(label: 'Arc Length', value: '${arcLength.toStringAsFixed(1)} u', color: Colors.teal),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Central angle θ: ${_angle.toStringAsFixed(0)}°',
            value: _angle,
            min: 10,
            max: 350,
            divisions: 34,
            activeColor: Colors.pink,
            onChanged: (v) => setState(() {
              _angle = v;
              _controller.forward(from: 0);
            }),
          ),
        ],
      ),
    );
  }
}

class _SectorPainter extends CustomPainter {
  final double angle;
  _SectorPainter({required this.angle});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final radius = size.height / 2 - 10;
    canvas.drawCircle(center, radius, Paint()..color = Colors.pink.shade100);
    final sweepRad = angle * 3.14159265 / 180;
    canvas.drawArc(Rect.fromCircle(center: center, radius: radius), -1.5708, sweepRad, true, Paint()..color = Colors.pink.shade400);
    canvas.drawCircle(center, radius, Paint()..color = Colors.pink.shade700..style = PaintingStyle.stroke..strokeWidth = 1.5);
  }

  @override
  bool shouldRepaint(covariant _SectorPainter oldDelegate) => oldDelegate.angle != angle;
}
