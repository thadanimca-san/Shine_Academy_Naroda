import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// An animated flame whose shape and colour respond to an oxygen-supply
/// slider: plenty of oxygen gives a clean blue flame (complete combustion);
/// starving it of oxygen gives a yellow, sooty flame (incomplete combustion).
class CombustionFlameSimulationWidget extends StatefulWidget {
  const CombustionFlameSimulationWidget({super.key});

  @override
  State<CombustionFlameSimulationWidget> createState() => _CombustionFlameSimulationWidgetState();
}

class _CombustionFlameSimulationWidgetState extends State<CombustionFlameSimulationWidget> with SingleTickerProviderStateMixin {
  double _oxygenSupply = 0.3; // 0 = starved, 1 = plenty
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 900))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  bool get _isComplete => _oxygenSupply > 0.55;

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Combustion & Flame',
      icon: Icons.local_fire_department,
      accent: Colors.deepOrange,
      description: 'Adjust the oxygen supply to see the difference between complete (blue, clean) and incomplete (yellow, sooty) combustion.',
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                height: 200,
                width: double.infinity,
                decoration: BoxDecoration(color: Colors.grey.shade900, borderRadius: BorderRadius.circular(10)),
                child: CustomPaint(
                  size: Size.infinite,
                  painter: _FlamePainter(t: _controller.value, oxygen: _oxygenSupply),
                ),
              ),
              const SizedBox(height: 12),
              SimMetricPanel(metrics: [
                SimMetric(label: 'Combustion Type', value: _isComplete ? 'Complete' : 'Incomplete', color: _isComplete ? Colors.blue : Colors.deepOrange),
                SimMetric(label: 'Product', value: _isComplete ? 'CO₂ + H₂O' : 'CO + soot', color: Colors.grey.shade700),
              ]),
              const SizedBox(height: 14),
              SimSlider(
                label: 'Oxygen supply: ${(_oxygenSupply * 100).toStringAsFixed(0)}%',
                value: _oxygenSupply,
                min: 0.05,
                max: 1.0,
                divisions: 19,
                activeColor: Colors.deepOrange,
                onChanged: (val) => setState(() => _oxygenSupply = val),
              ),
            ],
          );
        },
      ),
    );
  }
}

class _FlamePainter extends CustomPainter {
  final double t;
  final double oxygen;

  _FlamePainter({required this.t, required this.oxygen});

  @override
  void paint(Canvas canvas, Size size) {
    final base = Offset(size.width / 2, size.height - 20);
    final flicker = math.sin(t * 2 * math.pi) * 6;

    // Outer flame
    final outerColor = Color.lerp(const Color(0xFFFF7043), const Color(0xFF64B5F6), oxygen)!;
    final outerPath = _flamePath(base, 150 + flicker, 55, size.height);
    canvas.drawPath(outerPath, Paint()..color = outerColor.withValues(alpha: 0.9));

    // Middle flame
    final midColor = Color.lerp(const Color(0xFFFFCA28), const Color(0xFF90CAF9), oxygen)!;
    final midPath = _flamePath(base, 110 - flicker, 38, size.height);
    canvas.drawPath(midPath, Paint()..color = midColor.withValues(alpha: 0.9));

    // Inner dark zone (more prominent when oxygen is low = incomplete combustion / unburnt fuel)
    final innerHeight = 60 + (1 - oxygen) * 30;
    final innerPath = _flamePath(base, innerHeight, 18, size.height);
    canvas.drawPath(innerPath, Paint()..color = Colors.black.withValues(alpha: 0.55));

    // Soot particles when oxygen is low
    if (oxygen < 0.5) {
      final sootPaint = Paint()..color = Colors.black.withValues(alpha: 0.6);
      for (int i = 0; i < 6; i++) {
        final x = base.dx + math.sin(t * 2 * math.pi + i) * 20;
        final y = base.dy - 160 - i * 8 - (t * 10);
        canvas.drawCircle(Offset(x, y), 2.5, sootPaint);
      }
    }

    // Wick / fuel source
    canvas.drawRect(Rect.fromCenter(center: base + const Offset(0, 6), width: 8, height: 14), Paint()..color = Colors.grey.shade400);
  }

  Path _flamePath(Offset base, double height, double width, double maxHeight) {
    final tip = base - Offset(0, height.clamp(10, maxHeight - 20));
    final path = Path();
    path.moveTo(base.dx - width / 2, base.dy);
    path.quadraticBezierTo(base.dx - width, base.dy - height * 0.5, tip.dx, tip.dy);
    path.quadraticBezierTo(base.dx + width, base.dy - height * 0.5, base.dx + width / 2, base.dy);
    path.close();
    return path;
  }

  @override
  bool shouldRepaint(covariant _FlamePainter oldDelegate) => true;
}
