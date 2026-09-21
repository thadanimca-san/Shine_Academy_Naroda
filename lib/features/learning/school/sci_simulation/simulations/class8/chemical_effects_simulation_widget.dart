import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A conductivity tester: dissolve more salt into water and watch an LED
/// in the circuit glow brighter, showing that a stronger electrolyte
/// solution conducts more current.
class ChemicalEffectsSimulationWidget extends StatefulWidget {
  const ChemicalEffectsSimulationWidget({super.key});

  @override
  State<ChemicalEffectsSimulationWidget> createState() => _ChemicalEffectsSimulationWidgetState();
}

class _ChemicalEffectsSimulationWidgetState extends State<ChemicalEffectsSimulationWidget> {
  double _saltAmount = 0; // 0 = pure water, 10 = strong electrolyte

  @override
  Widget build(BuildContext context) {
    final brightness = (_saltAmount / 10).clamp(0.0, 1.0);

    return SimFrame(
      title: 'Testing Conductivity of Liquids',
      icon: Icons.bolt,
      accent: Colors.amber.shade800,
      description: 'Dissolve salt into the beaker of water and watch the LED brightness change as conductivity increases.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.blueGrey.shade900, borderRadius: BorderRadius.circular(10)),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(
                  Icons.lightbulb,
                  size: 70,
                  color: Color.lerp(Colors.grey.shade700, Colors.amberAccent, brightness),
                  shadows: brightness > 0.1
                      ? [Shadow(color: Colors.amberAccent.withValues(alpha: brightness), blurRadius: 30 * brightness)]
                      : null,
                ),
                const SizedBox(width: 20),
                Container(
                  width: 80,
                  height: 100,
                  decoration: BoxDecoration(
                    color: Colors.lightBlue.withValues(alpha: 0.3),
                    border: Border.all(color: Colors.lightBlue.shade200, width: 2),
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: Center(
                    child: Text('${_saltAmount.toStringAsFixed(0)}g\nsalt', textAlign: TextAlign.center, style: TextStyle(color: Colors.white, fontSize: 11)),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Salt Added', value: '${_saltAmount.toStringAsFixed(0)} g'),
            SimMetric(label: 'Conductivity', value: brightness < 0.1 ? 'Very Poor' : (brightness < 0.5 ? 'Moderate' : 'Good'), color: Colors.amber.shade800),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Salt dissolved in water: ${_saltAmount.toStringAsFixed(0)} g',
            value: _saltAmount,
            min: 0,
            max: 10,
            divisions: 10,
            activeColor: Colors.amber.shade800,
            onChanged: (val) => setState(() => _saltAmount = val),
          ),
          const SizedBox(height: 4),
          Text(TrilingualService.instance.getUIText('Pure water barely conducts; dissolved salt ions carry the current, lighting the LED.'), style: TextStyle(fontSize: 11.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
        ],
      ),
    );
  }
}
