import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Hydrocarbon {
  final String name;
  final String formula;
  final int bondType; // 1 = single, 2 = double, 3 = triple
  final String note;

  const _Hydrocarbon(this.name, this.formula, this.bondType, this.note);
}

/// A carbon-chain builder: pick single, double, or triple bonds and see
/// the chain redraw with the correct number of hydrogens, tying bond
/// type to alkane/alkene/alkyne naming.
class CarbonCompoundsSimulationWidget extends StatefulWidget {
  const CarbonCompoundsSimulationWidget({super.key});

  @override
  State<CarbonCompoundsSimulationWidget> createState() => _CarbonCompoundsSimulationWidgetState();
}

class _CarbonCompoundsSimulationWidgetState extends State<CarbonCompoundsSimulationWidget> {
  static const _options = [
    _Hydrocarbon('Ethane (Alkane)', 'C₂H₆', 1, 'Saturated — a single bond between carbons, each carbon bonded to 3 hydrogens.'),
    _Hydrocarbon('Ethene (Alkene)', 'C₂H₄', 2, 'Unsaturated — a double bond between carbons, each carbon bonded to 2 hydrogens.'),
    _Hydrocarbon('Ethyne (Alkyne)', 'C₂H₂', 3, 'Unsaturated — a triple bond between carbons, each carbon bonded to only 1 hydrogen.'),
  ];

  _Hydrocarbon _selected = _options[0];

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Carbon Bonding: Alkanes, Alkenes, Alkynes',
      icon: Icons.hub,
      accent: Colors.grey.shade800,
      description: 'The number of bonds between two carbon atoms determines how many hydrogens can attach, and the compound\'s name.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 150,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.grey.shade100, borderRadius: BorderRadius.circular(10)),
            child: CustomPaint(
              size: Size.infinite,
              painter: _MoleculePainter(bondType: _selected.bondType),
            ),
          ),
          const SizedBox(height: 12),
          SimMetricPanel(metrics: [
            SimMetric(label: 'Formula', value: _selected.formula, color: Colors.deepPurple),
            SimMetric(label: 'Bond Type', value: _selected.bondType == 1 ? 'Single' : (_selected.bondType == 2 ? 'Double' : 'Triple'), color: Colors.teal),
          ]),
          const SizedBox(height: 10),
          Text(_selected.note, style: TextStyle(fontSize: 13)),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            children: _options.map((o) {
              final isSelected = _selected.name == o.name;
              return ChoiceChip(
                label: Text(o.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.grey.shade800,
                backgroundColor: Colors.grey.shade200,
                onSelected: (_) => setState(() => _selected = o),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}

class _MoleculePainter extends CustomPainter {
  final int bondType;

  _MoleculePainter({required this.bondType});

  @override
  void paint(Canvas canvas, Size size) {
    final c1 = Offset(size.width / 2 - 40, size.height / 2);
    final c2 = Offset(size.width / 2 + 40, size.height / 2);
    final bondPaint = Paint()
      ..color = Colors.black87
      ..strokeWidth = 3;

    for (int i = 0; i < bondType; i++) {
      final offset = (i - (bondType - 1) / 2) * 6.0;
      canvas.drawLine(c1 + Offset(0, offset), c2 + Offset(0, offset), bondPaint);
    }

    canvas.drawCircle(c1, 18, Paint()..color = Colors.grey.shade800);
    canvas.drawCircle(c2, 18, Paint()..color = Colors.grey.shade800);

    final hydrogensPerCarbon = 3 - bondType + 1;
    _drawHydrogens(canvas, c1, hydrogensPerCarbon, true);
    _drawHydrogens(canvas, c2, hydrogensPerCarbon, false);
  }

  void _drawHydrogens(Canvas canvas, Offset center, int count, bool leftSide) {
    final hPaint = Paint()..color = Colors.blue.shade300;
    final positions = <Offset>[];
    if (count >= 1) positions.add(center + Offset(leftSide ? -35 : 35, -20));
    if (count >= 2) positions.add(center + Offset(leftSide ? -35 : 35, 20));
    if (count >= 3) positions.add(center + Offset(0, leftSide ? -35 : 35));
    for (final p in positions) {
      canvas.drawLine(center, p, Paint()..color = Colors.black45..strokeWidth = 1.5);
      canvas.drawCircle(p, 10, hPaint);
    }
  }

  @override
  bool shouldRepaint(covariant _MoleculePainter oldDelegate) => oldDelegate.bondType != bondType;
}
