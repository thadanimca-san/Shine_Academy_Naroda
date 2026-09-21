import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Animal {
  final String name;
  final String adaptation;
  final IconData icon;

  const _Animal(this.name, this.adaptation, this.icon);
}

/// Toggle between polar and tropical rainforest climates and see which
/// animals live there and how they've adapted to survive.
class WeatherClimateSimulationWidget extends StatefulWidget {
  const WeatherClimateSimulationWidget({super.key});

  @override
  State<WeatherClimateSimulationWidget> createState() => _WeatherClimateSimulationWidgetState();
}

class _WeatherClimateSimulationWidgetState extends State<WeatherClimateSimulationWidget> {
  bool _isPolar = true;
  int _index = 0;

  static const _polarAnimals = [
    _Animal('Polar Bear', 'A thick fat layer (blubber) and white fur keep it warm and camouflaged in snow.', Icons.pets),
    _Animal('Penguin', 'Huddles in large groups and has layers of feathers to conserve body heat.', Icons.ac_unit),
    _Animal('Arctic Fox', 'Small ears and a rounded body minimise heat loss in freezing temperatures.', Icons.cruelty_free),
  ];

  static const _tropicalAnimals = [
    _Animal('Toucan', 'A large beak helps it reach and eat fruit deep within dense trees.', Icons.flutter_dash),
    _Animal('Red-Eyed Tree Frog', 'Bright colours help startle predators and blend with leaves.', Icons.bug_report),
    _Animal('Sloth', 'Slow movement and green-tinted fur (from algae) help it stay camouflaged.', Icons.forest),
  ];

  @override
  Widget build(BuildContext context) {
    final animals = _isPolar ? _polarAnimals : _tropicalAnimals;
    final idx = _index.clamp(0, animals.length - 1);
    final animal = animals[idx];
    final accent = _isPolar ? Colors.lightBlue.shade700 : Colors.green.shade700;

    return SimFrame(
      title: 'Climate & Animal Adaptations',
      icon: Icons.public,
      accent: accent,
      description: 'Switch climates and tap through animals to see how each is adapted to survive there.',
      actions: [
        ToggleButtons(
          isSelected: [_isPolar, !_isPolar],
          onPressed: (i) => setState(() {
            _isPolar = i == 0;
            _index = 0;
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: accent,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 56),
          children: [Text(TrilingualService.instance.getUIText('Polar')), Text(TrilingualService.instance.getUIText('Tropical'))],
        ),
      ],
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(
              gradient: LinearGradient(colors: _isPolar ? [Colors.lightBlue.shade50, Colors.white] : [Colors.green.shade50, Colors.white]),
              borderRadius: BorderRadius.circular(12),
            ),
            child: Column(
              children: [
                Icon(animal.icon, size: 46, color: accent),
                const SizedBox(height: 10),
                Text(animal.name, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15, color: accent)),
                const SizedBox(height: 8),
                Text(animal.adaptation, textAlign: TextAlign.center, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            children: animals.asMap().entries.map((e) {
              final isSelected = e.key == idx;
              return ChoiceChip(
                label: Text(e.value.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: accent,
                backgroundColor: accent.withValues(alpha: 0.1),
                onSelected: (_) => setState(() => _index = e.key),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
