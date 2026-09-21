import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A balance scale for 2x + b = c: slide x and watch the beam smoothly
/// tilt to its new angle, generalising the balance metaphor to equations
/// with a coefficient.
class LinearEquationsSimulationWidget extends StatefulWidget {
  const LinearEquationsSimulationWidget({super.key});

  @override
  State<LinearEquationsSimulationWidget> createState() => _LinearEquationsSimulationWidgetState();
}

class _LinearEquationsSimulationWidgetState extends State<LinearEquationsSimulationWidget> with SingleTickerProviderStateMixin {
  double _x = 2;
  final double _coeff = 3;
  final double _b = 4;
  final double _c = 19;
  late AnimationController _controller;
  double _prevTilt = 0;
  double _targetTilt = 0;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 400));
    _targetTilt = _computeTilt();
    _prevTilt = _targetTilt;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  double _computeTilt() {
    final lhs = _coeff * _x + _b;
    return (lhs - _c).clamp(-10.0, 10.0);
  }

  void _updateX(double v) {
    setState(() {
      _x = v;
      _prevTilt = _lerpedTilt(_controller.value);
      _targetTilt = _computeTilt();
      _controller.forward(from: 0);
    });
  }

  double _lerpedTilt(double t) => _prevTilt + (_targetTilt - _prevTilt) * Curves.easeInOut.transform(t);

  @override
  Widget build(BuildContext context) {
    final lhs = _coeff * _x + _b;
    final diff = lhs - _c;
    final balanced = diff.abs() < 0.01;

    return SimFrame(
      title: 'Solving ${_coeff.toStringAsFixed(0)}x + ${_b.toStringAsFixed(0)} = ${_c.toStringAsFixed(0)}',
      icon: Icons.balance,
      accent: Colors.brown.shade600,
      description: 'Slide x and watch the scale tilt smoothly toward balance — the value where it settles flat is the solution.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 160,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.brown.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                return CustomPaint(size: Size.infinite, painter: _BalancePainter(tilt: _lerpedTilt(_controller.value)));
              },
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'x', value: _x.toStringAsFixed(1)),
            SimMetric(label: 'LHS', value: lhs.toStringAsFixed(1), color: Colors.blue),
            SimMetric(label: 'Balanced?', value: balanced ? 'Yes! ✓' : 'Not yet', color: balanced ? Colors.green : Colors.red),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'x: ${_x.toStringAsFixed(1)}', value: _x, min: 0, max: 10, divisions: 40, activeColor: balanced ? Colors.green : Colors.brown, onChanged: _updateX),
        ],
      ),
    );
  }
}

class _BalancePainter extends CustomPainter {
  final double tilt;
  _BalancePainter({required this.tilt});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, 40);
    final angle = (tilt / 10) * 0.25;
    canvas.drawLine(center, Offset(center.dx, size.height - 20), Paint()..color = Colors.brown.shade700..strokeWidth = 4);
    canvas.drawCircle(center, 6, Paint()..color = Colors.brown.shade800);
    canvas.save();
    canvas.translate(center.dx, center.dy);
    canvas.rotate(angle);
    final armLength = size.width * 0.35;
    canvas.drawLine(Offset(-armLength, 0), Offset(armLength, 0), Paint()..color = Colors.brown.shade600..strokeWidth = 3);
    final leftPan = Offset(-armLength, 30);
    final rightPan = Offset(armLength, 30);
    canvas.drawLine(Offset(-armLength, 0), leftPan, Paint()..color = Colors.grey.shade600..strokeWidth = 1.5);
    canvas.drawLine(Offset(armLength, 0), rightPan, Paint()..color = Colors.grey.shade600..strokeWidth = 1.5);
    canvas.drawOval(Rect.fromCenter(center: leftPan, width: 70, height: 16), Paint()..color = Colors.blue.shade200);
    canvas.drawOval(Rect.fromCenter(center: rightPan, width: 70, height: 16), Paint()..color = Colors.orange.shade200);
    canvas.restore();
  }

  @override
  bool shouldRepaint(covariant _BalancePainter oldDelegate) => oldDelegate.tilt != tilt;
}
