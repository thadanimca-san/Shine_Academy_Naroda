import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A right triangle with an adjustable angle θ: watch sin, cos and tan
/// recompute live as the triangle's shape changes, and press play to see
/// the angle sweep open from 0 up to θ.
class TrigonometrySimulationWidget extends StatefulWidget {
  const TrigonometrySimulationWidget({super.key});

  @override
  State<TrigonometrySimulationWidget> createState() => _TrigonometrySimulationWidgetState();
}

class _TrigonometrySimulationWidgetState extends State<TrigonometrySimulationWidget> with SingleTickerProviderStateMixin {
  double _angleDeg = 40;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 900));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _sweep() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final rad = _angleDeg * math.pi / 180;
    final sinV = math.sin(rad);
    final cosV = math.cos(rad);
    final tanV = math.tan(rad);

    return SimFrame(
      title: 'Trigonometric Ratios',
      icon: Icons.change_history,
      accent: Colors.teal.shade600,
      description: 'Slide the angle θ and watch sin, cos and tan update live, or press play to sweep the angle open.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.teal.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                final animatedAngle = _angleDeg * eased;
                return CustomPaint(size: Size.infinite, painter: _RightTrianglePainter(angleDeg: animatedAngle, fullAngleDeg: _angleDeg));
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: ElevatedButton.icon(
              onPressed: _sweep,
              icon: Icon(Icons.play_arrow),
              label: Text(TrilingualService.instance.getUIText('Sweep angle')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.teal.shade600, foregroundColor: Colors.white),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'sin θ', value: sinV.toStringAsFixed(3), color: Colors.blue),
            SimMetric(label: 'cos θ', value: cosV.toStringAsFixed(3), color: Colors.teal),
            SimMetric(label: 'tan θ', value: tanV.abs() > 100 ? '∞' : tanV.toStringAsFixed(3), color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'θ: ${_angleDeg.toStringAsFixed(0)}°', value: _angleDeg, min: 5, max: 85, divisions: 16, activeColor: Colors.teal, onChanged: (v) => setState(() { _angleDeg = v; _controller.value = 1; })),
        ],
      ),
    );
  }
}

class _RightTrianglePainter extends CustomPainter {
  final double angleDeg;
  final double fullAngleDeg;
  _RightTrianglePainter({required this.angleDeg, required this.fullAngleDeg});

  @override
  void paint(Canvas canvas, Size size) {
    final origin = Offset(30, size.height - 20);
    final hyp = 130.0;
    final rad = angleDeg * math.pi / 180;
    final top = origin + Offset(math.cos(rad) * hyp, -math.sin(rad) * hyp);
    final right = Offset(top.dx, origin.dy);
    final baseEnd = origin + const Offset(160, 0);

    final paint = Paint()
      ..color = Colors.teal.shade800
      ..strokeWidth = 2.5;
    canvas.drawLine(origin, baseEnd, paint);
    canvas.drawLine(right, top, paint);
    canvas.drawLine(origin, top, Paint()..color = Colors.deepOrange..strokeWidth = 2.5);

    canvas.drawRect(Rect.fromLTWH(right.dx - 10, right.dy - 10, 10, 10), Paint()..color = Colors.black45..style = PaintingStyle.stroke);

    // Traced arc showing the angle sweeping open at the origin.
    final arcRect = Rect.fromCircle(center: origin, radius: 28);
    canvas.drawArc(arcRect, -rad, rad, false, Paint()..color = Colors.teal.shade700..strokeWidth = 2..style = PaintingStyle.stroke);

    final tp = TextPainter(
      text: TextSpan(text: '${angleDeg.round()}°', style: TextStyle(fontSize: 11, color: Colors.teal.shade900, fontWeight: FontWeight.bold)),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, origin + const Offset(34, -18));
  }

  @override
  bool shouldRepaint(covariant _RightTrianglePainter oldDelegate) => oldDelegate.angleDeg != angleDeg;
}
