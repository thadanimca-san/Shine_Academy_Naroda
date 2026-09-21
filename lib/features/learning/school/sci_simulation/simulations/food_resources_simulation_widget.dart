import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Season {
  final String name;
  final String months;
  final String description;
  final Color color;
  final IconData icon;
  final List<String> crops;

  const _Season(this.name, this.months, this.description, this.color, this.icon, this.crops);
}

/// An interactive crop-season calendar for "Improvement in Food Resources":
/// pick Kharif or Rabi to see the growing months, climate needs, and the
/// crops that get sown then.
class FoodResourcesSimulationWidget extends StatefulWidget {
  const FoodResourcesSimulationWidget({super.key});

  @override
  State<FoodResourcesSimulationWidget> createState() => _FoodResourcesSimulationWidgetState();
}

class _FoodResourcesSimulationWidgetState extends State<FoodResourcesSimulationWidget> {
  static const _seasons = [
    _Season('Kharif', 'June – October (Rainy season)', 'Sown with the onset of monsoon; needs warm, wet conditions to germinate and grow.',
        Color(0xFF2E7D32), Icons.water, ['Paddy (Rice)', 'Maize', 'Soyabean', 'Cotton', 'Groundnut']),
    _Season('Rabi', 'November – April (Winter season)', 'Sown after the monsoon retreats; needs cool weather to grow and warm weather to mature and flower.',
        Color(0xFFEF6C00), Icons.ac_unit, ['Wheat', 'Gram (Chana)', 'Mustard', 'Peas', 'Linseed']),
  ];

  int _selectedIndex = 0;

  @override
  Widget build(BuildContext context) {
    final season = _seasons[_selectedIndex];

    return SimFrame(
      title: 'Crop Season Calendar',
      icon: Icons.agriculture,
      accent: Colors.brown.shade600,
      description: 'India\'s major cropping seasons drive which crops farmers sow — tap a season to explore it.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: _seasons.asMap().entries.map((entry) {
              final i = entry.key;
              final s = entry.value;
              final isSelected = i == _selectedIndex;
              return Expanded(
                child: GestureDetector(
                  onTap: () => setState(() => _selectedIndex = i),
                  child: AnimatedContainer(
                    duration: const Duration(milliseconds: 250),
                    margin: EdgeInsets.only(right: i == 0 ? 8 : 0),
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    decoration: BoxDecoration(
                      color: isSelected ? s.color : s.color.withValues(alpha: 0.12),
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: s.color, width: isSelected ? 0 : 1.4),
                    ),
                    child: Column(
                      children: [
                        Icon(s.icon, color: isSelected ? Colors.white : s.color, size: 28),
                        const SizedBox(height: 6),
                        Text(s.name, style: TextStyle(fontWeight: FontWeight.bold, color: isSelected ? Colors.white : s.color)),
                      ],
                    ),
                  ),
                ),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(color: season.color.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12), border: Border.all(color: season.color.withValues(alpha: 0.3))),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(children: [
                  Icon(Icons.calendar_month, size: 16, color: season.color),
                  const SizedBox(width: 6),
                  Text(season.months, style: TextStyle(fontWeight: FontWeight.w600, color: season.color)),
                ]),
                const SizedBox(height: 8),
                Text(season.description, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText('Typical Crops'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
          const SizedBox(height: 8),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: season.crops.map((c) {
              return Chip(
                avatar: Icon(Icons.eco, size: 16, color: season.color),
                label: Text(c, style: TextStyle(fontSize: 12.5)),
                backgroundColor: season.color.withValues(alpha: 0.1),
                side: BorderSide(color: season.color.withValues(alpha: 0.3)),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
