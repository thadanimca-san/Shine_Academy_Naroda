import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Step {
  final String title;
  final String description;
  const _Step(this.title, this.description);
}

/// Steps through constructing a triangle by the SSS method, one ruler-
/// and-compass move at a time. Each step animates in — the base line
/// draws left to right, each arc sweeps out from its centre, and the
/// final sides draw in — so the construction reads as a live drawing
/// rather than a static diagram switching states.
class PracticalGeometrySimulationWidget extends StatefulWidget {
  const PracticalGeometrySimulationWidget({super.key});

  @override
  State<PracticalGeometrySimulationWidget> createState() => _PracticalGeometrySimulationWidgetState();
}

class _PracticalGeometrySimulationWidgetState extends State<PracticalGeometrySimulationWidget> with SingleTickerProviderStateMixin {
  static const _steps = [
    _Step('Draw the base', 'Draw line segment BC of the given length using a ruler.'),
    _Step('Set compass for AB', 'Open the compass to the length of side AB and draw an arc from point B.'),
    _Step('Set compass for AC', 'Open the compass to the length of side AC and draw another arc from point C.'),
    _Step('Mark point A', 'The point where the two arcs intersect is vertex A.'),
    _Step('Complete the triangle', 'Join A to B and A to C with straight lines to complete triangle ABC.'),
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
      title: 'Constructing a Triangle (SSS)',
      icon: Icons.architecture,
      accent: Colors.deepPurple.shade400,
      description: 'Step through each move of a ruler-and-compass SSS construction and watch it draw itself.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 150,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.deepPurple.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                return CustomPaint(size: Size.infinite, painter: _ConstructionPainter(step: _index, stepT: eased));
              },
            ),
          ),
          const SizedBox(height: 10),
          Text('${_index + 1}. ${_steps[_index].title}', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15)),
          const SizedBox(height: 6),
          Text(_steps[_index].description, style: TextStyle(fontSize: 13)),
          const SizedBox(height: 12),
          LinearProgressIndicator(value: (_index + 1) / _steps.length, minHeight: 6, color: Colors.deepPurple, backgroundColor: Colors.deepPurple.shade100),
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
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.deepPurple.shade400, foregroundColor: Colors.white),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }
}

class _ConstructionPainter extends CustomPainter {
  final int step;
  final double stepT; // 0..1 progress of the current step's own animation
  _ConstructionPainter({required this.step, this.stepT = 1});

  @override
  void paint(Canvas canvas, Size size) {
    final b = Offset(size.width * 0.25, size.height * 0.8);
    final c = Offset(size.width * 0.75, size.height * 0.8);
    final a = Offset(size.width * 0.45, size.height * 0.25);
    final linePaint = Paint()
      ..color = Colors.deepPurple.shade800
      ..strokeWidth = 2.5;
    final arcPaint = Paint()
      ..color = Colors.deepPurple.shade300
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.5;

    // The base draws in on step 0; on later steps it's already complete.
    final baseT = step == 0 ? stepT : 1.0;
    canvas.drawLine(b, Offset.lerp(b, c, baseT)!, linePaint);
    canvas.drawCircle(b, 3, Paint()..color = Colors.black);
    if (baseT > 0.05) _label(canvas, b + const Offset(-14, 10), 'B');
    if (baseT >= 0.999) {
      canvas.drawCircle(c, 3, Paint()..color = Colors.black);
      _label(canvas, c + const Offset(6, 10), 'C');
    }

    if (step >= 1) {
      final arcT = step == 1 ? stepT : 1.0;
      final r1 = (a - b).distance;
      canvas.drawArc(Rect.fromCircle(center: b, radius: r1), -1.8, 1.4 * arcT, false, arcPaint);
    }
    if (step >= 2) {
      final arcT = step == 2 ? stepT : 1.0;
      final r2 = (a - c).distance;
      canvas.drawArc(Rect.fromCircle(center: c, radius: r2), -3.1, 1.4 * arcT, false, arcPaint);
    }
    if (step >= 3) {
      final markT = step == 3 ? stepT : 1.0;
      canvas.drawCircle(a, 3 * markT, Paint()..color = Colors.red);
      if (markT > 0.3) _label(canvas, a + const Offset(0, -12), 'A');
    }
    if (step >= 4) {
      final sideT = stepT;
      canvas.drawLine(a, Offset.lerp(a, b, sideT)!, linePaint);
      canvas.drawLine(a, Offset.lerp(a, c, sideT)!, linePaint);
    }
  }

  void _label(Canvas canvas, Offset pos, String text) {
    final tp = TextPainter(text: TextSpan(text: text, style: TextStyle(color: Colors.black87, fontWeight: FontWeight.bold, fontSize: 12)), textDirection: TextDirection.ltr)..layout();
    tp.paint(canvas, pos);
  }

  @override
  bool shouldRepaint(covariant _ConstructionPainter oldDelegate) => oldDelegate.step != step || oldDelegate.stepT != stepT;
}
