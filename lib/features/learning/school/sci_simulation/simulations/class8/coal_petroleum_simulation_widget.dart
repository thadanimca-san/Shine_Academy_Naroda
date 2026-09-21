import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Fraction {
  final String name;
  final String use;
  final Color color;

  const _Fraction(this.name, this.use, this.color);
}

/// A schematic fractional distillation column: petroleum is heated and its
/// components separate into layers by boiling point. Tap a band to see
/// what that fraction is used for.
class CoalPetroleumSimulationWidget extends StatefulWidget {
  const CoalPetroleumSimulationWidget({super.key});

  @override
  State<CoalPetroleumSimulationWidget> createState() => _CoalPetroleumSimulationWidgetState();
}

class _CoalPetroleumSimulationWidgetState extends State<CoalPetroleumSimulationWidget> {
  static const _fractions = [
    _Fraction('Petroleum Gas', 'Used as LPG for cooking fuel.', Color(0xFF81D4FA)),
    _Fraction('Petrol', 'Fuel for cars and light vehicles.', Color(0xFFFFD54F)),
    _Fraction('Kerosene', 'Used as fuel for stoves and lamps.', Color(0xFFFFB74D)),
    _Fraction('Diesel', 'Fuel for heavy vehicles, trucks and generators.', Color(0xFFA1887F)),
    _Fraction('Lubricating Oil', 'Reduces friction in machine parts.', Color(0xFF8D6E63)),
    _Fraction('Bitumen', 'Used for surfacing roads.', Color(0xFF4E342E)),
  ];

  int _selectedIndex = 1;

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Fractional Distillation of Petroleum',
      icon: Icons.local_gas_station,
      accent: Colors.brown.shade700,
      description: 'Petroleum is heated; lighter fractions rise higher in the column and are collected separately by boiling point. Tap a band.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            height: 220,
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.stretch,
              children: [
                Expanded(
                  child: Column(
                    children: _fractions.asMap().entries.map((entry) {
                      final i = entry.key;
                      final f = entry.value;
                      final isSelected = i == _selectedIndex;
                      return Expanded(
                        child: GestureDetector(
                          onTap: () => setState(() => _selectedIndex = i),
                          child: Container(
                            width: double.infinity,
                            margin: const EdgeInsets.symmetric(vertical: 1),
                            decoration: BoxDecoration(
                              color: f.color,
                              border: isSelected ? Border.all(color: Theme.of(context).colorScheme.onSurface, width: 2) : null,
                            ),
                            alignment: Alignment.center,
                            child: Text(f.name, style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold, color: i < 2 ? Colors.black87 : Colors.white)),
                          ),
                        ),
                      );
                    }).toList(),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 4),
          Text(TrilingualService.instance.getUIText('↑ lighter, lower boiling point         heavier, higher boiling point ↓'), style: TextStyle(fontSize: 10, color: Theme.of(context).colorScheme.onSurface.withOpacity(0.45))),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: _fractions[_selectedIndex].color.withValues(alpha: 0.15), borderRadius: BorderRadius.circular(10)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(_fractions[_selectedIndex].name, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
                const SizedBox(height: 4),
                Text(_fractions[_selectedIndex].use, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
