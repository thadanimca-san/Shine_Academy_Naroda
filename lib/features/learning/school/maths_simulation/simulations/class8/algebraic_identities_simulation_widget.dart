import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// The classic geometric proof of (a+b)²: an a×a square stays put while the
/// two ab rectangles slide in from the edges and the b² square scales into
/// the corner, animating the identity's four pieces assembling.
class AlgebraicIdentitiesSimulationWidget extends StatefulWidget {
  const AlgebraicIdentitiesSimulationWidget({super.key});

  @override
  State<AlgebraicIdentitiesSimulationWidget> createState() => _AlgebraicIdentitiesSimulationWidgetState();
}

class _AlgebraicIdentitiesSimulationWidgetState extends State<AlgebraicIdentitiesSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 3;
  double _b = 2;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 900));
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
    final aSq = _a * _a;
    final bSq = _b * _b;
    final ab = _a * _b;
    final total = aSq + 2 * ab + bSq;

    return SimFrame(
      title: '(a + b)² — Geometric Proof',
      icon: Icons.crop_square,
      accent: Colors.indigo.shade600,
      description: 'A square of side (a+b) splits into a², two ab rectangles, and b² — watch the pieces slide together.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 190,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.indigo.shade50, borderRadius: BorderRadius.circular(10)),
            child: Center(
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) {
                  // Right rectangle and bottom rectangle slide in from outside;
                  // the b² corner scales in last, staggered after both slide in.
                  final slideT = Curves.easeOutBack.transform((_controller.value / 0.7).clamp(0.0, 1.0));
                  final cornerT = Curves.easeOutBack.transform(((_controller.value - 0.5) / 0.5).clamp(0.0, 1.0));
                  final aPx = _a * 24;
                  final bPx = _b * 24;
                  return SizedBox(
                    width: aPx + bPx,
                    height: aPx + bPx,
                    child: Stack(
                      children: [
                        Positioned(
                          left: 0,
                          top: 0,
                          child: Container(width: aPx, height: aPx, color: Colors.blue.shade300, alignment: Alignment.center, child: Text(TrilingualService.instance.getUIText('a²'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))),
                        ),
                        Positioned(
                          left: aPx,
                          top: 0,
                          child: Transform.translate(
                            offset: Offset((1 - slideT) * bPx, 0),
                            child: Opacity(
                              opacity: slideT,
                              child: Container(width: bPx, height: aPx, color: Colors.teal.shade300, alignment: Alignment.center, child: Text(TrilingualService.instance.getUIText('ab'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))),
                            ),
                          ),
                        ),
                        Positioned(
                          left: 0,
                          top: aPx,
                          child: Transform.translate(
                            offset: Offset(0, (1 - slideT) * bPx),
                            child: Opacity(
                              opacity: slideT,
                              child: Container(width: aPx, height: bPx, color: Colors.teal.shade300, alignment: Alignment.center, child: Text(TrilingualService.instance.getUIText('ab'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))),
                            ),
                          ),
                        ),
                        Positioned(
                          left: aPx,
                          top: aPx,
                          child: Transform.scale(
                            scale: cornerT.clamp(0.0, 1.0),
                            alignment: Alignment.topLeft,
                            child: Container(width: bPx, height: bPx, color: Colors.orange.shade300, alignment: Alignment.center, child: Text(TrilingualService.instance.getUIText('b²'), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold))),
                          ),
                        ),
                      ],
                    ),
                  );
                },
              ),
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: TextButton.icon(
              onPressed: _replay,
              icon: Icon(Icons.replay, size: 18),
              label: Text(TrilingualService.instance.getUIText('Replay')),
              style: TextButton.styleFrom(foregroundColor: Colors.indigo.shade600),
            ),
          ),
          SimMetricPanel(metrics: [
            SimMetric(label: 'a²', value: aSq.toStringAsFixed(0), color: Colors.blue),
            SimMetric(label: '2ab', value: (2 * ab).toStringAsFixed(0), color: Colors.teal),
            SimMetric(label: 'b²', value: bSq.toStringAsFixed(0), color: Colors.orange),
          ]),
          const SizedBox(height: 6),
          Center(child: Text('(a+b)² = ${total.toStringAsFixed(0)}', style: TextStyle(fontWeight: FontWeight.bold, color: Colors.indigo.shade800))),
          const SizedBox(height: 14),
          SimSlider(label: 'a: ${_a.toStringAsFixed(0)}', value: _a, min: 1, max: 6, divisions: 5, activeColor: Colors.blue, onChanged: (v) => setState(() { _a = v; _replay(); })),
          SimSlider(label: 'b: ${_b.toStringAsFixed(0)}', value: _b, min: 1, max: 6, divisions: 5, activeColor: Colors.orange, onChanged: (v) => setState(() { _b = v; _replay(); })),
        ],
      ),
    );
  }
}
