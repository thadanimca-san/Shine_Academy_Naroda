import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Step {
  final String name;
  final IconData icon;
  final String description;
  const _Step(this.name, this.icon, this.description);
}

/// Steps through a sewage treatment plant, showing how dirty wastewater
/// is progressively cleaned before being released back to a water body.
class WastewaterSimulationWidget extends StatefulWidget {
  const WastewaterSimulationWidget({super.key});

  @override
  State<WastewaterSimulationWidget> createState() => _WastewaterSimulationWidgetState();
}

class _WastewaterSimulationWidgetState extends State<WastewaterSimulationWidget> {
  static const _steps = [
    _Step('Screening', Icons.filter_alt, 'Wastewater passes through a bar screen that removes large floating objects like rags and sticks.'),
    _Step('Grit & Sand Removal', Icons.grain, 'The water flows slowly so sand and grit settle at the bottom of the tank.'),
    _Step('Sedimentation', Icons.layers, 'Suspended solid impurities settle down as sludge; the water above is called clarified water.'),
    _Step('Aeration', Icons.bubble_chart, 'Air is pumped in so aerobic bacteria can break down remaining organic waste.'),
    _Step('Clean Water Released', Icons.water, 'Treated, clarified water is safe to release into a river or reused, while dried sludge becomes manure.'),
  ];

  int _index = 0;

  @override
  Widget build(BuildContext context) {
    final step = _steps[_index];
    final cleanliness = (_index + 1) / _steps.length;

    return SimFrame(
      title: 'Wastewater Treatment Plant',
      icon: Icons.water_damage,
      accent: Colors.blueGrey.shade700,
      description: 'Step through each stage and watch the water get progressively cleaner.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 90,
            width: double.infinity,
            decoration: BoxDecoration(
              color: Color.lerp(const Color(0xFF6D4C41), const Color(0xFF4FC3F7), cleanliness),
              borderRadius: BorderRadius.circular(10),
            ),
            alignment: Alignment.center,
            child: Icon(step.icon, size: 40, color: Colors.white),
          ),
          const SizedBox(height: 10),
          Text('${_index + 1}. ${step.name}', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15)),
          const SizedBox(height: 6),
          Text(step.description, style: TextStyle(fontSize: 13)),
          const SizedBox(height: 12),
          LinearProgressIndicator(value: cleanliness, minHeight: 8, color: Colors.blue, backgroundColor: Colors.brown.shade100),
          const SizedBox(height: 4),
          Text(TrilingualService.instance.getUIText('Water cleanliness'), style: TextStyle(fontSize: 11, color: Theme.of(context).colorScheme.onSurface.withOpacity(0.45))),
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
                  onPressed: _index == _steps.length - 1 ? null : () => setState(() => _index++),
                  icon: Icon(Icons.arrow_forward),
                  label: Text(TrilingualService.instance.getUIText('Next')),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.blueGrey.shade700, foregroundColor: Colors.white),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
