import 'dart:math' as math;
import 'package:flutter/material.dart';

/// A one-shot confetti burst that plays when mounted (re-key to replay).
/// Physically simulated: particles launch upward, tumble, and fall under
/// gravity. Use behind IgnorePointer over any celebratory moment.
class ConfettiBurst extends StatefulWidget {
  final double size;
  const ConfettiBurst({super.key, this.size = 160});

  @override
  State<ConfettiBurst> createState() => _ConfettiBurstState();
}

class _ConfettiBurstState extends State<ConfettiBurst>
    with SingleTickerProviderStateMixin {
  late final AnimationController _c;
  late final List<_Particle> _particles;

  static const _colors = [
    Color(0xFF4F46E5),
    Color(0xFFF59E0B),
    Color(0xFF16A34A),
    Color(0xFFF97316),
    Color(0xFF38BDF8),
    Color(0xFFDB2777),
  ];

  @override
  void initState() {
    super.initState();
    final rng = math.Random();
    _particles = List.generate(26, (i) {
      final angle = -math.pi / 2 + (rng.nextDouble() - 0.5) * math.pi * 0.9;
      final speed = 90 + rng.nextDouble() * 150;
      return _Particle(
        vx: speed * math.cos(angle),
        vy: speed * math.sin(angle),
        color: _colors[i % _colors.length],
        spin: (rng.nextDouble() - 0.5) * 14,
        size: 4 + rng.nextDouble() * 4,
        isRect: rng.nextBool(),
      );
    });
    _c = AnimationController(vsync: this, duration: const Duration(milliseconds: 950))
      ..forward();
  }

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return IgnorePointer(
      child: AnimatedBuilder(
        animation: _c,
        builder: (_, __) => CustomPaint(
          size: Size(widget.size, widget.size),
          painter: _ConfettiPainter(_particles, _c.value),
        ),
      ),
    );
  }
}

class _Particle {
  final double vx, vy, spin, size;
  final Color color;
  final bool isRect;
  _Particle({
    required this.vx,
    required this.vy,
    required this.color,
    required this.spin,
    required this.size,
    required this.isRect,
  });
}

class _ConfettiPainter extends CustomPainter {
  final List<_Particle> particles;
  final double t;
  static const double _g = 260;

  _ConfettiPainter(this.particles, this.t);

  @override
  void paint(Canvas canvas, Size size) {
    final origin = Offset(size.width / 2, size.height * 0.7);
    final fade = t < 0.7 ? 1.0 : (1 - (t - 0.7) / 0.3);
    for (final p in particles) {
      final x = origin.dx + p.vx * t;
      final y = origin.dy + p.vy * t + 0.5 * _g * t * t;
      final paint = Paint()..color = p.color.withValues(alpha: fade.clamp(0, 1));
      canvas.save();
      canvas.translate(x, y);
      canvas.rotate(p.spin * t);
      if (p.isRect) {
        canvas.drawRect(
            Rect.fromCenter(center: Offset.zero, width: p.size, height: p.size * 0.6),
            paint);
      } else {
        canvas.drawCircle(Offset.zero, p.size / 2, paint);
      }
      canvas.restore();
    }
  }

  @override
  bool shouldRepaint(_ConfettiPainter old) => old.t != t;
}
