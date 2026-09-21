import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Toggle between a normal eye, myopia (image forms before the retina),
/// and hypermetropia (image forms behind the retina) — then switch on the
/// corrective lens to see the image snap back onto the retina.
class HumanEyeSimulationWidget extends StatefulWidget {
  const HumanEyeSimulationWidget({super.key});

  @override
  State<HumanEyeSimulationWidget> createState() => _HumanEyeSimulationWidgetState();
}

enum _EyeCondition { normal, myopia, hypermetropia }

class _HumanEyeSimulationWidgetState extends State<HumanEyeSimulationWidget> {
  _EyeCondition _condition = _EyeCondition.myopia;
  bool _correctionOn = false;

  @override
  Widget build(BuildContext context) {
    final focusOffset = _condition == _EyeCondition.normal
        ? 0.0
        : (_correctionOn ? 0.0 : (_condition == _EyeCondition.myopia ? -18.0 : 18.0));

    return SimFrame(
      title: 'Eye Defects & Correction',
      icon: Icons.visibility,
      accent: Colors.blue.shade700,
      description: 'See where the image forms relative to the retina for each eye condition, then switch on the corrective lens.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 150,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.blue.shade50, borderRadius: BorderRadius.circular(10)),
            child: CustomPaint(
              size: Size.infinite,
              painter: _EyePainter(focusOffset: focusOffset, showCorrection: _correctionOn && _condition != _EyeCondition.normal, isMyopia: _condition == _EyeCondition.myopia),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Condition', value: _conditionName, color: Colors.blue),
            SimMetric(label: 'Image Focus', value: focusOffset == 0 ? 'On retina' : (focusOffset < 0 ? 'Before retina' : 'Behind retina'), color: focusOffset == 0 ? Colors.green : Colors.red),
          ]),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            children: [
              ChoiceChip(label: Text(TrilingualService.instance.getUIText('Normal')), selected: _condition == _EyeCondition.normal, onSelected: (_) => setState(() => _condition = _EyeCondition.normal)),
              ChoiceChip(label: Text(TrilingualService.instance.getUIText('Myopia')), selected: _condition == _EyeCondition.myopia, onSelected: (_) => setState(() => _condition = _EyeCondition.myopia)),
              ChoiceChip(label: Text(TrilingualService.instance.getUIText('Hypermetropia')), selected: _condition == _EyeCondition.hypermetropia, onSelected: (_) => setState(() => _condition = _EyeCondition.hypermetropia)),
            ],
          ),
          const SizedBox(height: 8),
          SwitchListTile(
            contentPadding: EdgeInsets.zero,
            title: Text(_condition == _EyeCondition.myopia ? 'Concave corrective lens' : 'Convex corrective lens', style: TextStyle(fontSize: 13)),
            value: _correctionOn,
            activeColor: Colors.blue,
            onChanged: _condition == _EyeCondition.normal ? null : (val) => setState(() => _correctionOn = val),
          ),
        ],
      ),
    );
  }

  String get _conditionName {
    switch (_condition) {
      case _EyeCondition.normal:
        return 'Normal';
      case _EyeCondition.myopia:
        return 'Myopia';
      case _EyeCondition.hypermetropia:
        return 'Hypermetropia';
    }
  }
}

class _EyePainter extends CustomPainter {
  final double focusOffset;
  final bool showCorrection;
  final bool isMyopia;

  _EyePainter({required this.focusOffset, required this.showCorrection, required this.isMyopia});

  @override
  void paint(Canvas canvas, Size size) {
    final retinaX = size.width - 30;
    final lensX = size.width * 0.4;
    final midY = size.height / 2;

    // eyeball outline
    canvas.drawOval(Rect.fromLTWH(20, 20, size.width - 50, size.height - 40), Paint()..color = Colors.white..style = PaintingStyle.fill);
    canvas.drawOval(Rect.fromLTWH(20, 20, size.width - 50, size.height - 40), Paint()..color = Colors.blue.shade200..style = PaintingStyle.stroke..strokeWidth = 2);
    // retina
    canvas.drawLine(Offset(retinaX, 25), Offset(retinaX, size.height - 25), Paint()..color = Colors.red.shade300..strokeWidth = 3);
    // lens
    canvas.drawOval(Rect.fromCenter(center: Offset(lensX, midY), width: 14, height: 60), Paint()..color = Colors.lightBlue.shade100..style = PaintingStyle.fill);

    // corrective lens
    if (showCorrection) {
      final corrX = lensX - 30;
      canvas.drawLine(Offset(corrX, midY - 35), Offset(corrX, midY + 35), Paint()..color = Colors.deepPurple..strokeWidth = 3);
    }

    // focus point (where rays converge)
    final focusX = retinaX + focusOffset;
    canvas.drawCircle(Offset(focusX, midY), 4, Paint()..color = focusOffset == 0 ? Colors.green : Colors.orange);

    // rays
    final rayPaint = Paint()
      ..color = Colors.orange.withValues(alpha: 0.8)
      ..strokeWidth = 1.5;
    canvas.drawLine(Offset(lensX, midY - 30), Offset(focusX, midY), rayPaint);
    canvas.drawLine(Offset(lensX, midY + 30), Offset(focusX, midY), rayPaint);
    if (focusOffset != 0) {
      canvas.drawLine(Offset(focusX, midY), Offset(retinaX, midY - (focusOffset > 0 ? 15 : -15)), rayPaint);
      canvas.drawLine(Offset(focusX, midY), Offset(retinaX, midY + (focusOffset > 0 ? 15 : -15)), rayPaint);
    }
  }

  @override
  bool shouldRepaint(covariant _EyePainter oldDelegate) => true;
}
