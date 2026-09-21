import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Doppler Effect Sandbox — a moving sound source emits wavefronts that
/// bunch up ahead of it and spread out behind it; an observer may also move.
/// Students adjust vs (source speed) and vo (observer speed) and read the
/// apparent frequency f' = f(v ± vo)/(v ∓ vs).
class DopplerEffectSandbox extends StatefulWidget {
  const DopplerEffectSandbox({super.key});

  @override
  State<DopplerEffectSandbox> createState() => _DopplerEffectSandboxState();
}

class _DopplerEffectSandboxState extends State<DopplerEffectSandbox>
    with SingleTickerProviderStateMixin {
  static const double _vSound = 340.0; // m/s, speed of sound reference
  double _f = 500; // source frequency Hz
  double _vs = 20; // source velocity, m/s (+ve = moving toward observer, i.e. rightward)
  double _vo = 0; // observer velocity, m/s (+ve = moving toward source, i.e. leftward, closing the gap)
  double _sourceX = 0.25; // fractional position along stage
  late final Ticker _ticker;
  Duration _last = Duration.zero;
  final List<_Wavefront> _fronts = [];
  double _emitAccum = 0;

  // Apparent frequency the (stationary-relative) observer standing to the
  // RIGHT of the source hears: f' = f (v + vo) / (v - vs)
  // vs > 0 means source moves toward observer (to the right) -> denominator shrinks -> higher pitch.
  // vo > 0 means observer moves toward source (to the left, closing in) -> numerator grows -> higher pitch.
  double get _fApparent => _f * (_vSound + _vo) / (_vSound - _vs);

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
    setState(() {
      // advance source position (wraps around for a continuous demo)
      _sourceX += (_vs / _vSound) * dt * 0.5;
      if (_sourceX > 0.85) _sourceX = 0.15;
      if (_sourceX < 0.15) _sourceX = 0.85;

      // emit a wavefront periodically, scaled by source frequency
      _emitAccum += dt * (_f / 90);
      if (_emitAccum >= 1) {
        _emitAccum = 0;
        _fronts.add(_Wavefront(originX: _sourceX, age: 0));
      }
      for (final w in _fronts) {
        w.age += dt;
      }
      _fronts.removeWhere((w) => w.age > 3.2);
    });
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 220,
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
            painter: _DopplerPainter(sourceX: _sourceX, fronts: _fronts, vs: _vs, vo: _vo),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Source freq  f',
              _f.toStringAsFixed(0), 'Hz', Palette.chWaves)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Apparent  f\'',
              _fApparent.toStringAsFixed(0), 'Hz', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Source freq f', _f, 200, 1000, 'Hz', const Color(0xFF0EA5E9),
            (x) => setState(() => _f = x)),
        _slider('Source speed vₛ (→ toward observer)', _vs, -40, 40, 'm/s', const Color(0xFF16A34A),
            (x) => setState(() => _vs = x)),
        _slider('Observer speed v₀ (→ toward source)', _vo, -40, 40, 'm/s', Palette.accent,
            (x) => setState(() => _vo = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: push vₛ positive (source moving toward the observer on the right) — the wavefronts crowd together ahead of it and f\' rises. Make vₛ negative and they spread out behind it, dropping f\' — exactly why an ambulance siren drops in pitch the instant it passes you.'),
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
              style: Type.bodyStrong.copyWith(
                  fontSize: 16, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max, String unit,
      Color color, ValueChanged<double> onChanged) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('$label = ${value.toStringAsFixed(0)} $unit',
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

class _Wavefront {
  final double originX; // fractional
  double age;
  _Wavefront({required this.originX, required this.age});
}

class _DopplerPainter extends CustomPainter {
  final double sourceX;
  final List<_Wavefront> fronts;
  final double vs, vo;
  _DopplerPainter({required this.sourceX, required this.fronts, required this.vs, required this.vo});

  @override
  void paint(Canvas canvas, Size size) {
    StageBackdrop.paint(canvas, size, groundY: size.height);

    final midY = size.height * 0.42;

    // Wavefronts as expanding circles, centre drifts with source motion history.
    for (final w in fronts) {
      final radius = w.age * 55.0;
      final alpha = (1 - w.age / 3.2).clamp(0.0, 1.0);
      final center = Offset(w.originX * size.width, midY);
      canvas.drawCircle(center, radius, Paint()
        ..color = Palette.chWaves.withValues(alpha: alpha * 0.7)
        ..style = PaintingStyle.stroke
        ..strokeWidth = 2);
    }

    // Source dot + velocity arrow.
    final srcPos = Offset(sourceX * size.width, midY);
    canvas.drawCircle(srcPos, 8, Paint()..color = Palette.accent);
    _label(canvas, 'S', srcPos - const Offset(0, 20), Palette.accent, 12);
    if (vs.abs() > 0.5) {
      final dir = vs > 0 ? 1.0 : -1.0;
      _arrow(canvas, srcPos, srcPos + Offset(dir * 26, 0), const Color(0xFF16A34A), 2.5);
    }

    // Observer fixed on the right edge with a velocity arrow (toward/away from source = left/right).
    final obsPos = Offset(size.width * 0.92, midY);
    canvas.drawCircle(obsPos, 8, Paint()..color = const Color(0xFF38BDF8));
    _label(canvas, 'O', obsPos - const Offset(0, 20), const Color(0xFF38BDF8), 12);
    if (vo.abs() > 0.5) {
      final dir = vo > 0 ? -1.0 : 1.0; // vo>0 = moving toward source = leftward
      _arrow(canvas, obsPos, obsPos + Offset(dir * 26, 0), Palette.accent, 2.5);
    }

    _label(canvas, 'sound speed v = 340 m/s (reference medium)',
        Offset(size.width / 2, size.height - 16), const Color(0xFFA5A9BF), 10);
  }

  void _arrow(Canvas canvas, Offset a, Offset b, Color color, double w) {
    final p = Paint()..color = color..strokeWidth = w..strokeCap = StrokeCap.round;
    canvas.drawLine(a, b, p);
    final dir = b - a;
    final len = dir.distance;
    if (len < 1) return;
    final un = dir / len;
    final n = Offset(-un.dy, un.dx);
    canvas.drawLine(b, b - un * 9 + n * 4, p);
    canvas.drawLine(b, b - un * 9 - n * 4, p);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_DopplerPainter old) => true;
}
