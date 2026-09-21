import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _AdjSet {
  final String positive, comparative, superlative;
  const _AdjSet(this.positive, this.comparative, this.superlative);
}

/// A degrees-of-comparison explorer focused on irregular forms (good/
/// bad/little/many), showing how the word changes entirely rather than
/// just adding -er/-est.
class DegreesComparisonSimulationWidget extends StatefulWidget {
  const DegreesComparisonSimulationWidget({super.key});

  @override
  State<DegreesComparisonSimulationWidget> createState() => _DegreesComparisonSimulationWidgetState();
}

class _DegreesComparisonSimulationWidgetState extends State<DegreesComparisonSimulationWidget> {
  static const _adjectives = [
    _AdjSet('good', 'better', 'best'),
    _AdjSet('bad', 'worse', 'worst'),
    _AdjSet('little', 'less', 'least'),
    _AdjSet('many/much', 'more', 'most'),
    _AdjSet('far', 'farther/further', 'farthest/furthest'),
    _AdjSet('old', 'older/elder', 'oldest/eldest'),
  ];

  int _index = 0;
  int _degree = 0; // 0=positive,1=comparative,2=superlative

  @override
  Widget build(BuildContext context) {
    final adj = _adjectives[_index];
    final word = _degree == 0 ? adj.positive : (_degree == 1 ? adj.comparative : adj.superlative);
    final degreeLabel = _degree == 0 ? 'Positive' : (_degree == 1 ? 'Comparative' : 'Superlative');
    final color = _degree == 0 ? Colors.blue : (_degree == 1 ? Colors.teal : Colors.deepOrange);

    return SimFrame(
      title: 'Irregular Degrees of Comparison',
      icon: Icons.stairs,
      accent: Colors.purple.shade600,
      description: 'Some adjectives change form completely instead of adding -er/-est. Explore them here.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            children: _adjectives.asMap().entries.map((e) {
              final isSelected = e.key == _index;
              return ChoiceChip(
                label: Text(e.value.positive, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.purple.shade600,
                backgroundColor: Colors.purple.shade50,
                onSelected: (_) => setState(() => _index = e.key),
              );
            }).toList(),
          ),
          const SizedBox(height: 16),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(color: color.withValues(alpha: 0.1), borderRadius: BorderRadius.circular(12)),
            child: Column(
              children: [
                Text(word, style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: color), textAlign: TextAlign.center),
                const SizedBox(height: 8),
                Text('$degreeLabel Degree', style: TextStyle(fontSize: 14, color: color)),
              ],
            ),
          ),
          const SizedBox(height: 16),
          Row(
            children: [0, 1, 2].map((d) {
              final isSelected = _degree == d;
              final label = d == 0 ? 'Positive' : (d == 1 ? 'Comparative' : 'Superlative');
              return Expanded(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 4),
                  child: ChoiceChip(
                    label: Text(label, style: TextStyle(fontSize: 11, color: isSelected ? Colors.white : Colors.black87)),
                    selected: isSelected,
                    selectedColor: Colors.purple.shade600,
                    backgroundColor: Colors.purple.shade50,
                    onSelected: (_) => setState(() => _degree = d),
                  ),
                ),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
