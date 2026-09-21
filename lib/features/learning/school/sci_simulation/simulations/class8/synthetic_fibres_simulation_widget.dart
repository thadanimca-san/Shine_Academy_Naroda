import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Fibre {
  final String name;
  final bool isSynthetic;
  final String source;
  final List<String> properties;
  final Color color;

  const _Fibre(this.name, this.isSynthetic, this.source, this.properties, this.color);
}

/// Compares natural and synthetic fibres side by side: tap a fibre to see
/// where it comes from and its defining properties.
class SyntheticFibresSimulationWidget extends StatefulWidget {
  const SyntheticFibresSimulationWidget({super.key});

  @override
  State<SyntheticFibresSimulationWidget> createState() => _SyntheticFibresSimulationWidgetState();
}

class _SyntheticFibresSimulationWidgetState extends State<SyntheticFibresSimulationWidget> {
  static const _fibres = [
    _Fibre('Cotton', false, 'Cotton plant (natural)', ['Absorbs moisture well', 'Breathable', 'Biodegradable'], Color(0xFF8D6E63)),
    _Fibre('Wool', false, 'Sheep (natural)', ['Good insulator', 'Warm', 'Biodegradable'], Color(0xFFA1887F)),
    _Fibre('Rayon', true, 'Wood pulp (semi-synthetic)', ['Feels like silk', 'Absorbent', 'Cheaper than natural silk'], Color(0xFF4FC3F7)),
    _Fibre('Nylon', true, 'Petrochemicals (fully synthetic)', ['Very strong & elastic', 'Lightweight', 'Used in ropes, parachutes'], Color(0xFF7E57C2)),
    _Fibre('Polyester', true, 'Petrochemicals (fully synthetic)', ['Wrinkle-resistant', 'Quick-drying', 'Used to make PET bottles'], Color(0xFFEF5350)),
    _Fibre('Acrylic', true, 'Petrochemicals (fully synthetic)', ['Resembles wool', 'Cheaper than wool', 'Used in sweaters, blankets'], Color(0xFFFFA726)),
  ];

  _Fibre _selected = _fibres[0];

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Natural vs Synthetic Fibres',
      icon: Icons.checkroom,
      accent: Colors.indigo.shade600,
      description: 'Tap a fibre to see its source and key properties.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Expanded(child: _buildLegend('Natural', Colors.brown)),
              Expanded(child: _buildLegend('Synthetic', Colors.indigo)),
            ],
          ),
          const SizedBox(height: 10),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _fibres.map((f) {
              final isSelected = _selected.name == f.name;
              return ChoiceChip(
                label: Text(f.name, style: TextStyle(fontSize: 12.5, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: f.color,
                backgroundColor: f.color.withValues(alpha: 0.15),
                onSelected: (_) => setState(() => _selected = f),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: _selected.color.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12), border: Border.all(color: _selected.color.withValues(alpha: 0.3))),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Icon(_selected.isSynthetic ? Icons.science : Icons.eco, color: _selected.color),
                    const SizedBox(width: 8),
                    Text(_selected.name, style: TextStyle(fontWeight: FontWeight.bold, color: _selected.color, fontSize: 15)),
                  ],
                ),
                const SizedBox(height: 6),
                Text('Source: ${_selected.source}', style: TextStyle(fontSize: 13, fontStyle: FontStyle.italic)),
                const SizedBox(height: 8),
                ..._selected.properties.map((p) => Padding(
                      padding: const EdgeInsets.only(bottom: 3),
                      child: Row(children: [Text(TrilingualService.instance.getUIText('• ')), Expanded(child: Text(p, style: TextStyle(fontSize: 13)))]),
                    )),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildLegend(String label, Color color) {
    return Row(
      children: [
        Container(width: 12, height: 12, decoration: BoxDecoration(color: color, shape: BoxShape.circle)),
        const SizedBox(width: 6),
        Text(label, style: TextStyle(fontSize: 12)),
      ],
    );
  }
}
