import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Five adjustable bars whose heights are live data points: mean, median
/// and mode recompute instantly as you drag, so central tendency stops
/// being an abstract formula. A dashed mean line animates smoothly to
/// its new height whenever the data set changes.
class DataHandlingSimulationWidget extends StatefulWidget {
  const DataHandlingSimulationWidget({super.key});

  @override
  State<DataHandlingSimulationWidget> createState() => _DataHandlingSimulationWidgetState();
}

class _DataHandlingSimulationWidgetState extends State<DataHandlingSimulationWidget> with SingleTickerProviderStateMixin {
  List<double> _data = [4, 8, 6, 8, 3];
  double _prevMean = 5.8;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 400));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  double get _mean => _data.reduce((a, b) => a + b) / _data.length;

  double get _median {
    final sorted = [..._data]..sort();
    final mid = sorted.length ~/ 2;
    return sorted.length.isOdd ? sorted[mid] : (sorted[mid - 1] + sorted[mid]) / 2;
  }

  double get _mode {
    final counts = <double, int>{};
    for (final v in _data) {
      counts[v] = (counts[v] ?? 0) + 1;
    }
    final maxCount = counts.values.reduce((a, b) => a > b ? a : b);
    return counts.entries.firstWhere((e) => e.value == maxCount).key;
  }

  void _updateData(int i, double newVal) {
    _prevMean = _mean;
    setState(() => _data[i] = newVal);
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Mean, Median & Mode',
      icon: Icons.bar_chart,
      accent: Colors.deepPurple.shade400,
      description: 'Drag each bar to change the data set and watch the mean, median and mode update live, with the mean line animating to its new level.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SizedBox(
            height: 160,
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeOutCubic.transform(_controller.value);
                final animMean = _prevMean + (_mean - _prevMean) * eased;
                return Stack(
                  children: [
                    Positioned(
                      left: 0,
                      right: 0,
                      bottom: animMean * 8,
                      child: Row(
                        children: [
                          Expanded(child: Container(height: 1.5, color: Colors.blue.withValues(alpha: 0.6))),
                          Text('  mean ${animMean.toStringAsFixed(1)}', style: TextStyle(fontSize: 9, color: Colors.blue)),
                        ],
                      ),
                    ),
                    Row(
                      crossAxisAlignment: CrossAxisAlignment.end,
                      mainAxisAlignment: MainAxisAlignment.spaceEvenly,
                      children: _data.asMap().entries.map((entry) {
                        final i = entry.key;
                        final v = entry.value;
                        return GestureDetector(
                          onVerticalDragUpdate: (details) {
                            final newVal = (v - details.delta.dy / 8).clamp(1.0, 15.0).roundToDouble();
                            if (newVal != v) _updateData(i, newVal);
                          },
                          child: Column(
                            mainAxisAlignment: MainAxisAlignment.end,
                            children: [
                              Text(v.toStringAsFixed(0), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12)),
                              const SizedBox(height: 4),
                              Container(
                                width: 30,
                                height: v * 8,
                                decoration: BoxDecoration(color: Colors.deepPurple.shade300, borderRadius: const BorderRadius.vertical(top: Radius.circular(4))),
                              ),
                            ],
                          ),
                        );
                      }).toList(),
                    ),
                  ],
                );
              },
            ),
          ),
          const SizedBox(height: 4),
          Text(TrilingualService.instance.getUIText('Drag a bar up or down to change its value'), style: TextStyle(fontSize: 11, color: Theme.of(context).colorScheme.onSurface.withOpacity(0.45))),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Mean', value: _mean.toStringAsFixed(1), color: Colors.blue),
            SimMetric(label: 'Median', value: _median.toStringAsFixed(1), color: Colors.green),
            SimMetric(label: 'Mode', value: _mode.toStringAsFixed(0), color: Colors.deepOrange),
          ]),
          const SizedBox(height: 8),
          Center(
            child: TextButton.icon(
              onPressed: () {
                _prevMean = _mean;
                setState(() => _data = [4, 8, 6, 8, 3]);
                _controller.forward(from: 0);
              },
              icon: Icon(Icons.refresh),
              label: Text(TrilingualService.instance.getUIText('Reset Data')),
            ),
          ),
        ],
      ),
    );
  }
}
