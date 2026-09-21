import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Material {
  final String name;
  final bool isMetal;
  final bool malleable;
  final bool ductile;
  final bool conductsElectricity;
  final bool sonorous;

  const _Material(this.name, this.isMetal, this.malleable, this.ductile, this.conductsElectricity, this.sonorous);
}

/// A materials-testing lab: pick a material and "run" property tests
/// (malleability, ductility, conductivity, sonorousity) to see whether it
/// behaves like a metal or a non-metal.
class MaterialsMetalsSimulationWidget extends StatefulWidget {
  const MaterialsMetalsSimulationWidget({super.key});

  @override
  State<MaterialsMetalsSimulationWidget> createState() => _MaterialsMetalsSimulationWidgetState();
}

class _MaterialsMetalsSimulationWidgetState extends State<MaterialsMetalsSimulationWidget> {
  static const _materials = [
    _Material('Iron', true, true, true, true, true),
    _Material('Copper', true, true, true, true, true),
    _Material('Aluminium', true, true, true, true, true),
    _Material('Sulphur', false, false, false, false, false),
    _Material('Carbon (Graphite)', false, false, false, true, false),
    _Material('Sodium', true, true, false, true, false),
  ];

  _Material _selected = _materials[0];

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Materials Testing Lab',
      icon: Icons.science,
      accent: Colors.blueGrey.shade700,
      description: 'Select a material and see how it performs on standard property tests used to classify metals and non-metals.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _materials.map((m) {
              final isSelected = _selected.name == m.name;
              final color = m.isMetal ? Colors.blueGrey : Colors.deepOrange;
              return ChoiceChip(
                label: Text(m.name, style: TextStyle(fontSize: 12.5, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: color,
                backgroundColor: color.withValues(alpha: 0.12),
                onSelected: (_) => setState(() => _selected = m),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            padding: const EdgeInsets.all(6),
            decoration: BoxDecoration(color: (_selected.isMetal ? Colors.blueGrey : Colors.deepOrange).withValues(alpha: 0.08), borderRadius: BorderRadius.circular(10)),
            child: Row(
              children: [
                Icon(_selected.isMetal ? Icons.hardware : Icons.category, color: _selected.isMetal ? Colors.blueGrey.shade700 : Colors.deepOrange.shade700),
                const SizedBox(width: 8),
                Text('${_selected.name} is a ${_selected.isMetal ? "METAL" : "NON-METAL"}',
                    style: TextStyle(fontWeight: FontWeight.bold, color: _selected.isMetal ? Colors.blueGrey.shade800 : Colors.deepOrange.shade800)),
              ],
            ),
          ),
          const SizedBox(height: 12),
          _testRow('Malleability (can be hammered into sheets)', _selected.malleable),
          _testRow('Ductility (can be drawn into wires)', _selected.ductile),
          _testRow('Conducts electricity', _selected.conductsElectricity),
          _testRow('Sonorous (rings when struck)', _selected.sonorous),
        ],
      ),
    );
  }

  Widget _testRow(String label, bool pass) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8),
      child: Row(
        children: [
          Icon(pass ? Icons.check_circle : Icons.cancel, color: pass ? Colors.green : Colors.red, size: 20),
          const SizedBox(width: 8),
          Expanded(child: Text(label, style: TextStyle(fontSize: 13))),
        ],
      ),
    );
  }
}
