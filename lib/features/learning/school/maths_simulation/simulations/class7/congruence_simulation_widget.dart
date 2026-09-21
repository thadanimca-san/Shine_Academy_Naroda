import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Criterion {
  final String name;
  final String description;

  const _Criterion(this.name, this.description);
}

/// Two side-by-side matching triangles: pick a congruence criterion and
/// see which parts (sides/angles marked with tick or arc symbols) are
/// given as equal to prove congruence. Press play to slide the second
/// triangle over onto the first, showing them settle into a perfect
/// overlay — the visual meaning of "congruent".
class CongruenceSimulationWidget extends StatefulWidget {
  const CongruenceSimulationWidget({super.key});

  @override
  State<CongruenceSimulationWidget> createState() => _CongruenceSimulationWidgetState();
}

class _CongruenceSimulationWidgetState extends State<CongruenceSimulationWidget> with SingleTickerProviderStateMixin {
  static const _criteria = [
    _Criterion('SSS', 'All three sides of one triangle equal all three sides of the other.'),
    _Criterion('SAS', 'Two sides and the angle between them are equal.'),
    _Criterion('ASA', 'Two angles and the side between them are equal.'),
    _Criterion('RHS', 'The hypotenuse and one side of right triangles are equal.'),
  ];

  int _selected = 0;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 900));
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _play() => _controller.forward(from: 0);

  @override
  Widget build(BuildContext context) {
    final criterion = _criteria[_selected];

    return SimFrame(
      title: 'Congruence Criteria',
      icon: Icons.compare,
      accent: Colors.blueGrey.shade700,
      description: 'Tap a criterion, then press play to slide the second triangle onto the first and see them overlay exactly.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 150,
            width: double.infinity,
            decoration: BoxDecoration(color: Colors.blueGrey.shade50, borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                return CustomPaint(size: Size.infinite, painter: _TrianglePairPainter(mode: _selected, overlayT: eased));
              },
            ),
          ),
          const SizedBox(height: 8),
          Align(
            alignment: Alignment.centerLeft,
            child: TextButton.icon(
              onPressed: _play,
              icon: Icon(Icons.play_arrow, size: 18),
              label: Text(TrilingualService.instance.getUIText('Overlay triangles')),
              style: TextButton.styleFrom(foregroundColor: Colors.blueGrey.shade700),
            ),
          ),
          Wrap(
            spacing: 8,
            children: _criteria.asMap().entries.map((e) {
              final isSelected = e.key == _selected;
              return ChoiceChip(
                label: Text(e.value.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.blueGrey.shade700,
                backgroundColor: Colors.blueGrey.shade50,
                onSelected: (_) => setState(() {
                  _selected = e.key;
                  _controller.value = 0;
                }),
              );
            }).toList(),
          ),
          const SizedBox(height: 10),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.blueGrey.shade50, borderRadius: BorderRadius.circular(10)),
            child: Text('${criterion.name}: ${criterion.description}', style: TextStyle(fontSize: 13)),
          ),
        ],
      ),
    );
  }
}

class _TrianglePairPainter extends CustomPainter {
  final int mode; // 0=SSS,1=SAS,2=ASA,3=RHS
  final double overlayT; // 0 = side by side, 1 = fully overlaid on the first triangle

  _TrianglePairPainter({required this.mode, required this.overlayT});

  @override
  void paint(Canvas canvas, Size size) {
    final origin1 = Offset(size.width * 0.05, size.height * 0.85);
    final origin2 = Offset(size.width * 0.55, size.height * 0.85);
    final w = size.width * 0.35;
    final h = size.height * 0.7;

    _drawTriangle(canvas, origin1, w, h, mode, Colors.blueGrey.shade200, Colors.blueGrey.shade800, 1.0);

    // The second triangle slides left to sit exactly on top of the first as overlayT -> 1,
    // and fades so the underlying triangle's outline stays visible through the overlay.
    final slid = Offset.lerp(origin2, origin1, overlayT)!;
    final opacity = 1.0 - 0.35 * overlayT;
    _drawTriangle(canvas, slid, w, h, mode, Colors.deepOrange.shade100.withValues(alpha: opacity), Colors.deepOrange.shade700.withValues(alpha: opacity), opacity);
  }

  void _drawTriangle(Canvas canvas, Offset origin, double w, double h, int mode, Color fill, Color stroke, double opacity) {
    final p1 = origin;
    final p2 = origin + Offset(w, 0);
    final p3 = origin + Offset(w * 0.4, -h);
    final path = Path()
      ..moveTo(p1.dx, p1.dy)
      ..lineTo(p2.dx, p2.dy)
      ..lineTo(p3.dx, p3.dy)
      ..close();
    canvas.drawPath(path, Paint()..color = fill);
    canvas.drawPath(path, Paint()..color = stroke..style = PaintingStyle.stroke..strokeWidth = 2);

    final markPaint = Paint()
      ..color = Colors.red.withValues(alpha: opacity)
      ..strokeWidth = 2;
    void tick(Offset a, Offset b) {
      final mid = Offset((a.dx + b.dx) / 2, (a.dy + b.dy) / 2);
      canvas.drawLine(mid + const Offset(-4, -4), mid + const Offset(4, 4), markPaint);
    }

    if (mode == 0) {
      tick(p1, p2);
      tick(p2, p3);
      tick(p3, p1);
    } else if (mode == 1) {
      tick(p1, p2);
      tick(p3, p1);
      canvas.drawCircle(p1, 10, Paint()..color = markPaint.color..style = PaintingStyle.stroke..strokeWidth = 2);
    } else if (mode == 2) {
      tick(p1, p2);
      canvas.drawCircle(p1, 10, Paint()..color = markPaint.color..style = PaintingStyle.stroke..strokeWidth = 2);
      canvas.drawCircle(p2, 10, Paint()..color = markPaint.color..style = PaintingStyle.stroke..strokeWidth = 2);
    } else {
      tick(p2, p3);
      tick(p1, p2);
    }
  }

  @override
  bool shouldRepaint(covariant _TrianglePairPainter oldDelegate) => oldDelegate.mode != mode || oldDelegate.overlayT != overlayT;
}
