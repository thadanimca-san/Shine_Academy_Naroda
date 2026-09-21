import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/bevel_button.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Collision Lab — two carts on a frictionless track.
///
/// Students control both masses, both initial velocities and the coefficient
/// of restitution, then watch momentum stay perfectly conserved while kinetic
/// energy survives only when e = 1. The grey marker is the center of mass:
/// it never notices the collision.
class CollisionLabSimulator extends StatefulWidget {
  const CollisionLabSimulator({super.key});

  @override
  State<CollisionLabSimulator> createState() => _CollisionLabSimulatorState();
}

class _CollisionLabSimulatorState extends State<CollisionLabSimulator>
    with SingleTickerProviderStateMixin {
  // Parameters
  double _m1 = 2.0, _m2 = 1.0; // kg
  double _u1 = 4.0, _u2 = -2.0; // m/s
  double _e = 1.0; // coefficient of restitution

  // Simulation state (world coords, metres; track is 20 m wide)
  static const double _world = 20.0;
  double _x1 = 5.0, _x2 = 15.0;
  double _v1 = 0, _v2 = 0;
  bool _running = false;
  bool _collided = false;
  double _simTime = 0;
  double? _impactAt;
  late final Ticker _ticker;
  Duration _last = Duration.zero;

  double get _halfW1 => _cartHalfWidth(_m1);
  double get _halfW2 => _cartHalfWidth(_m2);
  static double _cartHalfWidth(double m) => 0.45 + 0.22 * math.pow(m, 1 / 3);

  @override
  void initState() {
    super.initState();
    _ticker = createTicker(_tick);
    _reset();
  }

  @override
  void dispose() {
    _ticker.dispose();
    super.dispose();
  }

  void _tick(Duration elapsed) {
    final dt = math.min((elapsed - _last).inMicroseconds / 1e6, 0.032);
    _last = elapsed;
    setState(() {
      _simTime += dt;
      _x1 += _v1 * dt;
      _x2 += _v2 * dt;

      // Contact & approaching → resolve collision once.
      if (!_collided && (_x2 - _x1) <= (_halfW1 + _halfW2) && _v1 > _v2) {
        _impactAt = _simTime;
        final m1 = _m1, m2 = _m2, e = _e;
        final v1 = ((m1 - e * m2) * _v1 + (1 + e) * m2 * _v2) / (m1 + m2);
        final v2 = ((m2 - e * m1) * _v2 + (1 + e) * m1 * _v1) / (m1 + m2);
        _v1 = v1;
        _v2 = v2;
        _collided = true;
      }

      // Stop when both carts have left the visible track.
      final gone1 = _x1 < -3 || _x1 > _world + 3;
      final gone2 = _x2 < -3 || _x2 > _world + 3;
      if ((gone1 && gone2) || (_collided && _v1.abs() < 1e-6 && _v2.abs() < 1e-6)) {
        _running = false;
        _ticker.stop();
      }
    });
  }

  void _start() {
    if (_running) return;
    setState(() {
      _running = true;
      _last = Duration.zero;
    });
    _ticker.start();
  }

  void _reset() {
    _ticker.stop();
    setState(() {
      _running = false;
      _collided = false;
      _simTime = 0;
      _impactAt = null;
      _x1 = 5.0;
      _x2 = 15.0;
      _v1 = _u1;
      _v2 = _u2;
    });
  }

  // Live measurements
  double get _p => _m1 * _v1 + _m2 * _v2;
  double get _ke => 0.5 * _m1 * _v1 * _v1 + 0.5 * _m2 * _v2 * _v2;
  double get _keInitial => 0.5 * _m1 * _u1 * _u1 + 0.5 * _m2 * _u2 * _u2;

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        // ── Stage ──
        Container(
          height: 210,
          decoration: BoxDecoration(
            color: Palette.stage,
            borderRadius: BorderRadius.circular(Corner.lg),
          ),
          clipBehavior: Clip.antiAlias,
          child: CustomPaint(
            painter: _CollisionPainter(
              x1: _x1, x2: _x2, v1: _v1, v2: _v2,
              halfW1: _halfW1, halfW2: _halfW2,
              m1: _m1, m2: _m2, world: _world, collided: _collided,
              timeSinceImpact: _impactAt == null ? null : _simTime - _impactAt!,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),

        // ── Conservation meters ──
        Row(
          children: [
            Expanded(child: _meter('Momentum p', _p, _m1 * _u1 + _m2 * _u2, 'kg·m/s', Palette.primary)),
            const SizedBox(width: Gap.x3),
            Expanded(child: _meter('Kinetic energy', _ke, _keInitial, 'J', Palette.accent)),
          ],
        ),
        const SizedBox(height: Gap.x3),

        // ── Controls ──
        Row(children: [
          Expanded(child: _slider('m₁', _m1, 0.5, 8, 'kg', const Color(0xFFF97316), (v) {
            setState(() => _m1 = v);
            if (!_running) _reset();
          })),
          const SizedBox(width: Gap.x3),
          Expanded(child: _slider('m₂', _m2, 0.5, 8, 'kg', const Color(0xFF38BDF8), (v) {
            setState(() => _m2 = v);
            if (!_running) _reset();
          })),
        ]),
        Row(children: [
          Expanded(child: _slider('u₁', _u1, -6, 8, 'm/s', const Color(0xFFF97316), (v) {
            setState(() => _u1 = v);
            if (!_running) _reset();
          })),
          const SizedBox(width: Gap.x3),
          Expanded(child: _slider('u₂', _u2, -8, 6, 'm/s', const Color(0xFF38BDF8), (v) {
            setState(() => _u2 = v);
            if (!_running) _reset();
          })),
        ]),
        _slider(
          'Bounciness e  (0 = perfectly inelastic, 1 = elastic)',
          _e, 0, 1, '', Palette.primary,
          (v) => setState(() => _e = v),
        ),
        const SizedBox(height: Gap.x2),
        Row(
          children: [
            Expanded(
              child: BevelButton.go(
                label: 'Collide!',
                icon: Icons.play_arrow_rounded,
                onPressed: _running ? null : _start,
              ),
            ),
            const SizedBox(width: Gap.x3),
            BevelButton.quiet(
              label: 'Reset',
              icon: Icons.refresh_rounded,
              expanded: false,
              onPressed: _reset,
            ),
          ],
        ),
      ],
    );
  }

  Widget _meter(String label, double now, double initial, String unit, Color color) {
    final scale = math.max(initial.abs(), 1e-6);
    final frac = (now.abs() / scale).clamp(0.0, 1.2);
    return Container(
      padding: const EdgeInsets.all(Gap.x3),
      decoration: BoxDecoration(
        color: Palette.surface,
        borderRadius: BorderRadius.circular(Corner.md),
        border: Border.all(color: Palette.border),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(label.toUpperCase(), style: Type.label.copyWith(fontSize: 9)),
          const SizedBox(height: 4),
          Text('${now.toStringAsFixed(2)} $unit',
              style: Type.bodyStrong.copyWith(fontSize: 15, fontFamily: 'monospace')),
          const SizedBox(height: 6),
          ClipRRect(
            borderRadius: BorderRadius.circular(Corner.pill),
            child: LinearProgressIndicator(
              value: frac.clamp(0.0, 1.0),
              minHeight: 5,
              backgroundColor: Palette.surfaceAlt,
              color: color,
            ),
          ),
          const SizedBox(height: 3),
          Text('started at ${initial.toStringAsFixed(2)} $unit',
              style: Type.caption.copyWith(fontSize: 10)),
        ],
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max, String unit,
      Color color, ValueChanged<double> onChanged) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          unit.isEmpty
              ? '$label: ${value.toStringAsFixed(2)}'
              : '$label = ${value.toStringAsFixed(1)} $unit',
          style: Type.caption.copyWith(fontSize: 12, fontWeight: FontWeight.w600),
        ),
        SliderTheme(
          data: SliderTheme.of(context).copyWith(
            activeTrackColor: color,
            thumbColor: color,
            overlayColor: color.withValues(alpha: 0.12),
          ),
          child: Slider(value: value, min: min, max: max, onChanged: onChanged),
        ),
      ],
    );
  }
}

class _CollisionPainter extends CustomPainter {
  final double x1, x2, v1, v2, halfW1, halfW2, m1, m2, world;
  final bool collided;
  final double? timeSinceImpact;

  _CollisionPainter({
    required this.x1, required this.x2, required this.v1, required this.v2,
    required this.halfW1, required this.halfW2,
    required this.m1, required this.m2, required this.world, required this.collided,
    this.timeSinceImpact,
  });

  static const _c1 = Color(0xFFF97316);
  static const _c2 = Color(0xFF38BDF8);

  @override
  void paint(Canvas canvas, Size size) {
    final trackY = size.height * 0.68;
    double px(double x) => x / world * size.width;

    // ── Shared premium backdrop (sky, stars, ground) ──
    StageBackdrop.paint(canvas, size, groundY: trackY);
    final tick = Paint()..color = const Color(0x2EFFFFFF)..strokeWidth = 1;
    for (double m = 0; m <= world; m += 2) {
      canvas.drawLine(Offset(px(m), trackY + 4), Offset(px(m), trackY + 10), tick);
      _label(canvas, '${m.toInt()}', Offset(px(m), trackY + 18), Colors.white24, 8);
    }

    _cart(canvas, px(x1), trackY, halfW1 / world * size.width, m1, _c1, v1, x1);
    _cart(canvas, px(x2), trackY, halfW2 / world * size.width, m2, _c2, v2, x2);

    // ── Impact flash + sparks (first 0.35 s after collision) ──
    final tsi = timeSinceImpact;
    if (tsi != null && tsi < 0.35) {
      final k = tsi / 0.35;
      final cxImpact = px((x1 * m2 + x2 * m1) / (m1 + m2));
      final flashCenter = Offset(cxImpact, trackY - 22);
      canvas.drawCircle(
        flashCenter,
        10 + 42 * k,
        Paint()
          ..style = PaintingStyle.stroke
          ..strokeWidth = 3 * (1 - k)
          ..color = Colors.white.withValues(alpha: (1 - k) * 0.9),
      );
      final sparkRng = math.Random(3);
      for (var i = 0; i < 10; i++) {
        final a = sparkRng.nextDouble() * 2 * math.pi;
        final d = (14 + 46 * k) * (0.6 + sparkRng.nextDouble() * 0.4);
        canvas.drawCircle(
          flashCenter + Offset(math.cos(a) * d, math.sin(a) * d * 0.6),
          2.2 * (1 - k),
          Paint()..color = const Color(0xFFFFD166).withValues(alpha: 1 - k),
        );
      }
    }

    // ── Center of mass — sails straight through the collision ──
    final xcm = (m1 * x1 + m2 * x2) / (m1 + m2);
    final cm = Offset(px(xcm), trackY - 74);
    canvas.drawCircle(cm, 6.5, Paint()..color = const Color(0x40FFFFFF));
    canvas.drawCircle(cm, 4, Paint()..color = Colors.white70);
    canvas.drawCircle(cm, 1.8, Paint()..color = Palette.stage);
    _label(canvas, 'COM', cm + const Offset(0, -15), Colors.white54, 8.5);

    if (collided) {
      _badge(canvas, 'momentum conserved ✓', Offset(size.width / 2, 18));
    }
  }

  void _cart(Canvas canvas, double cx, double trackY, double halfWpx, double mass,
      Color color, double v, double worldX) {
    final h = 26.0 + 8.0 * math.pow(mass, 1 / 3);
    final bodyTop = trackY - h - 10;
    final body = Rect.fromLTWH(cx - halfWpx, bodyTop, halfWpx * 2, h);

    // Soft contact shadow
    canvas.drawOval(
      Rect.fromCenter(
          center: Offset(cx, trackY + 2), width: halfWpx * 2.2, height: 7),
      Paint()
        ..color = Colors.black.withValues(alpha: 0.35)
        ..maskFilter = const MaskFilter.blur(BlurStyle.normal, 3),
    );

    // Motion streak behind fast carts
    if (v.abs() > 1.5) {
      final streak = Paint()
        ..shader = LinearGradient(
          begin: v > 0 ? Alignment.centerRight : Alignment.centerLeft,
          end: v > 0 ? Alignment.centerLeft : Alignment.centerRight,
          colors: [color.withValues(alpha: 0.35), color.withValues(alpha: 0.0)],
        ).createShader(body);
      final len = (v.abs() * 6).clamp(8.0, 46.0);
      canvas.drawRRect(
        RRect.fromRectAndRadius(
          Rect.fromLTWH(v > 0 ? cx - halfWpx - len : cx + halfWpx,
              bodyTop + h * 0.25, len, h * 0.5),
          const Radius.circular(4),
        ),
        streak,
      );
    }

    // Body: vertical gradient + glossy top highlight
    final hsl = HSLColor.fromColor(color);
    final bodyPaint = Paint()
      ..shader = LinearGradient(
        begin: Alignment.topCenter,
        end: Alignment.bottomCenter,
        colors: [
          hsl.withLightness((hsl.lightness + 0.13).clamp(0.0, 1.0)).toColor(),
          color,
          hsl.withLightness((hsl.lightness - 0.12).clamp(0.0, 1.0)).toColor(),
        ],
      ).createShader(body);
    final rrect = RRect.fromRectAndRadius(body, const Radius.circular(8));
    canvas.drawRRect(rrect, bodyPaint);
    canvas.drawRRect(
      RRect.fromRectAndRadius(
          Rect.fromLTWH(body.left + 3, body.top + 2.5, body.width - 6, h * 0.28),
          const Radius.circular(6)),
      Paint()..color = Colors.white.withValues(alpha: 0.22),
    );

    // Cabin window
    canvas.drawRRect(
      RRect.fromRectAndRadius(
          Rect.fromLTWH(cx - halfWpx * 0.35, body.top + h * 0.22,
              halfWpx * 0.7, h * 0.34),
          const Radius.circular(4)),
      Paint()..color = const Color(0xCC10122B),
    );

    // Wheels with rotating spokes (angle from distance rolled)
    const wheelR = 6.0;
    final wheelAngle = worldX / (wheelR / 22); // world metres → spin
    for (final wx in [cx - halfWpx * 0.55, cx + halfWpx * 0.55]) {
      final wc = Offset(wx, trackY - 4);
      canvas.drawCircle(wc, wheelR, Paint()..color = const Color(0xFF2A2D55));
      canvas.drawCircle(wc, wheelR,
          Paint()
            ..style = PaintingStyle.stroke
            ..strokeWidth = 1.6
            ..color = const Color(0xFF565CC0));
      for (var s = 0; s < 3; s++) {
        final a = wheelAngle + s * math.pi / 1.5;
        canvas.drawLine(
          wc - Offset(math.cos(a), math.sin(a)) * (wheelR - 1.5),
          wc + Offset(math.cos(a), math.sin(a)) * (wheelR - 1.5),
          Paint()..color = const Color(0xFF8B90E8)..strokeWidth = 1.4,
        );
      }
      canvas.drawCircle(wc, 1.6, Paint()..color = const Color(0xFFB9BCF5));
    }

    // Velocity arrow + speed chip
    if (v.abs() > 0.05) {
      final y = bodyTop - 16;
      final len = (v.abs() * 9).clamp(12.0, 70.0) * v.sign;
      final p = Paint()..color = color..strokeWidth = 3..strokeCap = StrokeCap.round;
      canvas.drawLine(Offset(cx, y), Offset(cx + len, y), p);
      final tip = Offset(cx + len, y);
      final dir = v.sign;
      canvas.drawLine(tip, tip + Offset(-7 * dir, -4.5), p);
      canvas.drawLine(tip, tip + Offset(-7 * dir, 4.5), p);
      _label(canvas, '${v.toStringAsFixed(1)} m/s', Offset(cx, y - 13), color, 10);
    }
    _label(canvas, '${mass.toStringAsFixed(1)} kg',
        Offset(cx, bodyTop + h * 0.72), Colors.white, 10);
  }

  void _badge(Canvas canvas, String text, Offset center) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(
              color: Color(0xFF7EF5C1),
              fontSize: 10,
              fontWeight: FontWeight.w700,
              fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    final r = RRect.fromRectAndRadius(
      Rect.fromCenter(
          center: center, width: tp.width + 20, height: tp.height + 10),
      const Radius.circular(999),
    );
    canvas.drawRRect(r, Paint()..color = const Color(0x2E7EF5C1));
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fontSize) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(
              color: color, fontSize: fontSize, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_CollisionPainter old) =>
      old.x1 != x1 || old.x2 != x2 || old.v1 != v1 || old.v2 != v2 ||
      old.m1 != m1 || old.m2 != m2 || old.collided != collided ||
      old.timeSinceImpact != timeSinceImpact;
}
