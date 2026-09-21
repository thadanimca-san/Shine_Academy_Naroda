import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import '../widgets/sim_controls.dart';
import '../widgets/sim_kit.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Dimensional-Analysis Checker.
///
/// The student builds a formula's dimensions by choosing integer powers of
/// M, L and T, and compares them against a target quantity. The verdict tells
/// them instantly whether the two sides of an equation are dimensionally
/// consistent — the single most useful sanity check in all of physics.
class UnitsDimensionsSandbox extends StatefulWidget {
  const UnitsDimensionsSandbox({super.key});

  @override
  State<UnitsDimensionsSandbox> createState() => _UnitsDimensionsSandboxState();
}

class _Quantity {
  final String name;
  final int m, l, t;
  const _Quantity(this.name, this.m, this.l, this.t);
}

class _UnitsDimensionsSandboxState extends State<UnitsDimensionsSandbox>
    with TickerProviderStateMixin {
  // Common targets [M^a L^b T^c]
  static const List<_Quantity> _targets = [
    _Quantity('Velocity', 0, 1, -1),
    _Quantity('Acceleration', 0, 1, -2),
    _Quantity('Force', 1, 1, -2),
    _Quantity('Energy / Work', 1, 2, -2),
    _Quantity('Power', 1, 2, -3),
    _Quantity('Pressure', 1, -1, -2),
    _Quantity('Momentum', 1, 1, -1),
  ];

  int _targetIdx = 2; // Force by default
  int _m = 0, _l = 0, _t = 0; // student-built powers

  _Quantity get _target => _targets[_targetIdx];
  bool get _match => _m == _target.m && _l == _target.l && _t == _target.t;

  late final SimClock _clock = SimClock(this, _onTick);

  void _onTick() {
    if (_clock.running && _clock.t >= 2.2) _clock.pause();
    setState(() {});
  }

  /// Damped rocking of the beam while "weighing".
  double get _wobble {
    final t = _clock.t;
    if (t <= 0 || t >= 2.2) return 0;
    return math.exp(-2.2 * t) * math.sin(7 * t) * 0.25;
  }

  void _weigh() {
    _clock.reset();
    _clock.start();
  }

  void _resetAll() {
    _clock.reset();
    setState(() {
      _m = 0;
      _l = 0;
      _t = 0;
    });
  }

  @override
  void dispose() {
    _clock.dispose();
    super.dispose();
  }

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
            painter: _DimPainter(
              m: _m, l: _l, t: _t,
              tm: _target.m, tl: _target.l, tt: _target.t,
              targetName: _target.name, match: _match,
              wobble: _wobble,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: _match ? Palette.successSoft : Palette.surface,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: _match ? Palette.success : Palette.border),
          ),
          child: Row(
            children: [
              Icon(_match ? Icons.check_circle_rounded : Icons.rule_rounded,
                  color: _match ? Palette.success : Palette.textMuted, size: 20),
              const SizedBox(width: Gap.x2),
              Expanded(
                child: Text(
                  _match
                      ? 'Dimensionally consistent — your [M^${_m} L^${_l} T^${_t}] matches ${_target.name}.'
                      : 'Not yet. Build [${_dimStr(_target.m, _target.l, _target.t)}] to match ${_target.name}.',
                  style: Type.bodyStrong.copyWith(
                      color: _match ? Palette.success : Palette.textBody, fontSize: 13),
                ),
              ),
            ],
          ),
        ),
        const SizedBox(height: Gap.x3),
        Text(TrilingualService.instance.getUIText('TARGET QUANTITY'), style: Type.label.copyWith(fontSize: 10)),
        const SizedBox(height: Gap.x2),
        Wrap(
          spacing: Gap.x2,
          runSpacing: Gap.x2,
          children: [
            for (int i = 0; i < _targets.length; i++)
              ChoiceChip(
                label: Text(_targets[i].name),
                selected: _targetIdx == i,
                onSelected: (_) => setState(() => _targetIdx = i),
                selectedColor: Palette.primarySoft,
                labelStyle: Type.caption.copyWith(
                  color: _targetIdx == i ? Palette.primaryDeep : Palette.textBody,
                  fontWeight: _targetIdx == i ? FontWeight.w700 : FontWeight.w500,
                ),
              ),
          ],
        ),
        const SizedBox(height: Gap.x4),
        Text(TrilingualService.instance.getUIText('BUILD YOUR DIMENSIONS'), style: Type.label.copyWith(fontSize: 10)),
        const SizedBox(height: Gap.x2),
        _stepper('Mass  [M]', _m, const Color(0xFFF97316), (d) => setState(() => _m = (_m + d).clamp(-4, 4))),
        _stepper('Length  [L]', _l, const Color(0xFF38BDF8), (d) => setState(() => _l = (_l + d).clamp(-4, 4))),
        _stepper('Time  [T]', _t, const Color(0xFFA78BFA), (d) => setState(() => _t = (_t + d).clamp(-4, 4))),
        const SizedBox(height: Gap.x2),
        SimControls(
          running: _clock.running,
          onStart: _weigh,
          onPause: _clock.pause,
          onReset: _resetAll,
          startLabel: 'Weigh the pans',
        ),
      ],
    );
  }

  static String _dimStr(int m, int l, int t) {
    final parts = <String>[];
    if (m != 0) parts.add('M${_sup(m)}');
    if (l != 0) parts.add('L${_sup(l)}');
    if (t != 0) parts.add('T${_sup(t)}');
    return parts.isEmpty ? 'dimensionless' : parts.join(' ');
  }

  static String _sup(int n) {
    if (n == 1) return '';
    const map = {'-': '⁻', '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴'};
    return n.toString().split('').map((c) => map[c] ?? c).join();
  }

  Widget _stepper(String label, int value, Color color, ValueChanged<int> onStep) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: Gap.x1),
      child: Row(
        children: [
          Expanded(
            child: Text(label,
                style: Type.bodyStrong.copyWith(fontSize: 13.5, color: color)),
          ),
          _stepBtn(Icons.remove_rounded, color, () => onStep(-1)),
          Container(
            width: 44,
            alignment: Alignment.center,
            child: Text(value.toString(),
                style: Type.body.copyWith(fontFamily: 'monospace', fontSize: 16, color: Palette.textStrong)),
          ),
          _stepBtn(Icons.add_rounded, color, () => onStep(1)),
        ],
      ),
    );
  }

  Widget _stepBtn(IconData icon, Color color, VoidCallback onTap) {
    return InkWell(
      onTap: onTap,
      borderRadius: BorderRadius.circular(Corner.sm),
      child: Container(
        width: 34,
        height: 34,
        decoration: BoxDecoration(
          color: color.withValues(alpha: 0.12),
          borderRadius: BorderRadius.circular(Corner.sm),
        ),
        child: Icon(icon, size: 18, color: color),
      ),
    );
  }
}

class _DimPainter extends CustomPainter {
  final int m, l, t, tm, tl, tt;
  final String targetName;
  final bool match;
  final double wobble;

  _DimPainter({
    required this.m, required this.l, required this.t,
    required this.tm, required this.tl, required this.tt,
    required this.targetName, required this.match,
    this.wobble = 0,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final cx = size.width / 2;
    // Balance beam metaphor: your side vs target side.
    final beamY = size.height * 0.42;
    // Tilt if mismatch, plus the damped weighing wobble.
    final tilt = (match ? 0.0 : 0.12) + wobble;
    final left = Offset(cx - size.width * 0.32, beamY + math.sin(-tilt) * 40);
    final right = Offset(cx + size.width * 0.32, beamY + math.sin(tilt) * 40);

    // Pivot
    canvas.drawLine(Offset(cx, beamY - 20), Offset(cx, size.height * 0.9),
        Paint()..color = Palette.stageLine..strokeWidth = 3);
    canvas.drawCircle(Offset(cx, beamY - 20), 5, Paint()..color = Colors.white38);

    // Beam
    canvas.drawLine(left, right,
        Paint()..color = match ? const Color(0xFF34D399) : Colors.white54
          ..strokeWidth = 4..strokeCap = StrokeCap.round);

    // Pans
    _pan(canvas, left, _dimText(m, l, t), const Color(0xFF38BDF8), 'YOUR SIDE');
    _pan(canvas, right, _dimText(tm, tl, tt), const Color(0xFFF59E0B), targetName.toUpperCase());

    _label(canvas, match ? 'BALANCED · consistent' : 'UNBALANCED · not consistent',
        Offset(cx, 20), match ? const Color(0xFF34D399) : Colors.white54, 12);
  }

  String _dimText(int m, int l, int t) {
    final parts = <String>[];
    if (m != 0) parts.add('M${_sup(m)}');
    if (l != 0) parts.add('L${_sup(l)}');
    if (t != 0) parts.add('T${_sup(t)}');
    return parts.isEmpty ? 'M⁰L⁰T⁰' : parts.join(' ');
  }

  static String _sup(int n) {
    if (n == 1) return '';
    const map = {'-': '⁻', '0': '⁰', '1': '¹', '2': '²', '3': '³', '4': '⁴'};
    return n.toString().split('').map((c) => map[c] ?? c).join();
  }

  void _pan(Canvas canvas, Offset anchor, String text, Color color, String tag) {
    final pan = Offset(anchor.dx, anchor.dy + 34);
    canvas.drawLine(anchor, Offset(pan.dx - 26, pan.dy), Paint()..color = Palette.stageLine..strokeWidth = 1);
    canvas.drawLine(anchor, Offset(pan.dx + 26, pan.dy), Paint()..color = Palette.stageLine..strokeWidth = 1);
    final rect = RRect.fromRectAndRadius(
      Rect.fromCenter(center: pan, width: 96, height: 40), const Radius.circular(8));
    canvas.drawRRect(rect, Paint()..color = color.withValues(alpha: 0.18));
    canvas.drawRRect(rect, Paint()..color = color..style = PaintingStyle.stroke..strokeWidth = 1.5);
    _label(canvas, text, pan, Colors.white, 14);
    _label(canvas, tag, Offset(pan.dx, pan.dy + 30), color, 9);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fontSize) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(color: color, fontSize: fontSize, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_DimPainter old) =>
      old.m != m || old.l != l || old.t != t ||
      old.tm != tm || old.tl != tl || old.tt != tt || old.match != match ||
      old.wobble != wobble;
}
