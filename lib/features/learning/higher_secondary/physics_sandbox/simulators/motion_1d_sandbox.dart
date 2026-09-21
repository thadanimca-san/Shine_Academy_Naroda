import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/sim_controls.dart';
import '../widgets/sim_kit.dart';

/// Motion in 1D — a car on a straight road under constant acceleration.
///
/// Students set u and a (live, even mid-run), press Start, and watch the car
/// obey v = u + at and s = ut + ½at². Braking (negative a) lets them discover
/// the car slowing, stopping, then reversing.
class Motion1DSandbox extends StatefulWidget {
  const Motion1DSandbox({super.key});

  @override
  State<Motion1DSandbox> createState() => _Motion1DSandboxState();
}

class _Motion1DSandboxState extends State<Motion1DSandbox>
    with TickerProviderStateMixin {
  double _u = 4; // m/s
  double _a = 2; // m/s²

  late final SimClock _clock = SimClock(this, () => setState(() {}));

  double get _t => _clock.t;
  double get _v => _u + _a * _t;
  double get _s => _u * _t + 0.5 * _a * _t * _t;

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
        SandboxStage(
          child: CustomPaint(
            painter: _RoadPainter(s: _s, v: _v),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        TelemetryRow([
          TelemetryChip('t time', '${_t.toStringAsFixed(1)} s'),
          TelemetryChip('v velocity', '${_v.toStringAsFixed(1)} m/s',
              color: Palette.accent),
          TelemetryChip('s position', '${_s.toStringAsFixed(1)} m',
              color: Palette.success),
        ]),
        const SizedBox(height: Gap.x3),
        SimSlider(
          label: 'Initial velocity u',
          value: _u,
          min: 0,
          max: 15,
          unit: 'm/s',
          onChanged: (v) => setState(() => _u = v),
        ),
        SimSlider(
          label: 'Acceleration a',
          value: _a,
          min: -6,
          max: 6,
          unit: 'm/s²',
          color: Palette.accent,
          onChanged: (v) => setState(() => _a = v),
        ),
        const SizedBox(height: Gap.x2),
        SimControls(
          running: _clock.running,
          onStart: _clock.start,
          onPause: _clock.pause,
          onReset: _clock.reset,
        ),
      ],
    );
  }
}

class _RoadPainter extends CustomPainter {
  final double s, v;
  _RoadPainter({required this.s, required this.v});

  @override
  void paint(Canvas canvas, Size size) {
    final groundY = size.height * 0.72;
    const metersPerPx = 0.25; // 4 px per metre
    final worldWidth = size.width * metersPerPx;

    // Road
    canvas.drawLine(Offset(0, groundY), Offset(size.width, groundY),
        Paint()..color = Colors.white38..strokeWidth = 3);

    // The camera follows the car in world blocks: markers scroll under it.
    final blockStart = (s / worldWidth).floorToDouble() * worldWidth;
    for (double m = blockStart - worldWidth; m < blockStart + 2 * worldWidth; m += 10) {
      final x = (m - s) / metersPerPx + size.width * 0.35;
      if (x < -20 || x > size.width + 20) continue;
      canvas.drawLine(Offset(x, groundY), Offset(x, groundY + 7),
          Paint()..color = Colors.white30..strokeWidth = 1.5);
      _label(canvas, '${m.round()}m', Offset(x, groundY + 16),
          Colors.amberAccent.withValues(alpha: 0.8), 9);
    }

    // Car — fixed at 35% of the stage; the world moves past it.
    final carX = size.width * 0.35;
    const w = 46.0, h = 20.0;
    final body = RRect.fromRectAndRadius(
        Rect.fromLTWH(carX - w / 2, groundY - h - 8, w, h), const Radius.circular(6));
    canvas.drawRRect(body, Paint()..color = const Color(0xFF2DD4BF));
    canvas.drawRRect(
        RRect.fromRectAndRadius(
            Rect.fromLTWH(carX - w / 4, groundY - h - 17, w / 2, 11),
            const Radius.circular(4)),
        Paint()..color = const Color(0xFF14B8A6));
    for (final dx in [-w / 2 + 10, w / 2 - 10]) {
      canvas.drawCircle(Offset(carX + dx, groundY - 4), 5, Paint()..color = Colors.black87);
      canvas.drawCircle(Offset(carX + dx, groundY - 4), 2, Paint()..color = Colors.white54);
    }

    // Velocity arrow above the car
    if (v.abs() > 0.05) {
      final len = (v.abs() * 6).clamp(10.0, 90.0) * v.sign;
      final y = groundY - h - 34;
      final p = Paint()
        ..color = Palette.accent
        ..strokeWidth = 3
        ..strokeCap = StrokeCap.round;
      canvas.drawLine(Offset(carX, y), Offset(carX + len, y), p);
      final tip = Offset(carX + len, y);
      canvas.drawLine(tip, tip + Offset(-8 * v.sign, -4), p);
      canvas.drawLine(tip, tip + Offset(-8 * v.sign, 4), p);
      _label(canvas, 'v', Offset(carX + len / 2, y - 10), Palette.accent, 11);
    }
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(
              color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_RoadPainter old) => old.s != s || old.v != v;
}
