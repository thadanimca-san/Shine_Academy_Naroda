import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A prism dispersion demo: white light enters a prism and splits into
/// the seven colours of the rainbow (VIBGYOR), with a slider to spread
/// the band wider or narrower.
class Class7LightSimulationWidget extends StatefulWidget {
  const Class7LightSimulationWidget({super.key});

  @override
  State<Class7LightSimulationWidget> createState() => _Class7LightSimulationWidgetState();
}

class _Class7LightSimulationWidgetState extends State<Class7LightSimulationWidget> {
  double _spread = 0.5;

  static const _colors = [
    Colors.deepPurple, Colors.indigo, Colors.blue, Colors.green, Colors.yellow, Colors.orange, Colors.red,
  ];
  static const _names = ['Violet', 'Indigo', 'Blue', 'Green', 'Yellow', 'Orange', 'Red'];

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Dispersion of Light',
      icon: Icons.auto_awesome,
      accent: Colors.deepPurple.shade400,
      description: 'White light splits into seven colours (VIBGYOR) as it passes through a prism.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.grey.shade900, borderRadius: BorderRadius.circular(10)),
            child: LayoutBuilder(builder: (context, constraints) {
              final w = constraints.maxWidth;
              final prismX = w * 0.42;
              return Stack(
                children: [
                  Positioned(top: 78, left: 0, width: prismX, child: Container(height: 4, color: Colors.white)),
                  Positioned(
                    left: prismX - 22,
                    top: 55,
                    child: CustomPaint(size: const Size(44, 50), painter: _PrismPainter()),
                  ),
                  ...List.generate(7, (i) {
                    final spreadPx = 10 + _spread * 70;
                    return Positioned(
                      left: prismX + 22,
                      top: 78,
                      child: CustomPaint(
                        size: Size(w - prismX - 22, 1),
                        painter: _RayPainter(color: _colors[i], endOffset: Offset(w - prismX - 22, (i - 3) * spreadPx / 7 * 2)),
                      ),
                    );
                  }),
                ],
              );
            }),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 4,
            children: List.generate(7, (i) => Chip(label: Text(_names[i], style: TextStyle(fontSize: 10, color: Colors.white)), backgroundColor: _colors[i], padding: EdgeInsets.zero, visualDensity: VisualDensity.compact)),
          ),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Band spread',
            value: _spread,
            min: 0.1,
            max: 1.0,
            divisions: 18,
            activeColor: Colors.deepPurple,
            onChanged: (val) => setState(() => _spread = val),
          ),
        ],
      ),
    );
  }
}

class _PrismPainter extends CustomPainter {
  @override
  void paint(Canvas canvas, Size size) {
    final path = Path()
      ..moveTo(size.width / 2, 0)
      ..lineTo(0, size.height)
      ..lineTo(size.width, size.height)
      ..close();
    canvas.drawPath(path, Paint()..color = Colors.white.withValues(alpha: 0.85));
  }

  @override
  bool shouldRepaint(covariant _PrismPainter oldDelegate) => false;
}

class _RayPainter extends CustomPainter {
  final Color color;
  final Offset endOffset;

  _RayPainter({required this.color, required this.endOffset});

  @override
  void paint(Canvas canvas, Size size) {
    canvas.drawLine(Offset.zero, endOffset, Paint()..color = color..strokeWidth = 2.5);
  }

  @override
  bool shouldRepaint(covariant _RayPainter oldDelegate) => true;
}
