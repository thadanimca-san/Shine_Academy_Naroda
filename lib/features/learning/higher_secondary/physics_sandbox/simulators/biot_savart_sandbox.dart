import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Biot–Savart Sandbox — an infinite straight current-carrying wire with a
/// draggable observation point. Students change current I and the distance r
/// of the point from the wire and watch the field circles (right-hand rule)
/// and the live B = μ0 I / 2πr readout respond.
class BiotSavartSandbox extends StatefulWidget {
  const BiotSavartSandbox({super.key});

  @override
  State<BiotSavartSandbox> createState() => _BiotSavartSandboxState();
}

class _BiotSavartSandboxState extends State<BiotSavartSandbox> {
  double _current = 5.0; // amperes
  double _distancePx = 60; // pixels from wire (mapped to r in cm)
  bool _reversed = false; // current direction toggle

  // Model: use r in "relative cm" = distancePx / 4, keep numbers readable.
  double get _rMetres => _distancePx / 400; // px -> metres (toy scale)
  static const double _mu0Over2Pi = 2e-7; // μ0/2π = 2×10⁻⁷ T·m/A

  double get _fieldTesla => _mu0Over2Pi * _current / _rMetres;

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 240,
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
            onPanUpdate: (d) {
              setState(() {
                _distancePx = (_distancePx + d.delta.dx).clamp(24.0, 130.0);
              });
            },
            child: CustomPaint(
              painter: _WirePainter(
                current: _current,
                distancePx: _distancePx,
                reversed: _reversed,
                field: _fieldTesla,
              ),
              child: const SizedBox.expand(),
            ),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('Field  B = μ₀I/2πr', _fieldTesla.toStringAsExponential(2),
                  'T', Palette.chElectroMag)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Distance r', (_rMetres * 100).toStringAsFixed(1), 'cm', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Current I', _current, 0.5, 10, 'A', const Color(0xFF38BDF8),
            (x) => setState(() => _current = x)),
        Text(TrilingualService.instance.getUIText('Drag the observation dot in the scene to change r'),
            style: Type.caption.copyWith(fontSize: 11.5)),
        const SizedBox(height: Gap.x2),
        Row(children: [
          Expanded(
            child: OutlinedButton(
              onPressed: () => setState(() => _reversed = !_reversed),
              child: Text(_reversed ? 'Current: into page (reverse)' : 'Current: out of page'),
            ),
          ),
        ]),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: drag the point closer to the wire — B grows as 1/r. Reverse the current and every field circle flips direction with it (right-hand rule: thumb along I, fingers curl the way B points).'),
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

class _WirePainter extends CustomPainter {
  final double current, distancePx, field;
  final bool reversed;
  _WirePainter({
    required this.current,
    required this.distancePx,
    required this.reversed,
    required this.field,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final wireX = size.width / 2;

    // The wire, drawn vertically, current flowing along it.
    final wirePaint = Paint()
      ..color = const Color(0xFFF97316)
      ..strokeWidth = 5
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(Offset(wireX, 10), Offset(wireX, size.height - 10), wirePaint);

    // Direction arrow along the wire.
    final dir = reversed ? -1.0 : 1.0;
    final midY = size.height / 2;
    _arrow(canvas, Offset(wireX, midY - 30 * dir), Offset(wireX, midY + 30 * dir),
        const Color(0xFFFDBA74), 3);
    _label(canvas, 'I', Offset(wireX + 16, midY), const Color(0xFFFDBA74), 13);

    // Concentric field circles around the wire (right-hand rule sense).
    for (double r = 22; r < math.max(size.width, size.height); r += 26) {
      final rect = Rect.fromCircle(center: Offset(wireX, midY), radius: r);
      canvas.drawOval(
          rect,
          Paint()
            ..color = const Color(0x336D28D9)
            ..style = PaintingStyle.stroke
            ..strokeWidth = 1.4);
    }

    // Observation point on the right at `distancePx` from the wire.
    final obs = Offset(wireX + distancePx, midY);
    canvas.drawCircle(obs, 7, Paint()..color = Palette.accent);
    _label(canvas, 'P', obs + const Offset(0, -16), Palette.accent, 12);

    // r line from wire to point.
    canvas.drawLine(Offset(wireX, midY), obs,
        Paint()
          ..color = const Color(0x666D28D9)
          ..strokeWidth = 1.5);
    _label(canvas, 'r', Offset(wireX + distancePx / 2, midY - 12), const Color(0xFF9F7AEA), 11);

    // Field direction at P: tangent to the circle through P.
    // For current flowing +y (dir=+1, out toward bottom), by right-hand rule
    // the field on the right side (+x from wire) points into the page rotated
    // -> tangent direction (0,-1)*sign convention. We draw a simple tangent arrow.
    final tangent = Offset(0, -1) * dir; // up if current down-to-up... simplified consistent convention
    final bStart = obs;
    final bEnd = obs + tangent * 34;
    _arrow(canvas, bStart, bEnd, const Color(0xFF34D399), 2.5);
    _label(canvas, 'B', bEnd + Offset(tangent.dx * 14, tangent.dy * 14 - 2), const Color(0xFF34D399), 12);

    _label(canvas, reversed ? 'I into page ⊗ at top' : 'I flows downward ↓', Offset(size.width / 2, 16),
        const Color(0xFFFDBA74), 10);
  }

  void _arrow(Canvas canvas, Offset a, Offset b, Color color, double w) {
    final p = Paint()
      ..color = color
      ..strokeWidth = w
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(a, b, p);
    final dirV = b - a;
    final len = dirV.distance;
    if (len < 1) return;
    final un = dirV / len;
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
  bool shouldRepaint(_WirePainter old) =>
      old.current != current || old.distancePx != distancePx || old.reversed != reversed;
}
