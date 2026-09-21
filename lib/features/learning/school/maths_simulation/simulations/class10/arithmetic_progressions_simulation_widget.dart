import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A growing bar chart of AP terms: adjust the first term and common
/// difference and watch each bar step up (or down) by exactly d,
/// alongside the live nth-term and sum formulas.
class ArithmeticProgressionsSimulationWidget extends StatefulWidget {
  const ArithmeticProgressionsSimulationWidget({super.key});

  @override
  State<ArithmeticProgressionsSimulationWidget> createState() => _ArithmeticProgressionsSimulationWidgetState();
}

class _ArithmeticProgressionsSimulationWidgetState extends State<ArithmeticProgressionsSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 2;
  double _d = 3;
  int _n = 8;
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
    final terms = List.generate(_n, (i) => _a + i * _d);
    final maxAbs = terms.map((t) => t.abs()).reduce((x, y) => x > y ? x : y).clamp(1, double.infinity);
    final nthTerm = _a + (_n - 1) * _d;
    final sum = _n / 2 * (2 * _a + (_n - 1) * _d);

    return SimFrame(
      title: 'Arithmetic Progression Builder',
      icon: Icons.stacked_bar_chart,
      accent: Colors.blue.shade700,
      description: 'Each bar is the previous term plus the common difference d — watch the sequence build up term by term.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              return SizedBox(
                height: 130,
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.end,
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  children: List.generate(terms.length, (i) {
                    // Stagger each bar's growth so they rise left-to-right in sequence.
                    final start = i / terms.length;
                    final end = start + (1 / terms.length);
                    final localT = ((_controller.value - start) / (end - start)).clamp(0.0, 1.0);
                    final eased = Curves.easeOutBack.transform(localT);
                    final t = terms[i];
                    final height = ((t.abs() / maxAbs) * 100).clamp(4, 100) * eased;
                    return Container(
                      width: 22,
                      height: height,
                      margin: const EdgeInsets.symmetric(horizontal: 1),
                      decoration: BoxDecoration(color: t >= 0 ? Colors.blue.shade400 : Colors.red.shade300, borderRadius: const BorderRadius.vertical(top: Radius.circular(3))),
                    );
                  }),
                ),
              );
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
          SimMetricPanel(metrics: [
            SimMetric(label: 'nth term (aₙ)', value: nthTerm.toStringAsFixed(0), color: Colors.deepOrange),
            SimMetric(label: 'Sum (Sₙ)', value: sum.toStringAsFixed(0), color: Colors.teal),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'First term a: ${_a.toStringAsFixed(0)}', value: _a, min: -10, max: 10, divisions: 20, activeColor: Colors.blue, onChanged: (v) => setState(() { _a = v; _replay(); })),
          SimSlider(label: 'Common difference d: ${_d.toStringAsFixed(0)}', value: _d, min: -5, max: 5, divisions: 10, activeColor: Colors.teal, onChanged: (v) => setState(() { _d = v; _replay(); })),
          SimSlider(label: 'Number of terms n: $_n', value: _n.toDouble(), min: 2, max: 12, divisions: 10, activeColor: Colors.indigo, onChanged: (v) => setState(() { _n = v.round(); _replay(); })),
        ],
      ),
    );
  }
}
