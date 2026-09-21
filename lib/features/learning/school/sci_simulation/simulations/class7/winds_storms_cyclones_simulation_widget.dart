import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// An animated spinning cyclone whose intensity responds to a wind-speed
/// slider, illustrating how low pressure at the centre pulls in
/// fast-rotating air.
class WindsStormsCyclonesSimulationWidget extends StatefulWidget {
  const WindsStormsCyclonesSimulationWidget({super.key});

  @override
  State<WindsStormsCyclonesSimulationWidget> createState() => _WindsStormsCyclonesSimulationWidgetState();
}

class _WindsStormsCyclonesSimulationWidgetState extends State<WindsStormsCyclonesSimulationWidget> with SingleTickerProviderStateMixin {
  double _windSpeed = 40; // km/h
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 4))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  String get _category {
    if (_windSpeed < 63) return 'Breeze';
    if (_windSpeed < 118) return 'Tropical Storm';
    return 'Cyclone';
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Winds & Cyclones',
      icon: Icons.cyclone,
      accent: Colors.blueGrey.shade700,
      description: 'Faster-moving air creates lower pressure at the centre. Increase wind speed and watch the storm intensify.',
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          final speedFactor = (_windSpeed / 150).clamp(0.1, 1.0);
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                height: 200,
                width: double.infinity,
                decoration: BoxDecoration(
                  gradient: LinearGradient(colors: [Colors.blueGrey.shade900, Colors.blueGrey.shade700]),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: CustomPaint(
                  size: Size.infinite,
                  painter: _CyclonePainter(phase: _controller.value * 2 * math.pi * (1 + speedFactor * 2), intensity: speedFactor),
                ),
              ),
              const SizedBox(height: 12),
              SimMetricPanel(metrics: [
                SimMetric(label: 'Wind Speed', value: '${_windSpeed.toStringAsFixed(0)} km/h'),
                SimMetric(label: 'Category', value: _category, color: Colors.deepOrange),
              ]),
              const SizedBox(height: 14),
              SimSlider(
                label: 'Wind speed: ${_windSpeed.toStringAsFixed(0)} km/h',
                value: _windSpeed,
                min: 10,
                max: 150,
                divisions: 28,
                activeColor: Colors.blueGrey,
                onChanged: (val) => setState(() => _windSpeed = val),
              ),
            ],
          );
        },
      ),
    );
  }
}

class _CyclonePainter extends CustomPainter {
  final double phase;
  final double intensity;

  _CyclonePainter({required this.phase, required this.intensity});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final maxRadius = math.min(size.width, size.height) / 2 - 10;
    final arms = 4;

    for (int a = 0; a < arms; a++) {
      final path = Path();
      final baseAngle = phase + (2 * math.pi * a / arms);
      for (double r = 6; r <= maxRadius; r += 3) {
        final angle = baseAngle + r * (0.06 + intensity * 0.05);
        final x = center.dx + r * math.cos(angle);
        final y = center.dy + r * math.sin(angle);
        if (r == 6) {
          path.moveTo(x, y);
        } else {
          path.lineTo(x, y);
        }
      }
      canvas.drawPath(
        path,
        Paint()
          ..color = Colors.white.withValues(alpha: 0.5 + intensity * 0.4)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2 + intensity * 2,
      );
    }

    canvas.drawCircle(center, 6 + intensity * 4, Paint()..color = Colors.white);
  }

  @override
  bool shouldRepaint(covariant _CyclonePainter oldDelegate) => true;
}
