import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import '../common/graph_painter.dart';

/// A swinging pendulum used as a timer, next to a moving object whose
/// steady speed builds a distance-time graph — tying "motion" and "time"
/// together the way the chapter does.
class MotionTimeSimulationWidget extends StatefulWidget {
  const MotionTimeSimulationWidget({super.key});

  @override
  State<MotionTimeSimulationWidget> createState() => _MotionTimeSimulationWidgetState();
}

class _MotionTimeSimulationWidgetState extends State<MotionTimeSimulationWidget> with SingleTickerProviderStateMixin {
  double _speed = 5; // m/s, uniform
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 5))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Uniform Motion & Time',
      icon: Icons.timer,
      accent: Colors.blue.shade700,
      description: 'An object moving at constant speed covers equal distances in equal times — its distance-time graph is a straight line.',
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          final t = _controller.value * 5;
          final distance = _speed * t;
          final points = List.generate(30, (i) {
            final ti = 5 * i / 29;
            return Offset(ti / 5, (( _speed * ti) / (_speed * 5)).clamp(0.0, 1.0));
          });

          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              LayoutBuilder(builder: (context, constraints) {
                final trackWidth = constraints.maxWidth - 40;
                return Container(
                  height: 60,
                  decoration: BoxDecoration(color: Colors.blue.shade50, borderRadius: BorderRadius.circular(10)),
                  child: Stack(
                    alignment: Alignment.centerLeft,
                    children: [
                      Positioned(left: 16, right: 16, child: Container(height: 3, color: Colors.blue.shade200)),
                      Positioned(left: 16 + _controller.value * trackWidth, child: Icon(Icons.directions_car, color: Colors.blue, size: 30)),
                    ],
                  ),
                );
              }),
              const SizedBox(height: 10),
              // Pendulum as a visual timer
              SizedBox(
                height: 90,
                child: CustomPaint(
                  size: Size.infinite,
                  painter: _PendulumPainter(angle: math.sin(_controller.value * 2 * math.pi * 2) * 0.5),
                ),
              ),
              const SizedBox(height: 10),
              SimMetricPanel(metrics: [
                SimMetric(label: 'Time', value: '${t.toStringAsFixed(1)} s'),
                SimMetric(label: 'Distance', value: '${distance.toStringAsFixed(1)} m', color: Colors.teal),
                SimMetric(label: 'Speed', value: '${_speed.toStringAsFixed(1)} m/s', color: Colors.deepOrange),
              ]),
              const SizedBox(height: 12),
              MiniGraph(title: 'Distance vs Time (straight line = uniform motion)', points: points, color: Colors.blue, markerT: _controller.value),
              const SizedBox(height: 14),
              SimSlider(
                label: 'Speed: ${_speed.toStringAsFixed(1)} m/s',
                value: _speed,
                min: 1,
                max: 15,
                divisions: 28,
                activeColor: Colors.blue,
                onChanged: (val) => setState(() => _speed = val),
              ),
            ],
          );
        },
      ),
    );
  }
}

class _PendulumPainter extends CustomPainter {
  final double angle;

  _PendulumPainter({required this.angle});

  @override
  void paint(Canvas canvas, Size size) {
    final pivot = Offset(size.width / 2, 5);
    final length = 70.0;
    final bob = pivot + Offset(math.sin(angle) * length, math.cos(angle) * length);
    canvas.drawLine(pivot, bob, Paint()..color = Colors.grey.shade600..strokeWidth = 2);
    canvas.drawCircle(pivot, 3, Paint()..color = Colors.grey.shade800);
    canvas.drawCircle(bob, 12, Paint()..color = Colors.deepOrange.shade400);
  }

  @override
  bool shouldRepaint(covariant _PendulumPainter oldDelegate) => oldDelegate.angle != angle;
}
