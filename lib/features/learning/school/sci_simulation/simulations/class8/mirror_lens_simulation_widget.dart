import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

enum _OpticType { concaveMirror, convexMirror, convexLens, concaveLens }

/// Slide an object toward/away from a chosen mirror or lens and watch a
/// simplified, qualitatively-correct image respond: concave mirror/convex
/// lens images grow, invert, and shrink as distance increases; convex
/// mirror/concave lens images stay erect and diminished throughout —
/// matching Activities 10.3 and 10.9 in the chapter.
class MirrorLensSimulationWidget extends StatefulWidget {
  const MirrorLensSimulationWidget({super.key});

  @override
  State<MirrorLensSimulationWidget> createState() => _MirrorLensSimulationWidgetState();
}

class _MirrorLensSimulationWidgetState extends State<MirrorLensSimulationWidget> {
  _OpticType _type = _OpticType.concaveMirror;
  double _distance = 0.25; // 0 (close) .. 1 (far)

  bool get _convergesLikeConcaveMirror => _type == _OpticType.concaveMirror || _type == _OpticType.convexLens;

  @override
  Widget build(BuildContext context) {
    final label = switch (_type) {
      _OpticType.concaveMirror => 'Concave Mirror',
      _OpticType.convexMirror => 'Convex Mirror',
      _OpticType.convexLens => 'Convex Lens',
      _OpticType.concaveLens => 'Concave Lens',
    };

    return SimFrame(
      title: 'Mirror & Lens Image Explorer',
      icon: Icons.remove_red_eye,
      accent: const Color(0xFFD9622A),
      description: 'Pick a mirror or lens, then slide the object closer or farther to see how the image changes.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: _OpticType.values.map((t) {
              final isSelected = _type == t;
              final l = switch (t) {
                _OpticType.concaveMirror => 'Concave Mirror',
                _OpticType.convexMirror => 'Convex Mirror',
                _OpticType.convexLens => 'Convex Lens',
                _OpticType.concaveLens => 'Concave Lens',
              };
              return ChoiceChip(
                label: Text(l, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: const Color(0xFFD9622A),
                backgroundColor: const Color(0xFFD9622A).withValues(alpha: 0.15),
                onSelected: (_) => setState(() => _type = t),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: const Color(0xFFFBE8DC), borderRadius: BorderRadius.circular(14), border: Border.all(color: Colors.grey.shade300)),
            child: CustomPaint(
              size: Size.infinite,
              painter: _OpticsPainter(type: _type, distance: _distance),
            ),
          ),
          const SizedBox(height: 12),
          SimSlider(
            label: 'Object distance: ${_distance < 0.4 ? "Close" : _distance < 0.7 ? "Medium" : "Far"}',
            value: _distance,
            min: 0.1,
            max: 1.0,
            activeColor: const Color(0xFFD9622A),
            onChanged: (v) => setState(() => _distance = v),
          ),
          const SizedBox(height: 10),
          Text(
            _describeImage(label),
            style: TextStyle(fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant),
          ),
        ],
      ),
    );
  }

  String _describeImage(String label) {
    if (_convergesLikeConcaveMirror) {
      if (_distance < 0.45) {
        return '$label, object close: the image is erect and ENLARGED.';
      }
      return '$label, object far: the image becomes INVERTED, and changes size with distance.';
    }
    return '$label: the image is always erect and DIMINISHED (smaller), no matter the distance.';
  }
}

class _OpticsPainter extends CustomPainter {
  final _OpticType type;
  final double distance; // 0..1

  _OpticsPainter({required this.type, required this.distance});

  bool get _converges => type == _OpticType.concaveMirror || type == _OpticType.convexLens;
  bool get _isMirror => type == _OpticType.concaveMirror || type == _OpticType.convexMirror;

  @override
  void paint(Canvas canvas, Size size) {
    final w = size.width, h = size.height;
    final centerY = h / 2;
    final opticX = w * 0.42;

    // Draw the mirror/lens symbol.
    final opticPaint = Paint()
      ..color = const Color(0xFF9C3448)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 3;
    if (_isMirror) {
      final curveOut = type == _OpticType.concaveMirror ? -18.0 : 18.0;
      final path = Path()
        ..moveTo(opticX, centerY - 55)
        ..quadraticBezierTo(opticX + curveOut, centerY, opticX, centerY + 55);
      canvas.drawPath(path, opticPaint);
    } else {
      final bulge = type == _OpticType.convexLens ? 14.0 : -14.0;
      final path = Path()
        ..moveTo(opticX, centerY - 55)
        ..quadraticBezierTo(opticX + bulge, centerY, opticX, centerY + 55)
        ..moveTo(opticX, centerY - 55)
        ..quadraticBezierTo(opticX - bulge, centerY, opticX, centerY + 55);
      canvas.drawPath(path, opticPaint);
    }

    // Object: an upright arrow, placed to the left, distance controls how far.
    final objectX = w * 0.12;
    final objectHeight = 40.0;
    final objectPaint = Paint()
      ..color = const Color(0xFF3F6A9C)
      ..strokeWidth = 3
      ..strokeCap = StrokeCap.round;
    _drawArrow(canvas, Offset(objectX, centerY), objectHeight, objectPaint, pointingUp: true);

    // Image: size/orientation depend on optic type + distance.
    double scale;
    bool inverted;
    if (_converges) {
      if (distance < 0.45) {
        scale = 1.0 + (0.45 - distance) * 2.2; // enlarges as it gets closer
        inverted = false;
      } else {
        final t = ((distance - 0.45) / 0.55).clamp(0.0, 1.0);
        scale = 1.0 - t * 0.55; // shrinks as it moves further while inverted
        inverted = true;
      }
    } else {
      scale = 1.0 - distance * 0.35; // always diminished, shrinks slightly with distance
      inverted = false;
    }

    final imageX = w * 0.74;
    final imagePaint = Paint()
      ..color = const Color(0xFFD9622A)
      ..strokeWidth = 3
      ..strokeCap = StrokeCap.round;
    _drawArrow(canvas, Offset(imageX, centerY), objectHeight * scale, imagePaint, pointingUp: !inverted);
  }

  void _drawArrow(Canvas canvas, Offset base, double length, Paint paint, {required bool pointingUp}) {
    final tip = pointingUp ? base.translate(0, -length) : base.translate(0, length);
    canvas.drawLine(base, tip, paint);
    final dir = pointingUp ? -1.0 : 1.0;
    canvas.drawLine(tip, tip.translate(-6, -6 * dir), paint);
    canvas.drawLine(tip, tip.translate(6, -6 * dir), paint);
  }

  @override
  bool shouldRepaint(covariant _OpticsPainter oldDelegate) => oldDelegate.type != type || oldDelegate.distance != distance;
}
