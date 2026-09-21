import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Stage {
  final String name;
  final IconData icon;
  final String description;
  const _Stage(this.name, this.icon, this.description);
}

/// A tap-through farming cycle: each stage from preparing the soil to
/// storage, in the correct sequence, with a short explanation of what
/// happens and why it matters.
class CropProductionSimulationWidget extends StatefulWidget {
  const CropProductionSimulationWidget({super.key});

  @override
  State<CropProductionSimulationWidget> createState() => _CropProductionSimulationWidgetState();
}

class _CropProductionSimulationWidgetState extends State<CropProductionSimulationWidget> {
  static const _stages = [
    _Stage('Preparation of Soil', Icons.grass, 'Tilling loosens and turns the soil, bringing nutrients up and allowing roots to penetrate easily.'),
    _Stage('Sowing', Icons.grain, 'Good quality seeds are sown at the correct depth and spacing, by broadcasting, using a seed drill, or transplanting.'),
    _Stage('Adding Manure & Fertilisers', Icons.eco, 'Manure and fertilisers replenish nutrients in the soil that crops use up as they grow.'),
    _Stage('Irrigation', Icons.water_drop, 'Water is supplied to crops at the right intervals — by canals, wells, tube-wells, or sprinkler/drip systems.'),
    _Stage('Weeding', Icons.content_cut, 'Unwanted plants (weeds) are removed so they don\'t compete with the crop for nutrients, water and sunlight.'),
    _Stage('Protection from Pests', Icons.bug_report, 'Crops are protected from insects and diseases using pesticides or natural methods.'),
    _Stage('Harvesting', Icons.agriculture, 'The mature crop is cut and gathered, then threshed to separate grain from the plant.'),
    _Stage('Storage', Icons.warehouse, 'Grains must be dried and stored properly to protect them from moisture, insects, and rodents.'),
  ];

  int _index = 0;

  @override
  Widget build(BuildContext context) {
    final stage = _stages[_index];

    return SimFrame(
      title: 'The Farming Cycle',
      icon: Icons.agriculture,
      accent: Colors.green.shade700,
      description: 'Step through the sequence every crop goes through, from soil preparation to storage.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(12)),
            child: Column(
              children: [
                Icon(stage.icon, size: 48, color: Colors.green.shade700),
                const SizedBox(height: 10),
                Text(stage.name, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Colors.green.shade900)),
                const SizedBox(height: 8),
                Text(stage.description, textAlign: TextAlign.center, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
          const SizedBox(height: 10),
          Text('Step ${_index + 1} of ${_stages.length}', style: TextStyle(fontSize: 12, color: Theme.of(context).colorScheme.onSurfaceVariant)),
          const SizedBox(height: 10),
          LinearProgressIndicator(value: (_index + 1) / _stages.length, minHeight: 6, color: Colors.green.shade700, backgroundColor: Colors.green.shade100),
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
                  onPressed: _index == _stages.length - 1 ? null : () => setState(() => _index++),
                  icon: Icon(Icons.arrow_forward),
                  label: Text(TrilingualService.instance.getUIText('Next')),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.green.shade700, foregroundColor: Colors.white),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
