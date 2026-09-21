import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A transversal crossing two parallel lines: press play to watch the
/// transversal sweep to its angle, updating all eight angles together
/// and highlighting which pairs stay equal (corresponding, alternate)
/// and which stay supplementary (co-interior).
class Class9LinesAnglesSimulationWidget extends StatefulWidget {
  const Class9LinesAnglesSimulationWidget({super.key});

  @override
  State<Class9LinesAnglesSimulationWidget> createState() => _Class9LinesAnglesSimulationWidgetState();
}

class _Class9LinesAnglesSimulationWidgetState extends State<Class9LinesAnglesSimulationWidget> with SingleTickerProviderStateMixin {
  double _angle = 60;
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

  void _sweep() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final coInterior = 180 - _angle;

    return SimFrame(
      title: 'Transversal & Parallel Lines',
      icon: Icons.grid_3x3,
      accent: Colors.pink.shade600,
      description: 'Change the angle and see how corresponding & alternate angles stay equal, while co-interior angles stay supplementary.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 190,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.pink.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                // Sweep the transversal in from vertical (90°) to its target angle.
                final animatedAngle = 90 + (_angle - 90) * eased;
                return CustomPaint(size: Size.infinite, painter: _TransversalPainter(angle: animatedAngle));
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: TextButton.icon(
              onPressed: _sweep,
              icon: Icon(Icons.replay, size: 18),
              label: Text(TrilingualService.instance.getUIText('Replay sweep')),
              style: TextButton.styleFrom(foregroundColor: Colors.pink.shade700),
            ),
          ),
          const SizedBox(height: 6),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Angle a', value: '${_angle.toStringAsFixed(0)}°', color: Colors.red),
            SimMetric(label: 'Corresponding', value: '${_angle.toStringAsFixed(0)}°', color: Colors.red),
            SimMetric(label: 'Co-interior', value: '${coInterior.toStringAsFixed(0)}°', color: Colors.blue),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Angle a: ${_angle.toStringAsFixed(0)}°', value: _angle, min: 10, max: 170, divisions: 32, activeColor: Colors.pink, onChanged: (v) => setState(() { _angle = v; _sweep(); })),
        ],
      ),
    );
  }
}

class _TransversalPainter extends CustomPainter {
  final double angle;
  _TransversalPainter({required this.angle});

  @override
  void paint(Canvas canvas, Size size) {
    final y1 = size.height * 0.3;
    final y2 = size.height * 0.7;
    final linePaint = Paint()
      ..color = Colors.pink.shade700
      ..strokeWidth = 2.5;
    canvas.drawLine(Offset(10, y1), Offset(size.width - 10, y1), linePaint);
    canvas.drawLine(Offset(10, y2), Offset(size.width - 10, y2), linePaint);

    final slopeOffset = (90 - angle) / 90 * (size.width * 0.3);
    final topX = size.width / 2 - slopeOffset;
    final botX = size.width / 2 + slopeOffset;
    canvas.drawLine(Offset(topX, 10), Offset(botX, size.height - 10), Paint()..color = Colors.blue.shade700..strokeWidth = 2.5);
  }

  @override
  bool shouldRepaint(covariant _TransversalPainter oldDelegate) => oldDelegate.angle != angle;
}
