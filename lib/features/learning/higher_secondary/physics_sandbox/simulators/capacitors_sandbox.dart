import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Capacitors Sandbox — a parallel-plate capacitor whose area, plate
/// separation and dielectric the student controls. It shows capacitance C,
/// stored charge Q at a fixed battery voltage, and the field E live, so the
/// relationships C = ε₀εᵣA/d, Q = CV and E = V/d become discoverable.
class CapacitorsSandbox extends StatefulWidget {
  const CapacitorsSandbox({super.key});

  @override
  State<CapacitorsSandbox> createState() => _CapacitorsSandboxState();
}

class _CapacitorsSandboxState extends State<CapacitorsSandbox> {
  double _area = 200.0; // cm²
  double _d = 2.0; // mm
  double _k = 1.0; // dielectric constant εᵣ
  double _v = 12.0; // battery volts

  static const double _eps0 = 8.854e-12; // F/m

  double get _capF => _k * _eps0 * (_area * 1e-4) / (_d * 1e-3); // farads
  double get _capPF => _capF * 1e12; // picofarads
  double get _qNC => _capF * _v * 1e9; // nanocoulombs
  double get _eField => _v / (_d * 1e-3); // V/m
  double get _energyNJ => 0.5 * _capF * _v * _v * 1e9; // nanojoules

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
            painter: _CapPainter(area: _area, d: _d, k: _k, v: _v, eField: _eField),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Capacitance', '${_capPF.toStringAsFixed(1)} pF', Palette.primary)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Charge Q', '${_qNC.toStringAsFixed(2)} nC', Palette.accent)),
        ]),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(child: _meter('Field E', '${(_eField / 1000).toStringAsFixed(1)} kV/m', Palette.info)),
          const SizedBox(width: Gap.x3),
          Expanded(child: _meter('Energy U', '${_energyNJ.toStringAsFixed(1)} nJ', Palette.success)),
        ]),
        const SizedBox(height: Gap.x3),
        _slider('Plate area A', _area, 50, 400, 'cm²', const Color(0xFF38BDF8),
            (v) => setState(() => _area = v)),
        _slider('Separation d', _d, 0.5, 6, 'mm', const Color(0xFFF97316),
            (v) => setState(() => _d = v)),
        _slider('Dielectric εᵣ', _k, 1, 8, '', Palette.primary,
            (v) => setState(() => _k = v)),
        _slider('Battery V', _v, 2, 24, 'V', Palette.accent,
            (v) => setState(() => _v = v)),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.all(Gap.x3),
          decoration: BoxDecoration(
            color: Palette.primarySoft,
            borderRadius: BorderRadius.circular(Corner.md),
          ),
          child: Text(TrilingualService.instance.getUIText('C = ε₀εᵣA/d.  Halve d → C doubles.  Slide a dielectric in → C grows by εᵣ. ''With the battery attached, V is fixed so Q = CV rises with C.'),
            style: Type.caption.copyWith(color: Palette.primaryDeep),
          ),
        ),
      ],
    );
  }

  Widget _meter(String label, String value, Color color) {
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
          const SizedBox(height: 4),
          Text(value, style: Type.bodyStrong.copyWith(fontSize: 15, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max, String unit,
      Color color, ValueChanged<double> onChanged) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(
          unit.isEmpty
              ? '$label: ${value.toStringAsFixed(2)}'
              : '$label = ${value.toStringAsFixed(1)} $unit',
          style: Type.caption.copyWith(fontSize: 12, fontWeight: FontWeight.w600),
        ),
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

class _CapPainter extends CustomPainter {
  final double area, d, k, v, eField;
  _CapPainter({required this.area, required this.d, required this.k, required this.v, required this.eField});

  @override
  void paint(Canvas canvas, Size size) {
    final cx = size.width / 2;
    final cy = size.height / 2;
    final plateH = 20 + (area / 400) * 90; // area → plate height
    final gap = 20 + (d / 6) * 90; // separation → visible gap
    final leftX = cx - gap / 2;
    final rightX = cx + gap / 2;

    // Dielectric slab
    if (k > 1.01) {
      final slab = Rect.fromLTRB(leftX + 4, cy - plateH / 2, rightX - 4, cy + plateH / 2);
      canvas.drawRect(slab, Paint()..color = const Color(0x334F46E5));
      _label(canvas, 'εᵣ=${k.toStringAsFixed(1)}', Offset(cx, cy + plateH / 2 + 12), Colors.white54, 10);
    }

    // Field lines
    final fieldStrength = (eField / 24000).clamp(0.2, 1.0);
    final lineP = Paint()
      ..color = Color.fromRGBO(245, 158, 11, fieldStrength)
      ..strokeWidth = 1.5
      ..strokeCap = StrokeCap.round;
    final nLines = 5;
    for (int i = 0; i < nLines; i++) {
      final y = cy - plateH / 2 + plateH * (i + 0.5) / nLines;
      canvas.drawLine(Offset(leftX + 4, y), Offset(rightX - 8, y), lineP);
      canvas.drawLine(Offset(rightX - 8, y), Offset(rightX - 14, y - 3), lineP);
      canvas.drawLine(Offset(rightX - 8, y), Offset(rightX - 14, y + 3), lineP);
    }

    // Plates
    final pW = 8.0;
    canvas.drawRect(Rect.fromLTWH(leftX - pW, cy - plateH / 2, pW, plateH),
        Paint()..color = const Color(0xFFDC2626)); // + plate
    canvas.drawRect(Rect.fromLTWH(rightX, cy - plateH / 2, pW, plateH),
        Paint()..color = const Color(0xFF38BDF8)); // - plate

    // Charge symbols
    final chargeP = TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.w800);
    for (int i = 0; i < 4; i++) {
      final y = cy - plateH / 2 + plateH * (i + 0.5) / 4;
      _labelStyled(canvas, '+', Offset(leftX - pW / 2, y), chargeP);
      _labelStyled(canvas, '−', Offset(rightX + pW / 2, y), chargeP);
    }

    // Wires to battery
    final wireP = Paint()..color = Colors.white38..strokeWidth = 2;
    canvas.drawLine(Offset(leftX - pW, cy), Offset(leftX - pW - 30, cy), wireP);
    canvas.drawLine(Offset(leftX - pW - 30, cy), Offset(leftX - pW - 30, size.height - 18), wireP);
    canvas.drawLine(Offset(rightX + pW, cy), Offset(rightX + pW + 30, cy), wireP);
    canvas.drawLine(Offset(rightX + pW + 30, cy), Offset(rightX + pW + 30, size.height - 18), wireP);
    _label(canvas, '${v.toStringAsFixed(0)} V battery', Offset(cx, size.height - 12), Colors.white54, 10);
    _label(canvas, 'A = ${area.toStringAsFixed(0)} cm²   d = ${d.toStringAsFixed(1)} mm',
        Offset(cx, 16), Colors.white54, 10);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fontSize) {
    _labelStyled(canvas, text, center,
        TextStyle(color: color, fontSize: fontSize, fontWeight: FontWeight.w700, fontFamily: 'monospace'));
  }

  void _labelStyled(Canvas canvas, String text, Offset center, TextStyle style) {
    final tp = TextPainter(text: TextSpan(text: text, style: style), textDirection: TextDirection.ltr)..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_CapPainter old) =>
      old.area != area || old.d != d || old.k != k || old.v != v || old.eField != eField;
}
