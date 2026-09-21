import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Three side-length sliders that attempt to draw a triangle: press play
/// to watch the apex rise up from the flat base into the final shape
/// (or fail to lift at all when the triangle inequality is broken),
/// making "sum of two sides > third side" concrete.
class TrianglesSimulationWidget extends StatefulWidget {
  const TrianglesSimulationWidget({super.key});

  @override
  State<TrianglesSimulationWidget> createState() => _TrianglesSimulationWidgetState();
}

class _TrianglesSimulationWidgetState extends State<TrianglesSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 5, _b = 6, _c = 7;
  late AnimationController _controller;

  bool get _isValid => (_a + _b > _c) && (_b + _c > _a) && (_c + _a > _b);

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 800));
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
    return SimFrame(
      title: 'Triangle Inequality',
      icon: Icons.change_history,
      accent: Colors.green.shade700,
      description: 'The sum of any two sides of a triangle must exceed the third — press play to watch the apex try to rise; try to break the rule and see it stay flat.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 160,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeOutBack.transform(_controller.value).clamp(0.0, 1.2);
                return CustomPaint(size: Size.infinite, painter: _TrianglePainter(a: _a, b: _b, c: _c, valid: _isValid, rise: eased));
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
              style: TextButton.styleFrom(foregroundColor: Colors.green.shade700),
            ),
          ),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(color: _isValid ? Colors.green.shade50 : Colors.red.shade50, borderRadius: BorderRadius.circular(8)),
            child: Text(
              _isValid ? 'Valid triangle: all three inequalities hold.' : 'Not a valid triangle — one side is too long!',
              style: TextStyle(color: _isValid ? Colors.green.shade800 : Colors.red.shade800, fontWeight: FontWeight.w600),
            ),
          ),
          const SizedBox(height: 14),
          SimSlider(label: 'Side a: ${_a.toStringAsFixed(0)}', value: _a, min: 1, max: 15, divisions: 14, activeColor: Colors.green, onChanged: (v) => setState(() { _a = v; _replay(); })),
          SimSlider(label: 'Side b: ${_b.toStringAsFixed(0)}', value: _b, min: 1, max: 15, divisions: 14, activeColor: Colors.teal, onChanged: (v) => setState(() { _b = v; _replay(); })),
          SimSlider(label: 'Side c: ${_c.toStringAsFixed(0)}', value: _c, min: 1, max: 15, divisions: 14, activeColor: Colors.indigo, onChanged: (v) => setState(() { _c = v; _replay(); })),
        ],
      ),
    );
  }
}

class _TrianglePainter extends CustomPainter {
  final double a, b, c;
  final bool valid;
  final double rise;
  _TrianglePainter({required this.a, required this.b, required this.c, required this.valid, this.rise = 1});

  @override
  void paint(Canvas canvas, Size size) {
    const scale = 8.0;
    final base = Offset(size.width * 0.15, size.height * 0.75);
    final baseWidth = (c * scale).clamp(20.0, size.width * 0.7);
    final baseEnd = Offset(base.dx + baseWidth, size.height * 0.75);

    Offset apex;
    if (valid) {
      // Law of cosines to place the apex above the base.
      final x = (a * a - b * b + baseWidth * baseWidth) / (2 * baseWidth);
      final ySq = (a * a - x * x).clamp(0.0, double.infinity);
      final y = _sqrtApprox(ySq);
      apex = Offset(base.dx + x, base.dy - y * scale);
    } else {
      apex = Offset((base.dx + baseEnd.dx) / 2, base.dy - 4);
    }

    // The apex rises up from the flat base line as `rise` goes 0 -> 1.
    final flatApex = Offset((base.dx + baseEnd.dx) / 2, base.dy);
    final animatedApex = Offset.lerp(flatApex, apex, rise.clamp(0.0, 1.0)) ?? apex;

    final path = Path()
      ..moveTo(base.dx, base.dy)
      ..lineTo(baseEnd.dx, baseEnd.dy)
      ..lineTo(animatedApex.dx, animatedApex.dy)
      ..close();
    canvas.drawPath(path, Paint()..color = (valid ? Colors.green.shade200 : Colors.red.shade200));
    canvas.drawPath(path, Paint()..color = (valid ? Colors.green.shade800 : Colors.red.shade800)..style = PaintingStyle.stroke..strokeWidth = 2);
  }

  double _sqrtApprox(double v) {
    double x = v, guess = v / 2 == 0 ? 1 : v / 2;
    for (int i = 0; i < 20; i++) {
      guess = 0.5 * (guess + x / guess);
    }
    return guess;
  }

  @override
  bool shouldRepaint(covariant _TrianglePainter oldDelegate) =>
      oldDelegate.a != a || oldDelegate.b != b || oldDelegate.c != c || oldDelegate.valid != valid || oldDelegate.rise != rise;
}
