import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Power Sandbox — a vehicle climbing a slope at constant speed.
///
/// Students set the slope angle, vehicle mass, friction force and speed, and
/// watch the engine's instantaneous power P = Fv = (mg sinθ + f)·v update
/// live, along with a rolling average-power readout as the vehicle climbs.
class PowerSandbox extends StatefulWidget {
  const PowerSandbox({super.key});

  @override
  State<PowerSandbox> createState() => _PowerSandboxState();
}

class _PowerSandboxState extends State<PowerSandbox> with SingleTickerProviderStateMixin {
  double _mass = 800; // kg
  double _angleDeg = 10; // slope angle
  double _friction = 200; // N, resistive force
  double _speed = 8; // m/s, constant climbing speed
  static const double _g = 9.8;

  double _distance = 0; // m travelled (for the animation loop)
  double _workDone = 0; // J accumulated
  double _simTime = 0;
  late final Ticker _ticker;
  Duration _last = Duration.zero;

  double get _angleRad => _angleDeg * math.pi / 180;
  double get _driveForce => _mass * _g * math.sin(_angleRad) + _friction;
  double get _instantPower => _driveForce * _speed;
  double get _avgPower => _simTime > 0 ? _workDone / _simTime : 0;

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
    setState(() {
      _simTime += dt;
      _distance = (_distance + _speed * dt) % 6.0; // loop the visual travel every 6 m
      _workDone += _instantPower * dt;
    });
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
            painter: _SlopePainter(angleDeg: _angleDeg, progress: _distance / 6.0, force: _driveForce),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('Instantaneous P = Fv', _instantPower.toStringAsFixed(0), 'W',
                  const Color(0xFF38BDF8))),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Average P = W/t', _avgPower.toStringAsFixed(0), 'W', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x2),
        _meter('Drive force F = mg sinθ + f', _driveForce.toStringAsFixed(0), 'N', const Color(0xFF16A34A)),
        const SizedBox(height: Gap.x3),
        _slider('Mass m', _mass, 200, 2000, 'kg', const Color(0xFF16A34A), (x) => setState(() => _mass = x)),
        _slider('Slope angle θ', _angleDeg, 0, 30, '°', const Color(0xFFF97316),
            (x) => setState(() => _angleDeg = x)),
        _slider('Friction/drag f', _friction, 0, 800, 'N', const Color(0xFFDC2626),
            (x) => setState(() => _friction = x)),
        _slider('Speed v', _speed, 1, 25, 'm/s', const Color(0xFF38BDF8), (x) => setState(() => _speed = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: at constant speed, the engine must supply a force F = mg sinθ + f just to balance gravity and friction — zero net force, zero acceleration. Push the speed slider up and watch power rise in DIRECT proportion to v, even though the force needed does not change at all.'),
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
        Text('$label = ${value.toStringAsFixed(0)} $unit',
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

class _SlopePainter extends CustomPainter {
  final double angleDeg, progress, force;
  _SlopePainter({required this.angleDeg, required this.progress, required this.force});

  @override
  void paint(Canvas canvas, Size size) {
    final angle = angleDeg * math.pi / 180;
    final baseY = size.height - 30;
    final slopeLen = size.width - 40;
    final topY = baseY - slopeLen * math.tan(angle).clamp(0, 1.2);

    // Slope surface.
    final slopePath = Path()
      ..moveTo(20, baseY)
      ..lineTo(size.width - 20, topY)
      ..lineTo(size.width - 20, baseY)
      ..close();
    canvas.drawPath(slopePath, Paint()..color = const Color(0xFF232866));
    canvas.drawLine(Offset(20, baseY), Offset(size.width - 20, topY),
        Paint()..color = const Color(0xFF3E44A8)..strokeWidth = 3);

    // Vehicle position along the slope by progress (0..1).
    final vx = 20 + (size.width - 40) * progress;
    final vy = baseY - (baseY - topY) * progress;
    final carCenter = Offset(vx, vy - 14);

    // Car body.
    final carPaint = Paint()..color = Palette.accent;
    canvas.save();
    canvas.translate(carCenter.dx, carCenter.dy);
    canvas.rotate(-angle);
    canvas.drawRRect(
        RRect.fromRectAndRadius(const Rect.fromLTRB(-22, -10, 22, 10), const Radius.circular(5)), carPaint);
    canvas.drawCircle(const Offset(-13, 10), 6, Paint()..color = Colors.black87);
    canvas.drawCircle(const Offset(13, 10), 6, Paint()..color = Colors.black87);
    canvas.restore();

    // Force arrow along the slope (drive force direction).
    final dir = Offset(math.cos(angle), -math.sin(angle));
    final fLen = (force / 6000 * 40).clamp(14.0, 60.0);
    _arrow(canvas, carCenter, carCenter + dir * fLen, const Color(0xFF16A34A), 2.6);
    _label(canvas, 'F', carCenter + dir * (fLen + 14), const Color(0xFF16A34A), 11);

    _label(canvas, 'θ = ${angleDeg.toStringAsFixed(0)}°', Offset(50, baseY - 10), Colors.white70, 11);
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
  bool shouldRepaint(_SlopePainter old) =>
      old.angleDeg != angleDeg || old.progress != progress || old.force != force;
}
