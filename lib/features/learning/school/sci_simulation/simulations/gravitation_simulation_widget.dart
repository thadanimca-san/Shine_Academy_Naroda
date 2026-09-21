import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Two linked demos for the Gravitation chapter: a free-fall drop under
/// g = 9.8 m/s², and an Archimedes'-principle buoyancy tank where an
/// object floats, sinks, or hangs suspended based on relative density.
class GravitationSimulationWidget extends StatefulWidget {
  const GravitationSimulationWidget({super.key});

  @override
  State<GravitationSimulationWidget> createState() => _GravitationSimulationWidgetState();
}

class _GravitationSimulationWidgetState extends State<GravitationSimulationWidget> with SingleTickerProviderStateMixin {
  bool _showBuoyancy = false;

  // Free fall state
  double _height = 20.0; // m
  late AnimationController _fallController;

  // Buoyancy state
  double _objectDensity = 0.6; // relative to water (1.0)

  @override
  void initState() {
    super.initState();
    _fallController = AnimationController(vsync: this, duration: _fallDuration);
  }

  Duration get _fallDuration {
    final t = math.sqrt(2 * _height / 9.8);
    return Duration(milliseconds: (t * 1000).clamp(300, 8000).round());
  }

  @override
  void dispose() {
    _fallController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Gravitation Lab',
      icon: Icons.public,
      accent: Colors.brown,
      description: 'Explore free fall under gravity, and how buoyancy decides whether objects float or sink.',
      actions: [
        ToggleButtons(
          isSelected: [!_showBuoyancy, _showBuoyancy],
          onPressed: (i) => setState(() => _showBuoyancy = i == 1),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.brown,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 60),
          children: [Text(TrilingualService.instance.getUIText('Free Fall')), Text(TrilingualService.instance.getUIText('Buoyancy'))],
        ),
      ],
      child: _showBuoyancy ? _buildBuoyancy() : _buildFreeFall(),
    );
  }

  Widget _buildFreeFall() {
    return AnimatedBuilder(
      animation: _fallController,
      builder: (context, _) {
        final totalT = _fallDuration.inMilliseconds / 1000.0;
        final t = _fallController.value * totalT;
        final fallen = 0.5 * 9.8 * t * t;
        final v = 9.8 * t;
        final progress = _height > 0 ? (fallen / _height).clamp(0.0, 1.0) : 0.0;

        return Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            SimTransport(
              isPlaying: _fallController.isAnimating,
              color: Colors.brown,
              onPlayPause: () {
                setState(() {
                  if (_fallController.isAnimating) {
                    _fallController.stop();
                  } else {
                    if (_fallController.isCompleted) _fallController.value = 0;
                    _fallController.duration = _fallDuration;
                    _fallController.forward();
                  }
                });
              },
              onReset: () => setState(() => _fallController.value = 0),
            ),
            const SizedBox(height: 12),
            LayoutBuilder(builder: (context, constraints) {
              const towerHeight = 180.0;
              return Container(
                height: towerHeight,
                width: double.infinity,
                decoration: BoxDecoration(
                  gradient: LinearGradient(colors: [Colors.blue.shade50, Colors.brown.shade100], begin: Alignment.topCenter, end: Alignment.bottomCenter),
                  borderRadius: BorderRadius.circular(10),
                ),
                child: Stack(
                  children: [
                    Positioned(
                      left: 0,
                      right: 0,
                      top: 8 + progress * (towerHeight - 46),
                      child: const Center(child: Icon(Icons.circle, color: Colors.brown, size: 28)),
                    ),
                    Positioned(bottom: 4, left: 0, right: 0, child: Container(height: 4, color: Colors.brown.shade700)),
                  ],
                ),
              );
            }),
            const SizedBox(height: 12),
            SimMetricPanel(metrics: [
              SimMetric(label: 'Time', value: '${t.toStringAsFixed(2)} s'),
              SimMetric(label: 'Fallen', value: '${fallen.toStringAsFixed(1)} m', color: Colors.teal),
              SimMetric(label: 'Velocity', value: '${v.toStringAsFixed(1)} m/s', color: Colors.deepOrange),
            ]),
            const SizedBox(height: 14),
            SimSlider(
              label: 'Drop height: ${_height.toStringAsFixed(0)} m',
              value: _height,
              min: 5,
              max: 100,
              divisions: 19,
              activeColor: Colors.brown,
              onChanged: (val) => setState(() {
                _height = val;
                _fallController.value = 0;
              }),
            ),
          ],
        );
      },
    );
  }

  Widget _buildBuoyancy() {
    final waterDensity = 1.0;
    final relative = _objectDensity / waterDensity;
    String verdict;
    double restY; // 0 (top) .. 1 (bottom) fraction within tank
    if (relative < 0.97) {
      verdict = 'Floats — object density is less than water';
      restY = 0.15 + relative * 0.25;
    } else if (relative > 1.03) {
      verdict = 'Sinks — object density is greater than water';
      restY = 0.85;
    } else {
      verdict = 'Suspended — densities are nearly equal';
      restY = 0.5;
    }

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        LayoutBuilder(builder: (context, constraints) {
          const tankHeight = 180.0;
          return Container(
            height: tankHeight,
            width: double.infinity,
            decoration: BoxDecoration(
              color: Colors.blue.shade100,
              border: Border.all(color: Colors.blue.shade300, width: 2),
              borderRadius: BorderRadius.circular(10),
            ),
            child: AnimatedAlign(
              duration: const Duration(milliseconds: 400),
              curve: Curves.easeOut,
              alignment: Alignment(0, -1 + restY * 2),
              child: Container(
                width: 44,
                height: 44,
                decoration: BoxDecoration(
                  color: Colors.orange.shade700,
                  shape: BoxShape.circle,
                  boxShadow: [BoxShadow(color: Theme.of(context).colorScheme.onSurface.withOpacity(0.26), blurRadius: 4)],
                ),
                child: Center(
                  child: Text(relative.toStringAsFixed(1), style: TextStyle(color: Colors.white, fontWeight: FontWeight.bold, fontSize: 11)),
                ),
              ),
            ),
          );
        }),
        const SizedBox(height: 12),
        SimMetricPanel(metrics: [
          SimMetric(label: 'Object density', value: '${_objectDensity.toStringAsFixed(2)} g/cc', color: Colors.orange),
          SimMetric(label: 'Water density', value: '1.00 g/cc', color: Colors.blue),
        ]),
        const SizedBox(height: 8),
        Text(verdict, style: TextStyle(fontWeight: FontWeight.w600)),
        const SizedBox(height: 14),
        SimSlider(
          label: 'Object density (relative to water)',
          value: _objectDensity,
          min: 0.1,
          max: 2.0,
          divisions: 38,
          activeColor: Colors.orange,
          onChanged: (val) => setState(() => _objectDensity = val),
        ),
      ],
    );
  }
}
