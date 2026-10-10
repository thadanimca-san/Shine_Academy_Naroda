import 'dart:math' as math;

import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';

import '../../../../core/services/trilingual_service.dart';
import '../../../../foundation/theme/app_colors.dart';
import '../../../../foundation/theme/app_typography.dart';
import 'package:shine_academy_naroda/features/common/widgets/math_title.dart';

/// Splits [number] into one level per step: at each level the current value
/// is divided by its smallest prime. 140 gives (2, 70), (2, 35), (5, 7).
List<(int prime, int rest)> factorTreeLevels(int number) {
  final levels = <(int, int)>[];
  var value = number;
  while (true) {
    final prime = _smallestPrimeFactor(value);
    if (prime == value) break;
    levels.add((prime, value ~/ prime));
    value ~/= prime;
  }
  return levels;
}

int _smallestPrimeFactor(int n) {
  for (var d = 2; d * d <= n; d++) {
    if (n % d == 0) return d;
  }
  return n;
}

/// "2^{2} \times 5 \times 7" for 140.
String primePowerTex(int number) {
  final counts = <int, int>{};
  var value = number;
  while (value > 1) {
    final p = _smallestPrimeFactor(value);
    counts[p] = (counts[p] ?? 0) + 1;
    value ~/= p;
  }
  return counts.entries.map((e) => e.value > 1 ? '${e.key}^{${e.value}}' : '${e.key}').join(r' \times ');
}

/// Block `factor_tree`: grows the factor tree of `number` one branch at a
/// time, then shows the prime factorisation. JSON: {"number": 140, "title": "..."}.
class FactorTreeWidget extends StatefulWidget {
  final Map<String, dynamic> data;
  const FactorTreeWidget({super.key, required this.data});

  @override
  State<FactorTreeWidget> createState() => _FactorTreeWidgetState();
}

class _FactorTreeWidgetState extends State<FactorTreeWidget> with SingleTickerProviderStateMixin {
  static const _stepDuration = Duration(milliseconds: 900);

  late final int _number = (widget.data['number'] as num?)?.toInt() ?? 0;
  late final List<(int, int)> _levels = _number > 3 ? factorTreeLevels(_number) : const [];
  late final AnimationController _controller = AnimationController(
    vsync: this,
    duration: _stepDuration * math.max(_levels.length, 1),
  );

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
    final title = TrilingualService.instance.getLocalizedText(widget.data, 'title');
    final labelStyle = AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface, fontWeight: FontWeight.bold);

    if (_levels.isEmpty) {
      return Card(
        child: Padding(
          padding: const EdgeInsets.all(16),
          child: Text(TrilingualService.instance.getUIText('Factor tree needs a composite number.'), style: labelStyle),
        ),
      );
    }

    final factorisation = '$_number = ${primePowerTex(_number)}';
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
                const Icon(Icons.account_tree, color: AppColors.primary),
                const SizedBox(width: 8),
                Expanded(child: MathTitle(title.isEmpty ? TrilingualService.instance.getUIText('Factor tree') : title, style: labelStyle)),
                IconButton(
                  tooltip: TrilingualService.instance.getUIText('Play again'),
                  icon: const Icon(Icons.replay),
                  onPressed: () => _controller.forward(from: 0),
                ),
              ],
            ),
            const SizedBox(height: 8),
            AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final revealed = _controller.value * _levels.length;
                return Semantics(
                  label: factorisation,
                  child: Center(
                    child: FittedBox(
                      fit: BoxFit.scaleDown,
                      child: CustomPaint(
                        size: _FactorTreePainter.sizeFor(_levels.length, labelStyle.fontSize ?? 16),
                        painter: _FactorTreePainter(
                          root: _number,
                          levels: _levels,
                          revealed: revealed,
                          labelStyle: labelStyle,
                          lineColor: Colors.grey.shade500,
                          primeColor: AppColors.accent,
                        ),
                      ),
                    ),
                  ),
                );
              },
            ),
            const SizedBox(height: 12),
            AnimatedBuilder(
              animation: _controller,
              builder: (context, child) => AnimatedOpacity(
                opacity: _controller.isCompleted ? 1 : 0,
                duration: const Duration(milliseconds: 400),
                child: child,
              ),
              child: Center(child: Math.tex(factorisation, textStyle: labelStyle)),
            ),
          ],
        ),
      ),
    );
  }
}

class _FactorTreePainter extends CustomPainter {
  final int root;
  final List<(int, int)> levels;
  final double revealed;
  final TextStyle labelStyle;
  final Color lineColor;
  final Color primeColor;

  _FactorTreePainter({
    required this.root,
    required this.levels,
    required this.revealed,
    required this.labelStyle,
    required this.lineColor,
    required this.primeColor,
  });

  static double _step(double fontSize) => fontSize * 3.2;
  static double _rowHeight(double fontSize) => fontSize * 4;

  /// The tree descends to the right: each composite sits one step right of the
  /// one above it, with its prime factor one step to the left.
  static Size sizeFor(int levelCount, double fontSize) =>
      Size(_step(fontSize) * (levelCount + 3), _rowHeight(fontSize) * (levelCount + 0.8));

  @override
  void paint(Canvas canvas, Size size) {
    final fontSize = labelStyle.fontSize ?? 16;
    final step = _step(fontSize);
    final rowHeight = _rowHeight(fontSize);
    Offset nodeAt(int row, int column) => Offset(step * (column + 2), rowHeight * row + fontSize);

    final linePaint = Paint()
      ..color = lineColor
      ..strokeWidth = 2;

    _drawLabel(canvas, '$root', nodeAt(0, 0), 1, isPrime: false);
    for (var i = 0; i < levels.length; i++) {
      final opacity = (revealed - i).clamp(0.0, 1.0);
      if (opacity == 0) break;
      final (prime, rest) = levels[i];
      final parent = nodeAt(i, i);
      final primeNode = nodeAt(i + 1, i - 1);
      final restNode = nodeAt(i + 1, i + 1);
      linePaint.color = lineColor.withValues(alpha: opacity);
      final gap = Offset(0, fontSize * 0.9);
      canvas.drawLine(parent + gap, primeNode - gap, linePaint);
      canvas.drawLine(parent + gap, restNode - gap, linePaint);
      _drawLabel(canvas, '$prime', primeNode, opacity, isPrime: true);
      final restIsPrime = i == levels.length - 1;
      _drawLabel(canvas, '$rest', restNode, opacity, isPrime: restIsPrime);
    }
  }

  void _drawLabel(Canvas canvas, String text, Offset center, double opacity, {required bool isPrime}) {
    final color = (isPrime ? primeColor : labelStyle.color ?? Colors.black).withValues(alpha: opacity);
    final painter = TextPainter(
      text: TextSpan(text: text, style: labelStyle.copyWith(color: color)),
      textDirection: TextDirection.ltr,
    )..layout();
    final topLeft = center - Offset(painter.width / 2, painter.height / 2);
    if (isPrime) {
      final radius = math.max(painter.width, painter.height) / 2 + 6;
      canvas.drawCircle(
        center,
        radius,
        Paint()
          ..color = color
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2,
      );
    }
    painter.paint(canvas, topLeft);
  }

  @override
  bool shouldRepaint(_FactorTreePainter old) => old.revealed != revealed || old.labelStyle != labelStyle;
}
