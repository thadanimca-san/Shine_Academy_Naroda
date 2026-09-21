import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// A resistor circuit calculator: toggle series vs parallel wiring for
/// two resistors and see the total resistance and current change live,
/// applying Ohm's law.
class ElectricitySimulationWidget extends StatefulWidget {
  const ElectricitySimulationWidget({super.key});

  @override
  State<ElectricitySimulationWidget> createState() => _ElectricitySimulationWidgetState();
}

class _ElectricitySimulationWidgetState extends State<ElectricitySimulationWidget> {
  bool _isSeries = true;
  double _r1 = 5;
  double _r2 = 10;
  double _voltage = 12;

  @override
  Widget build(BuildContext context) {
    final totalR = _isSeries ? (_r1 + _r2) : (1 / (1 / _r1 + 1 / _r2));
    final current = _voltage / totalR;

    return SimFrame(
      title: 'Series vs Parallel Circuits',
      icon: Icons.electrical_services,
      accent: Colors.amber.shade800,
      description: 'Compare how total resistance and current differ between series and parallel resistor combinations (Ohm\'s Law: V = IR).',
      actions: [
        ToggleButtons(
          isSelected: [_isSeries, !_isSeries],
          onPressed: (i) => setState(() => _isSeries = i == 0),
          borderRadius: BorderRadius.circular(8),
          selectedColor: Colors.white,
          fillColor: Colors.amber.shade800,
          constraints: const BoxConstraints(minHeight: 34, minWidth: 60),
          children: [Text(TrilingualService.instance.getUIText('Series')), Text(TrilingualService.instance.getUIText('Parallel'))],
        ),
      ],
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 110,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.amber.shade50, borderRadius: BorderRadius.circular(10)),
            child: CustomPaint(size: Size.infinite, painter: _CircuitPainter(isSeries: _isSeries)),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Total Resistance', value: '${totalR.toStringAsFixed(1)} Ω', color: Colors.deepOrange),
            SimMetric(label: 'Current', value: '${current.toStringAsFixed(2)} A', color: Colors.blue),
          ]),
          const SizedBox(height: 14),
          SimSlider(label: 'R₁: ${_r1.toStringAsFixed(0)} Ω', value: _r1, min: 1, max: 30, divisions: 29, activeColor: Colors.amber.shade800, onChanged: (v) => setState(() => _r1 = v)),
          SimSlider(label: 'R₂: ${_r2.toStringAsFixed(0)} Ω', value: _r2, min: 1, max: 30, divisions: 29, activeColor: Colors.amber.shade800, onChanged: (v) => setState(() => _r2 = v)),
          SimSlider(label: 'Voltage: ${_voltage.toStringAsFixed(0)} V', value: _voltage, min: 1, max: 24, divisions: 23, activeColor: Colors.blue, onChanged: (v) => setState(() => _voltage = v)),
        ],
      ),
    );
  }
}

class _CircuitPainter extends CustomPainter {
  final bool isSeries;

  _CircuitPainter({required this.isSeries});

  @override
  void paint(Canvas canvas, Size size) {
    final wire = Paint()
      ..color = Colors.black87
      ..strokeWidth = 2;
    final midY = size.height / 2;

    if (isSeries) {
      canvas.drawLine(Offset(20, midY), Offset(size.width - 20, midY), wire);
      _drawResistor(canvas, Offset(size.width * 0.35, midY));
      _drawResistor(canvas, Offset(size.width * 0.65, midY));
    } else {
      canvas.drawLine(Offset(20, midY), Offset(60, midY), wire);
      canvas.drawLine(Offset(60, 25), Offset(60, size.height - 25), wire);
      canvas.drawLine(Offset(size.width - 60, 25), Offset(size.width - 60, size.height - 25), wire);
      canvas.drawLine(Offset(size.width - 60, midY), Offset(size.width - 20, midY), wire);
      _drawResistor(canvas, Offset(60, size.height * 0.3), horizontalWire: Offset(size.width - 60, size.height * 0.3));
      _drawResistor(canvas, Offset(60, size.height * 0.7), horizontalWire: Offset(size.width - 60, size.height * 0.7));
    }
  }

  void _drawResistor(Canvas canvas, Offset center, {Offset? horizontalWire}) {
    final paint = Paint()
      ..color = Colors.amber.shade800
      ..strokeWidth = 3
      ..style = PaintingStyle.stroke;
    if (horizontalWire != null) {
      canvas.drawLine(Offset(center.dx, center.dy), horizontalWire, Paint()..color = Colors.black87..strokeWidth = 2);
      final rectCenter = Offset((center.dx + horizontalWire.dx) / 2, center.dy);
      canvas.drawRect(Rect.fromCenter(center: rectCenter, width: 40, height: 16), paint);
    } else {
      canvas.drawRect(Rect.fromCenter(center: center, width: 16, height: 30), paint);
    }
  }

  @override
  bool shouldRepaint(covariant _CircuitPainter oldDelegate) => oldDelegate.isSeries != isSeries;
}
