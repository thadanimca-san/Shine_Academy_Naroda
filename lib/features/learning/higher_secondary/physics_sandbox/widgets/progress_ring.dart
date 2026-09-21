import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';

/// Circular progress with animated sweep — used on chapter cards.
class ProgressRing extends StatelessWidget {
  final double progress; // 0..1
  final double size;
  final Color color;
  final Widget? center;

  const ProgressRing({
    super.key,
    required this.progress,
    this.size = 40,
    this.color = Palette.primary,
    this.center,
  });

  @override
  Widget build(BuildContext context) {
    return TweenAnimationBuilder<double>(
      tween: Tween(begin: 0, end: progress.clamp(0.0, 1.0)),
      duration: Motion.slow,
      curve: Motion.ease,
      builder: (context, value, _) => SizedBox(
        width: size,
        height: size,
        child: CustomPaint(
          painter: _RingPainter(value, color),
          child: Center(child: center),
        ),
      ),
    );
  }
}

class _RingPainter extends CustomPainter {
  final double value;
  final Color color;
  _RingPainter(this.value, this.color);

  @override
  void paint(Canvas canvas, Size size) {
    final center = size.center(Offset.zero);
    final radius = size.width / 2 - 2.5;
    final track = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3.5
      ..color = Palette.border;
    canvas.drawCircle(center, radius, track);

    if (value > 0) {
      final arc = Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = 3.5
        ..strokeCap = StrokeCap.round
        ..color = color;
      canvas.drawArc(
        Rect.fromCircle(center: center, radius: radius),
        -math.pi / 2,
        2 * math.pi * value,
        false,
        arc,
      );
    }
  }

  @override
  bool shouldRepaint(_RingPainter old) => old.value != value || old.color != color;
}
