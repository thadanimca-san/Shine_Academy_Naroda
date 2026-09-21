import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Newton's Second Law sandbox: an applied force pushes a block against
/// friction. Students see the net force, resulting acceleration, and the
/// block visibly speed up, crawl, or stay put.
class ForceSimulationWidget extends StatefulWidget {
  const ForceSimulationWidget({super.key});

  @override
  State<ForceSimulationWidget> createState() => _ForceSimulationWidgetState();
}

class _ForceSimulationWidgetState extends State<ForceSimulationWidget> with SingleTickerProviderStateMixin {
  double _mass = 5.0; // kg
  double _appliedForce = 20.0; // N
  double _friction = 5.0; // N (opposing force, constant kinetic friction)
  late AnimationController _controller;
  double _blockX = 0.0; // 0..1 position on track
  double _velocity = 0.0;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(days: 1))
      ..addListener(_tick);
  }

  double get _netForce {
    final raw = _appliedForce - _friction;
    // friction cannot reverse motion from rest; if applied < friction and at rest, net = 0
    if (_velocity.abs() < 0.001 && _appliedForce <= _friction) return 0;
    return raw;
  }

  double get _acceleration => _netForce / _mass;

  double _lastTickMs = 0;
  void _tick() {
    final nowMs = _controller.lastElapsedDuration?.inMilliseconds.toDouble() ?? 0;
    if (_lastTickMs == 0) {
      _lastTickMs = nowMs;
      return;
    }
    final dt = (nowMs - _lastTickMs) / 1000.0;
    _lastTickMs = nowMs;
    setState(() {
      _velocity += _acceleration * dt;
      if (_velocity < 0) _velocity = 0;
      _blockX += _velocity * dt * 0.05;
      if (_blockX > 1.0) _blockX = 0.0; // loop the block back
    });
  }

  void _reset() {
    setState(() {
      _blockX = 0.0;
      _velocity = 0.0;
      _lastTickMs = 0;
      _controller.stop();
      _controller.reset();
    });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final isMoving = _controller.isAnimating;

    return SimFrame(
      title: "Newton's Second Law (F = ma)",
      icon: Icons.fitness_center,
      accent: Colors.deepPurple,
      description: 'Push the block with an applied force against friction and watch the net force determine its acceleration.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          SimTransport(
            isPlaying: isMoving,
            color: Colors.deepPurple,
            onPlayPause: () {
              setState(() {
                if (isMoving) {
                  _controller.stop();
                } else {
                  _lastTickMs = 0;
                  _controller.repeat();
                }
              });
            },
            onReset: _reset,
          ),
          const SizedBox(height: 14),
          LayoutBuilder(builder: (context, constraints) {
            final trackWidth = constraints.maxWidth - 60;
            return Container(
              height: 90,
              decoration: BoxDecoration(color: Colors.deepPurple.shade50, borderRadius: BorderRadius.circular(10)),
              child: Stack(
                alignment: Alignment.bottomLeft,
                children: [
                  Positioned(
                    left: 10,
                    right: 10,
                    bottom: 14,
                    child: Container(height: 3, color: Colors.brown.shade300),
                  ),
                  Positioned(
                    left: 20 + _blockX * trackWidth,
                    bottom: 16,
                    child: Container(
                      width: 46,
                      height: 46,
                      decoration: BoxDecoration(
                        color: Colors.deepPurple.shade400,
                        borderRadius: BorderRadius.circular(8),
                        boxShadow: [BoxShadow(color: Theme.of(context).colorScheme.onSurface.withOpacity(0.26), blurRadius: 4, offset: Offset(0, 2))],
                      ),
                      child: Icon(Icons.inventory_2, color: Colors.white),
                    ),
                  ),
                  if (_appliedForce > 0)
                    Positioned(
                      left: 20 + _blockX * trackWidth + 46,
                      bottom: 34,
                      child: Row(children: [
                        Container(width: (_appliedForce * 1.5).clamp(6, 90), height: 4, color: Colors.green),
                        Icon(Icons.arrow_right, color: Colors.green, size: 20),
                      ]),
                    ),
                  if (_friction > 0)
                    Positioned(
                      left: (20 + _blockX * trackWidth - (_friction * 1.5).clamp(6, 90) - 10).clamp(0, double.infinity),
                      bottom: 20,
                      child: Row(children: [
                        Icon(Icons.arrow_left, color: Colors.red, size: 16),
                        Container(width: (_friction * 1.5).clamp(6, 90), height: 3, color: Colors.red),
                      ]),
                    ),
                ],
              ),
            );
          }),
          const SizedBox(height: 4),
          Padding(
            padding: EdgeInsets.only(left: 4),
            child: Text(TrilingualService.instance.getUIText('green = applied force   •   red = friction'), style: TextStyle(fontSize: 11, color: Theme.of(context).colorScheme.onSurface.withOpacity(0.45))),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Net Force', value: '${_netForce.toStringAsFixed(1)} N', color: Colors.deepPurple),
            SimMetric(label: 'Acceleration', value: '${_acceleration.toStringAsFixed(2)} m/s²', color: Colors.teal),
            SimMetric(label: 'Velocity', value: '${_velocity.toStringAsFixed(1)} m/s', color: Colors.deepOrange),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Mass (m): ${_mass.toStringAsFixed(1)} kg',
            value: _mass,
            min: 1.0,
            max: 50.0,
            divisions: 49,
            activeColor: Colors.deepPurple,
            onChanged: (val) => setState(() => _mass = val),
          ),
          SimSlider(
            label: 'Applied Force: ${_appliedForce.toStringAsFixed(1)} N',
            value: _appliedForce,
            min: 0.0,
            max: 50.0,
            divisions: 50,
            activeColor: Colors.green,
            onChanged: (val) => setState(() => _appliedForce = val),
          ),
          SimSlider(
            label: 'Friction: ${_friction.toStringAsFixed(1)} N',
            value: _friction,
            min: 0.0,
            max: 30.0,
            divisions: 30,
            activeColor: Colors.red,
            onChanged: (val) => setState(() => _friction = val),
          ),
        ],
      ),
    );
  }
}
