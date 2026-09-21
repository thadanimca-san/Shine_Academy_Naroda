import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A coin-flip trial simulator: tap to flip (once or many times) and
/// watch the coin spin through a flip animation before landing, while
/// the empirical probability of heads converges toward 0.5 as trials
/// accumulate.
class ProbabilitySimulationWidget extends StatefulWidget {
  const ProbabilitySimulationWidget({super.key});

  @override
  State<ProbabilitySimulationWidget> createState() => _ProbabilitySimulationWidgetState();
}

class _ProbabilitySimulationWidgetState extends State<ProbabilitySimulationWidget> with SingleTickerProviderStateMixin {
  int _heads = 0;
  int _trials = 0;
  final math.Random _rand = math.Random();
  bool? _lastFlip;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 500));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _flip([int count = 1]) {
    setState(() {
      for (int i = 0; i < count; i++) {
        final isHeads = _rand.nextBool();
        _lastFlip = isHeads;
        if (isHeads) _heads++;
        _trials++;
      }
    });
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    final probability = _trials == 0 ? 0.0 : _heads / _trials;

    return SimFrame(
      title: 'Empirical Probability: Coin Flips',
      icon: Icons.casino,
      accent: Colors.green.shade700,
      description: 'Flip a coin many times — watch it spin and land — the empirical probability of heads settles closer to 0.5 as trials increase.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 110,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(10)),
            child: Center(
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) {
                  // Spin the coin several full turns, settling on the result face.
                  final t = Curves.easeOut.transform(_controller.value);
                  final spin = t * math.pi * 6;
                  final scaleX = math.cos(spin).abs().clamp(0.15, 1.0);
                  final showBack = (spin / math.pi).floor().isOdd;
                  final isHeads = _lastFlip == null ? true : _lastFlip!;
                  final faceIsHeads = _controller.isCompleted ? isHeads : (showBack ? !isHeads : isHeads);
                  return Transform(
                    alignment: Alignment.center,
                    transform: Matrix4.identity()..scaleByDouble(scaleX, 1.0, 1.0, 1.0),
                    child: Icon(
                      _lastFlip == null ? Icons.circle_outlined : (faceIsHeads ? Icons.circle : Icons.change_history),
                      size: 50,
                      color: _lastFlip == null ? Colors.grey : (faceIsHeads ? Colors.amber.shade700 : Colors.blueGrey),
                    ),
                  );
                },
              ),
            ),
          ),
          const SizedBox(height: 4),
          Center(child: Text(_lastFlip == null ? 'Tap Flip to begin' : (_lastFlip! ? 'Heads' : 'Tails'), style: TextStyle(fontWeight: FontWeight.w600))),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Trials', value: '$_trials'),
            SimMetric(label: 'Heads', value: '$_heads', color: Colors.amber.shade800),
            SimMetric(label: 'P(Heads)', value: probability.toStringAsFixed(3), color: Colors.green),
          ]),
          const SizedBox(height: 14),
          Row(
            children: [
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: () => _flip(),
                  icon: Icon(Icons.touch_app),
                  label: Text(TrilingualService.instance.getUIText('Flip Once')),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.green.shade700, foregroundColor: Colors.white),
                ),
              ),
              const SizedBox(width: 10),
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: () => _flip(50),
                  icon: Icon(Icons.fast_forward),
                  label: Text(TrilingualService.instance.getUIText('Flip 50×')),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.teal.shade700, foregroundColor: Colors.white),
                ),
              ),
              const SizedBox(width: 10),
              OutlinedButton.icon(
                onPressed: () => setState(() {
                  _heads = 0;
                  _trials = 0;
                  _lastFlip = null;
                }),
                icon: Icon(Icons.refresh),
                label: Text(TrilingualService.instance.getUIText('Reset')),
              ),
            ],
          ),
        ],
      ),
    );
  }
}
