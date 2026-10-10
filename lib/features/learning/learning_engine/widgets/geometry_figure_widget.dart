import 'dart:math' as math;

import 'package:flutter/material.dart';

import '../../../../core/services/trilingual_service.dart';
import '../../../../foundation/theme/app_colors.dart';
import '../../../../foundation/theme/app_typography.dart';
import 'package:shine_academy_naroda/features/common/widgets/math_title.dart';

/// Named points of a `geometry_figure` block, in maths coordinates (y up).
Map<String, Offset> geometryPoints(Map<String, dynamic> data) {
  final raw = data['points'] as Map? ?? const {};
  return {
    for (final entry in raw.entries)
      entry.key as String: Offset(((entry.value as List)[0] as num).toDouble(), ((entry.value as List)[1] as num).toDouble()),
  };
}

/// A line segment between two named points; [highlight] draws it in the accent colour.
class GeometrySegment {
  final String from;
  final String to;
  final bool highlight;
  final bool dashed;
  const GeometrySegment(this.from, this.to, {this.highlight = false, this.dashed = false});
}

/// Segments are written as `["A", "B"]` or `{"from": "A", "to": "B", "highlight": true, "dashed": false}`.
List<GeometrySegment> geometrySegments(Map<String, dynamic> data) => [
      for (final s in data['segments'] as List? ?? const [])
        if (s is List)
          GeometrySegment(s[0] as String, s[1] as String)
        else if (s is Map)
          GeometrySegment(s['from'] as String, s['to'] as String,
              highlight: s['highlight'] == true, dashed: s['dashed'] == true),
    ];

/// True when segment PQ is parallel to segment RS (within a small tolerance).
bool segmentsParallel(Offset p, Offset q, Offset r, Offset s) {
  final a = q - p, b = s - r;
  final cross = a.dx * b.dy - a.dy * b.dx;
  return cross.abs() <= 1e-6 * a.distance * b.distance;
}

/// True when the angle at [vertex] between rays to [a] and [b] is 90°.
bool isRightAngle(Offset a, Offset vertex, Offset b) {
  final u = a - vertex, v = b - vertex;
  final dot = u.dx * v.dx + u.dy * v.dy;
  return dot.abs() <= 1e-6 * u.distance * v.distance;
}

/// A circle with a named centre, a radius and the named points that lie on it.
class GeometryCircle {
  final String centre;
  final double radius;
  final List<String> through;
  const GeometryCircle(this.centre, this.radius, this.through);
}

/// Circles are written as `{"centre": "O", "radius": 5, "through": ["A", "B"]}`.
List<GeometryCircle> geometryCircles(Map<String, dynamic> data) => [
      for (final c in (data['circles'] as List? ?? const []).cast<Map>())
        GeometryCircle(c['centre'] as String, (c['radius'] as num).toDouble(), _names(c['through'])),
    ];

/// The region of the plane the figure shows. With `"axes": true` it also
/// includes the origin and one unit of space around the points.
Rect geometryBounds(Map<String, dynamic> data, Map<String, Offset> points) {
  final xs = [...points.values.map((p) => p.dx)], ys = [...points.values.map((p) => p.dy)];
  if (data['axes'] == true) {
    xs.add(0);
    ys.add(0);
  }
  for (final c in geometryCircles(data)) {
    final centre = points[c.centre];
    if (centre == null) continue;
    xs.addAll([centre.dx - c.radius, centre.dx + c.radius]);
    ys.addAll([centre.dy - c.radius, centre.dy + c.radius]);
  }
  final pad = data['axes'] == true ? 1.0 : 0.0;
  return Rect.fromLTRB(xs.reduce(math.min) - pad, ys.reduce(math.min) - pad, xs.reduce(math.max) + pad, ys.reduce(math.max) + pad);
}

List<String> _names(Object? list) => (list as List? ?? const []).cast<String>();

/// Block `geometry_figure`: a labelled diagram of points and segments, drawn
/// segment by segment, with optional marks.
///
/// JSON:
///   {"title": "...",
///    "points": {"A": [0, 4], "B": [-3, 0], "C": [4, 0], "D": [-1.5, 2], "E": [2, 2]},
///    "segments": [["A", "B"], ["B", "C"], ["C", "A"], {"from": "D", "to": "E", "highlight": true}],
///    "parallel": [["D", "E", "B", "C"]],          // arrow marks: DE ∥ BC
///    "right_angles": [["A", "D", "B"]],           // square mark at the middle point
///    "angles": [{"points": ["B", "A", "C"], "label": "x"}],   // arc at the middle point
///    "lengths": [{"from": "A", "to": "D", "label": "1.5 cm"}]}   // optional "label_hi" / "label_gu"
/// For coordinate geometry add `"axes": true` (x- and y-axes with a grid) and
/// `"labels": {"A": "A(2, 3)"}` to show coordinates beside the points.
/// Circles: `"circles": [{"centre": "O", "radius": 5, "through": ["A", "B"]}]`.
class GeometryFigureWidget extends StatefulWidget {
  final Map<String, dynamic> data;
  const GeometryFigureWidget({super.key, required this.data});

  @override
  State<GeometryFigureWidget> createState() => _GeometryFigureWidgetState();
}

class _GeometryFigureWidgetState extends State<GeometryFigureWidget> with SingleTickerProviderStateMixin {
  late final AnimationController _controller =
      AnimationController(vsync: this, duration: const Duration(milliseconds: 2200));
  bool _hasStarted = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    // Reduced motion (an accessibility setting, also used for PDF capture)
    // shows the finished figure straight away.
    if (MediaQuery.of(context).disableAnimations) {
      _controller.value = 1;
    } else if (!_hasStarted) {
      _hasStarted = true;
      _controller.forward();
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final points = geometryPoints(widget.data);
    final title = TrilingualService.instance.getLocalizedText(widget.data, 'title');
    final onSurface = Theme.of(context).colorScheme.onSurface;
    final textStyle = AppTypography.bodySmall(context, color: onSurface);

    if (points.isEmpty) {
      return Text(TrilingualService.instance.getUIText('Figure data is missing.'), style: textStyle);
    }
    final bounds = geometryBounds(widget.data, points);
    final aspect = bounds.height <= 0 ? 2.0 : (bounds.width / bounds.height).clamp(0.8, 2.0);

    return Card(
      margin: const EdgeInsets.symmetric(vertical: 8),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Padding(
        padding: const EdgeInsets.all(16),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Row(
              children: [
                const Icon(Icons.change_history, color: AppColors.primary),
                const SizedBox(width: 8),
                Expanded(
                  child: MathTitle(title.isEmpty ? TrilingualService.instance.getUIText('Figure') : title,
                      style: AppTypography.body(context, color: onSurface, fontWeight: FontWeight.bold)),
                ),
                IconButton(
                  tooltip: TrilingualService.instance.getUIText('Play again'),
                  icon: const Icon(Icons.replay),
                  onPressed: () => _controller.forward(from: 0),
                ),
              ],
            ),
            AspectRatio(
              aspectRatio: aspect.toDouble(),
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) => CustomPaint(
                  painter: _FigurePainter(
                    data: widget.data,
                    points: points,
                    segments: geometrySegments(widget.data),
                    progress: _controller.value,
                    textStyle: textStyle,
                    lineColor: AppColors.primary,
                    highlightColor: const Color(0xFFE65100),
                    markColor: onSurface.withValues(alpha: 0.75),
                  ),
                ),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class _FigurePainter extends CustomPainter {
  final Map<String, dynamic> data;
  final Map<String, Offset> points;
  final List<GeometrySegment> segments;
  final double progress;
  final TextStyle textStyle;
  final Color lineColor;
  final Color highlightColor;
  final Color markColor;

  _FigurePainter({
    required this.data,
    required this.points,
    required this.segments,
    required this.progress,
    required this.textStyle,
    required this.lineColor,
    required this.highlightColor,
    required this.markColor,
  });

  /// Segments are traced during this share of the animation; marks follow.
  static const _drawShare = 0.8;
  static const _margin = 28.0;

  @override
  void paint(Canvas canvas, Size size) {
    final bounds = geometryBounds(data, points);
    final minX = bounds.left, maxX = bounds.right, minY = bounds.top, maxY = bounds.bottom;
    final spanX = math.max(maxX - minX, 1e-9), spanY = math.max(maxY - minY, 1e-9);
    final scale = math.min((size.width - 2 * _margin) / spanX, (size.height - 2 * _margin) / spanY);
    final offsetX = (size.width - spanX * scale) / 2, offsetY = (size.height - spanY * scale) / 2;
    Offset toCanvas(Offset p) => Offset(offsetX + (p.dx - minX) * scale, size.height - offsetY - (p.dy - minY) * scale);
    final canvasPoints = {for (final e in points.entries) e.key: toCanvas(e.value)};
    final centre = canvasPoints.values.reduce((a, b) => a + b) / canvasPoints.length.toDouble();
    if (data['axes'] == true) _drawAxes(canvas, toCanvas, minX, maxX, minY, maxY);

    // Circles first, traced during the first part of the animation.
    for (final c in geometryCircles(data)) {
      final centre = canvasPoints[c.centre];
      if (centre == null) continue;
      final sweep = (progress / (_drawShare / 2)).clamp(0.0, 1.0) * 2 * math.pi;
      if (sweep <= 0) continue;
      canvas.drawArc(Rect.fromCircle(center: centre, radius: c.radius * scale), 0, -sweep, false,
          Paint()
            ..color = lineColor
            ..strokeWidth = 2.5
            ..style = PaintingStyle.stroke);
    }

    // Segments, one after another.
    final shown = <String>{};
    for (var i = 0; i < segments.length; i++) {
      final segment = segments[i];
      final start = canvasPoints[segment.from], end = canvasPoints[segment.to];
      if (start == null || end == null) continue;
      final t = ((progress / _drawShare) * segments.length - i).clamp(0.0, 1.0);
      if (t <= 0) continue;
      shown..add(segment.from)..add(segment.to);
      final paint = Paint()
        ..color = segment.highlight ? highlightColor : lineColor
        ..strokeWidth = segment.highlight ? 3.5 : 2.5
        ..strokeCap = StrokeCap.round;
      final tip = Offset.lerp(start, end, t)!;
      if (segment.dashed) {
        _drawDashed(canvas, start, tip, paint);
      } else {
        canvas.drawLine(start, tip, paint);
      }
    }
    if (segments.isEmpty || progress >= _drawShare) shown.addAll(points.keys);

    // Point labels, pushed away from the middle of the figure.
    for (final name in shown) {
      final p = canvasPoints[name]!;
      canvas.drawCircle(p, 3, Paint()..color = lineColor);
      final away = p - centre;
      final direction = away.distance < 1e-6 ? const Offset(0, -1) : away / away.distance;
      final label = (data['labels'] as Map?)?[name] as String? ?? name;
      _drawText(canvas, label, p + direction * (label.length > 2 ? 26 : 16), bold: true);
    }

    if (progress < _drawShare) return;
    final marks = Paint()
      ..color = markColor
      ..strokeWidth = 1.8
      ..style = PaintingStyle.stroke;

    // Parallel marks: one chevron for the first group, two for the second, ...
    final parallel = data['parallel'] as List? ?? const [];
    for (var g = 0; g < parallel.length; g++) {
      final names = _names(parallel[g]);
      for (var k = 0; k + 1 < names.length; k += 2) {
        final a = canvasPoints[names[k]], b = canvasPoints[names[k + 1]];
        if (a != null && b != null) _drawChevrons(canvas, a, b, g + 1, marks);
      }
    }

    for (final r in data['right_angles'] as List? ?? const []) {
      final names = _names(r);
      final a = canvasPoints[names[0]], v = canvasPoints[names[1]], b = canvasPoints[names[2]];
      if (a == null || v == null || b == null) continue;
      final u = (a - v) / (a - v).distance * 10, w = (b - v) / (b - v).distance * 10;
      canvas.drawPath(Path()..moveTo((v + u).dx, (v + u).dy)..lineTo((v + u + w).dx, (v + u + w).dy)..lineTo((v + w).dx, (v + w).dy), marks);
    }

    for (final angle in (data['angles'] as List? ?? const []).cast<Map>()) {
      final names = _names(angle['points']);
      final a = canvasPoints[names[0]], v = canvasPoints[names[1]], b = canvasPoints[names[2]];
      if (a == null || v == null || b == null) continue;
      var start = math.atan2((a - v).dy, (a - v).dx);
      var sweep = math.atan2((b - v).dy, (b - v).dx) - start;
      while (sweep > math.pi) {
        sweep -= 2 * math.pi;
      }
      while (sweep < -math.pi) {
        sweep += 2 * math.pi;
      }
      canvas.drawArc(Rect.fromCircle(center: v, radius: 18), start, sweep, false, marks);
      final label = angle['label'] as String? ?? '';
      if (label.isNotEmpty) {
        final mid = start + sweep / 2;
        _drawText(canvas, label, v + Offset(math.cos(mid), math.sin(mid)) * 32);
      }
    }

    for (final length in (data['lengths'] as List? ?? const []).cast<Map>()) {
      final a = canvasPoints[length['from']], b = canvasPoints[length['to']];
      if (a == null || b == null) continue;
      final mid = (a + b) / 2;
      final along = (b - a) / (b - a).distance;
      var normal = Offset(-along.dy, along.dx);
      if ((mid + normal - centre).distance < (mid - centre).distance) normal = -normal;
      _drawText(canvas, TrilingualService.instance.getLocalizedText(Map<String, dynamic>.from(length), 'label'), mid + normal * 14);
    }
  }

  void _drawAxes(Canvas canvas, Offset Function(Offset) toCanvas, double minX, double maxX, double minY, double maxY) {
    final span = math.max(maxX - minX, maxY - minY);
    final step = span <= 24 ? 1 : (span / 12).ceil();
    final grid = Paint()..color = markColor.withValues(alpha: 0.12);
    for (var x = (minX / step).ceil() * step; x <= maxX; x += step) {
      canvas.drawLine(toCanvas(Offset(x.toDouble(), minY)), toCanvas(Offset(x.toDouble(), maxY)), grid);
    }
    for (var y = (minY / step).ceil() * step; y <= maxY; y += step) {
      canvas.drawLine(toCanvas(Offset(minX, y.toDouble())), toCanvas(Offset(maxX, y.toDouble())), grid);
    }
    final axis = Paint()
      ..color = markColor
      ..strokeWidth = 1.5;
    canvas.drawLine(toCanvas(Offset(minX, 0)), toCanvas(Offset(maxX, 0)), axis);
    canvas.drawLine(toCanvas(Offset(0, minY)), toCanvas(Offset(0, maxY)), axis);
    _drawText(canvas, 'x', toCanvas(Offset(maxX, 0)) + const Offset(-8, 12));
    _drawText(canvas, 'y', toCanvas(Offset(0, maxY)) + const Offset(12, 8));
    _drawText(canvas, 'O', toCanvas(Offset.zero) + const Offset(-10, 10));
  }

  void _drawDashed(Canvas canvas, Offset from, Offset to, Paint paint) {
    final length = (to - from).distance;
    if (length == 0) return;
    final step = (to - from) / length;
    for (var d = 0.0; d < length; d += 10) {
      canvas.drawLine(from + step * d, from + step * math.min(d + 5, length), paint);
    }
  }

  void _drawChevrons(Canvas canvas, Offset a, Offset b, int count, Paint paint) {
    final along = (b - a) / (b - a).distance;
    final normal = Offset(-along.dy, along.dx);
    final mid = (a + b) / 2;
    for (var i = 0; i < count; i++) {
      final tip = mid + along * (i * 6.0 - (count - 1) * 3.0 + 4);
      final back = tip - along * 7;
      canvas.drawPath(
          Path()
            ..moveTo((back + normal * 5).dx, (back + normal * 5).dy)
            ..lineTo(tip.dx, tip.dy)
            ..lineTo((back - normal * 5).dx, (back - normal * 5).dy),
          paint);
    }
  }

  void _drawText(Canvas canvas, String text, Offset centre, {bool bold = false}) {
    final painter = TextPainter(
      text: TextSpan(text: text, style: textStyle.copyWith(fontWeight: bold ? FontWeight.bold : FontWeight.w500)),
      textDirection: TextDirection.ltr,
    )..layout();
    painter.paint(canvas, centre - Offset(painter.width / 2, painter.height / 2));
  }

  @override
  bool shouldRepaint(_FigurePainter old) => old.progress != progress || old.textStyle != textStyle || old.data != data;
}
