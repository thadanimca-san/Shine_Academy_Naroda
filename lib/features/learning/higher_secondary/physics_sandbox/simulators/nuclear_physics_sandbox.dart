import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Nuclear Physics Sandbox — adjustable mass number A and atomic number Z,
/// showing binding energy per nucleon on a simplified illustrative curve,
/// explaining why both fission (heavy → medium) and fusion (light → medium)
/// release energy as nuclei move toward the peak near A ≈ 56 (iron).
class NuclearPhysicsSandbox extends StatefulWidget {
  const NuclearPhysicsSandbox({super.key});

  @override
  State<NuclearPhysicsSandbox> createState() => _NuclearPhysicsSandboxState();
}

class _NuclearPhysicsSandboxState extends State<NuclearPhysicsSandbox>
    with SingleTickerProviderStateMixin {
  double _a = 56; // mass number
  double _z = 26; // atomic number (proton count)

  late final Ticker _ticker;
  Duration _last = Duration.zero;
  double _phase = 0;

  // Simplified illustrative binding-energy-per-nucleon curve (MeV),
  // shaped like the real curve: rises steeply, peaks near A≈56, decays slowly.
  double _beCurve(double a) {
    if (a < 1) return 0;
    final rise = 8.7 * (1 - math.exp(-a / 12));
    final fall = 0.9 * math.pow(math.max(a - 56, 0) / 140, 1.0);
    return math.max(rise - fall, 0.5);
  }

  double get _bePerNucleon => _beCurve(_a);

  // Simplified mass-defect-style estimate consistent with the curve above:
  // total binding energy = BE/nucleon * A; mass defect Δm(u) = BE(MeV)/931.5
  double get _totalBeMev => _bePerNucleon * _a;
  double get _massDefectU => _totalBeMev / 931.5;

  bool get _isFissionCandidate => _a > 140;
  bool get _isFusionCandidate => _a < 20;

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
    setState(() => _phase = (_phase + dt) % 1000);
  }

  @override
  Widget build(BuildContext context) {
    final n = (_a - _z).clamp(0, 500);
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
            painter: _NucleusPainter(
              a: _a,
              z: _z,
              phase: _phase,
              curve: _beCurve,
              bePerNucleon: _bePerNucleon,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('BE per nucleon', _bePerNucleon.toStringAsFixed(2), 'MeV',
                  Palette.accent)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Total binding energy', _totalBeMev.toStringAsFixed(1), 'MeV',
                  const Color(0xFF38BDF8))),
        ]),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Neutrons N = A − Z', n.toStringAsFixed(0), '', Palette.primary)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Mass defect Δm', _massDefectU.toStringAsFixed(3), 'u',
                  const Color(0xFF16A34A))),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Mass number A', _a, 4, 240, '', const Color(0xFF7C3AED),
            (x) => setState(() {
                  _a = x;
                  if (_z > _a) _z = _a;
                })),
        _slider('Atomic number Z', _z, 1, _a.clamp(1, 240), '', const Color(0xFFF59E0B),
            (x) => setState(() => _z = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(
            _isFissionCandidate
                ? 'This heavy nucleus (A > 140) sits LEFT of the peak. Splitting it (fission) into two medium nuclei moves both fragments toward the peak — releasing energy.'
                : _isFusionCandidate
                    ? 'This light nucleus (A < 20) sits well left of the peak too, but on the OTHER side. Fusing it with another light nucleus moves the product toward the peak — releasing energy.'
                    : 'This nucleus sits near the peak (around iron, A≈56) — the most tightly bound region. Nuclei here are stable and release energy neither easily fissioning nor fusing.',
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

class _NucleusPainter extends CustomPainter {
  final double a, z, phase, bePerNucleon;
  final double Function(double) curve;

  _NucleusPainter({
    required this.a,
    required this.z,
    required this.phase,
    required this.curve,
    required this.bePerNucleon,
  });

  @override
  void paint(Canvas canvas, Size size) {
    // Left: nucleus visualization (small cluster of dots).
    final nucleusCenter = Offset(size.width * 0.20, size.height * 0.42);
    final rng = math.Random(7);
    final dotCount = math.min(30, (a / 4).round().clamp(4, 30));
    for (var i = 0; i < dotCount; i++) {
      final ang = rng.nextDouble() * 2 * math.pi + phase * 0.1;
      final rad = rng.nextDouble() * 22;
      final isProton = i < (dotCount * (z / a)).round();
      final pos = nucleusCenter + Offset(rad * math.cos(ang), rad * math.sin(ang));
      canvas.drawCircle(pos, 4,
          Paint()..color = isProton ? const Color(0xFFF97316) : const Color(0xFF38BDF8));
    }
    _label(canvas, 'A=${a.toStringAsFixed(0)}, Z=${z.toStringAsFixed(0)}',
        nucleusCenter + const Offset(0, 46), Colors.white70, 10);
    _label(canvas, '● proton  ● neutron', nucleusCenter + const Offset(0, 60), Colors.white38, 8);

    // Right: BE/nucleon vs A curve.
    final plotLeft = size.width * 0.42;
    final plotRight = size.width - 16;
    final plotTop = 18.0;
    final plotBottom = size.height - 28;
    final maxA = 240.0;
    final maxBe = 9.5;

    canvas.drawLine(Offset(plotLeft, plotBottom), Offset(plotRight, plotBottom),
        Paint()..color = Colors.white30..strokeWidth = 1);
    canvas.drawLine(Offset(plotLeft, plotTop), Offset(plotLeft, plotBottom),
        Paint()..color = Colors.white30..strokeWidth = 1);
    _label(canvas, 'A →', Offset(plotRight - 8, plotBottom + 12), Colors.white54, 9);
    _label(canvas, 'BE/A', Offset(plotLeft - 4, plotTop - 8), Colors.white54, 9);

    final path = Path();
    for (var x = 1.0; x <= maxA; x += 2) {
      final px = plotLeft + (x / maxA) * (plotRight - plotLeft);
      final beVal = curve(x);
      final py = plotBottom - (beVal / maxBe) * (plotBottom - plotTop);
      if (x == 1.0) {
        path.moveTo(px, py);
      } else {
        path.lineTo(px, py);
      }
    }
    canvas.drawPath(path, Paint()
      ..color = const Color(0xFF16A34A)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2);

    // Peak marker near iron.
    final peakX = plotLeft + (56 / maxA) * (plotRight - plotLeft);
    canvas.drawLine(Offset(peakX, plotTop), Offset(peakX, plotBottom),
        Paint()..color = Colors.white24..strokeWidth = 1);
    _label(canvas, 'Fe peak', Offset(peakX, plotTop - 2), Colors.white54, 8);

    // Current nucleus marker.
    final curX = plotLeft + (a / maxA) * (plotRight - plotLeft);
    final curY = plotBottom - (bePerNucleon / maxBe) * (plotBottom - plotTop);
    canvas.drawCircle(Offset(curX, curY), 5, Paint()..color = Palette.accent);
    canvas.drawCircle(
        Offset(curX, curY),
        5,
        Paint()
          ..color = Colors.white
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
    )..layout(maxWidth: 140);
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_NucleusPainter old) =>
      old.a != a || old.z != z || old.phase != phase || old.bePerNucleon != bePerNucleon;
}
