import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A histogram with five adjustable bars and its frequency polygon
/// (the line joining bar-top midpoints) drawn on top: bars grow up from
/// zero on load and on reset, and the polygon draws itself in after,
/// so the connection between the two representations is visible.
class StatisticsSimulationWidget extends StatefulWidget {
  const StatisticsSimulationWidget({super.key});

  @override
  State<StatisticsSimulationWidget> createState() => _StatisticsSimulationWidgetState();
}

class _StatisticsSimulationWidgetState extends State<StatisticsSimulationWidget> with SingleTickerProviderStateMixin {
  List<double> _freq = [3, 7, 10, 6, 4];
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

  void _reset() {
    setState(() => _freq = [3, 7, 10, 6, 4]);
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Histogram & Frequency Polygon',
      icon: Icons.bar_chart,
      accent: Colors.deepOrange.shade400,
      description: 'Drag a bar to change its frequency — the frequency polygon (line) always joins the midpoints of the bar tops.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            height: 170,
            child: LayoutBuilder(builder: (context, constraints) {
              return GestureDetector(
                onPanUpdate: (details) {
                  final barWidth = constraints.maxWidth / _freq.length;
                  final index = (details.localPosition.dx / barWidth).floor().clamp(0, _freq.length - 1);
                  setState(() {
                    final newVal = (_freq[index] - details.delta.dy / 6).clamp(1.0, 15.0);
                    _freq[index] = newVal;
                  });
                  _controller.value = 1;
                },
                child: AnimatedBuilder(
                  animation: _controller,
                  builder: (context, _) {
                    final eased = Curves.easeOutBack.transform(_controller.value).clamp(0.0, 1.0);
                    return CustomPaint(
                      size: Size(constraints.maxWidth, 170),
                      painter: _HistogramPainter(freq: _freq, growth: eased),
                    );
                  },
                ),
              );
            }),
          ),
          const SizedBox(height: 4),
          Text(TrilingualService.instance.getUIText('Drag up/down on a bar to change its frequency'), style: TextStyle(fontSize: 11, color: Theme.of(context).colorScheme.onSurface.withOpacity(0.45))),
          const SizedBox(height: 12),
          Center(
            child: TextButton.icon(
              onPressed: _reset,
              icon: Icon(Icons.refresh),
              label: Text(TrilingualService.instance.getUIText('Reset')),
            ),
          ),
        ],
      ),
    );
  }
}

class _HistogramPainter extends CustomPainter {
  final List<double> freq;
  final double growth;
  _HistogramPainter({required this.freq, this.growth = 1});

  @override
  void paint(Canvas canvas, Size size) {
    final barWidth = size.width / freq.length;
    final maxFreq = 15.0;
    final points = <Offset>[];

    for (int i = 0; i < freq.length; i++) {
      final barHeight = (freq[i] / maxFreq) * (size.height - 20) * growth;
      final rect = Rect.fromLTWH(i * barWidth + 4, size.height - barHeight, barWidth - 8, barHeight);
      canvas.drawRect(rect, Paint()..color = Colors.deepOrange.shade200);
      canvas.drawRect(rect, Paint()..color = Colors.deepOrange.shade700..style = PaintingStyle.stroke..strokeWidth = 1.5);
      points.add(Offset(i * barWidth + barWidth / 2, size.height - barHeight));
    }

    final path = Path()..moveTo(points.first.dx, points.first.dy);
    for (final p in points.skip(1)) {
      path.lineTo(p.dx, p.dy);
    }
    canvas.drawPath(path, Paint()..color = Colors.indigo..style = PaintingStyle.stroke..strokeWidth = 2.5);
    for (final p in points) {
      canvas.drawCircle(p, 4, Paint()..color = Colors.indigo);
    }
  }

  @override
  bool shouldRepaint(covariant _HistogramPainter oldDelegate) => oldDelegate.freq != freq || oldDelegate.growth != growth;
}
