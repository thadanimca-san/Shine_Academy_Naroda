import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Logic Gates Sandbox — pick a gate (AND, OR, NOT, NAND, NOR, XOR), tap the
/// inputs A and B to toggle them between 0 and 1, and watch the output light
/// up while the matching row of the truth table highlights. The point students
/// discover: NAND and NOR are the "universal" gates — every other gate is just
/// an inverted AND/OR.
class LogicGatesSandbox extends StatefulWidget {
  const LogicGatesSandbox({super.key});

  @override
  State<LogicGatesSandbox> createState() => _LogicGatesSandboxState();
}

enum _Gate { and, or, not, nand, nor, xor }

class _LogicGatesSandboxState extends State<LogicGatesSandbox> {
  _Gate _gate = _Gate.and;
  bool _a = false;
  bool _b = false;

  bool get _single => _gate == _Gate.not;

  bool _eval(bool a, bool b) {
    switch (_gate) {
      case _Gate.and:
        return a && b;
      case _Gate.or:
        return a || b;
      case _Gate.not:
        return !a;
      case _Gate.nand:
        return !(a && b);
      case _Gate.nor:
        return !(a || b);
      case _Gate.xor:
        return a != b;
    }
  }

  String get _expr {
    switch (_gate) {
      case _Gate.and:
        return 'Y = A · B';
      case _Gate.or:
        return 'Y = A + B';
      case _Gate.not:
        return 'Y = Ā';
      case _Gate.nand:
        return 'Y = A · B  (bar)';
      case _Gate.nor:
        return 'Y = A + B  (bar)';
      case _Gate.xor:
        return 'Y = A ⊕ B';
    }
  }

  @override
  Widget build(BuildContext context) {
    final out = _eval(_a, _b);
    final rows = _single
        ? [
            [false, _eval(false, false)],
            [true, _eval(true, false)],
          ]
        : [
            [false, false, _eval(false, false)],
            [false, true, _eval(false, true)],
            [true, false, _eval(true, false)],
            [true, true, _eval(true, true)],
          ];
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
            painter: _GatePainter(
                gate: _gate, a: _a, b: _b, out: out, single: _single),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(
          children: [
            _inputBtn('A', _a, () => setState(() => _a = !_a)),
            const SizedBox(width: Gap.x3),
            if (!_single)
              _inputBtn('B', _b, () => setState(() => _b = !_b))
            else
              const Expanded(child: SizedBox()),
            const SizedBox(width: Gap.x3),
            Expanded(
              child: Container(
                padding: const EdgeInsets.symmetric(vertical: 14),
                alignment: Alignment.center,
                decoration: BoxDecoration(
                  color: out ? Palette.success : Palette.surfaceAlt,
                  borderRadius: BorderRadius.circular(Corner.md),
                  border: Border.all(color: Palette.border),
                ),
                child: Text('Y = ${out ? 1 : 0}',
                    style: Type.bodyStrong.copyWith(
                        fontSize: 18,
                        fontFamily: 'monospace',
                        color: out ? Colors.white : Palette.textMuted)),
              ),
            ),
          ],
        ),
        const SizedBox(height: Gap.x3),
        Text(TrilingualService.instance.getUIText('SELECT GATE'), style: Type.label.copyWith(fontSize: 9)),
        const SizedBox(height: Gap.x2),
        Wrap(
          spacing: Gap.x2,
          runSpacing: Gap.x2,
          children: _Gate.values.map((g) {
            final active = g == _gate;
            return GestureDetector(
              onTap: () => setState(() => _gate = g),
              child: Container(
                padding:
                    const EdgeInsets.symmetric(horizontal: 14, vertical: 8),
                decoration: BoxDecoration(
                  color: active ? Palette.primary : Palette.surfaceAlt,
                  borderRadius: BorderRadius.circular(Corner.pill),
                  border: Border.all(
                      color: active ? Palette.primary : Palette.border),
                ),
                child: Text(g.name.toUpperCase(),
                    style: Type.caption.copyWith(
                        fontSize: 12,
                        fontWeight: FontWeight.w700,
                        color: active ? Colors.white : Palette.textMuted)),
              ),
            );
          }).toList(),
        ),
        const SizedBox(height: Gap.x3),
        Text(_expr,
            style: Type.bodyStrong
                .copyWith(fontFamily: 'monospace', fontSize: 15)),
        const SizedBox(height: Gap.x3),
        _truthTable(rows),
      ],
    );
  }

  Widget _inputBtn(String label, bool value, VoidCallback onTap) {
    return Expanded(
      child: GestureDetector(
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 14),
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: value ? Palette.accent : Palette.surfaceAlt,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Text('$label = ${value ? 1 : 0}',
              style: Type.bodyStrong.copyWith(
                  fontSize: 16,
                  fontFamily: 'monospace',
                  color: value ? Colors.white : Palette.textMuted)),
        ),
      ),
    );
  }

  Widget _truthTable(List<List<bool>> rows) {
    Widget cell(String t, {bool header = false, bool hi = false}) => Expanded(
          child: Container(
            padding: const EdgeInsets.symmetric(vertical: 7),
            alignment: Alignment.center,
            color: header
                ? Palette.surfaceAlt
                : (hi ? Palette.primarySoft : Palette.surface),
            child: Text(t,
                style: (header ? Type.label : Type.mono).copyWith(
                    fontSize: header ? 10 : 13,
                    color: hi ? Palette.primaryDeep : null,
                    fontWeight: hi ? FontWeight.w800 : null)),
          ),
        );
    final headers = _single
        ? [cell('A', header: true), cell('Y', header: true)]
        : [
            cell('A', header: true),
            cell('B', header: true),
            cell('Y', header: true)
          ];
    return Container(
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(Corner.md),
        border: Border.all(color: Palette.border),
      ),
      clipBehavior: Clip.antiAlias,
      child: Column(
        children: [
          Row(children: headers),
          ...rows.map((r) {
            final hi = _single
                ? r[0] == _a
                : (r[0] == _a && r[1] == _b);
            return Row(
              children: r
                  .map((v) => cell(v ? '1' : '0', hi: hi))
                  .toList(),
            );
          }),
        ],
      ),
    );
  }
}

class _GatePainter extends CustomPainter {
  final _Gate gate;
  final bool a, b, out, single;
  _GatePainter(
      {required this.gate,
      required this.a,
      required this.b,
      required this.out,
      required this.single});

  static const _hot = Color(0xFFF59E0B);
  static const _cold = Color(0xFF5B5F7A);

  @override
  void paint(Canvas canvas, Size size) {
    final cx = size.width * 0.52;
    final cy = size.height * 0.5;
    final aY = cy - (single ? 0 : 26);
    final bY = cy + 26;
    final inX = size.width * 0.14;
    final gateLeft = size.width * 0.42;

    Paint wire(bool live) => Paint()
      ..color = live ? _hot : _cold
      ..strokeWidth = 3
      ..strokeCap = StrokeCap.round;

    // input wires
    canvas.drawLine(Offset(inX, aY), Offset(gateLeft, aY), wire(a));
    _dot(canvas, Offset(inX, aY), a, 'A');
    if (!single) {
      canvas.drawLine(Offset(inX, bY), Offset(gateLeft, bY), wire(b));
      _dot(canvas, Offset(inX, bY), b, 'B');
    }

    // gate body (simple block with the gate name)
    final body = RRect.fromRectAndRadius(
      Rect.fromCenter(center: Offset(cx, cy), width: 96, height: 74),
      const Radius.circular(10),
    );
    canvas.drawRRect(
        body, Paint()..color = out ? _hot.withValues(alpha: 0.9) : const Color(0xFF2A2E52));
    canvas.drawRRect(
        body,
        Paint()
          ..color = Colors.white30
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.5);
    _text(canvas, gate.name.toUpperCase(), Offset(cx, cy),
        out ? Colors.black : Colors.white, 15);

    // output wire
    final outStart = Offset(cx + 48, cy);
    final outEnd = Offset(size.width * 0.9, cy);
    canvas.drawLine(outStart, outEnd, wire(out));
    _dot(canvas, outEnd, out, 'Y');

    // bubble for inverting gates
    if (gate == _Gate.not ||
        gate == _Gate.nand ||
        gate == _Gate.nor) {
      canvas.drawCircle(Offset(cx + 48, cy), 5,
          Paint()..color = out ? _hot : const Color(0xFF2A2E52));
      canvas.drawCircle(
          Offset(cx + 48, cy),
          5,
          Paint()
            ..color = Colors.white54
            ..style = PaintingStyle.stroke
            ..strokeWidth = 1.5);
    }
  }

  void _dot(Canvas canvas, Offset c, bool live, String label) {
    canvas.drawCircle(c, 9, Paint()..color = live ? _hot : _cold);
    _text(canvas, live ? '1' : '0', c, Colors.white, 11);
    _text(canvas, label, c + const Offset(0, -18), Colors.white54, 10);
  }

  void _text(Canvas canvas, String t, Offset c, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: t,
          style: TextStyle(
              color: color,
              fontSize: fs,
              fontWeight: FontWeight.w800,
              fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, c - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_GatePainter old) =>
      old.gate != gate ||
      old.a != a ||
      old.b != b ||
      old.out != out ||
      old.single != single;
}
