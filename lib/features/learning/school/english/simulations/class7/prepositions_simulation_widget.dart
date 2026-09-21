import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A visual preposition picker: choose "in / on / under / above /
/// beside" and watch a ball move around a box to match — the spatial
/// relationship becomes literally visible.
class PrepositionsSimulationWidget extends StatefulWidget {
  const PrepositionsSimulationWidget({super.key});

  @override
  State<PrepositionsSimulationWidget> createState() => _PrepositionsSimulationWidgetState();
}

class _PrepositionsSimulationWidgetState extends State<PrepositionsSimulationWidget> {
  static const _prepositions = ['in', 'on', 'under', 'above', 'beside'];
  String _selected = 'on';

  Alignment get _ballAlignment {
    switch (_selected) {
      case 'in':
        return Alignment.center;
      case 'under':
        return const Alignment(0, 1.8);
      case 'above':
        return const Alignment(0, -1.8);
      case 'beside':
        return const Alignment(1.8, 0);
      default: // on
        return const Alignment(0, -1.05);
    }
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Prepositions of Place',
      icon: Icons.place,
      accent: Colors.orange.shade700,
      description: 'Pick a preposition and watch the ball move relative to the box — "The ball is $_selected the box."',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 190,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.orange.shade50, borderRadius: BorderRadius.circular(10)),
            child: Stack(
              alignment: Alignment.center,
              children: [
                Container(width: 90, height: 70, decoration: BoxDecoration(border: Border.all(color: Colors.brown.shade700, width: 3), borderRadius: BorderRadius.circular(6))),
                AnimatedAlign(
                  duration: const Duration(milliseconds: 400),
                  alignment: _ballAlignment,
                  child: Container(width: 28, height: 28, decoration: BoxDecoration(color: Colors.deepOrange, shape: BoxShape.circle)),
                ),
              ],
            ),
          ),
          const SizedBox(height: 4),
          Center(child: Text('The ball is $_selected the box.', style: TextStyle(fontWeight: FontWeight.w600))),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            children: _prepositions.map((p) {
              final isSelected = _selected == p;
              return ChoiceChip(
                label: Text(p, style: TextStyle(fontSize: 13, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.orange.shade700,
                backgroundColor: Colors.orange.shade50,
                onSelected: (_) => setState(() => _selected = p),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
