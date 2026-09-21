import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Part {
  final String name;
  final String function;
  final Color color;
  final Alignment position;

  const _Part(this.name, this.function, this.color, this.position);
}

/// A labelled flower diagram: tap a part to see its role in
/// reproduction, from pollen-producing stamens to the seed-bearing pistil.
class ReproductionPlantsSimulationWidget extends StatefulWidget {
  const ReproductionPlantsSimulationWidget({super.key});

  @override
  State<ReproductionPlantsSimulationWidget> createState() => _ReproductionPlantsSimulationWidgetState();
}

class _ReproductionPlantsSimulationWidgetState extends State<ReproductionPlantsSimulationWidget> {
  static const _parts = [
    _Part('Petals', 'Brightly coloured to attract insects for pollination.', Color(0xFFEC407A), Alignment(0, 0)),
    _Part('Stamen', 'The male part; its anther produces pollen grains.', Color(0xFFFFB74D), Alignment(-0.5, -0.5)),
    _Part('Pistil', 'The female part; its ovary contains ovules that become seeds after fertilisation.', Color(0xFF66BB6A), Alignment(0.5, -0.5)),
    _Part('Sepals', 'Green leaf-like parts that protect the flower bud before it blooms.', Color(0xFF81C784), Alignment(0, 0.6)),
  ];

  _Part _selected = _parts[0];

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Parts of a Flower',
      icon: Icons.local_florist,
      accent: Colors.pink.shade400,
      description: 'Tap a part of the flower to learn its role in reproduction.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AspectRatio(
            aspectRatio: 1.6,
            child: Container(
              decoration: BoxDecoration(color: Colors.pink.shade50, borderRadius: BorderRadius.circular(12)),
              child: Stack(
                alignment: Alignment.center,
                children: _parts.map((p) {
                  final isSelected = _selected.name == p.name;
                  return Align(
                    alignment: p.position,
                    child: GestureDetector(
                      onTap: () => setState(() => _selected = p),
                      child: Container(
                        width: p.name == 'Petals' ? 70 : 50,
                        height: p.name == 'Petals' ? 70 : 50,
                        decoration: BoxDecoration(
                          color: p.color.withValues(alpha: 0.85),
                          shape: BoxShape.circle,
                          border: Border.all(color: isSelected ? Colors.black87 : Colors.white, width: isSelected ? 2.5 : 1.5),
                        ),
                        alignment: Alignment.center,
                        child: Text(p.name[0], style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                      ),
                    ),
                  );
                }).toList(),
              ),
            ),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _parts.map((p) {
              final isSelected = _selected.name == p.name;
              return ActionChip(
                label: Text(p.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                backgroundColor: isSelected ? p.color : p.color.withValues(alpha: 0.2),
                onPressed: () => setState(() => _selected = p),
              );
            }).toList(),
          ),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(_selected.name, style: TextStyle(fontWeight: FontWeight.bold, color: _selected.color, fontSize: 14)),
                const SizedBox(height: 4),
                Text(_selected.function, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
