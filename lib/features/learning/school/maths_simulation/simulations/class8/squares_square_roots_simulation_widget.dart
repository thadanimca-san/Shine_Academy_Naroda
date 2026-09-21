import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// An n×n dot grid that builds itself row by row: slide n and watch the
/// perfect square n² appear as a literal square array of dots, plus the
/// odd-number-subtraction pattern.
class SquaresSquareRootsSimulationWidget extends StatefulWidget {
  const SquaresSquareRootsSimulationWidget({super.key});

  @override
  State<SquaresSquareRootsSimulationWidget> createState() => _SquaresSquareRootsSimulationWidgetState();
}

class _SquaresSquareRootsSimulationWidgetState extends State<SquaresSquareRootsSimulationWidget> with SingleTickerProviderStateMixin {
  int _n = 5;
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
    final square = _n * _n;
    final oddNumbers = List.generate(_n, (i) => 2 * i + 1);

    return SimFrame(
      title: 'Perfect Squares as Dot Grids',
      icon: Icons.grid_4x4,
      accent: Colors.teal.shade600,
      description: 'n² is literally an n-by-n grid of dots that builds row by row. Notice it also equals the sum of the first n odd numbers.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.teal.shade50, borderRadius: BorderRadius.circular(10)),
            child: Center(
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) {
                  return Wrap(
                    spacing: 4,
                    runSpacing: 4,
                    children: List.generate(square, (i) {
                      final row = i ~/ _n;
                      final start = row / _n;
                      final end = start + (1 / _n);
                      final localT = ((_controller.value - start) / (end - start)).clamp(0.0, 1.0);
                      final eased = Curves.easeOutBack.transform(localT);
                      return Opacity(
                        opacity: eased.clamp(0.0, 1.0),
                        child: Transform.scale(
                          scale: eased.clamp(0.0, 1.0),
                          child: Container(width: 12, height: 12, decoration: BoxDecoration(color: Colors.teal.shade600, shape: BoxShape.circle)),
                        ),
                      );
                    }),
                  );
                },
              ),
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: TextButton.icon(
              onPressed: _replay,
              icon: Icon(Icons.replay, size: 18),
              label: Text(TrilingualService.instance.getUIText('Replay')),
              style: TextButton.styleFrom(foregroundColor: Colors.teal.shade600),
            ),
          ),
          SimMetricPanel(metrics: [
            SimMetric(label: 'n', value: '$_n'),
            SimMetric(label: 'n²', value: '$square', color: Colors.teal),
            SimMetric(label: '√$square', value: '$_n', color: Colors.deepOrange),
          ]),
          const SizedBox(height: 8),
          Text('Sum of first $_n odd numbers: ${oddNumbers.join(' + ')} = $square', style: TextStyle(fontSize: 12, color: Theme.of(context).colorScheme.onSurfaceVariant)),
          const SizedBox(height: 14),
          SimSlider(label: 'n: $_n', value: _n.toDouble(), min: 1, max: 10, divisions: 9, activeColor: Colors.teal, onChanged: (v) => setState(() { _n = v.round(); _replay(); })),
        ],
      ),
    );
  }
}
