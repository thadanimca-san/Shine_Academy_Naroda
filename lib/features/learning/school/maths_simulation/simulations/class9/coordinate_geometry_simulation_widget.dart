import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A tappable Cartesian plane split into four coloured quadrants: tap to
/// plot a point that animates in from the origin, and see its coordinates
/// and which quadrant (with correct sign combination) it falls in.
class CoordinateGeometrySimulationWidget extends StatefulWidget {
  const CoordinateGeometrySimulationWidget({super.key});

  @override
  State<CoordinateGeometrySimulationWidget> createState() => _CoordinateGeometrySimulationWidgetState();
}

class _CoordinateGeometrySimulationWidgetState extends State<CoordinateGeometrySimulationWidget> with SingleTickerProviderStateMixin {
  Offset? _point;
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

  String get _quadrant {
    if (_point == null) return '-';
    final x = _point!.dx, y = _point!.dy;
    if (x == 0 && y == 0) return 'Origin';
    if (x > 0 && y > 0) return 'I (+, +)';
    if (x < 0 && y > 0) return 'II (−, +)';
    if (x < 0 && y < 0) return 'III (−, −)';
    if (x > 0 && y < 0) return 'IV (+, −)';
    return 'On an axis';
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'The Four Quadrants',
      icon: Icons.grid_on,
      accent: Colors.purple.shade600,
      description: 'Tap anywhere to plot a point and watch it travel out from the origin, based on the sign of its coordinates.',
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
                  final x = ((local.dx - size.width / 2) * (10 / size.width));
                  final y = -((local.dy - size.height / 2) * (10 / size.height));
                  setState(() => _point = Offset(x, y));
                  _controller.forward(from: 0);
                },
                child: Container(
                  decoration: BoxDecoration(borderRadius: BorderRadius.circular(10)),
                  child: AnimatedBuilder(
                    animation: _controller,
                    builder: (context, _) {
                      final eased = Curves.easeOutBack.transform(_controller.value);
                      final animatedPoint = _point == null ? null : Offset(_point!.dx * eased, _point!.dy * eased);
                      return CustomPaint(size: size, painter: _QuadrantPainter(point: animatedPoint));
                    },
                  ),
                ),
              );
            }),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Point', value: _point == null ? '-' : '(${_point!.dx.toStringAsFixed(1)}, ${_point!.dy.toStringAsFixed(1)})'),
            SimMetric(label: 'Quadrant', value: _quadrant, color: Colors.purple),
          ]),
        ],
      ),
    );
  }
}

class _QuadrantPainter extends CustomPainter {
  final Offset? point;
  _QuadrantPainter({required this.point});

  @override
  void paint(Canvas canvas, Size size) {
    final cx = size.width / 2, cy = size.height / 2;
    canvas.drawRect(Rect.fromLTWH(cx, 0, cx, cy), Paint()..color = Colors.blue.shade50);
    canvas.drawRect(Rect.fromLTWH(0, 0, cx, cy), Paint()..color = Colors.green.shade50);
    canvas.drawRect(Rect.fromLTWH(0, cy, cx, cy), Paint()..color = Colors.orange.shade50);
    canvas.drawRect(Rect.fromLTWH(cx, cy, cx, cy), Paint()..color = Colors.pink.shade50);

    final axisPaint = Paint()
      ..color = Colors.black54
      ..strokeWidth = 2;
    canvas.drawLine(Offset(0, cy), Offset(size.width, cy), axisPaint);
    canvas.drawLine(Offset(cx, 0), Offset(cx, size.height), axisPaint);

    _label(canvas, Offset(cx + cx / 2, cy / 2), 'I');
    _label(canvas, Offset(cx / 2, cy / 2), 'II');
    _label(canvas, Offset(cx / 2, cy + cy / 2), 'III');
    _label(canvas, Offset(cx + cx / 2, cy + cy / 2), 'IV');

    if (point != null) {
      final px = cx + point!.dx * (size.width / 10);
      final py = cy - point!.dy * (size.height / 10);
      canvas.drawLine(Offset(cx, cy), Offset(px, py), Paint()..color = Colors.deepPurple.withValues(alpha: 0.4)..strokeWidth = 1.5);
      canvas.drawCircle(Offset(px, py), 6, Paint()..color = Colors.deepPurple);
    }
  }

  void _label(Canvas canvas, Offset pos, String text) {
    final tp = TextPainter(text: TextSpan(text: text, style: TextStyle(color: Colors.black38, fontWeight: FontWeight.bold, fontSize: 20)), textDirection: TextDirection.ltr)..layout();
    tp.paint(canvas, pos - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(covariant _QuadrantPainter oldDelegate) => oldDelegate.point != point;
}
