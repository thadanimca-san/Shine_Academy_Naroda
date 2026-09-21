import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A visual for a² − b² = (a+b)(a−b): press play and watch the a×a square
/// have its b×b corner cut away, then the remaining L-shape crossfade into
/// an (a+b)×(a−b) rectangle of equal area.
class FactorisationSimulationWidget extends StatefulWidget {
  const FactorisationSimulationWidget({super.key});

  @override
  State<FactorisationSimulationWidget> createState() => _FactorisationSimulationWidgetState();
}

class _FactorisationSimulationWidgetState extends State<FactorisationSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 6;
  double _b = 3;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 1200));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _play() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final aSqMinusBSq = _a * _a - _b * _b;
    final rectArea = (_a + _b) * (_a - _b);

    return SimFrame(
      title: 'a² − b² = (a+b)(a−b)',
      icon: Icons.crop_free,
      accent: Colors.teal.shade600,
      description: 'Press play: the b² corner is cut from the a² square, then the L-shape rearranges into an (a+b) by (a−b) rectangle.',
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
                final t = _controller.value;
                // First half: L-shape fades out. Second half: rectangle fades in.
                final lShapeOpacity = (1 - (t / 0.5)).clamp(0.0, 1.0);
                final rectT = Curves.easeOutBack.transform(((t - 0.5) / 0.5).clamp(0.0, 1.0));
                return Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  crossAxisAlignment: CrossAxisAlignment.center,
                  children: [
                    Opacity(
                      opacity: lShapeOpacity,
                      child: CustomPaint(size: Size(_a * 12 + 10, _a * 12 + 10), painter: _LShapePainter(a: _a, b: _b)),
                    ),
                    Opacity(
                      opacity: rectT.clamp(0.0, 1.0),
                      child: Transform.scale(
                        scale: 0.6 + 0.4 * rectT.clamp(0.0, 1.0),
                        child: Container(
                          width: (_a + _b) * 8,
                          height: (_a - _b) * 8 + 4,
                          color: Colors.teal.shade400,
                          alignment: Alignment.center,
                          child: FittedBox(child: Text(TrilingualService.instance.getUIText('(a+b)×(a−b)'), style: TextStyle(color: Colors.white, fontSize: 10))),
                        ),
                      ),
                    ),
                  ],
                );
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: ElevatedButton.icon(
              onPressed: _play,
              icon: Icon(Icons.play_arrow),
              label: Text(TrilingualService.instance.getUIText('Play transformation')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.teal.shade600, foregroundColor: Colors.white),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'a² − b²', value: aSqMinusBSq.toStringAsFixed(0), color: Colors.teal),
            SimMetric(label: '(a+b)(a−b)', value: rectArea.toStringAsFixed(0), color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'a: ${_a.toStringAsFixed(0)}', value: _a, min: 3, max: 9, divisions: 6, activeColor: Colors.teal, onChanged: (v) => setState(() { _a = v; _controller.value = 1; })),
          SimSlider(label: 'b: ${_b.toStringAsFixed(0)}', value: _b, min: 1, max: _a - 1, divisions: (_a - 2).clamp(1, 8).toInt(), activeColor: Colors.deepOrange, onChanged: (v) => setState(() { _b = v; _controller.value = 1; })),
        ],
      ),
    );
  }
}

class _LShapePainter extends CustomPainter {
  final double a, b;
  _LShapePainter({required this.a, required this.b});

  @override
  void paint(Canvas canvas, Size size) {
    const scale = 12.0;
    final full = Rect.fromLTWH(0, 0, a * scale, a * scale);
    final corner = Rect.fromLTWH(a * scale - b * scale, 0, b * scale, b * scale);
    final path = Path.combine(PathOperation.difference, Path()..addRect(full), Path()..addRect(corner));
    canvas.drawPath(path, Paint()..color = Colors.teal.shade300);
    canvas.drawPath(path, Paint()..color = Colors.teal.shade800..style = PaintingStyle.stroke..strokeWidth = 1.5);
  }

  @override
  bool shouldRepaint(covariant _LShapePainter oldDelegate) => true;
}
