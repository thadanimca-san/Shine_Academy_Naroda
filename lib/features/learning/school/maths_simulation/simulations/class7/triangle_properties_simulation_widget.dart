import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Two angle sliders (the third computes itself to keep the sum at
/// 180°) with the triangle easing smoothly to its new shape, plus a
/// Pythagoras leg-length demo where squares animate onto each side and
/// grow to their true areas, making a² + b² = c² visible rather than
/// just computed.
class TrianglePropertiesSimulationWidget extends StatefulWidget {
  const TrianglePropertiesSimulationWidget({super.key});

  @override
  State<TrianglePropertiesSimulationWidget> createState() => _TrianglePropertiesSimulationWidgetState();
}

class _TrianglePropertiesSimulationWidgetState extends State<TrianglePropertiesSimulationWidget> with SingleTickerProviderStateMixin {
  double _angleA = 60;
  double _angleB = 70;
  double _legA = 3;
  double _legB = 4;
  bool _showPythagoras = false;

  double _prevAngleA = 60, _prevAngleB = 70;
  double _prevLegA = 3, _prevLegB = 4;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 450));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final angleC = 180 - _angleA - _angleB;
    final hypotenuse = _showPythagoras ? _pyth(_legA, _legB) : 0.0;

    return SimFrame(
      title: 'Triangle Angle Sum & Pythagoras',
      icon: Icons.change_history,
      accent: Colors.green.shade700,
      description: 'The three angles of a triangle always sum to 180°. Toggle to explore the Pythagoras property for right triangles.',
      actions: [
        ToggleButtons(
          isSelected: [!_showPythagoras, _showPythagoras],
          onPressed: (i) => setState(() {
            _showPythagoras = i == 1;
            _controller.value = 1;
          }),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.green.shade700,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 60),
          children: [Text(TrilingualService.instance.getUIText('Angle Sum')), Text(TrilingualService.instance.getUIText('Pythagoras'))],
        ),
      ],
      child: _showPythagoras ? _buildPythagoras(hypotenuse) : _buildAngleSum(angleC),
    );
  }

  double _pyth(double a, double b) => (a * a + b * b) > 0 ? (a * a + b * b) : 0;

  Widget _buildAngleSum(double angleC) {
    final valid = angleC > 0;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          height: 130,
          width: double.infinity,
          decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(10)),
          child: AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              final eased = Curves.easeInOut.transform(_controller.value);
              final animA = _prevAngleA + (_angleA - _prevAngleA) * eased;
              final animB = _prevAngleB + (_angleB - _prevAngleB) * eased;
              return CustomPaint(size: Size.infinite, painter: _TrianglePainter(angleA: animA, angleB: animB));
            },
          ),
        ),
        const SizedBox(height: 12),
        SimMetricPanel(metrics: [
          SimMetric(label: 'Angle A', value: '${_angleA.toStringAsFixed(0)}°'),
          SimMetric(label: 'Angle B', value: '${_angleB.toStringAsFixed(0)}°'),
          SimMetric(label: 'Angle C', value: valid ? '${angleC.toStringAsFixed(0)}°' : 'Invalid', color: valid ? Colors.green : Colors.red),
        ]),
        const SizedBox(height: 14),
        SimSlider(label: 'Angle A: ${_angleA.toStringAsFixed(0)}°', value: _angleA, min: 10, max: 150, divisions: 28, activeColor: Colors.green, onChanged: (v) => setState(() {
          _prevAngleA = _angleA;
          _prevAngleB = _angleB;
          _angleA = v;
          _controller.forward(from: 0);
        })),
        SimSlider(label: 'Angle B: ${_angleB.toStringAsFixed(0)}°', value: _angleB, min: 10, max: 150, divisions: 28, activeColor: Colors.teal, onChanged: (v) => setState(() {
          _prevAngleA = _angleA;
          _prevAngleB = _angleB;
          _angleB = v;
          _controller.forward(from: 0);
        })),
      ],
    );
  }

  Widget _buildPythagoras(double hypSquared) {
    final hyp = hypSquared > 0 ? hypSquared : 0.0;
    final hypVal = hyp > 0 ? mathSqrt(hyp) : 0.0;
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Container(
          height: 190,
          width: double.infinity,
          decoration: BoxDecoration(color: Colors.green.shade50, borderRadius: BorderRadius.circular(10)),
          child: AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              final eased = Curves.easeOutBack.transform(_controller.value);
              final animBase = _prevLegA + (_legA - _prevLegA) * eased;
              final animHeight = _prevLegB + (_legB - _prevLegB) * eased;
              return CustomPaint(size: Size.infinite, painter: _RightTrianglePainter(base: animBase, height: animHeight, squareT: eased));
            },
          ),
        ),
        const SizedBox(height: 12),
        SimMetricPanel(metrics: [
          SimMetric(label: 'Base', value: '${_legA.toStringAsFixed(1)} cm'),
          SimMetric(label: 'Height', value: '${_legB.toStringAsFixed(1)} cm'),
          SimMetric(label: 'Hypotenuse', value: '${hypVal.toStringAsFixed(2)} cm', color: Colors.deepOrange),
        ]),
        const SizedBox(height: 14),
        SimSlider(label: 'Base: ${_legA.toStringAsFixed(1)} cm', value: _legA, min: 1, max: 10, divisions: 18, activeColor: Colors.green, onChanged: (v) => setState(() {
          _prevLegA = _legA;
          _prevLegB = _legB;
          _legA = v;
          _controller.forward(from: 0);
        })),
        SimSlider(label: 'Height: ${_legB.toStringAsFixed(1)} cm', value: _legB, min: 1, max: 10, divisions: 18, activeColor: Colors.teal, onChanged: (v) => setState(() {
          _prevLegA = _legA;
          _prevLegB = _legB;
          _legB = v;
          _controller.forward(from: 0);
        })),
      ],
    );
  }
}

double mathSqrt(double v) {
  double x = v;
  double guess = v / 2 == 0 ? 1 : v / 2;
  for (int i = 0; i < 20; i++) {
    guess = 0.5 * (guess + x / guess);
  }
  return guess;
}

class _TrianglePainter extends CustomPainter {
  final double angleA, angleB;
  _TrianglePainter({required this.angleA, required this.angleB});

  @override
  void paint(Canvas canvas, Size size) {
    final base = Offset(size.width * 0.2, size.height * 0.8);
    final baseEnd = Offset(size.width * 0.8, size.height * 0.8);
    final apexFrac = (angleA / (angleA + angleB + 40)).clamp(0.2, 0.8);
    final apex = Offset(size.width * apexFrac, size.height * 0.15);
    final path = Path()
      ..moveTo(base.dx, base.dy)
      ..lineTo(baseEnd.dx, baseEnd.dy)
      ..lineTo(apex.dx, apex.dy)
      ..close();
    canvas.drawPath(path, Paint()..color = Colors.green.shade200..style = PaintingStyle.fill);
    canvas.drawPath(path, Paint()..color = Colors.green.shade800..style = PaintingStyle.stroke..strokeWidth = 2);
  }

  @override
  bool shouldRepaint(covariant _TrianglePainter oldDelegate) => oldDelegate.angleA != angleA || oldDelegate.angleB != angleB;
}

class _RightTrianglePainter extends CustomPainter {
  final double base, height;
  final double squareT; // 0..1, how grown-in the Pythagoras squares on each side are

  _RightTrianglePainter({required this.base, required this.height, this.squareT = 1});

  @override
  void paint(Canvas canvas, Size size) {
    final scale = 12.0;
    final origin = Offset(40, size.height - 30);
    final right = origin + Offset(base * scale, 0);
    final top = origin - Offset(0, height * scale);

    final path = Path()
      ..moveTo(origin.dx, origin.dy)
      ..lineTo(right.dx, right.dy)
      ..lineTo(top.dx, top.dy)
      ..close();

    // Square on the base, extending downward, scaling in from the shared edge.
    final baseVec = right - origin;
    final baseDown = Offset(0, baseVec.distance) * squareT;
    final baseSquare = Path()
      ..moveTo(origin.dx, origin.dy)
      ..lineTo(right.dx, right.dy)
      ..lineTo(right.dx + baseDown.dx, right.dy + baseDown.dy)
      ..lineTo(origin.dx + baseDown.dx, origin.dy + baseDown.dy)
      ..close();
    canvas.drawPath(baseSquare, Paint()..color = Colors.blue.withValues(alpha: 0.25 * squareT));
    canvas.drawPath(baseSquare, Paint()..color = Colors.blue.shade700.withValues(alpha: squareT)..style = PaintingStyle.stroke..strokeWidth = 1.5);

    // Square on the height, extending leftward.
    final heightVec = origin - top;
    final heightLeft = Offset(-heightVec.distance, 0) * squareT;
    final heightSquare = Path()
      ..moveTo(top.dx, top.dy)
      ..lineTo(origin.dx, origin.dy)
      ..lineTo(origin.dx + heightLeft.dx, origin.dy + heightLeft.dy)
      ..lineTo(top.dx + heightLeft.dx, top.dy + heightLeft.dy)
      ..close();
    canvas.drawPath(heightSquare, Paint()..color = Colors.orange.withValues(alpha: 0.25 * squareT));
    canvas.drawPath(heightSquare, Paint()..color = Colors.orange.shade700.withValues(alpha: squareT)..style = PaintingStyle.stroke..strokeWidth = 1.5);

    // Square on the hypotenuse, built outward on the far side from the right angle.
    final hypVec = top - right;
    final hypLen = hypVec.distance;
    if (hypLen > 0) {
      final unit = hypVec / hypLen;
      final normal = Offset(-unit.dy, unit.dx) * hypLen * squareT;
      final hypSquare = Path()
        ..moveTo(right.dx, right.dy)
        ..lineTo(top.dx, top.dy)
        ..lineTo(top.dx + normal.dx, top.dy + normal.dy)
        ..lineTo(right.dx + normal.dx, right.dy + normal.dy)
        ..close();
      canvas.drawPath(hypSquare, Paint()..color = Colors.deepOrange.withValues(alpha: 0.2 * squareT));
      canvas.drawPath(hypSquare, Paint()..color = Colors.deepOrange.withValues(alpha: squareT)..style = PaintingStyle.stroke..strokeWidth = 1.5);
    }

    canvas.drawPath(path, Paint()..color = Colors.teal.shade200);
    canvas.drawPath(path, Paint()..color = Colors.teal.shade800..style = PaintingStyle.stroke..strokeWidth = 2);
    canvas.drawRect(Rect.fromLTWH(origin.dx, origin.dy - 10, 10, 10), Paint()..color = Colors.black45..style = PaintingStyle.stroke);
  }

  @override
  bool shouldRepaint(covariant _RightTrianglePainter oldDelegate) =>
      oldDelegate.base != base || oldDelegate.height != height || oldDelegate.squareT != squareT;
}
