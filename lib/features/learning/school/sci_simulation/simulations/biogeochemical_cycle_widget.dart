import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _CycleStage {
  final String name;
  final String description;
  const _CycleStage(this.name, this.description);
}

class _Cycle {
  final String name;
  final Color color;
  final List<_CycleStage> stages;
  const _Cycle(this.name, this.color, this.stages);
}

const _cycles = [
  _Cycle('Water', Color(0xFF3F6A9C), [
    _CycleStage('Evaporation', 'The Sun heats water in oceans, rivers, and lakes, turning it into water vapour.'),
    _CycleStage('Condensation', 'Water vapour rises, cools, and condenses into tiny droplets, forming clouds.'),
    _CycleStage('Precipitation', 'Water falls back to Earth as rain, hail, or snow.'),
    _CycleStage('Infiltration & Runoff', 'Some water seeps into the ground (groundwater); the rest flows over land back to rivers and oceans.'),
  ]),
  _Cycle('Carbon', Color(0xFF6B9E5C), [
    _CycleStage('Photosynthesis', 'Plants absorb atmospheric CO₂ and convert it into glucose using sunlight.'),
    _CycleStage('Respiration', 'Plants and animals break down food for energy, releasing CO₂ back into the air.'),
    _CycleStage('Decomposition', 'When organisms die, decomposers break them down, releasing carbon back to air or soil.'),
    _CycleStage('Fossil Fuel Formation & Combustion', 'Over millions of years, buried dead matter forms coal, oil, and gas; burning these releases stored carbon as CO₂ rapidly.'),
  ]),
  _Cycle('Nitrogen', Color(0xFFB08D3D), [
    _CycleStage('Nitrogen Fixation', 'Bacteria like Rhizobium convert atmospheric N₂ gas into ammonia (NH₃), which plants can use.'),
    _CycleStage('Nitrification', 'Bacteria convert ammonia into nitrite, then into nitrate — forms plants can absorb.'),
    _CycleStage('Assimilation', 'Plants absorb nitrates from soil; animals get nitrogen by eating plants or other animals.'),
    _CycleStage('Ammonification', 'Decomposers break down dead organisms and waste, returning nitrogen to soil as ammonia.'),
    _CycleStage('Denitrification', 'Bacteria convert nitrates back into nitrogen gas, releasing it into the atmosphere — completing the cycle.'),
  ]),
  _Cycle('Oxygen', Color(0xFFC2455B), [
    _CycleStage('Photosynthesis (Production)', 'Plants release oxygen as a byproduct of making their own food using sunlight, water, and CO₂.'),
    _CycleStage('Respiration (Consumption)', 'Animals and plants use oxygen to break down food for energy, releasing CO₂.'),
    _CycleStage('Combustion (Consumption)', 'Burning fuels (wood, coal, petrol) consumes oxygen and releases CO₂.'),
  ]),
];

/// Step through the four biogeochemical cycles (water, carbon, nitrogen,
/// oxygen), tapping each stage in sequence to see what happens there —
/// mirrors the cycle diagrams (Fig. 13.12-13.16) in the chapter.
class BiogeochemicalCycleWidget extends StatefulWidget {
  const BiogeochemicalCycleWidget({super.key});

  @override
  State<BiogeochemicalCycleWidget> createState() => _BiogeochemicalCycleWidgetState();
}

class _BiogeochemicalCycleWidgetState extends State<BiogeochemicalCycleWidget> {
  _Cycle _cycle = _cycles[0];
  int _stageIndex = 0;

  @override
  Widget build(BuildContext context) {
    final stage = _cycle.stages[_stageIndex];
    return SimFrame(
      title: 'Biogeochemical Cycle Explorer',
      icon: Icons.loop,
      accent: _cycle.color,
      description: 'Pick a cycle, then step through each stage in order.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _cycles.map((c) {
              final isSelected = _cycle.name == c.name;
              return ChoiceChip(
                label: Text('${c.name} Cycle', style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: c.color,
                backgroundColor: c.color.withValues(alpha: 0.15),
                onSelected: (_) => setState(() {
                  _cycle = c;
                  _stageIndex = 0;
                }),
              );
            }).toList(),
          ),
          const SizedBox(height: 16),
          // Stage progress dots + connecting track.
          SizedBox(
            height: 46,
            child: LayoutBuilder(
              builder: (context, constraints) {
                final n = _cycle.stages.length;
                final spacing = n > 1 ? constraints.maxWidth / (n - 1) : 0.0;
                return Stack(
                  alignment: Alignment.center,
                  children: [
                    Positioned(
                      left: 10,
                      right: 10,
                      top: 20,
                      child: Container(height: 3, color: _cycle.color.withValues(alpha: 0.25)),
                    ),
                    for (int i = 0; i < n; i++)
                      Positioned(
                        left: n > 1 ? (i * spacing - 10).clamp(0.0, constraints.maxWidth - 20) : constraints.maxWidth / 2 - 10,
                        top: 8,
                        child: GestureDetector(
                          onTap: () => setState(() => _stageIndex = i),
                          child: Container(
                            width: 22,
                            height: 22,
                            alignment: Alignment.center,
                            decoration: BoxDecoration(
                              shape: BoxShape.circle,
                              color: i <= _stageIndex ? _cycle.color : Colors.white,
                              border: Border.all(color: _cycle.color, width: 2),
                            ),
                            child: Text('${i + 1}', style: TextStyle(fontSize: 10, fontWeight: FontWeight.bold, color: i <= _stageIndex ? Colors.white : _cycle.color)),
                          ),
                        ),
                      ),
                  ],
                );
              },
            ),
          ),
          const SizedBox(height: 8),
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              OutlinedButton.icon(
                onPressed: _stageIndex > 0 ? () => setState(() => _stageIndex--) : null,
                icon: Icon(Icons.chevron_left, size: 18),
                label: Text(TrilingualService.instance.getUIText('Back')),
              ),
              Text('Step ${_stageIndex + 1} of ${_cycle.stages.length}', style: TextStyle(fontSize: 12, color: Theme.of(context).colorScheme.onSurfaceVariant)),
              ElevatedButton.icon(
                onPressed: _stageIndex < _cycle.stages.length - 1 ? () => setState(() => _stageIndex++) : null,
                icon: Icon(Icons.chevron_right, size: 18),
                label: Text(TrilingualService.instance.getUIText('Next')),
                style: ElevatedButton.styleFrom(backgroundColor: _cycle.color, foregroundColor: Colors.white),
              ),
            ],
          ),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(stage.name, style: TextStyle(fontWeight: FontWeight.bold, color: _cycle.color, fontSize: 14)),
                const SizedBox(height: 4),
                Text(stage.description, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
