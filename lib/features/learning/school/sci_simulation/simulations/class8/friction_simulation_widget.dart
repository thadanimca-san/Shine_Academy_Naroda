import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Push a block across surfaces of different roughness and see how far it
/// slides before friction brings it to rest — rougher surfaces mean more
/// friction and a shorter slide.
class FrictionSimulationWidget extends StatefulWidget {
  const FrictionSimulationWidget({super.key});

  @override
  State<FrictionSimulationWidget> createState() => _FrictionSimulationWidgetState();
}

class _FrictionSimulationWidgetState extends State<FrictionSimulationWidget> with SingleTickerProviderStateMixin {
  double _roughness = 0.4; // 0 = ice-smooth, 1 = very rough
  bool _useWheels = false;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: _slideDuration);
  }

  Duration get _slideDuration {
    final effectiveFriction = _useWheels ? _roughness * 0.3 : _roughness;
    final ms = (600 + effectiveFriction * 2200).round();
    return Duration(milliseconds: ms);
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  double get _slideFraction {
    final effectiveFriction = _useWheels ? _roughness * 0.3 : _roughness;
    return (1.0 - effectiveFriction * 0.85).clamp(0.08, 1.0);
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Friction Track',
      icon: Icons.speed,
      accent: Colors.brown.shade600,
      description: 'Give the block a push and see how surface roughness — and rolling on wheels — changes how far it slides.',
      actions: [
        AnimatedBuilder(
          animation: _controller,
          builder: (context, _) => IconButton(
            icon: Icon(_controller.isAnimating ? Icons.pause_circle : Icons.play_circle, color: Colors.brown, size: 30),
            onPressed: () {
              setState(() {
                if (_controller.isAnimating) {
                  _controller.stop();
                } else {
                  _controller.duration = _slideDuration;
                  _controller.forward(from: 0);
                }
              });
            },
          ),
        ),
      ],
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          final progress = Curves.decelerate.transform(_controller.value) * _slideFraction;
          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              LayoutBuilder(builder: (context, constraints) {
                final trackWidth = constraints.maxWidth - 60;
                return Container(
                  height: 80,
                  decoration: BoxDecoration(
                    color: Color.lerp(Colors.blue.shade50, Colors.brown.shade200, _roughness),
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Stack(
                    alignment: Alignment.bottomLeft,
                    children: [
                      Positioned(
                        left: 20 + progress * trackWidth,
                        bottom: 14,
                        child: Icon(_useWheels ? Icons.airport_shuttle : Icons.inventory_2, size: 40, color: Colors.brown.shade800),
                      ),
                    ],
                  ),
                );
              }),
              const SizedBox(height: 12),
              SimMetricPanel(metrics: [
                SimMetric(label: 'Friction type', value: _useWheels ? 'Rolling' : 'Sliding', color: Colors.deepOrange),
                SimMetric(label: 'Surface', value: _roughness < 0.3 ? 'Smooth' : (_roughness < 0.7 ? 'Medium' : 'Rough'), color: Colors.brown),
              ]),
              const SizedBox(height: 14),
              SwitchListTile(
                contentPadding: EdgeInsets.zero,
                title: Text(TrilingualService.instance.getUIText('Use wheels (rolling friction)'), style: TextStyle(fontSize: 13)),
                value: _useWheels,
                activeColor: Colors.brown,
                onChanged: (val) => setState(() => _useWheels = val),
              ),
              SimSlider(
                label: 'Surface roughness: ${(_roughness * 100).toStringAsFixed(0)}%',
                value: _roughness,
                min: 0.05,
                max: 1.0,
                divisions: 19,
                activeColor: Colors.brown,
                onChanged: (val) => setState(() => _roughness = val),
              ),
            ],
          );
        },
      ),
    );
  }
}
