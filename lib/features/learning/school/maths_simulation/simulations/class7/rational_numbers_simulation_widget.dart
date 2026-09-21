import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// Two rational numbers plotted on a shared number line so students can
/// see which is greater, directly, instead of cross-multiplying blind.
/// Each point glides smoothly to its new position whenever the fraction
/// changes, keeping the "greater = further right" intuition visible.
class RationalNumbersSimulationWidget extends StatefulWidget {
  const RationalNumbersSimulationWidget({super.key});

  @override
  State<RationalNumbersSimulationWidget> createState() => _RationalNumbersSimulationWidgetState();
}

class _RationalNumbersSimulationWidgetState extends State<RationalNumbersSimulationWidget> with SingleTickerProviderStateMixin {
  int _num1 = -3, _den1 = 4;
  int _num2 = 1, _den2 = 2;
  double _prevV1 = -0.75, _prevV2 = 0.5;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 450));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _update(VoidCallback change) {
    _prevV1 = _num1 / _den1;
    _prevV2 = _num2 / _den2;
    setState(change);
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    final v1 = _num1 / _den1;
    final v2 = _num2 / _den2;
    final comparison = v1 == v2 ? '=' : (v1 > v2 ? '>' : '<');

    return SimFrame(
      title: 'Comparing Rational Numbers',
      icon: Icons.compare_arrows,
      accent: Colors.indigo.shade600,
      description: 'Plot two rational numbers on the same number line to see directly which is greater — watch them glide into place.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 100,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.indigo.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeOutBack.transform(_controller.value);
                final animV1 = _prevV1 + (v1 - _prevV1) * eased;
                final animV2 = _prevV2 + (v2 - _prevV2) * eased;
                return CustomPaint(size: Size.infinite, painter: _NumberLinePainter(v1: animV1, v2: animV2));
              },
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Number 1', value: '$_num1/$_den1 (${v1.toStringAsFixed(2)})', color: Colors.blue),
            SimMetric(label: 'Number 2', value: '$_num2/$_den2 (${v2.toStringAsFixed(2)})', color: Colors.orange),
            SimMetric(label: 'Comparison', value: '$_num1/$_den1  $comparison  $_num2/$_den2', color: Colors.indigo),
          ]),
          const SizedBox(height: 14),
          Row(children: [
            Expanded(child: _stepper('Num 1', _num1, -8, 8, (v) => _update(() => _num1 = v))),
            const SizedBox(width: 8),
            Expanded(child: _stepper('Den 1', _den1, 1, 8, (v) => _update(() => _den1 = v))),
          ]),
          const SizedBox(height: 4),
          Row(children: [
            Expanded(child: _stepper('Num 2', _num2, -8, 8, (v) => _update(() => _num2 = v))),
            const SizedBox(width: 8),
            Expanded(child: _stepper('Den 2', _den2, 1, 8, (v) => _update(() => _den2 = v))),
          ]),
        ],
      ),
    );
  }

  Widget _stepper(String label, int value, int min, int max, ValueChanged<int> onChanged) {
    return Row(
      mainAxisSize: MainAxisSize.min,
      children: [
        Text('$label:', style: TextStyle(fontSize: 12)),
        IconButton(icon: Icon(Icons.remove_circle_outline, size: 20), onPressed: value > min ? () => onChanged(value - 1) : null),
        SizedBox(width: 22, child: Text('$value', textAlign: TextAlign.center, style: TextStyle(fontWeight: FontWeight.bold))),
        IconButton(icon: Icon(Icons.add_circle_outline, size: 20), onPressed: value < max ? () => onChanged(value + 1) : null),
      ],
    );
  }
}

class _NumberLinePainter extends CustomPainter {
  final double v1, v2;
  _NumberLinePainter({required this.v1, required this.v2});

  @override
  void paint(Canvas canvas, Size size) {
    const minVal = -2.0, maxVal = 2.0;
    final midY = size.height / 2;
    double xFor(double v) => ((v - minVal) / (maxVal - minVal)) * (size.width - 20) + 10;

    canvas.drawLine(Offset(10, midY), Offset(size.width - 10, midY), Paint()..color = Colors.grey.shade500..strokeWidth = 1.5);
    for (double i = minVal; i <= maxVal; i += 1) {
      final x = xFor(i);
      canvas.drawLine(Offset(x, midY - 4), Offset(x, midY + 4), Paint()..color = Colors.grey.shade500);
    }
    canvas.drawCircle(Offset(xFor(v1), midY), 7, Paint()..color = Colors.blue);
    canvas.drawCircle(Offset(xFor(v2), midY), 7, Paint()..color = Colors.orange);
  }

  @override
  bool shouldRepaint(covariant _NumberLinePainter oldDelegate) => true;
}
