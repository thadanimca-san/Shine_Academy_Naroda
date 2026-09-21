import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Organ {
  final String name;
  final String function;
  final Color color;

  const _Organ(this.name, this.function, this.color);
}

/// Toggle between the male and female reproductive systems and tap
/// through their key organs to learn each one's role.
class ReproductionSimulationWidget extends StatefulWidget {
  const ReproductionSimulationWidget({super.key});

  @override
  State<ReproductionSimulationWidget> createState() => _ReproductionSimulationWidgetState();
}

class _ReproductionSimulationWidgetState extends State<ReproductionSimulationWidget> {
  bool _isFemale = true;
  int _index = 0;

  static const _maleOrgans = [
    _Organ('Testes', 'Produce sperm and the hormone testosterone.', Color(0xFF26A69A)),
    _Organ('Vas Deferens', 'Carries sperm from the testes toward the urethra.', Color(0xFF42A5F5)),
    _Organ('Urethra', 'A common passage for sperm and urine, out of the body.', Color(0xFF7E57C2)),
  ];

  static const _femaleOrgans = [
    _Organ('Ovaries', 'Produce eggs (ova) and hormones like estrogen.', Color(0xFFEC407A)),
    _Organ('Fallopian Tube', 'The site of fertilisation, carrying the egg toward the uterus.', Color(0xFFAB47BC)),
    _Organ('Uterus', 'Where a fertilised egg implants and the embryo develops until birth.', Color(0xFFFF7043)),
  ];

  @override
  Widget build(BuildContext context) {
    final organs = _isFemale ? _femaleOrgans : _maleOrgans;
    final idx = _index.clamp(0, organs.length - 1);
    final organ = organs[idx];

    return SimFrame(
      title: 'The Reproductive System',
      icon: Icons.family_restroom,
      accent: organ.color,
      description: 'Switch between systems and tap through the key organs to learn their function.',
      actions: [
        ToggleButtons(
          isSelected: [!_isFemale, _isFemale],
          onPressed: (i) => setState(() {
            _isFemale = i == 1;
            _index = 0;
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.pink.shade400,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 50),
          children: [Text(TrilingualService.instance.getUIText('Male')), Text(TrilingualService.instance.getUIText('Female'))],
        ),
      ],
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(18),
            decoration: BoxDecoration(color: organ.color.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12)),
            child: Column(
              children: [
                Icon(Icons.circle, size: 40, color: organ.color),
                const SizedBox(height: 10),
                Text(organ.name, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15, color: organ.color)),
                const SizedBox(height: 8),
                Text(organ.function, textAlign: TextAlign.center, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            children: organs.asMap().entries.map((e) {
              final isSelected = e.key == idx;
              return ChoiceChip(
                label: Text(e.value.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: e.value.color,
                backgroundColor: e.value.color.withValues(alpha: 0.1),
                onSelected: (_) => setState(() => _index = e.key),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
