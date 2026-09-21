import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _AdjSet {
  final String positive, comparative, superlative;
  const _AdjSet(this.positive, this.comparative, this.superlative);
}

/// A degrees-of-comparison ladder: pick an adjective and a number of
/// things being compared, and see which degree (positive, comparative,
/// superlative) applies, with the correct word form shown.
class AdjectivesSimulationWidget extends StatefulWidget {
  const AdjectivesSimulationWidget({super.key});

  @override
  State<AdjectivesSimulationWidget> createState() => _AdjectivesSimulationWidgetState();
}

class _AdjectivesSimulationWidgetState extends State<AdjectivesSimulationWidget> {
  static const _adjectives = [
    _AdjSet('tall', 'taller', 'tallest'),
    _AdjSet('big', 'bigger', 'biggest'),
    _AdjSet('happy', 'happier', 'happiest'),
    _AdjSet('good', 'better', 'best'),
    _AdjSet('bad', 'worse', 'worst'),
    _AdjSet('beautiful', 'more beautiful', 'most beautiful'),
    _AdjSet('careful', 'more careful', 'most careful'),
  ];

  int _adjIndex = 0;
  int _numCompared = 1; // 1 = positive, 2 = comparative, 3+ = superlative

  @override
  Widget build(BuildContext context) {
    final adj = _adjectives[_adjIndex];
    final degree = _numCompared == 1 ? 'Positive' : (_numCompared == 2 ? 'Comparative' : 'Superlative');
    final word = _numCompared == 1 ? adj.positive : (_numCompared == 2 ? adj.comparative : adj.superlative);
    final color = _numCompared == 1 ? Colors.blue : (_numCompared == 2 ? Colors.teal : Colors.deepOrange);

    return SimFrame(
      title: 'Degrees of Comparison',
      icon: Icons.stairs,
      accent: Colors.purple.shade600,
      description: 'Change how many things are being compared and watch the adjective form change.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            children: _adjectives.asMap().entries.map((e) {
              final isSelected = e.key == _adjIndex;
              return ChoiceChip(
                label: Text(e.value.positive, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.purple.shade600,
                backgroundColor: Colors.purple.shade50,
                onSelected: (_) => setState(() => _adjIndex = e.key),
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
                Text(word, style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold, color: color)),
                const SizedBox(height: 8),
                Text('$degree Degree', style: TextStyle(fontSize: 14, color: color)),
              ],
            ),
          ),
          const SizedBox(height: 16),
          Text(TrilingualService.instance.getUIText('Number of things being compared:'), style: TextStyle(fontWeight: FontWeight.w600, fontSize: 13)),
          const SizedBox(height: 8),
          Row(
            children: [1, 2, 3].map((n) {
              final isSelected = _numCompared == n;
              final label = n == 1 ? '1 (no comparison)' : (n == 2 ? '2 things' : '3+ things');
              return Expanded(
                child: Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 4),
                  child: ChoiceChip(
                    label: Text(label, style: TextStyle(fontSize: 11, color: isSelected ? Colors.white : Colors.black87)),
                    selected: isSelected,
                    selectedColor: Colors.purple.shade600,
                    backgroundColor: Colors.purple.shade50,
                    onSelected: (_) => setState(() => _numCompared = n),
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
