import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A resizable rectangle: drag length and breadth sliders and watch the
/// shape animate smoothly to its new size, with perimeter and area
/// updating together as the edges stretch.
class PerimeterAreaSimulationWidget extends StatefulWidget {
  const PerimeterAreaSimulationWidget({super.key});

  @override
  State<PerimeterAreaSimulationWidget> createState() => _PerimeterAreaSimulationWidgetState();
}

class _PerimeterAreaSimulationWidgetState extends State<PerimeterAreaSimulationWidget> with SingleTickerProviderStateMixin {
  double _length = 8;
  double _breadth = 5;
  double _prevLength = 8;
  double _prevBreadth = 5;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 350));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final perimeter = 2 * (_length + _breadth);
    final area = _length * _breadth;

    return SimFrame(
      title: 'Perimeter & Area of a Rectangle',
      icon: Icons.crop_square,
      accent: Colors.blue.shade700,
      description: 'Resize the rectangle and watch it stretch smoothly, while perimeter (the boundary) and area (the surface) change.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 160,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.blue.shade50, borderRadius: BorderRadius.circular(10)),
            child: Center(
              child: AnimatedBuilder(
                animation: _controller,
                builder: (context, _) {
                  final eased = Curves.easeInOut.transform(_controller.value);
                  final animLength = _prevLength + (_length - _prevLength) * eased;
                  final animBreadth = _prevBreadth + (_breadth - _prevBreadth) * eased;
                  final animArea = animLength * animBreadth;
                  return Container(
                    width: animLength * 15,
                    height: animBreadth * 15,
                    decoration: BoxDecoration(color: Colors.blue.shade300, border: Border.all(color: Colors.blue.shade800, width: 2)),
                    alignment: Alignment.center,
                    child: Text('${animArea.toStringAsFixed(0)} cm²', style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold)),
                  );
                },
              ),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Length', value: '${_length.toStringAsFixed(0)} cm'),
            SimMetric(label: 'Breadth', value: '${_breadth.toStringAsFixed(0)} cm'),
            SimMetric(label: 'Perimeter', value: '${perimeter.toStringAsFixed(0)} cm', color: Colors.deepOrange),
          ]),
          const SizedBox(height: 4),
          Center(child: Text('Area = ${area.toStringAsFixed(0)} cm²', style: TextStyle(fontWeight: FontWeight.bold, color: Colors.blue.shade800))),
          const SizedBox(height: 14),
          SimSlider(label: 'Length: ${_length.toStringAsFixed(0)} cm', value: _length, min: 2, max: 15, divisions: 13, activeColor: Colors.blue, onChanged: (v) => setState(() {
            _prevLength = _length;
            _prevBreadth = _breadth;
            _length = v;
            _controller.forward(from: 0);
          })),
          SimSlider(label: 'Breadth: ${_breadth.toStringAsFixed(0)} cm', value: _breadth, min: 2, max: 10, divisions: 8, activeColor: Colors.teal, onChanged: (v) => setState(() {
            _prevLength = _length;
            _prevBreadth = _breadth;
            _breadth = v;
            _controller.forward(from: 0);
          })),
        ],
      ),
    );
  }
}
