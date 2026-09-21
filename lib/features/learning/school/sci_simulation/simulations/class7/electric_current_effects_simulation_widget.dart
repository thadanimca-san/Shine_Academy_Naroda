import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A switchable circuit lighting a bulb, plus an electromagnet whose
/// strength (number of pins it can hold) grows with a current slider.
class ElectricCurrentEffectsSimulationWidget extends StatefulWidget {
  const ElectricCurrentEffectsSimulationWidget({super.key});

  @override
  State<ElectricCurrentEffectsSimulationWidget> createState() => _ElectricCurrentEffectsSimulationWidgetState();
}

class _ElectricCurrentEffectsSimulationWidgetState extends State<ElectricCurrentEffectsSimulationWidget> {
  bool _switchOn = false;
  double _current = 3; // affects electromagnet strength, 0-10

  @override
  Widget build(BuildContext context) {
    final pinsHeld = (_current / 2).round();

    return SimFrame(
      title: 'Effects of Electric Current',
      icon: Icons.electric_bolt,
      accent: Colors.amber.shade800,
      description: 'Flip the switch to complete the circuit and light the bulb. Increase the current to strengthen the electromagnet.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 130,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.blueGrey.shade900, borderRadius: BorderRadius.circular(10)),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                Icon(Icons.battery_full, color: Colors.white70, size: 32),
                Icon(_switchOn ? Icons.toggle_on : Icons.toggle_off, color: _switchOn ? Colors.greenAccent : Colors.white54, size: 40),
                Icon(Icons.lightbulb, size: 60, color: _switchOn ? Colors.amberAccent : Colors.grey.shade700),
              ],
            ),
          ),
          const SizedBox(height: 10),
          SizedBox(
            width: double.infinity,
            child: ElevatedButton.icon(
              onPressed: () => setState(() => _switchOn = !_switchOn),
              icon: Icon(_switchOn ? Icons.toggle_on : Icons.toggle_off),
              label: Text(_switchOn ? 'Switch On (circuit complete)' : 'Switch Off (circuit broken)'),
              style: ElevatedButton.styleFrom(backgroundColor: _switchOn ? Colors.green : Colors.grey.shade600, foregroundColor: Colors.white),
            ),
          ),
          const SizedBox(height: 16),
          Text(TrilingualService.instance.getUIText('Electromagnet Strength'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
          const SizedBox(height: 6),
          Container(
            height: 90,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.amber.shade50, borderRadius: BorderRadius.circular(10)),
            child: Center(
              child: Wrap(
                spacing: 4,
                children: List.generate(5, (i) {
                  final active = i < pinsHeld;
                  return Icon(Icons.push_pin, size: 24, color: active ? Colors.amber.shade800 : Colors.grey.shade300);
                }),
              ),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Current', value: '${_current.toStringAsFixed(0)} A'),
            SimMetric(label: 'Pins Held', value: '$pinsHeld', color: Colors.amber.shade800),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Current through coil: ${_current.toStringAsFixed(0)} A',
            value: _current,
            min: 0,
            max: 10,
            divisions: 10,
            activeColor: Colors.amber.shade800,
            onChanged: (val) => setState(() => _current = val),
          ),
        ],
      ),
    );
  }
}
