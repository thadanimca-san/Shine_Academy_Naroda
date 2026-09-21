import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Refraction Sandbox — a ray crossing a flat boundary between two media.
///
/// Students set the angle of incidence and the two refractive indices, then
/// watch the refracted ray bend by Snell's law n₁sinθ₁ = n₂sinθ₂. Push the
/// angle past the critical angle (only possible going dense → rare) and the
/// refracted ray vanishes — total internal reflection takes over.
class RefractionSandbox extends StatefulWidget {
  const RefractionSandbox({super.key});

  @override
  State<RefractionSandbox> createState() => _RefractionSandboxState();
}

class _RefractionSandboxState extends State<RefractionSandbox> {
  double _theta1 = 35.0; // degrees, angle of incidence
  double _n1 = 1.0; // top medium (incident side)
  double _n2 = 1.5; // bottom medium

  // Snell: sinθ₂ = (n₁/n₂) sinθ₁
  double get _sinT2 => (_n1 / _n2) * math.sin(_theta1 * math.pi / 180);
  bool get _tir => _sinT2.abs() > 1.0;
  double? get _theta2 =>
      _tir ? null : math.asin(_sinT2) * 180 / math.pi;

  // Critical angle exists only when n₁ > n₂ (dense → rare).
  double? get _critical =>
      _n1 > _n2 ? math.asin(_n2 / _n1) * 180 / math.pi : null;

  @override
  Widget build(BuildContext context) {
    final t2 = _theta2;
    final crit = _critical;

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
            painter: _RefractionPainter(
              theta1: _theta1,
              theta2: t2,
              n1: _n1,
              n2: _n2,
              tir: _tir,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),

        Row(children: [
          Expanded(
            child: _readout('Refraction θ₂',
                _tir ? 'TIR' : '${t2!.toStringAsFixed(1)}°',
                _tir ? Palette.danger : Palette.info),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _readout(
                'Critical angle',
                crit == null ? 'none' : '${crit.toStringAsFixed(1)}°',
                Palette.accent),
          ),
        ]),
        const SizedBox(height: Gap.x2),
        Container(
          padding:
              const EdgeInsets.symmetric(horizontal: Gap.x3, vertical: Gap.x2),
          decoration: BoxDecoration(
            color: _tir ? Palette.dangerSoft : Palette.infoSoft,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Text(
            _tir
                ? 'Beyond the critical angle — NO refracted ray. All light reflects back (total internal reflection).'
                : _n1 < _n2
                    ? 'Going into a denser medium → ray bends TOWARD the normal.'
                    : _n1 > _n2
                        ? 'Going into a rarer medium → ray bends AWAY from the normal.'
                        : 'Equal indices → no bending, the ray goes straight.',
            style: Type.bodyStrong.copyWith(fontSize: 12.5),
          ),
        ),
        const SizedBox(height: Gap.x3),

        _slider('Angle of incidence θ₁', _theta1, 0, 89, '°', Palette.primary,
            (val) => setState(() => _theta1 = val)),
        _slider('n₁ (incident medium)', _n1, 1.0, 2.4, '', Palette.jee,
            (val) => setState(() => _n1 = val)),
        _slider('n₂ (other medium)', _n2, 1.0, 2.4, '', Palette.neet,
            (val) => setState(() => _n2 = val)),
      ],
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
        Text(
            unit.isEmpty
                ? '$label = ${value.toStringAsFixed(2)}'
                : '$label = ${value.toStringAsFixed(0)} $unit',
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

class _RefractionPainter extends CustomPainter {
  final double theta1;
  final double? theta2;
  final double n1, n2;
  final bool tir;

  _RefractionPainter({
    required this.theta1,
    required this.theta2,
    required this.n1,
    required this.n2,
    required this.tir,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final cx = size.width * 0.5;
    final boundaryY = size.height * 0.5;
    final hit = Offset(cx, boundaryY);

    // Two media as tinted bands (denser = more tint).
    final topTint = (n1 - 1.0) / 1.5;
    final botTint = (n2 - 1.0) / 1.5;
    canvas.drawRect(
        Rect.fromLTWH(0, 0, size.width, boundaryY),
        Paint()
          ..color = Color.lerp(
              Palette.stage, const Color(0xFF1E3A8A), topTint * 0.6)!);
    canvas.drawRect(
        Rect.fromLTWH(0, boundaryY, size.width, size.height - boundaryY),
        Paint()
          ..color = Color.lerp(
              Palette.stage, const Color(0xFF1E3A8A), botTint * 0.6)!);

    // Boundary line
    canvas.drawLine(Offset(0, boundaryY), Offset(size.width, boundaryY),
        Paint()..color = Colors.white54..strokeWidth = 2);
    // Normal (dashed vertical)
    _dashed(canvas, Offset(cx, 10), Offset(cx, size.height - 10),
        Colors.white38);

    final t1 = theta1 * math.pi / 180;
    const len = 120.0;

    // Incident ray (comes from top-left, going down to the hit).
    final incStart = hit +
        Offset(-len * math.sin(t1), -len * math.cos(t1));
    _ray(canvas, incStart, hit, const Color(0xFFFBBF24), arrowAt: hit);

    if (tir) {
      // Reflected ray (mirror about normal, stays in top medium).
      final reflEnd = hit +
          Offset(len * math.sin(t1), -len * math.cos(t1));
      _ray(canvas, hit, reflEnd, const Color(0xFFF87171), arrowAt: reflEnd);
      _label(canvas, 'total internal reflection',
          Offset(cx, boundaryY + 24), const Color(0xFFF87171), 10);
    } else {
      final t2 = theta2! * math.pi / 180;
      // Refracted ray continues into bottom medium.
      final refEnd = hit +
          Offset(len * math.sin(t2), len * math.cos(t2));
      _ray(canvas, hit, refEnd, const Color(0xFF60A5FA), arrowAt: refEnd);
      // Faint partial reflection.
      final reflEnd = hit +
          Offset(len * 0.5 * math.sin(t1), -len * 0.5 * math.cos(t1));
      _ray(canvas, hit, reflEnd,
          const Color(0xFFF87171).withValues(alpha: 0.4));
      _label(canvas, 'θ₂ = ${theta2!.toStringAsFixed(0)}°',
          Offset(cx + 46, boundaryY + 40), const Color(0xFF60A5FA), 10);
    }

    _label(canvas, 'θ₁ = ${theta1.toStringAsFixed(0)}°',
        Offset(cx - 50, boundaryY - 40), const Color(0xFFFBBF24), 10);
    _label(canvas, 'n₁ = ${n1.toStringAsFixed(2)}',
        Offset(46, 16), Colors.white70, 10);
    _label(canvas, 'n₂ = ${n2.toStringAsFixed(2)}',
        Offset(46, size.height - 16), Colors.white70, 10);
  }

  void _ray(Canvas canvas, Offset a, Offset b, Color color, {Offset? arrowAt}) {
    final p = Paint()
      ..color = color
      ..strokeWidth = 2.4
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(a, b, p);
    if (arrowAt != null) {
      final dir = (b - a);
      final n = dir / dir.distance;
      final perp = Offset(-n.dy, n.dx);
      canvas.drawLine(arrowAt, arrowAt - n * 9 + perp * 5, p);
      canvas.drawLine(arrowAt, arrowAt - n * 9 - perp * 5, p);
    }
  }

  void _dashed(Canvas canvas, Offset a, Offset b, Color color) {
    final p = Paint()
      ..color = color
      ..strokeWidth = 1.2;
    const dash = 6.0;
    final total = (b - a).distance;
    final dir = (b - a) / total;
    double t = 0;
    while (t < total) {
      canvas.drawLine(
          a + dir * t, a + dir * math.min(t + dash, total), p);
      t += dash * 2;
    }
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
  bool shouldRepaint(_RefractionPainter old) =>
      old.theta1 != theta1 ||
      old.theta2 != theta2 ||
      old.n1 != n1 ||
      old.n2 != n2 ||
      old.tir != tir;
}
