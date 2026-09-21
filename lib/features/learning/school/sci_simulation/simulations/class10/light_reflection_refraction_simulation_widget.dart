import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// A convex-lens ray diagram: slide the object distance and see how the
/// image type (real/virtual, magnified/diminished, upright/inverted)
/// changes — the practical outcome of the lens formula.
class LightReflectionRefractionSimulationWidget extends StatefulWidget {
  const LightReflectionRefractionSimulationWidget({super.key});

  @override
  State<LightReflectionRefractionSimulationWidget> createState() => _LightReflectionRefractionSimulationWidgetState();
}

class _LightReflectionRefractionSimulationWidgetState extends State<LightReflectionRefractionSimulationWidget> {
  double _objectDistance = 30; // cm, positive = to the left of lens
  final double _focalLength = 15; // cm

  @override
  Widget build(BuildContext context) {
    // Lens formula: 1/v - 1/u = 1/f  (using u negative by convention, simplified here as magnitudes)
    final u = _objectDistance;
    final f = _focalLength;
    double v;
    String imageType;
    String orientation;
    String sizeDesc;

    if (u == f) {
      v = double.infinity;
      imageType = 'Image forms at infinity';
      orientation = '—';
      sizeDesc = 'Highly magnified';
    } else {
      v = (f * u) / (u - f);
      final isReal = u > f;
      imageType = isReal ? 'Real' : 'Virtual';
      orientation = isReal ? 'Inverted' : 'Upright';
      final magnitude = v.abs() / u;
      sizeDesc = magnitude > 1.05 ? 'Magnified' : (magnitude < 0.95 ? 'Diminished' : 'Same size');
    }

    return SimFrame(
      title: 'Convex Lens Ray Diagram',
      icon: Icons.center_focus_strong,
      accent: Colors.blue.shade700,
      description: 'Move the object and see how the image formed by a convex lens changes — this is the practical result of the lens formula.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 180,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.blue.shade50, borderRadius: BorderRadius.circular(10)),
            child: CustomPaint(
              size: Size.infinite,
              painter: _LensPainter(objectDistance: _objectDistance, focalLength: f),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Object Distance', value: '${u.toStringAsFixed(0)} cm'),
            SimMetric(label: 'Image', value: imageType, color: Colors.deepPurple),
            SimMetric(label: 'Nature', value: '$orientation, $sizeDesc', color: Colors.teal),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Object distance from lens: ${u.toStringAsFixed(0)} cm (focal length = ${f.toStringAsFixed(0)} cm)',
            value: _objectDistance,
            min: 5,
            max: 60,
            divisions: 55,
            activeColor: Colors.blue,
            onChanged: (val) => setState(() => _objectDistance = val),
          ),
        ],
      ),
    );
  }
}

class _LensPainter extends CustomPainter {
  final double objectDistance;
  final double focalLength;

  _LensPainter({required this.objectDistance, required this.focalLength});

  @override
  void paint(Canvas canvas, Size size) {
    final mid = Offset(size.width / 2, size.height / 2);
    final scale = 3.0;

    // principal axis
    canvas.drawLine(Offset(0, mid.dy), Offset(size.width, mid.dy), Paint()..color = Colors.grey.shade400..strokeWidth = 1);
    // lens
    canvas.drawLine(Offset(mid.dx, 10), Offset(mid.dx, size.height - 10), Paint()..color = Colors.blue.shade700..strokeWidth = 3);
    // focal points
    canvas.drawCircle(Offset(mid.dx - focalLength * scale, mid.dy), 3, Paint()..color = Colors.red);
    canvas.drawCircle(Offset(mid.dx + focalLength * scale, mid.dy), 3, Paint()..color = Colors.red);

    final objX = mid.dx - objectDistance * scale;
    if (objX < 5) return;
    final objTop = Offset(objX, mid.dy - 40);
    canvas.drawLine(Offset(objX, mid.dy), objTop, Paint()..color = Colors.green.shade700..strokeWidth = 2.5);

    // image using lens formula
    final u = objectDistance;
    final f = focalLength;
    if ((u - f).abs() < 0.5) return;
    final v = (f * u) / (u - f);
    final magnification = -v / u;
    final imgX = mid.dx + v * scale;
    final imgY = mid.dy - 40 * magnification;
    if (imgX.isFinite && imgX > 0 && imgX < size.width) {
      canvas.drawLine(Offset(imgX, mid.dy), Offset(imgX, imgY), Paint()..color = Colors.deepOrange..strokeWidth = 2.5);
    }
  }

  @override
  bool shouldRepaint(covariant _LensPainter oldDelegate) => true;
}
