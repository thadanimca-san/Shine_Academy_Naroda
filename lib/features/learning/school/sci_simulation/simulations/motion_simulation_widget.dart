import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'common/graph_painter.dart';

/// Animates a runner accelerating along a track and plots live
/// distance-time and velocity-time graphs so students can connect the
/// equations of motion (v = u + at, s = ut + 1/2at²) to what they see move.
class MotionSimulationWidget extends StatefulWidget {
  const MotionSimulationWidget({super.key});

  @override
  State<MotionSimulationWidget> createState() => _MotionSimulationWidgetState();
}

class _MotionSimulationWidgetState extends State<MotionSimulationWidget> with SingleTickerProviderStateMixin {
  double _u = 0.0; // initial velocity m/s
  double _a = 2.0; // acceleration m/s^2
  double _duration = 5.0; // total time modelled, s
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: Duration(milliseconds: (_duration * 1000).round()));
  }

  @override
  void didUpdateWidget(covariant MotionSimulationWidget oldWidget) {
    super.didUpdateWidget(oldWidget);
  }

  void _syncDuration() {
    final wasAnimating = _controller.isAnimating;
    _controller.duration = Duration(milliseconds: (_duration * 1000).round());
    if (wasAnimating) _controller.repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  double _distanceAt(double t) => _u * t + 0.5 * _a * t * t;
  double _velocityAt(double t) => _u + _a * t;

  @override
  Widget build(BuildContext context) {
    final maxDistance = _distanceAt(_duration).abs().clamp(0.1, double.infinity);
    final maxVelocity = [_u.abs(), _velocityAt(_duration).abs()].reduce(math.max).clamp(0.1, double.infinity);

    return SimFrame(
      title: 'Motion Simulator',
      icon: Icons.directions_run,
      accent: Colors.indigo,
      description: 'Watch how initial velocity and acceleration shape the distance-time and velocity-time graphs.',
      child: AnimatedBuilder(
        animation: _controller,
        builder: (context, _) {
          final t = _controller.value * _duration;
          final s = _distanceAt(t);
          final v = _velocityAt(t);

          final distPoints = List.generate(30, (i) {
            final ti = _duration * i / 29;
            return Offset(ti / _duration, (_distanceAt(ti) / maxDistance).clamp(0.0, 1.0));
          });
          final velPoints = List.generate(30, (i) {
            final ti = _duration * i / 29;
            return Offset(ti / _duration, (_velocityAt(ti) / maxVelocity).clamp(-1.0, 1.0) * 0.5 + 0.5);
          });

          return Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              SimTransport(
                isPlaying: _controller.isAnimating,
                color: Colors.indigo,
                onPlayPause: () {
                  setState(() {
                    if (_controller.isAnimating) {
                      _controller.stop();
                    } else {
                      if (_controller.isCompleted) _controller.value = 0;
                      _controller.repeat();
                    }
                  });
                },
                onReset: () => setState(() => _controller.value = 0),
              ),
              const SizedBox(height: 14),
              // Track
              LayoutBuilder(builder: (context, constraints) {
                final trackWidth = constraints.maxWidth - 40;
                final progress = maxDistance > 0 ? (s / maxDistance).clamp(0.0, 1.0) : 0.0;
                return Container(
                  height: 70,
                  decoration: BoxDecoration(
                    color: Colors.indigo.shade50,
                    borderRadius: BorderRadius.circular(10),
                  ),
                  child: Stack(
                    alignment: Alignment.centerLeft,
                    children: [
                      Positioned(
                        left: 16,
                        right: 16,
                        child: Container(height: 3, color: Colors.indigo.shade200),
                      ),
                      AnimatedPositioned(
                        duration: Duration.zero,
                        left: 16 + progress * trackWidth,
                        child: Icon(Icons.directions_run, size: 34, color: Colors.indigo),
                      ),
                    ],
                  ),
                );
              }),
              const SizedBox(height: 12),
              SimMetricPanel(metrics: [
                SimMetric(label: 'Time (t)', value: '${t.toStringAsFixed(1)} s'),
                SimMetric(label: 'Distance (s)', value: '${s.toStringAsFixed(1)} m', color: Colors.teal),
                SimMetric(label: 'Velocity (v)', value: '${v.toStringAsFixed(1)} m/s', color: Colors.deepOrange),
              ]),
              const SizedBox(height: 14),
              Row(
                children: [
                  Expanded(child: MiniGraph(title: 'Distance vs Time', points: distPoints, color: Colors.teal, markerT: _controller.value)),
                  const SizedBox(width: 10),
                  Expanded(child: MiniGraph(title: 'Velocity vs Time', points: velPoints, color: Colors.deepOrange, markerT: _controller.value)),
                ],
              ),
              const SizedBox(height: 14),
              SimSlider(
                label: 'Initial Velocity (u): ${_u.toStringAsFixed(1)} m/s',
                value: _u,
                min: 0.0,
                max: 20.0,
                divisions: 40,
                activeColor: Colors.indigo,
                onChanged: (val) => setState(() => _u = val),
              ),
              SimSlider(
                label: 'Acceleration (a): ${_a.toStringAsFixed(1)} m/s²',
                value: _a,
                min: -5.0,
                max: 10.0,
                divisions: 30,
                activeColor: Colors.indigo,
                onChanged: (val) => setState(() => _a = val),
              ),
              SimSlider(
                label: 'Time window: ${_duration.toStringAsFixed(1)} s',
                value: _duration,
                min: 2.0,
                max: 10.0,
                divisions: 16,
                activeColor: Colors.indigo,
                onChanged: (val) => setState(() {
                  _duration = val;
                  _syncDuration();
                }),
              ),
            ],
          );
        },
      ),
    );
  }
}
