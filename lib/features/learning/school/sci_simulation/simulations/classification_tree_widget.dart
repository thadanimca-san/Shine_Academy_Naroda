import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _KingdomInfo {
  final String name;
  final String feature;
  final Color color;
  final List<String> examples;
  const _KingdomInfo(this.name, this.feature, this.color, this.examples);
}

const _kingdoms = [
  _KingdomInfo('Monera', 'Unicellular, prokaryotic (no true nucleus)', Color(0xFF6B9E5C), ['Bacteria', 'Cyanobacteria']),
  _KingdomInfo('Protista', 'Unicellular, eukaryotic', Color(0xFF4A8B6F), ['Amoeba', 'Paramecium', 'Euglena']),
  _KingdomInfo('Fungi', 'Multicellular, heterotrophic, chitin cell wall', Color(0xFFB08D3D), ['Mushroom', 'Yeast', 'Aspergillus']),
  _KingdomInfo('Plantae', 'Multicellular, autotrophic, cellulose cell wall', Color(0xFF3E8E4A), ['Moss', 'Fern', 'Pine', 'Rose']),
  _KingdomInfo('Animalia', 'Multicellular, heterotrophic, no cell wall', Color(0xFFC2455B), ['Sponge', 'Insect', 'Fish', 'Human']),
];

const _plantClasses = [
  _KingdomInfo('Thallophyta', 'Simple body (thallus), no true root/stem/leaf', Color(0xFF6FBF73), ['Spirogyra']),
  _KingdomInfo('Bryophyta', 'First on land, still need water to reproduce', Color(0xFF5DAE60), ['Moss', 'Marchantia']),
  _KingdomInfo('Pteridophyta', 'True roots/stems/leaves + vascular tissue, no seeds', Color(0xFF4C9E50), ['Fern']),
  _KingdomInfo('Gymnosperm', '"Naked seeds" on cones, no fruit', Color(0xFF3B8E40), ['Pine', 'Cycad']),
  _KingdomInfo('Angiosperm', 'Flowers + fruits, seeds enclosed', Color(0xFF2A7E30), ['Rose', 'Mango tree']),
];

const _animalPhyla = [
  _KingdomInfo('Porifera', 'Pores, no true tissues, fixed in place', Color(0xFFE8917A), ['Sponge']),
  _KingdomInfo('Cnidaria', 'True tissues, tentacles, single body opening', Color(0xFFE07B6A), ['Hydra', 'Jellyfish']),
  _KingdomInfo('Platyhelminthes', 'Flat body, bilateral symmetry', Color(0xFFD8655A), ['Flatworm']),
  _KingdomInfo('Nematoda', 'Cylindrical body, two body openings', Color(0xFFD04F4A), ['Roundworm']),
  _KingdomInfo('Annelida', 'Segmented body, organ system level', Color(0xFFC8393A), ['Earthworm']),
  _KingdomInfo('Arthropoda', 'Jointed legs, hard exoskeleton', Color(0xFFC0232A), ['Insect', 'Crab', 'Spider']),
  _KingdomInfo('Mollusca', 'Soft body, often with a shell', Color(0xFFB8232A), ['Snail', 'Octopus']),
  _KingdomInfo('Echinodermata', 'Hard internal skeleton, marine only', Color(0xFFA8232A), ['Starfish']),
  _KingdomInfo('Vertebrata', 'Has a backbone', Color(0xFF98232A), ['Fish', 'Bird', 'Human']),
];

/// A drill-down classification explorer: tap a kingdom, then (for Plantae
/// or Animalia) drill into its classes/phyla, matching the hierarchical
/// "Kingdom -> ... -> example organisms" structure taught in the chapter.
class ClassificationTreeWidget extends StatefulWidget {
  const ClassificationTreeWidget({super.key});

  @override
  State<ClassificationTreeWidget> createState() => _ClassificationTreeWidgetState();
}

class _ClassificationTreeWidgetState extends State<ClassificationTreeWidget> {
  _KingdomInfo? _selectedKingdom;
  _KingdomInfo? _selectedSub;

  @override
  Widget build(BuildContext context) {
    final canDrillDown = _selectedKingdom?.name == 'Plantae' || _selectedKingdom?.name == 'Animalia';
    final subList = _selectedKingdom?.name == 'Plantae' ? _plantClasses : (_selectedKingdom?.name == 'Animalia' ? _animalPhyla : const <_KingdomInfo>[]);

    return SimFrame(
      title: 'Classification Tree Explorer',
      icon: Icons.account_tree,
      accent: const Color(0xFF4A8B6F),
      description: 'Tap a kingdom to see its features. Plantae and Animalia can be explored further, into classes/phyla.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(TrilingualService.instance.getUIText('Step 1 — Kingdom'), style: TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurfaceVariant, letterSpacing: 0.4)),
          const SizedBox(height: 6),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _kingdoms.map((k) {
              final isSelected = _selectedKingdom?.name == k.name;
              return ChoiceChip(
                label: Text(k.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: k.color,
                backgroundColor: k.color.withValues(alpha: 0.18),
                onSelected: (_) => setState(() {
                  _selectedKingdom = k;
                  _selectedSub = null;
                }),
              );
            }).toList(),
          ),
          if (canDrillDown) ...[
            const SizedBox(height: 14),
            Text('Step 2 — ${_selectedKingdom!.name == 'Plantae' ? 'Class' : 'Phylum'}', style: TextStyle(fontSize: 11.5, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurfaceVariant, letterSpacing: 0.4)),
            const SizedBox(height: 6),
            Wrap(
              spacing: 6,
              runSpacing: 6,
              children: subList.map((s) {
                final isSelected = _selectedSub?.name == s.name;
                return ChoiceChip(
                  label: Text(s.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                  selected: isSelected,
                  selectedColor: s.color,
                  backgroundColor: s.color.withValues(alpha: 0.18),
                  onSelected: (_) => setState(() => _selectedSub = s),
                );
              }).toList(),
            ),
          ],
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: _buildInfo(),
          ),
        ],
      ),
    );
  }

  Widget _buildInfo() {
    final shown = _selectedSub ?? _selectedKingdom;
    if (shown == null) {
      return Text(TrilingualService.instance.getUIText('Tap a kingdom above to begin exploring.'), style: TextStyle(color: Theme.of(context).colorScheme.onSurfaceVariant, fontSize: 13));
    }
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(shown.name, style: TextStyle(fontWeight: FontWeight.bold, color: shown.color, fontSize: 14)),
        const SizedBox(height: 4),
        Text(shown.feature, style: TextStyle(fontSize: 13)),
        const SizedBox(height: 8),
        Wrap(
          spacing: 6,
          runSpacing: 6,
          children: shown.examples
              .map((e) => Chip(
                    label: Text(e, style: TextStyle(fontSize: 11)),
                    backgroundColor: shown.color.withValues(alpha: 0.14),
                    visualDensity: VisualDensity.compact,
                    materialTapTargetSize: MaterialTapTargetSize.shrinkWrap,
                  ))
              .toList(),
        ),
      ],
    );
  }
}
