import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// The Basic Proportionality Theorem, live: slide line DE up and down
/// inside triangle ABC (always parallel to BC) and watch it glide smoothly
/// to its new position while AD/DB stays exactly equal to AE/EC.
class Class10TrianglesSimulationWidget extends StatefulWidget {
  const Class10TrianglesSimulationWidget({super.key});

  @override
  State<Class10TrianglesSimulationWidget> createState() => _Class10TrianglesSimulationWidgetState();
}

class _Class10TrianglesSimulationWidgetState extends State<Class10TrianglesSimulationWidget> with SingleTickerProviderStateMixin {
  double _t = 0.5; // fraction along AB/AC from A
  double _fromT = 0.5;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 450));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _slideTo(double newT) {
    _fromT = _t;
    _t = newT;
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    final ratio = _t / (1 - _t);

    return SimFrame(
      title: 'Basic Proportionality Theorem',
      icon: Icons.change_history,
      accent: Colors.green.shade700,
      description: 'DE is always parallel to BC. Slide it and watch it glide to its new position while AD/DB stays equal to AE/EC.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 180,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                final animatedT = _fromT + (_t - _fromT) * eased;
                return CustomPaint(size: Size.infinite, painter: _BPTPainter(t: animatedT));
              },
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'AD/DB', value: ratio.toStringAsFixed(2), color: Colors.blue),
            SimMetric(label: 'AE/EC', value: ratio.toStringAsFixed(2), color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Position of DE along AB/AC', value: _t, min: 0.15, max: 0.85, divisions: 14, activeColor: Colors.green, onChanged: (v) => setState(() => _slideTo(v))),
        ],
      ),
    );
  }
}

class _BPTPainter extends CustomPainter {
  final double t;
  _BPTPainter({required this.t});

  @override
  void paint(Canvas canvas, Size size) {
    final a = Offset(size.width * 0.5, size.height * 0.1);
    final b = Offset(size.width * 0.15, size.height * 0.9);
    final c = Offset(size.width * 0.85, size.height * 0.9);

    final trianglePaint = Paint()
      ..color = Colors.green.shade800
      ..strokeWidth = 2;
    canvas.drawLine(a, b, trianglePaint);
    canvas.drawLine(a, c, trianglePaint);
    canvas.drawLine(b, c, trianglePaint);

    final d = Offset.lerp(a, b, t)!;
    final e = Offset.lerp(a, c, t)!;
    canvas.drawLine(d, e, Paint()..color = Colors.deepOrange..strokeWidth = 3);
    canvas.drawCircle(d, 4, Paint()..color = Colors.deepOrange);
    canvas.drawCircle(e, 4, Paint()..color = Colors.deepOrange);

    _label(canvas, a + const Offset(-6, -14), 'A');
    _label(canvas, b + const Offset(-14, 4), 'B');
    _label(canvas, c + const Offset(6, 4), 'C');
    _label(canvas, d + const Offset(-16, 0), 'D');
    _label(canvas, e + const Offset(6, 0), 'E');
  }

  void _label(Canvas canvas, Offset pos, String text) {
    final tp = TextPainter(text: TextSpan(text: text, style: TextStyle(color: Colors.black87, fontWeight: FontWeight.bold, fontSize: 12)), textDirection: TextDirection.ltr)..layout();
    tp.paint(canvas, pos);
  }

  @override
  bool shouldRepaint(covariant _BPTPainter oldDelegate) => oldDelegate.t != t;
}
