import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// Steps through Euclid's Division Algorithm to find the HCF of two
/// numbers: each a = bq + r step fades and slides into place in sequence
/// until the remainder hits zero.
class RealNumbersSimulationWidget extends StatefulWidget {
  const RealNumbersSimulationWidget({super.key});

  @override
  State<RealNumbersSimulationWidget> createState() => _RealNumbersSimulationWidgetState();
}

class _RealNumbersSimulationWidgetState extends State<RealNumbersSimulationWidget> with SingleTickerProviderStateMixin {
  int _numA = 60;
  int _numB = 100;
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

  List<List<int>> _computeSteps() {
    int a = _numA > _numB ? _numA : _numB;
    int b = _numA > _numB ? _numB : _numA;
    final steps = <List<int>>[];
    while (b != 0) {
      final q = a ~/ b;
      final r = a % b;
      steps.add([a, b, q, r]);
      a = b;
      b = r;
    }
    return steps;
  }

  @override
  Widget build(BuildContext context) {
    final steps = _computeSteps();
    final hcf = steps.isEmpty ? _numA : steps.last[1];

    return SimFrame(
      title: "Euclid's Division Algorithm",
      icon: Icons.functions,
      accent: Colors.indigo.shade600,
      description: 'Watch the HCF of two numbers emerge step by step: a = bq + r, repeated until the remainder is zero.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(children: [
            Expanded(child: _stepper('a', _numA, (v) { setState(() => _numA = v); _replay(); })),
            const SizedBox(width: 10),
            Expanded(child: _stepper('b', _numB, (v) { setState(() => _numB = v); _replay(); })),
          ]),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.indigo.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                return Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: List.generate(steps.length, (i) {
                    // Stagger each step's fade/slide-in so they appear in algorithmic order.
                    final start = steps.isEmpty ? 0.0 : i / steps.length;
                    final end = steps.isEmpty ? 1.0 : start + (1 / steps.length);
                    final localT = ((_controller.value - start) / (end - start)).clamp(0.0, 1.0);
                    final eased = Curves.easeOut.transform(localT);
                    final s = steps[i];
                    return Opacity(
                      opacity: eased,
                      child: Transform.translate(
                        offset: Offset((1 - eased) * 24, 0),
                        child: Padding(
                          padding: const EdgeInsets.only(bottom: 4),
                          child: Text('${s[0]} = ${s[1]} × ${s[2]} + ${s[3]}', style: TextStyle(fontSize: 13, fontFamily: 'monospace')),
                        ),
                      ),
                    );
                  }),
                );
              },
            ),
          ),
          const SizedBox(height: 10),
          SimMetricPanel(metrics: [
            SimMetric(label: 'HCF', value: '$hcf', color: Colors.deepOrange),
          ]),
        ],
      ),
    );
  }

  Widget _stepper(String label, int value, ValueChanged<int> onChanged) {
    return Row(
      children: [
        Text('$label:', style: TextStyle(fontWeight: FontWeight.bold)),
        IconButton(icon: Icon(Icons.remove_circle_outline), onPressed: value > 2 ? () => onChanged(value - 2) : null),
        SizedBox(width: 40, child: Text('$value', textAlign: TextAlign.center)),
        IconButton(icon: Icon(Icons.add_circle_outline), onPressed: value < 200 ? () => onChanged(value + 2) : null),
      ],
    );
  }
}
