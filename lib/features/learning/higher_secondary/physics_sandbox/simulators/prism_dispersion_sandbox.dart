import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Prism & Dispersion Sandbox — a triangular prism refracting light.
///
/// Students adjust the prism's apex angle A and the angle of incidence i1,
/// and watch the ray bend at both faces to produce a total deviation δ.
/// A dispersion toggle switches the single ray for a fan of six spectral
/// colours (violet bending most, red least), visualising why white light
/// splits into a rainbow inside a prism.
class PrismDispersionSandbox extends StatefulWidget {
  const PrismDispersionSandbox({super.key});

  @override
  State<PrismDispersionSandbox> createState() => _PrismDispersionSandboxState();
}

class _PrismDispersionSandboxState extends State<PrismDispersionSandbox> {
  double _apexDeg = 60.0; // prism angle A
  double _incidenceDeg = 45.0; // angle of incidence i1
  double _nBase = 1.50; // refractive index for the "average" ray
  bool _dispersion = false;

  static const List<_SpectrumBand> _bands = [
    _SpectrumBand('Violet', Color(0xFF7C3AED), 0.030),
    _SpectrumBand('Blue', Color(0xFF3B82F6), 0.020),
    _SpectrumBand('Green', Color(0xFF22C55E), 0.010),
    _SpectrumBand('Yellow', Color(0xFFEAB308), 0.004),
    _SpectrumBand('Orange', Color(0xFFF97316), -0.006),
    _SpectrumBand('Red', Color(0xFFEF4444), -0.016),
  ];

  double get _apexRad => _apexDeg * math.pi / 180;
  double get _i1 => _incidenceDeg * math.pi / 180;

  // Trace refraction through both faces for a given refractive index n.
  // Returns (r1, r2, i2, delta) in radians, or null if TIR occurs at face 2.
  _PrismTrace? _trace(double n) {
    final sinR1 = math.sin(_i1) / n;
    if (sinR1.abs() > 1) return null;
    final r1 = math.asin(sinR1);
    final r2 = _apexRad - r1;
    if (r2.abs() > math.pi / 2) return null;
    final sinI2 = n * math.sin(r2);
    if (sinI2.abs() > 1) return null; // TIR at second face
    final i2 = math.asin(sinI2);
    final delta = _i1 + i2 - _apexRad;
    return _PrismTrace(r1: r1, r2: r2, i2: i2, delta: delta);
  }

  @override
  Widget build(BuildContext context) {
    final trace = _trace(_nBase);

    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 220,
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
            painter: _PrismPainter(
              apex: _apexRad,
              incidence: _i1,
              nBase: _nBase,
              dispersion: _dispersion,
              bands: _bands,
              traceFn: _trace,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
            child: _readout(
              'Deviation δ',
              trace == null ? 'TIR' : '${(trace.delta * 180 / math.pi).toStringAsFixed(1)}°',
              Palette.info,
            ),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _readout(
              'Refraction r1, r2',
              trace == null
                  ? '—'
                  : '${(trace.r1 * 180 / math.pi).toStringAsFixed(0)}°, ${(trace.r2 * 180 / math.pi).toStringAsFixed(0)}°',
              Palette.accent,
            ),
          ),
        ]),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: Gap.x3, vertical: Gap.x2),
          decoration: BoxDecoration(
            color: trace == null ? Palette.dangerSoft : Palette.infoSoft,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Text(
            trace == null
                ? 'Total internal reflection at the second face — no ray emerges. Reduce A or change i1.'
                : 'δ = (i1 + i2) − A. Try nudging i1 to find the angle that MINIMISES δ (minimum deviation).',
            style: Type.bodyStrong.copyWith(fontSize: 13),
          ),
        ),
        const SizedBox(height: Gap.x3),

        Row(children: [
          Expanded(child: _typeButton('Single colour', !_dispersion, () {
            setState(() => _dispersion = false);
          })),
          const SizedBox(width: Gap.x3),
          Expanded(child: _typeButton('White light (dispersion)', _dispersion, () {
            setState(() => _dispersion = true);
          })),
        ]),
        const SizedBox(height: Gap.x2),

        _slider('Prism angle A', _apexDeg, 30, 75, '°', Palette.primary,
            (val) => setState(() => _apexDeg = val)),
        _slider('Angle of incidence i1', _incidenceDeg, 20, 80, '°', Palette.jee,
            (val) => setState(() => _incidenceDeg = val)),
        _slider('Refractive index n', _nBase, 1.40, 1.70, '', Palette.neet,
            (val) => setState(() => _nBase = val)),
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
              color: active ? Colors.white : Palette.textBody, fontSize: 13),
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

class _SpectrumBand {
  final String name;
  final Color color;
  final double nOffset; // added to nBase; violet bends most (+), red least (−)
  const _SpectrumBand(this.name, this.color, this.nOffset);
}

class _PrismTrace {
  final double r1, r2, i2, delta;
  const _PrismTrace({required this.r1, required this.r2, required this.i2, required this.delta});
}

class _PrismPainter extends CustomPainter {
  final double apex; // A, radians
  final double incidence; // i1, radians
  final double nBase;
  final bool dispersion;
  final List<_SpectrumBand> bands;
  final _PrismTrace? Function(double n) traceFn;

  _PrismPainter({
    required this.apex,
    required this.incidence,
    required this.nBase,
    required this.dispersion,
    required this.bands,
    required this.traceFn,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final apexPt = Offset(size.width * 0.5, size.height * 0.18);
    const baseHalfWidth = 95.0;
    final baseY = size.height * 0.78;
    final leftBase = Offset(apexPt.dx - baseHalfWidth, baseY);
    final rightBase = Offset(apexPt.dx + baseHalfWidth, baseY);

    // Prism outline (isosceles triangle, apex angle purely illustrative).
    final prismPath = Path()
      ..moveTo(apexPt.dx, apexPt.dy)
      ..lineTo(leftBase.dx, leftBase.dy)
      ..lineTo(rightBase.dx, rightBase.dy)
      ..close();
    canvas.drawPath(prismPath, Paint()..color = const Color(0x22FFFFFF));
    canvas.drawPath(
        prismPath,
        Paint()
          ..color = Colors.white70
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2);

    _label(canvas, 'A', apexPt + const Offset(0, 16), Colors.white70, 11);

    // Incident ray direction: comes in at angle `incidence` from the normal
    // to the LEFT face. Normal to left face points up-left.
    final leftFaceDir = (leftBase - apexPt) / (leftBase - apexPt).distance;
    final leftNormal = Offset(-leftFaceDir.dy, leftFaceDir.dx); // outward-ish normal

    // Entry point on the left face (fixed partway down for a stable visual).
    final entry = apexPt + (leftBase - apexPt) * 0.55;

    // Incident ray comes from outside, at `incidence` measured from leftNormal.
    final inDir = _rotate(leftNormal, incidence);
    final incidentStart = entry - inDir * 90;
    _ray(canvas, incidentStart, entry, Colors.white, 2.2);

    if (!dispersion) {
      final t = traceFn(nBase);
      if (t != null) {
        _drawRefractedPath(canvas, size, apexPt, leftBase, rightBase, entry, t,
            const Color(0xFFFDE68A));
      } else {
        _tirNote(canvas, entry, size);
      }
    } else {
      for (final band in bands) {
        final n = (nBase + band.nOffset).clamp(1.05, 2.0);
        final t = traceFn(n);
        if (t != null) {
          _drawRefractedPath(canvas, size, apexPt, leftBase, rightBase, entry, t, band.color);
        }
      }
      _label(canvas, 'violet bends most · red bends least',
          Offset(size.width / 2, size.height - 8), Colors.white54, 9.5);
    }
  }

  void _drawRefractedPath(Canvas canvas, Size size, Offset apexPt, Offset leftBase,
      Offset rightBase, Offset entry, _PrismTrace t, Color color) {
    final leftFaceDir = (leftBase - apexPt) / (leftBase - apexPt).distance;
    final leftNormal = Offset(-leftFaceDir.dy, leftFaceDir.dx);
    final rightFaceDir = (rightBase - apexPt) / (rightBase - apexPt).distance;
    final rightNormal = Offset(-rightFaceDir.dy, rightFaceDir.dx);

    // Refracted ray inside the prism, bending toward the normal at entry.
    final innerDir = _rotate(leftNormal, -t.r1); // bends toward normal (opposite side of incidence)
    // Find exit point: travel from entry along innerDir until it crosses the right face.
    final exit = _intersectRay(entry, innerDir, apexPt, rightBase) ?? (apexPt + rightBase) / 2;
    _ray(canvas, entry, exit, color, 1.6);

    // Emergent ray bends away from normal at exit, angle i2 from rightNormal.
    final outDir = _rotate(rightNormal, t.i2);
    _ray(canvas, exit, exit + outDir * 90, color, 1.6);
  }

  Offset? _intersectRay(Offset p, Offset dir, Offset a, Offset b) {
    // Solve p + t*dir = a + s*(b-a) for t,s in [0,1]-ish.
    final abx = b.dx - a.dx, aby = b.dy - a.dy;
    final denom = dir.dx * aby - dir.dy * abx;
    if (denom.abs() < 1e-9) return null;
    final apx = a.dx - p.dx, apy = a.dy - p.dy;
    final t = (apx * aby - apy * abx) / denom;
    if (t <= 0) return null;
    return p + dir * t;
  }

  Offset _rotate(Offset v, double theta) {
    final c = math.cos(theta), s = math.sin(theta);
    return Offset(v.dx * c - v.dy * s, v.dx * s + v.dy * c);
  }

  void _ray(Canvas canvas, Offset a, Offset b, Color color, double w) {
    canvas.drawLine(a, b, Paint()..color = color..strokeWidth = w..strokeCap = StrokeCap.round);
  }

  void _tirNote(Canvas canvas, Offset entry, Size size) {
    _label(canvas, 'TIR at 2nd face — no emergent ray', entry + const Offset(0, -14),
        Palette.danger, 9.5);
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
  bool shouldRepaint(_PrismPainter old) =>
      old.apex != apex || old.incidence != incidence || old.nBase != nBase || old.dispersion != dispersion;
}
