import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A particle-physics style demo of solid, liquid and gas: raising the
/// temperature slider makes particles vibrate faster, break free of their
/// lattice, and eventually fly apart — the same idea NCERT's "Matter in
/// Our Surroundings" chapter describes with static diagrams.
class StatesOfMatterSimulationWidget extends StatefulWidget {
  const StatesOfMatterSimulationWidget({super.key});

  @override
  State<StatesOfMatterSimulationWidget> createState() => _StatesOfMatterSimulationWidgetState();
}

class _Particle {
  Offset base;
  Offset pos;
  Offset velocity;
  _Particle(this.base) : pos = base, velocity = Offset.zero;
}

class _StatesOfMatterSimulationWidgetState extends State<StatesOfMatterSimulationWidget> with SingleTickerProviderStateMixin {
  double _temperature = 20; // -50..150 marks solid/liquid/gas ranges
  late AnimationController _controller;
  final List<_Particle> _particles = [];
  final math.Random _rand = math.Random(7);
  Size _lastSize = Size.zero;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 16))
      ..addListener(_step)
      ..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  String get _state {
    if (_temperature < 0) return 'Solid';
    if (_temperature < 100) return 'Liquid';
    return 'Gas';
  }

  void _initParticles(Size size) {
    _particles.clear();
    const cols = 7, rows = 4;
    final spacingX = size.width / (cols + 1);
    final spacingY = size.height / (rows + 1);
    for (int r = 0; r < rows; r++) {
      for (int c = 0; c < cols; c++) {
        _particles.add(_Particle(Offset(spacingX * (c + 1), spacingY * (r + 1))));
      }
    }
    _lastSize = size;
  }

  void _step() {
    if (_particles.isEmpty) return;
    setState(() {
      final speedFactor = (0.2 + (_temperature + 50) / 200).clamp(0.2, 3.0);
      for (final p in _particles) {
        if (_state == 'Solid') {
          // vibrate around lattice point
          final angle = _rand.nextDouble() * 2 * math.pi;
          final jitter = speedFactor * 1.2;
          p.pos = p.base + Offset(math.cos(angle) * jitter, math.sin(angle) * jitter);
        } else if (_state == 'Liquid') {
          p.velocity += Offset((_rand.nextDouble() - 0.5) * speedFactor, (_rand.nextDouble() - 0.5) * speedFactor);
          p.velocity = Offset(p.velocity.dx.clamp(-2.5, 2.5), p.velocity.dy.clamp(-2.5, 2.5));
          p.pos += p.velocity;
          p.pos = Offset(p.pos.dx.clamp(6, _lastSize.width - 6), p.pos.dy.clamp(6, _lastSize.height - 6));
        } else {
          p.velocity += Offset((_rand.nextDouble() - 0.5) * speedFactor, (_rand.nextDouble() - 0.5) * speedFactor);
          p.velocity = Offset(p.velocity.dx.clamp(-6, 6), p.velocity.dy.clamp(-6, 6));
          p.pos += p.velocity;
          double x = p.pos.dx, y = p.pos.dy, vx = p.velocity.dx, vy = p.velocity.dy;
          if (x < 4 || x > _lastSize.width - 4) vx = -vx;
          if (y < 4 || y > _lastSize.height - 4) vy = -vy;
          p.velocity = Offset(vx, vy);
          p.pos = Offset(x.clamp(4, _lastSize.width - 4), y.clamp(4, _lastSize.height - 4));
        }
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    final stateColor = _state == 'Solid' ? Colors.blue : (_state == 'Liquid' ? Colors.teal : Colors.deepOrange);

    return SimFrame(
      title: 'States of Matter',
      icon: Icons.grain,
      accent: Colors.cyan.shade800,
      description: 'Heat energy increases particle motion — from a fixed vibrating lattice (solid), to free-flowing (liquid), to widely spread (gas).',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          LayoutBuilder(builder: (context, constraints) {
            final size = Size(constraints.maxWidth, 170);
            if (_lastSize != size) {
              WidgetsBinding.instance.addPostFrameCallback((_) {
                if (mounted) _initParticles(size);
              });
            }
            return Container(
              height: 170,
              width: double.infinity,
              decoration: BoxDecoration(
                color: Colors.blueGrey.shade900,
                borderRadius: BorderRadius.circular(10),
              ),
              child: CustomPaint(
                size: size,
                painter: _ParticleFieldPainter(_particles, stateColor),
              ),
            );
          }),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Temperature', value: '${_temperature.toStringAsFixed(0)} °C'),
            SimMetric(label: 'State', value: _state, color: stateColor),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Temperature',
            value: _temperature,
            min: -50,
            max: 150,
            divisions: 40,
            activeColor: stateColor,
            onChanged: (val) => setState(() => _temperature = val),
          ),
          const SizedBox(height: 4),
          Text(TrilingualService.instance.getUIText('< 0°C solid   •   0–100°C liquid   •   > 100°C gas'), style: TextStyle(fontSize: 11, color: Theme.of(context).colorScheme.onSurface.withOpacity(0.45))),
        ],
      ),
    );
  }
}

class _ParticleFieldPainter extends CustomPainter {
  final List<_Particle> particles;
  final Color color;

  _ParticleFieldPainter(this.particles, this.color);

  @override
  void paint(Canvas canvas, Size size) {
    final paint = Paint()..color = color;
    for (final p in particles) {
      canvas.drawCircle(p.pos, 6, paint);
    }
  }

  @override
  bool shouldRepaint(covariant _ParticleFieldPainter oldDelegate) => true;
}
