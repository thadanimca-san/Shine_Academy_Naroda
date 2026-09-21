import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Organ {
  final String name;
  final String function;
  final IconData icon;
  final Color color;

  const _Organ(this.name, this.function, this.icon, this.color);
}

/// Steps a food bolus through the human digestive tract: tap Next to move
/// it from mouth to large intestine, seeing what each organ does along
/// the way.
class NutritionAnimalsSimulationWidget extends StatefulWidget {
  const NutritionAnimalsSimulationWidget({super.key});

  @override
  State<NutritionAnimalsSimulationWidget> createState() => _NutritionAnimalsSimulationWidgetState();
}

class _NutritionAnimalsSimulationWidgetState extends State<NutritionAnimalsSimulationWidget> {
  static const _organs = [
    _Organ('Mouth', 'Teeth break food into small pieces; saliva begins starch digestion.', Icons.emoji_emotions, Colors.orange),
    _Organ('Oesophagus', 'A muscular tube that pushes food down to the stomach.', Icons.arrow_downward, Colors.deepOrange),
    _Organ('Stomach', 'Churns food with acid and enzymes, killing germs and breaking down proteins.', Icons.circle, Colors.red),
    _Organ('Small Intestine', 'Bile and pancreatic juices complete digestion; digested food is absorbed into blood.', Icons.route, Colors.green),
    _Organ('Large Intestine', 'Absorbs water from undigested food, forming solid waste.', Icons.horizontal_rule, Colors.brown),
  ];

  int _index = 0;

  @override
  Widget build(BuildContext context) {
    final organ = _organs[_index];

    return SimFrame(
      title: 'Journey Through the Digestive System',
      icon: Icons.emoji_food_beverage,
      accent: Colors.deepOrange.shade400,
      description: 'Step the food bolus through each organ and see what happens to it.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 140,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.orange.shade50, borderRadius: BorderRadius.circular(10)),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: _organs.asMap().entries.map((e) {
                final passed = e.key <= _index;
                return Column(
                  mainAxisAlignment: MainAxisAlignment.center,
                  children: [
                    Icon(e.value.icon, color: passed ? e.value.color : Colors.grey.shade300, size: e.key == _index ? 30 : 20),
                    if (e.key == _index) Icon(Icons.circle, size: 8, color: e.value.color),
                  ],
                );
              }).toList(),
            ),
          ),
          const SizedBox(height: 12),
          Text('${_index + 1}. ${organ.name}', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15, color: organ.color)),
          const SizedBox(height: 6),
          Text(organ.function, style: TextStyle(fontSize: 13)),
          const SizedBox(height: 14),
          LinearProgressIndicator(value: (_index + 1) / _organs.length, minHeight: 6, color: organ.color, backgroundColor: Colors.grey.shade200),
          const SizedBox(height: 14),
          Row(
            children: [
              Expanded(
                child: OutlinedButton.icon(
                  onPressed: _index == 0 ? null : () => setState(() => _index--),
                  icon: Icon(Icons.arrow_back),
                  label: Text(TrilingualService.instance.getUIText('Previous')),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: _index == _organs.length - 1 ? null : () => setState(() => _index++),
                  icon: Icon(Icons.arrow_forward),
                  label: Text(TrilingualService.instance.getUIText('Next')),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.deepOrange.shade400, foregroundColor: Colors.white),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
