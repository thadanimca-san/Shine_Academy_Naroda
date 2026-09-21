import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A base/exponent calculator that supports negative exponents: press play
/// to watch a bar shrink step by step toward zero as the exponent counts
/// down, showing the reciprocal form and decimal value live.
class Class8ExponentsPowersSimulationWidget extends StatefulWidget {
  const Class8ExponentsPowersSimulationWidget({super.key});

  @override
  State<Class8ExponentsPowersSimulationWidget> createState() => _ExponentsPowersSimulationWidgetState();
}

class _ExponentsPowersSimulationWidgetState extends State<Class8ExponentsPowersSimulationWidget> with SingleTickerProviderStateMixin {
  int _base = 2;
  int _exponent = -2;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 900));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _play() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    double value;
    String display;
    if (_exponent >= 0) {
      value = 1;
      for (int i = 0; i < _exponent; i++) {
        value *= _base;
      }
      display = '$_base$_supExponent = ${value.toStringAsFixed(0)}';
    } else {
      double posValue = 1;
      for (int i = 0; i < -_exponent; i++) {
        posValue *= _base;
      }
      value = 1 / posValue;
      display = '$_base$_supExponent = 1/$_base${_supPos(-_exponent)} = ${value.toStringAsFixed(4)}';
    }

    return SimFrame(
      title: 'Negative Exponents Calculator',
      icon: Icons.exposure,
      accent: Colors.purple.shade600,
      description: 'A negative exponent means "take the reciprocal." Press play to watch the value shrink toward zero step by step.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(color: Colors.purple.shade50, borderRadius: BorderRadius.circular(10)),
            child: Text(display, style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold), textAlign: TextAlign.center),
          ),
          const SizedBox(height: 10),
          Container(
            height: 60,
            width: double.infinity,
            padding: const EdgeInsets.symmetric(horizontal: 12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                // Bar width represents |value|, animating from full width (1) to the
                // final magnitude — visually shrinking for negative exponents and
                // growing for positive ones.
                final startFrac = 1.0;
                final endFrac = value.abs().clamp(0.0, 1.0);
                final frac = startFrac + (endFrac - startFrac) * eased;
                return LayoutBuilder(builder: (context, constraints) {
                  return Align(
                    alignment: Alignment.centerLeft,
                    child: Container(
                      height: 24,
                      width: constraints.maxWidth * frac,
                      decoration: BoxDecoration(color: Colors.purple.shade400, borderRadius: BorderRadius.circular(6)),
                    ),
                  );
                });
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: ElevatedButton.icon(
              onPressed: _play,
              icon: Icon(Icons.play_arrow),
              label: Text(TrilingualService.instance.getUIText('Play')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.purple.shade600, foregroundColor: Colors.white),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Base', value: '$_base'),
            SimMetric(label: 'Exponent', value: '$_exponent'),
            SimMetric(label: 'Value', value: value.toStringAsFixed(4), color: Colors.purple),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Base: $_base', value: _base.toDouble(), min: 2, max: 6, divisions: 4, activeColor: Colors.purple, onChanged: (v) => setState(() { _base = v.round(); _controller.value = 1; })),
          SimSlider(label: 'Exponent: $_exponent', value: _exponent.toDouble(), min: -5, max: 5, divisions: 10, activeColor: Colors.deepPurple, onChanged: (v) => setState(() { _exponent = v.round(); _controller.value = 1; })),
        ],
      ),
    );
  }

  String get _supExponent => _supFor(_exponent);

  String _supPos(int n) => _supFor(n);

  String _supFor(int n) {
    const supers = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶', '-': '⁻'};
    return '$n'.split('').map((c) => supers[c] ?? c).join();
  }
}
