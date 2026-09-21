import 'package:flutter/material.dart';
import '../theme/tokens.dart';
import '../widgets/sim_controls.dart';
import '../widgets/sim_kit.dart';

/// Relative Motion — two cars, three points of view.
///
/// Set each car's velocity, then switch the camera between the ground frame
/// and each car's frame. In A's frame, A freezes and the world slides past —
/// the moment relative velocity clicks.
class RelativeMotionSandbox extends StatefulWidget {
  const RelativeMotionSandbox({super.key});

  @override
  State<RelativeMotionSandbox> createState() => _RelativeMotionSandboxState();
}

enum _Frame { ground, carA, carB }

class _RelativeMotionSandboxState extends State<RelativeMotionSandbox>
    with TickerProviderStateMixin {
  double _vA = 12; // m/s
  double _vB = 6;
  _Frame _frame = _Frame.ground;

  late final SimClock _clock = SimClock(this, () => setState(() {}));

  double get _xA => _vA * _clock.t;
  double get _xB => _vB * _clock.t;
  double get _vRel => _vA - _vB;

  @override
  void dispose() {
    _clock.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    // Camera position: whatever the observer rides moves to rest.
    final camX = switch (_frame) {
      _Frame.ground => 0.0,
      _Frame.carA => _xA,
      _Frame.carB => _xB,
    };
    return ListView(
      padding: const EdgeInsets.fromLTRB(Gap.x4, Gap.x3, Gap.x4, Gap.x4),
      children: [
        SandboxStage(
          child: CustomPaint(
            painter: _TwoCarPainter(
              xA: _xA - camX,
              xB: _xB - camX,
              ground: _frame == _Frame.ground,
              camX: camX,
            ),
            child: const SizedBox.expand(),
          ),
        ),
        const SizedBox(height: Gap.x3),
        Row(
          children: [
            for (final (f, label) in [
              (_Frame.ground, 'Ground view'),
              (_Frame.carA, 'Ride car A'),
              (_Frame.carB, 'Ride car B'),
            ]) ...[
              if (f != _Frame.ground) const SizedBox(width: Gap.x2),
              Expanded(
                child: GestureDetector(
                  onTap: () => setState(() => _frame = f),
                  child: AnimatedContainer(
                    duration: Motion.fast,
                    padding: const EdgeInsets.symmetric(vertical: 9),
                    decoration: BoxDecoration(
                      color: _frame == f ? Palette.primary : Palette.surface,
                      borderRadius: BorderRadius.circular(Corner.pill),
                      border: Border.all(
                          color: _frame == f ? Palette.primary : Palette.border),
                    ),
                    alignment: Alignment.center,
                    child: Text(label,
                        style: Type.caption.copyWith(
                            fontWeight: FontWeight.w700,
                            color: _frame == f ? Colors.white : Palette.textMuted)),
                  ),
                ),
              ),
            ],
          ],
        ),
        const SizedBox(height: Gap.x3),
        TelemetryRow([
          TelemetryChip('v(A)', '${_vA.toStringAsFixed(1)} m/s',
              color: const Color(0xFFF97316)),
          TelemetryChip('v(B)', '${_vB.toStringAsFixed(1)} m/s',
              color: const Color(0xFF38BDF8)),
          TelemetryChip('v(A rel B)', '${_vRel.toStringAsFixed(1)} m/s',
              color: Palette.success),
        ]),
        const SizedBox(height: Gap.x3),
        SimSlider(
          label: 'Car A velocity',
          value: _vA,
          min: -15,
          max: 15,
          unit: 'm/s',
          color: const Color(0xFFF97316),
          onChanged: (v) => setState(() => _vA = v),
        ),
        SimSlider(
          label: 'Car B velocity',
          value: _vB,
          min: -15,
          max: 15,
          unit: 'm/s',
          color: const Color(0xFF38BDF8),
          onChanged: (v) => setState(() => _vB = v),
        ),
        const SizedBox(height: Gap.x2),
        SimControls(
          running: _clock.running,
          onStart: _clock.start,
          onPause: _clock.pause,
          onReset: _clock.reset,
        ),
      ],
    );
  }
}

class _TwoCarPainter extends CustomPainter {
  final double xA, xB, camX;
  final bool ground;
  _TwoCarPainter({required this.xA, required this.xB, required this.ground, required this.camX});

  static const _pxPerM = 4.0;

  @override
  void paint(Canvas canvas, Size size) {
    final laneA = size.height * 0.38;
    final laneB = size.height * 0.68;

    for (final y in [laneA, laneB]) {
      canvas.drawLine(Offset(0, y + 14), Offset(size.width, y + 14),
          Paint()..color = Colors.white30..strokeWidth = 2);
    }

    // Milestones scroll with the observed world (they belong to the ground).
    final worldW = size.width / _pxPerM;
    final blockStart = (camX / worldW).floorToDouble() * worldW;
    for (double m = blockStart - worldW; m < blockStart + 2 * worldW; m += 15) {
      final x = (m - camX) * _pxPerM + size.width * 0.4;
      if (x < -10 || x > size.width + 10) continue;
      canvas.drawLine(Offset(x, laneB + 14), Offset(x, laneB + 22),
          Paint()..color = Colors.white24..strokeWidth = 1.5);
    }

    _car(canvas, Offset(_wrap(xA * _pxPerM + size.width * 0.4, size.width), laneA),
        const Color(0xFFF97316), 'A');
    _car(canvas, Offset(_wrap(xB * _pxPerM + size.width * 0.4, size.width), laneB),
        const Color(0xFF38BDF8), 'B');
  }

  double _wrap(double x, double w) {
    final span = w + 60;
    var r = (x + 30) % span;
    if (r < 0) r += span;
    return r - 30;
  }

  void _car(Canvas canvas, Offset pos, Color color, String label) {
    const w = 44.0, h = 18.0;
    canvas.drawRRect(
        RRect.fromRectAndRadius(
            Rect.fromCenter(center: pos, width: w, height: h),
            const Radius.circular(5)),
        Paint()..color = color);
    for (final dx in [-w / 2 + 9, w / 2 - 9]) {
      canvas.drawCircle(pos + Offset(dx, h / 2 + 3), 4.5, Paint()..color = Colors.black87);
    }
    final tp = TextPainter(
      text: TextSpan(
          text: label,
          style: TextStyle(
              color: Colors.white, fontSize: 11, fontWeight: FontWeight.w800, fontFamily: 'monospace')),
      textDirection: TextDirection.ltr,
    )..layout();
    tp.paint(canvas, pos - Offset(tp.width / 2, tp.height / 2));
  }

  @override
  bool shouldRepaint(_TwoCarPainter old) =>
      old.xA != xA || old.xB != xB || old.ground != ground;
}
