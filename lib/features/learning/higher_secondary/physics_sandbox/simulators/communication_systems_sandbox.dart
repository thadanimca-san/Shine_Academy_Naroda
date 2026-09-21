import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Communication Systems Sandbox — amplitude modulation (AM) visualization.
/// A low-frequency message signal modulates a high-frequency carrier; the
/// adjustable modulation index m = Am/Ac controls how deeply the envelope
/// follows the message, from under-modulation to over-modulation.
class CommunicationSystemsSandbox extends StatefulWidget {
  const CommunicationSystemsSandbox({super.key});

  @override
  State<CommunicationSystemsSandbox> createState() => _CommunicationSystemsSandboxState();
}

class _CommunicationSystemsSandboxState extends State<CommunicationSystemsSandbox>
    with SingleTickerProviderStateMixin {
  double _carrierFreq = 10.0; // relative carrier frequency
  double _messageFreq = 1.0; // relative message (baseband) frequency
  double _modIndex = 0.5; // m = Am/Ac, 0..1.5 (allows over-modulation demo)

  late final Ticker _ticker;
  Duration _last = Duration.zero;
  double _t = 0;

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
    setState(() => _t = (_t + dt * 0.4) % 1000);
  }

  double get _bandwidth => 2 * _messageFreq; // BW = 2fm for AM

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
            painter: _AmPainter(
              t: _t,
              carrierFreq: _carrierFreq,
              messageFreq: _messageFreq,
              modIndex: _modIndex,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('Modulation index  m', _modIndex.toStringAsFixed(2), '',
                  _modIndex > 1 ? const Color(0xFFEF4444) : Palette.accent)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Bandwidth  2fₘ', _bandwidth.toStringAsFixed(1), 'rel',
                  const Color(0xFF38BDF8))),
        ]),
        const SizedBox(height: Gap.x2),
        if (_modIndex > 1)
          Container(
            padding: const EdgeInsets.all(Gap.x2),
            margin: const EdgeInsets.only(bottom: Gap.x2),
            decoration: BoxDecoration(
              color: Palette.dangerSoft,
              borderRadius: BorderRadius.circular(Corner.md),
            ),
            child: Text(TrilingualService.instance.getUIText('m > 1: OVER-MODULATION — the envelope distorts and the signal cannot be recovered cleanly.'),
                style: Type.caption.copyWith(color: Palette.danger)),
          ),
        _slider('Carrier frequency  f_c', _carrierFreq, 6, 16, 'rel', const Color(0xFF7C3AED),
            (x) => setState(() => _carrierFreq = x)),
        _slider('Message frequency  f_m', _messageFreq, 0.5, 3, 'rel', const Color(0xFF16A34A),
            (x) => setState(() => _messageFreq = x)),
        _slider('Modulation index  m', _modIndex, 0, 1.5, '', const Color(0xFFF59E0B),
            (x) => setState(() => _modIndex = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: raise m from 0 toward 1 and watch the envelope (dotted outline) hug the modulated wave more tightly, following the message shape. Push m past 1 and the envelope starts clipping — over-modulation.'),
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

class _AmPainter extends CustomPainter {
  final double t, carrierFreq, messageFreq, modIndex;
  _AmPainter({
    required this.t,
    required this.carrierFreq,
    required this.messageFreq,
    required this.modIndex,
  });

  @override
  void paint(Canvas canvas, Size size) {
    const rowH = 62.0;
    _drawWave(canvas, size, 8, rowH, 'Message signal (baseband)', const Color(0xFF16A34A),
        (x) => math.sin(2 * math.pi * messageFreq * (x + t)));

    _drawWave(canvas, size, 8 + rowH, rowH, 'Carrier wave', const Color(0xFF7C3AED),
        (x) => math.sin(2 * math.pi * carrierFreq * (x + t)));

    _drawModulated(canvas, size, 8 + rowH * 2, rowH + 20);
  }

  void _drawWave(Canvas canvas, Size size, double top, double h, String label, Color color,
      double Function(double) fn) {
    final mid = top + h / 2;
    final amp = h / 2 - 6;
    final path = Path();
    for (var px = 0.0; px <= size.width; px += 2) {
      final x = px / size.width; // 0..1 normalized
      final y = mid - fn(x) * amp;
      if (px == 0) {
        path.moveTo(px, y);
      } else {
        path.lineTo(px, y);
      }
    }
    canvas.drawPath(path, Paint()..color = color..style = PaintingStyle.stroke..strokeWidth = 1.8);
    _label(canvas, label, Offset(8, top - 2), color, 9, alignLeft: true);
  }

  void _drawModulated(Canvas canvas, Size size, double top, double h) {
    final mid = top + h / 2;
    final amp = h / 2 - 8;
    final path = Path();
    final envUpper = Path();
    final envLower = Path();
    for (var px = 0.0; px <= size.width; px += 2) {
      final x = px / size.width;
      final message = math.sin(2 * math.pi * messageFreq * (x + t));
      final envelope = (1 + modIndex * message).clamp(0.0, 1.6);
      final carrier = math.sin(2 * math.pi * carrierFreq * (x + t));
      final y = mid - envelope * carrier * amp * 0.55;
      if (px == 0) {
        path.moveTo(px, y);
      } else {
        path.lineTo(px, y);
      }
      final yUp = mid - envelope * amp * 0.55;
      final yLo = mid + envelope * amp * 0.55;
      if (px == 0) {
        envUpper.moveTo(px, yUp);
        envLower.moveTo(px, yLo);
      } else {
        envUpper.lineTo(px, yUp);
        envLower.lineTo(px, yLo);
      }
    }
    canvas.drawPath(
        envUpper,
        Paint()
          ..color = Colors.white54
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1);
    canvas.drawPath(
        envLower,
        Paint()
          ..color = Colors.white54
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1);
    canvas.drawPath(
        path,
        Paint()
          ..color = const Color(0xFF38BDF8)
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.8);
    _label(canvas, 'Modulated (AM) wave — envelope follows message', Offset(8, top - 2),
        const Color(0xFF38BDF8), 9, alignLeft: true);
  }

  void _label(Canvas canvas, String text, Offset pos, Color color, double fs,
      {bool alignLeft = false}) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, pos);
  }

  @override
  bool shouldRepaint(_AmPainter old) =>
      old.t != t ||
      old.carrierFreq != carrierFreq ||
      old.messageFreq != messageFreq ||
      old.modIndex != modIndex;
}
