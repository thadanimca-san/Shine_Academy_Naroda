import 'dart:math' as math;
import 'dart:ui' as ui;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Single-slit Diffraction Sandbox.
///
/// Students adjust slit width a and wavelength λ and watch the diffraction
/// pattern respond: a wide central maximum flanked by much dimmer secondary
/// maxima. The first-minimum angle sinθ = λ/a and the width of the central
/// maximum are read out live.
class DiffractionSandbox extends StatefulWidget {
  const DiffractionSandbox({super.key});

  @override
  State<DiffractionSandbox> createState() => _DiffractionSandboxState();
}

class _DiffractionSandboxState extends State<DiffractionSandbox> {
  double _slitWidthUm = 20.0; // slit width a, micrometres
  double _wavelengthNm = 550.0; // wavelength λ, nanometres
  double _screenDistCm = 100.0; // screen distance D, cm

  // sinθ1 = λ/a (first minimum)
  double get _sinTheta1 {
    final aM = _slitWidthUm * 1e-6;
    final lamM = _wavelengthNm * 1e-9;
    return (lamM / aM).clamp(0.0, 1.0);
  }

  double get _theta1Deg => math.asin(_sinTheta1) * 180 / math.pi;

  // linear position of first minimum on screen: y1 ≈ D * tanθ1
  double get _y1Cm {
    final t = _sinTheta1;
    if (t >= 1) return double.infinity;
    final tanT = t / math.sqrt(1 - t * t);
    return _screenDistCm * tanT;
  }

  double get _centralWidthCm => 2 * _y1Cm;

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
            painter: _DiffractionPainter(sinTheta1: _sinTheta1),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
            child: _readout(
              'First minimum θ1',
              _sinTheta1 >= 1 ? '—' : '${_theta1Deg.toStringAsFixed(1)}°',
              Palette.info,
            ),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _readout(
              'Central max width',
              _centralWidthCm.isInfinite ? '—' : '${_centralWidthCm.toStringAsFixed(1)} cm',
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
          child: Text(TrilingualService.instance.getUIText('a sinθ = λ gives the FIRST MINIMUM (not a maximum!). Shrink the slit width a and watch the whole pattern spread out wider.'),
            style: Type.bodyStrong.copyWith(fontSize: 13),
          ),
        ),
        const SizedBox(height: Gap.x3),

        _slider('Slit width a', _slitWidthUm, 5, 50, 'µm', Palette.primary,
            (val) => setState(() => _slitWidthUm = val)),
        _slider('Wavelength λ', _wavelengthNm, 400, 700, 'nm', Palette.jee,
            (val) => setState(() => _wavelengthNm = val)),
        _slider('Screen distance D', _screenDistCm, 50, 200, 'cm', Palette.neet,
            (val) => setState(() => _screenDistCm = val)),
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

class _DiffractionPainter extends CustomPainter {
  final double sinTheta1; // controls how spread-out the pattern is

  _DiffractionPainter({required this.sinTheta1});

  @override
  void paint(Canvas canvas, Size size) {
    final midY = size.height * 0.5;

    // Slit on the left, screen intensity pattern on the right.
    final slitX = size.width * 0.12;
    canvas.drawRect(
        Rect.fromLTWH(slitX - 4, 0, 8, size.height * 0.42), Paint()..color = Colors.white38);
    canvas.drawRect(
        Rect.fromLTWH(slitX - 4, size.height * 0.58, 8, size.height * 0.42),
        Paint()..color = Colors.white38);
    _label(canvas, 'slit', Offset(slitX, size.height * 0.5 - 2), Colors.white54, 9);

    // Intensity pattern drawn as a horizontal profile: central max wide,
    // side lobes narrower and dimmer, spacing controlled by sinTheta1.
    final screenX0 = size.width * 0.30;
    final screenW = size.width * 0.66;
    final path = Path();
    final points = <Offset>[];
    // spread factor: bigger sinTheta1 → narrower slit → wider pattern
    final spread = (40 + sinTheta1 * 300).clamp(40.0, 340.0);
    for (double x = 0; x <= screenW; x += 2) {
      final u = (x - screenW / 2) / spread * math.pi; // beta-like variable
      double intensity;
      if (u.abs() < 1e-3) {
        intensity = 1.0;
      } else {
        final s = math.sin(u) / u;
        intensity = s * s;
      }
      final px = screenX0 + x;
      final py = midY - intensity * (size.height * 0.42);
      points.add(Offset(px, py));
    }
    path.moveTo(points.first.dx, midY);
    for (final p in points) {
      path.lineTo(p.dx, p.dy);
    }
    path.lineTo(points.last.dx, midY);
    path.close();

    canvas.drawPath(
        path,
        Paint()
          ..shader = LinearGradient(
            begin: Alignment.topCenter,
            end: Alignment.bottomCenter,
            colors: [const Color(0xFFFDE68A).withValues(alpha: 0.55), Colors.transparent],
          ).createShader(Rect.fromLTWH(screenX0, 0, screenW, size.height)),
        );
    canvas.drawPoints(
        ui.PointMode.polygon,
        points,
        Paint()
          ..color = const Color(0xFFFBBF24)
          ..strokeWidth = 2
          ..style = PaintingStyle.stroke);

    canvas.drawLine(Offset(screenX0, midY), Offset(screenX0 + screenW, midY),
        Paint()..color = Palette.stageLine..strokeWidth = 1.2);
    _label(canvas, 'central maximum (wide)', Offset(screenX0 + screenW / 2, midY - size.height * 0.42 - 10),
        Colors.white70, 9.5);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700)),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_DiffractionPainter old) => old.sinTheta1 != sinTheta1;
}
