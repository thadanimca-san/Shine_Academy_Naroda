import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';

import '../../../../core/services/trilingual_service.dart';
import '../../../../foundation/theme/app_colors.dart';
import '../../../../foundation/theme/app_typography.dart';
import 'package:shine_academy_naroda/features/common/widgets/math_title.dart';

/// Value of the polynomial with [coefficients] (highest power first) at [x].
double evaluatePolynomial(List<double> coefficients, double x) =>
    coefficients.fold(0.0, (value, c) => value * x + c);

/// One curve y = p(x) on the graph, with an optional LaTeX label.
class GraphCurve {
  final List<double> coefficients;
  final String? label;
  const GraphCurve(this.coefficients, this.label);
}

/// A marked point, e.g. the intersection of two lines.
class GraphPoint {
  final double x;
  final double y;
  final String label;
  const GraphPoint(this.x, this.y, this.label);
}

List<double> _numbers(Object? list) => (list as List? ?? const []).map((v) => (v as num).toDouble()).toList();

/// Reads the curves of a `function_graph` block: either one `polynomial`
/// (with `label`) or a list of `curves`, each `{"polynomial": [...], "label": "..."}`.
List<GraphCurve> graphCurves(Map<String, dynamic> data) {
  final curves = data['curves'];
  if (curves is List && curves.isNotEmpty) {
    return curves.cast<Map<String, dynamic>>().map((c) => GraphCurve(_numbers(c['polynomial']), c['label'] as String?)).toList();
  }
  final single = _numbers(data['polynomial']);
  return single.isEmpty ? const [] : [GraphCurve(single, data['label'] as String?)];
}

/// Block `function_graph`: draws one or more curves y = p(x), tracing them
/// from left to right, and marks zeroes and named points.
///
/// JSON (single curve):
///   {"polynomial": [1, -3, -4], "x_range": [-3, 6], "zeroes": [-1, 4], "label": "y = x^{2} - 3x - 4", "title": "..."}
/// JSON (several lines, e.g. a pair of linear equations):
///   {"curves": [{"polynomial": [-1, 10], "label": "x + y = 10"}, {"polynomial": [1, -4], "label": "x - y = 4"}],
///    "points": [{"x": 7, "y": 3, "label": "(7, 3)"}], "x_range": [-1, 11], "title": "..."}
class FunctionGraphWidget extends StatefulWidget {
  final Map<String, dynamic> data;
  const FunctionGraphWidget({super.key, required this.data});

  @override
  State<FunctionGraphWidget> createState() => _FunctionGraphWidgetState();
}

class _FunctionGraphWidgetState extends State<FunctionGraphWidget> with SingleTickerProviderStateMixin {
  static const _curveColors = [AppColors.primary, Color(0xFFE65100), Color(0xFF2E7D32), Color(0xFF6A1B9A)];

  late final AnimationController _controller =
      AnimationController(vsync: this, duration: const Duration(milliseconds: 1800));

  bool _hasStarted = false;

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    // Reduced motion (an accessibility setting, also used for PDF capture)
    // shows the finished picture straight away.
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
    final curves = graphCurves(widget.data);
    final xRange = _numbers(widget.data['x_range']);
    final zeroes = _numbers(widget.data['zeroes']);
    final zeroLabels = List<String>.from(widget.data['zero_labels'] ?? zeroes.map(_formatNumber));
    final points = (widget.data['points'] as List? ?? const [])
        .cast<Map<String, dynamic>>()
        .map((p) => GraphPoint((p['x'] as num).toDouble(), (p['y'] as num).toDouble(), p['label'] as String? ?? ''))
        .toList();
    final title = TrilingualService.instance.getLocalizedText(widget.data, 'title');
    final onSurface = Theme.of(context).colorScheme.onSurface;
    final textStyle = AppTypography.bodySmall(context, color: onSurface);

    if (curves.isEmpty) {
      return Text(TrilingualService.instance.getUIText('Graph data is missing.'), style: textStyle);
    }
    final colors = [for (var i = 0; i < curves.length; i++) _curveColors[i % _curveColors.length]];
    final labelled = [for (var i = 0; i < curves.length; i++) if ((curves[i].label ?? '').isNotEmpty) i];

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
                const Icon(Icons.show_chart, color: AppColors.primary),
                const SizedBox(width: 8),
                Expanded(
                  child: MathTitle(title.isEmpty ? TrilingualService.instance.getUIText('Graph') : title,
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
              aspectRatio: 4 / 3,
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) => CustomPaint(
                  painter: _GraphPainter(
                    curves: curves,
                    curveColors: colors,
                    xMin: xRange.length == 2 ? xRange[0] : -5,
                    xMax: xRange.length == 2 ? xRange[1] : 5,
                    zeroes: zeroes,
                    zeroLabels: zeroLabels,
                    points: points,
                    progress: Curves.easeInOut.transform(_controller.value),
                    textStyle: textStyle,
                    axisColor: onSurface.withValues(alpha: 0.7),
                    gridColor: onSurface.withValues(alpha: 0.08),
                    markColor: Colors.red.shade600,
                  ),
                ),
              ),
            ),
            if (labelled.isNotEmpty)
              Padding(
                padding: const EdgeInsets.only(top: 8),
                child: Wrap(
                  alignment: WrapAlignment.center,
                  spacing: 16,
                  runSpacing: 4,
                  children: [
                    for (final i in labelled)
                      Row(
                        mainAxisSize: MainAxisSize.min,
                        children: [
                          if (curves.length > 1) Container(width: 18, height: 4, color: colors[i]),
                          if (curves.length > 1) const SizedBox(width: 6),
                          Math.tex(curves[i].label!, textStyle: AppTypography.body(context, color: curves.length > 1 ? colors[i] : onSurface)),
                        ],
                      ),
                  ],
                ),
              ),
          ],
        ),
      ),
    );
  }

  static String _formatNumber(double value) =>
      value == value.roundToDouble() ? value.toInt().toString() : value.toStringAsFixed(2);
}

class _GraphPainter extends CustomPainter {
  final List<GraphCurve> curves;
  final List<Color> curveColors;
  final double xMin;
  final double xMax;
  final List<double> zeroes;
  final List<String> zeroLabels;
  final List<GraphPoint> points;
  final double progress;
  final TextStyle textStyle;
  final Color axisColor;
  final Color gridColor;
  final Color markColor;

  _GraphPainter({
    required this.curves,
    required this.curveColors,
    required this.xMin,
    required this.xMax,
    required this.zeroes,
    required this.zeroLabels,
    required this.points,
    required this.progress,
    required this.textStyle,
    required this.axisColor,
    required this.gridColor,
    required this.markColor,
  });

  static const _samples = 240;

  @override
  void paint(Canvas canvas, Size size) {
    final xs = List.generate(_samples + 1, (i) => xMin + (xMax - xMin) * i / _samples);
    final ysPerCurve = [for (final c in curves) xs.map((x) => evaluatePolynomial(c.coefficients, x)).toList()];

    // Keep the x-axis and every marked point in view, with headroom.
    final allYs = [...ysPerCurve.expand((ys) => ys), ...points.map((p) => p.y), 0.0];
    var yMin = allYs.reduce(math.min);
    var yMax = allYs.reduce(math.max);
    final padding = math.max((yMax - yMin) * 0.1, 1.0);
    yMin -= padding;
    yMax += padding;

    Offset toCanvas(double x, double y) => Offset(
          (x - xMin) / (xMax - xMin) * size.width,
          size.height - (y - yMin) / (yMax - yMin) * size.height,
        );

    canvas.save();
    canvas.clipRect(Offset.zero & size);

    final gridPaint = Paint()..color = gridColor;
    for (var x = xMin.ceil(); x <= xMax.floor(); x++) {
      canvas.drawLine(toCanvas(x.toDouble(), yMin), toCanvas(x.toDouble(), yMax), gridPaint);
    }

    final axisPaint = Paint()
      ..color = axisColor
      ..strokeWidth = 1.5;
    canvas.drawLine(toCanvas(xMin, 0), toCanvas(xMax, 0), axisPaint);
    if (xMin <= 0 && xMax >= 0) canvas.drawLine(toCanvas(0, yMin), toCanvas(0, yMax), axisPaint);
    _drawText(canvas, 'x', toCanvas(xMax, 0) + const Offset(-12, 4));
    if (xMin <= 0 && xMax >= 0) _drawText(canvas, 'y', toCanvas(0, yMax) + const Offset(6, 0));

    final visible = (progress * _samples).round();
    if (visible > 0) {
      for (var c = 0; c < curves.length; c++) {
        final ys = ysPerCurve[c];
        final path = Path()..moveTo(toCanvas(xs[0], ys[0]).dx, toCanvas(xs[0], ys[0]).dy);
        for (var i = 1; i <= visible; i++) {
          final point = toCanvas(xs[i], ys[i]);
          path.lineTo(point.dx, point.dy);
        }
        canvas.drawPath(
          path,
          Paint()
            ..color = curveColors[c]
            ..strokeWidth = 3
            ..style = PaintingStyle.stroke,
        );
      }
    }

    // Marks appear once the curves have been traced past them.
    bool reached(double x) => progress >= (x - xMin) / (xMax - xMin);
    for (var i = 0; i < zeroes.length; i++) {
      if (!reached(zeroes[i])) continue;
      final point = toCanvas(zeroes[i], 0);
      canvas.drawCircle(point, 6, Paint()..color = markColor);
      _drawText(canvas, i < zeroLabels.length ? zeroLabels[i] : '', point + const Offset(-8, 8), color: markColor);
    }
    for (final p in points) {
      if (!reached(p.x)) continue;
      final point = toCanvas(p.x, p.y);
      canvas.drawCircle(point, 6, Paint()..color = markColor);
      _drawText(canvas, p.label, point + const Offset(8, -22), color: markColor);
    }
    canvas.restore();
  }

  void _drawText(Canvas canvas, String text, Offset at, {Color? color}) {
    final painter = TextPainter(
      text: TextSpan(text: text, style: textStyle.copyWith(color: color ?? textStyle.color, fontWeight: FontWeight.bold)),
      textDirection: TextDirection.ltr,
    )..layout();
    painter.paint(canvas, at);
  }

  @override
  bool shouldRepaint(_GraphPainter old) => old.progress != progress || old.textStyle != textStyle;
}
