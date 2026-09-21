import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _TrophicLevel {
  final String name;
  final String example;
  final IconData icon;
  final Color color;

  const _TrophicLevel(this.name, this.example, this.icon, this.color);
}

/// An energy pyramid: each trophic level only passes on about 10% of the
/// energy it receives, shown as shrinking tiers you can tap for details.
class OurEnvironmentSimulationWidget extends StatefulWidget {
  const OurEnvironmentSimulationWidget({super.key});

  @override
  State<OurEnvironmentSimulationWidget> createState() => _OurEnvironmentSimulationWidgetState();
}

class _OurEnvironmentSimulationWidgetState extends State<OurEnvironmentSimulationWidget> {
  static const _levels = [
    _TrophicLevel('Producers', 'Grass — captures 100% of the available energy from sunlight.', Icons.grass, Color(0xFF66BB6A)),
    _TrophicLevel('Primary Consumers', 'Deer — herbivores that eat producers, receiving only ~10% of that energy.', Icons.pets, Color(0xFF8D6E63)),
    _TrophicLevel('Secondary Consumers', 'Fox — carnivores that eat herbivores, receiving ~10% of the previous level\'s energy.', Icons.cruelty_free, Color(0xFFFFA726)),
    _TrophicLevel('Tertiary Consumers', 'Eagle — top predators, receiving only ~0.1% of the original energy from the sun.', Icons.flutter_dash, Color(0xFFEF5350)),
  ];

  int _selected = 0;

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Energy Flow: The Ecological Pyramid',
      icon: Icons.change_history,
      accent: Colors.green.shade800,
      description: 'At each trophic level, only about 10% of energy passes to the next — tap a level to explore.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          LayoutBuilder(builder: (context, constraints) {
            return Column(
              children: _levels.reversed.toList().asMap().entries.map((entry) {
                final reversedIndex = _levels.length - 1 - entry.key;
                final level = entry.value;
                final isSelected = _selected == reversedIndex;
                final widthFactor = 1.0 - reversedIndex * 0.22;
                return GestureDetector(
                  onTap: () => setState(() => _selected = reversedIndex),
                  child: Container(
                    margin: const EdgeInsets.symmetric(vertical: 2),
                    height: 40,
                    width: constraints.maxWidth * widthFactor,
                    decoration: BoxDecoration(
                      color: level.color,
                      borderRadius: BorderRadius.circular(6),
                      border: isSelected ? Border.all(color: Theme.of(context).colorScheme.onSurface, width: 2) : null,
                    ),
                    alignment: Alignment.center,
                    child: Text(level.name, style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 11)),
                  ),
                );
              }).toList(),
            );
          }),
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: _levels[_selected].color.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(10)),
            child: Row(
              children: [
                Icon(_levels[_selected].icon, color: _levels[_selected].color),
                const SizedBox(width: 10),
                Expanded(child: Text(_levels[_selected].example, style: TextStyle(fontSize: 13))),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
