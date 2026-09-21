import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../services/profile_service.dart';
import '../theme/tokens.dart';
import 'home_screen.dart';
import 'onboarding_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Animated brand reveal shown right after the native splash:
/// an orbiting "atom" draws itself, then Shine Academy presents
/// Physics Sandbox. Tap anywhere to skip.
class SplashScreen extends StatefulWidget {
  const SplashScreen({super.key});

  @override
  State<SplashScreen> createState() => _SplashScreenState();
}

class _SplashScreenState extends State<SplashScreen>
    with SingleTickerProviderStateMixin {
  late final AnimationController _c;
  bool _left = false;

  @override
  void initState() {
    super.initState();
    _c = AnimationController(vsync: this, duration: const Duration(milliseconds: 2600))
      ..addStatusListener((s) {
        if (s == AnimationStatus.completed) _leave();
      })
      ..forward();
  }

  void _leave() {
    if (_left || !mounted) return;
    _left = true;
    final next = const HomeScreen();
    Navigator.of(context).pushReplacement(PageRouteBuilder(
      transitionDuration: Motion.slow,
      pageBuilder: (_, __, ___) => next,
      transitionsBuilder: (_, anim, __, child) =>
          FadeTransition(opacity: anim, child: child),
    ));
  }

  @override
  void dispose() {
    _c.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return GestureDetector(
      onTap: _leave,
      child: Scaffold(
        backgroundColor: Palette.stage,
        body: AnimatedBuilder(
          animation: _c,
          builder: (context, _) {
            final t = _c.value;
            double seg(double a, double b) => ((t - a) / (b - a)).clamp(0.0, 1.0);
            final atom = Curves.easeOutCubic.transform(seg(0.0, 0.45));
            final academy = Curves.easeOut.transform(seg(0.30, 0.55));
            final title = Curves.easeOutCubic.transform(seg(0.45, 0.75));
            final tagline = Curves.easeOut.transform(seg(0.65, 0.9));

            return Center(
              child: Column(
                mainAxisAlignment: MainAxisAlignment.center,
                children: [
                  SizedBox(
                    width: 130,
                    height: 130,
                    child: CustomPaint(painter: _AtomPainter(atom, t)),
                  ),
                  const SizedBox(height: Gap.x8),
                  Opacity(
                    opacity: academy,
                    child: Text(TrilingualService.instance.getUIText('SHINE ACADEMY  ·  NARODA'),
                      style: Type.label.copyWith(
                        color: const Color(0xFF9BA3FF),
                        fontSize: 11,
                        letterSpacing: 3,
                      ),
                    ),
                  ),
                  const SizedBox(height: Gap.x3),
                  Opacity(
                    opacity: title,
                    child: Transform.translate(
                      offset: Offset(0, 14 * (1 - title)),
                      child: Text(TrilingualService.instance.getUIText('Physics Sandbox'),
                        style: Type.display.copyWith(
                          color: Colors.white,
                          fontSize: 32,
                          letterSpacing: -0.8,
                        ),
                      ),
                    ),
                  ),
                  const SizedBox(height: Gap.x3),
                  Opacity(
                    opacity: tagline,
                    child: Text(TrilingualService.instance.getUIText('where formulas are discovered, not memorized'),
                      style: Type.caption.copyWith(
                          color: Colors.white38, fontSize: 12.5, letterSpacing: 0.3),
                    ),
                  ),
                ],
              ),
            );
          },
        ),
      ),
    );
  }
}

class _AtomPainter extends CustomPainter {
  final double reveal; // 0..1 orbit draw-in
  final double t; // full timeline for electron motion
  _AtomPainter(this.reveal, this.t);

  @override
  void paint(Canvas canvas, Size size) {
    final center = size.center(Offset.zero);
    final r = size.width * 0.42;

    // Nucleus
    canvas.drawCircle(
        center, 7 * reveal, Paint()..color = const Color(0xFFF59E0B));
    canvas.drawCircle(center, 12 * reveal,
        Paint()..color = const Color(0x33F59E0B));

    // Three elliptical orbits drawing themselves in
    for (var i = 0; i < 3; i++) {
      final angle = i * math.pi / 3;
      final sweep = 2 * math.pi * reveal;
      final orbit = Paint()
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1.6
        ..color = const Color(0xFF6D74F6).withValues(alpha: 0.55);
      canvas.save();
      canvas.translate(center.dx, center.dy);
      canvas.rotate(angle);
      canvas.scale(1.0, 0.42);
      canvas.drawArc(
          Rect.fromCircle(center: Offset.zero, radius: r), -math.pi / 2, sweep,
          false, orbit);

      // Electron riding each orbit
      if (reveal > 0.6) {
        final ea = -math.pi / 2 + 2 * math.pi * ((t * 1.4 + i * 0.33) % 1.0);
        final e = Offset(r * math.cos(ea), r * math.sin(ea));
        canvas.drawCircle(e, 4.4, Paint()..color = const Color(0xFF7EF5C1));
        canvas.drawCircle(e, 8, Paint()..color = const Color(0x337EF5C1));
      }
      canvas.restore();
    }
  }

  @override
  bool shouldRepaint(_AtomPainter old) => old.reveal != reveal || old.t != t;
}
