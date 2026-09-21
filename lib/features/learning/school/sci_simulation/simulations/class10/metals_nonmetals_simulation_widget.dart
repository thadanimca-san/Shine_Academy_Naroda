import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// The reactivity series as a tappable ladder: pick two metals and see
/// whether the more reactive one can displace the other from a salt
/// solution.
class MetalsNonmetalsSimulationWidget extends StatefulWidget {
  const MetalsNonmetalsSimulationWidget({super.key});

  @override
  State<MetalsNonmetalsSimulationWidget> createState() => _MetalsNonmetalsSimulationWidgetState();
}

class _MetalsNonmetalsSimulationWidgetState extends State<MetalsNonmetalsSimulationWidget> {
  static const _series = ['Potassium', 'Sodium', 'Calcium', 'Magnesium', 'Aluminium', 'Zinc', 'Iron', 'Copper', 'Silver', 'Gold'];

  int _metalA = 5; // Zinc
  int _metalB = 7; // Copper

  @override
  Widget build(BuildContext context) {
    final aMoreReactive = _metalA < _metalB;
    final displaces = _metalA != _metalB && aMoreReactive;

    return SimFrame(
      title: 'The Reactivity Series',
      icon: Icons.stacked_bar_chart,
      accent: Colors.blueGrey.shade700,
      description: 'Pick a metal and dip it into a salt solution of another metal to see if a displacement reaction occurs.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(color: Colors.blueGrey.shade50, borderRadius: BorderRadius.circular(10)),
            child: Column(
              children: _series.asMap().entries.map((e) {
                final isA = e.key == _metalA;
                final isB = e.key == _metalB;
                return Padding(
                  padding: const EdgeInsets.symmetric(vertical: 2),
                  child: Row(
                    children: [
                      SizedBox(width: 20, child: Text('${e.key + 1}', style: TextStyle(fontSize: 10, color: Theme.of(context).colorScheme.onSurface.withOpacity(0.45)))),
                      Expanded(
                        child: Container(
                          padding: const EdgeInsets.symmetric(vertical: 4, horizontal: 8),
                          decoration: BoxDecoration(
                            color: isA ? Colors.blue.shade100 : (isB ? Colors.orange.shade100 : Colors.transparent),
                            borderRadius: BorderRadius.circular(4),
                          ),
                          child: Text(e.value, style: TextStyle(fontSize: 12.5, fontWeight: (isA || isB) ? FontWeight.bold : FontWeight.normal)),
                        ),
                      ),
                    ],
                  ),
                );
              }).toList(),
            ),
          ),
          const SizedBox(height: 12),
          Row(
            children: [
              Expanded(
                child: DropdownButtonFormField<int>(
                  initialValue: _metalA,
                  decoration: const InputDecoration(labelText: 'Metal (dipped in)', isDense: true, border: OutlineInputBorder()),
                  items: _series.asMap().entries.map((e) => DropdownMenuItem(value: e.key, child: Text(e.value, style: TextStyle(fontSize: 13)))).toList(),
                  onChanged: (val) => setState(() => _metalA = val!),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: DropdownButtonFormField<int>(
                  initialValue: _metalB,
                  decoration: const InputDecoration(labelText: 'Salt solution of', isDense: true, border: OutlineInputBorder()),
                  items: _series.asMap().entries.map((e) => DropdownMenuItem(value: e.key, child: Text(e.value, style: TextStyle(fontSize: 13)))).toList(),
                  onChanged: (val) => setState(() => _metalB = val!),
                ),
              ),
            ],
          ),
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: displaces ? Colors.green.shade50 : Colors.red.shade50, borderRadius: BorderRadius.circular(10)),
            child: Text(
              _metalA == _metalB
                  ? 'Same metal — no reaction.'
                  : (displaces
                      ? '${_series[_metalA]} is more reactive than ${_series[_metalB]} — it displaces ${_series[_metalB]} from its salt solution.'
                      : '${_series[_metalA]} is less reactive than ${_series[_metalB]} — no displacement reaction occurs.'),
              style: TextStyle(fontWeight: FontWeight.w600, color: displaces ? Colors.green.shade800 : Colors.red.shade800, fontSize: 13),
            ),
          ),
        ],
      ),
    );
  }
}
