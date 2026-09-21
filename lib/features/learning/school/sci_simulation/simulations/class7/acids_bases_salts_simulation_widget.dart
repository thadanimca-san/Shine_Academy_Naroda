import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Substance {
  final String name;
  final bool isAcid; // false = base, null-like neutral handled separately
  final bool isNeutral;
  final Color litmusColor;

  const _Substance(this.name, this.isAcid, this.isNeutral, this.litmusColor);
}

/// A litmus-paper tester: pick a household substance and see the litmus
/// paper change colour, revealing whether it's acidic, basic, or neutral.
class AcidsBasesSaltsSimulationWidget extends StatefulWidget {
  const AcidsBasesSaltsSimulationWidget({super.key});

  @override
  State<AcidsBasesSaltsSimulationWidget> createState() => _AcidsBasesSaltsSimulationWidgetState();
}

class _AcidsBasesSaltsSimulationWidgetState extends State<AcidsBasesSaltsSimulationWidget> {
  static const _substances = [
    _Substance('Lemon Juice', true, false, Colors.red),
    _Substance('Vinegar', true, false, Colors.red),
    _Substance('Baking Soda Solution', false, false, Colors.blue),
    _Substance('Soap Solution', false, false, Colors.blue),
    _Substance('Common Salt Solution', false, true, Colors.purple),
    _Substance('Distilled Water', false, true, Colors.purple),
    _Substance('Antacid Solution', false, false, Colors.blue),
    _Substance('Curd', true, false, Colors.red),
  ];

  _Substance _selected = _substances[0];

  String get _verdict => _selected.isNeutral ? 'Neutral' : (_selected.isAcid ? 'Acidic' : 'Basic');

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Litmus Test Lab',
      icon: Icons.science,
      accent: Colors.purple.shade600,
      description: 'Pick a substance and dip litmus paper in it to see whether it turns red (acid), blue (base), or stays purple (neutral).',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 140,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.grey.shade100, borderRadius: BorderRadius.circular(10)),
            child: Center(
              child: AnimatedContainer(
                duration: const Duration(milliseconds: 400),
                width: 40,
                height: 100,
                decoration: BoxDecoration(color: _selected.litmusColor, borderRadius: BorderRadius.circular(4), border: Border.all(color: Colors.grey.shade400)),
                alignment: Alignment.center,
                child: RotatedBox(quarterTurns: 3, child: Text(TrilingualService.instance.getUIText('litmus'), style: TextStyle(fontSize: 10, color: Colors.white))),
              ),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Substance', value: _selected.name, color: Theme.of(context).colorScheme.onSurface),
            SimMetric(label: 'Nature', value: _verdict, color: _selected.litmusColor),
          ]),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _substances.map((s) {
              final isSelected = _selected.name == s.name;
              return ChoiceChip(
                label: Text(s.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: s.litmusColor,
                backgroundColor: s.litmusColor.withValues(alpha: 0.12),
                onSelected: (_) => setState(() => _selected = s),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
