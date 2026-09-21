import 'package:flutter/material.dart';
import '../common/organelle_diagram.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A simplified interactive cell diagram for the Class 8 level: tap a part
/// to learn its basic function, and compare plant vs animal cells. Shares
/// the same textbook-accurate organelle shapes as the Class 9 diagram (see
/// [OrganelleDiagramView]) rather than generic circles.
class Class8CellStructureSimulationWidget extends StatefulWidget {
  const Class8CellStructureSimulationWidget({super.key});

  @override
  State<Class8CellStructureSimulationWidget> createState() => _Class8CellStructureSimulationWidgetState();
}

class _Class8CellStructureSimulationWidgetState extends State<Class8CellStructureSimulationWidget> {
  bool _isPlantCell = true;
  Organelle? _selected;

  static const _common = [
    Organelle('Cell Membrane', 'Membrane', 'The outer covering that controls what enters and leaves the cell.', Color(0xFF9575CD), Alignment(0, 0), 1.0, OrganelleShape.membrane),
    Organelle('Nucleus', 'Nucleus', 'Controls all the activities of the cell and holds genetic material.', Color(0xFF5C6BC0), Alignment(-0.35, -0.35), 0.85, OrganelleShape.nucleus),
    Organelle('Cytoplasm', 'Cytoplasm', 'The jelly-like substance in which the nucleus and organelles are suspended.', Color(0xFF4FC3F7), Alignment(0.6, -0.65), 1.0, OrganelleShape.cytoplasm),
  ];

  static const _plantExtras = [
    Organelle('Cell Wall', 'Cell Wall', 'A rigid outer layer that gives the plant cell shape and protection.', Color(0xFF8D6E63), Alignment(0, 0), 1.05, OrganelleShape.wall),
    Organelle('Vacuole', 'Vacuole', 'A large sac that stores water and cell sap, giving the cell rigidity.', Color(0xFF29B6F6), Alignment(0.5, 0.45), 0.75, OrganelleShape.vacuole),
  ];

  @override
  Widget build(BuildContext context) {
    final parts = [..._common, if (_isPlantCell) ..._plantExtras];

    return SimFrame(
      title: 'Inside the Cell',
      icon: Icons.hive,
      accent: Colors.green.shade700,
      description: 'Tap a part to see its function. Compare plant and animal cells.',
      actions: [
        ToggleButtons(
          isSelected: [!_isPlantCell, _isPlantCell],
          onPressed: (i) => setState(() {
            _isPlantCell = i == 1;
            _selected = null;
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.green.shade700,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 58),
          children: [Text(TrilingualService.instance.getUIText('Animal')), Text(TrilingualService.instance.getUIText('Plant'))],
        ),
      ],
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          OrganelleDiagramView(
            isPlantCell: _isPlantCell,
            organelles: parts,
            selected: _selected,
            onSelect: (p) => setState(() => _selected = p),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: parts.map((p) {
              final isSelected = _selected?.name == p.name;
              return ActionChip(
                label: Text(p.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                backgroundColor: isSelected ? p.color : p.color.withValues(alpha: 0.25),
                onPressed: () => setState(() => _selected = p),
              );
            }).toList(),
          ),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: _selected == null
                ? Text(TrilingualService.instance.getUIText('Tap a part above to see what it does.'), style: TextStyle(color: Theme.of(context).colorScheme.onSurfaceVariant, fontSize: 13))
                : Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(_selected!.name, style: TextStyle(fontWeight: FontWeight.bold, color: _selected!.color, fontSize: 14)),
                      const SizedBox(height: 4),
                      Text(_selected!.function, style: TextStyle(fontSize: 13)),
                    ],
                  ),
          ),
        ],
      ),
    );
  }
}
