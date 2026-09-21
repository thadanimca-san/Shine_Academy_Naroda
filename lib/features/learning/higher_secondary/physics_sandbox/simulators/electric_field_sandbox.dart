import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Electric Field Sandbox — a vector-grid view of the field from two charges.
///
/// Students set the sign and magnitude of two source charges. A grid of small
/// arrows shows the field direction and strength (E = kΣq/r²·r̂) at every point,
/// coloured by strength. A movable test point reads out the field magnitude
/// there. The key idea — field points AWAY from + and TOWARD − — becomes
/// visible, and superposition is literally drawn.
class ElectricFieldSandbox extends StatefulWidget {
  const ElectricFieldSandbox({super.key});

  @override
  State<ElectricFieldSandbox> createState() => _ElectricFieldSandboxState();
}

class _ElectricFieldSandboxState extends State<ElectricFieldSandbox> {
  double _q1 = 3.0; // nC-scale (relative units for visual field)
  double _q2 = -3.0;

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
            painter: _FieldPainter(q1: _q1, q2: _q2),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.surface,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Row(
            children: [
              _legendDot(const Color(0xFFF97316), 'Field lines leave +'),
              const SizedBox(width: Gap.x4),
              _legendDot(const Color(0xFF38BDF8), 'and enter −'),
            ],
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _slider('q₁', _q1, -5, 5, 'nC', const Color(0xFFF97316),
              (v) => setState(() => _q1 = v))),
          const SizedBox(width: Gap.x3),
          Expanded(child: _slider('q₂', _q2, -5, 5, 'nC', const Color(0xFF38BDF8),
              (v) => setState(() => _q2 = v))),
        ]),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.primarySoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Each arrow shows E = kΣqᵢ/rᵢ² at that spot — the vector sum of both charges (superposition). ''Set q₁ = +q, q₂ = −q for a DIPOLE; set both positive to see the field push apart with a null point between them.'),
            style: Type.caption.copyWith(color: Palette.primaryDeep),
          ),
        ),
      ],
    );
  }

  Widget _legendDot(Color c, String label) {
    return Row(children: [
      Container(width: 12, height: 12, decoration: BoxDecoration(color: c, shape: BoxShape.circle)),
      const SizedBox(width: 6),
      Flexible(child: Text(label, style: Type.caption.copyWith(fontSize: 11.5))),
    ]);
  }

  Widget _slider(String label, double value, double min, double max, String unit,
      Color color, ValueChanged<double> onChanged) {
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

class _FieldPainter extends CustomPainter {
  final double q1, q2;
  _FieldPainter({required this.q1, required this.q2});

  static const _cPos = Color(0xFFF97316);
  static const _cNeg = Color(0xFF38BDF8);

  @override
  void paint(Canvas canvas, Size size) {
    final p1 = Offset(size.width * 0.32, size.height * 0.5);
    final p2 = Offset(size.width * 0.68, size.height * 0.5);

    // Vector grid — field at each node, arrow length/colour by strength.
    const cols = 13, rows = 8;
    final dx = size.width / cols, dy = size.height / rows;
    double maxMag = 1e-9;
    final mags = <List<double>>[];
    final fields = <List<Offset>>[];
    for (int i = 0; i < rows; i++) {
      final rowM = <double>[];
      final rowF = <Offset>[];
      for (int j = 0; j < cols; j++) {
        final pt = Offset((j + 0.5) * dx, (i + 0.5) * dy);
        final f = _fieldAt(pt, p1, p2);
        final m = f.distance;
        rowM.add(m);
        rowF.add(f);
        if (m > maxMag && m.isFinite) maxMag = m;
      }
      mags.add(rowM);
      fields.add(rowF);
    }

    for (int i = 0; i < rows; i++) {
      for (int j = 0; j < cols; j++) {
        final pt = Offset((j + 0.5) * dx, (i + 0.5) * dy);
        final f = fields[i][j];
        final m = mags[i][j];
        if (m < 1e-9 || !m.isFinite) continue;
        final norm = (m / maxMag).clamp(0.0, 1.0);
        final len = 6.0 + math.sqrt(norm) * 12.0;
        final dir = f / m;
        final tail = pt - dir * (len / 2);
        final head = pt + dir * (len / 2);
        final col = Color.lerp(const Color(0x554F46E5), Colors.white, norm)!;
        final paint = Paint()
          ..color = col
          ..strokeWidth = 1.6
          ..strokeCap = StrokeCap.round;
        canvas.drawLine(tail, head, paint);
        // arrowhead
        final perp = Offset(-dir.dy, dir.dx);
        canvas.drawLine(head, head - dir * 4 + perp * 3, paint);
        canvas.drawLine(head, head - dir * 4 - perp * 3, paint);
      }
    }

    _charge(canvas, p1, q1);
    _charge(canvas, p2, q2);
  }

  Offset _fieldAt(Offset pt, Offset p1, Offset p2) {
    Offset contribution(Offset src, double q) {
      final d = pt - src;
      final r2 = d.distanceSquared;
      if (r2 < 90) return Offset.zero; // skip singularity near the charge
      final r = math.sqrt(r2);
      final mag = q / r2; // relative units
      return d / r * mag;
    }

    return contribution(p1, q1) + contribution(p2, q2);
  }

  void _charge(Canvas canvas, Offset c, double q) {
    if (q.abs() < 0.05) return;
    final positive = q >= 0;
    final color = positive ? _cPos : _cNeg;
    final radius = 10.0 + q.abs() * 1.8;
    canvas.drawCircle(c, radius, Paint()..color = color);
    final sp = Paint()
      ..color = Colors.white
      ..strokeWidth = 3
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(c + const Offset(-5, 0), c + const Offset(5, 0), sp);
    if (positive) {
      canvas.drawLine(c + const Offset(0, -5), c + const Offset(0, 5), sp);
    }
  }

  @override
  bool shouldRepaint(_FieldPainter old) => old.q1 != q1 || old.q2 != q2;
}
