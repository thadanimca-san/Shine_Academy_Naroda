import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _SoilType {
  final String name;
  final double percolationSeconds;
  final String note;
  final Color color;

  const _SoilType(this.name, this.percolationSeconds, this.note, this.color);
}

/// A percolation-rate demo: pour water on sandy, loamy, or clayey soil
/// and watch how quickly it drains through, plus a labelled soil profile.
class SoilSimulationWidget extends StatefulWidget {
  const SoilSimulationWidget({super.key});

  @override
  State<SoilSimulationWidget> createState() => _SoilSimulationWidgetState();
}

class _SoilSimulationWidgetState extends State<SoilSimulationWidget> with SingleTickerProviderStateMixin {
  static const _soils = [
    _SoilType('Sandy Soil', 1.0, 'Large particles, big air gaps — water drains through very fast.', Color(0xFFD7A86E)),
    _SoilType('Loamy Soil', 2.2, 'A balanced mix of sand, silt and clay — drains at a moderate rate, ideal for most crops.', Color(0xFF8D6E4A)),
    _SoilType('Clayey Soil', 3.5, 'Very fine, tightly packed particles — water drains through slowly, so it retains moisture well.', Color(0xFF5C4432)),
  ];

  _SoilType _selected = _soils[0];
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: Duration(milliseconds: (_selected.percolationSeconds * 1000).round()));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _pour() {
    _controller.duration = Duration(milliseconds: (_selected.percolationSeconds * 1000).round());
    _controller.forward(from: 0);
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Soil Percolation Test',
      icon: Icons.terrain,
      accent: Colors.brown.shade600,
      description: 'Pick a soil type and pour water on it to see how fast it percolates through.',
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          final level = (1 - _controller.value).clamp(0.0, 1.0);
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                height: 150,
                width: double.infinity,
                decoration: BoxDecoration(color: Colors.blue.shade50, borderRadius: BorderRadius.circular(10)),
                child: Stack(
                  alignment: Alignment.bottomCenter,
                  children: [
                    Positioned(
                      bottom: 0,
                      left: 0,
                      right: 0,
                      height: 90,
                      child: Container(color: _selected.color),
                    ),
                    Positioned(
                      bottom: 90,
                      left: 30,
                      right: 30,
                      height: 40 * level,
                      child: Container(color: Colors.blue.withValues(alpha: 0.5)),
                    ),
                  ],
                ),
              ),
              const SizedBox(height: 12),
              SimMetricPanel(metrics: [
                SimMetric(label: 'Soil Type', value: _selected.name, color: _selected.color),
                SimMetric(label: 'Percolation Rate', value: _selected.percolationSeconds < 1.5 ? 'Fast' : (_selected.percolationSeconds < 3 ? 'Medium' : 'Slow'), color: Colors.blue),
              ]),
              const SizedBox(height: 10),
              Text(_selected.note, style: TextStyle(fontSize: 13)),
              const SizedBox(height: 12),
              Wrap(
                spacing: 8,
                children: _soils.map((s) {
                  final isSelected = _selected.name == s.name;
                  return ChoiceChip(
                    label: Text(s.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                    selected: isSelected,
                    selectedColor: s.color,
                    backgroundColor: s.color.withValues(alpha: 0.15),
                    onSelected: (_) => setState(() {
                      _selected = s;
                      _controller.value = 0;
                    }),
                  );
                }).toList(),
              ),
              const SizedBox(height: 12),
              SizedBox(
                width: double.infinity,
                child: ElevatedButton.icon(
                  onPressed: _pour,
                  icon: Icon(Icons.water_drop),
                  label: Text(TrilingualService.instance.getUIText('Pour Water')),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.blue.shade700, foregroundColor: Colors.white),
                ),
              ),
            ],
          );
        },
      ),
    );
  }
}
