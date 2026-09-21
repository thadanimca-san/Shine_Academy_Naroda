import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A thermometer you can heat up, plus a tap-to-explore comparison of
/// conduction, convection and radiation — the three ways heat travels.
class HeatSimulationWidget extends StatefulWidget {
  const HeatSimulationWidget({super.key});

  @override
  State<HeatSimulationWidget> createState() => _HeatSimulationWidgetState();
}

class _HeatSimulationWidgetState extends State<HeatSimulationWidget> {
  double _temperature = 25;
  int _selectedMode = 0;

  static const _modes = [
    ('Conduction', Icons.linear_scale, 'Heat travels through a solid material, particle to particle, without the material itself moving. E.g. a metal spoon heating up in hot tea.'),
    ('Convection', Icons.waves, 'Heat travels through the actual movement of heated liquid or gas particles. E.g. water boiling in a pot, land and sea breezes.'),
    ('Radiation', Icons.wb_sunny, 'Heat travels as waves, needing no medium at all. E.g. heat reaching us from the Sun through empty space.'),
  ];

  @override
  Widget build(BuildContext context) {
    final fraction = ((_temperature + 10) / 120).clamp(0.0, 1.0);
    final mode = _modes[_selectedMode];

    return SimFrame(
      title: 'Heat & Temperature',
      icon: Icons.thermostat,
      accent: Colors.red.shade600,
      description: 'Heat the thermometer, and tap a mode below to see how heat can travel from one place to another.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            height: 150,
            child: Row(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Container(
                  width: 26,
                  height: 130,
                  decoration: BoxDecoration(color: Colors.grey.shade200, borderRadius: BorderRadius.circular(13), border: Border.all(color: Colors.grey.shade400)),
                  alignment: Alignment.bottomCenter,
                  padding: const EdgeInsets.all(3),
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 300),
                    width: double.infinity,
                    height: 124 * fraction,
                    decoration: BoxDecoration(
                      color: Color.lerp(Colors.blue, Colors.red, fraction),
                      borderRadius: BorderRadius.circular(10),
                    ),
                  ),
                ),
                const SizedBox(width: 16),
                Text('${_temperature.toStringAsFixed(0)}°C', style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Color.lerp(Colors.blue, Colors.red, fraction))),
              ],
            ),
          ),
          SimSlider(
            label: 'Temperature: ${_temperature.toStringAsFixed(0)}°C',
            value: _temperature,
            min: -10,
            max: 100,
            divisions: 22,
            activeColor: Colors.red,
            onChanged: (val) => setState(() => _temperature = val),
          ),
          const SizedBox(height: 10),
          Text(TrilingualService.instance.getUIText('Modes of Heat Transfer'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
          const SizedBox(height: 6),
          Wrap(
            spacing: 8,
            children: _modes.asMap().entries.map((e) {
              final isSelected = e.key == _selectedMode;
              return ChoiceChip(
                avatar: Icon(e.value.$2, size: 16, color: isSelected ? Colors.white : Colors.red.shade600),
                label: Text(e.value.$1, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.red.shade600,
                backgroundColor: Colors.red.shade50,
                onSelected: (_) => setState(() => _selectedMode = e.key),
              );
            }).toList(),
          ),
          const SizedBox(height: 10),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.red.shade50, borderRadius: BorderRadius.circular(10)),
            child: Text(mode.$3, style: TextStyle(fontSize: 13)),
          ),
        ],
      ),
    );
  }
}
