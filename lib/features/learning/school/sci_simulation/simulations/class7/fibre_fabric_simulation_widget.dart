import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Stage {
  final String name;
  final IconData icon;
  final String description;
  const _Stage(this.name, this.icon, this.description);
}

/// Steps through the silk moth's life cycle from egg to moth, and the
/// wool-making process, showing where fibre actually comes from.
class FibreFabricSimulationWidget extends StatefulWidget {
  const FibreFabricSimulationWidget({super.key});

  @override
  State<FibreFabricSimulationWidget> createState() => _FibreFabricSimulationWidgetState();
}

class _FibreFabricSimulationWidgetState extends State<FibreFabricSimulationWidget> {
  bool _showWool = false;

  static const _silkStages = [
    _Stage('Egg', Icons.circle, 'The female silk moth lays hundreds of tiny eggs.'),
    _Stage('Larva (Silkworm)', Icons.bug_report, 'A caterpillar hatches and feeds voraciously on mulberry leaves.'),
    _Stage('Cocoon', Icons.egg, 'The larva spins a protective silk thread cocoon around itself.'),
    _Stage('Pupa', Icons.hourglass_bottom, 'Inside the cocoon, the larva transforms into a pupa.'),
    _Stage('Moth', Icons.flutter_dash, 'An adult silk moth emerges, ready to lay eggs and start the cycle again.'),
  ];

  static const _woolStages = [
    _Stage('Rearing', Icons.pets, 'Sheep are reared and fed on grazing land for their fleece.'),
    _Stage('Shearing', Icons.content_cut, 'The fleece, with a thin layer of skin, is shaved off the sheep.'),
    _Stage('Scouring', Icons.water_drop, 'The sheared hair is washed to remove grease, dust and dirt.'),
    _Stage('Sorting', Icons.filter_alt, 'Hair of different textures is separated.'),
    _Stage('Spinning & Weaving', Icons.texture, 'Fibres are drawn out and twisted into yarn, then woven into wool fabric.'),
  ];

  int _index = 0;

  @override
  Widget build(BuildContext context) {
    final stages = _showWool ? _woolStages : _silkStages;
    final idx = _index.clamp(0, stages.length - 1);
    final stage = stages[idx];
    final accent = _showWool ? Colors.brown.shade600 : Colors.pink.shade400;

    return SimFrame(
      title: _showWool ? 'From Sheep to Wool' : 'Silk Moth Life Cycle',
      icon: Icons.checkroom,
      accent: accent,
      description: 'Step through how animal fibres are produced, from the living animal to the raw fibre.',
      actions: [
        ToggleButtons(
          isSelected: [!_showWool, _showWool],
          onPressed: (i) => setState(() {
            _showWool = i == 1;
            _index = 0;
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: accent,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 50),
          children: [Text(TrilingualService.instance.getUIText('Silk')), Text(TrilingualService.instance.getUIText('Wool'))],
        ),
      ],
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(color: accent.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12)),
            child: Column(
              children: [
                Icon(stage.icon, size: 46, color: accent),
                const SizedBox(height: 10),
                Text(stage.name, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15, color: accent)),
                const SizedBox(height: 8),
                Text(stage.description, textAlign: TextAlign.center, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
          const SizedBox(height: 10),
          LinearProgressIndicator(value: (idx + 1) / stages.length, minHeight: 6, color: accent, backgroundColor: accent.withValues(alpha: 0.15)),
          const SizedBox(height: 14),
          Row(
            children: [
              Expanded(
                child: OutlinedButton.icon(
                  onPressed: idx == 0 ? null : () => setState(() => _index--),
                  icon: Icon(Icons.arrow_back),
                  label: Text(TrilingualService.instance.getUIText('Previous')),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: idx == stages.length - 1 ? null : () => setState(() => _index++),
                  icon: Icon(Icons.arrow_forward),
                  label: Text(TrilingualService.instance.getUIText('Next')),
                  style: ElevatedButton.styleFrom(backgroundColor: accent, foregroundColor: Colors.white),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
