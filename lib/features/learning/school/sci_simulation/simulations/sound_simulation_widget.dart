import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Animates a travelling sound wave and a row of air particles that
/// compress and rarefy, so frequency (pitch) and amplitude (loudness)
/// stop being abstract slider numbers.
class SoundSimulationWidget extends StatefulWidget {
  const SoundSimulationWidget({super.key});

  @override
  State<SoundSimulationWidget> createState() => _SoundSimulationWidgetState();
}

class _SoundSimulationWidgetState extends State<SoundSimulationWidget> with SingleTickerProviderStateMixin {
  double _frequency = 2.0; // visual cycles across the box (represents pitch)
  double _amplitude = 0.6; // 0..1 (represents loudness)
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 2))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Sound Wave Lab',
      icon: Icons.graphic_eq,
      accent: Colors.pink,
      description: 'Frequency controls pitch and amplitude controls loudness. Watch the air particles compress and spread as the wave passes.',
      actions: [
        AnimatedBuilder(
          animation: _controller,
          builder: (context, _) => IconButton(
            icon: Icon(_controller.isAnimating ? Icons.pause_circle : Icons.play_circle, color: Colors.pink, size: 30),
            onPressed: () => setState(() => _controller.isAnimating ? _controller.stop() : _controller.repeat()),
          ),
        ),
      ],
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                height: 140,
                width: double.infinity,
                decoration: BoxDecoration(color: Colors.pink.shade50, borderRadius: BorderRadius.circular(10)),
                child: CustomPaint(
                  size: Size.infinite,
                  painter: _WavePainter(phase: _controller.value * 2 * math.pi, frequency: _frequency, amplitude: _amplitude),
                ),
              ),
              const SizedBox(height: 10),
              Text(TrilingualService.instance.getUIText('Particles (compression = high pitch/energy zones)'), style: TextStyle(fontSize: 11, color: Colors.grey.shade600)),
              const SizedBox(height: 6),
              SizedBox(
                height: 46,
                width: double.infinity,
                child: CustomPaint(
                  size: Size.infinite,
                  painter: _ParticlePainter(phase: _controller.value * 2 * math.pi, frequency: _frequency, amplitude: _amplitude),
                ),
              ),
              const SizedBox(height: 14),
              SimMetricPanel(metrics: [
                SimMetric(label: 'Pitch (frequency)', value: _frequency < 2.5 ? 'Low' : (_frequency < 4.5 ? 'Medium' : 'High'), color: Colors.pink),
                SimMetric(label: 'Loudness (amplitude)', value: _amplitude < 0.4 ? 'Soft' : (_amplitude < 0.75 ? 'Medium' : 'Loud'), color: Colors.deepPurple),
              ]),
              const SizedBox(height: 14),
              SimSlider(
                label: 'Frequency: ${_frequency.toStringAsFixed(1)} (relative pitch)',
                value: _frequency,
                min: 1.0,
                max: 6.0,
                divisions: 25,
                activeColor: Colors.pink,
                onChanged: (val) => setState(() => _frequency = val),
              ),
              SimSlider(
                label: 'Amplitude: ${(_amplitude * 100).toStringAsFixed(0)}% (loudness)',
                value: _amplitude,
                min: 0.1,
                max: 1.0,
                divisions: 18,
                activeColor: Colors.deepPurple,
                onChanged: (val) => setState(() => _amplitude = val),
              ),
            ],
          );
        },
      ),
    );
  }
}

class _WavePainter extends CustomPainter {
  final double phase;
  final double frequency;
  final double amplitude;

  _WavePainter({required this.phase, required this.frequency, required this.amplitude});

  @override
  void paint(Canvas canvas, Size size) {
    final midY = size.height / 2;
    final axisPaint = Paint()
      ..color = Colors.grey.shade300
      ..strokeWidth = 1;
    canvas.drawLine(Offset(0, midY), Offset(size.width, midY), axisPaint);

    final path = Path();
    for (double x = 0; x <= size.width; x++) {
      final theta = (x / size.width) * frequency * 2 * math.pi + phase;
      final y = midY - math.sin(theta) * amplitude * (size.height / 2 - 8);
      if (x == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
    }
    canvas.drawPath(
      path,
      Paint()
        ..color = Colors.pink.shade600
        ..style = PaintingStyle.stroke
        ..strokeWidth = 3,
    );
  }

  @override
  bool shouldRepaint(covariant _WavePainter oldDelegate) => true;
}

class _ParticlePainter extends CustomPainter {
  final double phase;
  final double frequency;
  final double amplitude;

  _ParticlePainter({required this.phase, required this.frequency, required this.amplitude});

  @override
  void paint(Canvas canvas, Size size) {
    const count = 26;
    final spacing = size.width / count;
    for (int i = 0; i < count; i++) {
      final baseX = spacing * i + spacing / 2;
      final theta = (baseX / size.width) * frequency * 2 * math.pi + phase;
      final displacement = math.sin(theta) * amplitude * spacing * 0.8;
      final x = (baseX + displacement).clamp(0.0, size.width);
      canvas.drawCircle(Offset(x, size.height / 2), 4, Paint()..color = Colors.deepPurple.shade400);
    }
  }

  @override
  bool shouldRepaint(covariant _ParticlePainter oldDelegate) => true;
}
