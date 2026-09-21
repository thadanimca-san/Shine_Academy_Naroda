import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/sim_controls.dart';
import '../widgets/sim_kit.dart';

/// Newton's First Law — a puck on adjustable ground.
///
/// Give the puck one push, then watch what the surface does to it. On ice
/// (μ = 0) it glides forever; raise μ and friction eats the motion. The law
/// becomes visible: no force → no change in velocity.
class FirstLawSandbox extends StatefulWidget {
  const FirstLawSandbox({super.key});

  @override
  State<FirstLawSandbox> createState() => _FirstLawSandboxState();
}

class _FirstLawSandboxState extends State<FirstLawSandbox>
    with TickerProviderStateMixin {
  double _push = 8; // initial velocity m/s
  double _mu = 0.0; // friction coefficient
  static const double _g = 9.8;

  double _v = 0, _x = 0, _lastT = 0;
  bool _pushed = false;

  late final SimClock _clock = SimClock(this, _onTick);

  void _onTick() {
    final dt = _clock.t - _lastT;
    _lastT = _clock.t;
    if (_pushed && _v > 0) {
      _v = (_v - _mu * _g * dt).clamp(0.0, double.infinity);
      _x += _v * dt;
    }
    setState(() {});
  }

  void _start() {
    if (!_pushed || _v <= 0) {
      _v = _push;
      _pushed = true;
    }
    _clock.start();
  }

  void _reset() {
    _clock.reset();
    _lastT = 0;
    _v = 0;
    _x = 0;
    _pushed = false;
    setState(() {});
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
        SandboxStage(
          child: CustomPaint(
            painter: _PuckPainter(x: _x, v: _v, mu: _mu),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        TelemetryRow([
          TelemetryChip('v velocity', '${_v.toStringAsFixed(1)} m/s'),
          TelemetryChip('distance', '${_x.toStringAsFixed(1)} m', color: Palette.success),
          TelemetryChip('friction decel',
              '${(_v > 0 ? _mu * _g : 0).toStringAsFixed(1)} m/s²',
              color: Palette.danger),
        ]),
        const SizedBox(height: Gap.x3),
        SimSlider(
          label: 'Push strength (initial v)',
          value: _push,
          min: 2,
          max: 15,
          unit: 'm/s',
          onChanged: (v) => setState(() => _push = v),
        ),
        SimSlider(
          label: 'Surface friction μ',
          value: _mu,
          min: 0,
          max: 0.8,
          decimals: 2,
          color: Palette.danger,
          onChanged: (v) => setState(() => _mu = v),
        ),
        const SizedBox(height: Gap.x2),
        SimControls(
          running: _clock.running,
          onStart: _start,
          onPause: _clock.pause,
          onReset: _reset,
          startLabel: 'Push the puck',
        ),
      ],
    );
  }
}

class _PuckPainter extends CustomPainter {
  final double x, v, mu;
  _PuckPainter({required this.x, required this.v, required this.mu});

  @override
  void paint(Canvas canvas, Size size) {
    final groundY = size.height * 0.72;

    // Surface tint: icy blue when frictionless → rough amber as μ grows
    final surface = Color.lerp(
        const Color(0xFF38BDF8), const Color(0xFF92400E), (mu / 0.8).clamp(0, 1))!;
    canvas.drawRect(
        Rect.fromLTWH(0, groundY, size.width, 6),
        Paint()..color = surface.withValues(alpha: 0.8));

    // Distance markers scroll under the puck (camera follows it).
    const pxPerM = 5.0;
    final worldW = size.width / pxPerM;
    final blockStart = (x / worldW).floorToDouble() * worldW;
    for (double m = blockStart - worldW; m < blockStart + 2 * worldW; m += 10) {
      final px = (m - x) * pxPerM + size.width * 0.35;
      if (px < -10 || px > size.width + 10) continue;
      canvas.drawLine(Offset(px, groundY + 6), Offset(px, groundY + 13),
          Paint()..color = Colors.white30..strokeWidth = 1.5);
      _label(canvas, '${m.round()}m', Offset(px, groundY + 21), Colors.amberAccent, 9);
    }

    // Puck
    final puck = Offset(size.width * 0.35, groundY - 11);
    canvas.drawOval(
        Rect.fromCenter(center: puck, width: 40, height: 20),
        Paint()..color = const Color(0xFF2DD4BF));
    canvas.drawOval(
        Rect.fromCenter(center: puck.translate(0, -4), width: 34, height: 12),
        Paint()..color = const Color(0xFF5EEAD4));

    // Velocity arrow
    if (v > 0.05) {
      final len = (v * 7).clamp(12.0, 100.0);
      final y = puck.dy - 26;
      final p = Paint()
        ..color = Palette.accent
        ..strokeWidth = 3
        ..strokeCap = StrokeCap.round;
      canvas.drawLine(Offset(puck.dx, y), Offset(puck.dx + len, y), p);
      canvas.drawLine(Offset(puck.dx + len, y), Offset(puck.dx + len - 8, y - 4), p);
      canvas.drawLine(Offset(puck.dx + len, y), Offset(puck.dx + len - 8, y + 4), p);
    }

    _label(
        canvas,
        mu < 0.02 ? 'FRICTIONLESS ICE — nothing slows it' : 'μ = ${mu.toStringAsFixed(2)}',
        Offset(size.width / 2, 18),
        mu < 0.02 ? const Color(0xFF7DD3FC) : Colors.white54,
        11);
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
  bool shouldRepaint(_PuckPainter old) => old.x != x || old.v != v || old.mu != mu;
}
