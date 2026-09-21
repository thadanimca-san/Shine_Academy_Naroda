import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Superposition & Beats Sandbox — two close-frequency waves add to form a
/// slowly-modulated "beat" envelope. Students tune f1 and f2 and watch the
/// beat frequency f_beat = |f1 - f2| appear as the throb of the envelope.
class SuperpositionBeatsSandbox extends StatefulWidget {
  const SuperpositionBeatsSandbox({super.key});

  @override
  State<SuperpositionBeatsSandbox> createState() => _SuperpositionBeatsSandboxState();
}

class _SuperpositionBeatsSandboxState extends State<SuperpositionBeatsSandbox>
    with SingleTickerProviderStateMixin {
  double _f1 = 6.0; // relative frequency units
  double _f2 = 7.0;
  double _t = 0;
  late final Ticker _ticker;
  Duration _last = Duration.zero;

  double get _beatFreq => (_f1 - _f2).abs();

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
    setState(() => _t += dt * 0.6);
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 260,
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
            painter: _BeatsPainter(f1: _f1, f2: _f2, t: _t),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Beat freq  |f1-f2|',
              _beatFreq.toStringAsFixed(2), 'Hz (rel)', Palette.chWaves)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Beat period  1/f_beat',
              _beatFreq < 0.01 ? '∞' : (1 / _beatFreq).toStringAsFixed(2), 's (rel)', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Frequency f₁', _f1, 3, 12, 'Hz', const Color(0xFF38BDF8),
            (x) => setState(() => _f1 = x)),
        _slider('Frequency f₂', _f2, 3, 12, 'Hz', const Color(0xFFF97316),
            (x) => setState(() => _f2 = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: bring f₂ close to f₁ — the beat envelope (bottom, bold curve) throbs SLOWER and slower. Set f₁ = f₂ exactly and the beats vanish (zero beats) — this is literally how musicians tune instruments by ear.'),
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

class _BeatsPainter extends CustomPainter {
  final double f1, f2, t;
  _BeatsPainter({required this.f1, required this.f2, required this.t});

  @override
  void paint(Canvas canvas, Size size) {
    StageBackdrop.paint(canvas, size, groundY: size.height);

    final rowH = size.height / 3;
    _drawWaveRow(canvas, size, 0, rowH, f1, const Color(0xFF38BDF8), 'wave 1 (f₁)');
    _drawWaveRow(canvas, size, rowH, rowH, f2, const Color(0xFFF97316), 'wave 2 (f₂)');
    _drawSumRow(canvas, size, rowH * 2, rowH);
  }

  void _drawWaveRow(Canvas canvas, Size size, double top, double h, double f, Color color, String label) {
    final midY = top + h / 2;
    final amp = h * 0.32;
    final path = Path();
    for (double x = 0; x <= size.width; x += 2) {
      final phase = 2 * math.pi * f * (x / size.width) - 2 * math.pi * f * t;
      final y = midY - amp * math.sin(phase);
      if (x == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
    }
    canvas.drawPath(path, Paint()
      ..color = color
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2);
    canvas.drawLine(Offset(0, midY), Offset(size.width, midY),
        Paint()..color = const Color(0x22FFFFFF)..strokeWidth = 1);
    _label(canvas, label, const Offset(8, 0) + Offset(0, top + 12), color, 11, left: true);
  }

  void _drawSumRow(Canvas canvas, Size size, double top, double h) {
    final midY = top + h / 2;
    final amp = h * 0.42 / 2; // each component amplitude 1, sum max 2
    final path = Path();
    final envUpper = Path();
    final envLower = Path();
    for (double x = 0; x <= size.width; x += 2) {
      final phase1 = 2 * math.pi * f1 * (x / size.width) - 2 * math.pi * f1 * t;
      final phase2 = 2 * math.pi * f2 * (x / size.width) - 2 * math.pi * f2 * t;
      final y1 = math.sin(phase1);
      final y2 = math.sin(phase2);
      final sum = y1 + y2;
      final y = midY - amp * sum;
      if (x == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
      // Envelope: 2*cos((f1-f2)/2 * angle) traced via beat term.
      final beatPhase = math.pi * (f1 - f2) * (x / size.width) - math.pi * (f1 - f2) * t;
      final env = 2 * amp * (math.cos(beatPhase)).abs();
      if (x == 0) {
        envUpper.moveTo(x, midY - env);
        envLower.moveTo(x, midY + env);
      } else {
        envUpper.lineTo(x, midY - env);
        envLower.lineTo(x, midY + env);
      }
    }
    canvas.drawPath(envUpper, Paint()
      ..color = const Color(0x66FFFFFF)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.4);
    canvas.drawPath(envLower, Paint()
      ..color = const Color(0x66FFFFFF)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.4);
    canvas.drawPath(path, Paint()
      ..color = Palette.accent
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.6);
    canvas.drawLine(Offset(0, midY), Offset(size.width, midY),
        Paint()..color = const Color(0x22FFFFFF)..strokeWidth = 1);
    _label(canvas, 'sum (beats)', Offset(8, top + 12), Palette.accent, 11, left: true);
  }

  void _label(Canvas canvas, String text, Offset topLeft, Color color, double fs, {bool left = false}) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, topLeft);
  }

  @override
  bool shouldRepaint(_BeatsPainter old) => old.f1 != f1 || old.f2 != f2 || old.t != t;
}
