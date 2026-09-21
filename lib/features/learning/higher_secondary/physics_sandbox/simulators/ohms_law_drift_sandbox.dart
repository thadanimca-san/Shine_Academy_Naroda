import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Ohm's Law & Drift Velocity Sandbox — a conducting wire with free electrons
/// that zig-zag with random thermal motion while slowly drifting under an
/// applied field. Sliders control voltage, resistivity/temperature and
/// geometry; live meters show I = V/R (Ohm's law) and v_d = I/(nAe).
class OhmsLawDriftSandbox extends StatefulWidget {
  const OhmsLawDriftSandbox({super.key});

  @override
  State<OhmsLawDriftSandbox> createState() => _OhmsLawDriftSandboxState();
}

class _Electron {
  double x, y;
  double phase;
  _Electron(this.x, this.y, this.phase);
}

class _OhmsLawDriftSandboxState extends State<OhmsLawDriftSandbox>
    with SingleTickerProviderStateMixin {
  double _voltage = 6.0; // volts
  double _resistivityRel = 1.0; // relative resistivity (temperature proxy)
  double _lengthM = 2.0; // metres
  double _areaMm2 = 1.0; // mm^2

  late final Ticker _ticker;
  Duration _last = Duration.zero;
  double _time = 0;
  final List<_Electron> _electrons = [];
  final _rng = math.Random(11);

  // Fixed "n" (charge carrier density) proxy and elementary charge, chosen
  // for readable on-screen numbers rather than SI realism at full scale.
  static const double _nProxy = 8.5; // ×10^28 /m^3 (typical for copper)
  static const double _eCharge = 1.6; // ×10^-19 C

  double get _resistance {
    final rho = 1.68 * _resistivityRel; // ×10^-8 Ω·m, copper-like baseline
    final areaM2 = _areaMm2 * 1e-6;
    return (rho * 1e-8) * _lengthM / areaM2;
  }

  double get _current => _voltage / _resistance; // amps

  double get _driftVelocity {
    // v_d = I / (n A e)
    final areaM2 = _areaMm2 * 1e-6;
    final n = _nProxy * 1e28;
    return _current / (n * areaM2 * (_eCharge * 1e-19));
  }

  @override
  void initState() {
    super.initState();
    for (var i = 0; i < 14; i++) {
      _electrons.add(_Electron(_rng.nextDouble(), _rng.nextDouble(), _rng.nextDouble() * 2 * math.pi));
    }
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
    _time += dt;
    // Net drift speed scaled for visibility (real drift ~mm/s is imperceptible;
    // here we exaggerate proportionally so faster current visibly moves faster).
    final driftPxPerSec = 0.015 + (_current.clamp(0, 40)) * 0.006;
    setState(() {
      for (final e in _electrons) {
        e.x += driftPxPerSec * dt;
        if (e.x > 1.05) e.x -= 1.1;
        e.phase += dt * 6;
      }
    });
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 200,
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
            painter: _WirePainter(electrons: _electrons, time: _time, current: _current),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
            child: _meter('Current  I = V/R', _current.toStringAsFixed(2), 'A', Palette.chElectroMag),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _meter('Drift velocity  v_d', (_driftVelocity * 1000).toStringAsFixed(3), 'mm/s',
                Palette.accent),
          ),
        ]),
        const SizedBox(height: Gap.x2),
        _meter('Resistance  R = ρL/A', _resistance.toStringAsFixed(2), 'Ω', const Color(0xFF38BDF8)),
        const SizedBox(height: Gap.x3),
        _slider('Voltage V', _voltage, 0.5, 20, 'V', Palette.chElectroMag,
            (x) => setState(() => _voltage = x)),
        _slider('Resistivity ρ (temperature ↑)', _resistivityRel, 0.3, 3, '× baseline',
            const Color(0xFFF97316), (x) => setState(() => _resistivityRel = x)),
        _slider('Length L', _lengthM, 0.5, 5, 'm', const Color(0xFF16A34A),
            (x) => setState(() => _lengthM = x)),
        _slider('Cross-section A', _areaMm2, 0.2, 4, 'mm²', const Color(0xFF38BDF8),
            (x) => setState(() => _areaMm2 = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: raise the resistivity slider (like heating a metal wire) and watch R rise and current I = V/R fall. Notice the electrons themselves — their frantic zig-zag thermal jitter is huge, but their NET rightward drift is barely visible. That tiny net creep, only millimetres per second, is the entire electric current.'),
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

class _WirePainter extends CustomPainter {
  final List<_Electron> electrons;
  final double time;
  final double current;
  _WirePainter({required this.electrons, required this.time, required this.current});

  @override
  void paint(Canvas canvas, Size size) {
    final wireTop = size.height * 0.35;
    final wireBottom = size.height * 0.65;

    // Wire body.
    canvas.drawRect(
      Rect.fromLTRB(20, wireTop, size.width - 20, wireBottom),
      Paint()..color = const Color(0xFF2A2E63),
    );
    canvas.drawRect(
      Rect.fromLTRB(20, wireTop, size.width - 20, wireBottom),
      Paint()
        ..color = const Color(0xFF5B61C9)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2,
    );

    // Battery symbol (left) and field arrow inside the wire (drift direction).
    _label(canvas, '+', Offset(14, wireTop - 10), Palette.accent, 13);
    _label(canvas, '−', Offset(size.width - 14, wireTop - 10), const Color(0xFF38BDF8), 13);

    final fieldPaint = Paint()
      ..color = Palette.chElectroMag.withValues(alpha: 0.5)
      ..strokeWidth = 1.6;
    for (double x = 40; x < size.width - 30; x += 50) {
      final y = (wireTop + wireBottom) / 2 - 22;
      _arrow(canvas, Offset(x, y), Offset(x + 24, y), fieldPaint.color, 1.6);
    }
    _label(canvas, 'E field →', Offset(size.width / 2, wireTop - 26), Colors.white54, 10);

    // Electrons: thermal zig-zag jitter overlaid on slow net drift (x in 0..1).
    for (final e in electrons) {
      final baseX = 30 + e.x * (size.width - 60);
      final jitterX = 5 * math.sin(e.phase * 2.3);
      final jitterY = 6 * math.sin(e.phase * 3.1 + e.x * 9);
      final cy = (wireTop + wireBottom) / 2 + jitterY;
      final pos = Offset(baseX + jitterX, cy.clamp(wireTop + 6, wireBottom - 6));
      canvas.drawCircle(pos, 4, Paint()..color = const Color(0xFFFDE68A));
      canvas.drawCircle(pos, 4, Paint()
        ..color = Colors.white24
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1);
    }

    _label(canvas, 'e⁻ conventional current drifts → (opposite to e⁻ actual motion ←)',
        Offset(size.width / 2, wireBottom + 18), Colors.white54, 9.5);
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
    canvas.drawLine(b, b - un * 7 + n * 3, p);
    canvas.drawLine(b, b - un * 7 - n * 3, p);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style:
              TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_WirePainter old) => true;
}
