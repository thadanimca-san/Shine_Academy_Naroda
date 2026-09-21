import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A three-category pie chart whose slices sweep open from 0° and whose
/// sizes recompute live as you adjust each category's value with sliders.
class Class8DataHandlingSimulationWidget extends StatefulWidget {
  const Class8DataHandlingSimulationWidget({super.key});

  @override
  State<Class8DataHandlingSimulationWidget> createState() => _DataHandlingSimulationWidgetState();
}

class _DataHandlingSimulationWidgetState extends State<Class8DataHandlingSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 30, _b = 45, _c = 25;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 900));
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
    final total = _a + _b + _c;
    final angleA = 360 * _a / total;
    final angleB = 360 * _b / total;
    final angleC = 360 * _c / total;

    return SimFrame(
      title: 'Pie Chart Builder',
      icon: Icons.pie_chart,
      accent: Colors.deepOrange.shade400,
      description: 'Adjust each category and watch the pie slices sweep open and the central angles update.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.deepOrange.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                return CustomPaint(size: Size.infinite, painter: _PiePainter(a: _a, b: _b, c: _c, sweepT: eased));
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: TextButton.icon(
              onPressed: _replay,
              icon: Icon(Icons.replay, size: 18),
              label: Text(TrilingualService.instance.getUIText('Replay')),
              style: TextButton.styleFrom(foregroundColor: Colors.deepOrange.shade400),
            ),
          ),
          SimMetricPanel(metrics: [
            SimMetric(label: 'A angle', value: '${angleA.toStringAsFixed(0)}°', color: Colors.blue),
            SimMetric(label: 'B angle', value: '${angleB.toStringAsFixed(0)}°', color: Colors.green),
            SimMetric(label: 'C angle', value: '${angleC.toStringAsFixed(0)}°', color: Colors.orange),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Category A: ${_a.toStringAsFixed(0)}', value: _a, min: 5, max: 100, divisions: 19, activeColor: Colors.blue, onChanged: (v) => setState(() { _a = v; _replay(); })),
          SimSlider(label: 'Category B: ${_b.toStringAsFixed(0)}', value: _b, min: 5, max: 100, divisions: 19, activeColor: Colors.green, onChanged: (v) => setState(() { _b = v; _replay(); })),
          SimSlider(label: 'Category C: ${_c.toStringAsFixed(0)}', value: _c, min: 5, max: 100, divisions: 19, activeColor: Colors.orange, onChanged: (v) => setState(() { _c = v; _replay(); })),
        ],
      ),
    );
  }
}

class _PiePainter extends CustomPainter {
  final double a, b, c;
  final double sweepT;
  _PiePainter({required this.a, required this.b, required this.c, required this.sweepT});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final radius = size.height / 2 - 10;
    final total = a + b + c;
    double start = -1.5708;
    final colors = [Colors.blue, Colors.green, Colors.orange];
    final values = [a, b, c];
    for (int i = 0; i < 3; i++) {
      final sweep = (values[i] / total) * 2 * 3.14159265 * sweepT;
      canvas.drawArc(Rect.fromCircle(center: center, radius: radius), start, sweep, true, Paint()..color = colors[i]);
      start += (values[i] / total) * 2 * 3.14159265;
    }
  }

  @override
  bool shouldRepaint(covariant _PiePainter oldDelegate) => true;
}
