import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Center of Mass Sandbox — three point masses on a horizontal line.
///
/// Students adjust each mass and its position; the COM marker updates live
/// as X_cm = Σmixi/Σmi, showing that the COM always sits closer to the
/// heavier mass and moves continuously and predictably with either masses
/// or positions.
class CenterOfMassSandbox extends StatefulWidget {
  const CenterOfMassSandbox({super.key});

  @override
  State<CenterOfMassSandbox> createState() => _CenterOfMassSandboxState();
}

class _CenterOfMassSandboxState extends State<CenterOfMassSandbox> {
  // Positions in metres along a 10 m line, masses in kg.
  double _m1 = 2, _m2 = 3, _m3 = 1;
  double _x1 = 1, _x2 = 5, _x3 = 8;

  double get _totalMass => _m1 + _m2 + _m3;
  double get _xcm => (_m1 * _x1 + _m2 * _x2 + _m3 * _x3) / _totalMass;

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 190,
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
            painter: _ComPainter(m1: _m1, m2: _m2, m3: _m3, x1: _x1, x2: _x2, x3: _x3, xcm: _xcm),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('X_cm = Σmᵢxᵢ/Σmᵢ', _xcm.toStringAsFixed(2), 'm', Palette.accent)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Total mass', _totalMass.toStringAsFixed(1), 'kg', const Color(0xFF38BDF8))),
        ]),
        const SizedBox(height: Gap.x3),
        _massRow('Mass 1', _m1, _x1, const Color(0xFF16A34A),
            (m) => setState(() => _m1 = m), (x) => setState(() => _x1 = x)),
        _massRow('Mass 2', _m2, _x2, const Color(0xFF38BDF8),
            (m) => setState(() => _m2 = m), (x) => setState(() => _x2 = x)),
        _massRow('Mass 3', _m3, _x3, const Color(0xFFF97316),
            (m) => setState(() => _m3 = m), (x) => setState(() => _x3 = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: drag mass 2 heavier and watch the golden COM marker slide TOWARD it — the centre of mass always sits closer to the bigger mass, exactly weighted by mᵢ. Spread all three masses out symmetrically and see the marker settle at the geometric middle.'),
            style: Type.caption.copyWith(color: Palette.primaryDeep),
          ),
        ),
      ],
    );
  }

  Widget _massRow(String label, double mass, double pos, Color color, ValueChanged<double> onMass,
      ValueChanged<double> onPos) {
    return Container(
      margin: const EdgeInsets.only(bottom: Gap.x2),
      padding: const EdgeInsets.all(Gap.x3),
      decoration: BoxDecoration(
        color: Palette.surface,
        borderRadius: BorderRadius.circular(Corner.md),
        border: Border.all(color: Palette.border),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(children: [
            Container(width: 10, height: 10, decoration: BoxDecoration(color: color, shape: BoxShape.circle)),
            const SizedBox(width: 6),
            Text(label, style: Type.bodyStrong.copyWith(fontSize: 13)),
          ]),
          _miniSlider('mass = ${mass.toStringAsFixed(1)} kg', mass, 0.5, 6, color, onMass),
          _miniSlider('position = ${pos.toStringAsFixed(1)} m', pos, 0, 10, color.withValues(alpha: 0.7), onPos),
        ],
      ),
    );
  }

  Widget _miniSlider(String label, double value, double min, double max, Color color, ValueChanged<double> onChanged) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(label, style: Type.caption.copyWith(fontSize: 11)),
        SliderTheme(
          data: SliderTheme.of(context).copyWith(
            activeTrackColor: color,
            thumbColor: color,
            overlayColor: color.withValues(alpha: 0.12),
            trackHeight: 3,
          ),
          child: Slider(value: value, min: min, max: max, onChanged: onChanged),
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
}

class _ComPainter extends CustomPainter {
  final double m1, m2, m3, x1, x2, x3, xcm;
  _ComPainter(
      {required this.m1,
      required this.m2,
      required this.m3,
      required this.x1,
      required this.x2,
      required this.x3,
      required this.xcm});

  static const double _worldLen = 10.0;

  double _px(double x, Size size) => 30 + (size.width - 60) * (x / _worldLen);

  @override
  void paint(Canvas canvas, Size size) {
    final lineY = size.height / 2 + 10;
    // Baseline rod.
    canvas.drawLine(Offset(30, lineY), Offset(size.width - 30, lineY),
        Paint()..color = const Color(0xFF9CA3E8)..strokeWidth = 3);

    _drawMass(canvas, _px(x1, size), lineY, m1, const Color(0xFF16A34A), 'm₁');
    _drawMass(canvas, _px(x2, size), lineY, m2, const Color(0xFF38BDF8), 'm₂');
    _drawMass(canvas, _px(x3, size), lineY, m3, const Color(0xFFF97316), 'm₃');

    // COM marker: a triangle below the rod plus vertical guide line.
    final cx = _px(xcm, size);
    canvas.drawLine(Offset(cx, lineY - 60), Offset(cx, lineY + 26),
        Paint()..color = Palette.accent.withValues(alpha: 0.55)..strokeWidth = 1.6);
    final tri = Path()
      ..moveTo(cx, lineY + 12)
      ..lineTo(cx - 9, lineY + 28)
      ..lineTo(cx + 9, lineY + 28)
      ..close();
    canvas.drawPath(tri, Paint()..color = Palette.accent);
    _label(canvas, 'X_cm', Offset(cx, lineY + 42), Palette.accent, 11);
  }

  void _drawMass(Canvas canvas, double x, double lineY, double mass, Color color, String label) {
    final r = 8 + mass * 2.4;
    canvas.drawCircle(Offset(x, lineY - r - 4), r, Paint()..color = color);
    canvas.drawCircle(Offset(x, lineY - r - 4), r,
        Paint()..color = Colors.white24..style = PaintingStyle.stroke..strokeWidth = 1.3);
    _label(canvas, label, Offset(x, lineY - r - 4), Colors.white, 10.5);
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
  bool shouldRepaint(_ComPainter old) =>
      old.m1 != m1 ||
      old.m2 != m2 ||
      old.m3 != m3 ||
      old.x1 != x1 ||
      old.x2 != x2 ||
      old.x3 != x3 ||
      old.xcm != xcm;
}
