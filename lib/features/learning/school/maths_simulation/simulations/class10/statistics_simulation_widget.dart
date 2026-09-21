import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// Slide the mean and median of a distribution and watch the three bars
/// (mean, median, mode) grow into place, with the empirical relationship
/// (Mode = 3×Median − 2×Mean) computing the mode live.
class Class10StatisticsSimulationWidget extends StatefulWidget {
  const Class10StatisticsSimulationWidget({super.key});

  @override
  State<Class10StatisticsSimulationWidget> createState() => _StatisticsSimulationWidgetState();
}

class _StatisticsSimulationWidgetState extends State<Class10StatisticsSimulationWidget> with SingleTickerProviderStateMixin {
  double _mean = 30;
  double _median = 28;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 700));
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
    final mode = 3 * _median - 2 * _mean;
    final maxVal = [_mean, _median, mode].reduce((a, b) => a > b ? a : b).clamp(1.0, double.infinity);

    return SimFrame(
      title: 'Empirical Relation: Mean, Median, Mode',
      icon: Icons.insights,
      accent: Colors.indigo.shade600,
      description: 'For moderately skewed data: Mode = 3×Median − 2×Mean. Adjust mean and median and watch the bars grow to the mode\'s response.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            height: 150,
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeOutBack.transform(_controller.value);
                return Row(
                  mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    _bar('Mean', _mean, maxVal, Colors.blue, eased),
                    _bar('Median', _median, maxVal, Colors.teal, eased),
                    _bar('Mode', mode, maxVal, Colors.deepOrange, eased),
                  ],
                );
              },
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Mean', value: _mean.toStringAsFixed(1), color: Colors.blue),
            SimMetric(label: 'Median', value: _median.toStringAsFixed(1), color: Colors.teal),
            SimMetric(label: 'Mode', value: mode.toStringAsFixed(1), color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'Mean: ${_mean.toStringAsFixed(0)}', value: _mean, min: 10, max: 50, divisions: 40, activeColor: Colors.blue, onChanged: (v) => setState(() { _mean = v; _replay(); })),
          SimSlider(label: 'Median: ${_median.toStringAsFixed(0)}', value: _median, min: 10, max: 50, divisions: 40, activeColor: Colors.teal, onChanged: (v) => setState(() { _median = v; _replay(); })),
        ],
      ),
    );
  }

  Widget _bar(String label, double value, double maxVal, Color color, double eased) {
    final height = (value.abs() / maxVal) * 100 * eased;
    return Column(
      mainAxisAlignment: MainAxisAlignment.end,
      children: [
        Text(value.toStringAsFixed(1), style: TextStyle(fontSize: 11, fontWeight: FontWeight.bold)),
        const SizedBox(height: 4),
        Container(width: 50, height: height.clamp(4, 100), decoration: BoxDecoration(color: color, borderRadius: const BorderRadius.vertical(top: Radius.circular(6)))),
        const SizedBox(height: 4),
        Text(label, style: TextStyle(fontSize: 12)),
      ],
    );
  }
}
