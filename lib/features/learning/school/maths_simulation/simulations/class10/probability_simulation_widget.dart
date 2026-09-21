import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Scenario {
  final String name;
  final int favourable;
  final int total;
  final String note;

  const _Scenario(this.name, this.favourable, this.total, this.note);
}

/// A tap-to-explore gallery of classic theoretical-probability scenarios
/// (dice, cards, coins): selecting one spins a die icon through random
/// faces before settling, then the favourable/total outcomes and the
/// resulting probability bar fill in.
class Class10ProbabilitySimulationWidget extends StatefulWidget {
  const Class10ProbabilitySimulationWidget({super.key});

  @override
  State<Class10ProbabilitySimulationWidget> createState() => _ProbabilitySimulationWidgetState();
}

class _ProbabilitySimulationWidgetState extends State<Class10ProbabilitySimulationWidget> with SingleTickerProviderStateMixin {
  static const _scenarios = [
    _Scenario('Even number on a die', 3, 6, 'Favourable: 2, 4, 6'),
    _Scenario('King from a deck', 4, 52, 'Favourable: 4 kings (one per suit)'),
    _Scenario('Head on a coin toss', 1, 2, 'Favourable: 1 head out of 2 outcomes'),
    _Scenario('Multiple of 3 on a die', 2, 6, 'Favourable: 3, 6'),
    _Scenario('Red card from a deck', 26, 52, 'Favourable: 26 red cards (hearts + diamonds)'),
    _Scenario('Sum of 7 with two dice', 6, 36, 'Favourable: (1,6),(2,5),(3,4),(4,3),(5,2),(6,1)'),
  ];

  _Scenario _selected = _scenarios[0];
  late AnimationController _controller;
  final _rand = math.Random();

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

  void _select(_Scenario s) {
    setState(() => _selected = s);
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    final probability = _selected.favourable / _selected.total;

    return SimFrame(
      title: 'Theoretical Probability Scenarios',
      icon: Icons.casino,
      accent: Colors.green.shade700,
      description: 'Tap a classic scenario to spin through the outcomes and watch the probability bar settle.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _scenarios.map((s) {
              final isSelected = _selected.name == s.name;
              return ChoiceChip(
                label: Text(s.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.green.shade700,
                backgroundColor: Colors.green.shade50,
                onSelected: (_) => _select(s),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              final t = _controller.value;
              // First 60% of the animation spins through random faces; final 40% settles.
              final spinning = t < 0.6;
              final face = spinning ? 1 + _rand.nextInt(6) : (_selected.favourable % 6) + 1;
              return Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(vertical: 14),
                decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(10)),
                child: Column(
                  children: [
                    Icon(_dieIcon(face), size: 46, color: Colors.green.shade700),
                    const SizedBox(height: 10),
                    ClipRRect(
                      borderRadius: BorderRadius.circular(6),
                      child: SizedBox(
                        height: 14,
                        width: MediaQuery.of(context).size.width * 0.7,
                        child: LinearProgressIndicator(
                          value: probability * Curves.easeOutCubic.transform(t),
                          backgroundColor: Colors.green.shade100,
                          valueColor: AlwaysStoppedAnimation(Colors.green.shade600),
                        ),
                      ),
                    ),
                  ],
                ),
              );
            },
          ),
          const SizedBox(height: 14),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Favourable', value: '${_selected.favourable}', color: Colors.blue),
            SimMetric(label: 'Total', value: '${_selected.total}', color: Colors.teal),
            SimMetric(label: 'P(Event)', value: probability.toStringAsFixed(3), color: Colors.green),
          ]),
          const SizedBox(height: 10),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(10)),
            child: Text(_selected.note, style: TextStyle(fontSize: 13)),
          ),
        ],
      ),
    );
  }

  IconData _dieIcon(int face) {
    switch (face) {
      case 1:
        return Icons.looks_one;
      case 2:
        return Icons.looks_two;
      case 3:
        return Icons.looks_3;
      case 4:
        return Icons.looks_4;
      case 5:
        return Icons.looks_5;
      default:
        return Icons.looks_6;
    }
  }
}
