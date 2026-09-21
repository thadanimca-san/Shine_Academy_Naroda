import 'package:flutter/material.dart';
import 'common/organelle_diagram.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// An interactive, textbook-style labeled cell diagram: tap any organelle to
/// reveal its function, and switch between plant and animal cells to compare
/// the extra structures (cell wall, chloroplast, large vacuole) plant cells
/// have. Every organelle is drawn as its real biological shape (folded
/// mitochondrial cristae, stacked Golgi cisternae, granular chloroplasts,
/// etc.) rather than a generic circle — see [OrganelleDiagramView].
class CellSimulationWidget extends StatefulWidget {
  const CellSimulationWidget({super.key});

  @override
  State<CellSimulationWidget> createState() => _CellSimulationWidgetState();
}

class _CellSimulationWidgetState extends State<CellSimulationWidget> {
  bool _isPlantCell = true;
  Organelle? _selected;

  static const _animalParts = [
    Organelle('Cell Membrane', 'Membrane', 'Thin outer covering that controls what enters and leaves the cell.', Color(0xFF9575CD), Alignment(0, 0), 1.0, OrganelleShape.membrane),
    Organelle('Nucleus', 'Nucleus', 'Control centre of the cell; contains nucleoplasm, chromatin (DNA + protein), and a prominent nucleolus, all bounded by a double nuclear membrane with pores.', Color(0xFF5C6BC0), Alignment(-0.4, -0.05), 0.85, OrganelleShape.nucleus),
    Organelle('Endoplasmic Reticulum', 'E.R.', 'A network of membranes continuous with the nuclear envelope. Rough ER (studded with ribosomes) makes proteins; smooth ER makes lipids and detoxifies substances.', Color(0xFF43A047), Alignment(0.05, -0.45), 0.85, OrganelleShape.reticulum),
    Organelle('Golgi Apparatus', 'Golgi', 'A stack of flattened, curved sacs (cisternae) that stores, modifies, and packages materials — especially proteins arriving from the ER — into vesicles.', Color(0xFFFB8C00), Alignment(0.55, -0.75), 0.68, OrganelleShape.golgi),
    Organelle('Lysosomes', 'Lysosome', 'Small round sacs full of digestive enzymes — the cell\'s "suicide bags" — that break down waste, worn-out cell parts, and foreign material.', Color(0xFFAB47BC), Alignment(0.78, -0.4), 0.5, OrganelleShape.lysosome),
    Organelle('Mitochondria', 'Mitochondria', 'The "powerhouse" of the cell — its folded inner membrane (cristae) is where aerobic respiration releases energy from food.', Color(0xFFE53935), Alignment(0.62, 0.02), 0.68, OrganelleShape.mitochondrion),
    Organelle('Ribosomes', 'Ribosomes', 'Tiny granules, either studding the rough ER or floating free in the cytoplasm, where proteins are synthesised.', Color(0xFF37474F), Alignment(-0.35, 0.6), 0.65, OrganelleShape.ribosomeCluster),
    Organelle('Cytoplasm', 'Cytoplasm', 'The jelly-like fluid filling the cell, where organelles are suspended and many chemical reactions take place.', Color(0xFF4FC3F7), Alignment(0.8, 0.75), 1.0, OrganelleShape.cytoplasm),
  ];

  static const _plantExtras = [
    Organelle('Cell Wall', 'Cell Wall', 'Rigid outer layer of cellulose giving the cell shape and protection.', Color(0xFF8D6E63), Alignment(0, 0), 1.05, OrganelleShape.wall),
    Organelle('Chloroplast', 'Chloroplast', 'Contains chlorophyll and internal stacks called grana; the site of photosynthesis.', Color(0xFF2E7D32), Alignment(0.58, 0.72), 0.65, OrganelleShape.chloroplast),
    Organelle('Vacuole', 'Vacuole', 'A large, permanent sap-filled sac that maintains turgor pressure and stores water, ions, and waste products.', Color(0xFF29B6F6), Alignment(-0.62, 0.5), 0.62, OrganelleShape.vacuole),
  ];

  @override
  Widget build(BuildContext context) {
    final parts = [..._animalParts, if (_isPlantCell) ..._plantExtras];

    return SimFrame(
      title: 'Inside the Cell',
      icon: Icons.hive,
      accent: Colors.green.shade700,
      description: 'Tap an organelle to learn its function. Compare plant and animal cells.',
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
            onSelect: (o) => setState(() => _selected = o),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: parts.map((o) {
              final isSelected = _selected?.name == o.name;
              return ActionChip(
                label: Text(o.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                backgroundColor: isSelected ? o.color : o.color.withValues(alpha: 0.25),
                onPressed: () => setState(() => _selected = o),
              );
            }).toList(),
          ),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: _selected == null
                ? Text(TrilingualService.instance.getUIText('Tap an organelle above to see what it does.'), style: TextStyle(color: Theme.of(context).colorScheme.onSurfaceVariant, fontSize: 13))
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
