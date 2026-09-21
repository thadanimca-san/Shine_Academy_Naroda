import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A forest-layer explorer (canopy, understorey, forest floor) combined
/// with a deforestation slider that visibly thins the tree cover.
class ForestsLifelineSimulationWidget extends StatefulWidget {
  const ForestsLifelineSimulationWidget({super.key});

  @override
  State<ForestsLifelineSimulationWidget> createState() => _ForestsLifelineSimulationWidgetState();
}

class _ForestsLifelineSimulationWidgetState extends State<ForestsLifelineSimulationWidget> {
  double _treeCover = 0.9;
  String _selectedLayer = 'Canopy';

  static const _layers = {
    'Canopy': 'The uppermost layer of tall trees that receives maximum sunlight and forms a leafy roof over the forest.',
    'Understorey': 'Shorter trees and shrubs growing beneath the canopy, adapted to less sunlight.',
    'Forest Floor': 'The ground layer where fallen leaves decompose, enriching the soil with nutrients.',
  };

  @override
  Widget build(BuildContext context) {
    final treeCount = (12 * _treeCover).round();

    return SimFrame(
      title: 'Forest Ecosystem',
      icon: Icons.forest,
      accent: Colors.green.shade800,
      description: 'Explore the layered structure of a forest, and see the effect of deforestation on tree cover.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 150,
            width: double.infinity,
            decoration: BoxDecoration(
              gradient: LinearGradient(colors: [Colors.lightBlue.shade100, Colors.green.shade100], begin: Alignment.topCenter, end: Alignment.bottomCenter, stops: const [0, 0.5]),
              borderRadius: BorderRadius.circular(10),
            ),
            child: Wrap(
              alignment: WrapAlignment.center,
              runAlignment: WrapAlignment.end,
              crossAxisAlignment: WrapCrossAlignment.end,
              children: List.generate(12, (i) {
                final visible = i < treeCount;
                return Padding(
                  padding: const EdgeInsets.symmetric(horizontal: 2),
                  child: Icon(Icons.park, size: 32, color: visible ? Colors.green.shade700 : Colors.transparent),
                );
              }),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Tree Cover', value: '${(_treeCover * 100).toStringAsFixed(0)}%', color: Colors.green),
            SimMetric(label: 'Rainfall/Humidity', value: _treeCover > 0.6 ? 'High' : (_treeCover > 0.3 ? 'Moderate' : 'Low'), color: Colors.blue),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Tree cover: ${(_treeCover * 100).toStringAsFixed(0)}% (drag down to simulate deforestation)',
            value: _treeCover,
            min: 0.1,
            max: 1.0,
            divisions: 18,
            activeColor: Colors.green,
            onChanged: (val) => setState(() => _treeCover = val),
          ),
          const SizedBox(height: 10),
          Text(TrilingualService.instance.getUIText('Forest Layers'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
          const SizedBox(height: 6),
          Wrap(
            spacing: 8,
            children: _layers.keys.map((name) {
              final isSelected = _selectedLayer == name;
              return ChoiceChip(
                label: Text(name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.green.shade700,
                backgroundColor: Colors.green.shade50,
                onSelected: (_) => setState(() => _selectedLayer = name),
              );
            }).toList(),
          ),
          const SizedBox(height: 8),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(10)),
            child: Text(_layers[_selectedLayer]!, style: TextStyle(fontSize: 13)),
          ),
        ],
      ),
    );
  }
}
