import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Three side-length sliders feed Heron's formula live: the triangle is
/// drawn to scale and its interior fills in with a growth animation each
/// time the sides change, tying the numeric area to the visible shape.
class HeronsFormulaSimulationWidget extends StatefulWidget {
  const HeronsFormulaSimulationWidget({super.key});

  @override
  State<HeronsFormulaSimulationWidget> createState() => _HeronsFormulaSimulationWidgetState();
}

class _HeronsFormulaSimulationWidgetState extends State<HeronsFormulaSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 5, _b = 6, _c = 7;
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

  void _replay() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final s = (_a + _b + _c) / 2;
    final valid = s > _a && s > _b && s > _c;
    final areaSq = valid ? s * (s - _a) * (s - _b) * (s - _c) : 0.0;
    final area = math.sqrt(areaSq.clamp(0, double.infinity));

    return SimFrame(
      title: "Heron's Formula",
      icon: Icons.calculate,
      accent: Colors.teal.shade600,
      description: 'Change the three sides and watch the triangle fill in and the semi-perimeter and area update — no height needed.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 140,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.teal.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeOutBack.transform(_controller.value).clamp(0.0, 1.0);
                return CustomPaint(size: Size.infinite, painter: _HeronTrianglePainter(a: _a, b: _b, c: _c, valid: valid, fill: eased));
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: TextButton.icon(
              onPressed: _replay,
              icon: Icon(Icons.replay, size: 18),
              label: Text(TrilingualService.instance.getUIText('Replay')),
              style: TextButton.styleFrom(foregroundColor: Colors.teal.shade700),
            ),
          ),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: Colors.teal.shade50, borderRadius: BorderRadius.circular(10)),
            child: Column(
              children: [
                Text('s = (a+b+c)/2 = ${s.toStringAsFixed(1)}', style: TextStyle(fontSize: 13)),
                const SizedBox(height: 6),
                Text(
                  valid ? 'Area = √[s(s−a)(s−b)(s−c)] = ${area.toStringAsFixed(2)} units²' : 'Not a valid triangle for these sides!',
                  style: TextStyle(fontSize: 13, fontWeight: FontWeight.bold, color: valid ? Colors.teal.shade800 : Colors.red.shade700),
                  textAlign: TextAlign.center,
                ),
              ],
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'a', value: _a.toStringAsFixed(0)),
            SimMetric(label: 'b', value: _b.toStringAsFixed(0)),
            SimMetric(label: 'c', value: _c.toStringAsFixed(0)),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Side a: ${_a.toStringAsFixed(0)}', value: _a, min: 1, max: 15, divisions: 14, activeColor: Colors.teal, onChanged: (v) => setState(() { _a = v; _replay(); })),
          SimSlider(label: 'Side b: ${_b.toStringAsFixed(0)}', value: _b, min: 1, max: 15, divisions: 14, activeColor: Colors.blue, onChanged: (v) => setState(() { _b = v; _replay(); })),
          SimSlider(label: 'Side c: ${_c.toStringAsFixed(0)}', value: _c, min: 1, max: 15, divisions: 14, activeColor: Colors.indigo, onChanged: (v) => setState(() { _c = v; _replay(); })),
        ],
      ),
    );
  }
}

class _HeronTrianglePainter extends CustomPainter {
  final double a, b, c;
  final bool valid;
  final double fill;
  _HeronTrianglePainter({required this.a, required this.b, required this.c, required this.valid, required this.fill});

  @override
  void paint(Canvas canvas, Size size) {
    if (!valid) return;
    const scale = 7.0;
    final base = Offset(size.width * 0.5 - (c * scale) / 2, size.height * 0.8);
    final baseWidth = (c * scale).clamp(20.0, size.width * 0.7);
    final baseEnd = Offset(base.dx + baseWidth, base.dy);

    final x = (a * a - b * b + baseWidth * baseWidth) / (2 * baseWidth);
    final ySq = (a * a - x * x).clamp(0.0, double.infinity);
    final y = math.sqrt(ySq);
    final apex = Offset(base.dx + x, base.dy - y * scale);

    // Apex grows up from the base line as fill goes 0 -> 1.
    final animatedApex = Offset.lerp(Offset(apex.dx, base.dy), apex, fill) ?? apex;

    final path = Path()
      ..moveTo(base.dx, base.dy)
      ..lineTo(baseEnd.dx, baseEnd.dy)
      ..lineTo(animatedApex.dx, animatedApex.dy)
      ..close();
    canvas.drawPath(path, Paint()..color = Colors.teal.withValues(alpha: 0.35 * fill));
    canvas.drawPath(path, Paint()..color = Colors.teal.shade800..style = PaintingStyle.stroke..strokeWidth = 2);
  }

  @override
  bool shouldRepaint(covariant _HeronTrianglePainter oldDelegate) =>
      oldDelegate.a != a || oldDelegate.b != b || oldDelegate.c != c || oldDelegate.valid != valid || oldDelegate.fill != fill;
}
