import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Kinetic Theory Sandbox — a box of gas molecules bouncing elastically off
/// the walls. Raising temperature speeds every molecule up (and shifts dot
/// color hotter), visualizing v_rms = sqrt(3RT/M) and the microscopic origin
/// of pressure and temperature.
class KineticTheorySandbox extends StatefulWidget {
  const KineticTheorySandbox({super.key});

  @override
  State<KineticTheorySandbox> createState() => _KineticTheorySandboxState();
}

class _Molecule {
  Offset pos;
  Offset vel; // unit-ish direction, scaled by speed each frame
  _Molecule({required this.pos, required this.vel});
}

class _KineticTheorySandboxState extends State<KineticTheorySandbox>
    with SingleTickerProviderStateMixin {
  double _temperatureK = 300; // Kelvin
  static const double _molarMass = 0.029; // kg/mol, ~air
  static const double _gasConstantR = 8.314;

  late final List<_Molecule> _molecules;
  late final Ticker _ticker;
  Duration _last = Duration.zero;
  final _rng = math.Random(11);

  double get _vRms => math.sqrt(3 * _gasConstantR * _temperatureK / _molarMass);
  double get _vAvg => _vRms * math.sqrt(8 / (3 * math.pi)); // v_avg/v_rms = sqrt(8/3π)
  double get _vMp => _vRms * math.sqrt(2 / 3); // v_mp/v_rms = sqrt(2/3)
  double get _avgKePerMolecule => 1.5 * 1.380649e-23 * _temperatureK; // (3/2)kT in Joules

  @override
  void initState() {
    super.initState();
    _molecules = List.generate(26, (i) {
      final angle = _rng.nextDouble() * 2 * math.pi;
      return _Molecule(
        pos: Offset(20 + _rng.nextDouble() * 260, 20 + _rng.nextDouble() * 150),
        vel: Offset(math.cos(angle), math.sin(angle)),
      );
    });
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
    // Visual speed scale (not physical units) so higher T clearly moves faster.
    final speedScale = 40 * math.sqrt(_temperatureK / 300);
    setState(() {
      for (final m in _molecules) {
        var next = m.pos + m.vel * speedScale * dt;
        double vx = m.vel.dx;
        double vy = m.vel.dy;
        if (next.dx < 6 || next.dx > 294) vx = -vx;
        if (next.dy < 6 || next.dy > 184) vy = -vy;
        m.vel = Offset(vx, vy);
        next = Offset(next.dx.clamp(6, 294), next.dy.clamp(6, 184));
        m.pos = next;
      }
    });
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
            painter: _GasPainter(molecules: _molecules, temperatureK: _temperatureK),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('v_rms = √(3RT/M)',
              _vRms.toStringAsFixed(0), 'm/s', Palette.chThermal)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Avg KE = (3/2)kT',
              (_avgKePerMolecule * 1e21).toStringAsFixed(2), '×10⁻²¹ J', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x2),
        Row(children: [
          Expanded(child: _meter('v_avg', _vAvg.toStringAsFixed(0), 'm/s', const Color(0xFF38BDF8))),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('v_mp (most probable)', _vMp.toStringAsFixed(0), 'm/s', const Color(0xFF16A34A))),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Temperature T', _temperatureK, 100, 900, 'K', const Color(0xFFDC2626),
            (x) => setState(() => _temperatureK = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: drag T up and watch every dot speed up together (color shifts hotter) — temperature IS the average kinetic energy of the molecules, nothing more mysterious than that. Note v_rms > v_avg > v_mp always, in that fixed order, at any temperature.'),
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

class _GasPainter extends CustomPainter {
  final List<_Molecule> molecules;
  final double temperatureK;
  _GasPainter({required this.molecules, required this.temperatureK});

  @override
  void paint(Canvas canvas, Size size) {
    StageBackdrop.paint(canvas, size, groundY: size.height);

    final boxRect = Rect.fromLTWH(size.width * 0.05, size.height * 0.08,
        size.width * 0.9, size.height * 0.8);
    canvas.drawRRect(
      RRect.fromRectAndRadius(boxRect, const Radius.circular(10)),
      Paint()
        ..color = const Color(0x33FFFFFF)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2,
    );

    final heat = ((temperatureK - 100) / 800).clamp(0.0, 1.0);
    final dotColor = Color.lerp(const Color(0xFF38BDF8), const Color(0xFFDC2626), heat)!;

    final scaleX = boxRect.width / 300;
    final scaleY = boxRect.height / 190;
    for (final m in molecules) {
      final p = Offset(boxRect.left + m.pos.dx * scaleX, boxRect.top + m.pos.dy * scaleY);
      canvas.drawCircle(p, 4.2, Paint()..color = dotColor.withValues(alpha: 0.9));
      // faint motion trail
      final trail = p - m.vel * 10;
      canvas.drawLine(p, trail, Paint()..color = dotColor.withValues(alpha: 0.25)..strokeWidth = 1.6);
    }

    _label(canvas, 'T = ${temperatureK.toStringAsFixed(0)} K', Offset(size.width / 2, size.height * 0.06),
        Colors.white, 12);
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
  bool shouldRepaint(_GasPainter old) => true;
}
