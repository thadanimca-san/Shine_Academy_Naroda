import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Meter Bridge Sandbox — a 1-metre Wheatstone-bridge wire with a sliding
/// jockey. Student adjusts the known resistance S and the balance-point
/// length l; the unknown resistance R is computed live via R/S = l/(100−l).
class MeterBridgeSandbox extends StatefulWidget {
  const MeterBridgeSandbox({super.key});

  @override
  State<MeterBridgeSandbox> createState() => _MeterBridgeSandboxState();
}

class _MeterBridgeSandboxState extends State<MeterBridgeSandbox> {
  double _balanceCm = 40.0; // jockey position from left end, in cm (0-100)
  double _knownS = 10.0; // known resistance S, ohms

  // Balance condition: R/S = l/(100-l)  =>  R = S * l/(100-l)
  double get _unknownR {
    final l = _balanceCm;
    final denom = (100 - l);
    if (denom <= 0.001) return double.infinity;
    return _knownS * l / denom;
  }

  double get _galvanometerDeflection {
    // Purely illustrative: deflection proportional to distance from a
    // "true" balance point fixed at 50 cm for visual feedback purposes.
    return (_balanceCm - 50).abs();
  }

  @override
  Widget build(BuildContext context) {
    final r = _unknownR;
    final nearBalance = _galvanometerDeflection < 2;
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
            painter: _BridgePainter(balanceCm: _balanceCm, knownS: _knownS, unknownR: r, nearBalance: nearBalance),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
            child: _meter('Unknown  R = Sl/(100−l)',
                r.isFinite ? r.toStringAsFixed(2) : '∞', 'Ω', Palette.chElectroMag),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _meter('Galvanometer', nearBalance ? 'BALANCED (0)' : _galvanometerDeflection.toStringAsFixed(0),
                nearBalance ? '' : '(rel. deflection)',
                nearBalance ? Palette.success : Palette.accent),
          ),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Jockey position  l', _balanceCm, 1, 99, 'cm', const Color(0xFF38BDF8),
            (x) => setState(() => _balanceCm = x)),
        _slider('Known resistance  S', _knownS, 1, 50, 'Ω', Palette.accent,
            (x) => setState(() => _knownS = x)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.accentSoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('Try it: slide the jockey until the galvanometer reads BALANCED (zero deflection). At that exact point, no current flows through the galvanometer branch, and the unknown resistance follows from just the wire\'s length ratio: R/S = l/(100−l).'),
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
              style: Type.bodyStrong.copyWith(fontSize: 15, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max, String unit, Color color,
      ValueChanged<double> onChanged) {
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

class _BridgePainter extends CustomPainter {
  final double balanceCm;
  final double knownS;
  final double unknownR;
  final bool nearBalance;
  _BridgePainter({
    required this.balanceCm,
    required this.knownS,
    required this.unknownR,
    required this.nearBalance,
  });

  @override
  void paint(Canvas canvas, Size size) {
    final wireY = size.height * 0.55;
    final leftX = size.width * 0.10;
    final rightX = size.width * 0.90;
    final wireLen = rightX - leftX;

    // The 1-metre bridge wire.
    canvas.drawLine(Offset(leftX, wireY), Offset(rightX, wireY), Paint()
      ..color = const Color(0xFFFDE68A)
      ..strokeWidth = 3);
    _label(canvas, '0 cm', Offset(leftX, wireY + 16), Colors.white54, 9.5);
    _label(canvas, '100 cm', Offset(rightX, wireY + 16), Colors.white54, 9.5);

    // Jockey position.
    final jockeyX = leftX + (balanceCm / 100) * wireLen;
    canvas.drawLine(Offset(jockeyX, wireY - 40), Offset(jockeyX, wireY + 4), Paint()
      ..color = nearBalance ? Palette.success : const Color(0xFF38BDF8)
      ..strokeWidth = 2.5);
    canvas.drawCircle(Offset(jockeyX, wireY), 5, Paint()..color = nearBalance ? Palette.success : const Color(0xFF38BDF8));
    _label(canvas, 'jockey (l=${balanceCm.toStringAsFixed(0)}cm)', Offset(jockeyX, wireY - 50),
        nearBalance ? Palette.success : const Color(0xFF38BDF8), 10);

    // Galvanometer branch (from jockey up to a node connecting R and S box).
    final topY = size.height * 0.16;
    final topMidX = size.width / 2;
    canvas.drawLine(Offset(jockeyX, wireY - 4), Offset(topMidX, topY), Paint()
      ..color = Colors.white54
      ..strokeWidth = 1.6);
    canvas.drawCircle(Offset(topMidX, topY), 12, Paint()
      ..color = Colors.transparent
      ..style = PaintingStyle.stroke);
    canvas.drawCircle(Offset(topMidX, topY), 12, Paint()
      ..color = nearBalance ? Palette.success : Colors.white70
      ..style = PaintingStyle.stroke
      ..strokeWidth = 2);
    _label(canvas, 'G', Offset(topMidX, topY), nearBalance ? Palette.success : Colors.white70, 11);

    // R (unknown, left gap box) and S (known, right gap box) above the wire ends.
    _resistorBox(canvas, Offset(leftX + wireLen * 0.22, topY - 30), 'R', Palette.chElectroMag,
        unknownR.isFinite ? unknownR.toStringAsFixed(1) : '∞');
    _resistorBox(canvas, Offset(leftX + wireLen * 0.78, topY - 30), 'S', Palette.accent,
        knownS.toStringAsFixed(1));

    // Connect boxes to the top node and down to wire ends.
    canvas.drawLine(Offset(leftX + wireLen * 0.22, topY - 12), Offset(topMidX, topY), Paint()
      ..color = Colors.white38
      ..strokeWidth = 1.4);
    canvas.drawLine(Offset(leftX + wireLen * 0.78, topY - 12), Offset(topMidX, topY), Paint()
      ..color = Colors.white38
      ..strokeWidth = 1.4);
    canvas.drawLine(Offset(leftX, wireY), Offset(leftX + wireLen * 0.22, topY - 12), Paint()
      ..color = Colors.white38
      ..strokeWidth = 1.4);
    canvas.drawLine(Offset(rightX, wireY), Offset(leftX + wireLen * 0.78, topY - 12), Paint()
      ..color = Colors.white38
      ..strokeWidth = 1.4);

    // Battery below the wire.
    final battY = size.height * 0.86;
    canvas.drawLine(Offset(leftX, wireY), Offset(leftX, battY), Paint()..color = Colors.white38..strokeWidth = 1.4);
    canvas.drawLine(Offset(rightX, wireY), Offset(rightX, battY), Paint()..color = Colors.white38..strokeWidth = 1.4);
    canvas.drawLine(Offset(leftX, battY), Offset(rightX, battY), Paint()..color = Colors.white38..strokeWidth = 1.4);
    _label(canvas, 'battery + key', Offset((leftX + rightX) / 2, battY + 14), Colors.white38, 9.5);
  }

  void _resistorBox(Canvas canvas, Offset topLeft, String label, Color color, String value) {
    final rect = Rect.fromLTWH(topLeft.dx - 22, topLeft.dy - 12, 44, 24);
    canvas.drawRRect(RRect.fromRectAndRadius(rect, const Radius.circular(4)), Paint()
      ..color = color.withValues(alpha: 0.22));
    canvas.drawRRect(RRect.fromRectAndRadius(rect, const Radius.circular(4)), Paint()
      ..color = color
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.6);
    _label(canvas, '$label=$value Ω', rect.center, color, 10);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style:
              TextStyle(color: color, fontSize: fs, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
      textAlign: TextAlign.center,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_BridgePainter old) =>
      old.balanceCm != balanceCm || old.knownS != knownS || old.unknownR != unknownR;
}
