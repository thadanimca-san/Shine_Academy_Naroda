import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Side-by-side growth bars for simple vs compound interest on the same
/// principal, rate and time — the bars rise from zero on load or replay,
/// showing why compound interest pulls ahead.
class Class8ComparingQuantitiesSimulationWidget extends StatefulWidget {
  const Class8ComparingQuantitiesSimulationWidget({super.key});

  @override
  State<Class8ComparingQuantitiesSimulationWidget> createState() => _ComparingQuantitiesSimulationWidgetState();
}

class _ComparingQuantitiesSimulationWidgetState extends State<Class8ComparingQuantitiesSimulationWidget> with SingleTickerProviderStateMixin {
  double _principal = 5000;
  double _rate = 10;
  double _time = 3;
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
    final si = (_principal * _rate * _time) / 100;
    double amountCI = _principal;
    for (int i = 0; i < _time.round(); i++) {
      amountCI *= (1 + _rate / 100);
    }
    final ci = amountCI - _principal;
    final maxVal = [si, ci].reduce((a, b) => a > b ? a : b);

    return SimFrame(
      title: 'Simple vs Compound Interest',
      icon: Icons.trending_up,
      accent: Colors.green.shade700,
      description: 'Same principal, rate and time — watch both bars grow and compare how much more compound interest earns.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              final siT = Curves.easeOutBack.transform((_controller.value / 0.75).clamp(0.0, 1.0));
              final ciT = Curves.easeOutBack.transform(((_controller.value - 0.15) / 0.85).clamp(0.0, 1.0));
              return SizedBox(
                height: 160,
                child: Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    _bar('SI', si, maxVal, Colors.blue, siT),
                    _bar('CI', ci, maxVal, Colors.green, ciT),
                  ],
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
              style: TextButton.styleFrom(foregroundColor: Colors.green.shade700),
            ),
          ),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Simple Interest', value: '₹${si.toStringAsFixed(0)}', color: Colors.blue),
            SimMetric(label: 'Compound Interest', value: '₹${ci.toStringAsFixed(0)}', color: Colors.green),
            SimMetric(label: 'Difference', value: '₹${(ci - si).toStringAsFixed(0)}', color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Principal: ₹${_principal.toStringAsFixed(0)}', value: _principal, min: 1000, max: 20000, divisions: 19, activeColor: Colors.green, onChanged: (v) => setState(() { _principal = v; _replay(); })),
          SimSlider(label: 'Rate: ${_rate.toStringAsFixed(0)}%', value: _rate, min: 1, max: 20, divisions: 19, activeColor: Colors.teal, onChanged: (v) => setState(() { _rate = v; _replay(); })),
          SimSlider(label: 'Time: ${_time.toStringAsFixed(0)} years', value: _time, min: 1, max: 8, divisions: 7, activeColor: Colors.indigo, onChanged: (v) => setState(() { _time = v; _replay(); })),
        ],
      ),
    );
  }

  Widget _bar(String label, double value, double maxVal, Color color, double t) {
    final height = (maxVal > 0 ? (value / maxVal) * 110 : 0.0) * t.clamp(0.0, 1.0);
    return Column(
      mainAxisAlignment: MainAxisAlignment.end,
      children: [
        Text('₹${value.toStringAsFixed(0)}', style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold)),
        const SizedBox(height: 4),
        Container(width: 50, height: height, decoration: BoxDecoration(color: color, borderRadius: const BorderRadius.vertical(top: Radius.circular(6)))),
        const SizedBox(height: 4),
        Text(label, style: TextStyle(fontSize: 12)),
      ],
    );
  }
}
