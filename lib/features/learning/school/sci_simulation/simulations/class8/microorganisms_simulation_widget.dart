import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Microbe {
  final String name;
  final String group;
  final bool isFriend;
  final String detail;
  final Color color;
  final IconData icon;

  const _Microbe(this.name, this.group, this.isFriend, this.detail, this.color, this.icon);
}

/// A "Friend or Foe" sorter: tap a microorganism to see which group it
/// belongs to and whether it's generally helpful or harmful to us.
class MicroorganismsSimulationWidget extends StatefulWidget {
  const MicroorganismsSimulationWidget({super.key});

  @override
  State<MicroorganismsSimulationWidget> createState() => _MicroorganismsSimulationWidgetState();
}

class _MicroorganismsSimulationWidgetState extends State<MicroorganismsSimulationWidget> {
  static const _microbes = [
    _Microbe('Yeast', 'Fungi', true, 'Used in baking (makes bread rise) and brewing, through fermentation.', Colors.amber, Icons.bakery_dining),
    _Microbe('Lactobacillus', 'Bacteria', true, 'Converts milk into curd.', Colors.lightGreen, Icons.icecream),
    _Microbe('Rhizobium', 'Bacteria', true, 'Fixes atmospheric nitrogen in the roots of leguminous plants, enriching soil.', Colors.teal, Icons.eco),
    _Microbe('Penicillium', 'Fungi', true, 'Source of the antibiotic penicillin.', Colors.lightBlue, Icons.medical_services),
    _Microbe('Plasmodium', 'Protozoa', false, 'Causes malaria, spread by female Anopheles mosquitoes.', Colors.red, Icons.coronavirus),
    _Microbe('Mycobacterium tuberculosis', 'Bacteria', false, 'Causes tuberculosis (TB), a serious lung infection.', Colors.redAccent, Icons.coronavirus),
    _Microbe('Influenza Virus', 'Virus', false, 'Causes the flu, spread through the air by coughing and sneezing.', Colors.deepOrange, Icons.coronavirus),
    _Microbe('Bread Mould', 'Fungi', false, 'Spoils bread and other food by growing on it and releasing toxins.', Colors.brown, Icons.warning_amber),
  ];

  _Microbe _selected = _microbes[0];

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Microorganisms: Friend or Foe?',
      icon: Icons.biotech,
      accent: Colors.purple.shade700,
      description: 'Tap a microorganism to see which group it belongs to, and whether it helps or harms us.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _microbes.map((m) {
              final isSelected = _selected.name == m.name;
              return ChoiceChip(
                avatar: Icon(m.icon, size: 16, color: isSelected ? Colors.white : m.color),
                label: Text(m.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: m.color,
                backgroundColor: m.color.withValues(alpha: 0.12),
                onSelected: (_) => setState(() => _selected = m),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              color: _selected.isFriend ? Colors.green.shade50 : Colors.red.shade50,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: _selected.isFriend ? Colors.green.shade200 : Colors.red.shade200),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Icon(_selected.isFriend ? Icons.thumb_up : Icons.thumb_down, color: _selected.isFriend ? Colors.green.shade700 : Colors.red.shade700),
                    const SizedBox(width: 8),
                    Text(_selected.isFriend ? 'Friend' : 'Foe', style: TextStyle(fontWeight: FontWeight.bold, color: _selected.isFriend ? Colors.green.shade800 : Colors.red.shade800)),
                    const Spacer(),
                    Chip(label: Text(_selected.group, style: TextStyle(fontSize: 11)), backgroundColor: Colors.white),
                  ],
                ),
                const SizedBox(height: 8),
                Text(_selected.detail, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
