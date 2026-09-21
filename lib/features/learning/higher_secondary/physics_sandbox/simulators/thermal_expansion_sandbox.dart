import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Thermal Expansion Sandbox — a metal rod elongates as ΔT rises
/// (ΔL = L₀αΔT), and a bimetallic-strip toggle shows two bonded metals with
/// different α bending as they're heated, because one expands more than
/// the other.
class ThermalExpansionSandbox extends StatefulWidget {
  const ThermalExpansionSandbox({super.key});

  @override
  State<ThermalExpansionSandbox> createState() => _ThermalExpansionSandboxState();
}

class _ThermalExpansionSandboxState extends State<ThermalExpansionSandbox> {
  double _deltaT = 60; // °C rise
  bool _bimetal = false;

  // Steel rod, L0 = 1.0 m (relative), alpha ~ 12e-6 /°C — scaled up for visibility.
  static const double _l0 = 1.0;
  static const double _alphaSteel = 12e-6;

  double get _deltaL => _l0 * _alphaSteel * _deltaT;
  double get _newLength => _l0 + _deltaL;

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
            painter: _ExpansionPainter(deltaT: _deltaT, bimetal: _bimetal),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Length change  ΔL',
              (_deltaL * 1000).toStringAsFixed(2), 'mm (per m, steel)', Palette.chThermal)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('New length  L₀+ΔL',
              _newLength.toStringAsFixed(5), 'm', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Temperature rise ΔT', _deltaT, 0, 200, '°C', const Color(0xFFDC2626),
            (x) => setState(() => _deltaT = x)),
        const SizedBox(height: Gap.x2),
        Row(
          children: [
            Expanded(
              child: GestureDetector(
                onTap: () => setState(() => _bimetal = !_bimetal),
                child: Container(
                  padding: const EdgeInsets.symmetric(vertical: 12),
                  decoration: BoxDecoration(
                    color: _bimetal ? Palette.chThermal : Palette.surface,
                    borderRadius: BorderRadius.circular(Corner.md),
                    border: Border.all(color: _bimetal ? Palette.chThermal : Palette.border),
                  ),
                  alignment: Alignment.center,
                  child: Text(
                    _bimetal ? 'Bimetallic strip view — ON' : 'Bimetallic strip view — OFF',
                    style: Type.caption.copyWith(
                        fontWeight: FontWeight.w700,
                        color: _bimetal ? Colors.white : Palette.textBody),
                  ),
                ),
              ),
            ),
          ],
        ),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(
            _bimetal
                ? 'Try it: raise ΔT and watch the strip curl — brass (α larger) stretches more than steel bonded to it, forcing the whole strip to bend toward the steel side. This is exactly how an old-fashioned thermostat switch works.'
                : 'Try it: raise ΔT from 0 to 200°C and watch the rod visibly stretch. Even though ΔL looks tiny in real units, this exact effect is why railway tracks and bridges need expansion gaps.',
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

class _ExpansionPainter extends CustomPainter {
  final double deltaT;
  final bool bimetal;
  _ExpansionPainter({required this.deltaT, required this.bimetal});

  static const double _alphaSteel = 12e-6;
  static const double _alphaBrass = 19e-6;

  @override
  void paint(Canvas canvas, Size size) {
    StageBackdrop.paint(canvas, size, groundY: size.height);

    final midY = size.height / 2;
    final baseLen = size.width * 0.6;
    // Amplify visually: real ΔL/L is tiny, so scale by a large visibility factor.
    const visualFactor = 400.0;

    if (!bimetal) {
      final growth = baseLen * _alphaSteel * deltaT * visualFactor;
      final len = (baseLen + growth).clamp(baseLen * 0.9, size.width * 0.94);
      final left = (size.width - len) / 2;
      final barColor = Color.lerp(const Color(0xFF64748B), const Color(0xFFDC2626),
          (deltaT / 200).clamp(0.0, 1.0))!;
      // Fixed left wall.
      canvas.drawRect(Rect.fromLTWH(left - 6, midY - 26, 6, 52), Paint()..color = Palette.textFaint);
      canvas.drawRRect(
        RRect.fromRectAndRadius(Rect.fromLTWH(left, midY - 14, len, 28), const Radius.circular(6)),
        Paint()..color = barColor,
      );
      _label(canvas, 'ΔT = ${deltaT.toStringAsFixed(0)}°C', Offset(size.width / 2, midY - 40),
          Colors.white, 12);
      // Dashed original-length marker.
      final originalRight = left + baseLen;
      final dashPaint = Paint()..color = const Color(0x66FFFFFF)..strokeWidth = 1.5;
      double dy = midY - 24;
      while (dy < midY + 24) {
        canvas.drawLine(Offset(originalRight, dy), Offset(originalRight, dy + 6), dashPaint);
        dy += 10;
      }
      _label(canvas, 'original L₀', Offset(originalRight, midY + 38), const Color(0xFFA5A9BF), 9);
    } else {
      final growthSteel = baseLen * _alphaSteel * deltaT * visualFactor;
      final growthBrass = baseLen * _alphaBrass * deltaT * visualFactor;
      final diff = growthBrass - growthSteel;
      // Bend angle proportional to differential expansion.
      final bend = (diff / baseLen).clamp(-0.6, 0.6);
      final left = size.width * 0.22;

      canvas.save();
      canvas.translate(left, midY);
      canvas.rotate(0); // pivot fixed at left
      final segments = 24;
      final segLen = baseLen / segments;
      final pathTop = Path();
      final pathBottom = Path();
      Offset topPt = const Offset(0, -7);
      Offset botPt = const Offset(0, 7);
      pathTop.moveTo(topPt.dx, topPt.dy);
      pathBottom.moveTo(botPt.dx, botPt.dy);
      for (int i = 1; i <= segments; i++) {
        final dx = segLen * (i);
        final curve = bend * dx * 0.5 * (i / segments);
        topPt = Offset(dx, -7 - curve * 30);
        botPt = Offset(dx, 7 - curve * 30);
        pathTop.lineTo(topPt.dx, topPt.dy);
        pathBottom.lineTo(botPt.dx, botPt.dy);
      }
      // Draw brass (top) and steel (bottom) as two colored bands following the curve.
      final brassPaint = Paint()
        ..color = const Color(0xFFF59E0B)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 7
        ..strokeCap = StrokeCap.round;
      final steelPaint = Paint()
        ..color = const Color(0xFF64748B)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 7
        ..strokeCap = StrokeCap.round;
      canvas.drawPath(pathTop, brassPaint);
      canvas.drawPath(pathBottom, steelPaint);
      canvas.restore();

      _label(canvas, 'brass (α=19×10⁻⁶) — top', Offset(size.width / 2, midY - 46),
          const Color(0xFFF59E0B), 10);
      _label(canvas, 'steel (α=12×10⁻⁶) — bottom', Offset(size.width / 2, midY + 46),
          const Color(0xFF64748B), 10);
      _label(canvas, 'ΔT = ${deltaT.toStringAsFixed(0)}°C', Offset(size.width / 2, midY - 70),
          Colors.white, 12);
    }
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
  bool shouldRepaint(_ExpansionPainter old) => old.deltaT != deltaT || old.bimetal != bimetal;
}
