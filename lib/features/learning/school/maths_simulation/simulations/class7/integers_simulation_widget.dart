import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A number-line jumper: two integer sliders (a and b) animate as hops
/// along a number line, landing on a + b, making integer addition and
/// direction (left for negative, right for positive) visible.
class IntegersSimulationWidget extends StatefulWidget {
  const IntegersSimulationWidget({super.key});

  @override
  State<IntegersSimulationWidget> createState() => _IntegersSimulationWidgetState();
}

class _IntegersSimulationWidgetState extends State<IntegersSimulationWidget> with SingleTickerProviderStateMixin {
  double _a = 3;
  double _b = -5;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 1400));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _play() {
    _controller.forward(from: 0);
    setState(() {});
  }

  @override
  Widget build(BuildContext context) {
    final sum = _a + _b;

    return SimFrame(
      title: 'Integer Number Line',
      icon: Icons.timeline,
      accent: Colors.indigo.shade600,
      description: 'Press play to watch the hop from 0 to a, then from a to a + b — right for positive, left for negative.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 110,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.indigo.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                // First half of the animation hops 0 -> a, second half hops a -> a+b.
                final t = _controller.value;
                double hopStart, hopEnd, hopT;
                if (t < 0.5) {
                  hopStart = 0;
                  hopEnd = _a;
                  hopT = (t / 0.5).clamp(0.0, 1.0);
                } else {
                  hopStart = _a;
                  hopEnd = sum;
                  hopT = ((t - 0.5) / 0.5).clamp(0.0, 1.0);
                }
                // Ease the hop with a slight arc-like bounce via a sine curve.
                final eased = Curves.easeInOut.transform(hopT);
                final tokenPos = hopStart + (hopEnd - hopStart) * eased;
                final arcLift = 10.0 * (1 - (2 * hopT - 1).abs());

                return CustomPaint(
                  size: Size.infinite,
                  painter: _NumberLinePainter(
                    start: _a,
                    end: sum,
                    tokenPos: tokenPos,
                    arcLift: arcLift,
                    showFinal: _controller.isCompleted,
                  ),
                );
              },
            ),
          ),
          const SizedBox(height: 10),
          Align(
            alignment: Alignment.centerLeft,
            child: ElevatedButton.icon(
              onPressed: _play,
              icon: Icon(Icons.play_arrow),
              label: Text(TrilingualService.instance.getUIText('Play hop')),
              style: ElevatedButton.styleFrom(backgroundColor: Colors.indigo.shade600, foregroundColor: Colors.white),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'a', value: _a.toStringAsFixed(0)),
            SimMetric(label: 'b', value: _b.toStringAsFixed(0)),
            SimMetric(label: 'a + b', value: sum.toStringAsFixed(0), color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'a: ${_a.toStringAsFixed(0)}', value: _a, min: -10, max: 10, divisions: 20, activeColor: Colors.indigo, onChanged: (v) => setState(() { _a = v; _controller.value = 0; })),
          SimSlider(label: 'b: ${_b.toStringAsFixed(0)}', value: _b, min: -10, max: 10, divisions: 20, activeColor: Colors.deepOrange, onChanged: (v) => setState(() { _b = v; _controller.value = 0; })),
        ],
      ),
    );
  }
}

class _NumberLinePainter extends CustomPainter {
  final double start;
  final double end;
  final double tokenPos;
  final double arcLift;
  final bool showFinal;

  _NumberLinePainter({required this.start, required this.end, required this.tokenPos, required this.arcLift, required this.showFinal});

  @override
  void paint(Canvas canvas, Size size) {
    const minVal = -15.0, maxVal = 15.0;
    final midY = size.height / 2;
    double xFor(double v) => (v - minVal) / (maxVal - minVal) * (size.width - 20) + 10;

    canvas.drawLine(Offset(10, midY), Offset(size.width - 10, midY), Paint()..color = Colors.grey.shade500..strokeWidth = 1.5);
    for (int i = minVal.toInt(); i <= maxVal.toInt(); i += 5) {
      final x = xFor(i.toDouble());
      canvas.drawLine(Offset(x, midY - 4), Offset(x, midY + 4), Paint()..color = Colors.grey.shade500);
      final tp = TextPainter(text: TextSpan(text: '$i', style: TextStyle(fontSize: 9, color: Colors.grey.shade700)), textDirection: TextDirection.ltr)..layout();
      tp.paint(canvas, Offset(x - tp.width / 2, midY + 8));
    }

    canvas.drawCircle(Offset(xFor(0), midY), 4, Paint()..color = Colors.black45);

    // Faded markers for the resting points once the hop has passed them.
    canvas.drawCircle(Offset(xFor(start), midY), 5, Paint()..color = Colors.indigo.withValues(alpha: 0.4));
    if (showFinal) {
      canvas.drawCircle(Offset(xFor(end), midY), 7, Paint()..color = Colors.deepOrange);
    }

    // The hopping token, lifted along a small arc mid-hop.
    final tokenCenter = Offset(xFor(tokenPos), midY - arcLift);
    canvas.drawCircle(tokenCenter, 7, Paint()..color = Colors.deepOrange);
    canvas.drawCircle(tokenCenter, 7, Paint()..color = Colors.white..style = PaintingStyle.stroke..strokeWidth = 1.5);
  }

  @override
  bool shouldRepaint(covariant _NumberLinePainter oldDelegate) =>
      oldDelegate.tokenPos != tokenPos || oldDelegate.arcLift != arcLift || oldDelegate.showFinal != showFinal || oldDelegate.start != start || oldDelegate.end != end;
}
