import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Lenses Sandbox — a thin lens on the principal axis.
///
/// Students toggle converging/diverging, slide the object distance and the
/// focal length, and watch three standard rays trace out to locate the
/// image. The readout reports whether the image is real or virtual, upright
/// or inverted, and its magnification — all from the lens formula
/// 1/v − 1/u = 1/f under the Cartesian sign convention.
class LensesSandbox extends StatefulWidget {
  const LensesSandbox({super.key});

  @override
  State<LensesSandbox> createState() => _LensesSandboxState();
}

class _LensesSandboxState extends State<LensesSandbox> {
  bool _converging = true;
  double _objDist = 30.0; // |u| in cm (positive magnitude the student sets)
  double _focal = 15.0; // |f| in cm
  double _objHeight = 8.0; // cm, above axis

  // Cartesian convention: object on the left → u is negative.
  double get _u => -_objDist;
  // Converging lens: f positive. Diverging lens: f negative.
  double get _f => _converging ? _focal : -_focal;

  // Lens formula 1/v − 1/u = 1/f → v = uf/(u+f)
  double? get _v {
    final denom = _u + _f;
    if (denom.abs() < 1e-6) return null; // object at focus → image at infinity
    return _u * _f / denom;
  }

  double? get _m {
    final v = _v;
    if (v == null) return null;
    return v / _u; // m = v/u
  }

  @override
  Widget build(BuildContext context) {
    final v = _v;
    final m = _m;
    final real = v != null && v > 0; // real image forms on the far side (v positive)
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
            painter: _LensPainter(
              converging: _converging,
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
          padding: const EdgeInsets.symmetric(horizontal: Gap.x3, vertical: Gap.x2),
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

        // Lens type toggle
        Row(children: [
          Expanded(child: _typeButton('Converging', _converging, () {
            setState(() => _converging = true);
          })),
          const SizedBox(width: Gap.x3),
          Expanded(child: _typeButton('Diverging', !_converging, () {
            setState(() => _converging = false);
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
          border: Border.all(color: active ? Palette.primary : Palette.border),
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

class _LensPainter extends CustomPainter {
  final bool converging;
  final double u; // negative
  final double f; // signed
  final double? v; // signed or null
  final double objHeight;

  _LensPainter({
    required this.converging,
    required this.u,
    required this.f,
    required this.v,
    required this.objHeight,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final lensX = size.width * 0.55; // lens at centre
    final axisY = size.height * 0.52;
    const scale = 2.0; // px per cm

    double sx(double cm) => lensX + cm * scale; // cm are signed (left = neg)
    double sy(double cm) => axisY - cm * scale;

    // Principal axis
    canvas.drawLine(Offset(0, axisY), Offset(size.width, axisY),
        Paint()..color = Palette.stageLine..strokeWidth = 1.5);

    // Lens body: biconvex (converging) or biconcave (diverging) symbol.
    final lensPaint = Paint()
      ..color = Colors.white70
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3;
    const arcH = 62.0;
    if (converging) {
      final path = Path()
        ..moveTo(lensX, axisY - arcH)
        ..quadraticBezierTo(lensX + 16, axisY, lensX, axisY + arcH)
        ..quadraticBezierTo(lensX - 16, axisY, lensX, axisY - arcH);
      canvas.drawPath(path, lensPaint);
    } else {
      canvas.drawLine(Offset(lensX, axisY - arcH), Offset(lensX, axisY + arcH), lensPaint);
      final path = Path()
        ..moveTo(lensX - 10, axisY - arcH + 8)
        ..quadraticBezierTo(lensX, axisY - arcH + 22, lensX + 10, axisY - arcH + 8);
      canvas.drawPath(path, lensPaint);
      final path2 = Path()
        ..moveTo(lensX - 10, axisY + arcH - 8)
        ..quadraticBezierTo(lensX, axisY + arcH - 22, lensX + 10, axisY + arcH - 8);
      canvas.drawPath(path2, lensPaint);
    }

    // F markers on both sides (converging: real foci; diverging: virtual foci).
    final fMag = f.abs();
    _dot(canvas, Offset(sx(-fMag), axisY), Colors.white54, 'F');
    _dot(canvas, Offset(sx(fMag), axisY), Colors.white54, 'F');
    _dot(canvas, Offset(sx(-2 * fMag), axisY), Colors.white38, '2F');
    _dot(canvas, Offset(sx(2 * fMag), axisY), Colors.white38, '2F');

    // Object: upright arrow on the axis at u (left side).
    final objX = sx(u);
    final objTop = Offset(objX, sy(objHeight));
    _arrow(canvas, Offset(objX, axisY), objTop, const Color(0xFF34D399), 'object');

    final tip = objTop;
    final rayP = Paint()
      ..color = const Color(0xFFFBBF24)
      ..strokeWidth = 1.8
      ..style = PaintingStyle.stroke;

    // Ray 1: parallel to axis → after lens, bends through far F (converging)
    // or appears to diverge from near F (diverging).
    final hitParallel = Offset(lensX, tip.dy);
    canvas.drawLine(tip, hitParallel, rayP);
    if (converging) {
      _throughPoint(canvas, hitParallel, Offset(sx(fMag), axisY), rayP, size);
    } else {
      // Bends away as if from near-side F; draw solid forward ray plus dashed backward trace.
      final appearFrom = Offset(sx(-fMag), axisY);
      final dir = hitParallel - appearFrom;
      final norm = dir / dir.distance;
      final end = hitParallel + norm * (size.width);
      canvas.drawLine(hitParallel, end, rayP);
      _dashed(canvas, hitParallel, appearFrom, const Color(0xFFFBBF24));
    }

    // Ray 2: through the optical centre → goes straight, undeviated.
    final centre = Offset(lensX, axisY);
    canvas.drawLine(tip, centre, rayP);
    final slope = (centre.dy - tip.dy) / (centre.dx - tip.dx);
    final farEnd = Offset(size.width, centre.dy + slope * (size.width - centre.dx));
    canvas.drawLine(centre, farEnd, rayP);

    // Ray 3: through near-side focal point (converging) or heading toward far
    // F (diverging) → emerges parallel to the axis.
    if (converging) {
      final nearF = Offset(sx(-fMag), axisY);
      // Ray from tip through nearF, hits lens plane, then emerges parallel to the axis.
      final slopeIn = (axisY - tip.dy) / (nearF.dx - objX);
      final hitX = lensX;
      final hitY = tip.dy + slopeIn * (hitX - objX);
      final hitPt = Offset(hitX, hitY);
      canvas.drawLine(tip, hitPt, rayP);
      canvas.drawLine(hitPt, Offset(size.width, hitPt.dy), rayP);
    } else {
      // Ray directed toward the far-side F emerges parallel to the axis.
      final farF = Offset(sx(fMag), axisY);
      final slopeIn = (axisY - tip.dy) / (farF.dx - objX);
      final hitX = lensX;
      final hitY = tip.dy + slopeIn * (hitX - objX);
      final hitPt = Offset(hitX, hitY);
      canvas.drawLine(tip, hitPt, rayP);
      canvas.drawLine(hitPt, Offset(size.width, hitPt.dy), rayP);
      _dashed(canvas, hitPt, farF, const Color(0xFFFBBF24));
    }

    // Image arrow (if finite).
    if (v != null) {
      final imgX = sx(v!);
      final mag = v! / u;
      final imgH = objHeight * mag; // signed
      final imgTip = Offset(imgX, sy(imgH));
      final realImg = v! > 0;
      final imgColor = realImg ? const Color(0xFF60A5FA) : const Color(0xFFC084FC);
      _arrow(canvas, Offset(imgX, axisY), imgTip, imgColor, realImg ? 'real image' : 'virtual');
    }
  }

  void _throughPoint(Canvas canvas, Offset hit, Offset through, Paint p, Size size) {
    final dx = through.dx - hit.dx;
    final dy = through.dy - hit.dy;
    if (dx.abs() < 1e-6) return;
    final slope = dy / dx;
    final endX = size.width;
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
    if (total < 1) return;
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
  bool shouldRepaint(_LensPainter old) =>
      old.converging != converging || old.u != u || old.f != f || old.v != v || old.objHeight != objHeight;
}
