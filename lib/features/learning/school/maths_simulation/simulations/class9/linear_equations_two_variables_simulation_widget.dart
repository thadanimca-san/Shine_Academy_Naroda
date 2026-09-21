import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import '../common/graph_painter.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Graphs ax + by + c = 0 as sliders change a, b, c: the line traces
/// itself in from left to right each time the equation changes, showing
/// that every linear equation in two variables draws a straight line.
class LinearEquationsTwoVariablesSimulationWidget extends StatefulWidget {
  const LinearEquationsTwoVariablesSimulationWidget({super.key});

  @override
  State<LinearEquationsTwoVariablesSimulationWidget> createState() => _LinearEquationsTwoVariablesSimulationWidgetState();
}

class _LinearEquationsTwoVariablesSimulationWidgetState extends State<LinearEquationsTwoVariablesSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 1, _b = 1, _c = -4;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 800));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _replay() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    // ax + by + c = 0  =>  y = (-a x - c) / b  (guard b == 0)
    final safeB = _b == 0 ? 0.001 : _b;
    final allPoints = List.generate(40, (i) {
      final xi = -10 + i * (20.0 / 39);
      final yi = (-_a * xi - _c) / safeB;
      return Offset((xi + 10) / 20, ((yi + 10) / 20).clamp(0.0, 1.0));
    });

    return SimFrame(
      title: 'Graphing ax + by + c = 0',
      icon: Icons.timeline,
      accent: Colors.blue.shade700,
      description: 'Every linear equation in two variables graphs as a straight line. Adjust a, b, c and watch the line trace itself.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              final eased = Curves.easeInOut.transform(_controller.value);
              final count = (allPoints.length * eased).clamp(2, allPoints.length).round();
              final visiblePoints = allPoints.sublist(0, count);
              return MiniGraph(title: '${_a.toStringAsFixed(0)}x + ${_b.toStringAsFixed(0)}y + ${_c.toStringAsFixed(0)} = 0', points: visiblePoints, color: Colors.blue);
            },
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: TextButton.icon(
              onPressed: _replay,
              icon: Icon(Icons.replay, size: 18),
              label: Text(TrilingualService.instance.getUIText('Replay')),
              style: TextButton.styleFrom(foregroundColor: Colors.blue.shade700),
            ),
          ),
          const SizedBox(height: 6),
          SimSlider(label: 'a: ${_a.toStringAsFixed(0)}', value: _a, min: -5, max: 5, divisions: 10, activeColor: Colors.blue, onChanged: (v) => setState(() { _a = v; _replay(); })),
          SimSlider(label: 'b: ${_b.toStringAsFixed(0)}', value: _b, min: -5, max: 5, divisions: 10, activeColor: Colors.teal, onChanged: (v) => setState(() { _b = v; _replay(); })),
          SimSlider(label: 'c: ${_c.toStringAsFixed(0)}', value: _c, min: -10, max: 10, divisions: 20, activeColor: Colors.indigo, onChanged: (v) => setState(() { _c = v; _replay(); })),
        ],
      ),
    );
  }
}
