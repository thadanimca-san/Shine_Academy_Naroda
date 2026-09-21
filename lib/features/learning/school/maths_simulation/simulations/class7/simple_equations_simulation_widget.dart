import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A balance-scale metaphor for solving x + b = c: slide x until both
/// pans balance, tying "keep both sides equal" to something physical.
/// The beam animates smoothly to its new tilt on every slide, and gives
/// a little settling bounce the moment it reaches perfect balance.
class SimpleEquationsSimulationWidget extends StatefulWidget {
  const SimpleEquationsSimulationWidget({super.key});

  @override
  State<SimpleEquationsSimulationWidget> createState() => _SimpleEquationsSimulationWidgetState();
}

class _SimpleEquationsSimulationWidgetState extends State<SimpleEquationsSimulationWidget> with SingleTickerProviderStateMixin {
  double _x = 3;
  final double _b = 4;
  final double _c = 12;
  double _prevTilt = -5;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 400));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final lhs = _x + _b;
    final diff = lhs - _c;
    final balanced = diff.abs() < 0.01;
    final targetTilt = diff.clamp(-8.0, 8.0);

    return SimFrame(
      title: 'Balancing an Equation',
      icon: Icons.balance,
      accent: Colors.brown.shade600,
      description: 'Solve x + $_b = $_c by sliding x until the scale balances — that\'s the value of x.',
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
                final eased = (balanced ? Curves.easeOutBack : Curves.easeInOut).transform(_controller.value);
                final animTilt = _prevTilt + (targetTilt - _prevTilt) * eased;
                return CustomPaint(
                  size: Size.infinite,
                  painter: _BalancePainter(tilt: animTilt),
                );
              },
            ),
          ),
          const SizedBox(height: 4),
          Center(
            child: Text(
              'x + $_b  vs  $_c',
              style: TextStyle(fontWeight: FontWeight.w600),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'x', value: _x.toStringAsFixed(0)),
            SimMetric(label: 'LHS (x + $_b)', value: lhs.toStringAsFixed(0), color: Colors.blue),
            SimMetric(label: 'Balanced?', value: balanced ? 'Yes! ✓' : 'Not yet', color: balanced ? Colors.green : Colors.red),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'x: ${_x.toStringAsFixed(0)}',
            value: _x,
            min: 0,
            max: 15,
            divisions: 15,
            activeColor: balanced ? Colors.green : Colors.brown,
            onChanged: (val) => setState(() {
              _prevTilt = targetTilt;
              _x = val;
              _controller.forward(from: 0);
            }),
          ),
        ],
      ),
    );
  }
}

class _BalancePainter extends CustomPainter {
  final double tilt; // -8..8 degrees-ish

  _BalancePainter({required this.tilt});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, 40);
    final angle = (tilt / 8) * 0.25;

    canvas.drawLine(Offset(center.dx, center.dy), Offset(center.dx, size.height - 20), Paint()..color = Colors.brown.shade700..strokeWidth = 4);
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
