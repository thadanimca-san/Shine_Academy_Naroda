import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Faraday & Lenz Law Sandbox — a bar magnet approaches/recedes from a coil.
/// Students set the magnet's speed and direction and watch flux, induced EMF
/// (ε = -dΦ/dt) and the galvanometer needle respond live, with Lenz's law
/// direction shown by an induced-current loop arrow.
class FaradayLenzSandbox extends StatefulWidget {
  const FaradayLenzSandbox({super.key});

  @override
  State<FaradayLenzSandbox> createState() => _FaradayLenzSandboxState();
}

class _FaradayLenzSandboxState extends State<FaradayLenzSandbox>
    with SingleTickerProviderStateMixin {
  double _speed = 0.4; // relative speed of magnet, signed by _approaching
  bool _approaching = true;
  double _magnetX = 0.15; // 0..1 position along the track (left = far, right = at coil)
  late final Ticker _ticker;
  Duration _last = Duration.zero;
  double _emf = 0; // computed live
  double _needle = 0; // galvanometer deflection, smoothed

  static const double _coilPos = 0.62; // coil centre position on track
  static const double _fluxScale = 6.0; // arbitrary flux constant for realism

  double _fluxAt(double x) {
    final d = (x - _coilPos).abs();
    // Flux falls off with distance from magnet to coil (dipole-like falloff).
    return _fluxScale / (1 + (d * 8) * (d * 8));
  }

  @override
  void initState() {
    super.initState();
    _ticker = createTicker(_tick)..start();
  }

  @override
  void dispose() {
    _ticker.dispose();
    super.dispose();
  }

  void _tick(Duration elapsed) {
    final dt = math.min((elapsed - _last).inMicroseconds / 1e6, 0.032);
    _last = elapsed;
    final dir = _approaching ? 1.0 : -1.0;
    final prevFlux = _fluxAt(_magnetX);
    var nx = _magnetX + dir * _speed * dt * 0.5;
    if (nx < 0.02 || nx > 0.98) {
      // bounce and flip direction of travel at the ends
      _approaching = !_approaching;
      nx = nx.clamp(0.02, 0.98);
    }
    final newFlux = _fluxAt(nx);
    final dPhi = newFlux - prevFlux;
    final instEmf = -dPhi / (dt == 0 ? 1 : dt);
    setState(() {
      _magnetX = nx;
      _emf = instEmf;
      _needle = _needle + (instEmf.clamp(-40.0, 40.0) - _needle) * 0.25;
    });
  }

  @override
  Widget build(BuildContext context) {
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
            painter: _CoilPainter(magnetX: _magnetX, needle: _needle, emf: _emf),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('Induced EMF  ε = -dΦ/dt', _emf.toStringAsFixed(1), '(rel)',
                  Palette.chElectroMag)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Flux Φ through coil', _fluxAt(_magnetX).toStringAsFixed(2), '(rel)',
                  Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Magnet speed', _speed, 0.05, 1.2, '', const Color(0xFF38BDF8),
            (x) => setState(() => _speed = x)),
        Row(children: [
          Expanded(
            child: OutlinedButton(
              onPressed: () => setState(() => _approaching = !_approaching),
              child: Text(_approaching ? 'Direction: moving right →' : 'Direction: moving left ←'),
            ),
          ),
        ]),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: push the magnet TOWARD the coil and note the needle swings one way; pull it AWAY and the needle swings the OTHER way — Lenz\'s law: the induced current always opposes the CHANGE in flux, not the flux itself. Raise the speed and watch the EMF reading grow, even though the magnet\'s strength never changed.'),
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

  Widget _slider(String label, double value, double min, double max, String unit,
      Color color, ValueChanged<double> onChanged) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('$label = ${value.toStringAsFixed(2)} $unit',
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

class _CoilPainter extends CustomPainter {
  final double magnetX, needle, emf;
  _CoilPainter({required this.magnetX, required this.needle, required this.emf});

  @override
  void paint(Canvas canvas, Size size) {
    final trackY = size.height * 0.55;
    final coilCx = size.width * 0.62;

    // Track line
    canvas.drawLine(Offset(10, trackY), Offset(size.width - 10, trackY),
        Paint()..color = const Color(0x33FFFFFF)..strokeWidth = 1.5);

    // Coil: a few loops drawn as vertical ovals.
    final loopPaint = Paint()
      ..color = const Color(0xFFF97316)
      ..strokeWidth = 2.6
      ..style = PaintingStyle.stroke;
    for (int i = -2; i <= 2; i++) {
      canvas.drawOval(
          Rect.fromCenter(center: Offset(coilCx + i * 9, trackY), width: 16, height: 62), loopPaint);
    }
    _label(canvas, 'coil', Offset(coilCx, trackY + 44), const Color(0xFFFDBA74), 10);

    // Galvanometer above the coil.
    final galCenter = Offset(coilCx, trackY - 78);
    canvas.drawCircle(galCenter, 26, Paint()
      ..color = const Color(0x1AFFFFFF)
      ..style = PaintingStyle.fill);
    canvas.drawCircle(galCenter, 26, Paint()
      ..color = const Color(0x66FFFFFF)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.5);
    final needleAngle = (needle / 40).clamp(-1.0, 1.0) * (math.pi / 2.4);
    final needleEnd = galCenter + Offset(math.sin(needleAngle), -math.cos(needleAngle)) * 20;
    canvas.drawLine(galCenter, needleEnd, Paint()..color = const Color(0xFF34D399)..strokeWidth = 2.5);
    _label(canvas, 'G', galCenter + const Offset(0, -36), const Color(0xFFE5E7F0), 11);

    // Bar magnet: N (red) - S (blue) block.
    final magX = 20 + magnetX * (size.width - 40);
    final magRect = Rect.fromCenter(center: Offset(magX, trackY), width: 46, height: 20);
    canvas.drawRect(
        Rect.fromLTRB(magRect.left, magRect.top, magRect.center.dx, magRect.bottom),
        Paint()..color = const Color(0xFFDC2626));
    canvas.drawRect(
        Rect.fromLTRB(magRect.center.dx, magRect.top, magRect.right, magRect.bottom),
        Paint()..color = const Color(0xFF2563EB));
    _label(canvas, 'N', Offset(magRect.left + 11, trackY), Colors.white, 11);
    _label(canvas, 'S', Offset(magRect.right - 11, trackY), Colors.white, 11);

    // Induced current direction arrow on the near coil loop, if emf significant.
    if (emf.abs() > 1.5) {
      final curved = emf > 0; // sign flips the visual loop direction
      final arrowColor = const Color(0xFF34D399);
      final top = Offset(coilCx, trackY - 31);
      final bot = Offset(coilCx, trackY + 31);
      _arrow(canvas, curved ? top : bot, curved ? bot : top, arrowColor, 2.2);
      _label(canvas, 'induced I', Offset(coilCx + 34, trackY), arrowColor, 9);
    }
  }

  void _arrow(Canvas canvas, Offset a, Offset b, Color color, double w) {
    final p = Paint()
      ..color = color
      ..strokeWidth = w
      ..strokeCap = StrokeCap.round;
    canvas.drawLine(a, b, p);
    final dir = b - a;
    final len = dir.distance;
    if (len < 1) return;
    final un = dir / len;
    final n = Offset(-un.dy, un.dx);
    canvas.drawLine(b, b - un * 8 + n * 3.5, p);
    canvas.drawLine(b, b - un * 8 - n * 3.5, p);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style:
              TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_CoilPainter old) =>
      old.magnetX != magnetX || old.needle != needle || old.emf != emf;
}
