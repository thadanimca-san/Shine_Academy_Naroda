import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// The Midpoint Theorem, shown live: press play to watch the apex swing
/// through a range of positions while the segment joining two
/// side-midpoints keeps re-forming, staying parallel to (and half the
/// length of) the third side.
class Class9QuadrilateralsSimulationWidget extends StatefulWidget {
  const Class9QuadrilateralsSimulationWidget({super.key});

  @override
  State<Class9QuadrilateralsSimulationWidget> createState() => _Class9QuadrilateralsSimulationWidgetState();
}

class _Class9QuadrilateralsSimulationWidgetState extends State<Class9QuadrilateralsSimulationWidget> with SingleTickerProviderStateMixin {
  double _apexX = 0.5;
  double _apexY = 0.2;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 1800));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _play() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'The Midpoint Theorem',
      icon: Icons.horizontal_split,
      accent: Colors.indigo.shade600,
      description: 'Press play to swing the apex — the segment joining the midpoints of two sides of a triangle stays parallel to the third side and half its length, no matter the shape.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 180,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.indigo.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final t = _controller.value;
                final eased = Curves.easeInOut.transform(t);
                final sweep = eased < 0.5 ? eased * 2 : (1 - eased) * 2;
                final animatedX = t == 0 ? _apexX : 0.25 + sweep * 0.5;
                return CustomPaint(size: Size.infinite, painter: _MidpointPainter(apexX: animatedX, apexY: _apexY));
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: ElevatedButton.icon(
              onPressed: _play,
              icon: Icon(Icons.play_arrow),
              label: Text(TrilingualService.instance.getUIText('Swing apex')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.indigo.shade600, foregroundColor: Colors.white),
            ),
          ),
          const SizedBox(height: 14),
          SimSlider(label: 'Apex horizontal position', value: _apexX, min: 0.2, max: 0.8, divisions: 12, activeColor: Colors.indigo, onChanged: (v) => setState(() { _apexX = v; _controller.value = 0; })),
          SimSlider(label: 'Apex height', value: _apexY, min: 0.1, max: 0.6, divisions: 10, activeColor: Colors.teal, onChanged: (v) => setState(() { _apexY = v; _controller.value = 0; })),
        ],
      ),
    );
  }
}

class _MidpointPainter extends CustomPainter {
  final double apexX, apexY;
  _MidpointPainter({required this.apexX, required this.apexY});

  @override
  void paint(Canvas canvas, Size size) {
    final b = Offset(size.width * 0.15, size.height * 0.85);
    final c = Offset(size.width * 0.85, size.height * 0.85);
    final a = Offset(size.width * apexX, size.height * apexY);

    final trianglePaint = Paint()
      ..color = Colors.indigo.shade800
      ..strokeWidth = 2;
    canvas.drawLine(b, c, trianglePaint);
    canvas.drawLine(b, a, trianglePaint);
    canvas.drawLine(c, a, trianglePaint);

    final midAB = Offset((a.dx + b.dx) / 2, (a.dy + b.dy) / 2);
    final midAC = Offset((a.dx + c.dx) / 2, (a.dy + c.dy) / 2);
    canvas.drawLine(midAB, midAC, Paint()..color = Colors.deepOrange..strokeWidth = 3);
    canvas.drawCircle(midAB, 4, Paint()..color = Colors.deepOrange);
    canvas.drawCircle(midAC, 4, Paint()..color = Colors.deepOrange);
  }

  @override
  bool shouldRepaint(covariant _MidpointPainter oldDelegate) => oldDelegate.apexX != apexX || oldDelegate.apexY != apexY;
}
