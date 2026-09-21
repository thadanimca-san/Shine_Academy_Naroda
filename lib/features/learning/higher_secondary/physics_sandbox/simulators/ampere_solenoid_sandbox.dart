import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Ampere's Law & Solenoid Sandbox — a coil of adjustable turn density n and
/// current I. Field lines inside become uniform and parallel (like a bar
/// magnet) with a live B = μ0 n I readout; field outside is drawn faint/absent.
class AmpereSolenoidSandbox extends StatefulWidget {
  const AmpereSolenoidSandbox({super.key});

  @override
  State<AmpereSolenoidSandbox> createState() => _AmpereSolenoidSandboxState();
}

class _AmpereSolenoidSandboxState extends State<AmpereSolenoidSandbox> {
  double _turnsPerCm = 5; // n in turns per cm (toy units)
  double _current = 3.0; // amperes

  static const double _mu0 = 4 * math.pi * 1e-7;

  // n in turns per metre for the formula.
  double get _nPerMetre => _turnsPerCm * 100;
  double get _fieldTesla => _mu0 * _nPerMetre * _current;

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
            painter: _SolenoidPainter(turnsPerCm: _turnsPerCm, current: _current),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('Field inside  B = μ₀nI', _fieldTesla.toStringAsExponential(2),
                  'T', Palette.chElectroMag)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Turn density n', _nPerMetre.toStringAsFixed(0), 'turns/m', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Turns per cm (n)', _turnsPerCm, 1, 12, '', const Color(0xFF38BDF8),
            (x) => setState(() => _turnsPerCm = x)),
        _slider('Current I', _current, 0.5, 8, 'A', const Color(0xFFF97316),
            (x) => setState(() => _current = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: pack the turns closer together (raise n) and watch the field lines inside tighten into a uniform, parallel bundle — while outside the coil, the field stays essentially zero. B = μ₀nI depends only on current and turn density, never on the radius of the coil.'),
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
        Text('$label = ${value.toStringAsFixed(1)} $unit',
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

class _SolenoidPainter extends CustomPainter {
  final double turnsPerCm, current;
  _SolenoidPainter({required this.turnsPerCm, required this.current});

  @override
  void paint(Canvas canvas, Size size) {
    final coilLeft = size.width * 0.18;
    final coilRight = size.width * 0.82;
    final midY = size.height / 2;
    final coilHalfH = size.height * 0.28;

    // Number of loop turns to draw (visual density, capped for clarity).
    final spacing = (18 - turnsPerCm).clamp(6.0, 16.0);
    final loopCount = ((coilRight - coilLeft) / spacing).floor().clamp(4, 40);
    final loopPaint = Paint()
      ..color = const Color(0xFFF97316)
      ..strokeWidth = 2.6
      ..style = PaintingStyle.stroke;

    for (int i = 0; i <= loopCount; i++) {
      final x = coilLeft + i * (coilRight - coilLeft) / loopCount;
      canvas.drawOval(
        Rect.fromCenter(center: Offset(x, midY), width: 14, height: coilHalfH * 2),
        loopPaint,
      );
    }

    // Uniform parallel field lines inside the solenoid.
    final fieldPaint = Paint()
      ..color = const Color(0xFF34D399)
      ..strokeWidth = 2;
    final lineYs = [midY - coilHalfH * 0.55, midY, midY + coilHalfH * 0.55];
    for (final y in lineYs) {
      _arrow(canvas, Offset(coilLeft + 6, y), Offset(coilRight - 6, y), fieldPaint.color, 2);
    }
    _label(canvas, 'B uniform & parallel inside', Offset(size.width / 2, midY - coilHalfH - 24),
        const Color(0xFF34D399), 11);

    // Faint scattered field outside (near zero).
    final outsidePaint = Paint()..color = const Color(0x2234D399);
    for (int i = 0; i < 6; i++) {
      final y = midY - coilHalfH - 10 - i * 4.0;
      canvas.drawLine(Offset(coilLeft - 20, y), Offset(coilRight + 20, y), outsidePaint..strokeWidth = 1);
    }
    _label(canvas, 'B ≈ 0 outside', Offset(size.width / 2, 16), const Color(0xFFA5A9BF), 10);

    // Current direction indicator at ends.
    _label(canvas, 'I', Offset(coilLeft - 14, midY), const Color(0xFFFDBA74), 13);
    _label(canvas, 'I', Offset(coilRight + 14, midY), const Color(0xFFFDBA74), 13);
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
  bool shouldRepaint(_SolenoidPainter old) =>
      old.turnsPerCm != turnsPerCm || old.current != current;
}
