import 'package:flutter/material.dart';
import 'common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

enum _TissuePattern { brickRows, elongatedFibres, scatteredCells, branchedNetwork, denseCluster }

class _Tissue {
  final String name;
  final String category; // Plant / Animal
  final String description;
  final Color color;
  final _TissuePattern pattern;

  const _Tissue(this.name, this.category, this.description, this.color, this.pattern);
}

/// A tap-to-explore microscope view of plant and animal tissue types.
/// Each tissue gets a distinct schematic cell-pattern so students learn to
/// visually tell, say, muscle fibres from epithelial sheets.
class TissuesSimulationWidget extends StatefulWidget {
  const TissuesSimulationWidget({super.key});

  @override
  State<TissuesSimulationWidget> createState() => _TissuesSimulationWidgetState();
}

class _TissuesSimulationWidgetState extends State<TissuesSimulationWidget> {
  static const _tissues = [
    _Tissue('Meristematic', 'Plant', 'Actively dividing cells found at root and shoot tips, responsible for plant growth.', Color(0xFF66BB6A), _TissuePattern.denseCluster),
    _Tissue('Permanent (Simple)', 'Plant', 'Cells that have lost the ability to divide and are specialised, e.g. parenchyma, collenchyma, sclerenchyma.', Color(0xFF9CCC65), _TissuePattern.brickRows),
    _Tissue('Vascular (Xylem/Phloem)', 'Plant', 'Complex tissue that transports water (xylem) and food (phloem) throughout the plant.', Color(0xFF43A047), _TissuePattern.elongatedFibres),
    _Tissue('Epithelial', 'Animal', 'Thin, tightly packed sheets of cells that cover body surfaces and line organs.', Color(0xFF42A5F5), _TissuePattern.brickRows),
    _Tissue('Connective', 'Animal', 'Cells scattered in a matrix; binds and supports other tissues, e.g. bone, blood, cartilage.', Color(0xFFFFA726), _TissuePattern.scatteredCells),
    _Tissue('Muscular', 'Animal', 'Long, contractile fibres that enable body movement.', Color(0xFFEF5350), _TissuePattern.elongatedFibres),
    _Tissue('Nervous', 'Animal', 'Branched neurons that carry electrical impulses to communicate across the body.', Color(0xFF7E57C2), _TissuePattern.branchedNetwork),
  ];

  _Tissue _selected = _tissues[0];

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Tissue Explorer',
      icon: Icons.biotech,
      accent: Colors.deepPurple,
      description: 'Tap a tissue type to see its schematic cell pattern under the "microscope" and what it does.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 160,
            width: double.infinity,
            decoration: BoxDecoration(color: Theme.of(context).colorScheme.onSurface, borderRadius: BorderRadius.circular(70)),
            clipBehavior: Clip.antiAlias,
            child: CustomPaint(
              size: Size.infinite,
              painter: _TissuePainter(pattern: _selected.pattern, color: _selected.color),
            ),
          ),
          const SizedBox(height: 12),
          Text(TrilingualService.instance.getUIText('Plant Tissues'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
          const SizedBox(height: 6),
          _buildChipRow('Plant'),
          const SizedBox(height: 10),
          Text(TrilingualService.instance.getUIText('Animal Tissues'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
          const SizedBox(height: 6),
          _buildChipRow('Animal'),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(_selected.name, style: TextStyle(fontWeight: FontWeight.bold, color: _selected.color, fontSize: 14)),
                const SizedBox(height: 4),
                Text(_selected.description, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildChipRow(String category) {
    return Wrap(
      spacing: 6,
      runSpacing: 6,
      children: _tissues.where((t) => t.category == category).map((t) {
        final isSelected = _selected.name == t.name;
        return ChoiceChip(
          label: Text(t.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
          selected: isSelected,
          selectedColor: t.color,
          backgroundColor: t.color.withValues(alpha: 0.18),
          onSelected: (_) => setState(() => _selected = t),
        );
      }).toList(),
    );
  }
}

class _TissuePainter extends CustomPainter {
  final _TissuePattern pattern;
  final Color color;

  _TissuePainter({required this.pattern, required this.color});

  @override
  void paint(Canvas canvas, Size size) {
    final fill = Paint()..color = color.withValues(alpha: 0.85);
    final stroke = Paint()
      ..color = Colors.black54
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1;

    switch (pattern) {
      case _TissuePattern.brickRows:
        const rows = 5;
        final rowH = size.height / rows;
        for (int r = 0; r < rows; r++) {
          final offset = (r.isEven) ? 0.0 : 20.0;
          double x = -20 + offset;
          while (x < size.width) {
            final rect = Rect.fromLTWH(x, r * rowH, 38, rowH - 3);
            canvas.drawRect(rect, fill);
            canvas.drawRect(rect, stroke);
            x += 40;
          }
        }
        break;
      case _TissuePattern.elongatedFibres:
        for (int i = 0; i < 8; i++) {
          final y = 10.0 + i * (size.height - 20) / 7;
          final rect = Rect.fromLTWH(0, y, size.width, 10);
          canvas.drawRRect(RRect.fromRectAndRadius(rect, const Radius.circular(5)), fill);
          canvas.drawRRect(RRect.fromRectAndRadius(rect, const Radius.circular(5)), stroke);
        }
        break;
      case _TissuePattern.scatteredCells:
        final rnd = [12.0, 40, 70, 100, 130, 160, 25, 55, 85, 115, 145, 175, 8, 38, 68, 98, 128, 158];
        for (int i = 0; i < 16; i++) {
          final cx = (rnd[i % rnd.length] * 2) % size.width;
          final cy = (rnd[(i * 3) % rnd.length] * 0.8) % size.height;
          canvas.drawCircle(Offset(cx, cy), 8, fill);
          canvas.drawCircle(Offset(cx, cy), 8, stroke);
        }
        break;
      case _TissuePattern.branchedNetwork:
        final centers = [Offset(size.width * 0.2, size.height * 0.3), Offset(size.width * 0.6, size.height * 0.25), Offset(size.width * 0.4, size.height * 0.7), Offset(size.width * 0.85, size.height * 0.65)];
        final branchPaint = Paint()
          ..color = color
          ..strokeWidth = 2;
        for (final c in centers) {
          canvas.drawCircle(c, 10, fill);
          for (int i = 0; i < 5; i++) {
            final angle = i * 1.3;
            final end = c + Offset(30 * (i.isEven ? 1 : -1) * (0.5 + i * 0.1), 25 * (angle % 2 == 0 ? 1 : -1) * 0.6);
            canvas.drawLine(c, end, branchPaint);
          }
        }
        break;
      case _TissuePattern.denseCluster:
        for (int r = 0; r < 6; r++) {
          for (int c = 0; c < 9; c++) {
            final cx = 10.0 + c * (size.width - 20) / 8;
            final cy = 10.0 + r * (size.height - 20) / 5;
            canvas.drawRect(Rect.fromCenter(center: Offset(cx, cy), width: 14, height: 14), fill);
            canvas.drawRect(Rect.fromCenter(center: Offset(cx, cy), width: 14, height: 14), stroke);
          }
        }
        break;
    }
  }

  @override
  bool shouldRepaint(covariant _TissuePainter oldDelegate) => oldDelegate.pattern != pattern || oldDelegate.color != color;
}
