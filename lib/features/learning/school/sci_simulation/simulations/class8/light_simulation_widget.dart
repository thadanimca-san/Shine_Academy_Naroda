import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A mirror reflection demo: drag the angle-of-incidence slider and watch
/// the reflected ray obey the law of reflection — angle of incidence
/// always equals angle of reflection.
class LightSimulationWidget extends StatefulWidget {
  const LightSimulationWidget({super.key});

  @override
  State<LightSimulationWidget> createState() => _LightSimulationWidgetState();
}

class _LightSimulationWidgetState extends State<LightSimulationWidget> {
  double _angleDeg = 40;

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Reflection of Light',
      icon: Icons.wb_sunny,
      accent: Colors.orange.shade700,
      description: 'The angle of incidence always equals the angle of reflection, both measured from the normal.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 200,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.blueGrey.shade900, borderRadius: BorderRadius.circular(10)),
            child: CustomPaint(
              size: Size.infinite,
              painter: _MirrorPainter(angleDeg: _angleDeg),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Angle of Incidence', value: '${_angleDeg.toStringAsFixed(0)}°', color: Colors.orange),
            SimMetric(label: 'Angle of Reflection', value: '${_angleDeg.toStringAsFixed(0)}°', color: Colors.lightBlue),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Angle of incidence: ${_angleDeg.toStringAsFixed(0)}°',
            value: _angleDeg,
            min: 5,
            max: 80,
            divisions: 15,
            activeColor: Colors.orange,
            onChanged: (val) => setState(() => _angleDeg = val),
          ),
        ],
      ),
    );
  }
}

class _MirrorPainter extends CustomPainter {
  final double angleDeg;

  _MirrorPainter({required this.angleDeg});

  @override
  void paint(Canvas canvas, Size size) {
    final origin = Offset(size.width / 2, size.height - 20);
    final mirrorPaint = Paint()
      ..color = Colors.lightBlueAccent
      ..strokeWidth = 4;
    canvas.drawLine(Offset(0, origin.dy), Offset(size.width, origin.dy), mirrorPaint);

    final normalPaint = Paint()
      ..color = Colors.white54
      ..strokeWidth = 1.2;
    canvas.drawLine(origin, Offset(origin.dx, 10), normalPaint);

    final angleRad = angleDeg * math.pi / 180;
    final rayLength = size.height - 40;

    final incidentStart = origin + Offset(-math.sin(angleRad) * rayLength, -math.cos(angleRad) * rayLength);
    canvas.drawLine(incidentStart, origin, Paint()..color = Colors.orangeAccent..strokeWidth = 2.5);
    _arrowHead(canvas, incidentStart, origin, Colors.orangeAccent);

    final reflectedEnd = origin + Offset(math.sin(angleRad) * rayLength, -math.cos(angleRad) * rayLength);
    canvas.drawLine(origin, reflectedEnd, Paint()..color = Colors.greenAccent..strokeWidth = 2.5);
    _arrowHead(canvas, origin, reflectedEnd, Colors.greenAccent);

    final textPainter = TextPainter(
      text: const TextSpan(text: 'Mirror', style: TextStyle(color: Colors.white70, fontSize: 11)),
      textDirection: TextDirection.ltr,
    )..layout();
    textPainter.paint(canvas, Offset(8, origin.dy + 4));
  }

  void _arrowHead(Canvas canvas, Offset from, Offset to, Color color) {
    final dir = (to - from);
    final len = dir.distance;
    if (len == 0) return;
    final unit = dir / len;
    final normal = Offset(-unit.dy, unit.dx);
    final tip = to;
    final left = tip - unit * 10 + normal * 5;
    final right = tip - unit * 10 - normal * 5;
    final path = Path()
      ..moveTo(tip.dx, tip.dy)
      ..lineTo(left.dx, left.dy)
      ..lineTo(right.dx, right.dy)
      ..close();
    canvas.drawPath(path, Paint()..color = color);
  }

  @override
  bool shouldRepaint(covariant _MirrorPainter oldDelegate) => oldDelegate.angleDeg != angleDeg;
}
