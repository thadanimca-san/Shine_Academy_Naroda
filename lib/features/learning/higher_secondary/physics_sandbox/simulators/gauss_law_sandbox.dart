import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Gauss's Law Sandbox — a closed spherical surface with an adjustable
/// enclosed charge. A toggle moves the charge INSIDE or OUTSIDE the surface.
/// Field lines pierce the surface either way, but the computed flux
/// Φ = Q_enc/ε₀ is only ever non-zero when the charge is enclosed.
class GaussLawSandbox extends StatefulWidget {
  const GaussLawSandbox({super.key});

  @override
  State<GaussLawSandbox> createState() => _GaussLawSandboxState();
}

class _GaussLawSandboxState extends State<GaussLawSandbox> {
  double _q = 5.0; // charge in nC
  bool _inside = true;

  static const double _eps0 = 8.85e-12;

  double get _fluxNm2PerC => _inside ? (_q * 1e-9) / _eps0 : 0.0;

  @override
  Widget build(BuildContext context) {
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
          child: CustomPaint(
            painter: _GaussPainter(q: _q, inside: _inside),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
            child: _meter('Flux  Φ = Q_enc/ε₀', _fluxNm2PerC.toStringAsExponential(2), 'N·m²/C',
                _inside ? Palette.chElectroMag : Palette.textMuted),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _meter('Enclosed charge', _inside ? _q.toStringAsFixed(1) : '0.0', 'nC',
                Palette.accent),
          ),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Charge Q', _q, 1, 12, 'nC', Palette.chElectroMag, (x) => setState(() => _q = x)),
        const SizedBox(height: Gap.x2),
        Row(
          children: [
            Expanded(
              child: _toggleChip('Charge INSIDE', _inside, () => setState(() => _inside = true)),
            ),
            const SizedBox(width: Gap.x2),
            Expanded(
              child: _toggleChip('Charge OUTSIDE', !_inside, () => setState(() => _inside = false)),
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
            _inside
                ? 'The charge is enclosed: every field line that pierces the surface leaves for good, so net flux = Q/ε₀ > 0.'
                : 'Try it: move the charge OUTSIDE. Field lines still cross the surface — some enter, but every one that enters also exits. The lines entering exactly cancel the lines leaving, so the NET flux is exactly zero, no matter how close the charge sits to the surface.',
            style: Type.caption.copyWith(color: Palette.primaryDeep),
          ),
        ),
      ],
    );
  }

  Widget _toggleChip(String label, bool selected, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 10),
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: selected ? Palette.chElectroMag : Palette.surface,
          borderRadius: BorderRadius.circular(Corner.md),
          border: Border.all(color: selected ? Palette.chElectroMag : Palette.border),
        ),
        child: Text(
          label,
          style: Type.bodyStrong.copyWith(
              fontSize: 12.5, color: selected ? Colors.white : Palette.textBody),
        ),
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
              style: Type.bodyStrong.copyWith(fontSize: 14.5, fontFamily: 'monospace', color: color)),
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

class _GaussPainter extends CustomPainter {
  final double q;
  final bool inside;
  _GaussPainter({required this.q, required this.inside});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    final surfaceR = math.min(size.width, size.height) * 0.32;

    // Gaussian (closed) surface.
    canvas.drawCircle(
      center,
      surfaceR,
      Paint()
        ..color = const Color(0xFF38BDF8)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2,
    );
    _label(canvas, 'Gaussian surface', center + Offset(0, -surfaceR - 16),
        const Color(0xFF38BDF8), 10.5);

    // Charge position: centre if inside, offset outside the circle otherwise.
    final chargePos = inside ? center : center + Offset(surfaceR * 1.7, 0);

    // Field lines radiating from the charge, each drawn as a ray; mark
    // where they cross the Gaussian circle (entry/exit points).
    const lineCount = 16;
    for (var i = 0; i < lineCount; i++) {
      final angle = i * 2 * math.pi / lineCount;
      final dir = Offset(math.cos(angle), math.sin(angle));
      final farPoint = chargePos + dir * 300;
      final linePaint = Paint()
        ..color = Palette.chElectroMag.withValues(alpha: 0.45)
        ..strokeWidth = 1.4;
      canvas.drawLine(chargePos, farPoint, linePaint);

      if (!inside) {
        // Find intersections of this ray with the Gaussian circle (if any),
        // to visualize entry AND exit piercing points.
        final pts = _rayCircleIntersections(chargePos, dir, center, surfaceR);
        for (final p in pts) {
          canvas.drawCircle(p, 3, Paint()..color = Colors.white70);
        }
      }
    }

    // Charge marker.
    canvas.drawCircle(chargePos, 12, Paint()..color = Palette.accent);
    _label(canvas, '+Q', chargePos, Colors.white, 11);

    // Arrowheads on lines that actually cross the surface when charge inside.
    if (inside) {
      for (var i = 0; i < lineCount; i++) {
        final angle = i * 2 * math.pi / lineCount;
        final dir = Offset(math.cos(angle), math.sin(angle));
        final edge = center + dir * surfaceR;
        _arrow(canvas, edge - dir * 14, edge + dir * 4, Palette.chElectroMag, 1.8);
      }
    }

    _label(canvas, inside ? 'Every line LEAVES the surface' : 'Lines enter AND exit — net = 0',
        Offset(center.dx, size.height - 16), Colors.white70, 10.5);
  }

  List<Offset> _rayCircleIntersections(Offset origin, Offset dir, Offset c, double r) {
    // Solve |origin + t*dir - c|^2 = r^2 for t >= 0.
    final oc = origin - c;
    final a = dir.dx * dir.dx + dir.dy * dir.dy;
    final b = 2 * (oc.dx * dir.dx + oc.dy * dir.dy);
    final cc = oc.dx * oc.dx + oc.dy * oc.dy - r * r;
    final disc = b * b - 4 * a * cc;
    if (disc < 0) return [];
    final sq = math.sqrt(disc);
    final t1 = (-b - sq) / (2 * a);
    final t2 = (-b + sq) / (2 * a);
    final pts = <Offset>[];
    if (t1 > 0) pts.add(origin + dir * t1);
    if (t2 > 0) pts.add(origin + dir * t2);
    return pts;
  }

  void _arrow(Canvas canvas, Offset a, Offset b, Color color, double w) {
    final p = Paint()
      ..color = color
      ..strokeWidth = w
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(a, b, p);
    final dir = b - a;
    final len = dir.distance;
    if (len < 1) return;
    final un = dir / len;
    final n = Offset(-un.dy, un.dx);
    canvas.drawLine(b, b - un * 8 + n * 3.5, p);
    canvas.drawLine(b, b - un * 8 - n * 3.5, p);
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
  bool shouldRepaint(_GaussPainter old) => old.q != q || old.inside != inside;
}
