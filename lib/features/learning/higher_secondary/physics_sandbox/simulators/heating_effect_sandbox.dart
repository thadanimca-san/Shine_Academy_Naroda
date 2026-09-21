import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Heating Effect Sandbox — a resistive heating element glows brighter and
/// hotter (color shift) as power P = I²R rises. A time slider accumulates
/// total heat Q = I²Rt.
class HeatingEffectSandbox extends StatefulWidget {
  const HeatingEffectSandbox({super.key});

  @override
  State<HeatingEffectSandbox> createState() => _HeatingEffectSandboxState();
}

class _HeatingEffectSandboxState extends State<HeatingEffectSandbox> {
  double _current = 3.0; // amps
  double _resistance = 4.0; // ohms
  double _timeS = 10.0; // seconds

  double get _power => _current * _current * _resistance; // watts
  double get _heatJ => _power * _timeS; // joules
  double get _heatCal => _heatJ / 4.186;

  @override
  Widget build(BuildContext context) {
    final power = _power;
    final glow = (power / 200).clamp(0.0, 1.0); // 0..1 intensity

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
            painter: _ElementPainter(glow: glow, current: _current),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Power  P = I²R', power.toStringAsFixed(1), 'W', Palette.chElectroMag)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Heat  Q = I²Rt', _heatJ.toStringAsFixed(0), 'J', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x2),
        _meter('Heat in calories', _heatCal.toStringAsFixed(1), 'cal', const Color(0xFFF97316)),
        const SizedBox(height: Gap.x3),
        _slider('Current I', _current, 0.5, 10, 'A', Palette.chElectroMag,
            (x) => setState(() => _current = x)),
        _slider('Resistance R', _resistance, 0.5, 10, 'Ω', const Color(0xFF38BDF8),
            (x) => setState(() => _resistance = x)),
        _slider('Time t', _timeS, 1, 60, 's', const Color(0xFF16A34A),
            (x) => setState(() => _timeS = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: double the current and watch power quadruple (P ∝ I²) — the element glows from a dull red to a searing white far faster than a simple doubling. This I² dependence is exactly why thin wires and loose connections overheat and fail.'),
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

class _ElementPainter extends CustomPainter {
  final double glow; // 0..1
  final double current;
  _ElementPainter({required this.glow, required this.current});

  Color _glowColor(double g) {
    // dull red -> orange -> yellow-white as glow rises
    if (g < 0.35) {
      return Color.lerp(const Color(0xFF7F1D1D), const Color(0xFFDC2626), g / 0.35)!;
    } else if (g < 0.7) {
      return Color.lerp(const Color(0xFFDC2626), const Color(0xFFF97316), (g - 0.35) / 0.35)!;
    }
    return Color.lerp(const Color(0xFFF97316), const Color(0xFFFEF3C7), (g - 0.7) / 0.3)!;
  }

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final color = _glowColor(glow);

    // Outer glow halo, radius/opacity scale with power.
    final haloR = 40 + glow * 70;
    canvas.drawCircle(
      center,
      haloR,
      Paint()
        ..color = color.withValues(alpha: 0.25 * glow + 0.05)
        ..maskFilter = MaskFilter.blur(BlurStyle.normal, 20 + glow * 20),
    );

    // Coiled heating element (zig-zag).
    final path = Path();
    final coilWidth = size.width * 0.55;
    final startX = center.dx - coilWidth / 2;
    final endX = center.dx + coilWidth / 2;
    const coils = 8;
    path.moveTo(startX, center.dy);
    for (var i = 1; i <= coils; i++) {
      final x = startX + (endX - startX) * i / coils;
      final y = center.dy + (i.isOdd ? -22.0 : 22.0);
      path.lineTo(x, y);
    }
    canvas.drawPath(
      path,
      Paint()
        ..color = color
        ..style = PaintingStyle.stroke
        ..strokeWidth = 6 + glow * 2
        ..strokeCap = StrokeCap.round,
    );
    // Bright core line for high glow.
    if (glow > 0.5) {
      canvas.drawPath(
        path,
        Paint()
          ..color = Colors.white.withValues(alpha: (glow - 0.5) * 1.2)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2,
      );
    }

    _label(canvas, '${(glow * 100).toStringAsFixed(0)}% max glow', Offset(center.dx, size.height - 20),
        Colors.white70, 10.5);
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
  bool shouldRepaint(_ElementPainter old) => old.glow != glow || old.current != current;
}
