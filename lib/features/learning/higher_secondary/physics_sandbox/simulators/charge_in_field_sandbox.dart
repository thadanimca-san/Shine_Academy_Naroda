import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Charge-in-Field Sandbox — a charge circling in a uniform magnetic field.
///
/// The charge moves on a circle of radius r = mv/qB. Students change mass,
/// speed, charge and field and watch the radius and period respond live,
/// discovering that the period T = 2πm/qB does NOT depend on speed.
class ChargeInFieldSandbox extends StatefulWidget {
  const ChargeInFieldSandbox({super.key});

  @override
  State<ChargeInFieldSandbox> createState() => _ChargeInFieldSandboxState();
}

class _ChargeInFieldSandboxState extends State<ChargeInFieldSandbox>
    with SingleTickerProviderStateMixin {
  double _m = 1.0; // relative mass units
  double _v = 3.0; // relative speed units
  double _q = 1.0; // relative charge units
  double _b = 1.0; // relative field units
  double _angle = 0; // current phase on the circle
  late final Ticker _ticker;
  Duration _last = Duration.zero;

  // radius (pixels) proportional to mv/qB, period ∝ m/qB
  double get _radiusPx => (28 * _m * _v / (_q * _b)).clamp(12.0, 92.0);
  double get _omega => (_q * _b / _m); // angular speed ∝ qB/m
  double get _periodModel => 2 * math.pi * _m / (_q * _b);

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
          height: 210,
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
            painter: _OrbitPainter(radius: _radiusPx, angle: _angle),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Radius  r = mv/qB',
              (_m * _v / (_q * _b)).toStringAsFixed(2), '(rel)', Palette.primary)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Period  T = 2πm/qB',
              _periodModel.toStringAsFixed(2), '(rel)', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Mass m', _m, 0.5, 3, '', const Color(0xFF38BDF8),
            (x) => setState(() => _m = x)),
        _slider('Speed v', _v, 1, 6, '', const Color(0xFF16A34A),
            (x) => setState(() => _v = x)),
        _slider('Charge q', _q, 0.5, 3, '', Palette.accent,
            (x) => setState(() => _q = x)),
        _slider('Field B', _b, 0.5, 3, '', const Color(0xFFF97316),
            (x) => setState(() => _b = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: raise v and the circle GROWS but the dot still comes round in the same time — the period T = 2πm/qB is independent of speed. That is the secret behind the cyclotron.'),
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
              style: Type.bodyStrong.copyWith(
                  fontSize: 16, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max, String unit,
      Color color, ValueChanged<double> onChanged) {
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

class _OrbitPainter extends CustomPainter {
  final double radius, angle;
  _OrbitPainter({required this.radius, required this.angle});

  @override
  void paint(Canvas canvas, Size size) {
    final c = Offset(size.width / 2, size.height / 2);

    // Field region: crosses = B into the screen.
    final crossPaint = Paint()
      ..color = const Color(0x33F97316)
      ..strokeWidth = 1.4;
    for (double x = 26; x < size.width; x += 44) {
      for (double y = 24; y < size.height; y += 42) {
        canvas.drawLine(Offset(x - 3, y - 3), Offset(x + 3, y + 3), crossPaint);
        canvas.drawLine(Offset(x - 3, y + 3), Offset(x + 3, y - 3), crossPaint);
      }
    }
    _label(canvas, 'B into screen ⊗', Offset(size.width / 2, 14),
        const Color(0xFFF97316), 10);

    // Orbit circle.
    canvas.drawCircle(c, radius, Paint()
      ..color = const Color(0x554F46E5)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2);

    // Charge on the circle.
    final pos = c + Offset(radius * math.cos(angle), radius * math.sin(angle));
    canvas.drawCircle(pos, 8, Paint()..color = Palette.accent);

    // Velocity (tangent) and force (toward centre) arrows.
    final tangent = Offset(-math.sin(angle), math.cos(angle));
    _arrow(canvas, pos, pos + tangent * 30, const Color(0xFF16A34A), 2.5);
    _label(canvas, 'v', pos + tangent * 40, const Color(0xFF16A34A), 11);
    final toCentre = (c - pos);
    final u = toCentre / toCentre.distance;
    _arrow(canvas, pos, pos + u * 26, const Color(0xFF38BDF8), 2.5);
    _label(canvas, 'F', pos + u * 38, const Color(0xFF38BDF8), 11);

    // Radius line.
    canvas.drawLine(c, pos, Paint()
      ..color = const Color(0x334F46E5)
      ..strokeWidth = 1);
    canvas.drawCircle(c, 2.5, Paint()..color = Colors.white54);
  }

  void _arrow(Canvas canvas, Offset a, Offset b, Color color, double w) {
    final p = Paint()..color = color..strokeWidth = w..strokeCap = StrokeCap.round;
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
          style: TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_OrbitPainter old) => old.radius != radius || old.angle != angle;
}
