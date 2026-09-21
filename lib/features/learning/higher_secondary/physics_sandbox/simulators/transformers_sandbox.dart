import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Transformers Sandbox — adjustable primary/secondary turns ratio and input
/// voltage. Shows live-computed output voltage Vs/Vp = Ns/Np and the
/// power-conserving current relationship VpIp = VsIs, with a step-up/step-down toggle.
class TransformersSandbox extends StatefulWidget {
  const TransformersSandbox({super.key});

  @override
  State<TransformersSandbox> createState() => _TransformersSandboxState();
}

class _TransformersSandboxState extends State<TransformersSandbox> {
  double _vp = 100; // primary voltage (V)
  double _turnsRatio = 2.0; // Ns/Np (>1 step-up, <1 step-down)
  double _ip = 4.0; // primary current (A), for illustrating power conservation

  double get _vs => _vp * _turnsRatio;
  double get _isec => _ip / _turnsRatio; // ideal: VpIp = VsIs
  double get _power => _vp * _ip;
  bool get _isStepUp => _turnsRatio >= 1;

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
            painter: _TransformerPainter(turnsRatio: _turnsRatio, stepUp: _isStepUp),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Vₚ (primary)', _vp.toStringAsFixed(0), 'V', const Color(0xFF38BDF8))),
          const SizedBox(width: Gap.x3),
          Expanded(
              child: _meter('Vₛ = Vₚ(Nₛ/Nₚ)', _vs.toStringAsFixed(0), 'V', Palette.chElectroMag)),
        ]),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Iₚ (primary)', _ip.toStringAsFixed(2), 'A', const Color(0xFFF97316))),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Iₛ = Iₚ(Nₚ/Nₛ)', _isec.toStringAsFixed(2), 'A', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        Container(
          padding: const EdgeInsets.symmetric(vertical: Gap.x2, horizontal: Gap.x3),
          decoration: BoxDecoration(
            color: Palette.surface,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Text(
            'Power  Pₚ = VₚIₚ = ${_power.toStringAsFixed(0)} W   ≈   Pₛ = VₛIₛ = ${(_vs * _isec).toStringAsFixed(0)} W  (ideal — power conserved)',
            style: Type.caption.copyWith(fontSize: 11.5, fontFamily: 'monospace'),
          ),
        ),
        const SizedBox(height: Gap.x3),
        _slider('Primary voltage Vₚ', _vp, 20, 240, 'V', const Color(0xFF38BDF8),
            (x) => setState(() => _vp = x)),
        _slider('Turns ratio Nₛ/Nₚ', _turnsRatio, 0.2, 5, '', const Color(0xFF9F7AEA),
            (x) => setState(() => _turnsRatio = x)),
        _slider('Primary current Iₚ', _ip, 0.5, 10, 'A', const Color(0xFFF97316),
            (x) => setState(() => _ip = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(
            _isStepUp
                ? 'Step-up transformer: Nₛ > Nₚ, so Vₛ > Vₚ — but Iₛ < Iₚ, since power VI must stay (ideally) the same on both sides.'
                : 'Step-down transformer: Nₛ < Nₚ, so Vₛ < Vₚ — but Iₛ > Iₚ. Notice Vₚ×Iₚ always equals Vₛ×Iₛ, the ideal power-conservation rule.',
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
              style: Type.bodyStrong.copyWith(fontSize: 16, fontFamily: 'monospace', color: color)),
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

class _TransformerPainter extends CustomPainter {
  final double turnsRatio;
  final bool stepUp;
  _TransformerPainter({required this.turnsRatio, required this.stepUp});

  @override
  void paint(Canvas canvas, Size size) {
    final coreLeft = size.width * 0.42;
    final coreRight = size.width * 0.58;
    final coreTop = size.height * 0.18;
    final coreBot = size.height * 0.82;

    // Iron core (rectangle outline).
    final corePaint = Paint()
      ..color = const Color(0xFF9CA3AF)
      ..strokeWidth = 10
      ..style = PaintingStyle.stroke;
    canvas.drawRect(Rect.fromLTRB(coreLeft, coreTop, coreRight, coreBot), corePaint);

    // Primary coil (left), secondary coil (right). Turn count reflects ratio.
    final npTurns = stepUp ? 5 : (5 * turnsRatio).clamp(2, 5).round();
    final nsTurns = stepUp ? (5 * turnsRatio).clamp(2, 14).round() : 5;

    _drawCoil(canvas, Offset(coreLeft, (coreTop + coreBot) / 2), npTurns.toDouble(),
        const Color(0xFF38BDF8), size.height * 0.5, left: true);
    _drawCoil(canvas, Offset(coreRight, (coreTop + coreBot) / 2), nsTurns.toDouble(),
        const Color(0xFFF97316), size.height * 0.5, left: false);

    _label(canvas, 'Nₚ', Offset(coreLeft - 34, coreTop - 6), const Color(0xFF38BDF8), 12);
    _label(canvas, 'Nₛ', Offset(coreRight + 34, coreTop - 6), const Color(0xFFF97316), 12);
    _label(canvas, stepUp ? 'STEP-UP' : 'STEP-DOWN', Offset(size.width / 2, 16),
        const Color(0xFF34D399), 11);
  }

  void _drawCoil(Canvas canvas, Offset axisPoint, double turns, Color color, double totalH,
      {required bool left}) {
    final n = turns.clamp(2, 14).toInt();
    final spacing = totalH / (n + 1);
    final paint = Paint()
      ..color = color
      ..strokeWidth = 2.4
      ..style = PaintingStyle.stroke;
    for (int i = 0; i < n; i++) {
      final y = axisPoint.dy - totalH / 2 + spacing * (i + 1);
      canvas.drawOval(
        Rect.fromCenter(center: Offset(axisPoint.dx + (left ? -10 : 10), y), width: 22, height: 12),
        paint,
      );
    }
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
  bool shouldRepaint(_TransformerPainter old) =>
      old.turnsRatio != turnsRatio || old.stepUp != stepUp;
}
