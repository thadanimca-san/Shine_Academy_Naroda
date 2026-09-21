import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Solid {
  final String name;
  final int faces, edges, vertices;
  final IconData icon;

  const _Solid(this.name, this.faces, this.edges, this.vertices, this.icon);
}

/// Tap-to-explore polyhedra checking Euler's formula (F + V − E = 2) for
/// each: the icon spins and scales in on selection, reinforcing the
/// relationship with different shapes than earlier grades.
class Class8SolidShapesSimulationWidget extends StatefulWidget {
  const Class8SolidShapesSimulationWidget({super.key});

  @override
  State<Class8SolidShapesSimulationWidget> createState() => _SolidShapesSimulationWidgetState();
}

class _SolidShapesSimulationWidgetState extends State<Class8SolidShapesSimulationWidget> with SingleTickerProviderStateMixin {
  static const _solids = [
    _Solid('Octahedron', 8, 12, 6, Icons.diamond_outlined),
    _Solid('Pentagonal Prism', 7, 15, 10, Icons.pentagon_outlined),
    _Solid('Hexagonal Pyramid', 7, 12, 7, Icons.hexagon_outlined),
    _Solid('Cube', 6, 12, 8, Icons.crop_din),
    _Solid('Triangular Pyramid', 4, 6, 4, Icons.change_history),
  ];

  _Solid _selected = _solids[0];
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 600));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _select(_Solid s) {
    setState(() {
      _selected = s;
      _controller.forward(from: 0);
    });
  }

  @override
  Widget build(BuildContext context) {
    final euler = _selected.faces + _selected.vertices - _selected.edges;

    return SimFrame(
      title: "Euler's Formula Explorer",
      icon: Icons.view_in_ar,
      accent: Colors.brown.shade600,
      description: "Tap a solid and verify Euler's formula: Faces + Vertices − Edges = 2.",
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 120,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.brown.shade50, borderRadius: BorderRadius.circular(10)),
            child: Center(
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) {
                  final eased = Curves.easeOutBack.transform(_controller.value);
                  return Transform.scale(
                    scale: eased.clamp(0.0, 1.2),
                    child: Transform.rotate(
                      angle: (1 - _controller.value.clamp(0.0, 1.0)) * 0.8,
                      child: Icon(_selected.icon, size: 64, color: Colors.brown.shade700),
                    ),
                  );
                },
              ),
            ),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _solids.map((s) {
              final isSelected = _selected.name == s.name;
              return ChoiceChip(
                label: Text(s.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.brown.shade600,
                backgroundColor: Colors.brown.shade50,
                onSelected: (_) => _select(s),
              );
            }).toList(),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Faces', value: '${_selected.faces}', color: Colors.blue),
            SimMetric(label: 'Edges', value: '${_selected.edges}', color: Colors.deepOrange),
            SimMetric(label: 'Vertices', value: '${_selected.vertices}', color: Colors.green),
          ]),
          const SizedBox(height: 10),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: euler == 2 ? Colors.green.shade50 : Colors.red.shade50, borderRadius: BorderRadius.circular(10)),
            child: Text('${_selected.faces} + ${_selected.vertices} − ${_selected.edges} = $euler ${euler == 2 ? "✓" : ""}', style: TextStyle(fontWeight: FontWeight.bold, color: euler == 2 ? Colors.green.shade800 : Colors.red.shade800)),
          ),
        ],
      ),
    );
  }
}
