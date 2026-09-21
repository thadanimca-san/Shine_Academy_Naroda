import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import '../widgets/fx/lottie_fx.dart';
import '../widgets/fx/lottie_sprite.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Coulomb's Law Sandbox — two point charges on a line.
///
/// Students set each charge's sign and magnitude, and slide them closer or
/// farther apart. The force vectors on each charge update live, and a 1/r²
/// curve shows how brutally the force collapses with distance. The key
/// relationship — F ∝ q₁q₂/r² — becomes discoverable by dragging r.
class CoulombsLawSandbox extends StatefulWidget {
  const CoulombsLawSandbox({super.key});

  @override
  State<CoulombsLawSandbox> createState() => _CoulombsLawSandboxState();
}

class _CoulombsLawSandboxState extends State<CoulombsLawSandbox> {
  // Charges in microcoulombs (µC); separation in metres.
  double _q1 = 2.0;
  double _q2 = -3.0;
  double _r = 0.30; // m

  static const double _k = 9e9; // N·m²/C²

  // Force magnitude in newtons: k·|q1·q2|/r²  (charges given in µC → ×1e-6)
  double get _force =>
      _k * (_q1.abs() * 1e-6) * (_q2.abs() * 1e-6) / (_r * _r);

  bool get _attract => _q1 * _q2 < 0;

  @override
  Widget build(BuildContext context) {
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        // ── Stage ──
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
          child: Builder(builder: (context) {
            // Mirror the painter's world transform for sprite anchors.
            final frac = ((_r - 0.08) / (0.60 - 0.08)).clamp(0.0, 1.0);
            final sepFrac = 0.14 + frac * 0.48;
            double spriteSize(double q) => (12.0 + q.abs() * 2.6) * 4.8;
            return SpriteStage(
              stage: CustomPaint(
                painter: _CoulombPainter(
                  q1: _q1, q2: _q2, r: _r, force: _force, attract: _attract,
                ),
                child: const SizedBox.expand(),
              ),
              actors: [
                SpriteActor(
                  anchor: Offset(0.5 - sepFrac / 2, 0.5),
                  sprite: LottieSprite(
                    _q1 >= 0 ? LottieFx.proton : LottieFx.electron,
                    size: spriteSize(_q1),
                  ),
                ),
                SpriteActor(
                  anchor: Offset(0.5 + sepFrac / 2, 0.5),
                  sprite: LottieSprite(
                    _q2 >= 0 ? LottieFx.proton : LottieFx.electron,
                    size: spriteSize(_q2),
                  ),
                ),
              ],
            );
          }),
        ),
        const SizedBox(height: Gap.x3),

        // ── Readout ──
        Row(
          children: [
            Expanded(
              child: _card(
                'FORCE ON EACH CHARGE',
                _fmtForce(_force),
                _attract ? 'Attractive (pulling together)' : 'Repulsive (pushing apart)',
                _attract ? Palette.info : Palette.danger,
              ),
            ),
            const SizedBox(width: Gap.x3),
            Expanded(
              child: _card(
                'IF r IS HALVED',
                '× 4',
                'Force quadruples: F ∝ 1/r²',
                Palette.accent,
              ),
            ),
          ],
        ),
        const SizedBox(height: Gap.x3),

        // ── Controls ──
        Row(children: [
          Expanded(child: _slider('q₁', _q1, -5, 5, 'µC', const Color(0xFFF97316),
              (v) => setState(() => _q1 = v))),
          const SizedBox(width: Gap.x3),
          Expanded(child: _slider('q₂', _q2, -5, 5, 'µC', const Color(0xFF38BDF8),
              (v) => setState(() => _q2 = v))),
        ]),
        _slider('Separation r', _r, 0.08, 0.60, 'm', Palette.primary,
            (v) => setState(() => _r = v)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.primarySoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('F = k·|q₁q₂| / r²  with k = 9×10⁹.  ''Drag r toward 0.08 m and watch the force explode — that is the 1/r² law biting.'),
            style: Type.caption.copyWith(color: Palette.primaryDeep),
          ),
        ),
      ],
    );
  }

  String _fmtForce(double f) {
    if (f >= 1) return '${f.toStringAsFixed(2)} N';
    return '${(f * 1000).toStringAsFixed(1)} mN';
  }

  Widget _card(String label, String value, String sub, Color color) {
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
          Text(label, style: Type.label.copyWith(fontSize: 9)),
          const SizedBox(height: 4),
          Text(value,
              style: Type.bodyStrong.copyWith(
                  fontSize: 17, fontFamily: 'monospace', color: color)),
          const SizedBox(height: 4),
          Text(sub, style: Type.caption.copyWith(fontSize: 10.5)),
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

class _CoulombPainter extends CustomPainter {
  final double q1, q2, r, force;
  final bool attract;

  _CoulombPainter({
    required this.q1,
    required this.q2,
    required this.r,
    required this.force,
    required this.attract,
  });

  static const _cPos = Color(0xFFF97316);
  static const _cNeg = Color(0xFF38BDF8);

  @override
  void paint(Canvas canvas, Size size) {
    final cy = size.height * 0.5;
    // Map separation 0.08..0.60 m onto a fraction of the width.
    final maxSep = size.width * 0.62;
    final minSep = size.width * 0.14;
    final frac = ((r - 0.08) / (0.60 - 0.08)).clamp(0.0, 1.0);
    final sep = minSep + frac * (maxSep - minSep);
    final cx = size.width / 2;
    final x1 = cx - sep / 2;
    final x2 = cx + sep / 2;

    // separation line
    canvas.drawLine(Offset(x1, cy), Offset(x2, cy),
        Paint()..color = Palette.stageLine..strokeWidth = 1.5);
    _label(canvas, 'r = ${r.toStringAsFixed(2)} m',
        Offset(cx, cy + 26), Colors.white54, 11);

    // Force arrows — attractive: point inward; repulsive: outward.
    final arrowLen = (math.log(force * 1000 + 1) * 9).clamp(10.0, 68.0);
    final dir = attract ? 1.0 : -1.0; // +1 means charge1 arrow points right (inward)
    _forceArrow(canvas, Offset(x1, cy - 40), arrowLen * dir);
    _forceArrow(canvas, Offset(x2, cy - 40), -arrowLen * dir);

    _charge(canvas, Offset(x1, cy), q1);
    _charge(canvas, Offset(x2, cy), q2);

    _label(canvas, attract ? 'ATTRACT' : 'REPEL',
        Offset(cx, cy - 62), attract ? _cNeg : _cPos, 12);
  }

  void _forceArrow(Canvas canvas, Offset from, double len) {
    if (len.abs() < 4) return;
    final p = Paint()
      ..color = Colors.white70
      ..strokeWidth = 2.5
      ..strokeCap = StrokeCap.round;
    final to = from + Offset(len, 0);
    canvas.drawLine(from, to, p);
    final s = len.sign;
    canvas.drawLine(to, to + Offset(-8 * s, -4), p);
    canvas.drawLine(to, to + Offset(-8 * s, 4), p);
  }

  // The charge bodies themselves are Lottie sprites overlaid by SpriteStage;
  // the painter only labels their magnitude.
  void _charge(Canvas canvas, Offset c, double q) {
    final color = q >= 0 ? _cPos : _cNeg;
    _label(canvas, '${q.toStringAsFixed(1)} µC', c + const Offset(0, 40), color, 10.5);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fontSize) {
    final tp = TextPainter(
      text: TextSpan(
        text: text,
        style: TextStyle(
            color: color,
            fontSize: fontSize,
            fontWeight: FontWeight.w700,
            fontFamily: 'monospace'),
      ),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_CoulombPainter old) =>
      old.q1 != q1 || old.q2 != q2 || old.r != r || old.force != force;
}
