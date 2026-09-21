import 'dart:math' as math;
import 'package:flutter/painting.dart';

/// Shared premium stage rendering for simulator painters — one visual
/// language for every lab: deep-space gradient sky, starfield, ground slab.
/// Call from any CustomPainter's paint() before drawing physics objects.
abstract final class StageBackdrop {
  static const skyTop = Color(0xFF0B0D24);
  static const skyMid = Color(0xFF181B45);
  static const skyLow = Color(0xFF232866);
  static const ground = Color(0xFF14163A);
  static const groundLine = Color(0xFF3E44A8);

  /// Paints sky + stars + ground. [groundY] is the track/floor height in px.
  static void paint(Canvas canvas, Size size, {required double groundY}) {
    canvas.drawRect(
      Offset.zero & size,
      Paint()
        ..shader = const LinearGradient(
          begin: Alignment.topCenter,
          end: Alignment.bottomCenter,
          colors: [skyTop, skyMid, skyLow],
          stops: [0.0, 0.75, 1.0],
        ).createShader(Offset.zero & size),
    );
    final starPaint = Paint()..color = const Color(0x33FFFFFF);
    final rng = math.Random(7); // fixed seed → stable starfield
    for (var i = 0; i < 28; i++) {
      canvas.drawCircle(
        Offset(rng.nextDouble() * size.width, rng.nextDouble() * groundY * 0.85),
        rng.nextDouble() * 1.3 + 0.4,
        starPaint,
      );
    }
    canvas.drawRect(
      Rect.fromLTRB(0, groundY, size.width, size.height),
      Paint()..color = ground,
    );
    canvas.drawLine(Offset(0, groundY), Offset(size.width, groundY),
        Paint()..color = groundLine..strokeWidth = 2);
  }
}
