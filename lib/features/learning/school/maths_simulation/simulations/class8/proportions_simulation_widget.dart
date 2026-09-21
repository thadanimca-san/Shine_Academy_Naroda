import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import '../common/graph_painter.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Toggle between direct proportion (a straight line through the origin)
/// and inverse proportion (a curve) as the constant k changes — the curve
/// draws itself left-to-right whenever it changes, so the graph shapes
/// stop being abstract vocabulary.
class ProportionsSimulationWidget extends StatefulWidget {
  const ProportionsSimulationWidget({super.key});

  @override
  State<ProportionsSimulationWidget> createState() => _ProportionsSimulationWidgetState();
}

class _ProportionsSimulationWidgetState extends State<ProportionsSimulationWidget> with SingleTickerProviderStateMixin {
  bool _isInverse = false;
  double _k = 4;
  late AnimationController _controller;

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

  void _replay() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final points = List.generate(40, (i) {
      final x = 0.2 + i * (10.0 / 39);
      final y = _isInverse ? _k / x : _k * x;
      return Offset(x / 10, (y / (_isInverse ? _k / 0.2 : _k * 10)).clamp(0.0, 1.0));
    });

    return SimFrame(
      title: 'Direct vs Inverse Proportion Graphs',
      icon: Icons.show_chart,
      accent: Colors.blue.shade700,
      description: 'Direct proportion (y = kx) graphs as a straight line; inverse proportion (y = k/x) graphs as a curve — watch it draw in.',
      actions: [
        ToggleButtons(
          isSelected: [!_isInverse, _isInverse],
          onPressed: (i) => setState(() {
            _isInverse = i == 1;
            _replay();
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.blue.shade700,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 55),
          children: [Text(TrilingualService.instance.getUIText('Direct')), Text(TrilingualService.instance.getUIText('Inverse'))],
        ),
      ],
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              final eased = Curves.easeInOut.transform(_controller.value);
              final visibleCount = (points.length * eased).ceil().clamp(0, points.length);
              return MiniGraph(
                title: _isInverse ? 'y = $_k / x' : 'y = $_k × x',
                points: points.sublist(0, visibleCount),
                color: _isInverse ? Colors.deepOrange : Colors.blue,
              );
            },
          ),
          const SizedBox(height: 6),
          Align(
            alignment: Alignment.centerLeft,
            child: TextButton.icon(
              onPressed: _replay,
              icon: Icon(Icons.replay, size: 18),
              label: Text(TrilingualService.instance.getUIText('Replay')),
              style: TextButton.styleFrom(foregroundColor: Colors.blue.shade700),
            ),
          ),
          SimSlider(label: 'Constant k: ${_k.toStringAsFixed(0)}', value: _k, min: 1, max: 10, divisions: 9, activeColor: Colors.blue, onChanged: (v) => setState(() { _k = v; _replay(); })),
        ],
      ),
    );
  }
}
