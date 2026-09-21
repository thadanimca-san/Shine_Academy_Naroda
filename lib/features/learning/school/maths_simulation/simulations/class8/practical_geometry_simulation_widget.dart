import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Step {
  final String title;
  final String description;
  const _Step(this.title, this.description);
}

/// Steps through constructing a quadrilateral given four sides and a
/// diagonal, by splitting it into two triangles — each step's new lines
/// draw themselves in rather than appearing instantly.
class Class8PracticalGeometrySimulationWidget extends StatefulWidget {
  const Class8PracticalGeometrySimulationWidget({super.key});

  @override
  State<Class8PracticalGeometrySimulationWidget> createState() => _PracticalGeometrySimulationWidgetState();
}

class _PracticalGeometrySimulationWidgetState extends State<Class8PracticalGeometrySimulationWidget> with SingleTickerProviderStateMixin {
  static const _steps = [
    _Step('Draw the diagonal', 'Draw diagonal AC of the given length using a ruler.'),
    _Step('Construct triangle ABC', 'Using sides AB and BC, draw arcs from A and C to locate vertex B (SSS).'),
    _Step('Construct triangle ACD', 'Using sides AD and CD, draw arcs from A and C on the other side to locate vertex D.'),
    _Step('Join the vertices', 'Join A-B, B-C, C-D and D-A to complete quadrilateral ABCD.'),
  ];

  int _index = 0;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 600));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _goTo(int newIndex) {
    setState(() {
      _index = newIndex;
      _controller.forward(from: 0);
    });
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Constructing a Quadrilateral',
      icon: Icons.architecture,
      accent: Colors.deepPurple.shade400,
      description: 'Step through constructing a quadrilateral from four sides and one diagonal — each step draws itself in.',
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
                return CustomPaint(size: Size.infinite, painter: _QuadConstructionPainter(step: _index, stepT: eased));
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

class _QuadConstructionPainter extends CustomPainter {
  final int step;
  final double stepT;
  _QuadConstructionPainter({required this.step, required this.stepT});

  @override
  void paint(Canvas canvas, Size size) {
    final a = Offset(size.width * 0.2, size.height * 0.5);
    final c = Offset(size.width * 0.8, size.height * 0.5);
    final b = Offset(size.width * 0.55, size.height * 0.85);
    final d = Offset(size.width * 0.45, size.height * 0.15);
    final linePaint = Paint()
      ..color = Colors.deepPurple.shade800
      ..strokeWidth = 2.5;

    // Step 0's diagonal grows in; earlier steps' lines are already complete.
    final acEnd = step == 0 ? Offset.lerp(a, c, stepT)! : c;
    canvas.drawLine(a, acEnd, linePaint);
    canvas.drawCircle(a, 3, Paint()..color = Colors.black);
    if (step > 0 || stepT > 0.9) {
      canvas.drawCircle(c, 3, Paint()..color = Colors.black);
      _label(canvas, c + const Offset(6, 0), 'C');
    }
    _label(canvas, a + const Offset(-14, 0), 'A');

    if (step >= 1) {
      final t = step == 1 ? stepT : 1.0;
      canvas.drawLine(a, Offset.lerp(a, b, t)!, linePaint);
      canvas.drawLine(c, Offset.lerp(c, b, t)!, linePaint);
      if (t > 0.9) {
        canvas.drawCircle(b, 3, Paint()..color = Colors.red);
        _label(canvas, b + const Offset(0, 12), 'B');
      }
    }
    if (step >= 2) {
      final t = step == 2 ? stepT : 1.0;
      canvas.drawLine(a, Offset.lerp(a, d, t)!, linePaint);
      canvas.drawLine(c, Offset.lerp(c, d, t)!, linePaint);
      if (t > 0.9) {
        canvas.drawCircle(d, 3, Paint()..color = Colors.red);
        _label(canvas, d + const Offset(0, -16), 'D');
      }
    }
    if (step >= 3) {
      // Final step re-traces the four sides to emphasise the closed shape.
      final t = stepT;
      final segs = [
        [a, b],
        [b, c],
        [c, d],
        [d, a],
      ];
      final total = segs.length;
      for (int i = 0; i < total; i++) {
        final segStart = i / total;
        final segEnd = segStart + 1 / total;
        final segT = ((t - segStart) / (segEnd - segStart)).clamp(0.0, 1.0);
        if (segT <= 0) continue;
        canvas.drawLine(segs[i][0], Offset.lerp(segs[i][0], segs[i][1], segT)!, Paint()..color = Colors.deepPurple..strokeWidth = 3.5);
      }
    }
  }

  void _label(Canvas canvas, Offset pos, String text) {
    final tp = TextPainter(text: TextSpan(text: text, style: TextStyle(color: Colors.black87, fontWeight: FontWeight.bold, fontSize: 12)), textDirection: TextDirection.ltr)..layout();
    tp.paint(canvas, pos);
  }

  @override
  bool shouldRepaint(covariant _QuadConstructionPainter oldDelegate) => oldDelegate.step != step || oldDelegate.stepT != stepT;
}
