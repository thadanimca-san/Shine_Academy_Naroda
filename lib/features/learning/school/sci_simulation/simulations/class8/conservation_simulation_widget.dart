import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Species {
  final String name;
  final String status; // Endangered / Extinct / Least Concern
  final String note;
  final Color color;

  const _Species(this.name, this.status, this.note, this.color);
}

/// An explorer of conservation status: tap a species to see whether it's
/// endangered, extinct, or of least concern, and why.
class ConservationSimulationWidget extends StatefulWidget {
  const ConservationSimulationWidget({super.key});

  @override
  State<ConservationSimulationWidget> createState() => _ConservationSimulationWidgetState();
}

class _ConservationSimulationWidgetState extends State<ConservationSimulationWidget> {
  static const _species = [
    _Species('Bengal Tiger', 'Endangered', 'Threatened by poaching and habitat loss; protected under Project Tiger.', Colors.orange),
    _Species('Great Indian Bustard', 'Endangered', 'One of the heaviest flying birds; population critically low due to habitat loss.', Colors.brown),
    _Species('Dodo', 'Extinct', 'A flightless bird that went extinct in the 17th century due to hunting and habitat destruction.', Colors.grey),
    _Species('Asiatic Cheetah (India)', 'Extinct', 'Declared extinct in India in 1952, mainly due to hunting and habitat loss.', Colors.blueGrey),
    _Species('House Sparrow', 'Least Concern', 'Still common, though declining in cities due to pollution and lack of nesting spaces.', Colors.green),
    _Species('Indian Peafowl', 'Least Concern', 'India\'s national bird; stable population, legally protected from hunting.', Colors.teal),
  ];

  _Species _selected = _species[0];

  Color _statusColor(String status) {
    switch (status) {
      case 'Extinct':
        return Colors.grey.shade700;
      case 'Endangered':
        return Colors.red.shade700;
      default:
        return Colors.green.shade700;
    }
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Conservation Status Explorer',
      icon: Icons.forest,
      accent: Colors.green.shade800,
      description: 'Tap a species to see its conservation status and why it matters.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _species.map((s) {
              final isSelected = _selected.name == s.name;
              final color = _statusColor(s.status);
              return ChoiceChip(
                label: Text(s.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: color,
                backgroundColor: color.withValues(alpha: 0.12),
                onSelected: (_) => setState(() => _selected = s),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: _statusColor(_selected.status).withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12), border: Border.all(color: _statusColor(_selected.status).withValues(alpha: 0.3))),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(
                  children: [
                    Text(_selected.name, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15)),
                    const Spacer(),
                    Chip(label: Text(_selected.status, style: TextStyle(color: Colors.white, fontSize: 11)), backgroundColor: _statusColor(_selected.status)),
                  ],
                ),
                const SizedBox(height: 8),
                Text(_selected.note, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
