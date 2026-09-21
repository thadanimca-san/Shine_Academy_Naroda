import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'common/sim_frame.dart';

/// A swinging pendulum that continuously converts potential energy into
/// kinetic energy and back, with live bar meters so the law of conservation
/// of energy is visible rather than abstract.
class WorkEnergySimulationWidget extends StatefulWidget {
  const WorkEnergySimulationWidget({super.key});

  @override
  State<WorkEnergySimulationWidget> createState() => _WorkEnergySimulationWidgetState();
}

class _WorkEnergySimulationWidgetState extends State<WorkEnergySimulationWidget> with SingleTickerProviderStateMixin {
  double _amplitudeDeg = 45.0; // max swing angle
  double _mass = 2.0; // kg
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 3));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    const g = 9.8;
    const stringLength = 1.4; // m

    return SimFrame(
      title: 'Work & Energy: Swinging Pendulum',
      icon: Icons.timeline,
      accent: Colors.green,
      description: 'As the bob swings, potential energy (height) trades off with kinetic energy (speed) — total mechanical energy stays constant.',
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          // Oscillation: angle(t) = amplitude * cos(2*pi*t)
          final amplitudeRad = _amplitudeDeg * math.pi / 180;
          final angle = amplitudeRad * math.cos(2 * math.pi * _controller.value);

          final heightAtAngle = stringLength * (1 - math.cos(angle));
          final maxHeight = stringLength * (1 - math.cos(amplitudeRad));
          final pe = _mass * g * heightAtAngle;
          final peMax = _mass * g * maxHeight;
          final ke = (peMax - pe).clamp(0, double.infinity);
          final speed = math.sqrt((2 * ke / _mass).clamp(0, double.infinity));

          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              SimTransport(
                isPlaying: _controller.isAnimating,
                color: Colors.green,
                onPlayPause: () {
                  setState(() {
                    if (_controller.isAnimating) {
                      _controller.stop();
                    } else {
                      _controller.repeat();
                    }
                  });
                },
                onReset: () => setState(() => _controller.value = 0),
              ),
              const SizedBox(height: 14),
              LayoutBuilder(builder: (context, constraints) {
                const boxHeight = 190.0;
                final pivot = Offset(constraints.maxWidth / 2, 14);
                final pxLength = 130.0;
                final bobX = pivot.dx + pxLength * math.sin(angle);
                final bobY = pivot.dy + pxLength * math.cos(angle);
                return Container(
                  height: boxHeight,
                  width: double.infinity,
                  decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(10)),
                  child: CustomPaint(
                    size: Size(constraints.maxWidth, boxHeight),
                    painter: _PendulumPainter(pivot: pivot, bob: Offset(bobX, bobY)),
                  ),
                );
              }),
              const SizedBox(height: 12),
              SimMetricPanel(metrics: [
                SimMetric(label: 'Height', value: '${heightAtAngle.toStringAsFixed(2)} m'),
                SimMetric(label: 'Speed', value: '${speed.toStringAsFixed(2)} m/s', color: Colors.deepOrange),
              ]),
              const SizedBox(height: 12),
              _EnergyBar(label: 'Potential Energy', value: pe.toDouble(), max: peMax <= 0 ? 1 : peMax.toDouble(), color: Colors.blue),
              const SizedBox(height: 8),
              _EnergyBar(label: 'Kinetic Energy', value: ke.toDouble(), max: peMax <= 0 ? 1 : peMax.toDouble(), color: Colors.red),
              const SizedBox(height: 14),
              SimSlider(
                label: 'Swing amplitude: ${_amplitudeDeg.toStringAsFixed(0)}°',
                value: _amplitudeDeg,
                min: 10,
                max: 70,
                divisions: 12,
                activeColor: Colors.green,
                onChanged: (val) => setState(() => _amplitudeDeg = val),
              ),
              SimSlider(
                label: 'Bob mass: ${_mass.toStringAsFixed(1)} kg',
                value: _mass,
                min: 0.5,
                max: 5.0,
                divisions: 45,
                activeColor: Colors.green,
                onChanged: (val) => setState(() => _mass = val),
              ),
            ],
          );
        },
      ),
    );
  }
}

class _PendulumPainter extends CustomPainter {
  final Offset pivot;
  final Offset bob;

  _PendulumPainter({required this.pivot, required this.bob});

  @override
  void paint(Canvas canvas, Size size) {
    final stringPaint = Paint()
      ..color = Colors.grey.shade600
      ..strokeWidth = 2;
    canvas.drawLine(pivot, bob, stringPaint);
    canvas.drawCircle(pivot, 4, Paint()..color = Colors.grey.shade800);
    canvas.drawCircle(
        bob, 16, Paint()..shader = RadialGradient(colors: [Colors.orange.shade200, Colors.orange.shade800]).createShader(Rect.fromCircle(center: bob, radius: 16)));
  }

  @override
  bool shouldRepaint(covariant _PendulumPainter oldDelegate) => oldDelegate.bob != bob;
}

class _EnergyBar extends StatelessWidget {
  final String label;
  final double value;
  final double max;
  final Color color;

  const _EnergyBar({required this.label, required this.value, required this.max, required this.color});

  @override
  Widget build(BuildContext context) {
    final fraction = (value / max).clamp(0.0, 1.0);
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            Text(label, style: TextStyle(fontSize: 12.5, fontWeight: FontWeight.w600)),
            Text('${value.toStringAsFixed(1)} J', style: TextStyle(fontSize: 12, color: color, fontWeight: FontWeight.bold)),
          ],
        ),
        const SizedBox(height: 4),
        ClipRRect(
          borderRadius: BorderRadius.circular(6),
          child: LinearProgressIndicator(value: fraction, minHeight: 12, backgroundColor: Colors.grey.shade200, valueColor: AlwaysStoppedAnimation(color)),
        ),
      ],
    );
  }
}
