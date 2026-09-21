import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Magnetic Force Sandbox — a single charge moving through a uniform field.
///
/// Students set the speed, the field strength, the charge sign and the angle
/// between v and B, then read the force magnitude F = qvB·sinθ and see the
/// F = qv×B vector pop out of the plane (right-hand rule made visible).
class MagneticForceSandbox extends StatefulWidget {
  const MagneticForceSandbox({super.key});

  @override
  State<MagneticForceSandbox> createState() => _MagneticForceSandboxState();
}

class _MagneticForceSandboxState extends State<MagneticForceSandbox> {
  double _v = 3.0e5; // speed, m/s (shown as ×10⁵)
  double _b = 0.5; // field, T
  double _q = 1.0; // charge, ×10⁻⁶ C (sign carries)
  double _theta = 90.0; // angle between v and B, degrees

  double get _force => _q.abs() * 1e-6 * _v * _b * math.sin(_theta * math.pi / 180);

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
            painter: _ForcePainter(
              theta: _theta, qSign: _q >= 0 ? 1 : -1, forceMag: _force,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Force  F = qvB sinθ',
              '${(_force * 1e6).toStringAsFixed(2)}', 'µN', Palette.accent)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Angle factor sinθ',
              math.sin(_theta * math.pi / 180).toStringAsFixed(2), '', Palette.primary)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Speed v', _v / 1e5, 0.5, 8, '×10⁵ m/s', const Color(0xFF38BDF8),
            (x) => setState(() => _v = x * 1e5)),
        _slider('Field B', _b, 0.1, 2.0, 'T', const Color(0xFFF97316),
            (x) => setState(() => _b = x)),
        _slider('Charge q', _q, -3, 3, '×10⁻⁶ C', Palette.accent,
            (x) => setState(() => _q = x)),
        _slider('Angle θ (v to B)', _theta, 0, 180, '°', Palette.primary,
            (x) => setState(() => _theta = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.primarySoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(
            _theta < 1 || _theta > 179
                ? 'θ ≈ 0 or 180° → v is parallel to B → force is ZERO. A charge fired along the field lines feels nothing.'
                : _q >= 0
                    ? 'Positive charge: F = qv×B points OUT of the screen (dot). Flip q negative to reverse it.'
                    : 'Negative charge: F points INTO the screen (cross). The sign of q flips the force direction.',
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
          Text(unit.isEmpty ? value : '$value $unit',
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
        Text('$label = ${value.toStringAsFixed(unit == '°' ? 0 : 2)} $unit',
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

class _ForcePainter extends CustomPainter {
  final double theta; // deg
  final int qSign;
  final double forceMag;
  _ForcePainter({required this.theta, required this.qSign, required this.forceMag});

  @override
  void paint(Canvas canvas, Size size) {
    final c = Offset(size.width / 2, size.height / 2);

    // Field region: dots = B out of screen (uniform, into the page grid).
    final dotPaint = Paint()..color = const Color(0x33F97316);
    for (double x = 26; x < size.width; x += 42) {
      for (double y = 24; y < size.height; y += 40) {
        canvas.drawCircle(Offset(x, y), 2.2, dotPaint);
      }
    }
    _label(canvas, 'B  (uniform field, out of screen)',
        Offset(size.width / 2, 14), const Color(0xFFF97316), 10);

    // Velocity vector v — drawn at angle θ from B. We treat B as pointing "up".
    final rad = theta * math.pi / 180;
    final vDir = Offset(math.sin(rad), -math.cos(rad));
    final vEnd = c + vDir * 62;
    _arrow(canvas, c, vEnd, const Color(0xFF38BDF8), 3);
    _label(canvas, 'v', vEnd + const Offset(10, -6), const Color(0xFF38BDF8), 13);

    // B reference direction (up).
    _arrow(canvas, c, c + const Offset(0, -70), const Color(0x88F97316), 2);
    _label(canvas, 'B', c + const Offset(-14, -74), const Color(0xFFF97316), 12);

    // Charge dot at origin.
    canvas.drawCircle(c, 9, Paint()..color = qSign >= 0 ? Palette.accent : const Color(0xFF38BDF8));
    _label(canvas, qSign >= 0 ? '+' : '−', c, Colors.black, 14);

    // Force symbol: out of screen (dot) for +q, into screen (cross) for −q.
    // Positioned off to the side to represent perpendicular-to-plane direction.
    if (forceMag > 1e-9) {
      final fc = c + const Offset(90, 40);
      final green = const Color(0xFF16A34A);
      canvas.drawCircle(fc, 16, Paint()
        ..color = green
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2.5);
      if (qSign >= 0) {
        canvas.drawCircle(fc, 3.5, Paint()..color = green);
      } else {
        final p = Paint()..color = green..strokeWidth = 2.5..strokeCap = StrokeCap.round;
        canvas.drawLine(fc + const Offset(-8, -8), fc + const Offset(8, 8), p);
        canvas.drawLine(fc + const Offset(-8, 8), fc + const Offset(8, -8), p);
      }
      _label(canvas, qSign >= 0 ? 'F out' : 'F in', fc + const Offset(0, 28), green, 10);
    } else {
      _label(canvas, 'F = 0', c + const Offset(90, 40), Palette.textFaint, 12);
    }
  }

  void _arrow(Canvas canvas, Offset a, Offset b, Color color, double w) {
    final p = Paint()..color = color..strokeWidth = w..strokeCap = StrokeCap.round;
    canvas.drawLine(a, b, p);
    final dir = (b - a);
    final len = dir.distance;
    if (len < 1) return;
    final u = dir / len;
    final n = Offset(-u.dy, u.dx);
    canvas.drawLine(b, b - u * 10 + n * 5, p);
    canvas.drawLine(b, b - u * 10 - n * 5, p);
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
  bool shouldRepaint(_ForcePainter old) =>
      old.theta != theta || old.qSign != qSign || old.forceMag != forceMag;
}
