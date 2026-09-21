import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// Slide a scale factor and watch a similar triangle animate as it grows
/// or shrinks out from the original, visualising what "scale factor p/q" means.
class Class10ConstructionsSimulationWidget extends StatefulWidget {
  const Class10ConstructionsSimulationWidget({super.key});

  @override
  State<Class10ConstructionsSimulationWidget> createState() => _Class10ConstructionsSimulationWidgetState();
}

class _Class10ConstructionsSimulationWidgetState extends State<Class10ConstructionsSimulationWidget> with SingleTickerProviderStateMixin {
  int _p = 3;
  int _q = 2;
  late AnimationController _controller;
  double _animateFrom = 1;

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

  void _replay(double previousScale) {
    _animateFrom = previousScale;
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    final scale = _p / _q;

    return SimFrame(
      title: 'Similar Triangle: Scale Factor p/q',
      icon: Icons.zoom_out_map,
      accent: Colors.deepOrange.shade400,
      description: 'Construct a triangle similar to a given one, scaled by p/q — watch the new triangle grow or shrink into place.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 180,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.deepOrange.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeOutBack.transform(_controller.value);
                final animatedScale = _animateFrom + (scale - _animateFrom) * eased;
                return CustomPaint(size: Size.infinite, painter: _SimilarTrianglePainter(scale: animatedScale));
              },
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'p', value: '$_p'),
            SimMetric(label: 'q', value: '$_q'),
            SimMetric(label: 'Scale Factor', value: scale.toStringAsFixed(2), color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'p: $_p',
            value: _p.toDouble(),
            min: 1,
            max: 6,
            divisions: 5,
            activeColor: Colors.blue,
            onChanged: (v) => setState(() {
              final prev = _p / _q;
              _p = v.round();
              _replay(prev);
            }),
          ),
          SimSlider(
            label: 'q: $_q',
            value: _q.toDouble(),
            min: 1,
            max: 6,
            divisions: 5,
            activeColor: Colors.teal,
            onChanged: (v) => setState(() {
              final prev = _p / _q;
              _q = v.round();
              _replay(prev);
            }),
          ),
        ],
      ),
    );
  }
}

class _SimilarTrianglePainter extends CustomPainter {
  final double scale;
  _SimilarTrianglePainter({required this.scale});

  @override
  void paint(Canvas canvas, Size size) {
    final base = Offset(size.width * 0.15, size.height * 0.85);
    const origW = 60.0, origH = 80.0;
    final orig = [
      base,
      base + const Offset(origW, 0),
      base + const Offset(origW * 0.3, -origH),
    ];
    final origPath = Path()..addPolygon(orig, true);
    canvas.drawPath(origPath, Paint()..color = Colors.blue.shade200);
    canvas.drawPath(origPath, Paint()..color = Colors.blue.shade800..style = PaintingStyle.stroke..strokeWidth = 2);

    final scaled = orig.map((p) => base + (p - base) * scale).toList();
    final scaledPath = Path()..addPolygon(scaled, true);
    canvas.drawPath(scaledPath, Paint()..color = Colors.deepOrange.withValues(alpha: 0.3));
    canvas.drawPath(scaledPath, Paint()..color = Colors.deepOrange.shade800..style = PaintingStyle.stroke..strokeWidth = 2);
  }

  @override
  bool shouldRepaint(covariant _SimilarTrianglePainter oldDelegate) => oldDelegate.scale != scale;
}
