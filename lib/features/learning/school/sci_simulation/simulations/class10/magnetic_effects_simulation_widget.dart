import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

/// Concentric magnetic field rings around a current-carrying wire that
/// grow denser (and reverse direction) as the current slider changes —
/// a direct visual for the right-hand thumb rule.
class MagneticEffectsSimulationWidget extends StatefulWidget {
  const MagneticEffectsSimulationWidget({super.key});

  @override
  State<MagneticEffectsSimulationWidget> createState() => _MagneticEffectsSimulationWidgetState();
}

class _MagneticEffectsSimulationWidgetState extends State<MagneticEffectsSimulationWidget> {
  double _current = 5; // -10 to 10, sign = direction

  @override
  Widget build(BuildContext context) {
    final isUpward = _current >= 0;
    final magnitude = _current.abs();

    return SimFrame(
      title: 'Magnetic Field Around a Current-Carrying Wire',
      icon: Icons.blur_circular,
      accent: Colors.deepPurple.shade400,
      description: 'The magnetic field forms concentric circles around a wire; its direction depends on current direction (right-hand thumb rule) and its strength on current magnitude.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 170,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.deepPurple.shade900, borderRadius: BorderRadius.circular(10)),
            child: CustomPaint(
              size: Size.infinite,
              painter: _FieldPainter(magnitude: magnitude, isUpward: isUpward),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Current', value: '${_current.toStringAsFixed(1)} A', color: Colors.deepPurple),
            SimMetric(label: 'Direction', value: isUpward ? 'Out of page' : 'Into page', color: Colors.teal),
          ]),
          const SizedBox(height: 14),
          SimSlider(
            label: 'Current (negative reverses direction): ${_current.toStringAsFixed(1)} A',
            value: _current,
            min: -10,
            max: 10,
            divisions: 40,
            activeColor: Colors.deepPurple,
            onChanged: (val) => setState(() => _current = val),
          ),
        ],
      ),
    );
  }
}

class _FieldPainter extends CustomPainter {
  final double magnitude;
  final bool isUpward;

  _FieldPainter({required this.magnitude, required this.isUpward});

  @override
  void paint(Canvas canvas, Size size) {
    final center = Offset(size.width / 2, size.height / 2);
    canvas.drawCircle(center, 8, Paint()..color = Colors.white);

    final ringCount = 2 + (magnitude / 2).round();
    for (int i = 1; i <= ringCount.clamp(1, 6); i++) {
      final radius = i * 18.0;
      canvas.drawCircle(
        center,
        radius,
        Paint()
          ..color = Colors.tealAccent.withValues(alpha: (1 - i / 7).clamp(0.2, 1.0))
          ..style = PaintingStyle.stroke
          ..strokeWidth = 1.5,
      );
      // arrow marker on the ring, direction indicates field rotation
      final angle = isUpward ? -0.4 : 0.4 + 3.14159;
      final arrowPos = center + Offset(radius * 0.0, -radius) ;
      final tangentAngle = angle;
      canvas.save();
      canvas.translate(arrowPos.dx, arrowPos.dy);
      canvas.rotate(tangentAngle);
      final path = Path()..moveTo(-4, -4)..lineTo(0, 4)..lineTo(4, -4);
      canvas.drawPath(path, Paint()..color = Colors.white..style = PaintingStyle.stroke..strokeWidth = 1.5);
      canvas.restore();
    }
  }

  @override
  bool shouldRepaint(covariant _FieldPainter oldDelegate) => true;
}
