import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'package:flutter/scheduler.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Bohr Model Sandbox — a hydrogen atom with quantised circular orbits.
/// Students pick an initial and final level (n1, n2), see the electron
/// "jump" between allowed orbits, and watch a photon of energy
/// ΔE = 13.6(1/n1² − 1/n2²) eV get emitted or absorbed accordingly.
class BohrModelSandbox extends StatefulWidget {
  const BohrModelSandbox({super.key});

  @override
  State<BohrModelSandbox> createState() => _BohrModelSandboxState();
}

class _BohrModelSandboxState extends State<BohrModelSandbox>
    with SingleTickerProviderStateMixin {
  int _nHigh = 3; // upper level involved in the transition
  int _nLow = 1; // lower level involved in the transition
  bool _emitting = true; // true = emission (nHigh -> nLow), false = absorption

  late final Ticker _ticker;
  Duration _last = Duration.zero;
  double _phase = 0; // orbital phase for animating electron motion
  double _jumpT = -1; // -1 = not jumping; 0..1 progress of a jump animation
  double _photonT = -1; // -1 = no photon; 0..1 progress of photon flight

  static const double _rydbergEv = 13.6;

  double get _energy1 => -_rydbergEv / (_nLow * _nLow);
  double get _energy2 => -_rydbergEv / (_nHigh * _nHigh);
  double get _deltaE => (_energy2 - _energy1).abs(); // eV, magnitude
  // λ(nm) = 1240 / E(eV)
  double get _wavelengthNm => 1240 / _deltaE;

  String get _seriesName {
    final nFinal = _nLow;
    switch (nFinal) {
      case 1:
        return 'Lyman (UV)';
      case 2:
        return 'Balmer (visible)';
      case 3:
        return 'Paschen (IR)';
      default:
        return 'n=$nFinal series (IR)';
    }
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
    setState(() {
      _phase = (_phase + dt * 0.6) % (2 * math.pi);
      if (_jumpT >= 0) {
        _jumpT += dt * 0.9;
        if (_jumpT > 1) {
          _jumpT = -1;
          _photonT = 0; // start photon flight after the jump completes
        }
      } else if (_photonT >= 0) {
        _photonT += dt * 0.7;
        if (_photonT > 1) _photonT = -1;
      }
    });
  }

  void _triggerTransition() {
    setState(() {
      _jumpT = 0;
      _photonT = -1;
    });
  }

  @override
  Widget build(BuildContext context) {
    final levels = [1, 2, 3, 4, 5];
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
            painter: _BohrPainter(
              nLow: _nLow,
              nHigh: _nHigh,
              phase: _phase,
              jumpT: _jumpT,
              photonT: _photonT,
              emitting: _emitting,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
              child: _meter('Transition energy  ΔE', _deltaE.toStringAsFixed(2), 'eV',
                  Palette.accent)),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Photon wavelength  λ', _wavelengthNm.toStringAsFixed(0), 'nm',
                  const Color(0xFF38BDF8))),
        ]),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: Gap.x3, vertical: Gap.x2),
          decoration: BoxDecoration(
            color: Palette.surface,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text('Series: $_seriesName', style: Type.bodyStrong.copyWith(fontSize: 13)),
              Text(_emitting ? 'EMISSION' : 'ABSORPTION',
                  style: Type.label.copyWith(
                      color: _emitting ? const Color(0xFF16A34A) : const Color(0xFFEA580C))),
            ],
          ),
        ),
        const SizedBox(height: Gap.x3),
        Text(TrilingualService.instance.getUIText('Upper level n₂'), style: Type.caption.copyWith(fontWeight: FontWeight.w600)),
        Wrap(
          spacing: Gap.x2,
          children: levels
              .where((n) => n > _nLow)
              .map((n) => ChoiceChip(
                    label: Text('n=$n'),
                    selected: _nHigh == n,
                    onSelected: (_) => setState(() => _nHigh = n),
                  ))
              .toList(),
        ),
        const SizedBox(height: Gap.x3),
        Text(TrilingualService.instance.getUIText('Lower level n₁'), style: Type.caption.copyWith(fontWeight: FontWeight.w600)),
        Wrap(
          spacing: Gap.x2,
          children: levels
              .where((n) => n < _nHigh)
              .map((n) => ChoiceChip(
                    label: Text('n=$n'),
                    selected: _nLow == n,
                    onSelected: (_) => setState(() => _nLow = n),
                  ))
              .toList(),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
            child: OutlinedButton(
              onPressed: () => setState(() => _emitting = true),
              child: Text(TrilingualService.instance.getUIText('Emission (n₂→n₁)')),
            ),
          ),
          const SizedBox(width: Gap.x2),
          Expanded(
            child: OutlinedButton(
              onPressed: () => setState(() => _emitting = false),
              child: Text(TrilingualService.instance.getUIText('Absorption (n₁→n₂)')),
            ),
          ),
        ]),
        const SizedBox(height: Gap.x2),
        SizedBox(
          width: double.infinity,
          child: FilledButton(
            onPressed: _triggerTransition,
            style: FilledButton.styleFrom(backgroundColor: Palette.chModern),
            child: Text(TrilingualService.instance.getUIText('Trigger transition')),
          ),
        ),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: pick n₂=3, n₁=1 (Lyman, UV) then n₂=3, n₁=2 (Balmer, visible) — same upper level, very different photon energy and colour, because ΔE depends on BOTH levels.'),
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
}

class _BohrPainter extends CustomPainter {
  final int nLow, nHigh;
  final double phase, jumpT, photonT;
  final bool emitting;

  _BohrPainter({
    required this.nLow,
    required this.nHigh,
    required this.phase,
    required this.jumpT,
    required this.photonT,
    required this.emitting,
  });

  double _radiusFor(int n, double maxR) => maxR * (n * n) / 25.0; // r ∝ n², n up to 5

  @override
  void paint(Canvas canvas, Size size) {
    final c = Offset(size.width / 2, size.height / 2 + 6);
    final maxR = math.min(size.width, size.height) / 2 - 10;

    // Nucleus.
    canvas.drawCircle(c, 7, Paint()..color = const Color(0xFFF97316));
    _label(canvas, 'p⁺', c, Colors.white, 8);

    // Draw allowed orbits n = 1..5.
    for (var n = 1; n <= 5; n++) {
      final r = _radiusFor(n, maxR);
      final isActive = n == nLow || n == nHigh;
      canvas.drawCircle(
        c,
        r,
        Paint()
          ..color = isActive ? const Color(0x99BE185D) : const Color(0x22FFFFFF)
          ..style = PaintingStyle.stroke
          ..strokeWidth = isActive ? 1.6 : 1,
      );
      _label(canvas, 'n=$n', c + Offset(r * math.cos(-math.pi / 2.4), r * math.sin(-math.pi / 2.4)),
          isActive ? const Color(0xFFF472B6) : Colors.white38, 9);
    }

    final rLow = _radiusFor(nLow, maxR);
    final rHigh = _radiusFor(nHigh, maxR);

    // Electron position: animate the jump between orbits, else orbit steadily
    // on whichever level corresponds to the "before" state.
    Offset electronPos;
    if (jumpT >= 0) {
      // Jumping: interpolate radius smoothly between the two orbits.
      final fromR = emitting ? rHigh : rLow;
      final toR = emitting ? rLow : rHigh;
      final r = fromR + (toR - fromR) * Curves.easeInOut.transform(jumpT);
      electronPos = c + Offset(r * math.cos(phase * 3), r * math.sin(phase * 3));
    } else {
      final restR = emitting ? (photonT >= 0 ? rLow : rHigh) : (photonT >= 0 ? rHigh : rLow);
      electronPos = c + Offset(restR * math.cos(phase * 3), restR * math.sin(phase * 3));
    }

    canvas.drawCircle(electronPos, 5, Paint()..color = const Color(0xFF38BDF8));
    canvas.drawCircle(
        electronPos,
        5,
        Paint()
          ..color = Colors.white
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1);

    // Photon: shown flying outward (emission) or inward (absorption).
    if (photonT >= 0) {
      final dir = emitting ? 1.0 : -1.0;
      final startR = emitting ? rLow : maxR + 20;
      final endR = emitting ? maxR + 20 : rHigh;
      final r = startR + (endR - startR) * photonT;
      final ang = math.pi / 4;
      final pos = c + Offset(r * math.cos(ang) * dir.sign, r * math.sin(ang));
      final col = const Color(0xFFFDE047);
      canvas.drawCircle(pos, 3.5, Paint()..color = col);
      final tailDir = Offset(math.cos(ang), math.sin(ang)) * dir;
      canvas.drawLine(pos, pos - tailDir * 14, Paint()..color = col.withValues(alpha: 0.7)..strokeWidth = 2);
    }

    _label(
        canvas,
        emitting ? 'photon emitted ↗' : 'photon absorbed ↙',
        Offset(size.width / 2, 14),
        const Color(0xFFFDE047),
        10);
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
  bool shouldRepaint(_BohrPainter old) =>
      old.nLow != nLow ||
      old.nHigh != nHigh ||
      old.phase != phase ||
      old.jumpT != jumpT ||
      old.photonT != photonT ||
      old.emitting != emitting;
}
