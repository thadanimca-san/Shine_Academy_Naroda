import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// An ice-cream-cone combination solid (cone + hemisphere on top): the
/// cone and its scoop scale up into place whenever radius or height
/// change, and the combined volume and surface area recompute live.
class Class10SurfaceAreasVolumesSimulationWidget extends StatefulWidget {
  const Class10SurfaceAreasVolumesSimulationWidget({super.key});

  @override
  State<Class10SurfaceAreasVolumesSimulationWidget> createState() => _SurfaceAreasVolumesSimulationWidgetState();
}

class _SurfaceAreasVolumesSimulationWidgetState extends State<Class10SurfaceAreasVolumesSimulationWidget> with SingleTickerProviderStateMixin {
  double _r = 3;
  double _h = 8;
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
    const pi = 3.14159265;
    final l = _sqrt(_r * _r + _h * _h);
    final coneVolume = (1 / 3) * pi * _r * _r * _h;
    final hemisphereVolume = (2 / 3) * pi * _r * _r * _r;
    final totalVolume = coneVolume + hemisphereVolume;
    final coneCurvedSA = pi * _r * l;
    final hemisphereCurvedSA = 2 * pi * _r * _r;
    final totalSA = coneCurvedSA + hemisphereCurvedSA;

    return SimFrame(
      title: 'Cone + Hemisphere Combination',
      icon: Icons.icecream,
      accent: Colors.orange.shade700,
      description: 'A classic "ice-cream cone" shape: total volume and surface area are the sum of the cone and hemisphere parts — watch it scale as you adjust them.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 150,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.orange.shade50, borderRadius: BorderRadius.circular(10)),
            child: Center(
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) {
                  final eased = Curves.easeOutBack.transform(_controller.value);
                  return Transform.scale(
                    scale: eased.clamp(0.0, 1.3),
                    child: Icon(Icons.icecream, size: 70, color: Colors.orange.shade700),
                  );
                },
              ),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Total Volume', value: '${totalVolume.toStringAsFixed(1)} u³', color: Colors.deepOrange),
            SimMetric(label: 'Total Surface Area', value: '${totalSA.toStringAsFixed(1)} u²', color: Colors.teal),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Radius: ${_r.toStringAsFixed(0)}', value: _r, min: 1, max: 6, divisions: 5, activeColor: Colors.orange, onChanged: (v) => setState(() { _r = v; _replay(); })),
          SimSlider(label: 'Cone height: ${_h.toStringAsFixed(0)}', value: _h, min: 2, max: 12, divisions: 10, activeColor: Colors.brown, onChanged: (v) => setState(() { _h = v; _replay(); })),
        ],
      ),
    );
  }

  double _sqrt(double v) {
    double x = v, guess = v / 2 == 0 ? 1 : v / 2;
    for (int i = 0; i < 20; i++) {
      guess = 0.5 * (guess + x / guess);
    }
    return guess;
  }
}
