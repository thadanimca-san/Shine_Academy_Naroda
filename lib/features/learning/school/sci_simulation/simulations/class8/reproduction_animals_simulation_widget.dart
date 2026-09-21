import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Compares the two modes of reproduction — sexual (fusion of gametes) and
/// asexual (single parent) — and lets students step through each type's
/// examples.
class ReproductionAnimalsSimulationWidget extends StatefulWidget {
  const ReproductionAnimalsSimulationWidget({super.key});

  @override
  State<ReproductionAnimalsSimulationWidget> createState() => _ReproductionAnimalsSimulationWidgetState();
}

class _ReproductionAnimalsSimulationWidgetState extends State<ReproductionAnimalsSimulationWidget> {
  bool _isSexual = true;
  int _exampleIndex = 0;

  static const _sexualExamples = [
    ('Internal Fertilisation', 'Sperm meets egg inside the female\'s body. Seen in humans, cows, hens.', Icons.pets),
    ('External Fertilisation', 'Sperm meets egg outside the body, usually in water. Seen in fish and frogs.', Icons.water),
    ('Viviparous', 'The embryo develops inside the mother, who gives birth to live young. E.g. humans, dogs.', Icons.child_care),
    ('Oviparous', 'The fertilised egg is laid, and the embryo develops outside the body. E.g. birds, reptiles.', Icons.egg),
  ];

  static const _asexualExamples = [
    ('Binary Fission', 'A single parent cell splits into two identical daughter cells. Seen in Amoeba.', Icons.call_split),
    ('Budding', 'A new individual grows as an outgrowth (bud) from the parent\'s body. Seen in Hydra.', Icons.spa),
  ];

  @override
  Widget build(BuildContext context) {
    final examples = _isSexual ? _sexualExamples : _asexualExamples;
    final idx = _exampleIndex.clamp(0, examples.length - 1);
    final example = examples[idx];

    return SimFrame(
      title: 'Modes of Reproduction',
      icon: Icons.pets,
      accent: Colors.pink.shade600,
      description: 'Compare sexual and asexual reproduction and their examples.',
      actions: [
        ToggleButtons(
          isSelected: [_isSexual, !_isSexual],
          onPressed: (i) => setState(() {
            _isSexual = i == 0;
            _exampleIndex = 0;
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.pink.shade600,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 58),
          children: [Text(TrilingualService.instance.getUIText('Sexual')), Text(TrilingualService.instance.getUIText('Asexual'))],
        ),
      ],
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(color: Colors.pink.shade50, borderRadius: BorderRadius.circular(12)),
            child: Column(
              children: [
                Icon(example.$3, size: 42, color: Colors.pink.shade700),
                const SizedBox(height: 10),
                Text(example.$1, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15, color: Colors.pink.shade900)),
                const SizedBox(height: 6),
                Text(example.$2, textAlign: TextAlign.center, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            children: examples.asMap().entries.map((e) {
              final isSelected = e.key == idx;
              return ChoiceChip(
                label: Text(e.value.$1, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.pink.shade600,
                backgroundColor: Colors.pink.shade50,
                onSelected: (_) => setState(() => _exampleIndex = e.key),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
