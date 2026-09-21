import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Kirchhoff's Laws Sandbox — a fixed two-loop circuit topology (two EMF
/// sources, three resistors, a shared middle branch) with adjustable EMFs
/// and resistances. Loop currents are solved live via the standard 2-mesh
/// KVL system, demonstrating that KCL + KVL fully determine any circuit.
class KirchhoffLawsSandbox extends StatefulWidget {
  const KirchhoffLawsSandbox({super.key});

  @override
  State<KirchhoffLawsSandbox> createState() => _KirchhoffLawsSandboxState();
}

class _KirchhoffLawsSandboxState extends State<KirchhoffLawsSandbox> {
  double _e1 = 12.0; // volts
  double _e2 = 6.0; // volts
  double _r1 = 4.0; // ohms
  double _r2 = 3.0; // ohms
  double _r3 = 5.0; // ohms (shared middle branch)

  // Mesh equations (loop currents I1, I2, both assumed clockwise):
  //   I1(R1+R3) - I2 R3 = E1
  //  -I1 R3 + I2(R2+R3) = E2
  ({double i1, double i2, double iMid}) get _currents {
    final a11 = _r1 + _r3, a12 = -_r3;
    final a21 = -_r3, a22 = _r2 + _r3;
    final det = a11 * a22 - a12 * a21;
    final i1 = (_e1 * a22 - a12 * _e2) / det;
    final i2 = (a11 * _e2 - a21 * _e1) / det;
    return (i1: i1, i2: i2, iMid: i1 - i2);
  }

  @override
  Widget build(BuildContext context) {
    final c = _currents;
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
            painter: _CircuitPainter(i1: c.i1, i2: c.i2, iMid: c.iMid, r1: _r1, r2: _r2, r3: _r3, e1: _e1, e2: _e2),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Loop 1 current  I₁', c.i1.toStringAsFixed(2), 'A', Palette.chElectroMag)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Loop 2 current  I₂', c.i2.toStringAsFixed(2), 'A', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _meter('Middle branch  I₁−I₂ (through R₃)', c.iMid.toStringAsFixed(2), 'A',
            const Color(0xFF38BDF8)),
        const SizedBox(height: Gap.x3),
        _slider('EMF ε₁', _e1, 1, 20, 'V', Palette.chElectroMag, (x) => setState(() => _e1 = x)),
        _slider('EMF ε₂', _e2, 1, 20, 'V', Palette.accent, (x) => setState(() => _e2 = x)),
        _slider('R₁', _r1, 1, 10, 'Ω', const Color(0xFF16A34A), (x) => setState(() => _r1 = x)),
        _slider('R₂', _r2, 1, 10, 'Ω', const Color(0xFFF97316), (x) => setState(() => _r2 = x)),
        _slider('R₃ (shared branch)', _r3, 1, 10, 'Ω', const Color(0xFF38BDF8),
            (x) => setState(() => _r3 = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: raise ε₂ until it rivals ε₁ — watch the shared-branch current (I₁−I₂) shrink toward zero and even reverse sign. This whole circuit, however you tweak it, is solved by just two rules: KCL at each junction and KVL around each loop.'),
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

class _CircuitPainter extends CustomPainter {
  final double i1, i2, iMid, r1, r2, r3, e1, e2;
  _CircuitPainter({
    required this.i1,
    required this.i2,
    required this.iMid,
    required this.r1,
    required this.r2,
    required this.r3,
    required this.e1,
    required this.e2,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final wire = Paint()
      ..color = Colors.white70
      ..strokeWidth = 2.2;

    final midX = size.width / 2;
    final top = size.height * 0.28;
    final bottom = size.height * 0.78;
    final leftX = size.width * 0.12;
    final rightX = size.width * 0.88;

    // Outer rectangle (two loops sharing the middle vertical branch).
    canvas.drawLine(Offset(leftX, top), Offset(midX, top), wire);
    canvas.drawLine(Offset(midX, top), Offset(rightX, top), wire);
    canvas.drawLine(Offset(leftX, top), Offset(leftX, bottom), wire);
    canvas.drawLine(Offset(rightX, top), Offset(rightX, bottom), wire);
    canvas.drawLine(Offset(leftX, bottom), Offset(midX, bottom), wire);
    canvas.drawLine(Offset(midX, bottom), Offset(rightX, bottom), wire);
    // Middle shared branch.
    canvas.drawLine(Offset(midX, top), Offset(midX, bottom), wire);

    // Resistor zig-zags: R1 on left vertical, R2 on right vertical, R3 on middle.
    _zigzag(canvas, Offset(leftX, top + 20), Offset(leftX, bottom - 20), wire.color);
    _zigzag(canvas, Offset(rightX, top + 20), Offset(rightX, bottom - 20), wire.color);
    _zigzag(canvas, Offset(midX, top + 20), Offset(midX, bottom - 20), wire.color);

    _label(canvas, 'R₁=${r1.toStringAsFixed(1)}Ω', Offset(leftX - 30, (top + bottom) / 2),
        const Color(0xFF16A34A), 10.5);
    _label(canvas, 'R₂=${r2.toStringAsFixed(1)}Ω', Offset(rightX + 34, (top + bottom) / 2),
        const Color(0xFFF97316), 10.5);
    _label(canvas, 'R₃=${r3.toStringAsFixed(1)}Ω', Offset(midX + 34, (top + bottom) / 2 - 30),
        const Color(0xFF38BDF8), 10.5);

    // EMF markers on the bottom rail (battery symbols), left loop and right loop.
    final battLeftX = (leftX + midX) / 2;
    final battRightX = (midX + rightX) / 2;
    _battery(canvas, Offset(battLeftX, bottom));
    _battery(canvas, Offset(battRightX, bottom));
    _label(canvas, 'ε₁=${e1.toStringAsFixed(1)}V', Offset(battLeftX, bottom + 16),
        Palette.chElectroMag, 10.5);
    _label(canvas, 'ε₂=${e2.toStringAsFixed(1)}V', Offset(battRightX, bottom + 16),
        Palette.accent, 10.5);

    // Loop current arrows (curved indicators) with labels.
    _label(canvas, 'I₁=${i1.toStringAsFixed(2)}A ↻', Offset((leftX + midX) / 2, top - 14),
        Palette.chElectroMag, 11);
    _label(canvas, 'I₂=${i2.toStringAsFixed(2)}A ↻', Offset((midX + rightX) / 2, top - 14),
        Palette.accent, 11);
    _label(canvas, '(I₁−I₂)=${iMid.toStringAsFixed(2)}A', Offset(midX, top - 30),
        const Color(0xFF38BDF8), 10.5);

    // Junction dots.
    canvas.drawCircle(Offset(midX, top), 4, Paint()..color = Colors.white);
    canvas.drawCircle(Offset(midX, bottom), 4, Paint()..color = Colors.white);
  }

  void _zigzag(Canvas canvas, Offset a, Offset b, Color color) {
    final path = Path()..moveTo(a.dx, a.dy);
    final segs = 6;
    final dy = (b.dy - a.dy) / segs;
    for (var i = 1; i < segs; i++) {
      final y = a.dy + dy * i;
      final x = a.dx + (i.isOdd ? 10.0 : -10.0);
      path.lineTo(x, y);
    }
    path.lineTo(b.dx, b.dy);
    canvas.drawPath(path, Paint()
      ..color = color
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2);
  }

  void _battery(Canvas canvas, Offset center) {
    final p = Paint()
      ..color = Colors.white
      ..strokeWidth = 2.5;
    canvas.drawLine(center + const Offset(-2, -10), center + const Offset(-2, 10), p..strokeWidth = 3);
    canvas.drawLine(center + const Offset(4, -6), center + const Offset(4, 6), p..strokeWidth = 1.4);
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
  bool shouldRepaint(_CircuitPainter old) =>
      old.i1 != i1 || old.i2 != i2 || old.iMid != iMid || old.r1 != r1 || old.r2 != r2 || old.r3 != r3;
}
