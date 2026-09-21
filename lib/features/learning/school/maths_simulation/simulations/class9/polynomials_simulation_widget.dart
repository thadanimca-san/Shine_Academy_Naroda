import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import '../common/graph_painter.dart';

/// Graphs p(x) = ax² + bx + c live as sliders change: the curve traces
/// itself left-to-right whenever a, b or c changes, with a marker at
/// the evaluated point, tying "zero of a polynomial" to where the curve
/// crosses the x-axis.
class PolynomialsSimulationWidget extends StatefulWidget {
  const PolynomialsSimulationWidget({super.key});

  @override
  State<PolynomialsSimulationWidget> createState() => _PolynomialsSimulationWidgetState();
}

class _PolynomialsSimulationWidgetState extends State<PolynomialsSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 1, _b = -2, _c = -3;
  double _x = 0;
  late AnimationController _controller;

  double _p(double x) => _a * x * x + _b * x + _c;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 700));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _redraw() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final allPoints = List.generate(50, (i) {
      final xi = -6 + i * (12.0 / 49);
      final yi = _p(xi);
      return Offset((xi + 6) / 12, ((yi + 20) / 40).clamp(0.0, 1.0));
    });
    final px = _p(_x);

    return SimFrame(
      title: 'p(x) = ax² + bx + c',
      icon: Icons.show_chart,
      accent: Colors.deepOrange.shade400,
      description: 'Adjust a, b, c to reshape the polynomial — the curve redraws itself — and slide x to evaluate p(x): zeroes are where the curve crosses zero.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              final eased = Curves.easeInOut.transform(_controller.value);
              final count = (allPoints.length * eased).clamp(2, allPoints.length).round();
              final visiblePoints = allPoints.sublist(0, count);
              final markerT = eased >= 0.999 ? (_x + 6) / 12 : -1.0;
              return MiniGraph(title: 'y = p(x)', points: visiblePoints, color: Colors.deepOrange, markerT: markerT);
            },
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'x', value: _x.toStringAsFixed(1)),
            SimMetric(label: 'p(x)', value: px.toStringAsFixed(1), color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'x: ${_x.toStringAsFixed(1)}', value: _x, min: -6, max: 6, divisions: 48, activeColor: Colors.deepOrange, onChanged: (v) => setState(() => _x = v)),
          SimSlider(label: 'a: ${_a.toStringAsFixed(0)}', value: _a, min: -3, max: 3, divisions: 6, activeColor: Colors.blue, onChanged: (v) => setState(() { _a = v; _redraw(); })),
          SimSlider(label: 'b: ${_b.toStringAsFixed(0)}', value: _b, min: -5, max: 5, divisions: 10, activeColor: Colors.teal, onChanged: (v) => setState(() { _b = v; _redraw(); })),
          SimSlider(label: 'c: ${_c.toStringAsFixed(0)}', value: _c, min: -5, max: 5, divisions: 10, activeColor: Colors.indigo, onChanged: (v) => setState(() { _c = v; _redraw(); })),
        ],
      ),
    );
  }
}
