import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A pressure sandbox: the same force spread over a smaller or larger
/// contact area sinks a block into sand more or less — showing why a
/// sharp knife cuts better and wide straps hurt less.
class ForcePressureSimulationWidget extends StatefulWidget {
  const ForcePressureSimulationWidget({super.key});

  @override
  State<ForcePressureSimulationWidget> createState() => _ForcePressureSimulationWidgetState();
}

class _ForcePressureSimulationWidgetState extends State<ForcePressureSimulationWidget> {
  double _force = 50; // N
  double _area = 10; // cm^2

  @override
  Widget build(BuildContext context) {
    final pressure = _force / _area;
    final sinkDepth = (pressure * 3).clamp(4.0, 90.0);

    return SimFrame(
      title: 'Force & Pressure Sandbox',
      icon: Icons.compress,
      accent: Colors.teal.shade700,
      description: 'The same force spread over a smaller area produces greater pressure — watch the block sink into sand.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 160,
            width: double.infinity,
            decoration: BoxDecoration(
              gradient: LinearGradient(colors: [Colors.teal.shade50, Colors.brown.shade200], begin: Alignment.topCenter, end: Alignment.bottomCenter, stops: const [0.55, 0.55]),
              borderRadius: BorderRadius.circular(10),
            ),
            child: Stack(
              alignment: Alignment.bottomCenter,
              children: [
                AnimatedContainer(
                  duration: const Duration(milliseconds: 300),
                  margin: EdgeInsets.only(bottom: 72 - sinkDepth * 0.5),
                  width: 20 + _area * 2.5,
                  height: 36,
                  decoration: BoxDecoration(color: Colors.blueGrey.shade600, borderRadius: BorderRadius.circular(4)),
                  alignment: Alignment.center,
                  child: Icon(Icons.arrow_downward, color: Colors.white, size: 18),
                ),
              ],
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Force', value: '${_force.toStringAsFixed(0)} N'),
            SimMetric(label: 'Contact Area', value: '${_area.toStringAsFixed(0)} cm²', color: Colors.brown),
            SimMetric(label: 'Pressure', value: '${pressure.toStringAsFixed(1)} N/cm²', color: Colors.teal.shade700),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Force applied: ${_force.toStringAsFixed(0)} N',
            value: _force,
            min: 10,
            max: 100,
            divisions: 18,
            activeColor: Colors.teal,
            onChanged: (val) => setState(() => _force = val),
          ),
          SimSlider(
            label: 'Contact area: ${_area.toStringAsFixed(0)} cm² (smaller = sharper)',
            value: _area,
            min: 2,
            max: 30,
            divisions: 28,
            activeColor: Colors.brown,
            onChanged: (val) => setState(() => _area = val),
          ),
        ],
      ),
    );
  }
}
