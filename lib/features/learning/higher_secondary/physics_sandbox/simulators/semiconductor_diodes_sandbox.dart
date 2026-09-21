import 'dart:math' as math;
import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Semiconductor Diodes Sandbox — a p-n junction whose applied bias the
/// student sweeps from reverse to forward. The depletion region narrows under
/// forward bias and widens under reverse bias, and a live V–I characteristic
/// traces out the diode curve, so the ~0.7 V knee and reverse saturation
/// current become discoverable.
class SemiconductorDiodesSandbox extends StatefulWidget {
  const SemiconductorDiodesSandbox({super.key});

  @override
  State<SemiconductorDiodesSandbox> createState() =>
      _SemiconductorDiodesSandboxState();
}

class _SemiconductorDiodesSandboxState
    extends State<SemiconductorDiodesSandbox> {
  double _bias = 0.0; // volts, negative = reverse
  double _tempK = 300.0; // kelvin
  bool _silicon = true; // true = Si (0.7 V), false = Ge (0.3 V)

  // Shockley diode: I = Is (exp(V/(n·Vt)) − 1)
  static const double _isSi = 1e-12; // A (reverse saturation)
  static const double _isGe = 1e-6; // A (Ge leaks far more)
  double get _vt => 8.617e-5 * _tempK; // thermal voltage kT/q (V)
  double get _n => 1.0;

  double _current(double v) {
    final iS = _silicon ? _isSi : _isGe;
    final arg = (v / (_n * _vt)).clamp(-40.0, 30.0);
    return iS * (math.exp(arg) - 1); // amperes
  }

  double get _iMA => _current(_bias) * 1e3; // milliamps at the working point
  double get _knee => _silicon ? 0.7 : 0.3;
  // Depletion width shrinks as forward bias approaches the built-in potential.
  double get _depletion {
    final vbi = _knee;
    final ratio = (1 - _bias / vbi).clamp(0.0, 3.0);
    return math.sqrt(ratio); // relative width
  }

  @override
  Widget build(BuildContext context) {
    final forward = _bias > 0.02;
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
            painter: _DiodePainter(
              bias: _bias,
              depletion: _depletion,
              current: _current(_bias),
              knee: _knee,
              vt: _vt,
              iScale: _silicon ? _isSi : _isGe,
              n: _n,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(
          children: [
            Expanded(
              child: _readout('BIAS', '${_bias.toStringAsFixed(2)} V',
                  forward ? Palette.success : Palette.info),
            ),
            const SizedBox(width: Gap.x3),
            Expanded(
              child: _readout('CURRENT', _fmtCurrent(_current(_bias)),
                  Palette.accent),
            ),
            const SizedBox(width: Gap.x3),
            Expanded(
              child: _readout(
                  'STATE',
                  _bias < -0.02
                      ? 'REVERSE'
                      : (_iMA > 0.5 ? 'CONDUCTING' : 'OFF'),
                  forward ? Palette.success : Palette.textMuted),
            ),
          ],
        ),
        const SizedBox(height: Gap.x3),
        _slider('Applied bias V (− reverse · + forward)', _bias, -5, 1.0, 'V',
            Palette.primary, (v) => setState(() => _bias = v)),
        _slider('Temperature T', _tempK, 250, 450, 'K', Palette.accent,
            (v) => setState(() => _tempK = v)),
        const SizedBox(height: Gap.x2),
        Row(
          children: [
            _materialChip('Silicon (0.7 V)', _silicon,
                () => setState(() => _silicon = true)),
            const SizedBox(width: Gap.x3),
            _materialChip('Germanium (0.3 V)', !_silicon,
                () => setState(() => _silicon = false)),
          ],
        ),
        const SizedBox(height: Gap.x2),
        Text(
          forward
              ? 'Forward bias: the depletion layer thins and current climbs steeply once V passes the ${_knee} V knee.'
              : (_bias < -0.02
                  ? 'Reverse bias: the depletion layer widens and only a tiny saturation current leaks across.'
                  : 'Zero bias: the built-in potential holds carriers back — no net current.'),
          style: Type.caption.copyWith(fontSize: 12),
        ),
      ],
    );
  }

  String _fmtCurrent(double a) {
    if (a.abs() >= 1e-3) return '${(a * 1e3).toStringAsFixed(2)} mA';
    if (a.abs() >= 1e-6) return '${(a * 1e6).toStringAsFixed(2)} µA';
    if (a.abs() >= 1e-9) return '${(a * 1e9).toStringAsFixed(2)} nA';
    return '${(a * 1e12).toStringAsFixed(2)} pA';
  }

  Widget _readout(String label, String value, Color color) {
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
              style: Type.bodyStrong
                  .copyWith(fontSize: 14, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }

  Widget _materialChip(String label, bool active, VoidCallback onTap) {
    return Expanded(
      child: GestureDetector(
        onTap: onTap,
        child: Container(
          padding: const EdgeInsets.symmetric(vertical: 10),
          alignment: Alignment.center,
          decoration: BoxDecoration(
            color: active ? Palette.primary : Palette.surfaceAlt,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(
                color: active ? Palette.primary : Palette.border),
          ),
          child: Text(label,
              style: Type.caption.copyWith(
                  fontSize: 12,
                  fontWeight: FontWeight.w700,
                  color: active ? Colors.white : Palette.textMuted)),
        ),
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max, String unit,
      Color color, ValueChanged<double> onChanged) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text('$label = ${value.toStringAsFixed(unit == 'K' ? 0 : 2)} $unit',
            style: Type.caption
                .copyWith(fontSize: 12, fontWeight: FontWeight.w600)),
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

class _DiodePainter extends CustomPainter {
  final double bias, depletion, current, knee, vt, iScale, n;
  _DiodePainter({
    required this.bias,
    required this.depletion,
    required this.current,
    required this.knee,
    required this.vt,
    required this.iScale,
    required this.n,
  });

  static const _pColor = Color(0xFFF97316); // p-type (holes)
  static const _nColor = Color(0xFF38BDF8); // n-type (electrons)

  @override
  void paint(Canvas canvas, Size size) {
    // ── Top half: the junction bar ──
    final barTop = 18.0;
    final barH = 58.0;
    final barLeft = 20.0;
    final barRight = size.width - 20.0;
    final mid = (barLeft + barRight) / 2;
    final barW = barRight - barLeft;

    // p region and n region
    canvas.drawRect(
        Rect.fromLTRB(barLeft, barTop, mid, barTop + barH),
        Paint()..color = _pColor.withValues(alpha: 0.85));
    canvas.drawRect(
        Rect.fromLTRB(mid, barTop, barRight, barTop + barH),
        Paint()..color = _nColor.withValues(alpha: 0.85));

    // depletion region straddling the junction
    final depW = (depletion * barW * 0.14).clamp(2.0, barW * 0.42);
    canvas.drawRect(
        Rect.fromLTRB(mid - depW, barTop, mid + depW, barTop + barH),
        Paint()..color = const Color(0xEE10122B));
    canvas.drawRect(
        Rect.fromLTRB(mid - depW, barTop, mid + depW, barTop + barH),
        Paint()
          ..color = Colors.white38
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1);

    _label(canvas, 'p', Offset(barLeft + barW * 0.22, barTop + barH / 2),
        Colors.white, 13);
    _label(canvas, 'n', Offset(barRight - barW * 0.22, barTop + barH / 2),
        Colors.white, 13);
    _label(canvas, 'depletion', Offset(mid, barTop + barH + 12),
        Colors.white54, 9);
    _label(canvas, '${(depW / barW * 200).toStringAsFixed(0)}% width',
        Offset(mid, barTop - 8), Colors.white54, 9);

    // ── Bottom half: V–I characteristic curve ──
    final gTop = barTop + barH + 26;
    final gBottom = size.height - 14;
    final gLeft = 34.0;
    final gRight = size.width - 14;
    final gH = gBottom - gTop;
    final gW = gRight - gLeft;
    final vMin = -5.0, vMax = 1.0;
    final iMaxMA = 20.0;

    double vx(double v) => gLeft + (v - vMin) / (vMax - vMin) * gW;
    double iy(double iMA) {
      final c = iMA.clamp(-2.0, iMaxMA);
      return gBottom - (c + 2.0) / (iMaxMA + 2.0) * gH;
    }

    // axes
    final axis = Paint()
      ..color = Colors.white30
      ..strokeWidth = 1;
    final zeroY = iy(0);
    final zeroX = vx(0);
    canvas.drawLine(Offset(gLeft, zeroY), Offset(gRight, zeroY), axis);
    canvas.drawLine(Offset(zeroX, gTop), Offset(zeroX, gBottom), axis);
    _label(canvas, 'I', Offset(zeroX - 10, gTop + 4), Colors.white38, 9);
    _label(canvas, 'V', Offset(gRight - 6, zeroY + 10), Colors.white38, 9);

    // curve
    final path = Path();
    bool started = false;
    for (double v = vMin; v <= vMax; v += 0.02) {
      final arg = (v / (n * vt)).clamp(-40.0, 30.0);
      final iMA = iScale * (math.exp(arg) - 1) * 1e3;
      final p = Offset(vx(v), iy(iMA));
      if (!started) {
        path.moveTo(p.dx, p.dy);
        started = true;
      } else {
        path.lineTo(p.dx, p.dy);
      }
    }
    canvas.drawPath(
        path,
        Paint()
          ..color = Palette.accent
          ..style = PaintingStyle.stroke
          ..strokeWidth = 2.5
          ..strokeCap = StrokeCap.round);

    // knee marker
    final kneeX = vx(knee);
    canvas.drawLine(Offset(kneeX, gTop), Offset(kneeX, gBottom),
        Paint()..color = Colors.white12..strokeWidth = 1);
    _label(canvas, 'knee ${knee}V', Offset(kneeX, gTop - 2),
        Colors.white38, 8);

    // working point
    final wp = Offset(vx(bias), iy(current * 1e3));
    canvas.drawCircle(wp, 5, Paint()..color = Palette.success);
    canvas.drawCircle(wp, 5,
        Paint()..color = Colors.white..style = PaintingStyle.stroke..strokeWidth = 1.5);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fs) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(
              color: color,
              fontSize: fs,
              fontWeight: FontWeight.w700,
              fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_DiodePainter old) =>
      old.bias != bias ||
      old.depletion != depletion ||
      old.current != current ||
      old.knee != knee ||
      old.vt != vt ||
      old.iScale != iScale;
}
