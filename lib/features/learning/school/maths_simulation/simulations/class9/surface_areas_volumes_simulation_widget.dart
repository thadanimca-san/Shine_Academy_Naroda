import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Pick a cone, sphere or hemisphere and adjust its dimensions: the
/// solid spins into view with a scale-and-rotate animation whenever the
/// shape or a dimension changes, and surface area / volume recompute
/// live.
class SurfaceAreasVolumesSimulationWidget extends StatefulWidget {
  const SurfaceAreasVolumesSimulationWidget({super.key});

  @override
  State<SurfaceAreasVolumesSimulationWidget> createState() => _SurfaceAreasVolumesSimulationWidgetState();
}

class _SurfaceAreasVolumesSimulationWidgetState extends State<SurfaceAreasVolumesSimulationWidget> with SingleTickerProviderStateMixin {
  int _shapeIndex = 0; // 0=cone,1=sphere,2=hemisphere
  double _r = 4;
  double _h = 6;
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
    double sa, vol;
    String name;
    final l = _sqrt(_r * _r + _h * _h);
    switch (_shapeIndex) {
      case 1:
        name = 'Sphere';
        sa = 4 * pi * _r * _r;
        vol = (4 / 3) * pi * _r * _r * _r;
        break;
      case 2:
        name = 'Hemisphere';
        sa = 3 * pi * _r * _r;
        vol = (2 / 3) * pi * _r * _r * _r;
        break;
      default:
        name = 'Cone';
        sa = pi * _r * _r + pi * _r * l;
        vol = (1 / 3) * pi * _r * _r * _h;
    }

    return SimFrame(
      title: 'Surface Area & Volume',
      icon: Icons.view_in_ar,
      accent: Colors.blue.shade700,
      description: 'Pick a solid and adjust its dimensions to see it spin into place and surface area / volume update.',
      actions: [
        DropdownButton<int>(
          value: _shapeIndex,
          items: [
            DropdownMenuItem(value: 0, child: Text(TrilingualService.instance.getUIText('Cone'))),
            DropdownMenuItem(value: 1, child: Text(TrilingualService.instance.getUIText('Sphere'))),
            DropdownMenuItem(value: 2, child: Text(TrilingualService.instance.getUIText('Hemisphere'))),
          ],
          onChanged: (v) => setState(() { _shapeIndex = v!; _replay(); }),
        ),
      ],
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 120,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.blue.shade50, borderRadius: BorderRadius.circular(10)),
            child: Center(
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) {
                  final eased = Curves.easeOutBack.transform(_controller.value).clamp(0.0, 1.5);
                  final spin = (1 - _controller.value) * 3.14159265;
                  return Transform(
                    alignment: Alignment.center,
                    transform: Matrix4.identity()
                      ..scaleByDouble(eased, eased, 1.0, 1.0)
                      ..rotateY(spin),
                    child: Icon(_shapeIndex == 0 ? Icons.change_history : Icons.circle, size: 70, color: Colors.blue.shade700),
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
              style: TextButton.styleFrom(foregroundColor: Colors.blue.shade700),
            ),
          ),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Shape', value: name, color: Colors.blue),
            SimMetric(label: 'Surface Area', value: '${sa.toStringAsFixed(1)} u²', color: Colors.deepOrange),
            SimMetric(label: 'Volume', value: '${vol.toStringAsFixed(1)} u³', color: Colors.teal),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Radius: ${_r.toStringAsFixed(0)}', value: _r, min: 1, max: 8, divisions: 7, activeColor: Colors.blue, onChanged: (v) => setState(() { _r = v; _replay(); })),
          if (_shapeIndex == 0) SimSlider(label: 'Height: ${_h.toStringAsFixed(0)}', value: _h, min: 1, max: 10, divisions: 9, activeColor: Colors.indigo, onChanged: (v) => setState(() { _h = v; _replay(); })),
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
