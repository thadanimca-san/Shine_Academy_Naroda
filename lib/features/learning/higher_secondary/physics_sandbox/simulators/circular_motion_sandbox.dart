import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Circular Motion Sandbox — a ball whirling on a string in a horizontal
/// circle. Students change radius, speed and mass and watch the centripetal
/// force vector (always pointing toward the centre) and the period respond
/// live, discovering F = mv²/r = mω²r and T = 2πr/v.
class CircularMotionSandbox extends StatefulWidget {
  const CircularMotionSandbox({super.key});

  @override
  State<CircularMotionSandbox> createState() => _CircularMotionSandboxState();
}

class _CircularMotionSandboxState extends State<CircularMotionSandbox>
    with SingleTickerProviderStateMixin {
  double _r = 1.5; // metres (model radius)
  double _v = 3.0; // m/s (tangential speed)
  double _m = 0.5; // kg
  double _angle = 0;
  late final Ticker _ticker;
  Duration _last = Duration.zero;

  double get _omega => _v / _r; // rad/s
  double get _force => _m * _v * _v / _r; // N, centripetal
  double get _period => 2 * math.pi * _r / _v; // s

  double get _radiusPx => (18 * _r).clamp(30.0, 100.0);

  @override
  void initState() {
    super.initState();
    _ticker = createTicker(_tick)..start();
  }

  @override
  void dispose() {
    _ticker.dispose();
    super.dispose();
  }

  void _tick(Duration elapsed) {
    final dt = math.min((elapsed - _last).inMicroseconds / 1e6, 0.032);
    _last = elapsed;
    setState(() => _angle = (_angle + _omega * dt) % (2 * math.pi));
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 220,
          decoration: BoxDecoration(
            gradient: const LinearGradient(
              begin: Alignment.topCenter,
              end: Alignment.bottomCenter,
              colors: [StageBackdrop.skyTop, StageBackdrop.skyMid, StageBackdrop.skyLow],
              stops: [0.0, 0.75, 1.0],
            ),
            borderRadius: BorderRadius.circular(Corner.lg),
          ),
          clipBehavior: Clip.antiAlias,
          child: CustomPaint(
            painter: _CircularPainter(radius: _radiusPx, angle: _angle),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('Centripetal F = mv²/r', _force.toStringAsFixed(2), 'N',
                  const Color(0xFF38BDF8))),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Period T = 2πr/v', _period.toStringAsFixed(2), 's', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Radius r', _r, 0.5, 3.0, 'm', const Color(0xFF16A34A),
            (x) => setState(() => _r = x)),
        _slider('Speed v', _v, 0.5, 8.0, 'm/s', const Color(0xFF38BDF8),
            (x) => setState(() => _v = x)),
        _slider('Mass m', _m, 0.1, 2.0, 'kg', Palette.accent, (x) => setState(() => _m = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: the blue arrow always points from the ball straight to the centre — never outward. That inward pull is the ONLY real force keeping the ball on the circle; nothing pushes it out. Raise v and watch F = mv²/r shoot up much faster than v itself (it depends on v²).'),
            style: Type.caption.copyWith(color: Palette.primaryDeep),
          ),
        ),
      ],
    );
  }

  Widget _meter(String label, String value, String unit, Color color) {
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
          const SizedBox(height: 6),
          Text('$value $unit',
              style: Type.bodyStrong.copyWith(fontSize: 16, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max, String unit, Color color,
      ValueChanged<double> onChanged) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('$label = ${value.toStringAsFixed(2)} $unit',
            style: Type.caption.copyWith(fontSize: 12, fontWeight: FontWeight.w600)),
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

class _CircularPainter extends CustomPainter {
  final double radius, angle;
  _CircularPainter({required this.radius, required this.angle});

  @override
  void paint(Canvas canvas, Size size) {
    final c = Offset(size.width / 2, size.height / 2);

    // Orbit circle (string path).
    canvas.drawCircle(
        c,
        radius,
        Paint()
          ..color = const Color(0x554F46E5)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2);

    // Ball position.
    final pos = c + Offset(radius * math.cos(angle), radius * math.sin(angle));

    // String from centre pivot to ball.
    canvas.drawLine(c, pos, Paint()..color = const Color(0x66FFFFFF)..strokeWidth = 1.6);

    // Pivot post.
    canvas.drawCircle(c, 4, Paint()..color = Colors.white70);

    // Ball.
    canvas.drawCircle(pos, 10, Paint()..color = Palette.accent);
    canvas.drawCircle(
        pos, 10, Paint()..color = Colors.white24..style = PaintingStyle.stroke..strokeWidth = 1.5);

    // Velocity (tangent) arrow.
    final tangent = Offset(-math.sin(angle), math.cos(angle));
    _arrow(canvas, pos, pos + tangent * 34, const Color(0xFF16A34A), 2.5);
    _label(canvas, 'v', pos + tangent * 46, const Color(0xFF16A34A), 11);

    // Centripetal force arrow — ALWAYS toward centre.
    final toCentre = c - pos;
    final u = toCentre / toCentre.distance;
    _arrow(canvas, pos, pos + u * 30, const Color(0xFF38BDF8), 3);
    _label(canvas, 'F', pos + u * 44, const Color(0xFF38BDF8), 12);

    _label(canvas, 'F always points to centre — never outward', Offset(size.width / 2, 16),
        Colors.white70, 10.5);
  }

  void _arrow(Canvas canvas, Offset a, Offset b, Color color, double w) {
    final p = Paint()
      ..color = color
      ..strokeWidth = w
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(a, b, p);
    final dir = b - a;
    final len = dir.distance;
    if (len < 1) return;
    final un = dir / len;
    final n = Offset(-un.dy, un.dx);
    canvas.drawLine(b, b - un * 9 + n * 4, p);
    canvas.drawLine(b, b - un * 9 - n * 4, p);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style:
              TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_CircularPainter old) => old.radius != radius || old.angle != angle;
}
