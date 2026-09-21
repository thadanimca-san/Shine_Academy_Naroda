import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Radioactivity Sandbox — a sample of N0 radioactive nuclei (dots), each
/// decaying randomly (individually unpredictable) but following the
/// statistical law N(t) = N0 e^(-λt) as a large population. An adjustable
/// half-life slider lets students confirm N drops to N0/2, N0/4, N0/8 at
/// t = T, 2T, 3T.
class RadioactivitySandbox extends StatefulWidget {
  const RadioactivitySandbox({super.key});

  @override
  State<RadioactivitySandbox> createState() => _RadioactivitySandboxState();
}

class _RadioactivitySandboxState extends State<RadioactivitySandbox>
    with SingleTickerProviderStateMixin {
  static const int _n0 = 80;
  double _halfLifeS = 4.0; // seconds, simulated time

  late final Ticker _ticker;
  Duration _last = Duration.zero;
  double _t = 0; // elapsed simulated seconds
  final math.Random _rng = math.Random(3);
  late List<bool> _decayed; // per-nucleus decayed flag
  late List<Offset> _positions;

  double get _lambda => math.log(2) / _halfLifeS;
  int get _decayedCount => _decayed.where((d) => d).length;
  int get _remaining => _n0 - _decayedCount;
  double get _nModel => _n0 * math.exp(-_lambda * _t);
  int get _halfLivesElapsed => (_t / _halfLifeS).floor();

  @override
  void initState() {
    super.initState();
    _positions = List.generate(
        _n0,
        (i) => Offset(
              20 + _rng.nextDouble() * 260,
              20 + _rng.nextDouble() * 140,
            ));
    _decayed = List.filled(_n0, false);
    _ticker = createTicker(_tick)..start();
  }

  @override
  void dispose() {
    _ticker.dispose();
    super.dispose();
  }

  void _tick(Duration elapsed) {
    final dt = math.min((elapsed - _last).inMicroseconds / 1e6, 0.05);
    _last = elapsed;
    setState(() {
      _t += dt;
      // Probabilistic decay: each still-active nucleus has hazard rate λ.
      final pDecayThisStep = 1 - math.exp(-_lambda * dt);
      for (var i = 0; i < _n0; i++) {
        if (!_decayed[i] && _rng.nextDouble() < pDecayThisStep) {
          _decayed[i] = true;
        }
      }
    });
  }

  void _reset() {
    setState(() {
      _t = 0;
      _decayed = List.filled(_n0, false);
    });
  }

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        Container(
          height: 200,
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
            painter: _SamplePainter(positions: _positions, decayed: _decayed),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Container(
          height: 110,
          padding: const EdgeInsets.all(Gap.x2),
          decoration: BoxDecoration(
            color: Palette.surface,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: CustomPaint(
            painter: _DecayGraphPainter(
              t: _t,
              halfLife: _halfLifeS,
              n0: _n0.toDouble(),
              currentN: _remaining.toDouble(),
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Remaining N', '$_remaining', '/ $_n0', Palette.accent)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Model N(t)=N₀e^(−λt)', _nModel.toStringAsFixed(1), '',
                  const Color(0xFF38BDF8))),
        ]),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Elapsed time t', _t.toStringAsFixed(1), 's', Palette.primary)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Half-lives elapsed', '$_halfLivesElapsed', 'T½',
                  const Color(0xFF16A34A))),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Half-life T½', _halfLifeS, 1, 10, 's', const Color(0xFFEF4444),
            (x) => setState(() => _halfLifeS = x)),
        const SizedBox(height: Gap.x2),
        SizedBox(
          width: double.infinity,
          child: OutlinedButton(onPressed: _reset, child: Text(TrilingualService.instance.getUIText('Reset sample'))),
        ),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Watch closely: you cannot predict WHICH dot decays next (random for each nucleus), but the population as a whole reliably halves every T½ seconds — that\'s the statistical law N=N₀e^(−λt) at work.'),
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
        Text('$label = ${value.toStringAsFixed(1)} $unit',
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

class _SamplePainter extends CustomPainter {
  final List<Offset> positions;
  final List<bool> decayed;
  _SamplePainter({required this.positions, required this.decayed});

  @override
  void paint(Canvas canvas, Size size) {
    for (var i = 0; i < positions.length; i++) {
      final color = decayed[i] ? const Color(0x552563EB) : const Color(0xFF16A34A);
      canvas.drawCircle(positions[i], decayed[i] ? 3.5 : 4.5, Paint()..color = color);
    }
    _label(canvas, 'green = undecayed nucleus   faded = decayed', Offset(size.width / 2, 12),
        Colors.white54, 9);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w600, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_SamplePainter old) => true;
}

class _DecayGraphPainter extends CustomPainter {
  final double t, halfLife, n0, currentN;
  _DecayGraphPainter(
      {required this.t, required this.halfLife, required this.n0, required this.currentN});

  @override
  void paint(Canvas canvas, Size size) {
    final left = 28.0, right = size.width - 8, top = 8.0, bottom = size.height - 18;
    final maxT = math.max(halfLife * 4, t + 1);

    canvas.drawLine(Offset(left, bottom), Offset(right, bottom), Paint()..color = Palette.border..strokeWidth = 1);
    canvas.drawLine(Offset(left, top), Offset(left, bottom), Paint()..color = Palette.border..strokeWidth = 1);

    // Model curve N0 e^{-lambda t}
    final lambda = math.log(2) / halfLife;
    final path = Path();
    for (var i = 0; i <= 100; i++) {
      final tt = maxT * i / 100;
      final n = n0 * math.exp(-lambda * tt);
      final px = left + (tt / maxT) * (right - left);
      final py = bottom - (n / n0) * (bottom - top);
      if (i == 0) {
        path.moveTo(px, py);
      } else {
        path.lineTo(px, py);
      }
    }
    canvas.drawPath(path, Paint()..color = const Color(0xFF38BDF8)..style = PaintingStyle.stroke..strokeWidth = 2);

    // Half-life gridlines at T, 2T, 3T with N0/2, N0/4, N0/8 markers.
    for (var k = 1; k <= 3; k++) {
      final tk = halfLife * k;
      if (tk > maxT) continue;
      final px = left + (tk / maxT) * (right - left);
      canvas.drawLine(Offset(px, top), Offset(px, bottom), Paint()..color = Colors.white24..strokeWidth = 1);
      _tinyLabel(canvas, '${k}T', Offset(px, bottom + 9));
    }

    // Current point.
    final curPx = left + (t.clamp(0, maxT) / maxT) * (right - left);
    final curPy = bottom - (currentN / n0) * (bottom - top);
    canvas.drawCircle(Offset(curPx, curPy), 4, Paint()..color = Palette.accent);

    _tinyLabel(canvas, 'N₀', Offset(left - 14, top + 4));
    _tinyLabel(canvas, '0', Offset(left - 8, bottom + 2));
  }

  void _tinyLabel(Canvas canvas, String text, Offset pos) {
    final tp = TextPainter(
      text: TextSpan(text: text, style: TextStyle(color: Colors.white54, fontSize: 8.5, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, pos);
  }

  @override
  bool shouldRepaint(_DecayGraphPainter old) => true;
}
