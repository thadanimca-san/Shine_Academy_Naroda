import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// Shows a vibrating tuning-fork-like source and the resulting wave: the
/// amplitude slider controls loudness, the frequency slider controls
/// pitch, tying the abstract graph to a visibly vibrating object.
class Class8SoundSimulationWidget extends StatefulWidget {
  const Class8SoundSimulationWidget({super.key});

  @override
  State<Class8SoundSimulationWidget> createState() => _Class8SoundSimulationWidgetState();
}

class _Class8SoundSimulationWidgetState extends State<Class8SoundSimulationWidget> with SingleTickerProviderStateMixin {
  double _frequency = 3.0;
  double _amplitude = 0.5;
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
      title: 'Vibrations & Sound',
      icon: Icons.graphic_eq,
      accent: Colors.deepPurple,
      description: 'A vibrating object produces sound. Frequency (how fast it vibrates) sets the pitch; amplitude (how far it moves) sets the loudness.',
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          final wobble = math.sin(_controller.value * 2 * math.pi * _frequency) * _amplitude * 18;
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Container(
                height: 130,
                width: double.infinity,
                decoration: BoxDecoration(color: Colors.deepPurple.shade50, borderRadius: BorderRadius.circular(10)),
                child: Center(
                  child: Transform.translate(
                    offset: Offset(wobble, 0),
                    child: Container(
                      width: 14,
                      height: 90,
                      decoration: BoxDecoration(color: Colors.deepPurple.shade400, borderRadius: BorderRadius.circular(6)),
                    ),
                  ),
                ),
              ),
              const SizedBox(height: 10),
              SizedBox(
                height: 90,
                width: double.infinity,
                child: CustomPaint(
                  size: Size.infinite,
                  painter: _WavePainter(phase: _controller.value * 2 * math.pi, frequency: _frequency, amplitude: _amplitude),
                ),
              ),
              const SizedBox(height: 12),
              SimMetricPanel(metrics: [
                SimMetric(label: 'Pitch', value: _frequency < 2.5 ? 'Low' : (_frequency < 4.5 ? 'Medium' : 'High'), color: Colors.deepPurple),
                SimMetric(label: 'Loudness', value: _amplitude < 0.4 ? 'Soft' : (_amplitude < 0.75 ? 'Medium' : 'Loud'), color: Colors.pink),
              ]),
              const SizedBox(height: 14),
              SimSlider(
                label: 'Frequency (vibrations per second)',
                value: _frequency,
                min: 1,
                max: 6,
                divisions: 25,
                activeColor: Colors.deepPurple,
                onChanged: (val) => setState(() => _frequency = val),
              ),
              SimSlider(
                label: 'Amplitude (size of vibration)',
                value: _amplitude,
                min: 0.1,
                max: 1.0,
                divisions: 18,
                activeColor: Colors.pink,
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
    canvas.drawLine(Offset(0, midY), Offset(size.width, midY), Paint()..color = Colors.grey.shade300..strokeWidth = 1);
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
    canvas.drawPath(path, Paint()..color = Colors.deepPurple.shade400..style = PaintingStyle.stroke..strokeWidth = 3);
  }

  @override
  bool shouldRepaint(covariant _WavePainter oldDelegate) => true;
}
