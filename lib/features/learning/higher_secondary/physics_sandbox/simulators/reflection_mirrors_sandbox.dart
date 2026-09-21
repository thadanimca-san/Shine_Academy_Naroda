import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Reflection & Mirrors Sandbox — a spherical mirror on the principal axis.
///
/// Students toggle concave/convex, slide the object distance and the focal
/// length, and watch two standard rays trace out to locate the image. The
/// readout reports whether the image is real or virtual, upright or inverted,
/// and its magnification — all from the mirror formula 1/v + 1/u = 1/f under
/// the New Cartesian sign convention.
class ReflectionMirrorsSandbox extends StatefulWidget {
  const ReflectionMirrorsSandbox({super.key});

  @override
  State<ReflectionMirrorsSandbox> createState() =>
      _ReflectionMirrorsSandboxState();
}

class _ReflectionMirrorsSandboxState extends State<ReflectionMirrorsSandbox> {
  bool _concave = true;
  double _objDist = 30.0; // |u| in cm (positive magnitude the student sets)
  double _focal = 15.0; // |f| in cm
  double _objHeight = 8.0; // cm, above axis

  // New Cartesian: object on the left → u is negative.
  double get _u => -_objDist;
  // Concave mirror: f negative. Convex mirror: f positive.
  double get _f => _concave ? -_focal : _focal;

  // Mirror formula 1/v + 1/u = 1/f → v = uf/(u−f)
  double? get _v {
    final denom = _u - _f;
    if (denom.abs() < 1e-6) return null; // object at focus → image at infinity
    return _u * _f / denom;
  }

  double? get _m {
    final v = _v;
    if (v == null) return null;
    return -v / _u; // m = −v/u
  }

  @override
  Widget build(BuildContext context) {
    final v = _v;
    final m = _m;
    final real = v != null && v < 0; // real image forms in front (v negative)
    final inverted = m != null && m < 0;

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
            painter: _MirrorPainter(
              concave: _concave,
              u: _u,
              f: _f,
              v: v,
              objHeight: _objHeight,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),

        // Live readouts
        Row(children: [
          Expanded(
            child: _readout(
              'Image distance v',
              v == null ? '∞' : '${v.toStringAsFixed(1)} cm',
              Palette.info,
            ),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _readout(
              'Magnification m',
              m == null ? '∞' : m.toStringAsFixed(2),
              Palette.accent,
            ),
          ),
        ]),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.symmetric(
              horizontal: Gap.x3, vertical: Gap.x2),
          decoration: BoxDecoration(
            color: real ? Palette.successSoft : Palette.infoSoft,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Text(
            v == null
                ? 'Object at focus → rays emerge parallel → image at infinity.'
                : '${real ? "REAL" : "VIRTUAL"} · '
                    '${inverted ? "INVERTED" : "UPRIGHT"} · '
                    '${m!.abs() > 1 ? "MAGNIFIED" : m.abs() < 1 ? "DIMINISHED" : "SAME SIZE"}',
            style: Type.bodyStrong.copyWith(fontSize: 13),
          ),
        ),
        const SizedBox(height: Gap.x3),

        // Mirror type toggle
        Row(children: [
          Expanded(child: _typeButton('Concave', _concave, () {
            setState(() => _concave = true);
          })),
          const SizedBox(width: Gap.x3),
          Expanded(child: _typeButton('Convex', !_concave, () {
            setState(() => _concave = false);
          })),
        ]),
        const SizedBox(height: Gap.x2),

        _slider('Object distance |u|', _objDist, 5, 60, 'cm', Palette.primary,
            (val) => setState(() => _objDist = val)),
        _slider('Focal length |f|', _focal, 6, 30, 'cm', Palette.jee,
            (val) => setState(() => _focal = val)),
        _slider('Object height', _objHeight, 3, 12, 'cm', Palette.neet,
            (val) => setState(() => _objHeight = val)),
      ],
    );
  }

  Widget _typeButton(String label, bool active, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 11),
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: active ? Palette.primary : Palette.surface,
          borderRadius: BorderRadius.circular(Corner.md),
          border: Border.all(
              color: active ? Palette.primary : Palette.border),
        ),
        child: Text(
          label,
          style: Type.bodyStrong.copyWith(
              color: active ? Colors.white : Palette.textBody, fontSize: 14),
        ),
      ),
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
        Text('$label = ${value.toStringAsFixed(1)} $unit',
            style: Type.caption
                .copyWith(fontSize: 12, fontWeight: FontWeight.w600)),
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

class _MirrorPainter extends CustomPainter {
  final bool concave;
  final double u; // negative
  final double f; // signed
  final double? v; // signed or null
  final double objHeight;

  _MirrorPainter({
    required this.concave,
    required this.u,
    required this.f,
    required this.v,
    required this.objHeight,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final poleX = size.width * 0.62; // mirror pole near the right
    final axisY = size.height * 0.52;
    const scale = 2.2; // px per cm

    double sx(double cm) => poleX + cm * scale; // cm are signed (left = neg)
    double sy(double cm) => axisY - cm * scale;

    // Principal axis
    canvas.drawLine(Offset(0, axisY), Offset(size.width, axisY),
        Paint()..color = Palette.stageLine..strokeWidth = 1.5);

    // Mirror arc (concave curves toward the object → center to the left)
    final mirrorPaint = Paint()
      ..color = Colors.white70
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3;
    final path = Path();
    const arcH = 62.0;
    final bulge = concave ? -14.0 : 14.0; // concave dips left
    path.moveTo(poleX, axisY - arcH);
    path.quadraticBezierTo(poleX + bulge, axisY, poleX, axisY + arcH);
    canvas.drawPath(path, mirrorPaint);

    // F and C markers (f<0 → left for concave). |C| = 2|f|.
    final fx = sx(f);
    final cx = sx(2 * f);
    _dot(canvas, Offset(fx, axisY), Colors.white54, 'F');
    _dot(canvas, Offset(cx, axisY), Colors.white38, 'C');

    // Object: upright arrow on the axis at u (left side).
    final objX = sx(u);
    final objTop = Offset(objX, sy(objHeight));
    _arrow(canvas, Offset(objX, axisY), objTop,
        const Color(0xFF34D399), 'object');

    // Two rays from the object tip.
    final tip = objTop;
    final rayP = Paint()
      ..color = const Color(0xFFFBBF24)
      ..strokeWidth = 1.8
      ..style = PaintingStyle.stroke;

    // Ray 1: parallel to axis → reflects through F.
    final hitParallel = Offset(poleX, tip.dy);
    canvas.drawLine(tip, hitParallel, rayP);
    // reflected line direction: from hit toward F (or its backward extension)
    _drawReflected(canvas, hitParallel, Offset(fx, axisY), rayP, concave, size);

    // Ray 2: toward the pole → reflects symmetrically about the axis.
    final pole = Offset(poleX, axisY);
    canvas.drawLine(tip, pole, rayP);
    final slope = (pole.dy - tip.dy) / (pole.dx - tip.dx);
    final reflEnd = Offset(0, pole.dy + slope * (pole.dx - 0));
    canvas.drawLine(pole, reflEnd, rayP);

    // Image arrow (if finite).
    if (v != null) {
      final imgX = sx(v!);
      final mag = -v! / u;
      final imgH = objHeight * mag; // signed
      final imgTip = Offset(imgX, sy(imgH));
      final real = v! < 0;
      final imgColor =
          real ? const Color(0xFF60A5FA) : const Color(0xFFC084FC);
      _arrow(canvas, Offset(imgX, axisY), imgTip, imgColor,
          real ? 'real image' : 'virtual');
      if (!real) {
        // dashed extension behind mirror
        _dashed(canvas, hitParallel, imgTip, imgColor);
      }
    }
  }

  void _drawReflected(Canvas canvas, Offset hit, Offset through, Paint p,
      bool concave, Size size) {
    // Reflected ray passes through F (concave, real) or appears to come from F.
    final dx = through.dx - hit.dx;
    final dy = through.dy - hit.dy;
    if (dx.abs() < 1e-6) return;
    final slope = dy / dx;
    final endX = 0.0;
    final endY = hit.dy + slope * (endX - hit.dx);
    canvas.drawLine(hit, Offset(endX, endY), p);
  }

  void _arrow(Canvas canvas, Offset base, Offset tip, Color color, String tag) {
    final p = Paint()
      ..color = color
      ..strokeWidth = 2.5
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(base, tip, p);
    final dir = (tip.dy < base.dy) ? -1.0 : 1.0;
    canvas.drawLine(tip, tip + Offset(-4, 7 * dir), p);
    canvas.drawLine(tip, tip + Offset(4, 7 * dir), p);
    _label(canvas, tag, tip + Offset(0, dir < 0 ? -10 : 12), color, 9);
  }

  void _dashed(Canvas canvas, Offset a, Offset b, Color color) {
    final p = Paint()
      ..color = color.withValues(alpha: 0.5)
      ..strokeWidth = 1.2;
    const dash = 5.0;
    final total = (b - a).distance;
    final dir = (b - a) / total;
    double t = 0;
    while (t < total) {
      final start = a + dir * t;
      final end = a + dir * math.min(t + dash, total);
      canvas.drawLine(start, end, p);
      t += dash * 2;
    }
  }

  void _dot(Canvas canvas, Offset o, Color color, String label) {
    canvas.drawCircle(o, 3, Paint()..color = color);
    _label(canvas, label, o + const Offset(0, 12), color, 9);
  }

  void _label(Canvas canvas, String text, Offset center, Color color,
      double fontSize) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(
              color: color,
              fontSize: fontSize,
              fontWeight: FontWeight.w700,
              fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_MirrorPainter old) =>
      old.concave != concave ||
      old.u != u ||
      old.f != f ||
      old.v != v ||
      old.objHeight != objHeight;
}
