import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// An observer at a fixed distance from a tower: the line of sight sweeps
/// up to the current angle of elevation whenever you move the slider,
/// with the tower growing in sync to the computed height.
class ApplicationsTrigonometrySimulationWidget extends StatefulWidget {
  const ApplicationsTrigonometrySimulationWidget({super.key});

  @override
  State<ApplicationsTrigonometrySimulationWidget> createState() => _ApplicationsTrigonometrySimulationWidgetState();
}

class _ApplicationsTrigonometrySimulationWidgetState extends State<ApplicationsTrigonometrySimulationWidget> with SingleTickerProviderStateMixin {
  double _angleDeg = 45;
  final double _distance = 40;
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

  @override
  Widget build(BuildContext context) {
    final height = _distance * math.tan(_angleDeg * math.pi / 180);

    return SimFrame(
      title: 'Angle of Elevation & Height',
      icon: Icons.height,
      accent: Colors.brown.shade600,
      description: 'From a fixed distance, slide the angle of elevation and watch the line of sight sweep up as the tower height changes.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.brown.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                return CustomPaint(size: Size.infinite, painter: _TowerPainter(angleDeg: _angleDeg * eased));
              },
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Distance', value: '${_distance.toStringAsFixed(0)} m'),
            SimMetric(label: 'Angle of Elevation', value: '${_angleDeg.toStringAsFixed(0)}°', color: Colors.deepOrange),
            SimMetric(label: 'Tower Height', value: '${height.toStringAsFixed(1)} m', color: Colors.teal),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Angle of elevation: ${_angleDeg.toStringAsFixed(0)}°',
            value: _angleDeg,
            min: 10,
            max: 80,
            divisions: 14,
            activeColor: Colors.brown,
            onChanged: (v) => setState(() {
              _angleDeg = v;
              _controller.forward(from: 0);
            }),
          ),
        ],
      ),
    );
  }
}

class _TowerPainter extends CustomPainter {
  final double angleDeg;
  _TowerPainter({required this.angleDeg});

  @override
  void paint(Canvas canvas, Size size) {
    final ground = size.height - 20;
    final observer = Offset(size.width - 20, ground);
    final towerBase = Offset(20, ground);
    final rad = angleDeg * math.pi / 180;
    final towerHeightPx = (observer.dx - towerBase.dx) * math.tan(rad);
    final towerTop = Offset(towerBase.dx, (ground - towerHeightPx).clamp(10.0, ground));

    canvas.drawLine(towerBase, observer, Paint()..color = Colors.grey.shade500..strokeWidth = 1.5);
    canvas.drawLine(towerBase, towerTop, Paint()..color = Colors.brown.shade800..strokeWidth = 4);
    canvas.drawLine(observer, towerTop, Paint()..color = Colors.deepOrange..strokeWidth = 2);
    canvas.drawCircle(observer, 5, Paint()..color = Colors.blue.shade700);
  }

  @override
  bool shouldRepaint(covariant _TowerPainter oldDelegate) => oldDelegate.angleDeg != angleDeg;
}
