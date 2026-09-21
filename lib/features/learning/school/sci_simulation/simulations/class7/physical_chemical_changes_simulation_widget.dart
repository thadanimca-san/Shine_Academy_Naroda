import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Change {
  final String name;
  final bool isChemical;
  final String explanation;
  final IconData icon;

  const _Change(this.name, this.isChemical, this.explanation, this.icon);
}

/// A sorter: tap an everyday example and see whether it's a physical
/// change (no new substance, often reversible) or a chemical change (a
/// new substance forms, usually irreversible).
class PhysicalChemicalChangesSimulationWidget extends StatefulWidget {
  const PhysicalChemicalChangesSimulationWidget({super.key});

  @override
  State<PhysicalChemicalChangesSimulationWidget> createState() => _PhysicalChemicalChangesSimulationWidgetState();
}

class _PhysicalChemicalChangesSimulationWidgetState extends State<PhysicalChemicalChangesSimulationWidget> {
  static const _changes = [
    _Change('Melting Ice', false, 'Ice turns to water — same substance (H₂O), just a change of state. Reversible.', Icons.icecream),
    _Change('Burning Paper', true, 'Paper turns to ash and gases — new substances form. Irreversible.', Icons.local_fire_department),
    _Change('Cutting Paper', false, 'Only the shape changes — still paper. Reversible in principle (rejoin pieces).', Icons.content_cut),
    _Change('Rusting of Iron', true, 'Iron reacts with oxygen and moisture to form a new substance, rust. Irreversible.', Icons.warning_amber),
    _Change('Dissolving Sugar in Water', false, 'Sugar spreads through water but is still sugar — can be recovered by evaporation.', Icons.water_drop),
    _Change('Souring of Milk', true, 'Bacteria convert milk into curd — a new substance forms. Irreversible.', Icons.icecream),
    _Change('Stretching a Rubber Band', false, 'Only shape changes temporarily; the rubber band returns to its original form.', Icons.linear_scale),
    _Change('Burning Magnesium Ribbon', true, 'Magnesium reacts with oxygen to form magnesium oxide, releasing bright light.', Icons.flare),
  ];

  _Change _selected = _changes[0];

  @override
  Widget build(BuildContext context) {
    final color = _selected.isChemical ? Colors.deepOrange : Colors.blue;

    return SimFrame(
      title: 'Physical or Chemical Change?',
      icon: Icons.compare_arrows,
      accent: Colors.indigo.shade600,
      description: 'Tap an example to see whether it\'s a physical change or a chemical change, and why.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _changes.map((c) {
              final isSelected = _selected.name == c.name;
              final chipColor = c.isChemical ? Colors.deepOrange : Colors.blue;
              return ChoiceChip(
                avatar: Icon(c.icon, size: 16, color: isSelected ? Colors.white : chipColor),
                label: Text(c.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: chipColor,
                backgroundColor: chipColor.withValues(alpha: 0.12),
                onSelected: (_) => setState(() => _selected = c),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(14),
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
                    Chip(label: Text(_selected.isChemical ? 'Chemical Change' : 'Physical Change', style: TextStyle(color: Colors.white, fontSize: 11)), backgroundColor: color),
                  ],
                ),
                const SizedBox(height: 8),
                Text(_selected.explanation, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
