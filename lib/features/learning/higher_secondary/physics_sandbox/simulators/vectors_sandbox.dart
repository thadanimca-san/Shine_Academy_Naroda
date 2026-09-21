import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import '../widgets/sim_controls.dart';
import '../widgets/sim_kit.dart';

/// Vector Adder — two vectors, one resultant.
///
/// The student sets the magnitude and direction of two vectors and watches the
/// parallelogram resultant update live, along with its magnitude, angle and
/// x/y components. The key discovery: the resultant depends on the ANGLE
/// between the vectors, not just their sizes.
class VectorsSandbox extends StatefulWidget {
  const VectorsSandbox({super.key});

  @override
  State<VectorsSandbox> createState() => _VectorsSandboxState();
}

class _VectorsSandboxState extends State<VectorsSandbox>
    with TickerProviderStateMixin {
  double _a = 5, _thetaA = 0; // magnitude, degrees
  double _b = 4, _thetaB = 90;

  static const double _animSeconds = 3;
  late final SimClock _clock = SimClock(this, _onTick);

  void _onTick() {
    if (_clock.running && _clock.t >= _animSeconds) _clock.pause();
    setState(() {});
  }

  /// 0→1 sweep of the tip-to-tail construction; idle shows the full diagram.
  double get _progress {
    if (!_clock.running && _clock.t == 0) return 1;
    return (_clock.t / _animSeconds).clamp(0.0, 1.0);
  }

  void _animate() {
    _clock.reset();
    _clock.start();
  }

  @override
  void dispose() {
    _clock.dispose();
    super.dispose();
  }

  double get _ax => _a * math.cos(_thetaA * math.pi / 180);
  double get _ay => _a * math.sin(_thetaA * math.pi / 180);
  double get _bx => _b * math.cos(_thetaB * math.pi / 180);
  double get _by => _b * math.sin(_thetaB * math.pi / 180);
  double get _rx => _ax + _bx;
  double get _ry => _ay + _by;
  double get _r => math.sqrt(_rx * _rx + _ry * _ry);
  double get _rTheta => math.atan2(_ry, _rx) * 180 / math.pi;
  double get _between => (_thetaB - _thetaA).abs();

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
            painter: _VectorPainter(
                ax: _ax, ay: _ay, bx: _bx, by: _by, rx: _rx, ry: _ry,
                progress: _progress),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(
          children: [
            Expanded(child: _readout('|R| resultant', _r.toStringAsFixed(2), Palette.primary)),
            const SizedBox(width: Gap.x3),
            Expanded(child: _readout('angle of R', '${_rTheta.toStringAsFixed(1)}°', Palette.accent)),
          ],
        ),
        const SizedBox(height: Gap.x3),
        Row(
          children: [
            Expanded(child: _readout('Rₓ = Aₓ + Bₓ', _rx.toStringAsFixed(2), const Color(0xFF38BDF8))),
            const SizedBox(width: Gap.x3),
            Expanded(child: _readout('Rᵧ = Aᵧ + Bᵧ', _ry.toStringAsFixed(2), const Color(0xFF34D399))),
          ],
        ),
        const SizedBox(height: Gap.x3),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.infoSoft,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Text(
            'Angle between A and B: ${_between.toStringAsFixed(0)}°   →   '
            '|R|² = A² + B² + 2·A·B·cos(θ) = ${(_a * _a + _b * _b + 2 * _a * _b * math.cos(_between * math.pi / 180)).toStringAsFixed(2)}',
            style: Type.caption.copyWith(fontFamily: 'monospace', color: Palette.textBody),
          ),
        ),
        const SizedBox(height: Gap.x3),
        _slider('A magnitude', _a, 0, 8, '', const Color(0xFFF97316), (v) => setState(() => _a = v)),
        _slider('A direction', _thetaA, 0, 360, '°', const Color(0xFFF97316), (v) => setState(() => _thetaA = v)),
        _slider('B magnitude', _b, 0, 8, '', const Color(0xFF38BDF8), (v) => setState(() => _b = v)),
        _slider('B direction', _thetaB, 0, 360, '°', const Color(0xFF38BDF8), (v) => setState(() => _thetaB = v)),
        const SizedBox(height: Gap.x2),
        SimControls(
          running: _clock.running,
          onStart: _animate,
          onPause: _clock.pause,
          onReset: _clock.reset,
          startLabel: 'Animate tip-to-tail',
        ),
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
          Text(value, style: Type.bodyStrong.copyWith(fontSize: 16, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max, String unit,
      Color color, ValueChanged<double> onChanged) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('$label = ${value.toStringAsFixed(unit == '°' ? 0 : 1)} $unit',
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

class _VectorPainter extends CustomPainter {
  final double ax, ay, bx, by, rx, ry;
  final double progress; // 1 = full diagram; <1 animates A → B tip-to-tail → R
  _VectorPainter({required this.ax, required this.ay, required this.bx, required this.by, required this.rx, required this.ry, this.progress = 1});

  static const _cA = Color(0xFFF97316);
  static const _cB = Color(0xFF38BDF8);
  static const _cR = Color(0xFFA78BFA);

  @override
  void paint(Canvas canvas, Size size) {
    final origin = Offset(size.width * 0.5, size.height * 0.55);
    const scale = 16.0; // px per unit
    Offset p(double x, double y) => origin + Offset(x * scale, -y * scale);

    // Axes
    final axis = Paint()..color = Palette.stageLine..strokeWidth = 1;
    canvas.drawLine(Offset(0, origin.dy), Offset(size.width, origin.dy), axis);
    canvas.drawLine(Offset(origin.dx, 0), Offset(origin.dx, size.height), axis);

    if (progress >= 1) {
      // Full parallelogram diagram
      final guide = Paint()..color = Colors.white24..strokeWidth = 1;
      canvas.drawLine(p(ax, ay), p(rx, ry), guide);
      canvas.drawLine(p(bx, by), p(rx, ry), guide);

      _arrow(canvas, origin, p(ax, ay), _cA, 'A');
      _arrow(canvas, origin, p(bx, by), _cB, 'B');
      _arrow(canvas, origin, p(rx, ry), _cR, 'R');
      return;
    }

    // Animated tip-to-tail construction: A grows, then B from A's tip, then R.
    double phase(double from, double to) =>
        ((progress - from) / (to - from)).clamp(0.0, 1.0);

    final fA = phase(0, 1 / 3);
    if (fA > 0) {
      _arrow(canvas, origin, p(ax * fA, ay * fA), _cA, fA == 1 ? 'A' : '');
    }
    final fB = phase(1 / 3, 2 / 3);
    if (fB > 0) {
      _arrow(canvas, p(ax, ay), p(ax + bx * fB, ay + by * fB), _cB, fB == 1 ? 'B' : '');
    }
    final fR = phase(2 / 3, 1);
    if (fR > 0) {
      _arrow(canvas, origin, p(rx * fR, ry * fR), _cR, fR == 1 ? 'R' : '');
    }
  }

  void _arrow(Canvas canvas, Offset from, Offset to, Color color, String label) {
    final paint = Paint()..color = color..strokeWidth = 3..strokeCap = StrokeCap.round;
    canvas.drawLine(from, to, paint);
    final dir = (to - from);
    final len = dir.distance;
    if (len < 2) return;
    final u = dir / len;
    final n = Offset(-u.dy, u.dx);
    canvas.drawLine(to, to - u * 10 + n * 5, paint);
    canvas.drawLine(to, to - u * 10 - n * 5, paint);
    _label(canvas, label, to + u * 12, color, 12);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fontSize) {
    final tp = TextPainter(
      text: TextSpan(text: text, style: TextStyle(color: color, fontSize: fontSize, fontWeight: FontWeight.w800, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_VectorPainter old) =>
      old.ax != ax || old.ay != ay || old.bx != bx || old.by != by ||
      old.rx != rx || old.ry != ry || old.progress != progress;
}
