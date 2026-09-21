import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Angular Momentum Sandbox — a spinning figure that can pull its "arms"
/// in or push them out. Moment of inertia I = k·m·r_arm² changes with the
/// arm-radius slider while angular momentum L = Iω is held fixed (no
/// external torque), so ω visibly speeds up as the arms come in and slows
/// down as they extend — the ice-skater effect.
class AngularMomentumSandbox extends StatefulWidget {
  const AngularMomentumSandbox({super.key});

  @override
  State<AngularMomentumSandbox> createState() => _AngularMomentumSandboxState();
}

class _AngularMomentumSandboxState extends State<AngularMomentumSandbox>
    with SingleTickerProviderStateMixin {
  double _armR = 1.0; // relative arm extension, 0.3 (tucked) .. 1.0 (extended)
  double _bodyMass = 1.0; // relative body mass unit
  double _angMomentum = 4.0; // fixed angular momentum (student can also change L)
  double _theta = 0;
  late final Ticker _ticker;
  Duration _last = Duration.zero;

  // Moment of inertia model: body (fixed small I0) + arms (m*r^2 each side).
  double get _momentOfInertia => 0.4 * _bodyMass + 2 * _bodyMass * _armR * _armR;
  double get _omega => _angMomentum / _momentOfInertia;

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
    setState(() => _theta = (_theta + _omega * dt) % (2 * math.pi));
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
            painter: _SpinPainter(theta: _theta, armR: _armR),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Moment of inertia I', _momentOfInertia.toStringAsFixed(2), '(rel)', const Color(0xFF38BDF8))),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Angular speed ω = L/I', _omega.toStringAsFixed(2), 'rad/s', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x2),
        _meter('Angular momentum L = Iω (conserved)', _angMomentum.toStringAsFixed(2), '(rel)', const Color(0xFF16A34A)),
        const SizedBox(height: Gap.x3),
        _slider('Arms in ↔ out', _armR, 0.3, 1.0, '', const Color(0xFFF97316),
            (x) => setState(() => _armR = x)),
        _slider('Body mass', _bodyMass, 0.5, 2.0, '', const Color(0xFF16A34A),
            (x) => setState(() => _bodyMass = x)),
        _slider('Angular momentum L (set by initial push)', _angMomentum, 1.0, 8.0, '', const Color(0xFF38BDF8),
            (x) => setState(() => _angMomentum = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: drag "arms in ↔ out" toward IN and watch the spin visibly speed up — L = Iω stays fixed (no external torque acts once spinning), so shrinking I forces ω to grow. This is exactly how a figure skater speeds up a spin by pulling their arms close to their body.'),
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

class _SpinPainter extends CustomPainter {
  final double theta, armR;
  _SpinPainter({required this.theta, required this.armR});

  @override
  void paint(Canvas canvas, Size size) {
    final c = Offset(size.width / 2, size.height / 2 + 10);
    final armLenPx = 24 + armR * 64;

    // Body torso.
    canvas.drawRRect(
        RRect.fromRectAndRadius(
            Rect.fromCenter(center: c, width: 22, height: 60), const Radius.circular(11)),
        Paint()..color = Palette.accent);
    canvas.drawCircle(c - const Offset(0, 42), 12, Paint()..color = Palette.accent);

    // Two arms extending outward from the torso, rotating with theta.
    for (final side in [-1.0, 1.0]) {
      final armAngle = theta + (side > 0 ? 0 : math.pi);
      final dir = Offset(math.cos(armAngle), math.sin(armAngle));
      final start = c + Offset(0, -6);
      final end = start + dir * armLenPx;
      canvas.drawLine(start, end, Paint()..color = const Color(0xFF38BDF8)..strokeWidth = 6..strokeCap = StrokeCap.round);
      canvas.drawCircle(end, 8, Paint()..color = const Color(0xFF38BDF8));
    }

    // Rotation direction indicator (curved arrow) above.
    final path = Path()
      ..addArc(Rect.fromCircle(center: c, radius: armLenPx + 20), -math.pi / 2 - 0.9, 1.6);
    canvas.drawPath(path, Paint()..color = Colors.white38..style = PaintingStyle.stroke..strokeWidth = 1.6);

    _label(canvas, armR < 0.55 ? 'ARMS IN — spinning FAST' : 'ARMS OUT — spinning SLOW',
        Offset(size.width / 2, 16), Colors.white70, 11);
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
  bool shouldRepaint(_SpinPainter old) => old.theta != theta || old.armR != armR;
}
