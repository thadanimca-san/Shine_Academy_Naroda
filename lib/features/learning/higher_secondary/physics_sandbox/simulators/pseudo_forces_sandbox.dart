import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Pseudo Forces Sandbox — a block standing on a weighing scale inside a
/// lift. Students drag the lift's acceleration (positive = upward) and
/// toggle between the ground-frame view (only real forces: gravity + normal
/// reaction) and the lift-frame view (a pseudo-force ma appears, opposite to
/// the lift's acceleration, needed to make Newton's laws work in that
/// non-inertial frame).
class PseudoForcesSandbox extends StatefulWidget {
  const PseudoForcesSandbox({super.key});

  @override
  State<PseudoForcesSandbox> createState() => _PseudoForcesSandboxState();
}

class _PseudoForcesSandboxState extends State<PseudoForcesSandbox> {
  double _a = 0; // lift acceleration, m/s^2, +ve = upward
  double _m = 60; // kg (person on the scale)
  static const double _g = 9.8;
  bool _liftFrame = false; // false = ground frame, true = lift frame

  double get _apparentWeight => _m * (_g + _a); // Normal force reading (N)
  double get _pseudoForce => -_m * _a; // opposite to lift's acceleration

  @override
  Widget build(BuildContext context) {
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
            painter: _LiftPainter(a: _a, liftFrame: _liftFrame, weight: _apparentWeight, m: _m, g: _g),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        // Frame toggle
        Row(children: [
          Expanded(child: _frameButton('Ground frame', !_liftFrame, () => setState(() => _liftFrame = false))),
          const SizedBox(width: Gap.x2),
          Expanded(child: _frameButton('Lift frame', _liftFrame, () => setState(() => _liftFrame = true))),
        ]),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('Apparent weight N', _apparentWeight.toStringAsFixed(0), 'N',
                  const Color(0xFF38BDF8))),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter(_liftFrame ? 'Pseudo-force' : 'Real net force', _liftFrame
                  ? _pseudoForce.toStringAsFixed(0)
                  : (_m * _a).toStringAsFixed(0), 'N', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Lift acceleration a', _a, -6, 6, 'm/s²', const Color(0xFFF97316),
            (x) => setState(() => _a = x)),
        _slider('Mass m', _m, 20, 100, 'kg', const Color(0xFF16A34A), (x) => setState(() => _m = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(
            _liftFrame
                ? 'Lift frame: to make F=ma work here (the person is at rest relative to the lift), we must ADD a fictitious pseudo-force = -ma, opposite to the lift\'s acceleration. It has no real source and no Newton\'s-third-law partner.'
                : 'Ground frame: only two REAL forces act — gravity mg down, and the normal reaction N up from the scale. Apply F_net = ma: N − mg = ma, so N = m(g+a). This N is exactly what the scale reads — your "apparent weight."',
            style: Type.caption.copyWith(color: Palette.primaryDeep),
          ),
        ),
      ],
    );
  }

  Widget _frameButton(String label, bool selected, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: AnimatedContainer(
        duration: Motion.base,
        curve: Motion.ease,
        padding: const EdgeInsets.symmetric(vertical: Gap.x3),
        decoration: BoxDecoration(
          color: selected ? Palette.primary : Palette.surfaceAlt,
          borderRadius: BorderRadius.circular(Corner.md),
          border: Border.all(color: selected ? Palette.primary : Palette.border),
        ),
        alignment: Alignment.center,
        child: Text(label,
            style: Type.bodyStrong.copyWith(
                color: selected ? Colors.white : Palette.textBody, fontSize: 13)),
      ),
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

class _LiftPainter extends CustomPainter {
  final double a, weight, m, g;
  final bool liftFrame;
  _LiftPainter({required this.a, required this.liftFrame, required this.weight, required this.m, required this.g});

  @override
  void paint(Canvas canvas, Size size) {
    // Lift shaft.
    final shaftW = 120.0;
    final shaftRect = Rect.fromCenter(
        center: Offset(size.width / 2, size.height / 2 + 6), width: shaftW, height: size.height - 40);
    canvas.drawRRect(RRect.fromRectAndRadius(shaftRect, const Radius.circular(6)),
        Paint()..color = const Color(0x22FFFFFF));
    canvas.drawRRect(
        RRect.fromRectAndRadius(shaftRect, const Radius.circular(6)),
        Paint()
          ..color = const Color(0x55FFFFFF)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.5);

    // Cabin floor near the bottom of the shaft.
    final floorY = shaftRect.bottom - 46;
    canvas.drawLine(Offset(shaftRect.left + 8, floorY), Offset(shaftRect.right - 8, floorY),
        Paint()..color = const Color(0xFF9CA3E8)..strokeWidth = 3);

    // Person (simple stick figure block) standing on the floor.
    final personX = size.width / 2;
    final personBaseY = floorY;
    final bodyPaint = Paint()..color = Palette.accent;
    canvas.drawRRect(
        RRect.fromRectAndRadius(
            Rect.fromLTRB(personX - 12, personBaseY - 46, personX + 12, personBaseY - 4),
            const Radius.circular(6)),
        bodyPaint);
    canvas.drawCircle(Offset(personX, personBaseY - 54), 9, bodyPaint);

    // Gravity arrow (always present, real force).
    _arrow(canvas, Offset(personX - 30, personBaseY - 30), Offset(personX - 30, personBaseY - 30 + 34),
        const Color(0xFFDC2626), 2.5);
    _label(canvas, 'mg', Offset(personX - 30, personBaseY - 30 + 46), const Color(0xFFDC2626), 10);

    // Normal reaction arrow (always present, real force) — length ∝ weight.
    final nLen = (weight / (m * g) * 34).clamp(10.0, 60.0);
    _arrow(canvas, Offset(personX + 30, personBaseY - 4), Offset(personX + 30, personBaseY - 4 - nLen),
        const Color(0xFF38BDF8), 2.5);
    _label(canvas, 'N', Offset(personX + 30, personBaseY - 4 - nLen - 12), const Color(0xFF38BDF8), 10);

    // Lift acceleration indicator arrow, drawn on the cabin frame.
    if (a.abs() > 0.05) {
      final dir = a > 0 ? -1.0 : 1.0; // up = negative y
      final start = Offset(shaftRect.right + 18, floorY);
      final end = Offset(shaftRect.right + 18, floorY + dir * 30);
      _arrow(canvas, start, end, const Color(0xFFF97316), 2.5);
      _label(canvas, 'a', Offset(shaftRect.right + 18, floorY + dir * 30 + (dir > 0 ? 14 : -14)),
          const Color(0xFFF97316), 10);
    }

    // Pseudo-force arrow, ONLY drawn in lift-frame view.
    if (liftFrame && a.abs() > 0.05) {
      final dir = a > 0 ? 1.0 : -1.0; // opposite to a: a up -> pseudo force down
      final start = Offset(personX, personBaseY - 26);
      final end = Offset(personX, personBaseY - 26 + dir * 36);
      _arrow(canvas, start, end, const Color(0xFFA78BFA), 3);
      _label(canvas, 'F_pseudo = -ma', Offset(personX, personBaseY - 26 + dir * 36 + (dir > 0 ? 14 : -14)),
          const Color(0xFFA78BFA), 10.5);
    }

    _label(canvas, liftFrame ? 'LIFT FRAME (non-inertial)' : 'GROUND FRAME (inertial)',
        Offset(size.width / 2, 16), Colors.white70, 11);
  }

  void _arrow(Canvas canvas, Offset a0, Offset b, Color color, double w) {
    final p = Paint()
      ..color = color
      ..strokeWidth = w
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(a0, b, p);
    final dir = b - a0;
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
      textAlign: TextAlign.center,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_LiftPainter old) =>
      old.a != a || old.liftFrame != liftFrame || old.weight != weight || old.m != m;
}
