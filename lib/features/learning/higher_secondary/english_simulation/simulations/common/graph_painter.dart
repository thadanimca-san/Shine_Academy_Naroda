import 'package:flutter/material.dart';

/// Simple axes + single-line plot painter used by several simulations
/// (distance-time, velocity-time, KE/PE bars via reuse elsewhere).
class LineGraphPainter extends CustomPainter {
  final List<Offset> points; // x: 0..1 (time fraction), y: 0..1 (value fraction)
  final Color lineColor;
  final String xLabel;
  final String yLabel;
  final double markerT; // 0..1, draws a dot at this progress along the line, -1 to hide

  LineGraphPainter({
    required this.points,
    required this.xLabel,
    required this.yLabel,
    this.lineColor = Colors.blue,
    this.markerT = -1,
  });

  @override
  void paint(Canvas canvas, Size size) {
    const leftPad = 8.0, bottomPad = 8.0, topPad = 8.0, rightPad = 8.0;
    final plotRect = Rect.fromLTWH(leftPad, topPad, size.width - leftPad - rightPad, size.height - topPad - bottomPad);

    final axisPaint = Paint()
      ..color = Colors.grey.shade400
      ..strokeWidth = 1.5;
    canvas.drawLine(plotRect.bottomLeft, plotRect.bottomRight, axisPaint);
    canvas.drawLine(plotRect.bottomLeft, plotRect.topLeft, axisPaint);

    if (points.length >= 2) {
      final path = Path();
      for (int i = 0; i < points.length; i++) {
        final p = points[i];
        final dx = plotRect.left + p.dx * plotRect.width;
        final dy = plotRect.bottom - p.dy * plotRect.height;
        if (i == 0) {
          path.moveTo(dx, dy);
        } else {
          path.lineTo(dx, dy);
        }
      }
      canvas.drawPath(
        path,
        Paint()
          ..color = lineColor
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2.5
          ..strokeJoin = StrokeJoin.round,
      );

      if (markerT >= 0 && markerT <= 1) {
        final idx = (markerT * (points.length - 1)).clamp(0, points.length - 1).toInt();
        final p = points[idx];
        final dx = plotRect.left + p.dx * plotRect.width;
        final dy = plotRect.bottom - p.dy * plotRect.height;
        canvas.drawCircle(Offset(dx, dy), 4.5, Paint()..color = lineColor);
        canvas.drawCircle(Offset(dx, dy), 4.5, Paint()..color = Colors.white..style = PaintingStyle.stroke..strokeWidth = 1.5);
      }
    }
  }

  @override
  bool shouldRepaint(covariant LineGraphPainter oldDelegate) =>
      oldDelegate.points != points || oldDelegate.markerT != markerT;
}

/// A titled mini-graph box combining axis labels with a [LineGraphPainter].
class MiniGraph extends StatelessWidget {
  final String title;
  final List<Offset> points;
  final Color color;
  final double markerT;

  const MiniGraph({
    super.key,
    required this.title,
    required this.points,
    this.color = Colors.blue,
    this.markerT = -1,
  });

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(title, style: TextStyle(fontSize: 11.5, fontWeight: FontWeight.w600, color: Theme.of(context).colorScheme.onSurfaceVariant)),
        const SizedBox(height: 4),
        Container(
          height: 110,
          padding: const EdgeInsets.all(6),
          decoration: BoxDecoration(
            color: Colors.white,
            border: Border.all(color: Colors.grey.shade300),
            borderRadius: BorderRadius.circular(8),
          ),
          child: CustomPaint(
            size: Size.infinite,
            painter: LineGraphPainter(points: points, xLabel: 'time', yLabel: title, lineColor: color, markerT: markerT),
          ),
        ),
      ],
    );
  }
}
