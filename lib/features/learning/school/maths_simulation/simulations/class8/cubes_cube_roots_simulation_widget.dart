import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A stack of n layers, each an n×n grid of small cubes, that build up
/// one layer at a time — a visual for why n³ means "n multiplied by
/// itself three times."
class CubesCubeRootsSimulationWidget extends StatefulWidget {
  const CubesCubeRootsSimulationWidget({super.key});

  @override
  State<CubesCubeRootsSimulationWidget> createState() => _CubesCubeRootsSimulationWidgetState();
}

class _CubesCubeRootsSimulationWidgetState extends State<CubesCubeRootsSimulationWidget> with SingleTickerProviderStateMixin {
  int _n = 3;
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
    final cube = _n * _n * _n;

    return SimFrame(
      title: 'Perfect Cubes as Stacked Layers',
      icon: Icons.view_in_ar,
      accent: Colors.deepOrange.shade400,
      description: 'n³ is n layers, each an n-by-n grid, stacking up one at a time — n multiplied by itself three times.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 180,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.deepOrange.shade50, borderRadius: BorderRadius.circular(10)),
            padding: const EdgeInsets.all(8),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                return SingleChildScrollView(
                  child: Column(
                    children: List.generate(_n, (layer) {
                      final start = layer / _n;
                      final end = start + (1 / _n);
                      final localT = ((_controller.value - start) / (end - start)).clamp(0.0, 1.0);
                      final eased = Curves.easeOutBack.transform(localT);
                      return Padding(
                        padding: const EdgeInsets.symmetric(vertical: 3),
                        child: Opacity(
                          opacity: eased.clamp(0.0, 1.0),
                          child: Transform.scale(
                            scale: 0.4 + 0.6 * eased.clamp(0.0, 1.0),
                            child: Wrap(
                              spacing: 3,
                              runSpacing: 3,
                              children: List.generate(_n * _n, (i) => Container(width: 14, height: 14, decoration: BoxDecoration(color: Colors.deepOrange.shade400, borderRadius: BorderRadius.circular(2)))),
                            ),
                          ),
                        ),
                      );
                    }),
                  ),
                );
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
              style: TextButton.styleFrom(foregroundColor: Colors.deepOrange.shade400),
            ),
          ),
          SimMetricPanel(metrics: [
            SimMetric(label: 'n', value: '$_n'),
            SimMetric(label: 'n³', value: '$cube', color: Colors.deepOrange),
            SimMetric(label: '∛$cube', value: '$_n', color: Colors.teal),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'n: $_n', value: _n.toDouble(), min: 1, max: 6, divisions: 5, activeColor: Colors.deepOrange, onChanged: (v) => setState(() { _n = v.round(); _replay(); })),
        ],
      ),
    );
  }
}
