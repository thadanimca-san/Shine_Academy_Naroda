import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A triangle and parallelogram sharing the same base and lying between
/// the same two parallel lines: press play to watch the apex glide back
/// and forth across the top parallel while both areas stay exactly
/// constant, or drag the slider to explore any single position.
class AreasParallelogramsTrianglesSimulationWidget extends StatefulWidget {
  const AreasParallelogramsTrianglesSimulationWidget({super.key});

  @override
  State<AreasParallelogramsTrianglesSimulationWidget> createState() => _AreasParallelogramsTrianglesSimulationWidgetState();
}

class _AreasParallelogramsTrianglesSimulationWidgetState extends State<AreasParallelogramsTrianglesSimulationWidget> with SingleTickerProviderStateMixin {
  double _shift = 0.3;
  final double _base = 6;
  final double _height = 4;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 1600));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _play() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final triangleArea = 0.5 * _base * _height;
    final parallelogramArea = _base * _height;

    return SimFrame(
      title: 'Same Base, Same Parallels',
      icon: Icons.compare_arrows,
      accent: Colors.teal.shade600,
      description: 'Press play to slide the apex along the top parallel — the triangle stays on the same base, between the same parallels — its area never changes.',
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
                // Sweep the apex from 0 to 1 and back to 0 across the animation.
                final t = _controller.value;
                final eased = Curves.easeInOut.transform(t);
                final sweep = eased < 0.5 ? eased * 2 : (1 - eased) * 2;
                final animatedShift = _controller.isAnimating || _controller.isCompleted ? sweep : _shift;
                return CustomPaint(size: Size.infinite, painter: _SameBasePainter(shift: _controller.value == 0 ? _shift : animatedShift));
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: ElevatedButton.icon(
              onPressed: _play,
              icon: Icon(Icons.play_arrow),
              label: Text(TrilingualService.instance.getUIText('Slide apex')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.teal.shade600, foregroundColor: Colors.white),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Triangle Area', value: '${triangleArea.toStringAsFixed(0)} units²', color: Colors.deepOrange),
            SimMetric(label: 'Parallelogram Area', value: '${parallelogramArea.toStringAsFixed(0)} units²', color: Colors.blue),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Apex position (area stays constant!)', value: _shift, min: 0, max: 1, divisions: 20, activeColor: Colors.teal, onChanged: (v) => setState(() { _shift = v; _controller.value = 0; })),
        ],
      ),
    );
  }
}

class _SameBasePainter extends CustomPainter {
  final double shift;
  _SameBasePainter({required this.shift});

  @override
  void paint(Canvas canvas, Size size) {
    final topY = size.height * 0.2;
    final baseY = size.height * 0.8;
    canvas.drawLine(Offset(10, topY), Offset(size.width - 10, topY), Paint()..color = Colors.grey.shade400..strokeWidth = 1.5);
    canvas.drawLine(Offset(10, baseY), Offset(size.width - 10, baseY), Paint()..color = Colors.grey.shade400..strokeWidth = 1.5);

    final b = Offset(size.width * 0.3, baseY);
    final c = Offset(size.width * 0.7, baseY);
    final apexX = size.width * (0.15 + shift * 0.7);
    final apex = Offset(apexX, topY);

    final path = Path()
      ..moveTo(b.dx, b.dy)
      ..lineTo(c.dx, c.dy)
      ..lineTo(apex.dx, apex.dy)
      ..close();
    canvas.drawPath(path, Paint()..color = Colors.deepOrange.withValues(alpha: 0.4));
    canvas.drawPath(path, Paint()..color = Colors.deepOrange.shade800..style = PaintingStyle.stroke..strokeWidth = 2);
  }

  @override
  bool shouldRepaint(covariant _SameBasePainter oldDelegate) => oldDelegate.shift != shift;
}
