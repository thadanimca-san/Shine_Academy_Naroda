import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import '../common/graph_painter.dart';

/// Graphs a quadratic and verifies the sum/product-of-zeroes identities
/// (α+β = −b/a, αβ = c/a) live as sliders reshape the parabola, with the
/// curve tracing itself left-to-right whenever it changes.
class Class10PolynomialsSimulationWidget extends StatefulWidget {
  const Class10PolynomialsSimulationWidget({super.key});

  @override
  State<Class10PolynomialsSimulationWidget> createState() => _Class10PolynomialsSimulationWidgetState();
}

class _Class10PolynomialsSimulationWidgetState extends State<Class10PolynomialsSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 1, _b = -1, _c = -6;
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

  double _p(double x) => _a * x * x + _b * x + _c;

  @override
  Widget build(BuildContext context) {
    final points = List.generate(50, (i) {
      final xi = -6 + i * (12.0 / 49);
      final yi = _p(xi);
      return Offset((xi + 6) / 12, ((yi + 20) / 40).clamp(0.0, 1.0));
    });
    final sumZeroes = -_b / _a;
    final productZeroes = _c / _a;

    return SimFrame(
      title: 'Sum & Product of Zeroes',
      icon: Icons.show_chart,
      accent: Colors.deepOrange.shade400,
      description: 'For ax²+bx+c, sum of zeroes = −b/a and product of zeroes = c/a — watch the parabola trace itself as you reshape it.',
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
                color: Colors.deepOrange,
                markerT: eased < 1 ? 1 : -1,
              );
            },
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Sum (−b/a)', value: sumZeroes.toStringAsFixed(2), color: Colors.blue),
            SimMetric(label: 'Product (c/a)', value: productZeroes.toStringAsFixed(2), color: Colors.teal),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'a: ${_a.toStringAsFixed(0)}', value: _a, min: -3, max: 3, divisions: 6, activeColor: Colors.blue, onChanged: (v) => setState(() { _a = v == 0 ? 1 : v; _replay(); })),
          SimSlider(label: 'b: ${_b.toStringAsFixed(0)}', value: _b, min: -5, max: 5, divisions: 10, activeColor: Colors.teal, onChanged: (v) => setState(() { _b = v; _replay(); })),
          SimSlider(label: 'c: ${_c.toStringAsFixed(0)}', value: _c, min: -8, max: 8, divisions: 16, activeColor: Colors.indigo, onChanged: (v) => setState(() { _c = v; _replay(); })),
        ],
      ),
    );
  }
}
