import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Organism {
  final String name;
  final String emoji;
  final int trophicLevel; // 1 = producer, 2 = herbivore, 3 = carnivore, 4 = top carnivore
  final List<String> eats; // names of organisms this one eats
  const _Organism(this.name, this.emoji, this.trophicLevel, this.eats);
}

const _organisms = [
  _Organism('Grass', '🌾', 1, []),
  _Organism('Hare', '🐇', 2, ['Grass']),
  _Organism('Grasshopper', '🦗', 2, ['Grass']),
  _Organism('Mouse', '🐭', 2, ['Grass']),
  _Organism('Frog', '🐸', 3, ['Grasshopper']),
  _Organism('Snake', '🐍', 3, ['Frog', 'Mouse']),
  _Organism('Fox', '🦊', 3, ['Hare', 'Mouse']),
  _Organism('Owl', '🦉', 4, ['Mouse', 'Frog']),
  _Organism('Hawk', '🦅', 4, ['Snake', 'Hare', 'Owl']),
];

/// Tap any organism to trace its position in the food web: what it eats
/// (below) and what eats it (above) — building up an understanding that
/// food chains interlink into a web, matching Activity 12.8 in the chapter.
class FoodWebSimulationWidget extends StatefulWidget {
  const FoodWebSimulationWidget({super.key});

  @override
  State<FoodWebSimulationWidget> createState() => _FoodWebSimulationWidgetState();
}

class _FoodWebSimulationWidgetState extends State<FoodWebSimulationWidget> {
  _Organism? _selected;

  List<_Organism> get _predators {
    if (_selected == null) return [];
    return _organisms.where((o) => o.eats.contains(_selected!.name)).toList();
  }

  List<_Organism> get _prey {
    if (_selected == null) return [];
    return _organisms.where((o) => _selected!.eats.contains(o.name)).toList();
  }

  static const _levelColors = {
    1: Color(0xFF6B9E5C),
    2: Color(0xFF3F6A9C),
    3: Color(0xFFD9622A),
    4: Color(0xFFC2455B),
  };

  static const _levelNames = {
    1: 'Producer',
    2: 'Herbivore',
    3: 'Carnivore',
    4: 'Top Carnivore',
  };

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Food Web Explorer',
      icon: Icons.hub,
      accent: const Color(0xFF6B9E5C),
      description: 'Tap an organism to see what it eats and what eats it.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          for (int level = 4; level >= 1; level--) ...[
            Wrap(
              spacing: 6,
              runSpacing: 6,
              children: _organisms.where((o) => o.trophicLevel == level).map((o) {
                final isSelected = _selected?.name == o.name;
                final isLinked = _predators.contains(o) || _prey.contains(o);
                final color = _levelColors[level]!;
                return ChoiceChip(
                  label: Text('${o.emoji} ${o.name}', style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                  selected: isSelected,
                  selectedColor: color,
                  backgroundColor: isLinked ? color.withValues(alpha: 0.4) : color.withValues(alpha: 0.15),
                  onSelected: (_) => setState(() => _selected = o),
                );
              }).toList(),
            ),
            const SizedBox(height: 6),
          ],
          const SizedBox(height: 8),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: _selected == null
                ? Text(TrilingualService.instance.getUIText('Tap an organism above to trace its food web connections.'), style: TextStyle(color: Theme.of(context).colorScheme.onSurfaceVariant, fontSize: 13))
                : Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        '${_selected!.emoji} ${_selected!.name}  ·  ${_levelNames[_selected!.trophicLevel]}',
                        style: TextStyle(fontWeight: FontWeight.bold, color: _levelColors[_selected!.trophicLevel], fontSize: 14),
                      ),
                      const SizedBox(height: 8),
                      Text(
                        _prey.isEmpty ? 'Eats: nothing (it\'s a producer, makes its own food)' : 'Eats: ${_prey.map((p) => '${p.emoji} ${p.name}').join(', ')}',
                        style: TextStyle(fontSize: 13),
                      ),
                      const SizedBox(height: 4),
                      Text(
                        _predators.isEmpty ? 'Eaten by: nothing (it\'s a top predator here)' : 'Eaten by: ${_predators.map((p) => '${p.emoji} ${p.name}').join(', ')}',
                        style: TextStyle(fontSize: 13),
                      ),
                    ],
                  ),
          ),
        ],
      ),
    );
  }
}
