import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A tappable Cartesian plane: tap anywhere to plot a point that animates
/// in from the origin, and read off its (x, y) coordinates.
class IntroductionGraphsSimulationWidget extends StatefulWidget {
  const IntroductionGraphsSimulationWidget({super.key});

  @override
  State<IntroductionGraphsSimulationWidget> createState() => _IntroductionGraphsSimulationWidgetState();
}

class _IntroductionGraphsSimulationWidgetState extends State<IntroductionGraphsSimulationWidget> with SingleTickerProviderStateMixin {
  Offset? _point; // in plane units, e.g. (-5..5)
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

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'The Cartesian Plane',
      icon: Icons.grid_on,
      accent: Colors.indigo.shade600,
      description: 'Tap anywhere on the grid to plot a point and watch it travel out from the origin.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AspectRatio(
            aspectRatio: 1.3,
            child: LayoutBuilder(builder: (context, constraints) {
              final size = Size(constraints.maxWidth, constraints.maxHeight);
              return GestureDetector(
                onTapUp: (details) {
                  final local = details.localPosition;
                  final unitsPerPxX = 10 / size.width;
                  final unitsPerPxY = 10 / size.height;
                  final x = ((local.dx - size.width / 2) * unitsPerPxX);
                  final y = -((local.dy - size.height / 2) * unitsPerPxY);
                  setState(() => _point = Offset(x, y));
                  _controller.forward(from: 0);
                },
                child: Container(
                  decoration: BoxDecoration(color: Colors.indigo.shade50, borderRadius: BorderRadius.circular(10)),
                  child: AnimatedBuilder(
                    animation: _controller,
                    builder: (context, _) {
                      final eased = Curves.easeOutBack.transform(_controller.value);
                      final animatedPoint = _point == null ? null : Offset(_point!.dx * eased, _point!.dy * eased);
                      return CustomPaint(size: size, painter: _GridPainter(point: animatedPoint));
                    },
                  ),
                ),
              );
            }),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'x-coordinate', value: _point == null ? '-' : _point!.dx.toStringAsFixed(1), color: Colors.blue),
            SimMetric(label: 'y-coordinate', value: _point == null ? '-' : _point!.dy.toStringAsFixed(1), color: Colors.deepOrange),
          ]),
        ],
      ),
    );
  }
}

class _GridPainter extends CustomPainter {
  final Offset? point;
  _GridPainter({required this.point});

  @override
  void paint(Canvas canvas, Size size) {
    final cx = size.width / 2, cy = size.height / 2;
    final gridPaint = Paint()
      ..color = Colors.indigo.shade100
      ..strokeWidth = 1;
    for (int i = -5; i <= 5; i++) {
      final x = cx + i * (size.width / 10);
      final y = cy + i * (size.height / 10);
      canvas.drawLine(Offset(x, 0), Offset(x, size.height), gridPaint);
      canvas.drawLine(Offset(0, y), Offset(size.width, y), gridPaint);
    }
    final axisPaint = Paint()
      ..color = Colors.indigo.shade700
      ..strokeWidth = 2;
    canvas.drawLine(Offset(0, cy), Offset(size.width, cy), axisPaint);
    canvas.drawLine(Offset(cx, 0), Offset(cx, size.height), axisPaint);

    if (point != null) {
      final px = cx + point!.dx * (size.width / 10);
      final py = cy - point!.dy * (size.height / 10);
      canvas.drawCircle(Offset(px, py), 6, Paint()..color = Colors.deepOrange);
    }
  }

  @override
  bool shouldRepaint(covariant _GridPainter oldDelegate) => true;
}
