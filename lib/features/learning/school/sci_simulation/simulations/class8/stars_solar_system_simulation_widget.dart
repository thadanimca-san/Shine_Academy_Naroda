import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Planet {
  final String name;
  final double orbitRadiusFactor; // relative
  final double relativeSpeed;
  final double size;
  final Color color;
  final String fact;

  const _Planet(this.name, this.orbitRadiusFactor, this.relativeSpeed, this.size, this.color, this.fact);
}

/// An animated orbit diagram of the Sun and inner-to-outer planets. Tap a
/// planet to learn a quick fact; speeds are exaggerated but keep the
/// relative order of orbital periods correct (closer planets orbit faster).
class StarsSolarSystemSimulationWidget extends StatefulWidget {
  const StarsSolarSystemSimulationWidget({super.key});

  @override
  State<StarsSolarSystemSimulationWidget> createState() => _StarsSolarSystemSimulationWidgetState();
}

class _StarsSolarSystemSimulationWidgetState extends State<StarsSolarSystemSimulationWidget> with SingleTickerProviderStateMixin {
  late AnimationController _controller;
  _Planet? _selected;

  static const _planets = [
    _Planet('Mercury', 0.16, 4.1, 6, Color(0xFFB0BEC5), 'The smallest planet and closest to the Sun.'),
    _Planet('Venus', 0.24, 1.6, 9, Color(0xFFFFCC80), 'The hottest planet due to its thick, heat-trapping atmosphere.'),
    _Planet('Earth', 0.33, 1.0, 9.5, Color(0xFF4FC3F7), 'The only known planet with life.'),
    _Planet('Mars', 0.42, 0.53, 7, Color(0xFFEF5350), 'Known as the Red Planet due to iron oxide on its surface.'),
    _Planet('Jupiter', 0.58, 0.084, 20, Color(0xFFFFB74D), 'The largest planet in the solar system.'),
    _Planet('Saturn', 0.74, 0.034, 17, Color(0xFFFFF176), 'Famous for its beautiful ring system.'),
    _Planet('Uranus', 0.88, 0.012, 13, Color(0xFF80DEEA), 'Rotates on its side, almost rolling along its orbit.'),
    _Planet('Neptune', 1.0, 0.006, 13, Color(0xFF5C6BC0), 'The most distant planet, with the fastest winds in the solar system.'),
  ];

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(seconds: 20))..repeat();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'The Solar System',
      icon: Icons.public,
      accent: Colors.indigo.shade700,
      description: 'Planets closer to the Sun orbit faster. Tap a planet to learn a fact about it.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              return LayoutBuilder(builder: (context, constraints) {
                final size = Size(constraints.maxWidth, 260);
                return GestureDetector(
                  onTapUp: (details) => _handleTap(details.localPosition, size),
                  child: Container(
                    height: 260,
                    width: double.infinity,
                    decoration: BoxDecoration(
                      gradient: const LinearGradient(colors: [Color(0xFF0D1333), Color(0xFF1A1F4B)], begin: Alignment.topLeft, end: Alignment.bottomRight),
                      borderRadius: BorderRadius.circular(10),
                    ),
                    child: CustomPaint(
                      size: size,
                      painter: _SolarSystemPainter(t: _controller.value, planets: _planets, selected: _selected),
                    ),
                  ),
                );
              });
            },
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _planets.map((p) {
              final isSelected = _selected?.name == p.name;
              return ActionChip(
                label: Text(p.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                backgroundColor: isSelected ? p.color : p.color.withValues(alpha: 0.25),
                onPressed: () => setState(() => _selected = p),
              );
            }).toList(),
          ),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: _selected == null
                ? Text(TrilingualService.instance.getUIText('Tap a planet to learn a quick fact.'), style: TextStyle(color: Theme.of(context).colorScheme.onSurfaceVariant, fontSize: 13))
                : Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(_selected!.name, style: TextStyle(fontWeight: FontWeight.bold, color: _selected!.color, fontSize: 14)),
                      const SizedBox(height: 4),
                      Text(_selected!.fact, style: TextStyle(fontSize: 13)),
                    ],
                  ),
          ),
        ],
      ),
    );
  }

  void _handleTap(Offset tapPos, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final maxRadius = math.min(size.width, size.height) / 2 - 14;
    for (final p in _planets) {
      final radius = maxRadius * p.orbitRadiusFactor;
      final angle = _controller.value * 2 * math.pi * p.relativeSpeed;
      final pos = center + Offset(math.cos(angle) * radius, math.sin(angle) * radius * 0.55);
      if ((pos - tapPos).distance < p.size + 8) {
        setState(() => _selected = p);
        return;
      }
    }
  }
}

class _SolarSystemPainter extends CustomPainter {
  final double t;
  final List<_Planet> planets;
  final _Planet? selected;

  _SolarSystemPainter({required this.t, required this.planets, required this.selected});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final maxRadius = math.min(size.width, size.height) / 2 - 14;

    canvas.drawCircle(center, 16, Paint()..shader = RadialGradient(colors: [Colors.yellow.shade100, Colors.orange.shade700]).createShader(Rect.fromCircle(center: center, radius: 16)));

    for (final p in planets) {
      final radius = maxRadius * p.orbitRadiusFactor;
      final orbitRect = Rect.fromCenter(center: center, width: radius * 2, height: radius * 2 * 0.55);
      canvas.drawOval(orbitRect, Paint()..color = Colors.white.withValues(alpha: 0.15)..style = PaintingStyle.stroke..strokeWidth = 1);

      final angle = t * 2 * math.pi * p.relativeSpeed;
      final pos = center + Offset(math.cos(angle) * radius, math.sin(angle) * radius * 0.55);
      final isSelected = selected?.name == p.name;
      canvas.drawCircle(pos, p.size / 2, Paint()..color = p.color);
      if (isSelected) {
        canvas.drawCircle(pos, p.size / 2 + 4, Paint()..color = Colors.white..style = PaintingStyle.stroke..strokeWidth = 1.5);
      }
    }
  }

  @override
  bool shouldRepaint(covariant _SolarSystemPainter oldDelegate) => true;
}
