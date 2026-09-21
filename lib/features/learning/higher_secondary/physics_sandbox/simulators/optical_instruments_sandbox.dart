import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/fx/stage_backdrop.dart';

/// Optical Instruments Sandbox — astronomical telescope ray schematic.
///
/// Students adjust the objective and eyepiece focal lengths (both converging
/// lenses) and watch the schematic tube length change while the magnifying
/// power M = fo/fe updates live. A toggle switches to the simple microscope
/// (magnifying glass) case, M = D/fe for image at infinity vs 1 + D/fe for
/// image at the near point.
class OpticalInstrumentsSandbox extends StatefulWidget {
  const OpticalInstrumentsSandbox({super.key});

  @override
  State<OpticalInstrumentsSandbox> createState() => _OpticalInstrumentsSandboxState();
}

class _OpticalInstrumentsSandboxState extends State<OpticalInstrumentsSandbox> {
  bool _telescope = true; // false → simple microscope (magnifier)
  double _fo = 60.0; // objective focal length, cm (telescope)
  double _fe = 5.0; // eyepiece focal length, cm
  bool _relaxedEye = true; // simple microscope: image at infinity vs near point
  static const double _d = 25.0; // near point distance, cm

  double get _telescopeM => _fo / _fe;
  double get _microscopeM => _relaxedEye ? _d / _fe : 1 + _d / _fe;

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
            painter: _InstrumentPainter(
              telescope: _telescope,
              fo: _fo,
              fe: _fe,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(children: [
          Expanded(
            child: _readout(
              'Magnifying power M',
              '${(_telescope ? _telescopeM : _microscopeM).toStringAsFixed(1)}×',
              Palette.info,
            ),
          ),
          const SizedBox(width: Gap.x3),
          Expanded(
            child: _readout(
              _telescope ? 'Tube length fo+fe' : 'Near point D',
              _telescope ? '${(_fo + _fe).toStringAsFixed(0)} cm' : '${_d.toStringAsFixed(0)} cm',
              Palette.accent,
            ),
          ),
        ]),
        const SizedBox(height: Gap.x2),
        Container(
          padding: const EdgeInsets.symmetric(horizontal: Gap.x3, vertical: Gap.x2),
          decoration: BoxDecoration(
            color: Palette.infoSoft,
            borderRadius: BorderRadius.circular(Corner.md),
            border: Border.all(color: Palette.border),
          ),
          child: Text(
            _telescope
                ? 'M = fo/fe — a LARGE objective focal length and a SHORT eyepiece focal length give high magnification.'
                : (_relaxedEye
                    ? 'Relaxed eye, image at infinity: M = D/fe.'
                    : 'Image formed at the near point: M = 1 + D/fe (slightly higher magnification, but the eye must strain).'),
            style: Type.bodyStrong.copyWith(fontSize: 13),
          ),
        ),
        const SizedBox(height: Gap.x3),

        Row(children: [
          Expanded(child: _typeButton('Telescope', _telescope, () {
            setState(() => _telescope = true);
          })),
          const SizedBox(width: Gap.x3),
          Expanded(child: _typeButton('Simple microscope', !_telescope, () {
            setState(() => _telescope = false);
          })),
        ]),
        const SizedBox(height: Gap.x2),

        if (_telescope) ...[
          _slider('Objective focal length fo', _fo, 20, 100, 'cm', Palette.primary,
              (val) => setState(() => _fo = val)),
          _slider('Eyepiece focal length fe', _fe, 1, 20, 'cm', Palette.jee,
              (val) => setState(() => _fe = val)),
        ] else ...[
          _slider('Lens focal length fe', _fe, 2, 20, 'cm', Palette.jee,
              (val) => setState(() => _fe = val)),
          Row(children: [
            Expanded(child: _typeButton('Relaxed eye (∞)', _relaxedEye, () {
              setState(() => _relaxedEye = true);
            })),
            const SizedBox(width: Gap.x3),
            Expanded(child: _typeButton('Image at near point', !_relaxedEye, () {
              setState(() => _relaxedEye = false);
            })),
          ]),
        ],
      ],
    );
  }

  Widget _typeButton(String label, bool active, VoidCallback onTap) {
    return GestureDetector(
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(vertical: 11),
        alignment: Alignment.center,
        decoration: BoxDecoration(
          color: active ? Palette.primary : Palette.surface,
          borderRadius: BorderRadius.circular(Corner.md),
          border: Border.all(color: active ? Palette.primary : Palette.border),
        ),
        child: Text(
          label,
          style: Type.bodyStrong.copyWith(
              color: active ? Colors.white : Palette.textBody, fontSize: 13),
        ),
      ),
    );
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
          Text(label.toUpperCase(), style: Type.label.copyWith(fontSize: 9)),
          const SizedBox(height: 4),
          Text(value,
              style: Type.bodyStrong.copyWith(
                  fontSize: 17, fontFamily: 'monospace', color: color)),
        ],
      ),
    );
  }

  Widget _slider(String label, double value, double min, double max,
      String unit, Color color, ValueChanged<double> onChanged) {
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

class _InstrumentPainter extends CustomPainter {
  final bool telescope;
  final double fo, fe;

  _InstrumentPainter({required this.telescope, required this.fo, required this.fe});

  @override
  void paint(Canvas canvas, Size size) {
    final axisY = size.height * 0.52;
    canvas.drawLine(Offset(0, axisY), Offset(size.width, axisY),
        Paint()..color = Palette.stageLine..strokeWidth = 1.5);

    if (telescope) {
      _drawTelescope(canvas, size, axisY);
    } else {
      _drawMicroscope(canvas, size, axisY);
    }
  }

  void _drawTelescope(Canvas canvas, Size size, double axisY) {
    final scale = (size.width * 0.7) / (fo + fe);
    final objX = size.width * 0.18;
    final eyeX = objX + fo * scale;

    _lens(canvas, Offset(objX, axisY), 55, const Color(0xFF60A5FA), 'Objective (fo)');
    _lens(canvas, Offset(eyeX, axisY), 34, const Color(0xFFFBBF24), 'Eyepiece (fe)');

    // Parallel incoming rays from a distant object (two rays).
    final rayP = Paint()..color = Colors.white70..strokeWidth = 1.6;
    for (final dy in [-28.0, 28.0]) {
      final start = Offset(0, axisY + dy);
      final hit = Offset(objX, axisY + dy);
      canvas.drawLine(start, hit, rayP);
      // both converge to the common focal point of the objective, fo to the right
      final focusPt = Offset(objX + fo * scale, axisY);
      canvas.drawLine(hit, focusPt, Paint()..color = const Color(0xFFFDE68A)..strokeWidth = 1.6);
    }

    _label(canvas, 'fo', Offset((objX + eyeX) / 2, axisY - 68), Colors.white54, 10);
  }

  void _drawMicroscope(Canvas canvas, Size size, double axisY) {
    final lensX = size.width * 0.5;
    _lens(canvas, Offset(lensX, axisY), 50, const Color(0xFFFBBF24), 'Lens (fe)');

    // Small object near the lens (inside focal length) with two rays to the eye.
    final objX = lensX - 40;
    final objTop = Offset(objX, axisY - 18);
    canvas.drawLine(Offset(objX, axisY), objTop,
        Paint()..color = const Color(0xFF34D399)..strokeWidth = 2.5..strokeCap = StrokeCap.round);

    final rayP = Paint()..color = Colors.white70..strokeWidth = 1.4;
    canvas.drawLine(objTop, Offset(lensX, axisY - 55), rayP);
    canvas.drawLine(Offset(lensX, axisY - 55), Offset(size.width, axisY - 90), rayP);
    canvas.drawLine(objTop, Offset(lensX, axisY), rayP);
    canvas.drawLine(Offset(lensX, axisY), Offset(size.width, axisY - 8), rayP);

    _label(canvas, 'virtual, magnified image', Offset(size.width * 0.78, axisY - 100),
        const Color(0xFFC084FC), 9);
  }

  void _lens(Canvas canvas, Offset centre, double halfHeight, Color color, String tag) {
    final path = Path()
      ..moveTo(centre.dx, centre.dy - halfHeight)
      ..quadraticBezierTo(centre.dx + 14, centre.dy, centre.dx, centre.dy + halfHeight)
      ..quadraticBezierTo(centre.dx - 14, centre.dy, centre.dx, centre.dy - halfHeight);
    canvas.drawPath(
        path,
        Paint()
          ..color = color
          ..style = PaintingStyle.stroke
          ..strokeWidth = 3);
    _label(canvas, tag, Offset(centre.dx, centre.dy + halfHeight + 14), color, 9.5);
  }

  void _label(Canvas canvas, String text, Offset center, Color color, double fontSize) {
    final tp = TextPainter(
      text: TextSpan(
          text: text,
          style: TextStyle(
              color: color, fontSize: fontSize, fontWeight: FontWeight.w700, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, center - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_InstrumentPainter old) =>
      old.telescope != telescope || old.fo != fo || old.fe != fe;
}
