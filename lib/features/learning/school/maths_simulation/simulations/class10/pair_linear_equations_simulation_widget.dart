import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Two lines drawn from sliders a₁,b₁,c₁ and a₂,b₂,c₂: each line draws
/// itself outward from the centre whenever a value changes, so you can
/// watch them intersect, run parallel, or coincide, with the
/// classification (unique solution / no solution / infinite solutions)
/// updating live.
class PairLinearEquationsSimulationWidget extends StatefulWidget {
  const PairLinearEquationsSimulationWidget({super.key});

  @override
  State<PairLinearEquationsSimulationWidget> createState() => _PairLinearEquationsSimulationWidgetState();
}

class _PairLinearEquationsSimulationWidgetState extends State<PairLinearEquationsSimulationWidget> with SingleTickerProviderStateMixin {
  double _a1 = 1, _b1 = 1, _c1 = -4;
  double _a2 = 1, _b2 = -1, _c2 = 0;
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

  String get _classification {
    final cross1 = _a1 * _b2 - _a2 * _b1;
    if (cross1 != 0) return 'Unique solution (lines intersect)';
    final cross2 = _b1 * _c2 - _b2 * _c1;
    if (cross2 != 0) return 'No solution (parallel lines)';
    return 'Infinitely many solutions (coincident lines)';
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Pair of Linear Equations',
      icon: Icons.timeline,
      accent: Colors.blue.shade700,
      description: 'Adjust both equations and watch each line draw itself out from the centre — see whether they intersect, are parallel, or coincide.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 180,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.blue.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeOutCubic.transform(_controller.value);
                return CustomPaint(
                  size: Size.infinite,
                  painter: _TwoLinesPainter(a1: _a1, b1: _b1, c1: _c1, a2: _a2, b2: _b2, c2: _c2, drawT: eased),
                );
              },
            ),
          ),
          const SizedBox(height: 10),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(color: Colors.blue.shade50, borderRadius: BorderRadius.circular(8)),
            child: Text(_classification, style: TextStyle(fontWeight: FontWeight.bold, color: Colors.blue.shade800), textAlign: TextAlign.center),
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText('Line 1'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
          SimSlider(label: 'a₁: ${_a1.toStringAsFixed(0)}', value: _a1, min: -3, max: 3, divisions: 6, activeColor: Colors.red, onChanged: (v) => setState(() { _a1 = v; _replay(); })),
          SimSlider(label: 'b₁: ${_b1.toStringAsFixed(0)}', value: _b1, min: -3, max: 3, divisions: 6, activeColor: Colors.red, onChanged: (v) => setState(() { _b1 = v; _replay(); })),
          SimSlider(label: 'c₁: ${_c1.toStringAsFixed(0)}', value: _c1, min: -8, max: 8, divisions: 16, activeColor: Colors.red, onChanged: (v) => setState(() { _c1 = v; _replay(); })),
          const SizedBox(height: 8),
          Text(TrilingualService.instance.getUIText('Line 2'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
          SimSlider(label: 'a₂: ${_a2.toStringAsFixed(0)}', value: _a2, min: -3, max: 3, divisions: 6, activeColor: Colors.blue, onChanged: (v) => setState(() { _a2 = v; _replay(); })),
          SimSlider(label: 'b₂: ${_b2.toStringAsFixed(0)}', value: _b2, min: -3, max: 3, divisions: 6, activeColor: Colors.blue, onChanged: (v) => setState(() { _b2 = v; _replay(); })),
          SimSlider(label: 'c₂: ${_c2.toStringAsFixed(0)}', value: _c2, min: -8, max: 8, divisions: 16, activeColor: Colors.blue, onChanged: (v) => setState(() { _c2 = v; _replay(); })),
        ],
      ),
    );
  }
}

class _TwoLinesPainter extends CustomPainter {
  final double a1, b1, c1, a2, b2, c2, drawT;
  _TwoLinesPainter({
    required this.a1,
    required this.b1,
    required this.c1,
    required this.a2,
    required this.b2,
    required this.c2,
    required this.drawT,
  });

  @override
  void paint(Canvas canvas, Size size) {
    _drawLine(canvas, size, a1, b1, c1, Colors.red);
    _drawLine(canvas, size, a2, b2, c2, Colors.blue);
  }

  void _drawLine(Canvas canvas, Size size, double a, double b, double c, Color color) {
    final safeB = b == 0 ? 0.001 : b;
    Offset pointAt(double x) => Offset(x, (-a * x - c) / safeB);

    final x1 = -10.0, x2 = 10.0;
    final p1 = pointAt(x1);
    final p2 = pointAt(x2);
    final mid = Offset.lerp(p1, p2, 0.5)!;

    Offset toScreen(Offset p) => Offset((p.dx + 10) / 20 * size.width, size.height - (p.dy + 10) / 20 * size.height);

    // Draw the line growing outward from its midpoint in both directions.
    final drawnStart = Offset.lerp(mid, p1, drawT)!;
    final drawnEnd = Offset.lerp(mid, p2, drawT)!;

    canvas.drawLine(toScreen(drawnStart), toScreen(drawnEnd), Paint()..color = color..strokeWidth = 2.5);
  }

  @override
  bool shouldRepaint(covariant _TwoLinesPainter oldDelegate) => true;
}
