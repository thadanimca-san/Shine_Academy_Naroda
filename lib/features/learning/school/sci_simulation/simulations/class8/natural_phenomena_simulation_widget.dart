import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Two demos: charged balloons that attract or repel depending on their
/// charge signs, and a seismograph trace whose intensity you control —
/// covering the chapter's two "natural phenomena," static charge and
/// earthquakes.
class NaturalPhenomenaSimulationWidget extends StatefulWidget {
  const NaturalPhenomenaSimulationWidget({super.key});

  @override
  State<NaturalPhenomenaSimulationWidget> createState() => _NaturalPhenomenaSimulationWidgetState();
}

class _NaturalPhenomenaSimulationWidgetState extends State<NaturalPhenomenaSimulationWidget> with SingleTickerProviderStateMixin {
  bool _showSeismograph = false;
  bool _sameCharge = false;
  late AnimationController _controller;
  double _magnitude = 3;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 3))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Charges & Earthquakes',
      icon: Icons.bolt,
      accent: Colors.blueGrey.shade700,
      description: 'Explore how electric charges interact, and how a seismograph records earthquake intensity.',
      actions: [
        ToggleButtons(
          isSelected: [!_showSeismograph, _showSeismograph],
          onPressed: (i) => setState(() => _showSeismograph = i == 1),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.blueGrey.shade700,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 60),
          children: [Text(TrilingualService.instance.getUIText('Charges')), Text(TrilingualService.instance.getUIText('Seismograph'))],
        ),
      ],
      child: _showSeismograph ? _buildSeismograph() : _buildCharges(),
    );
  }

  Widget _buildCharges() {
    final separation = _sameCharge ? 0.7 : 0.25;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        AnimatedBuilder(
          animation: _controller,
          builder: (context, _) {
            return SizedBox(
              height: 150,
              child: Stack(
                alignment: Alignment.center,
                children: [
                  AnimatedAlign(
                    duration: const Duration(milliseconds: 500),
                    alignment: Alignment(-separation, 0),
                    child: _balloon('+', Colors.red),
                  ),
                  AnimatedAlign(
                    duration: const Duration(milliseconds: 500),
                    alignment: Alignment(separation, 0),
                    child: _balloon(_sameCharge ? '+' : '-', _sameCharge ? Colors.red : Colors.blue),
                  ),
                ],
              ),
            );
          },
        ),
        const SizedBox(height: 8),
        Text(_sameCharge ? 'Like charges repel — the balloons push apart.' : 'Unlike charges attract — the balloons pull together.',
            style: TextStyle(fontWeight: FontWeight.w600)),
        const SizedBox(height: 14),
        SwitchListTile(
          contentPadding: EdgeInsets.zero,
          title: Text(TrilingualService.instance.getUIText('Same charge on both balloons'), style: TextStyle(fontSize: 13)),
          value: _sameCharge,
          activeColor: Colors.blueGrey,
          onChanged: (val) => setState(() => _sameCharge = val),
        ),
      ],
    );
  }

  Widget _balloon(String sign, Color color) {
    return Container(
      width: 60,
      height: 70,
      decoration: BoxDecoration(color: color, borderRadius: BorderRadius.circular(30)),
      alignment: Alignment.center,
      child: Text(sign, style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 24)),
    );
  }

  Widget _buildSeismograph() {
    return AnimatedBuilder(
      animation: _controller,
      builder: (context, _) {
        return Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Container(
              height: 140,
              width: double.infinity,
              decoration: BoxDecoration(color: Colors.grey.shade900, borderRadius: BorderRadius.circular(10)),
              child: CustomPaint(
                size: Size.infinite,
                painter: _SeismographPainter(phase: _controller.value * 2 * math.pi, magnitude: _magnitude),
              ),
            ),
            const SizedBox(height: 12),
            SimMetricPanel(metrics: [
              SimMetric(label: 'Magnitude', value: _magnitude.toStringAsFixed(1), color: Colors.deepOrange),
              SimMetric(label: 'Severity', value: _magnitude < 4 ? 'Minor' : (_magnitude < 6 ? 'Moderate' : 'Severe'), color: Colors.red),
            ]),
            const SizedBox(height: 14),
            SimSlider(
              label: 'Richter scale magnitude: ${_magnitude.toStringAsFixed(1)}',
              value: _magnitude,
              min: 1,
              max: 9,
              divisions: 16,
              activeColor: Colors.deepOrange,
              onChanged: (val) => setState(() => _magnitude = val),
            ),
          ],
        );
      },
    );
  }
}

class _SeismographPainter extends CustomPainter {
  final double phase;
  final double magnitude;

  _SeismographPainter({required this.phase, required this.magnitude});

  @override
  void paint(Canvas canvas, Size size) {
    final midY = size.height / 2;
    final path = Path();
    final rand = math.Random(1);
    for (double x = 0; x <= size.width; x += 2) {
      final noise = (rand.nextDouble() - 0.5) * magnitude * 3;
      final wave = math.sin((x / size.width) * 20 * math.pi + phase) * magnitude * 4;
      final y = midY + wave + noise;
      if (x == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
    }
    canvas.drawPath(path, Paint()..color = Colors.greenAccent..style = PaintingStyle.stroke..strokeWidth = 1.5);
  }

  @override
  bool shouldRepaint(covariant _SeismographPainter oldDelegate) => true;
}
