import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

enum _MicrobePattern { rod, spiral, spherical, branchedFilament, irregularBlob, sacCluster }

class _Microbe {
  final String name;
  final String group;
  final String role;
  final Color color;
  final _MicrobePattern pattern;
  const _Microbe(this.name, this.group, this.role, this.color, this.pattern);
}

const _microbes = [
  _Microbe('Rhizobium', 'Bacteria', 'Lives in legume root nodules and fixes nitrogen from the air, enriching soil naturally.', Color(0xFF6B9E5C), _MicrobePattern.rod),
  _Microbe('Lactobacillus', 'Bacteria', 'Turns milk into curd by producing lactic acid; also helps ferment idli/dosa batter.', Color(0xFF4A8B6F), _MicrobePattern.spiral),
  _Microbe('Yeast', 'Fungi', 'A unicellular fungus that releases CO₂ during respiration, making bread dough soft and fluffy.', Color(0xFFB08D3D), _MicrobePattern.sacCluster),
  _Microbe('Bread Mould', 'Fungi', 'A multicellular fungus with branched filaments; grows on spoiled bread/fruit, helps decomposition.', Color(0xFF8D6E63), _MicrobePattern.branchedFilament),
  _Microbe('Amoeba', 'Protozoa', 'A unicellular organism with an irregular, ever-changing shape, found in pond water.', Color(0xFF3F6A9C), _MicrobePattern.irregularBlob),
  _Microbe('Paramecium', 'Protozoa', 'A unicellular organism that moves using tiny hair-like structures called cilia.', Color(0xFF5B84B1), _MicrobePattern.irregularBlob),
  _Microbe('Spirulina', 'Algae', 'A microalga rich in protein and vitamin B12; produces oxygen and is farmed as a "superfood".', Color(0xFF2E9E5B), _MicrobePattern.spiral),
  _Microbe('Chlorella', 'Algae', 'A single-celled green microalga that photosynthesises and helps purify water.', Color(0xFF2A8C4A), _MicrobePattern.spherical),
];

/// A tap-to-explore microscope view of common microorganisms, grouped by
/// type (bacteria/fungi/protozoa/algae), each drawn with a distinct
/// schematic shape so students learn to visually tell them apart — mirrors
/// the "identify the microorganism" tables in the chapter.
class MicrobeExplorerSimulationWidget extends StatefulWidget {
  const MicrobeExplorerSimulationWidget({super.key});

  @override
  State<MicrobeExplorerSimulationWidget> createState() => _MicrobeExplorerSimulationWidgetState();
}

class _MicrobeExplorerSimulationWidgetState extends State<MicrobeExplorerSimulationWidget> {
  _Microbe _selected = _microbes[0];

  @override
  Widget build(BuildContext context) {
    final groups = {'Bacteria', 'Fungi', 'Protozoa', 'Algae'};
    return SimFrame(
      title: 'Microorganism Explorer',
      icon: Icons.biotech,
      accent: const Color(0xFF4A8B6F),
      description: 'Tap a microbe to see its shape under the "microscope" and what it does.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 150,
            width: double.infinity,
            decoration: BoxDecoration(color: Theme.of(context).colorScheme.onSurface, borderRadius: BorderRadius.circular(16)),
            clipBehavior: Clip.antiAlias,
            child: CustomPaint(
              size: Size.infinite,
              painter: _MicrobePainter(pattern: _selected.pattern, color: _selected.color),
            ),
          ),
          const SizedBox(height: 12),
          for (final group in groups) ...[
            Text(group, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant)),
            const SizedBox(height: 6),
            Wrap(
              spacing: 6,
              runSpacing: 6,
              children: _microbes.where((m) => m.group == group).map((m) {
                final isSelected = _selected.name == m.name;
                return ChoiceChip(
                  label: Text(m.name, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
                  selected: isSelected,
                  selectedColor: m.color,
                  backgroundColor: m.color.withValues(alpha: 0.18),
                  onSelected: (_) => setState(() => _selected = m),
                );
              }).toList(),
            ),
            const SizedBox(height: 8),
          ],
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text('${_selected.name}  ·  ${_selected.group}', style: TextStyle(fontWeight: FontWeight.bold, color: _selected.color, fontSize: 14)),
                const SizedBox(height: 4),
                Text(_selected.role, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}

class _MicrobePainter extends CustomPainter {
  final _MicrobePattern pattern;
  final Color color;
  _MicrobePainter({required this.pattern, required this.color});

  @override
  void paint(Canvas canvas, Size size) {
    final fill = Paint()..color = color.withValues(alpha: 0.85);
    final stroke = Paint()
      ..color = Colors.white.withValues(alpha: 0.4)
      ..style = PaintingStyle.stroke
      ..strokeWidth = 1.2;

    switch (pattern) {
      case _MicrobePattern.rod:
        for (int i = 0; i < 6; i++) {
          final x = 20.0 + i * 40;
          final y = size.height / 2 + (i.isEven ? -8 : 8);
          final rect = Rect.fromCenter(center: Offset(x, y), width: 34, height: 12);
          canvas.drawRRect(RRect.fromRectAndRadius(rect, const Radius.circular(6)), fill);
          canvas.drawRRect(RRect.fromRectAndRadius(rect, const Radius.circular(6)), stroke);
        }
        break;
      case _MicrobePattern.spiral:
        for (int i = 0; i < 5; i++) {
          final cx = 30.0 + i * 45;
          final path = Path();
          for (double a = 0; a <= 4 * 3.14159; a += 0.2) {
            final r = 3 + a * 1.4;
            final x = cx + r * (a.remainder(6.28) < 3.14 ? 1 : -1) * 0.4 * (a / 12);
            final y = size.height / 2 + r * (a % 2 == 0 ? 1 : -1) * 0.3;
            if (a == 0) {
              path.moveTo(x, y);
            } else {
              path.lineTo(x, y);
            }
          }
          canvas.drawPath(path, Paint()
            ..color = color
            ..style = PaintingStyle.stroke
            ..strokeWidth = 3
            ..strokeCap = StrokeCap.round);
        }
        break;
      case _MicrobePattern.spherical:
        final rnd = [20.0, 60, 100, 140, 180, 220, 40, 80, 120, 160, 200];
        for (int i = 0; i < rnd.length; i++) {
          final cx = rnd[i] % size.width;
          final cy = (rnd[(i * 3) % rnd.length] * 0.6) % size.height;
          canvas.drawCircle(Offset(cx, cy), 9, fill);
          canvas.drawCircle(Offset(cx, cy), 9, stroke);
        }
        break;
      case _MicrobePattern.branchedFilament:
        final branchPaint = Paint()
          ..color = color
          ..strokeWidth = 2.4
          ..strokeCap = StrokeCap.round;
        final bases = [Offset(size.width * 0.2, size.height * 0.85), Offset(size.width * 0.55, size.height * 0.85), Offset(size.width * 0.85, size.height * 0.85)];
        for (final base in bases) {
          canvas.drawLine(base, base - const Offset(0, 40), branchPaint);
          for (int i = 0; i < 4; i++) {
            final tip = base - Offset((i - 1.5) * 10, 40 + i * 4);
            canvas.drawLine(base - const Offset(0, 40), tip, branchPaint);
            canvas.drawCircle(tip, 5, fill);
          }
        }
        break;
      case _MicrobePattern.irregularBlob:
        final path = Path()..moveTo(size.width * 0.3, size.height * 0.3);
        final pts = [
          Offset(size.width * 0.55, size.height * 0.2),
          Offset(size.width * 0.7, size.height * 0.4),
          Offset(size.width * 0.65, size.height * 0.65),
          Offset(size.width * 0.45, size.height * 0.75),
          Offset(size.width * 0.25, size.height * 0.6),
          Offset(size.width * 0.2, size.height * 0.4),
        ];
        for (final p in pts) {
          path.lineTo(p.dx, p.dy);
        }
        path.close();
        canvas.drawPath(path, fill);
        canvas.drawPath(path, stroke);
        canvas.drawCircle(Offset(size.width * 0.45, size.height * 0.48), 8, Paint()..color = Colors.white.withValues(alpha: 0.7));
        break;
      case _MicrobePattern.sacCluster:
        for (int i = 0; i < 8; i++) {
          final cx = 25.0 + (i % 4) * 60;
          final cy = size.height * 0.3 + (i ~/ 4) * (size.height * 0.4);
          canvas.drawOval(Rect.fromCenter(center: Offset(cx, cy), width: 26, height: 20), fill);
          canvas.drawOval(Rect.fromCenter(center: Offset(cx, cy), width: 26, height: 20), stroke);
          canvas.drawOval(Rect.fromCenter(center: Offset(cx + 14, cy - 6), width: 14, height: 11), fill);
        }
        break;
    }
  }

  @override
  bool shouldRepaint(covariant _MicrobePainter oldDelegate) => oldDelegate.pattern != pattern || oldDelegate.color != color;
}
