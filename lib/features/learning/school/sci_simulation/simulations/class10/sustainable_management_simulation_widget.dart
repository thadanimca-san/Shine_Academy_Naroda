import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Action {
  final String name;
  final String category; // Reduce, Reuse, Recycle
  final IconData icon;

  const _Action(this.name, this.category, this.icon);
}

/// A sorter for the 3 Rs: tap an everyday action and see whether it
/// counts as reducing, reusing, or recycling a resource.
class SustainableManagementSimulationWidget extends StatefulWidget {
  const SustainableManagementSimulationWidget({super.key});

  @override
  State<SustainableManagementSimulationWidget> createState() => _SustainableManagementSimulationWidgetState();
}

class _SustainableManagementSimulationWidgetState extends State<SustainableManagementSimulationWidget> {
  static const _actions = [
    _Action('Turning off unused lights', 'Reduce', Icons.lightbulb_outline),
    _Action('Taking shorter showers', 'Reduce', Icons.shower),
    _Action('Using a cloth bag again', 'Reuse', Icons.shopping_bag),
    _Action('Refilling a glass bottle', 'Reuse', Icons.local_drink),
    _Action('Making new paper from old paper', 'Recycle', Icons.description),
    _Action('Melting plastic to make new items', 'Recycle', Icons.recycling),
    _Action('Buying only what you need', 'Reduce', Icons.shopping_cart_checkout),
    _Action('Donating old clothes', 'Reuse', Icons.checkroom),
  ];

  static const _colors = {'Reduce': Color(0xFF66BB6A), 'Reuse': Color(0xFF42A5F5), 'Recycle': Color(0xFFFFA726)};

  _Action _selected = _actions[0];

  @override
  Widget build(BuildContext context) {
    final color = _colors[_selected.category]!;

    return SimFrame(
      title: 'Reduce, Reuse, Recycle',
      icon: Icons.recycling,
      accent: Colors.green.shade700,
      description: 'Tap an everyday action to see which of the 3 Rs it belongs to.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _actions.map((a) {
              final isSelected = _selected.name == a.name;
              final c = _colors[a.category]!;
              return ChoiceChip(
                avatar: Icon(a.icon, size: 16, color: isSelected ? Colors.white : c),
                label: Text(a.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: c,
                backgroundColor: c.withValues(alpha: 0.12),
                onSelected: (_) => setState(() => _selected = a),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(color: color.withValues(alpha: 0.1), borderRadius: BorderRadius.circular(12), border: Border.all(color: color.withValues(alpha: 0.3))),
            child: Column(
              children: [
                Icon(_selected.icon, size: 34, color: color),
                const SizedBox(height: 8),
                Text(_selected.name, style: TextStyle(fontWeight: FontWeight.w600, fontSize: 13), textAlign: TextAlign.center),
                const SizedBox(height: 8),
                Chip(label: Text(_selected.category, style: TextStyle(color: Colors.white)), backgroundColor: color),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
