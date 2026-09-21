import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// AC Circuits Sandbox — a series RLC circuit driven at adjustable angular
/// frequency ω. Shows live impedance Z, reactances XL/XC, phase angle, and a
/// rotating phasor diagram, with resonance (ω0 = 1/√LC) marked.
class AcCircuitsSandbox extends StatefulWidget {
  const AcCircuitsSandbox({super.key});

  @override
  State<AcCircuitsSandbox> createState() => _AcCircuitsSandboxState();
}

class _AcCircuitsSandboxState extends State<AcCircuitsSandbox>
    with SingleTickerProviderStateMixin {
  double _r = 20; // ohms
  double _l = 0.4; // henries
  double _c = 40e-6; // farads
  double _omega = 100; // rad/s (driving angular frequency)
  double _phase = 0;
  late final Ticker _ticker;
  Duration _last = Duration.zero;

  double get _xl => _omega * _l;
  double get _xc => 1 / (_omega * _c);
  double get _z => math.sqrt(_r * _r + (_xl - _xc) * (_xl - _xc));
  double get _phi => math.atan2(_xl - _xc, _r); // phase of V ahead of I
  double get _omega0 => 1 / math.sqrt(_l * _c);

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
    setState(() => _phase = (_phase + 2.2 * dt) % (2 * math.pi));
  }

  @override
  Widget build(BuildContext context) {
    final atResonance = (_omega - _omega0).abs() / _omega0 < 0.03;
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 230,
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
            painter: _PhasorPainter(xl: _xl, xc: _xc, r: _r, phi: _phi, phase: _phase),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Impedance Z', _z.toStringAsFixed(1), 'Ω', Palette.chElectroMag)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Phase φ', (_phi * 180 / math.pi).toStringAsFixed(1), '°', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Xₗ = ωL', _xl.toStringAsFixed(1), 'Ω', const Color(0xFF38BDF8))),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('X꜀ = 1/ωC', _xc.toStringAsFixed(1), 'Ω', const Color(0xFFF97316))),
        ]),
        const SizedBox(height: Gap.x3),
        if (atResonance)
          Container(
            margin: const EdgeInsets.only(bottom: Gap.x3),
            padding: const EdgeInsets.all(Gap.x3),
            decoration: BoxDecoration(
              color: Palette.successSoft,
              borderRadius: BorderRadius.circular(Corner.md),
            ),
            child: Text(TrilingualService.instance.getUIText('RESONANCE: ω ≈ ω₀ = 1/√LC — Xₗ = X꜀, impedance is minimum (Z = R), current is maximum.'),
              style: Type.caption.copyWith(color: Palette.success, fontWeight: FontWeight.w700),
            ),
          ),
        _slider('Frequency ω', _omega, 20, 400, 'rad/s', const Color(0xFF9F7AEA),
            (x) => setState(() => _omega = x)),
        _slider('Resistance R', _r, 2, 100, 'Ω', const Color(0xFF34D399),
            (x) => setState(() => _r = x)),
        _slider('Inductance L', _l, 0.05, 1.0, 'H', const Color(0xFF38BDF8),
            (x) => setState(() => _l = x)),
        _slider('Capacitance C', _c * 1e6, 5, 100, 'µF',
            const Color(0xFFF97316), (x) => setState(() => _c = x * 1e-6)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: drag ω until Xₗ and X꜀ meet — Z drops to its minimum (Z = R) and the phase angle collapses to 0°. That special frequency is ω₀ = 1/√LC, the resonance point where the circuit draws maximum current.'),
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

class _PhasorPainter extends CustomPainter {
  final double xl, xc, r, phi, phase;
  _PhasorPainter(
      {required this.xl, required this.xc, required this.r, required this.phi, required this.phase});

  @override
  void paint(Canvas canvas, Size size) {
    final c = Offset(size.width / 2, size.height / 2 + 8);

    // Axes
    final axisPaint = Paint()..color = const Color(0x33FFFFFF)..strokeWidth = 1;
    canvas.drawLine(Offset(c.dx - 100, c.dy), Offset(c.dx + 100, c.dy), axisPaint);
    canvas.drawLine(Offset(c.dx, c.dy - 100), Offset(c.dx, c.dy + 100), axisPaint);
    _label(canvas, 'I (reference)', Offset(c.dx + 70, c.dy + 14), const Color(0xFFA5A9BF), 9);

    // Current phasor along +x (reference), rotating for visual life.
    final iDir = Offset(math.cos(phase * 0.15), -math.sin(phase * 0.15));
    _arrow(canvas, c, c + iDir * 60, const Color(0xFF34D399), 2.5);
    _label(canvas, 'I', c + iDir * 72, const Color(0xFF34D399), 12);

    // Voltage phasor at angle phi ahead of current.
    final vAngle = phase * 0.15 - phi; // screen y flipped, so subtract for CCW-lead
    final vDir = Offset(math.cos(vAngle), -math.sin(vAngle));
    _arrow(canvas, c, c + vDir * 80, const Color(0xFFF59E0B), 2.8);
    _label(canvas, 'V', c + vDir * 92, const Color(0xFFF59E0B), 12);

    // R, XL, XC vertical stack diagram on the right side for clarity.
    final baseX = size.width - 46;
    final baseY = size.height - 20;
    final barScale = 1.6;
    _bar(canvas, Offset(baseX - 24, baseY), r * barScale, const Color(0xFF34D399), 'R');
    _bar(canvas, Offset(baseX, baseY), xl * barScale, const Color(0xFF38BDF8), 'Xₗ');
    _bar(canvas, Offset(baseX + 24, baseY), xc * barScale, const Color(0xFFF97316), 'X꜀');

    _label(canvas, 'phasor diagram', Offset(c.dx, 16), const Color(0xFFA5A9BF), 10);
  }

  void _bar(Canvas canvas, Offset base, double height, Color color, String label) {
    final h = height.clamp(2.0, 150.0);
    final rect = Rect.fromLTWH(base.dx - 7, base.dy - h, 14, h);
    canvas.drawRect(rect, Paint()..color = color.withValues(alpha: 0.85));
    _label(canvas, label, Offset(base.dx, base.dy + 12), color, 9);
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
    canvas.drawLine(b, b - un * 10 + n * 4.5, p);
    canvas.drawLine(b, b - un * 10 - n * 4.5, p);
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
  bool shouldRepaint(_PhasorPainter old) =>
      old.xl != xl || old.xc != xc || old.r != r || old.phi != phi || old.phase != phase;
}
