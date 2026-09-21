import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Locates √n on the number line using the classic right-triangle
/// (Pythagoras) construction: press play to watch the hypotenuse
/// physically swing down like a compass arm and land on the number
/// line at exactly √n.
class NumberSystemsSimulationWidget extends StatefulWidget {
  const NumberSystemsSimulationWidget({super.key});

  @override
  State<NumberSystemsSimulationWidget> createState() => _NumberSystemsSimulationWidgetState();
}

class _NumberSystemsSimulationWidgetState extends State<NumberSystemsSimulationWidget> with SingleTickerProviderStateMixin {
  int _n = 2;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 1100));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _swing() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final sqrtN = math.sqrt(_n.toDouble());

    return SimFrame(
      title: 'Locating √n on the Number Line',
      icon: Icons.timeline,
      accent: Colors.indigo.shade600,
      description: 'A right triangle with legs 1 and √(n-1) has hypotenuse √n — press play to swing that hypotenuse down like a compass arm onto the number line at exactly √n.',
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
                final eased = Curves.easeInOut.transform(_controller.value);
                return CustomPaint(size: Size.infinite, painter: _SqrtPainter(n: _n, swing: eased));
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: ElevatedButton.icon(
              onPressed: _swing,
              icon: Icon(Icons.play_arrow),
              label: Text(TrilingualService.instance.getUIText('Swing arc')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.indigo.shade600, foregroundColor: Colors.white),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'n', value: '$_n'),
            SimMetric(label: '√n', value: sqrtN.toStringAsFixed(3), color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'n: $_n', value: _n.toDouble(), min: 2, max: 10, divisions: 8, activeColor: Colors.indigo, onChanged: (v) => setState(() { _n = v.round(); _swing(); })),
        ],
      ),
    );
  }
}

class _SqrtPainter extends CustomPainter {
  final int n;
  final double swing; // 0 = hypotenuse standing up, 1 = fully swung down onto the line
  _SqrtPainter({required this.n, this.swing = 1});

  @override
  void paint(Canvas canvas, Size size) {
    final scale = 30.0;
    final origin = Offset(30, size.height - 30);
    final lineEnd = Offset(size.width - 20, size.height - 30);
    canvas.drawLine(origin, lineEnd, Paint()..color = Colors.grey.shade600..strokeWidth = 1.5);

    for (int i = 0; i <= 10; i++) {
      final x = origin.dx + i * scale;
      canvas.drawLine(Offset(x, size.height - 34), Offset(x, size.height - 26), Paint()..color = Colors.grey.shade500);
    }

    final legB = math.sqrt((n - 1).toDouble().clamp(0, double.infinity));
    final vertex = Offset(origin.dx + scale, size.height - 30 - legB * scale);

    canvas.drawLine(origin + Offset(scale, 0), vertex, Paint()..color = Colors.teal.shade700..strokeWidth = 2.5);
    canvas.drawLine(origin, vertex, Paint()..color = Colors.deepOrange..strokeWidth = 2.5..style = PaintingStyle.stroke);

    final sqrtN = math.sqrt(n.toDouble());
    // The hypotenuse swings from standing at `vertex` down to lying flat
    // on the number line at distance sqrtN from origin.
    final startAngle = math.atan2(vertex.dy - origin.dy, vertex.dx - origin.dx);
    final endAngle = 0.0; // flat along the number line
    final currentAngle = startAngle + (endAngle - startAngle) * swing;
    final swingTip = origin + Offset(math.cos(currentAngle), math.sin(currentAngle)) * (sqrtN * scale);
    canvas.drawLine(origin, swingTip, Paint()..color = Colors.deepOrange..strokeWidth = 2.5);

    canvas.drawArc(Rect.fromCircle(center: origin, radius: sqrtN * scale), startAngle, (endAngle - startAngle) * swing, false, Paint()..color = Colors.deepOrange.withValues(alpha: 0.5)..style = PaintingStyle.stroke..strokeWidth = 1.5);

    final markerX = origin.dx + math.cos(currentAngle) * sqrtN * scale;
    final markerY = origin.dy + math.sin(currentAngle) * sqrtN * scale;
    canvas.drawCircle(Offset(markerX, markerY), 5, Paint()..color = Colors.red);
  }

  @override
  bool shouldRepaint(covariant _SqrtPainter oldDelegate) => oldDelegate.n != n || oldDelegate.swing != swing;
}
