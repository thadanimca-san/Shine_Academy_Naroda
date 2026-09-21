import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A base/exponent calculator: slide the base and exponent to see the
/// expanded multiplication form and final value compute live. Press
/// play to watch each factor of the expansion appear one at a time,
/// left to right, making "repeated multiplication" concrete.
class ExponentsPowersSimulationWidget extends StatefulWidget {
  const ExponentsPowersSimulationWidget({super.key});

  @override
  State<ExponentsPowersSimulationWidget> createState() => _ExponentsPowersSimulationWidgetState();
}

class _ExponentsPowersSimulationWidgetState extends State<ExponentsPowersSimulationWidget> with SingleTickerProviderStateMixin {
  int _base = 2;
  int _exponent = 4;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 1000));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _play() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    int result = 1;
    for (int i = 0; i < _exponent; i++) {
      result *= _base;
    }
    final factors = List.filled(_exponent, _base);

    return SimFrame(
      title: 'Exponents Calculator',
      icon: Icons.exposure,
      accent: Colors.purple.shade600,
      description: 'Change the base and exponent, then press play to watch the multiplication build up factor by factor.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(color: Colors.purple.shade50, borderRadius: BorderRadius.circular(10)),
            child: Column(
              children: [
                Text('$_base$_supExponent', style: TextStyle(fontSize: 22, fontWeight: FontWeight.bold)),
                const SizedBox(height: 10),
                AnimatedBuilder(
                  animation: _controller,
                  builder: (context, _) {
                    if (_exponent == 0) {
                      return Text(TrilingualService.instance.getUIText('= 1 (any non-zero number to the power 0)'), style: TextStyle(fontSize: 14), textAlign: TextAlign.center);
                    }
                    final shown = (factors.length * _controller.value).ceil().clamp(0, factors.length);
                    final expanded = factors.take(shown).map((f) => '$f').join(' × ');
                    final complete = shown == factors.length;
                    return Wrap(
                      alignment: WrapAlignment.center,
                      crossAxisAlignment: WrapCrossAlignment.center,
                      children: [
                        Text('= $expanded', style: TextStyle(fontSize: 14, color: Colors.purple.shade800, fontWeight: FontWeight.bold)),
                        if (complete) Text('  =  $result', style: TextStyle(fontSize: 14, color: Colors.purple.shade800, fontWeight: FontWeight.bold)),
                      ],
                    );
                  },
                ),
              ],
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: TextButton.icon(
              onPressed: _play,
              icon: Icon(Icons.play_arrow, size: 18),
              label: Text(TrilingualService.instance.getUIText('Build expansion')),
              style: TextButton.styleFrom(foregroundColor: Colors.purple.shade600),
            ),
          ),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Base', value: '$_base'),
            SimMetric(label: 'Exponent', value: '$_exponent'),
            SimMetric(label: 'Value', value: '$result', color: Colors.purple),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Base: $_base', value: _base.toDouble(), min: 1, max: 6, divisions: 5, activeColor: Colors.purple, onChanged: (v) => setState(() { _base = v.round(); _play(); })),
          SimSlider(label: 'Exponent: $_exponent', value: _exponent.toDouble(), min: 0, max: 6, divisions: 6, activeColor: Colors.deepPurple, onChanged: (v) => setState(() { _exponent = v.round(); _play(); })),
        ],
      ),
    );
  }

  String get _supExponent {
    const supers = {'0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴', '5': '⁵', '6': '⁶'};
    return '$_exponent'.split('').map((c) => supers[c] ?? c).join();
  }
}
