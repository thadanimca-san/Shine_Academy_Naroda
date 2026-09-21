import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Element {
  final String symbol;
  final int period;
  final int group;
  final Color color;

  const _Element(this.symbol, this.period, this.group, this.color);
}

/// A simplified periodic table grid: tap any element to see how atomic
/// size and metallic character trend across its period and down its group.
class PeriodicClassificationSimulationWidget extends StatefulWidget {
  const PeriodicClassificationSimulationWidget({super.key});

  @override
  State<PeriodicClassificationSimulationWidget> createState() => _PeriodicClassificationSimulationWidgetState();
}

class _PeriodicClassificationSimulationWidgetState extends State<PeriodicClassificationSimulationWidget> {
  static const _elements = [
    _Element('Li', 2, 1, Color(0xFFEF5350)), _Element('Be', 2, 2, Color(0xFFEF9A9A)), _Element('B', 2, 13, Color(0xFF90A4AE)),
    _Element('C', 2, 14, Color(0xFF78909C)), _Element('N', 2, 15, Color(0xFF78909C)), _Element('O', 2, 16, Color(0xFF78909C)), _Element('F', 2, 17, Color(0xFF66BB6A)), _Element('Ne', 2, 18, Color(0xFF42A5F5)),
    _Element('Na', 3, 1, Color(0xFFEF5350)), _Element('Mg', 3, 2, Color(0xFFEF9A9A)), _Element('Al', 3, 13, Color(0xFF90A4AE)),
    _Element('Si', 3, 14, Color(0xFF78909C)), _Element('P', 3, 15, Color(0xFF78909C)), _Element('S', 3, 16, Color(0xFF78909C)), _Element('Cl', 3, 17, Color(0xFF66BB6A)), _Element('Ar', 3, 18, Color(0xFF42A5F5)),
  ];

  _Element _selected = _elements[8]; // Na

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Periodic Trends Explorer',
      icon: Icons.grid_view,
      accent: Colors.indigo.shade600,
      description: 'Tap an element to see how atomic size shrinks across a period and grows down a group.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 4,
            runSpacing: 4,
            children: _elements.map((e) {
              final isSelected = _selected.symbol == e.symbol;
              final sameGroup = e.group == _selected.group;
              final samePeriod = e.period == _selected.period;
              return GestureDetector(
                onTap: () => setState(() => _selected = e),
                child: Container(
                  width: 40,
                  height: 40,
                  decoration: BoxDecoration(
                    color: e.color,
                    borderRadius: BorderRadius.circular(6),
                    border: Border.all(
                      color: isSelected ? Colors.black87 : ((sameGroup || samePeriod) ? Colors.white : Colors.transparent),
                      width: isSelected ? 2.5 : 1.5,
                    ),
                  ),
                  alignment: Alignment.center,
                  child: Text(e.symbol, style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 12)),
                ),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Element', value: _selected.symbol, color: _selected.color),
            SimMetric(label: 'Period', value: '${_selected.period}'),
            SimMetric(label: 'Group', value: '${_selected.group}'),
          ]),
          const SizedBox(height: 10),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.indigo.shade50, borderRadius: BorderRadius.circular(10)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('Across Period ${_selected.period} (left → right): atomic size decreases, metallic character decreases.', style: TextStyle(fontSize: 12.5)),
                const SizedBox(height: 4),
                Text('Down Group ${_selected.group} (top → bottom): atomic size increases, metallic character increases.', style: TextStyle(fontSize: 12.5)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
