import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Solid {
  final String name;
  final int faces, edges, vertices;
  final IconData icon;

  const _Solid(this.name, this.faces, this.edges, this.vertices, this.icon);
}

/// A tap-to-explore gallery of solids showing face, edge and vertex
/// counts, and checking Euler's formula (F + V − E = 2) live. Selecting
/// a new solid animates it in with a scale-and-rotate entrance, giving
/// each shape a distinct physical "arrival" instead of just swapping.
class SolidShapesSimulationWidget extends StatefulWidget {
  const SolidShapesSimulationWidget({super.key});

  @override
  State<SolidShapesSimulationWidget> createState() => _SolidShapesSimulationWidgetState();
}

class _SolidShapesSimulationWidgetState extends State<SolidShapesSimulationWidget> with SingleTickerProviderStateMixin {
  static const _solids = [
    _Solid('Cube', 6, 12, 8, Icons.crop_din),
    _Solid('Cuboid', 6, 12, 8, Icons.crop_7_5),
    _Solid('Tetrahedron', 4, 6, 4, Icons.change_history),
    _Solid('Square Pyramid', 5, 8, 5, Icons.signal_cellular_4_bar),
    _Solid('Triangular Prism', 5, 9, 6, Icons.view_in_ar),
  ];

  _Solid _selected = _solids[0];
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 550));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final eulerCheck = _selected.faces + _selected.vertices - _selected.edges;

    return SimFrame(
      title: 'Faces, Edges & Vertices',
      icon: Icons.view_in_ar,
      accent: Colors.brown.shade600,
      description: "Tap a solid to see its face/edge/vertex counts, and check Euler's formula: F + V − E = 2.",
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 130,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.brown.shade50, borderRadius: BorderRadius.circular(10)),
            child: Center(
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) {
                  final eased = Curves.easeOutBack.transform(_controller.value);
                  return Transform.scale(
                    scale: eased.clamp(0.0, 1.4),
                    child: Transform.rotate(
                      angle: (1 - eased) * 0.6,
                      child: Icon(_selected.icon, size: 70, color: Colors.brown.shade700),
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
                onSelected: (_) => setState(() {
                  _selected = s;
                  _controller.forward(from: 0);
                }),
              );
            }).toList(),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Faces (F)', value: '${_selected.faces}', color: Colors.blue),
            SimMetric(label: 'Edges (E)', value: '${_selected.edges}', color: Colors.deepOrange),
            SimMetric(label: 'Vertices (V)', value: '${_selected.vertices}', color: Colors.green),
          ]),
          const SizedBox(height: 10),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: eulerCheck == 2 ? Colors.green.shade50 : Colors.red.shade50, borderRadius: BorderRadius.circular(10)),
            child: Text(
              'F + V − E = ${_selected.faces} + ${_selected.vertices} − ${_selected.edges} = $eulerCheck ${eulerCheck == 2 ? "✓" : ""}',
              style: TextStyle(fontWeight: FontWeight.bold, color: eulerCheck == 2 ? Colors.green.shade800 : Colors.red.shade800),
            ),
          ),
        ],
      ),
    );
  }
}
