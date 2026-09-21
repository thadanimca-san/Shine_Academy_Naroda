import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Source {
  final String name;
  final bool renewable;
  final String note;
  final IconData icon;

  const _Source(this.name, this.renewable, this.note, this.icon);
}

/// A tap-to-explore gallery of energy sources, sorted into renewable and
/// non-renewable, with a quick note on how each is harnessed.
class SourcesEnergySimulationWidget extends StatefulWidget {
  const SourcesEnergySimulationWidget({super.key});

  @override
  State<SourcesEnergySimulationWidget> createState() => _SourcesEnergySimulationWidgetState();
}

class _SourcesEnergySimulationWidgetState extends State<SourcesEnergySimulationWidget> {
  static const _sources = [
    _Source('Solar', true, 'Solar cells convert sunlight directly into electricity.', Icons.wb_sunny),
    _Source('Wind', true, 'Wind turbines convert moving air into mechanical, then electrical, energy.', Icons.air),
    _Source('Hydro', true, 'Falling water from dams turns turbines to generate electricity.', Icons.water),
    _Source('Geothermal', true, 'Heat trapped inside the Earth is used to generate power.', Icons.terrain),
    _Source('Biogas', true, 'Decomposing organic waste produces a flammable gas used as fuel.', Icons.eco),
    _Source('Coal', false, 'A fossil fuel burned in thermal power plants; limited reserves.', Icons.local_fire_department),
    _Source('Petroleum', false, 'A fossil fuel refined into fuels like petrol and diesel; limited reserves.', Icons.local_gas_station),
    _Source('Nuclear', false, 'Splitting heavy atomic nuclei (fission) releases large amounts of energy.', Icons.warning_amber),
  ];

  _Source _selected = _sources[0];

  @override
  Widget build(BuildContext context) {
    final color = _selected.renewable ? Colors.green.shade700 : Colors.deepOrange.shade700;

    return SimFrame(
      title: 'Sources of Energy',
      icon: Icons.bolt,
      accent: Colors.amber.shade800,
      description: 'Tap a source to see whether it\'s renewable or non-renewable, and how it\'s harnessed.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _sources.map((s) {
              final isSelected = _selected.name == s.name;
              final c = s.renewable ? Colors.green.shade700 : Colors.deepOrange.shade700;
              return ChoiceChip(
                avatar: Icon(s.icon, size: 16, color: isSelected ? Colors.white : c),
                label: Text(s.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: c,
                backgroundColor: c.withValues(alpha: 0.12),
                onSelected: (_) => setState(() => _selected = s),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(color: color.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12), border: Border.all(color: color.withValues(alpha: 0.3))),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Icon(_selected.icon, color: color),
                    const SizedBox(width: 8),
                    Text(_selected.name, style: TextStyle(fontWeight: FontWeight.bold, color: color, fontSize: 15)),
                    const Spacer(),
                    Chip(label: Text(_selected.renewable ? 'Renewable' : 'Non-Renewable', style: TextStyle(color: Colors.white, fontSize: 11)), backgroundColor: color),
                  ],
                ),
                const SizedBox(height: 8),
                Text(_selected.note, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
