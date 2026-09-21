import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Animated lungs that expand and contract with breathing, plus a
/// tap-to-explore chart of how different organisms breathe.
class RespirationSimulationWidget extends StatefulWidget {
  const RespirationSimulationWidget({super.key});

  @override
  State<RespirationSimulationWidget> createState() => _RespirationSimulationWidgetState();
}

class _RespirationSimulationWidgetState extends State<RespirationSimulationWidget> with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  int _selected = 0;

  static const _organisms = [
    ('Humans', Icons.person, 'Breathe using lungs; air passes through the windpipe into tiny air sacs called alveoli.'),
    ('Fish', Icons.set_meal, 'Breathe using gills, which absorb dissolved oxygen directly from water.'),
    ('Earthworm', Icons.pest_control, 'Breathes through its moist skin, which absorbs oxygen from the soil.'),
    ('Insects', Icons.bug_report, 'Breathe through tiny openings on their body called spiracles.'),
    ('Plants', Icons.eco, 'Exchange gases through pores called stomata on their leaves.'),
  ];

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 3))..repeat(reverse: true);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Breathing & Respiration',
      icon: Icons.air,
      accent: Colors.teal.shade600,
      description: 'Watch the lungs inhale and exhale, and tap through how different organisms breathe.',
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          final scale = 0.85 + _controller.value * 0.3;
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                height: 140,
                width: double.infinity,
                decoration: BoxDecoration(color: Colors.teal.shade50, borderRadius: BorderRadius.circular(10)),
                child: Center(
                  child: Row(
                    mainAxisAlignment: MainAxisAlignment.center,
                    children: [
                      Transform.scale(scale: scale, child: Icon(Icons.circle, size: 50, color: Colors.pink.shade300)),
                      const SizedBox(width: 6),
                      Icon(Icons.remove, color: Colors.grey.shade400),
                      const SizedBox(width: 6),
                      Transform.scale(scale: scale, child: Icon(Icons.circle, size: 50, color: Colors.pink.shade300)),
                    ],
                  ),
                ),
              ),
              const SizedBox(height: 4),
              Center(child: Text(_controller.status == AnimationStatus.forward || scale > 1.0 ? 'Inhaling' : 'Exhaling', style: TextStyle(color: Colors.teal.shade700, fontWeight: FontWeight.w600))),
              const SizedBox(height: 12),
              Text(TrilingualService.instance.getUIText('How Different Organisms Breathe'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
              const SizedBox(height: 6),
              Wrap(
                spacing: 8,
                runSpacing: 8,
                children: _organisms.asMap().entries.map((e) {
                  final isSelected = e.key == _selected;
                  return ChoiceChip(
                    avatar: Icon(e.value.$2, size: 16, color: isSelected ? Colors.white : Colors.teal.shade700),
                    label: Text(e.value.$1, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                    selected: isSelected,
                    selectedColor: Colors.teal.shade600,
                    backgroundColor: Colors.teal.shade50,
                    onSelected: (_) => setState(() => _selected = e.key),
                  );
                }).toList(),
              ),
              const SizedBox(height: 10),
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(color: Colors.teal.shade50, borderRadius: BorderRadius.circular(10)),
                child: Text(_organisms[_selected].$3, style: TextStyle(fontSize: 13)),
              ),
            ],
          );
        },
      ),
    );
  }
}
