import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Satellite Motion — a satellite in circular orbit around the Earth.
///
/// Students drag the orbital altitude and watch orbital speed and period
/// respond. A dashed ring marks the geostationary orbit (T = 24 h). Push
/// the speed above circular and the orbit becomes an escape trajectory;
/// drop it below and the satellite spirals in (deorbit).
class SatelliteMotionSandbox extends StatefulWidget {
  const SatelliteMotionSandbox({super.key});

  @override
  State<SatelliteMotionSandbox> createState() => _SatelliteMotionSandboxState();
}

class _SatelliteMotionSandboxState extends State<SatelliteMotionSandbox>
    with SingleTickerProviderStateMixin {
  // Earth constants (SI)
  static const double _g = 6.674e-11;
  static const double _mEarth = 5.972e24;
  static const double _rEarth = 6.371e6; // m
  static const double _gm = _g * _mEarth;

  // Controls
  double _altitude = 400; // km above surface
  double _speedFactor = 1.0; // multiple of circular speed

  // Animation
  late final Ticker _ticker;
  Duration _last = Duration.zero;
  double _angle = 0;

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

  double get _r => _rEarth + _altitude * 1000; // orbital radius, m
  double get _vCircular => math.sqrt(_gm / _r); // m/s
  double get _vEscape => math.sqrt(2 * _gm / _r); // m/s
  double get _v => _vCircular * _speedFactor;
  double get _period => 2 * math.pi * _r / _vCircular; // s (circular)
  bool get _willEscape => _speedFactor >= math.sqrt2 - 1e-9;

  // Geostationary altitude ≈ 35 786 km
  static const double _geoAltKm = 35786;

  void _tick(Duration elapsed) {
    final dt = math.min((elapsed - _last).inMicroseconds / 1e6, 0.032);
    _last = elapsed;
    // Scale angular speed so a low orbit looks fast and GEO looks slow,
    // but keep it watchable (compress real periods hugely).
    final omega = 2 * math.pi / (_period / 3600); // rev per (hour→sec) demo
    setState(() => _angle = (_angle + omega * dt) % (2 * math.pi));
  }

  @override
  Widget build(BuildContext context) {
    final vKms = _v / 1000;
    final periodHours = _period / 3600;
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
            painter: _OrbitPainter(
              altitudeKm: _altitude,
              rEarthKm: _rEarth / 1000,
              geoAltKm: _geoAltKm,
              angle: _angle,
              speedFactor: _speedFactor,
              willEscape: _willEscape,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _readout('ORBITAL SPEED', '${vKms.toStringAsFixed(2)} km/s', Palette.primary)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _readout(
                  'PERIOD',
                  periodHours < 100
                      ? '${periodHours.toStringAsFixed(1)} h'
                      : '${(periodHours / 24).toStringAsFixed(0)} d',
                  Palette.accent)),
        ]),
        const SizedBox(height: Gap.x2),
        Row(children: [
          Expanded(child: _readout('ESCAPE SPEED', '${(_vEscape / 1000).toStringAsFixed(2)} km/s', Palette.danger)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _readout(
                  'STATUS',
                  _willEscape
                      ? 'ESCAPE'
                      : _speedFactor < 0.98
                          ? 'DEORBIT'
                          : 'STABLE',
                  _willEscape
                      ? Palette.danger
                      : _speedFactor < 0.98
                          ? Palette.accent
                          : Palette.success)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Altitude', _altitude, 200, 36000, 'km', Palette.primary,
            (v) => setState(() => _altitude = v)),
        _slider(
          'Speed  (1.00 = circular, ${math.sqrt2.toStringAsFixed(2)} = escape)',
          _speedFactor, 0.7, 1.6, '× v_c', Palette.accent,
          (v) => setState(() => _speedFactor = v),
        ),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.infoSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(
            _willEscape
                ? 'At v ≥ √2 × v_c the satellite has enough KE to escape Earth\'s gravity forever — the orbit opens into a parabola/hyperbola.'
                : _speedFactor < 0.98
                    ? 'Below circular speed gravity wins: the satellite falls to a lower point each pass and eventually re-enters (deorbit).'
                    : 'Set the altitude to ${_geoAltKm.toStringAsFixed(0)} km and watch the period lock to 24 h — that is the geostationary orbit.',
            style: Type.caption.copyWith(color: Palette.info, fontSize: 12),
          ),
        ),
      ],
    );
  }

  Widget _readout(String label, String value, Color color) {
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
          Text(label, style: Type.label.copyWith(fontSize: 9)),
          const SizedBox(height: 4),
          Text(value, style: Type.bodyStrong.copyWith(fontSize: 15, fontFamily: 'monospace', color: color)),
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
          '$label = ${value.toStringAsFixed(unit == '× v_c' ? 2 : 0)} $unit',
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

class _OrbitPainter extends CustomPainter {
  final double altitudeKm, rEarthKm, geoAltKm, angle, speedFactor;
  final bool willEscape;

  _OrbitPainter({
    required this.altitudeKm,
    required this.rEarthKm,
    required this.geoAltKm,
    required this.angle,
    required this.speedFactor,
    required this.willEscape,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    // Map real radii to pixels: max radius shown = GEO + a bit.
    final maxR = (rEarthKm + geoAltKm) * 1.05;
    final scale = (math.min(size.width, size.height) / 2 - 10) / maxR;

    final earthR = rEarthKm * scale;
    final orbitR = (rEarthKm + altitudeKm) * scale;
    final geoR = (rEarthKm + geoAltKm) * scale;

    // Earth
    canvas.drawCircle(center, earthR, Paint()..color = const Color(0xFF2563EB));
    canvas.drawCircle(center, earthR, Paint()..color = const Color(0x334ADE80));

    // Geostationary ring (dashed)
    _dashedCircle(canvas, center, geoR, const Color(0x66F59E0B));
    _label(canvas, 'GEO', center + Offset(0, -geoR - 8), const Color(0xFFF59E0B), 9);

    // Orbit path
    final orbitPaint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.4
      ..color = willEscape ? const Color(0x55DC2626) : const Color(0x554F46E5);
    if (willEscape) {
      // Draw an opening spiral to suggest escape.
      final path = Path();
      for (double t = 0; t < 2.4; t += 0.05) {
        final rr = orbitR * (1 + t * 0.9);
        final p = center + Offset(rr * math.cos(t + angle - angle), rr * math.sin(t));
        if (t == 0) {
          path.moveTo(p.dx, p.dy);
        } else {
          path.lineTo(p.dx, p.dy);
        }
      }
      canvas.drawPath(path, orbitPaint);
    } else {
      canvas.drawCircle(center, orbitR, orbitPaint);
    }

    // Satellite
    final effR = willEscape ? orbitR * (1 + angle * 0.25) : orbitR;
    final sat = center + Offset(effR * math.cos(angle), effR * math.sin(angle));
    canvas.drawCircle(sat, 5, Paint()..color = Colors.white);
    canvas.drawCircle(sat, 5, Paint()..color = willEscape ? const Color(0xFFDC2626) : const Color(0xFF4F46E5)..style = PaintingStyle.stroke..strokeWidth = 2);

    // Velocity arrow (tangent)
    final tangent = Offset(-math.sin(angle), math.cos(angle)) * (14.0 + speedFactor * 8);
    final vp = Paint()
      ..color = const Color(0xFFF59E0B)
      ..strokeWidth = 2
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(sat, sat + tangent, vp);

    _label(canvas, '${altitudeKm.toStringAsFixed(0)} km', center + Offset(0, earthR + 12), Colors.white70, 10);
  }

  void _dashedCircle(Canvas canvas, Offset c, double r, Color color) {
    final paint = Paint()
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1
      ..color = color;
    const seg = 0.16;
    for (double a = 0; a < 2 * math.pi; a += seg * 2) {
      final path = Path();
      path.addArc(Rect.fromCircle(center: c, radius: r), a, seg);
      canvas.drawPath(path, paint);
    }
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fontSize) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(color: color, fontSize: fontSize, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_OrbitPainter old) =>
      old.altitudeKm != altitudeKm ||
      old.angle != angle ||
      old.speedFactor != speedFactor ||
      old.willEscape != willEscape;
}
