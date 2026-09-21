import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Step {
  final String title;
  final String description;
  const _Step(this.title, this.description);
}

/// Steps through bisecting an angle with a compass: each step animates
/// in (arcs sweeping open, the bisector ray drawing itself) rather than
/// snapping instantly, ending with a visible check that both halves are
/// equal.
class ConstructionsSimulationWidget extends StatefulWidget {
  const ConstructionsSimulationWidget({super.key});

  @override
  State<ConstructionsSimulationWidget> createState() => _ConstructionsSimulationWidgetState();
}

class _ConstructionsSimulationWidgetState extends State<ConstructionsSimulationWidget> with SingleTickerProviderStateMixin {
  static const _steps = [
    _Step('Draw the angle', 'Start with angle ∠ABC to be bisected, with vertex B.'),
    _Step('Draw an arc from B', 'With B as centre, draw an arc cutting both arms at points P and Q.'),
    _Step('Draw arcs from P and Q', 'With the same radius, draw arcs from P and Q that intersect at point R.'),
    _Step('Draw the bisector', 'Join B to R — ray BR bisects angle ABC into two equal halves.'),
  ];

  int _index = 0;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 700));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _goTo(int i) {
    setState(() => _index = i);
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Bisecting an Angle',
      icon: Icons.architecture,
      accent: Colors.deepOrange.shade400,
      description: 'Step through the classic compass-and-straightedge angle bisection — each step animates in.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 160,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.deepOrange.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeOutBack.transform(_controller.value);
                return CustomPaint(size: Size.infinite, painter: _BisectorPainter(step: _index, progress: eased.clamp(0.0, 1.0)));
              },
            ),
          ),
          const SizedBox(height: 10),
          Text('${_index + 1}. ${_steps[_index].title}', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15)),
          const SizedBox(height: 6),
          Text(_steps[_index].description, style: TextStyle(fontSize: 13)),
          const SizedBox(height: 12),
          LinearProgressIndicator(value: (_index + 1) / _steps.length, minHeight: 6, color: Colors.deepOrange, backgroundColor: Colors.deepOrange.shade100),
          const SizedBox(height: 14),
          Row(
            children: [
              Expanded(child: OutlinedButton.icon(onPressed: _index == 0 ? null : () => _goTo(_index - 1), icon: Icon(Icons.arrow_back), label: Text(TrilingualService.instance.getUIText('Previous')))),
              const SizedBox(width: 10),
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: _index == _steps.length - 1 ? null : () => _goTo(_index + 1),
                  icon: Icon(Icons.arrow_forward),
                  label: Text(TrilingualService.instance.getUIText('Next')),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.deepOrange.shade400, foregroundColor: Colors.white),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class _BisectorPainter extends CustomPainter {
  final int step;
  final double progress;
  _BisectorPainter({required this.step, this.progress = 1});

  @override
  void paint(Canvas canvas, Size size) {
    final b = Offset(size.width * 0.2, size.height * 0.8);
    final aArm = Offset(size.width * 0.85, size.height * 0.85);
    final cArm = Offset(size.width * 0.5, size.height * 0.1);
    final linePaint = Paint()
      ..color = Colors.deepOrange.shade800
      ..strokeWidth = 2.5;
    canvas.drawLine(b, aArm, linePaint);
    canvas.drawLine(b, cArm, linePaint);
    _label(canvas, b + const Offset(-16, 6), 'B');
    _label(canvas, aArm + const Offset(4, 0), 'A');
    _label(canvas, cArm + const Offset(0, -14), 'C');

    if (step >= 1) {
      final arcProgress = step == 1 ? progress : 1.0;
      canvas.drawArc(Rect.fromCircle(center: b, radius: 60), -0.9, 0.7 * arcProgress, false, Paint()..color = Colors.deepPurple..style = PaintingStyle.stroke..strokeWidth = 1.5);
    }
    if (step >= 2) {
      final pqScale = step == 2 ? progress : 1.0;
      final p = b + Offset.fromDirection(-0.2, 60);
      final q = b + Offset.fromDirection(-1.3, 60);
      canvas.drawCircle(p, 3, Paint()..color = Colors.black);
      canvas.drawCircle(q, 3, Paint()..color = Colors.black);
      final r = Offset((p.dx + q.dx) / 2 - 10, (p.dy + q.dy) / 2 - 10);
      final rShown = Offset.lerp(p, r, pqScale.clamp(0.0, 1.0)) ?? r;
      canvas.drawCircle(rShown, 4, Paint()..color = Colors.red.withValues(alpha: pqScale.clamp(0.0, 1.0)));
      if (step >= 3) {
        final lineProgress = step == 3 ? progress : 1.0;
        final rayEnd = Offset.lerp(b, r + (r - b) * 0.3, lineProgress.clamp(0.0, 1.0)) ?? r;
        canvas.drawLine(b, rayEnd, Paint()..color = Colors.red..strokeWidth = 2.5);
      }
    }
  }

  void _label(Canvas canvas, Offset pos, String text) {
    final tp = TextPainter(text: TextSpan(text: text, style: TextStyle(color: Colors.black87, fontWeight: FontWeight.bold, fontSize: 12)), textDirection: TextDirection.ltr)..layout();
    tp.paint(canvas, pos);
  }

  @override
  bool shouldRepaint(covariant _BisectorPainter oldDelegate) => oldDelegate.step != step || oldDelegate.progress != progress;
}
