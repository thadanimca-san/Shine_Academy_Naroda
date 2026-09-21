import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Photoelectric Effect Sandbox — light of adjustable frequency and intensity
/// strikes a metal surface. Students discover that electrons are ejected
/// ONLY above a threshold frequency ν0 (work function φ = hν0), that raising
/// intensity below threshold ejects nothing, and that above threshold,
/// intensity controls electron COUNT while frequency alone controls their
/// max kinetic energy (via Einstein's equation KE_max = hν − φ).
class PhotoelectricEffectSandbox extends StatefulWidget {
  const PhotoelectricEffectSandbox({super.key});

  @override
  State<PhotoelectricEffectSandbox> createState() => _PhotoelectricEffectSandboxState();
}

class _PhotoelectricEffectSandboxState extends State<PhotoelectricEffectSandbox>
    with SingleTickerProviderStateMixin {
  // Frequency in units of 10^14 Hz (1.0 .. 12.0 spans below/above typical thresholds)
  double _freq = 5.0;
  // Intensity 0..1 (controls photon rate / brightness)
  double _intensity = 0.5;
  // Work function in eV (typical metals: 2.0 - 5.0 eV)
  double _workFn = 3.0;

  late final Ticker _ticker;
  Duration _last = Duration.zero;
  double _phase = 0;
  final List<_Electron> _electrons = [];
  final math.Random _rng = math.Random(11);
  double _spawnAccum = 0;

  // Planck's constant in eV·s equivalent for our unit system:
  // h·ν(Hz) in eV, with ν = _freq × 10^14 Hz, h = 4.136×10⁻¹⁵ eV·s
  // hν(eV) = 4.136e-15 * freq*1e14 = 0.4136 * freq
  double get _photonEnergyEv => 0.4136 * _freq;
  double get _thresholdFreq => _workFn / 0.4136; // ν0 such that hν0 = φ
  bool get _aboveThreshold => _photonEnergyEv > _workFn;
  double get _maxKeEv => _aboveThreshold ? (_photonEnergyEv - _workFn) : 0.0;
  double get _stoppingPotentialV => _maxKeEv; // eV0 = KE_max, numerically eV=eV so V0 = KE_max(eV)

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
      _phase = (_phase + dt * (1.5 + _freq * 0.3)) % 1000;

      // Spawn ejected electrons only if above threshold; rate ∝ intensity.
      if (_aboveThreshold) {
        _spawnAccum += dt * (0.8 + _intensity * 5.5);
        while (_spawnAccum >= 1) {
          _spawnAccum -= 1;
          _electrons.add(_Electron(
            y: 30 + _rng.nextDouble() * 140,
            speed: 60 + _maxKeEv * 55,
            born: _phase,
          ));
        }
      }
      _electrons.removeWhere((e) => e.x(_phase) > 400);
    });
  }

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
            painter: _PhotoelectricPainter(
              freq: _freq,
              intensity: _intensity,
              phase: _phase,
              aboveThreshold: _aboveThreshold,
              electrons: _electrons,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('Photon energy  hν', _photonEnergyEv.toStringAsFixed(2), 'eV',
                  _aboveThreshold ? Palette.accent : Palette.textFaint)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Max KE  hν − φ', _maxKeEv.toStringAsFixed(2), 'eV',
                  _aboveThreshold ? const Color(0xFF16A34A) : Palette.textFaint)),
        ]),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('Stopping potential  V₀', _stoppingPotentialV.toStringAsFixed(2), 'V',
                  const Color(0xFF38BDF8))),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Threshold  ν₀', _thresholdFreq.toStringAsFixed(2), '×10¹⁴ Hz',
                  Palette.primary)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Frequency ν', _freq, 1, 12, '×10¹⁴ Hz', const Color(0xFF7C3AED),
            (x) => setState(() => _freq = x)),
        _slider('Intensity', _intensity, 0, 1, '', const Color(0xFFF59E0B),
            (x) => setState(() => _intensity = x)),
        _slider('Work function φ', _workFn, 1.5, 5, 'eV', const Color(0xFFEF4444),
            (x) => setState(() => _workFn = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(
            _aboveThreshold
                ? 'Above threshold: raising INTENSITY spawns more electrons per second (more current) but does NOT change their max KE — only frequency does that.'
                : 'Below threshold ν₀: no electrons are ejected no matter how high you push intensity. This is the result classical wave theory could not explain.',
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

class _Electron {
  final double y;
  final double speed; // px/sec
  final double born; // phase time of birth
  _Electron({required this.y, required this.speed, required this.born});
  double x(double phase) => (phase - born) * speed;
}

class _PhotoelectricPainter extends CustomPainter {
  final double freq, intensity, phase;
  final bool aboveThreshold;
  final List<_Electron> electrons;

  _PhotoelectricPainter({
    required this.freq,
    required this.intensity,
    required this.phase,
    required this.aboveThreshold,
    required this.electrons,
  });

  Color _lightColor() {
    // Rough visible-spectrum mapping: low freq -> red, high -> violet.
    final t = ((freq - 1) / 11).clamp(0.0, 1.0);
    return Color.lerp(const Color(0xFFEF4444), const Color(0xFF7C3AED), t)!;
  }

  @override
  void paint(Canvas canvas, Size size) {
    final metalX = size.width * 0.62;

    // Metal plate.
    canvas.drawRect(
      Rect.fromLTRB(metalX, 10, metalX + 14, size.height - 10),
      Paint()..color = const Color(0xFF6B7280),
    );
    canvas.drawRect(
      Rect.fromLTRB(metalX, 10, metalX + 14, size.height - 10),
      Paint()
        ..color = Colors.white24
        ..style = PaintingStyle.stroke
        ..strokeWidth = 1,
    );
    _label(canvas, 'METAL SURFACE', Offset(metalX + 40, size.height - 4),
        Colors.white54, 9);

    final color = _lightColor();
    final nPhotons = (2 + intensity * 8).round();
    final spacing = (size.height - 30) / nPhotons;
    for (var i = 0; i < nPhotons; i++) {
      final y = 20 + spacing * i + (spacing / 2);
      final travel = (phase * (80 + freq * 20)) % (metalX + 40);
      final x = travel;
      if (x > metalX - 6) continue; // absorbed into metal
      // photon as a little wavy dash
      final p = Paint()..color = color.withValues(alpha: 0.85)..strokeWidth = 2.2;
      final segLen = 10.0;
      canvas.drawLine(Offset(x, y), Offset(x + segLen, y), p);
      canvas.drawCircle(Offset(x + segLen, y), 2.2, Paint()..color = color);
    }
    _label(canvas, 'incident light (ν = ${freq.toStringAsFixed(1)}×10¹⁴ Hz)',
        Offset(size.width * 0.30, 12), color, 9);

    // Ejected electrons.
    for (final e in electrons) {
      final x = metalX + 14 + e.x(phase) * 0.14;
      if (x > size.width - 6) continue;
      canvas.drawCircle(Offset(x, e.y), 4.5, Paint()..color = const Color(0xFF38BDF8));
      canvas.drawCircle(
          Offset(x, e.y), 4.5,
          Paint()
            ..color = Colors.white
            ..style = PaintingStyle.stroke
            ..strokeWidth = 0.8);
    }

    if (!aboveThreshold) {
      _label(canvas, 'ν < ν₀ — no electrons ejected, regardless of intensity',
          Offset(size.width * 0.5, size.height / 2 + 2), const Color(0xFFFCA5A5), 10.5);
    }
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
    )..layout(maxWidth: 260);
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_PhotoelectricPainter old) =>
      old.freq != freq ||
      old.intensity != intensity ||
      old.phase != phase ||
      old.aboveThreshold != aboveThreshold;
}
