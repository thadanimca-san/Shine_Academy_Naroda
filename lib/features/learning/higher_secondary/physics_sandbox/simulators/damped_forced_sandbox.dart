import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Damping & Resonance Sandbox — a spring-mass oscillator with adjustable
/// damping coefficient (showing exponential amplitude decay and the
/// underdamped envelope ±Ae^(-bt/2m)) and an adjustable driving frequency
/// (showing the amplitude-vs-frequency resonance curve peak near ω ≈ ω0).
class DampedForcedSandbox extends StatefulWidget {
  const DampedForcedSandbox({super.key});

  @override
  State<DampedForcedSandbox> createState() => _DampedForcedSandboxState();
}

class _DampedForcedSandboxState extends State<DampedForcedSandbox>
    with SingleTickerProviderStateMixin {
  double _m = 1.0; // kg
  double _k = 4.0; // N/m spring constant
  double _b = 0.3; // damping coefficient (kg/s)
  double _omegaDrive = 2.0; // rad/s driving frequency
  double _simTime = 0;
  late final Ticker _ticker;
  Duration _last = Duration.zero;
  bool _forced = false; // toggle: free damped vs driven steady-state

  double get _omega0 => math.sqrt(_k / _m); // natural frequency
  double get _dampingRatioTerm => _b / (2 * _m); // decay rate in exponent

  // Steady-state driven amplitude (standard forced-oscillator formula).
  double _amplitudeAt(double omegaDrive) {
    const f0 = 1.0; // relative driving force amplitude
    final denom = math.sqrt(math.pow(_k - _m * omegaDrive * omegaDrive, 2) +
        math.pow(_b * omegaDrive, 2));
    return denom < 1e-6 ? 999 : f0 / denom;
  }

  double get _resonantAmplitude => _amplitudeAt(_omegaDrive);

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
    setState(() => _simTime += dt);
  }

  double _displacementAt(double t) {
    if (!_forced) {
      // Free damped oscillation: x = A e^{-bt/2m} cos(omega_d t)
      final decay = math.exp(-_dampingRatioTerm * t);
      final omegaDSq = _omega0 * _omega0 - _dampingRatioTerm * _dampingRatioTerm;
      final omegaD = omegaDSq > 0 ? math.sqrt(omegaDSq) : 0.0;
      return decay * math.cos(omegaD * t);
    } else {
      // Driven steady state, normalized amplitude for display.
      final amp = (_resonantAmplitude).clamp(0.0, 6.0);
      return amp * math.cos(_omegaDrive * t) / 6.0 * 1.4;
    }
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
            painter: _OscillatorPainter(
              t: _simTime,
              displacementFn: _displacementAt,
              forced: _forced,
              omega0: _omega0,
              omegaDrive: _omegaDrive,
              amplitudeFn: _amplitudeAt,
              decayRate: _dampingRatioTerm,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _modeButton('Free damped', !_forced, () => setState(() => _forced = false))),
          const SizedBox(width: Gap.x2),
          Expanded(child: _modeButton('Driven / resonance', _forced, () => setState(() => _forced = true))),
        ]),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Natural ω₀ = √(k/m)', _omega0.toStringAsFixed(2), 'rad/s', const Color(0xFF38BDF8))),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter(_forced ? 'Steady amplitude' : 'Decay rate b/2m',
                  _forced ? _resonantAmplitude.toStringAsFixed(2) : _dampingRatioTerm.toStringAsFixed(2),
                  _forced ? '(rel)' : '1/s', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Mass m', _m, 0.5, 3.0, 'kg', const Color(0xFF16A34A), (x) => setState(() => _m = x)),
        _slider('Spring constant k', _k, 1.0, 10.0, 'N/m', const Color(0xFF38BDF8),
            (x) => setState(() => _k = x)),
        _slider('Damping b', _b, 0.0, 3.0, 'kg/s', const Color(0xFFDC2626), (x) => setState(() => _b = x)),
        if (_forced)
          _slider('Driving frequency ω', _omegaDrive, 0.2, 6.0, 'rad/s', const Color(0xFFF97316),
              (x) => setState(() => _omegaDrive = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(
            _forced
                ? 'Try it: slide the driving frequency ω toward the natural frequency ω₀ — the steady-state amplitude spikes sharply near resonance. Increase damping b and see that peak flatten out and broaden — damping is what keeps real resonance from blowing up to infinity.'
                : 'Try it: raise the damping b and watch the oscillation die out faster — the dashed envelope ±Ae^(-bt/2m) hugs the decaying wave tighter. Push b high enough and the mass barely oscillates before settling — that is the overdamped/critically-damped regime.',
            style: Type.caption.copyWith(color: Palette.primaryDeep),
          ),
        ),
      ],
    );
  }

  Widget _modeButton(String label, bool selected, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: AnimatedContainer(
        duration: Motion.base,
        curve: Motion.ease,
        padding: const EdgeInsets.symmetric(vertical: Gap.x3),
        decoration: BoxDecoration(
          color: selected ? Palette.primary : Palette.surfaceAlt,
          borderRadius: BorderRadius.circular(Corner.md),
          border: Border.all(color: selected ? Palette.primary : Palette.border),
        ),
        alignment: Alignment.center,
        child: Text(label,
            style: Type.bodyStrong.copyWith(color: selected ? Colors.white : Palette.textBody, fontSize: 13)),
      ),
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

  Widget _slider(String label, double value, double min, double max, String unit, Color color,
      ValueChanged<double> onChanged) {
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

class _OscillatorPainter extends CustomPainter {
  final double t;
  final double Function(double) displacementFn;
  final bool forced;
  final double omega0, omegaDrive;
  final double Function(double) amplitudeFn;
  final double decayRate;

  _OscillatorPainter({
    required this.t,
    required this.displacementFn,
    required this.forced,
    required this.omega0,
    required this.omegaDrive,
    required this.amplitudeFn,
    required this.decayRate,
  });

  @override
  void paint(Canvas canvas, Size size) {
    if (!forced) {
      _paintWaveform(canvas, size);
    } else {
      _paintResonanceCurve(canvas, size);
    }
  }

  void _paintWaveform(Canvas canvas, Size size) {
    final midY = size.height / 2;
    final ampPx = size.height * 0.32;
    final wavePath = Path();
    final envTopPath = Path();
    final envBotPath = Path();
    const window = 12.0; // seconds visible

    for (double px = 0; px <= size.width; px += 2) {
      final tt = t - window + (px / size.width) * window;
      final tClamped = tt < 0 ? 0.0 : tt;
      final x = displacementFn(tClamped);
      final y = midY - x * ampPx;
      final envelope = math.exp(-decayRate * tClamped);
      final yTop = midY - envelope * ampPx;
      final yBot = midY + envelope * ampPx;
      if (px == 0) {
        wavePath.moveTo(px, y);
        envTopPath.moveTo(px, yTop);
        envBotPath.moveTo(px, yBot);
      } else {
        wavePath.lineTo(px, y);
        envTopPath.lineTo(px, yTop);
        envBotPath.lineTo(px, yBot);
      }
    }

    // Dashed decay envelope ±Ae^(-bt/2m), drawn behind the oscillation itself.
    canvas.drawPath(envTopPath, Paint()
      ..color = const Color(0x99F59E0B)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.4);
    canvas.drawPath(envBotPath, Paint()
      ..color = const Color(0x99F59E0B)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.4);

    canvas.drawPath(wavePath, Paint()
      ..color = const Color(0xFF38BDF8)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.4);

    // Baseline.
    canvas.drawLine(Offset(0, midY), Offset(size.width, midY), Paint()..color = const Color(0x33FFFFFF)..strokeWidth = 1);

    // Mass marker at the current instant (right edge = "now").
    final xNow = displacementFn(t);
    canvas.drawCircle(Offset(size.width - 14, midY - xNow * ampPx), 9, Paint()..color = Palette.accent);

    _label(canvas, 'Displacement vs time (envelope ±Ae^(-bt/2m) in amber)', Offset(size.width / 2, 16),
        Colors.white70, 10.5);
  }

  void _paintResonanceCurve(Canvas canvas, Size size) {
    final padding = 30.0;
    final maxOmega = 6.0;
    final maxAmp = <double>[];
    for (double w = 0.05; w <= maxOmega; w += 0.05) {
      maxAmp.add(amplitudeFn(w));
    }
    final ampCeiling = (maxAmp.reduce(math.max)).clamp(1.0, 20.0);

    // Axes.
    canvas.drawLine(Offset(padding, size.height - padding), Offset(size.width - 10, size.height - padding),
        Paint()..color = const Color(0x55FFFFFF)..strokeWidth = 1.4);
    canvas.drawLine(Offset(padding, size.height - padding), Offset(padding, 14),
        Paint()..color = const Color(0x55FFFFFF)..strokeWidth = 1.4);

    // Resonance curve.
    final path = Path();
    for (double w = 0.05; w <= maxOmega; w += 0.05) {
      final amp = amplitudeFn(w).clamp(0.0, ampCeiling);
      final px = padding + (w / maxOmega) * (size.width - padding - 10);
      final py = (size.height - padding) - (amp / ampCeiling) * (size.height - padding - 20);
      if (w <= 0.05) {
        path.moveTo(px, py);
      } else {
        path.lineTo(px, py);
      }
    }
    canvas.drawPath(path, Paint()..color = const Color(0xFFF97316)..style = PaintingStyle.stroke..strokeWidth = 2.4);

    // Natural frequency marker line.
    final wxNat = padding + (omega0 / maxOmega) * (size.width - padding - 10);
    canvas.drawLine(Offset(wxNat, 14), Offset(wxNat, size.height - padding),
        Paint()..color = const Color(0x6638BDF8)..strokeWidth = 1.4);
    _label(canvas, 'ω₀', Offset(wxNat, 8), const Color(0xFF38BDF8), 10.5);

    // Current driving-frequency marker + amplitude dot.
    final wxDrive = padding + (omegaDrive / maxOmega) * (size.width - padding - 10);
    final ampNow = amplitudeFn(omegaDrive).clamp(0.0, ampCeiling);
    final pyNow = (size.height - padding) - (ampNow / ampCeiling) * (size.height - padding - 20);
    canvas.drawCircle(Offset(wxDrive, pyNow), 6, Paint()..color = Palette.accent);
    canvas.drawLine(Offset(wxDrive, size.height - padding), Offset(wxDrive, pyNow),
        Paint()..color = const Color(0x66F59E0B)..strokeWidth = 1.2);

    _label(canvas, 'Amplitude vs driving frequency ω', Offset(size.width / 2, 16), Colors.white70, 10.5);
    _label(canvas, 'ω →', Offset(size.width - 24, size.height - padding + 14), Colors.white54, 10);
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
  bool shouldRepaint(_OscillatorPainter old) =>
      old.t != t || old.forced != forced || old.omega0 != omega0 || old.omegaDrive != omegaDrive;
}
