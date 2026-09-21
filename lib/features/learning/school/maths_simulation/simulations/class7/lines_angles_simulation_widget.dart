import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// Two intersecting lines with a draggable angle: watch the vertically
/// opposite angle stay equal and the linear-pair neighbours always sum
/// to 180°, live. The tilted line animates smoothly to each new angle
/// instead of jumping, making the rotation itself part of the intuition.
class LinesAnglesSimulationWidget extends StatefulWidget {
  const LinesAnglesSimulationWidget({super.key});

  @override
  State<LinesAnglesSimulationWidget> createState() => _LinesAnglesSimulationWidgetState();
}

class _LinesAnglesSimulationWidgetState extends State<LinesAnglesSimulationWidget> with SingleTickerProviderStateMixin {
  double _angle = 50;
  double _prevAngle = 50;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 400));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final vertOpp = _angle;
    final linearPair = 180 - _angle;

    return SimFrame(
      title: 'Intersecting Lines & Angle Pairs',
      icon: Icons.close,
      accent: Colors.pink.shade600,
      description: 'Change one angle and see how vertically opposite angles stay equal, and linear-pair angles always sum to 180°.',
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
                final animAngle = _prevAngle + (_angle - _prevAngle) * eased;
                return CustomPaint(
                  size: Size.infinite,
                  painter: _AnglePainter(angleDeg: animAngle),
                );
              },
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Angle a', value: '${_angle.toStringAsFixed(0)}°', color: Colors.red),
            SimMetric(label: 'Vert. Opposite', value: '${vertOpp.toStringAsFixed(0)}°', color: Colors.red),
            SimMetric(label: 'Linear Pair', value: '${linearPair.toStringAsFixed(0)}°', color: Colors.blue),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Angle a: ${_angle.toStringAsFixed(0)}°',
            value: _angle,
            min: 10,
            max: 170,
            divisions: 32,
            activeColor: Colors.pink,
            onChanged: (val) => setState(() {
              _prevAngle = _angle;
              _angle = val;
              _controller.forward(from: 0);
            }),
          ),
        ],
      ),
    );
  }
}

class _AnglePainter extends CustomPainter {
  final double angleDeg;

  _AnglePainter({required this.angleDeg});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final len = 90.0;
    final rad = angleDeg * math.pi / 180;

    final dirA = Offset(math.cos(rad), -math.sin(rad));
    final dirB = Offset(-math.cos(rad), math.sin(rad));
    final dirC = Offset(-math.cos(math.pi - rad), -math.sin(math.pi - rad));
    final dirD = -dirC;

    final linePaint = Paint()
      ..color = Colors.pink.shade700
      ..strokeWidth = 2.5;
    canvas.drawLine(center - dirA * len, center + dirA * len, linePaint);
    canvas.drawLine(center - dirC * len, center + dirC * len, Paint()..color = Colors.blue.shade700..strokeWidth = 2.5);

    _label(canvas, center + dirA * (len + 14), 'a', Colors.red);
    _label(canvas, center + dirB * (len + 14), 'a', Colors.red);
    _label(canvas, center + dirC * (len + 14), 'b', Colors.blue);
    _label(canvas, center + dirD * (len + 14), 'b', Colors.blue);
  }

  void _label(Canvas canvas, Offset pos, String text, Color color) {
    final tp = TextPainter(text: TextSpan(text: text, style: TextStyle(color: color, fontWeight: FontWeight.bold, fontSize: 13)), textDirection: TextDirection.ltr)..layout();
    tp.paint(canvas, pos - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(covariant _AnglePainter oldDelegate) => true;
}
