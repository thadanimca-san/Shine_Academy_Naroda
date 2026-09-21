import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// An area model for fraction multiplication: two fraction sliders shade
/// a grid horizontally and vertically, and the doubly-shaded overlap
/// visually is the product. Whenever a fraction changes, the shading
/// animates in — rows sweep down, then columns sweep across — so the
/// overlap forming the product is visibly built, not just redrawn.
class FractionsDecimalsSimulationWidget extends StatefulWidget {
  const FractionsDecimalsSimulationWidget({super.key});

  @override
  State<FractionsDecimalsSimulationWidget> createState() => _FractionsDecimalsSimulationWidgetState();
}

class _FractionsDecimalsSimulationWidgetState extends State<FractionsDecimalsSimulationWidget> with SingleTickerProviderStateMixin {
  int _num1 = 2, _den1 = 3;
  int _num2 = 3, _den2 = 4;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 800));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _replay() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final productNum = _num1 * _num2;
    final productDen = _den1 * _den2;

    return SimFrame(
      title: 'Multiplying Fractions (Area Model)',
      icon: Icons.grid_on,
      accent: Colors.teal.shade600,
      description: 'The overlapping shaded region shows the product of two fractions visually — watch it sweep in.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AspectRatio(
            aspectRatio: 1.6,
            child: Container(
              decoration: BoxDecoration(border: Border.all(color: Colors.grey.shade400), borderRadius: BorderRadius.circular(8)),
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) {
                  // First half sweeps the horizontal (row) shading in, second half the vertical (column) shading.
                  final t = _controller.value;
                  final rowT = Curves.easeOut.transform((t / 0.6).clamp(0.0, 1.0));
                  final colT = Curves.easeOut.transform(((t - 0.4) / 0.6).clamp(0.0, 1.0));
                  return CustomPaint(
                    size: Size.infinite,
                    painter: _GridPainter(num1: _num1, den1: _den1, num2: _num2, den2: _den2, rowT: rowT, colT: colT),
                  );
                },
              ),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Fraction 1', value: '$_num1/$_den1', color: Colors.blue),
            SimMetric(label: 'Fraction 2', value: '$_num2/$_den2', color: Colors.orange),
            SimMetric(label: 'Product', value: '$productNum/$productDen', color: Colors.teal),
          ]),
          const SizedBox(height: 14),
          Row(children: [
            Expanded(child: _stepper('Num 1', _num1, (v) => setState(() { _num1 = v; _replay(); }), 1, _den1)),
            const SizedBox(width: 8),
            Expanded(child: _stepper('Den 1', _den1, (v) => setState(() { _den1 = v; _replay(); }), _num1, 8)),
          ]),
          Row(children: [
            Expanded(child: _stepper('Num 2', _num2, (v) => setState(() { _num2 = v; _replay(); }), 1, _den2)),
            const SizedBox(width: 8),
            Expanded(child: _stepper('Den 2', _den2, (v) => setState(() { _den2 = v; _replay(); }), _num2, 8)),
          ]),
        ],
      ),
    );
  }

  Widget _stepper(String label, int value, ValueChanged<int> onChanged, int min, int max) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text('$label:', style: TextStyle(fontSize: 12)),
        IconButton(icon: Icon(Icons.remove_circle_outline, size: 20), onPressed: value > min ? () => onChanged(value - 1) : null),
        Text('$value', style: TextStyle(fontWeight: FontWeight.bold)),
        IconButton(icon: Icon(Icons.add_circle_outline, size: 20), onPressed: value < max ? () => onChanged(value + 1) : null),
      ],
    );
  }
}

class _GridPainter extends CustomPainter {
  final int num1, den1, num2, den2;
  final double rowT;
  final double colT;

  _GridPainter({required this.num1, required this.den1, required this.num2, required this.den2, this.rowT = 1, this.colT = 1});

  @override
  void paint(Canvas canvas, Size size) {
    final cellW = size.width / den2;
    final cellH = size.height / den1;
    // Rows sweep in top-to-bottom, columns sweep in left-to-right, based on how many
    // whole rows/columns the current animation progress has revealed.
    final rowsRevealed = (num1 * rowT).clamp(0.0, num1.toDouble());
    final colsRevealed = (num2 * colT).clamp(0.0, num2.toDouble());

    for (int r = 0; r < den1; r++) {
      for (int c = 0; c < den2; c++) {
        final rect = Rect.fromLTWH(c * cellW, r * cellH, cellW, cellH);
        canvas.drawRect(rect, Paint()..color = Colors.white..style = PaintingStyle.fill);
        final rowFrac = (rowsRevealed - r).clamp(0.0, 1.0);
        final colFrac = (colsRevealed - c).clamp(0.0, 1.0);
        final horizontalShaded = rowFrac > 0;
        final verticalShaded = colFrac > 0;
        Color? fill;
        if (horizontalShaded && verticalShaded) {
          fill = Colors.teal.withValues(alpha: 0.7 * (rowFrac * colFrac));
        } else if (horizontalShaded) {
          fill = Colors.blue.withValues(alpha: 0.35 * rowFrac);
        } else if (verticalShaded) {
          fill = Colors.orange.withValues(alpha: 0.35 * colFrac);
        }
        if (fill != null) canvas.drawRect(rect, Paint()..color = fill);
        canvas.drawRect(rect, Paint()..color = Colors.grey.shade300..style = PaintingStyle.stroke..strokeWidth = 1);
      }
    }
  }

  @override
  bool shouldRepaint(covariant _GridPainter oldDelegate) =>
      oldDelegate.num1 != num1 || oldDelegate.den1 != den1 || oldDelegate.num2 != num2 || oldDelegate.den2 != den2 || oldDelegate.rowT != rowT || oldDelegate.colT != colT;
}
