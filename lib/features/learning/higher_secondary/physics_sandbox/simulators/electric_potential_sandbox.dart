import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Electric Potential Sandbox — a point charge surrounded by equipotential
/// circles, with a draggable test point that shows V = kQ/r fall off with
/// distance, framed as an "energy landscape" (higher near the charge).
class ElectricPotentialSandbox extends StatefulWidget {
  const ElectricPotentialSandbox({super.key});

  @override
  State<ElectricPotentialSandbox> createState() => _ElectricPotentialSandboxState();
}

class _ElectricPotentialSandboxState extends State<ElectricPotentialSandbox> {
  double _q = 4.0; // charge in µC (can be negative)
  double _rNorm = 0.45; // test point radial position, 0..1 of max radius

  static const double _maxRadiusM = 0.60; // metres represented by full slider

  double get _rMeters => 0.08 + _rNorm * (_maxRadiusM - 0.08);

  // V = kQ/r, with Q in µC (1e-6 C) and k = 9e9 → V in volts, r in metres.
  double get _potentialAtTest => (9e9 * (_q * 1e-6)) / _rMeters;

  @override
  Widget build(BuildContext context) {
    final v = _potentialAtTest;
    final isNeg = _q < 0;
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 250,
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
          child: GestureDetector(
            onPanUpdate: (d) => _updateFromLocal(d.localPosition),
            onPanDown: (d) => _updateFromLocal(d.localPosition),
            child: CustomPaint(
              painter: _PotentialPainter(
                q: _q,
                rNorm: _rNorm,
                maxRadiusM: _maxRadiusM,
                potential: v,
              ),
              child: const SizedBox.expand(),
            ),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
            child: _meter('Potential  V = kQ/r', '${v >= 0 ? '+' : ''}${v.toStringAsFixed(0)}', 'V',
                isNeg ? Palette.danger : Palette.chElectroMag),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _meter('Distance  r', _rMeters.toStringAsFixed(2), 'm', Palette.accent),
          ),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Charge Q', _q, -8, 8, 'µC', Palette.chElectroMag, (x) => setState(() => _q = x)),
        _slider('Test point radius (drag on stage too)', _rNorm, 0, 1, '',
            const Color(0xFF38BDF8), (x) => setState(() => _rNorm = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: drag the glowing dot outward. Each ring is an equipotential circle — every point on ONE ring has the SAME potential. Notice V falls as 1/r (not 1/r² like the field), and think of it as height on a hill: the charge is the peak, and V is how high the "electric hill" is at that radius.'),
            style: Type.caption.copyWith(color: Palette.primaryDeep),
          ),
        ),
      ],
    );
  }

  void _updateFromLocal(Offset local) {
    // Stage size is fixed at build time via LayoutBuilder-less approach:
    // approximate using the last known painter geometry (center at box center).
    const boxHeight = 250.0;
    // width comes from parent constraints; use a reasonable default via context.
    final renderBox = context.findRenderObject();
    double width = 320;
    if (renderBox is RenderBox && renderBox.hasSize) {
      width = renderBox.size.width;
    }
    final center = Offset(width / 2, boxHeight / 2);
    final maxR = math.min(width, boxHeight) / 2 - 20;
    final dist = (local - center).distance.clamp(18.0, maxR);
    setState(() => _rNorm = ((dist - 18.0) / (maxR - 18.0)).clamp(0.0, 1.0));
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

class _PotentialPainter extends CustomPainter {
  final double q;
  final double rNorm;
  final double maxRadiusM;
  final double potential;

  _PotentialPainter({
    required this.q,
    required this.rNorm,
    required this.maxRadiusM,
    required this.potential,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final maxR = math.min(size.width, size.height) / 2 - 20;
    final isNeg = q < 0;
    final chargeColor = isNeg ? Palette.danger : Palette.chElectroMag;

    // Equipotential rings at fixed fractions of maxR, with live V labels.
    const fractions = [0.22, 0.42, 0.62, 0.82, 1.0];
    for (final f in fractions) {
      final ringR = 18 + f * (maxR - 18);
      final ringMeters = 0.08 + f * (maxRadiusM - 0.08);
      final ringV = 9e9 * (q * 1e-6) / ringMeters;
      canvas.drawCircle(
        center,
        ringR,
        Paint()
          ..color = chargeColor.withValues(alpha: 0.28)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.3,
      );
      _label(canvas, '${ringV >= 0 ? '+' : ''}${ringV.toStringAsFixed(0)}V',
          center + Offset(ringR * math.cos(-math.pi / 4), ringR * math.sin(-math.pi / 4)),
          chargeColor.withValues(alpha: 0.85), 9.5);
    }

    // Radial field-direction ticks (perpendicular to equipotentials).
    final tickPaint = Paint()
      ..color = Colors.white24
      ..strokeWidth = 1;
    for (var i = 0; i < 16; i++) {
      final a = i * math.pi / 8;
      final p1 = center + Offset(24 * math.cos(a), 24 * math.sin(a));
      final p2 = center + Offset(maxR * math.cos(a), maxR * math.sin(a));
      canvas.drawLine(p1, p2, tickPaint..color = Colors.white.withValues(alpha: 0.06));
    }

    // Central charge.
    canvas.drawCircle(center, 14, Paint()..color = chargeColor);
    _label(canvas, isNeg ? '−' : '+', center, Colors.white, 15);
    _label(canvas, isNeg ? 'Q (−)' : 'Q (+)', center + const Offset(0, 24), chargeColor, 10.5);

    // Draggable test point on the current radius.
    final testR = 18 + rNorm * (maxR - 18);
    const testAngle = -math.pi / 4;
    final testPos = center + Offset(testR * math.cos(testAngle), testR * math.sin(testAngle));
    canvas.drawLine(center, testPos, Paint()
      ..color = const Color(0xFF38BDF8).withValues(alpha: 0.55)
      ..strokeWidth = 1.6);
    canvas.drawCircle(testPos, 8, Paint()..color = const Color(0xFF38BDF8));
    canvas.drawCircle(testPos, 8, Paint()
      ..color = Colors.white
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.5);
    _label(canvas, '${potential >= 0 ? '+' : ''}${potential.toStringAsFixed(0)} V',
        testPos + const Offset(0, -16), const Color(0xFF38BDF8), 11.5);

    // "Energy landscape" bar on the right: height ∝ potential.
    _drawLandscapeBar(canvas, size, potential, chargeColor);
  }

  void _drawLandscapeBar(Canvas canvas, Size size, double v, Color color) {
    final barX = size.width - 30;
    const barTop = 20.0;
    final barBottom = size.height - 20.0;
    canvas.drawLine(Offset(barX, barTop), Offset(barX, barBottom), Paint()
      ..color = Colors.white24
      ..strokeWidth = 2);
    // Map potential (roughly -800..+800 V range) to a height along the bar.
    final clampedV = v.clamp(-800.0, 800.0);
    final t = (clampedV + 800) / 1600; // 0..1
    final markerY = barBottom - t * (barBottom - barTop);
    canvas.drawCircle(Offset(barX, markerY), 6, Paint()..color = color);
    _label(canvas, 'V', Offset(barX, barTop - 10), Colors.white54, 9);
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
  bool shouldRepaint(_PotentialPainter old) =>
      old.q != q || old.rNorm != rNorm || old.potential != potential;
}
