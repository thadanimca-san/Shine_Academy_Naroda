import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import '../common/graph_painter.dart';

/// Graphs ax²+bx+c and shows the discriminant b²−4ac live, connecting
/// its sign directly to how many times the parabola crosses the x-axis —
/// the curve traces itself left-to-right whenever it's reshaped.
class QuadraticEquationsSimulationWidget extends StatefulWidget {
  const QuadraticEquationsSimulationWidget({super.key});

  @override
  State<QuadraticEquationsSimulationWidget> createState() => _QuadraticEquationsSimulationWidgetState();
}

class _QuadraticEquationsSimulationWidgetState extends State<QuadraticEquationsSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 1, _b = -2, _c = 1;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 900));
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
    final discriminant = _b * _b - 4 * _a * _c;
    final points = List.generate(50, (i) {
      final xi = -6 + i * (12.0 / 49);
      final yi = _a * xi * xi + _b * xi + _c;
      return Offset((xi + 6) / 12, ((yi + 20) / 40).clamp(0.0, 1.0));
    });

    String nature;
    Color color;
    if (discriminant > 0) {
      nature = 'Two distinct real roots';
      color = Colors.green;
    } else if (discriminant == 0) {
      nature = 'Two equal real roots';
      color = Colors.orange;
    } else {
      nature = 'No real roots';
      color = Colors.red;
    }

    return SimFrame(
      title: 'The Discriminant',
      icon: Icons.show_chart,
      accent: Colors.purple.shade600,
      description: 'The sign of b²−4ac tells you how many times the parabola crosses the x-axis — watch it trace itself as you reshape it.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              final eased = Curves.easeInOut.transform(_controller.value);
              final visibleCount = (points.length * eased).clamp(2, points.length).round();
              return MiniGraph(
                title: 'y = ${_a.toStringAsFixed(0)}x² + ${_b.toStringAsFixed(0)}x + ${_c.toStringAsFixed(0)}',
                points: points.sublist(0, visibleCount),
                color: color,
                markerT: eased < 1 ? 1 : -1,
              );
            },
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Discriminant', value: discriminant.toStringAsFixed(0), color: color),
            SimMetric(label: 'Nature of Roots', value: nature, color: color),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'a: ${_a.toStringAsFixed(0)}', value: _a, min: -3, max: 3, divisions: 6, activeColor: Colors.blue, onChanged: (v) => setState(() { _a = v == 0 ? 1 : v; _replay(); })),
          SimSlider(label: 'b: ${_b.toStringAsFixed(0)}', value: _b, min: -6, max: 6, divisions: 12, activeColor: Colors.teal, onChanged: (v) => setState(() { _b = v; _replay(); })),
          SimSlider(label: 'c: ${_c.toStringAsFixed(0)}', value: _c, min: -6, max: 6, divisions: 12, activeColor: Colors.indigo, onChanged: (v) => setState(() { _c = v; _replay(); })),
        ],
      ),
    );
  }
}
