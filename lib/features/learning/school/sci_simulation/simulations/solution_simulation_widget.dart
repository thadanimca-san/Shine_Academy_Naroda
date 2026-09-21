import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A dissolving-solute demo for "Is Matter Around Us Pure": add spoonfuls
/// of solute to a beaker of solvent and watch particles dissolve and
/// spread evenly until the solution is saturated and excess settles out.
class SolutionSimulationWidget extends StatefulWidget {
  const SolutionSimulationWidget({super.key});

  @override
  State<SolutionSimulationWidget> createState() => _SolutionSimulationWidgetState();
}

class _SolutionSimulationWidgetState extends State<SolutionSimulationWidget> with SingleTickerProviderStateMixin {
  int _spoonsAdded = 0;
  static const int _saturationPoint = 6;
  late AnimationController _controller;
  final math.Random _rand = math.Random(3);

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 40))
      ..addListener(() => setState(() {}))
      ..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  bool get _isSaturated => _spoonsAdded > _saturationPoint;
  int get _dissolvedSpoons => math.min(_spoonsAdded, _saturationPoint);
  int get _undissolvedSpoons => (_spoonsAdded - _saturationPoint).clamp(0, 999);

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Solutions & Saturation',
      icon: Icons.water_drop,
      accent: Colors.lightBlue.shade700,
      description: 'Add solute (sugar) spoon by spoon. Dissolved particles spread evenly through the solvent — until the solution is saturated and no more will dissolve.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          LayoutBuilder(builder: (context, constraints) {
            const beakerHeight = 170.0;
            return Container(
              height: beakerHeight,
              width: double.infinity,
              decoration: BoxDecoration(
                color: Colors.lightBlue.shade50,
                border: Border.all(color: Colors.blueGrey.shade300, width: 2),
                borderRadius: BorderRadius.circular(10),
              ),
              child: CustomPaint(
                size: Size(constraints.maxWidth, beakerHeight),
                painter: _SolutionPainter(
                  dissolved: _dissolvedSpoons,
                  undissolved: _undissolvedSpoons,
                  t: _controller.value,
                  seed: _rand,
                ),
              ),
            );
          }),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Spoons added', value: '$_spoonsAdded'),
            SimMetric(label: 'Dissolved', value: '$_dissolvedSpoons', color: Colors.teal),
            SimMetric(label: 'Settled (excess)', value: '$_undissolvedSpoons', color: Colors.deepOrange),
          ]),
          const SizedBox(height: 8),
          Text(
            _isSaturated
                ? 'Saturated: extra solute simply settles at the bottom — the solution can\'t dissolve more at this temperature.'
                : (_spoonsAdded == 0 ? 'Tap "Add Spoon" to begin dissolving solute.' : 'Unsaturated: all the solute dissolves and spreads evenly.'),
            style: TextStyle(fontWeight: FontWeight.w600, color: _isSaturated ? Colors.deepOrange : Colors.teal.shade700, fontSize: 13),
          ),
          const SizedBox(height: 14),
          Row(
            children: [
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: () => setState(() => _spoonsAdded++),
                  icon: Icon(Icons.add),
                  label: Text(TrilingualService.instance.getUIText('Add Spoon')),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.lightBlue.shade700, foregroundColor: Colors.white),
                ),
              ),
              const SizedBox(width: 10),
              OutlinedButton.icon(
                onPressed: _spoonsAdded == 0 ? null : () => setState(() => _spoonsAdded = 0),
                icon: Icon(Icons.replay),
                label: Text(TrilingualService.instance.getUIText('Reset')),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class _SolutionPainter extends CustomPainter {
  final int dissolved;
  final int undissolved;
  final double t;
  final math.Random seed;

  _SolutionPainter({required this.dissolved, required this.undissolved, required this.t, required this.seed});

  @override
  void paint(Canvas canvas, Size size) {
    // liquid fill
    canvas.drawRect(Rect.fromLTWH(0, size.height * 0.15, size.width, size.height * 0.85), Paint()..color = Colors.blue.withValues(alpha: 0.15));

    // dissolved particles spread evenly, gently drifting
    final rnd = math.Random(42);
    for (int i = 0; i < dissolved * 12; i++) {
      final baseX = rnd.nextDouble() * size.width;
      final baseY = size.height * 0.2 + rnd.nextDouble() * size.height * 0.65;
      final dx = math.sin(t * 2 * math.pi + i) * 2;
      final dy = math.cos(t * 2 * math.pi + i * 1.3) * 2;
      canvas.drawCircle(Offset(baseX + dx, baseY + dy), 1.8, Paint()..color = Colors.blue.shade300);
    }

    // undissolved settles as a heap at the bottom
    if (undissolved > 0) {
      final heapWidth = (undissolved * 14).clamp(0, size.width - 20).toDouble();
      final rect = Rect.fromCenter(center: Offset(size.width / 2, size.height - 14), width: heapWidth, height: 18);
      canvas.drawRRect(RRect.fromRectAndRadius(rect, const Radius.circular(4)), Paint()..color = Colors.white);
      final rnd2 = math.Random(99);
      for (int i = 0; i < undissolved * 20; i++) {
        final x = rect.left + rnd2.nextDouble() * rect.width;
        final y = rect.top + rnd2.nextDouble() * rect.height;
        canvas.drawCircle(Offset(x, y), 1.2, Paint()..color = Colors.blueGrey.shade300);
      }
    }
  }

  @override
  bool shouldRepaint(covariant _SolutionPainter oldDelegate) => true;
}
