import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

enum _Medium { air, water, steel }

/// Sound Waves Sandbox — a longitudinal pressure wave shown two ways: a
/// column of "particles" that bunch into compressions and spread into
/// rarefactions, and the corresponding pressure-vs-position graph. Sliders
/// control frequency, amplitude (loudness), and the propagation medium
/// (which sets wave speed).
class SoundWavesSandbox extends StatefulWidget {
  const SoundWavesSandbox({super.key});

  @override
  State<SoundWavesSandbox> createState() => _SoundWavesSandboxState();
}

class _SoundWavesSandboxState extends State<SoundWavesSandbox>
    with SingleTickerProviderStateMixin {
  double _freq = 4.0; // relative frequency units
  double _amp = 0.6; // 0..1 (loudness / displacement amplitude)
  _Medium _medium = _Medium.air;
  double _t = 0;
  late final Ticker _ticker;
  Duration _last = Duration.zero;

  double get _speed {
    switch (_medium) {
      case _Medium.air:
        return 340;
      case _Medium.water:
        return 1480;
      case _Medium.steel:
        return 5960;
    }
  }

  String get _mediumLabel {
    switch (_medium) {
      case _Medium.air:
        return 'Air (gas)';
      case _Medium.water:
        return 'Water (liquid)';
      case _Medium.steel:
        return 'Steel (solid)';
    }
  }

  // Rough intensity level in dB relative to amplitude, purely illustrative:
  // intensity I ∝ A², dB level shown on an arbitrary 0-90 scale.
  double get _dbLevel => 20 + 70 * _amp * _amp;

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
    setState(() => _t += dt * 0.7);
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
            painter: _SoundPainter(freq: _freq, amp: _amp, t: _t),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Speed in ${_mediumLabel.split(' ')[0]}',
              _speed.toStringAsFixed(0), 'm/s', Palette.chWaves)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Intensity level',
              _dbLevel.toStringAsFixed(0), 'dB (illus.)', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Frequency (pitch)', _freq, 1, 10, 'Hz (rel)', const Color(0xFF38BDF8),
            (x) => setState(() => _freq = x)),
        _slider('Amplitude (loudness)', _amp, 0.1, 1.0, '', const Color(0xFFF97316),
            (x) => setState(() => _amp = x)),
        const SizedBox(height: Gap.x2),
        Text(TrilingualService.instance.getUIText('MEDIUM'), style: Type.label.copyWith(fontSize: 10)),
        const SizedBox(height: 6),
        Row(
          children: _Medium.values.map((m) {
            final selected = m == _medium;
            return Expanded(
              child: GestureDetector(
                onTap: () => setState(() => _medium = m),
                child: Container(
                  margin: const EdgeInsets.symmetric(horizontal: 3),
                  padding: const EdgeInsets.symmetric(vertical: 10),
                  decoration: BoxDecoration(
                    color: selected ? Palette.chWaves : Palette.surface,
                    borderRadius: BorderRadius.circular(Corner.md),
                    border: Border.all(color: selected ? Palette.chWaves : Palette.border),
                  ),
                  alignment: Alignment.center,
                  child: Text(
                    m == _Medium.air ? 'Air' : (m == _Medium.water ? 'Water' : 'Steel'),
                    style: Type.caption.copyWith(
                        fontWeight: FontWeight.w700,
                        color: selected ? Colors.white : Palette.textBody),
                  ),
                ),
              ),
            );
          }).toList(),
        ),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: switch medium from Air to Steel and watch the wave speed jump nearly 18× — solids carry sound fastest because their tightly-bonded particles transmit compressions almost instantly. Raise amplitude and watch the compressions (dark bands) pack denser — that\'s louder, not higher-pitched.'),
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

class _SoundPainter extends CustomPainter {
  final double freq, amp, t;
  _SoundPainter({required this.freq, required this.amp, required this.t});

  @override
  void paint(Canvas canvas, Size size) {
    StageBackdrop.paint(canvas, size, groundY: size.height);

    final particleRowY = size.height * 0.28;
    final graphMidY = size.height * 0.72;
    final graphAmp = size.height * 0.16;

    // Particle column: dots displaced longitudinally to show compression/rarefaction.
    const nParticles = 40;
    final spacing = size.width / nParticles;
    for (int i = 0; i < nParticles; i++) {
      final x0 = i * spacing + spacing / 2;
      final phase = 2 * math.pi * freq * (x0 / size.width) - 2 * math.pi * freq * t;
      final displacement = amp * (spacing * 0.9) * math.sin(phase);
      final x = x0 + displacement;
      // Local density -> darker/closer = compression.
      final density = (math.cos(phase)).abs();
      final color = Color.lerp(const Color(0xFF64748B), const Color(0xFFE2E8F0), density)!;
      canvas.drawCircle(Offset(x, particleRowY), 3.2, Paint()..color = color);
    }
    _label(canvas, 'compressions ↔ rarefactions', Offset(size.width / 2, particleRowY - 22),
        const Color(0xFFA5A9BF), 10);

    // Pressure-vs-position graph.
    canvas.drawLine(Offset(0, graphMidY), Offset(size.width, graphMidY),
        Paint()..color = const Color(0x33FFFFFF)..strokeWidth = 1);
    final path = Path();
    for (double x = 0; x <= size.width; x += 2) {
      final phase = 2 * math.pi * freq * (x / size.width) - 2 * math.pi * freq * t;
      final y = graphMidY - graphAmp * amp * math.sin(phase);
      if (x == 0) {
        path.moveTo(x, y);
      } else {
        path.lineTo(x, y);
      }
    }
    canvas.drawPath(path, Paint()
      ..color = Palette.chWaves
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2.4);
    _label(canvas, 'pressure excess Δp(x)', Offset(size.width / 2, graphMidY - graphAmp - 16),
        Palette.chWaves, 10);
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
  bool shouldRepaint(_SoundPainter old) => old.freq != freq || old.amp != amp || old.t != t;
}
