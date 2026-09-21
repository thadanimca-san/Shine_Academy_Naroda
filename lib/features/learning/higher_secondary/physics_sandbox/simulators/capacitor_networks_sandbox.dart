import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Capacitor Networks Sandbox — three capacitors the student can wire in
/// series or parallel, with a live equivalent-capacitance bar. The point to
/// discover: parallel adds (C grows), series is reciprocal (C shrinks below
/// the smallest member).
class CapacitorNetworksSandbox extends StatefulWidget {
  const CapacitorNetworksSandbox({super.key});

  @override
  State<CapacitorNetworksSandbox> createState() => _CapacitorNetworksSandboxState();
}

class _CapacitorNetworksSandboxState extends State<CapacitorNetworksSandbox> {
  double _c1 = 2.0, _c2 = 3.0, _c3 = 6.0; // µF
  double _v = 12.0; // volts
  bool _parallel = true;

  double get _cEq {
    if (_parallel) return _c1 + _c2 + _c3;
    return 1 / (1 / _c1 + 1 / _c2 + 1 / _c3);
  }

  double get _qTotal => _cEq * _v; // µC
  static const double _barMax = 12.0; // µF for scaling the bar

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
            painter: _NetworkPainter(c1: _c1, c2: _c2, c3: _c3, v: _v, parallel: _parallel),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Equivalent C', '${_cEq.toStringAsFixed(2)} µF', Palette.primary)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Total charge', '${_qTotal.toStringAsFixed(1)} µC', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        // Equivalent-C bar
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.surface,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(TrilingualService.instance.getUIText('EQUIVALENT CAPACITANCE'), style: Type.label.copyWith(fontSize: 9)),
              const SizedBox(height: 6),
              ClipRRect(
                borderRadius: BorderRadius.circular(Corner.pill),
                child: LinearProgressIndicator(
                  value: (_cEq / _barMax).clamp(0.0, 1.0),
                  minHeight: 10,
                  backgroundColor: Palette.surfaceAlt,
                  color: _parallel ? Palette.success : Palette.jee,
                ),
              ),
              const SizedBox(height: 4),
              Text(
                _parallel
                    ? 'Parallel: C_eq = C₁+C₂+C₃ — always larger than any one.'
                    : 'Series: 1/C_eq = 1/C₁+1/C₂+1/C₃ — always smaller than the smallest.',
                style: Type.caption.copyWith(fontSize: 11),
              ),
            ],
          ),
        ),
        const SizedBox(height: Gap.x3),
        // Series / parallel toggle
        Row(children: [
          Expanded(
            child: _toggleButton('Parallel', _parallel, () => setState(() => _parallel = true)),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _toggleButton('Series', !_parallel, () => setState(() => _parallel = false)),
          ),
        ]),
        const SizedBox(height: Gap.x2),
        _slider('C₁', _c1, 1, 10, 'µF', const Color(0xFFF97316), (v) => setState(() => _c1 = v)),
        _slider('C₂', _c2, 1, 10, 'µF', const Color(0xFF38BDF8), (v) => setState(() => _c2 = v)),
        _slider('C₃', _c3, 1, 10, 'µF', Palette.primary, (v) => setState(() => _c3 = v)),
        _slider('Battery V', _v, 2, 24, 'V', Palette.accent, (v) => setState(() => _v = v)),
      ],
    );
  }

  Widget _toggleButton(String label, bool active, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 12),
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: active ? Palette.primary : Palette.surfaceAlt,
          borderRadius: BorderRadius.circular(Corner.md),
        ),
        child: Text(label,
            style: Type.bodyStrong.copyWith(color: active ? Colors.white : Palette.textMuted)),
      ),
    );
  }

  Widget _meter(String label, String value, Color color) {
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
          Text(value, style: Type.bodyStrong.copyWith(fontSize: 15, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
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

class _NetworkPainter extends CustomPainter {
  final double c1, c2, c3, v;
  final bool parallel;
  _NetworkPainter({required this.c1, required this.c2, required this.c3, required this.v, required this.parallel});

  static const _colors = [Color(0xFFF97316), Color(0xFF38BDF8), Color(0xFF4F46E5)];

  @override
  void paint(Canvas canvas, Size size) {
    final wire = Paint()..color = Colors.white54..strokeWidth = 2;
    final caps = [c1, c2, c3];
    final leftX = 34.0;
    final rightX = size.width - 34;

    // Battery on the left
    _label(canvas, '${v.toStringAsFixed(0)}V', Offset(leftX - 14, size.height / 2), Colors.white70, 11);

    if (parallel) {
      // Three horizontal branches sharing left and right rails
      canvas.drawLine(Offset(leftX, 30), Offset(leftX, size.height - 30), wire);
      canvas.drawLine(Offset(rightX, 30), Offset(rightX, size.height - 30), wire);
      for (int i = 0; i < 3; i++) {
        final y = 45.0 + i * (size.height - 90) / 2;
        canvas.drawLine(Offset(leftX, y), Offset(size.width / 2 - 12, y), wire);
        canvas.drawLine(Offset(size.width / 2 + 12, y), Offset(rightX, y), wire);
        _capSymbol(canvas, Offset(size.width / 2, y), true, _colors[i], caps[i]);
      }
    } else {
      // Series chain along the middle
      final y = size.height / 2;
      canvas.drawLine(Offset(leftX, y), Offset(leftX, y), wire);
      double x = leftX;
      final seg = (rightX - leftX) / 3;
      for (int i = 0; i < 3; i++) {
        final capX = x + seg / 2;
        canvas.drawLine(Offset(x, y), Offset(capX - 12, y), wire);
        _capSymbol(canvas, Offset(capX, y), false, _colors[i], caps[i]);
        canvas.drawLine(Offset(capX + 12, y), Offset(x + seg, y), wire);
        x += seg;
      }
    }

    _label(canvas, parallel ? 'PARALLEL — same V, charges add' : 'SERIES — same Q, voltages add',
        Offset(size.width / 2, size.height - 14), Colors.white38, 10);
  }

  void _capSymbol(Canvas canvas, Offset c, bool horizontalPlates, Color color, double val) {
    final p = Paint()..color = color..strokeWidth = 3..strokeCap = StrokeCap.round;
    if (horizontalPlates) {
      canvas.drawLine(c + const Offset(-12, 0), c + const Offset(12, 0), p);
      canvas.drawLine(c + const Offset(-12, 8), c + const Offset(12, 8), p);
      _label(canvas, '${val.toStringAsFixed(1)}µF', c + const Offset(0, -12), color, 9);
    } else {
      canvas.drawLine(c + const Offset(0, -12), c + const Offset(0, 12), p);
      canvas.drawLine(c + const Offset(8, -12), c + const Offset(8, 12), p);
      _label(canvas, '${val.toStringAsFixed(1)}µF', c + const Offset(4, -22), color, 9);
    }
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
  bool shouldRepaint(_NetworkPainter old) =>
      old.c1 != c1 || old.c2 != c2 || old.c3 != c3 || old.v != v || old.parallel != parallel;
}
