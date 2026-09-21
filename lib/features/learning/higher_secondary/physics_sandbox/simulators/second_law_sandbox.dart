import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/sim_controls.dart';
import '../widgets/sim_kit.dart';

/// Newton's Second Law — force cart.
///
/// One cart, one force arrow, two sliders. Change F or m even while the cart
/// runs and watch a = F/m respond instantly — the law as a living machine.
class SecondLawSandbox extends StatefulWidget {
  const SecondLawSandbox({super.key});

  @override
  State<SecondLawSandbox> createState() => _SecondLawSandboxState();
}

class _SecondLawSandboxState extends State<SecondLawSandbox>
    with TickerProviderStateMixin {
  double _f = 10; // N
  double _m = 2; // kg

  double _v = 0, _x = 0, _lastT = 0;

  late final SimClock _clock = SimClock(this, _onTick);

  double get _a => _f / _m;

  void _onTick() {
    final dt = _clock.t - _lastT;
    _lastT = _clock.t;
    _v += _a * dt;
    _x += _v * dt;
    setState(() {});
  }

  void _reset() {
    _clock.reset();
    _lastT = 0;
    _v = 0;
    _x = 0;
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
            painter: _CartPainter(x: _x, f: _f, m: _m, v: _v),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        TelemetryRow([
          TelemetryChip('a = F/m', '${_a.toStringAsFixed(2)} m/s²'),
          TelemetryChip('v velocity', '${_v.toStringAsFixed(1)} m/s',
              color: Palette.accent),
          TelemetryChip('x distance', '${_x.toStringAsFixed(1)} m',
              color: Palette.success),
        ]),
        const SizedBox(height: Gap.x3),
        SimSlider(
          label: 'Applied force F',
          value: _f,
          min: 0,
          max: 40,
          unit: 'N',
          decimals: 0,
          onChanged: (v) => setState(() => _f = v),
        ),
        SimSlider(
          label: 'Cart mass m',
          value: _m,
          min: 0.5,
          max: 10,
          unit: 'kg',
          color: const Color(0xFF38BDF8),
          onChanged: (v) => setState(() => _m = v),
        ),
        const SizedBox(height: Gap.x2),
        SimControls(
          running: _clock.running,
          onStart: _clock.start,
          onPause: _clock.pause,
          onReset: _reset,
          startLabel: 'Apply the force',
        ),
      ],
    );
  }
}

class _CartPainter extends CustomPainter {
  final double x, f, m, v;
  _CartPainter({required this.x, required this.f, required this.m, required this.v});

  @override
  void paint(Canvas canvas, Size size) {
    final groundY = size.height * 0.72;
    canvas.drawLine(Offset(0, groundY), Offset(size.width, groundY),
        Paint()..color = Colors.white38..strokeWidth = 3);

    // Scrolling markers, camera on cart
    const pxPerM = 5.0;
    final worldW = size.width / pxPerM;
    final blockStart = (x / worldW).floorToDouble() * worldW;
    for (double mk = blockStart - worldW; mk < blockStart + 2 * worldW; mk += 10) {
      final px = (mk - x) * pxPerM + size.width * 0.4;
      if (px < -10 || px > size.width + 10) continue;
      canvas.drawLine(Offset(px, groundY), Offset(px, groundY + 7),
          Paint()..color = Colors.white30..strokeWidth = 1.5);
      _label(canvas, '${mk.round()}m', Offset(px, groundY + 15), Colors.amberAccent, 9);
    }

    // Cart: size grows subtly with mass
    final cartX = size.width * 0.4;
    final w = 40.0 + m * 3;
    final h = 20.0 + m * 1.6;
    canvas.drawRRect(
        RRect.fromRectAndRadius(
            Rect.fromLTWH(cartX - w / 2, groundY - h - 10, w, h),
            const Radius.circular(6)),
        Paint()..color = const Color(0xFF38BDF8));
    for (final dx in [-w / 2 + 10, w / 2 - 10]) {
      canvas.drawCircle(Offset(cartX + dx, groundY - 5), 5.5, Paint()..color = Colors.black87);
      canvas.drawCircle(Offset(cartX + dx, groundY - 5), 2, Paint()..color = Colors.white54);
    }
    _label(canvas, '${m.toStringAsFixed(1)} kg',
        Offset(cartX, groundY - h / 2 - 10), Colors.white, 11);

    // Force arrow pushing the cart
    if (f > 0.5) {
      final len = (f * 2.6).clamp(14.0, 110.0);
      final y = groundY - h / 2 - 10;
      final from = Offset(cartX - w / 2 - len, y);
      final to = Offset(cartX - w / 2 - 4, y);
      final p = Paint()
        ..color = const Color(0xFFF97316)
        ..strokeWidth = 4
        ..strokeCap = StrokeCap.round;
      canvas.drawLine(from, to, p);
      canvas.drawLine(to, to + const Offset(-9, -5), p);
      canvas.drawLine(to, to + const Offset(-9, 5), p);
      _label(canvas, 'F = ${f.round()} N', Offset(from.dx + len / 2, y - 14),
          const Color(0xFFF97316), 10);
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
  bool shouldRepaint(_CartPainter old) =>
      old.x != x || old.f != f || old.m != m || old.v != v;
}
