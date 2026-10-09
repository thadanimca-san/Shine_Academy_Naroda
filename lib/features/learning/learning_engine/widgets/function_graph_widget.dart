import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';

import '../../../../core/services/trilingual_service.dart';
import '../../../../foundation/theme/app_colors.dart';
import '../../../../foundation/theme/app_typography.dart';

/// Value of the polynomial with [coefficients] (highest power first) at [x].
double evaluatePolynomial(List<double> coefficients, double x) =>
    coefficients.fold(0.0, (value, c) => value * x + c);

/// Block `function_graph`: draws y = p(x) for a polynomial, tracing the curve
/// from left to right and marking its zeroes on the x-axis.
///
/// JSON:
/// {
///   "polynomial": [1, -3, -4],     coefficients, highest power first
///   "x_range": [-3, 6],            optional, default [-5, 5]
///   "zeroes": [-1, 4],             optional, marked with dots
///   "zero_labels": ["-1", "4"],    optional text for the marks
///   "label": "y = x^{2} - 3x - 4", optional LaTeX caption
///   "title": "..."
/// }
class FunctionGraphWidget extends StatefulWidget {
  final Map<String, dynamic> data;
  const FunctionGraphWidget({super.key, required this.data});

  @override
  State<FunctionGraphWidget> createState() => _FunctionGraphWidgetState();
}

class _FunctionGraphWidgetState extends State<FunctionGraphWidget> with SingleTickerProviderStateMixin {
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

  List<double> _numbers(String key) => (widget.data[key] as List? ?? const []).map((v) => (v as num).toDouble()).toList();

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final coefficients = _numbers('polynomial');
    final xRange = _numbers('x_range');
    final zeroes = _numbers('zeroes');
    final zeroLabels = List<String>.from(widget.data['zero_labels'] ?? zeroes.map(_formatNumber));
    final title = TrilingualService.instance.getLocalizedText(widget.data, 'title');
    final label = widget.data['label'] as String?;
    final onSurface = Theme.of(context).colorScheme.onSurface;
    final textStyle = AppTypography.bodySmall(context, color: onSurface);

    if (coefficients.isEmpty) {
      return Text(TrilingualService.instance.getUIText('Graph data is missing.'), style: textStyle);
    }

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
                  child: Text(title.isEmpty ? TrilingualService.instance.getUIText('Graph') : title,
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
                    coefficients: coefficients,
                    xMin: xRange.length == 2 ? xRange[0] : -5,
                    xMax: xRange.length == 2 ? xRange[1] : 5,
                    zeroes: zeroes,
                    zeroLabels: zeroLabels,
                    progress: Curves.easeInOut.transform(_controller.value),
                    textStyle: textStyle,
                    axisColor: onSurface.withValues(alpha: 0.7),
                    gridColor: onSurface.withValues(alpha: 0.08),
                    curveColor: AppColors.primary,
                    zeroColor: Colors.red.shade600,
                  ),
                ),
              ),
            ),
            if (label != null && label.isNotEmpty)
              Padding(
                padding: const EdgeInsets.only(top: 8),
                child: Center(child: Math.tex(label, textStyle: AppTypography.body(context, color: onSurface))),
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
  final List<double> coefficients;
  final double xMin;
  final double xMax;
  final List<double> zeroes;
  final List<String> zeroLabels;
  final double progress;
  final TextStyle textStyle;
  final Color axisColor;
  final Color gridColor;
  final Color curveColor;
  final Color zeroColor;

  _GraphPainter({
    required this.coefficients,
    required this.xMin,
    required this.xMax,
    required this.zeroes,
    required this.zeroLabels,
    required this.progress,
    required this.textStyle,
    required this.axisColor,
    required this.gridColor,
    required this.curveColor,
    required this.zeroColor,
  });

  static const _samples = 240;

  @override
  void paint(Canvas canvas, Size size) {
    final xs = List.generate(_samples + 1, (i) => xMin + (xMax - xMin) * i / _samples);
    final ys = xs.map((x) => evaluatePolynomial(coefficients, x)).toList();

    // Keep the x-axis in view and leave headroom above and below the curve.
    var yMin = math.min(ys.reduce(math.min), 0.0);
    var yMax = math.max(ys.reduce(math.max), 0.0);
    final padding = math.max((yMax - yMin) * 0.1, 1.0);
    yMin -= padding;
    yMax += padding;

    Offset toCanvas(double x, double y) => Offset(
          (x - xMin) / (xMax - xMin) * size.width,
          size.height - (y - yMin) / (yMax - yMin) * size.height,
        );

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
      final path = Path()..moveTo(toCanvas(xs[0], ys[0]).dx, toCanvas(xs[0], ys[0]).dy);
      for (var i = 1; i <= visible; i++) {
        final point = toCanvas(xs[i], ys[i]);
        path.lineTo(point.dx, point.dy);
      }
      canvas.drawPath(
        path,
        Paint()
          ..color = curveColor
          ..strokeWidth = 3
          ..style = PaintingStyle.stroke,
      );
    }

    // Each zero appears once the curve has been traced past it.
    for (var i = 0; i < zeroes.length; i++) {
      final reachedAt = (zeroes[i] - xMin) / (xMax - xMin);
      if (progress < reachedAt) continue;
      final point = toCanvas(zeroes[i], 0);
      canvas.drawCircle(point, 6, Paint()..color = zeroColor);
      _drawText(canvas, i < zeroLabels.length ? zeroLabels[i] : '', point + const Offset(-8, 8), color: zeroColor);
    }
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
