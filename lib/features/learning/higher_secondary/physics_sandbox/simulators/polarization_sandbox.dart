import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Polarization Sandbox — unpolarized light through a polarizer + analyzer.
///
/// Students adjust the angle θ between the polarizer's and analyzer's
/// transmission axes and watch the transmitted intensity follow Malus's law
/// I = I0 cos²θ live, alongside a schematic of vibration directions being
/// filtered down to one plane and then attenuated by the second filter.
class PolarizationSandbox extends StatefulWidget {
  const PolarizationSandbox({super.key});

  @override
  State<PolarizationSandbox> createState() => _PolarizationSandboxState();
}

class _PolarizationSandboxState extends State<PolarizationSandbox> {
  double _thetaDeg = 45.0; // angle between polarizer and analyzer axes

  double get _thetaRad => _thetaDeg * math.pi / 180;
  double get _intensityFraction => math.pow(math.cos(_thetaRad), 2).toDouble();

  @override
  Widget build(BuildContext context) {
    final frac = _intensityFraction;

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
            painter: _PolarizationPainter(thetaRad: _thetaRad, intensityFraction: frac),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
            child: _readout(
              'Angle θ (polarizer↔analyzer)',
              '${_thetaDeg.toStringAsFixed(0)}°',
              Palette.info,
            ),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _readout(
              'Transmitted I / I0',
              frac.toStringAsFixed(3),
              Palette.accent,
            ),
          ),
        ]),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: Gap.x3, vertical: Gap.x2),
          decoration: BoxDecoration(
            color: Palette.infoSoft,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Text(TrilingualService.instance.getUIText('Malus\'s law: I = I0 cos²θ. At θ = 0° all the polarized light gets through; at θ = 90° (crossed polarizers) the light is completely blocked.'),
            style: Type.bodyStrong.copyWith(fontSize: 13),
          ),
        ),
        const SizedBox(height: Gap.x3),

        _slider('Angle between axes θ', _thetaDeg, 0, 90, '°', Palette.primary,
            (val) => setState(() => _thetaDeg = val)),
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
          Text(label.toUpperCase(), style: Type.label.copyWith(fontSize: 9)),
          const SizedBox(height: 4),
          Text(value,
              style: Type.bodyStrong.copyWith(
                  fontSize: 17, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max,
      String unit, Color color, ValueChanged<double> onChanged) {
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

class _PolarizationPainter extends CustomPainter {
  final double thetaRad;
  final double intensityFraction;

  _PolarizationPainter({required this.thetaRad, required this.intensityFraction});

  @override
  void paint(Canvas canvas, Size size) {
    final midY = size.height * 0.52;
    final srcX = size.width * 0.10;
    final polX = size.width * 0.42;
    final anaX = size.width * 0.70;
    final screenX = size.width * 0.94;

    // Source: unpolarized light — vibration directions in many planes (draw a
    // star of short lines) traveling toward the polarizer.
    for (int i = 0; i < 8; i++) {
      final a = i * math.pi / 8;
      final dx = 10 * math.cos(a), dy = 10 * math.sin(a);
      canvas.drawLine(Offset(srcX, midY) + Offset(-dx, -dy), Offset(srcX, midY) + Offset(dx, dy),
          Paint()..color = Colors.white38..strokeWidth = 1.2);
    }
    canvas.drawLine(Offset(srcX + 12, midY), Offset(polX - 18, midY),
        Paint()..color = Colors.white54..strokeWidth = 1.4);

    // Polarizer: vertical transmission axis (fixed reference, θ=0).
    _filter(canvas, polX, midY, 0, const Color(0xFF60A5FA), 'Polarizer');

    // Light between polarizer and analyzer: polarized vertically, full amplitude.
    _polarizedBeam(canvas, Offset(polX + 16, midY), Offset(anaX - 18, midY), 0, 1.0,
        const Color(0xFFFDE68A));

    // Analyzer: transmission axis at angle θ from the polarizer's axis.
    _filter(canvas, anaX, midY, thetaRad, const Color(0xFFC084FC), 'Analyzer');

    // Light after analyzer: amplitude scaled by cosθ (intensity by cos²θ),
    // oriented along the analyzer's axis.
    final afterColor = const Color(0xFFFDE68A).withValues(alpha: (0.15 + 0.85 * intensityFraction));
    _polarizedBeam(
        canvas, Offset(anaX + 16, midY), Offset(screenX - 6, midY), thetaRad, intensityFraction, afterColor);

    // Screen showing brightness proportional to intensity.
    final screenPaint = Paint()
      ..color = Colors.white.withValues(alpha: (0.10 + 0.80 * intensityFraction));
    canvas.drawRect(Rect.fromLTWH(screenX - 6, midY - 40, 10, 80), screenPaint);
    _label(canvas, 'screen', Offset(screenX, midY + 52), Colors.white54, 9);
  }

  void _filter(Canvas canvas, double x, double y, double axisAngle, Color color, String tag) {
    // Draw the filter as a disc with a line indicating its transmission axis.
    canvas.drawCircle(Offset(x, y), 34, Paint()..color = color.withValues(alpha: 0.12));
    canvas.drawCircle(Offset(x, y), 34, Paint()..color = color..style = PaintingStyle.stroke..strokeWidth = 2);
    final dir = Offset(math.sin(axisAngle), -math.cos(axisAngle)); // 0 → vertical axis
    canvas.drawLine(Offset(x, y) - dir * 30, Offset(x, y) + dir * 30,
        Paint()..color = color..strokeWidth = 2.5);
    _label(canvas, tag, Offset(x, y + 48), color, 9.5);
  }

  void _polarizedBeam(Canvas canvas, Offset a, Offset b, double axisAngle, double amplitudeFrac, Color color) {
    // Draw the beam as a line with small perpendicular ticks showing vibration
    // direction, amplitude scaled by amplitudeFrac (clamped for visibility).
    canvas.drawLine(a, b, Paint()..color = color.withValues(alpha: 0.4 + 0.5 * amplitudeFrac)..strokeWidth = 1.4);
    final dir = Offset(math.sin(axisAngle), -math.cos(axisAngle));
    final total = (b - a).distance;
    final steps = (total / 14).floor().clamp(1, 40);
    final amp = (6 + 10 * amplitudeFrac);
    for (int i = 1; i < steps; i++) {
      final t = i / steps;
      final p = Offset(a.dx + (b.dx - a.dx) * t, a.dy + (b.dy - a.dy) * t);
      canvas.drawLine(p - dir * amp, p + dir * amp, Paint()..color = color..strokeWidth = 1.6);
    }
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
  bool shouldRepaint(_PolarizationPainter old) =>
      old.thetaRad != thetaRad || old.intensityFraction != intensityFraction;
}
