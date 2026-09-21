import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// An expression evaluator: slide x and watch 2x² + 3x − 1 recompute
/// term by term, with each term's contribution bar animating to its new
/// height so the total visibly builds up out of its parts.
class AlgebraicExpressionsSimulationWidget extends StatefulWidget {
  const AlgebraicExpressionsSimulationWidget({super.key});

  @override
  State<AlgebraicExpressionsSimulationWidget> createState() => _AlgebraicExpressionsSimulationWidgetState();
}

class _AlgebraicExpressionsSimulationWidgetState extends State<AlgebraicExpressionsSimulationWidget> with SingleTickerProviderStateMixin {
  double _x = 2;
  double _prevTerm1 = 8, _prevTerm2 = 6, _prevTotal = 13;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 500));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final term1 = 2 * _x * _x;
    final term2 = 3 * _x;
    const term3 = -1;
    final total = term1 + term2 + term3;

    return SimFrame(
      title: 'Evaluating an Algebraic Expression',
      icon: Icons.functions,
      accent: Colors.deepOrange.shade400,
      description: 'Slide x and watch each term of 2x² + 3x − 1 animate to its new value, building the total live.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(color: Colors.deepOrange.shade50, borderRadius: BorderRadius.circular(10)),
            child: Column(
              children: [
                Text('2x² + 3x − 1  where x = ${_x.toStringAsFixed(0)}', style: TextStyle(fontSize: 15, fontWeight: FontWeight.w600)),
                const SizedBox(height: 10),
                AnimatedBuilder(
                  animation: _controller,
                  builder: (context, _) {
                    final eased = Curves.easeInOut.transform(_controller.value);
                    final t1 = _prevTerm1 + (term1 - _prevTerm1) * eased;
                    final t2 = _prevTerm2 + (term2 - _prevTerm2) * eased;
                    final tot = _prevTotal + (total - _prevTotal) * eased;
                    return Text(
                      '2(${_x.toStringAsFixed(0)})² + 3(${_x.toStringAsFixed(0)}) − 1  =  ${t1.round()} + ${t2.round()} + $term3  =  ${tot.round()}',
                      style: TextStyle(fontSize: 14, color: Colors.deepOrange.shade800, fontWeight: FontWeight.bold),
                      textAlign: TextAlign.center,
                    );
                  },
                ),
                const SizedBox(height: 12),
                AnimatedBuilder(
                  animation: _controller,
                  builder: (context, _) {
                    final eased = Curves.easeInOut.transform(_controller.value);
                    final t1 = _prevTerm1 + (term1 - _prevTerm1) * eased;
                    final t2 = _prevTerm2 + (term2 - _prevTerm2) * eased;
                    final maxAbs = [t1.abs(), t2.abs(), 1.0].reduce((a, b) => a > b ? a : b);
                    double barH(double v) => (v.abs() / maxAbs) * 60 + 4;
                    return SizedBox(
                      height: 70,
                      child: Row(
                        mainAxisAlignment: MainAxisAlignment.center,
                        crossAxisAlignment: CrossAxisAlignment.end,
                        children: [
                          _bar('2x²', barH(t1), Colors.blue),
                          const SizedBox(width: 14),
                          _bar('3x', barH(t2), Colors.teal),
                        ],
                      ),
                    );
                  },
                ),
              ],
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: '2x²', value: '$term1', color: Colors.blue),
            SimMetric(label: '3x', value: '$term2', color: Colors.teal),
            SimMetric(label: 'Total', value: '$total', color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'x: ${_x.toStringAsFixed(0)}',
            value: _x,
            min: -5,
            max: 5,
            divisions: 10,
            activeColor: Colors.deepOrange,
            onChanged: (val) => setState(() {
              _prevTerm1 = term1;
              _prevTerm2 = term2;
              _prevTotal = total;
              _x = val;
              _controller.forward(from: 0);
            }),
          ),
        ],
      ),
    );
  }

  Widget _bar(String label, double height, Color color) {
    return Column(
      mainAxisSize: MainAxisSize.min,
      children: [
        Container(width: 26, height: height, decoration: BoxDecoration(color: color.withValues(alpha: 0.75), borderRadius: const BorderRadius.vertical(top: Radius.circular(4)))),
        const SizedBox(height: 4),
        Text(label, style: TextStyle(fontSize: 10)),
      ],
    );
  }
}
