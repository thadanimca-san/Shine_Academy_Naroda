import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Young's Double-Slit Lab — control slit separation d, wavelength λ and the
/// slit-to-screen distance D, then watch the fringe pattern and its intensity
/// curve rebuild live. The key relationship to discover: fringe width
/// β = λD/d — fringes spread out as d shrinks or λ grows.
class InterferenceSandbox extends StatelessWidget {
  const InterferenceSandbox({super.key});

  @override
  Widget build(BuildContext context) => const _InterferenceView();
}

class _InterferenceView extends StatefulWidget {
  const _InterferenceView();
  @override
  State<_InterferenceView> createState() => _InterferenceViewState();
}

class _InterferenceViewState extends State<_InterferenceView> {
  double _dMicron = 250; // slit separation d (µm)
  double _lambdaNm = 550; // wavelength (nm)
  double _dMeter = 1.5; // slit-to-screen distance D (m)

  // fringe width β in millimetres:  β = λD/d
  double get _betaMm {
    final lambda = _lambdaNm * 1e-9; // m
    final d = _dMicron * 1e-6; // m
    return lambda * _dMeter / d * 1e3; // mm
  }

  Color get _tint => _wavelengthColor(_lambdaNm);

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
            painter: _FringePainter(
              dMicron: _dMicron,
              lambdaNm: _lambdaNm,
              dMeter: _dMeter,
              tint: _tint,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(
          children: [
            Expanded(child: _readout('FRINGE WIDTH β', '${_betaMm.toStringAsFixed(2)} mm', Palette.primary)),
            const SizedBox(width: Gap.x3),
            Expanded(child: _readout('β = λD/d', 'λ=${_lambdaNm.toStringAsFixed(0)}nm', _tint)),
          ],
        ),
        const SizedBox(height: Gap.x3),
        _slider('Slit separation d', _dMicron, 100, 600, 'µm', Palette.primary,
            (v) => setState(() => _dMicron = v)),
        _slider('Wavelength λ', _lambdaNm, 400, 700, 'nm', _tint,
            (v) => setState(() => _lambdaNm = v)),
        _slider('Screen distance D', _dMeter, 0.5, 3.0, 'm', Palette.accent,
            (v) => setState(() => _dMeter = v)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.primarySoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Halve d and the fringes spread twice as far apart. Increase D and they fan out too. That is β = λD/d in action.'),
            style: Type.caption.copyWith(color: Palette.primaryDeep),
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
          Text(value,
              style: Type.bodyStrong.copyWith(fontSize: 15, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max, String unit,
      Color color, ValueChanged<double> onChanged) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('$label = ${value.toStringAsFixed(unit == 'm' ? 2 : 0)} $unit',
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

Color _wavelengthColor(double nm) {
  // Approximate visible spectrum mapping.
  if (nm < 440) return const Color(0xFF7A5CFF);
  if (nm < 490) return const Color(0xFF3B82F6);
  if (nm < 510) return const Color(0xFF22D3AA);
  if (nm < 560) return const Color(0xFF84CC16);
  if (nm < 590) return const Color(0xFFEAB308);
  if (nm < 640) return const Color(0xFFF97316);
  return const Color(0xFFEF4444);
}

class _FringePainter extends CustomPainter {
  final double dMicron, lambdaNm, dMeter;
  final Color tint;
  _FringePainter({
    required this.dMicron,
    required this.lambdaNm,
    required this.dMeter,
    required this.tint,
  });

  @override
  void paint(Canvas canvas, Size size) {
    // Fringe width on screen in metres: β = λD/d
    final beta = lambdaNm * 1e-9 * dMeter / (dMicron * 1e-6); // m
    // Map: screen spans about 40 mm across canvas width.
    const screenSpanMm = 40.0;
    final pxPerMm = size.width / screenSpanMm;
    final betaPx = beta * 1e3 * pxPerMm;

    final patternTop = size.height * 0.05;
    final patternBottom = size.height * 0.62;

    // Intensity I = I0 cos²(π x / β), painted as vertical bands.
    for (double x = 0; x <= size.width; x += 1) {
      final xMm = (x - size.width / 2) / pxPerMm;
      final phase = math.pi * (xMm) / (beta * 1e3);
      final c = math.cos(phase);
      final intensity = (c * c).clamp(0.0, 1.0);
      final paint = Paint()
        ..color = Color.lerp(Palette.stage, tint, intensity)!;
      canvas.drawRect(
          Rect.fromLTWH(x, patternTop, 1.4, patternBottom - patternTop), paint);
    }

    // Intensity curve below the band pattern.
    final curveTop = patternBottom + 12;
    final curveBottom = size.height - 20;
    final axis = Paint()
      ..color = Palette.stageLine
      ..strokeWidth = 1;
    canvas.drawLine(Offset(0, curveBottom), Offset(size.width, curveBottom), axis);

    final path = Path();
    for (double x = 0; x <= size.width; x += 2) {
      final xMm = (x - size.width / 2) / pxPerMm;
      final phase = math.pi * xMm / (beta * 1e3);
      final c = math.cos(phase);
      final intensity = (c * c).clamp(0.0, 1.0);
      final y = curveBottom - intensity * (curveBottom - curveTop);
      if (x == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
    }
    canvas.drawPath(
        path,
        Paint()
          ..color = tint
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2);

    // Mark fringe spacing β with a bracket between central max and first max.
    final centre = size.width / 2;
    if (betaPx > 8 && betaPx < size.width / 2) {
      final markPaint = Paint()
        ..color = Colors.white70
        ..strokeWidth = 1.2;
      final y = patternBottom - 6;
      canvas.drawLine(Offset(centre, y), Offset(centre + betaPx, y), markPaint);
      canvas.drawLine(Offset(centre, y - 4), Offset(centre, y + 4), markPaint);
      canvas.drawLine(
          Offset(centre + betaPx, y - 4), Offset(centre + betaPx, y + 4), markPaint);
      _label(canvas, 'β = ${(beta * 1e3).toStringAsFixed(2)} mm',
          Offset(centre + betaPx / 2, y - 12), Colors.white70, 10);
    }
    _label(canvas, 'INTENSITY  I = I₀cos²(πx/β)',
        Offset(size.width / 2, size.height - 8), Colors.white38, 9);
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
  bool shouldRepaint(_FringePainter old) =>
      old.dMicron != dMicron ||
      old.lambdaNm != lambdaNm ||
      old.dMeter != dMeter ||
      old.tint != tint;
}
