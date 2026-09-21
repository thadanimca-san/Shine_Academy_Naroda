import 'package:flutter/material.dart';
import '../common/sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class _Quad {
  final String name;
  final List<String> properties;
  final Color color;

  const _Quad(this.name, this.properties, this.color);
}

/// A tap-to-explore gallery of quadrilateral types whose schematic shape
/// morphs smoothly from one outline to the next, alongside their defining
/// properties.
class QuadrilateralsSimulationWidget extends StatefulWidget {
  const QuadrilateralsSimulationWidget({super.key});

  @override
  State<QuadrilateralsSimulationWidget> createState() => _QuadrilateralsSimulationWidgetState();
}

class _QuadrilateralsSimulationWidgetState extends State<QuadrilateralsSimulationWidget> with SingleTickerProviderStateMixin {
  static const _quads = [
    _Quad('Parallelogram', ['Opposite sides parallel & equal', 'Opposite angles equal', 'Diagonals bisect each other'], Color(0xFF42A5F5)),
    _Quad('Rectangle', ['All angles 90°', 'Opposite sides equal', 'Diagonals equal & bisect each other'], Color(0xFF66BB6A)),
    _Quad('Rhombus', ['All sides equal', 'Diagonals bisect at 90°', 'Opposite angles equal'], Color(0xFFEF5350)),
    _Quad('Square', ['All sides equal', 'All angles 90°', 'Diagonals equal & perpendicular'], Color(0xFFAB47BC)),
    _Quad('Trapezium', ['Exactly one pair of parallel sides'], Color(0xFFFFA726)),
    _Quad('Kite', ['Two pairs of adjacent equal sides', 'Diagonals perpendicular'], Color(0xFF26A69A)),
  ];

  _Quad _selected = _quads[0];
  _Quad _previous = _quads[0];
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 500));
    _controller.value = 1;
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _select(_Quad q) {
    if (q.name == _selected.name) return;
    setState(() {
      _previous = _selected;
      _selected = q;
      _controller.forward(from: 0);
    });
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Quadrilateral Properties',
      icon: Icons.category,
      accent: Colors.deepPurple.shade400,
      description: 'Tap a quadrilateral to watch it morph into shape and see its defining properties.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            height: 130,
            width: double.infinity,
            decoration: BoxDecoration(color: _selected.color.withValues(alpha: 0.1), borderRadius: BorderRadius.circular(10)),
            child: AnimatedBuilder(
              animation: _controller,
              builder: (context, _) {
                final eased = Curves.easeInOut.transform(_controller.value);
                return CustomPaint(size: Size.infinite, painter: _QuadPainter(fromType: _previous.name, toType: _selected.name, fromColor: _previous.color, toColor: _selected.color, t: eased));
              },
            ),
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _quads.map((q) {
              final isSelected = _selected.name == q.name;
              return ChoiceChip(
                label: Text(q.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: q.color,
                backgroundColor: q.color.withValues(alpha: 0.12),
                onSelected: (_) => _select(q),
              );
            }).toList(),
          ),
          const SizedBox(height: 10),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: _selected.color.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(10)),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: _selected.properties.map((p) => Padding(padding: const EdgeInsets.only(bottom: 3), child: Row(children: [Text(TrilingualService.instance.getUIText('• ')), Expanded(child: Text(p, style: TextStyle(fontSize: 13)))]))).toList(),
            ),
          ),
        ],
      ),
    );
  }
}

List<Offset> _pointsFor(String type, double cx, double cy) {
  switch (type) {
    case 'Rectangle':
      return [Offset(cx - 70, cy - 35), Offset(cx + 70, cy - 35), Offset(cx + 70, cy + 35), Offset(cx - 70, cy + 35)];
    case 'Square':
      return [Offset(cx - 50, cy - 50), Offset(cx + 50, cy - 50), Offset(cx + 50, cy + 50), Offset(cx - 50, cy + 50)];
    case 'Rhombus':
      return [Offset(cx, cy - 50), Offset(cx + 60, cy), Offset(cx, cy + 50), Offset(cx - 60, cy)];
    case 'Trapezium':
      return [Offset(cx - 40, cy - 35), Offset(cx + 40, cy - 35), Offset(cx + 70, cy + 35), Offset(cx - 70, cy + 35)];
    case 'Kite':
      return [Offset(cx, cy - 55), Offset(cx + 40, cy - 5), Offset(cx, cy + 55), Offset(cx - 40, cy - 5)];
    default: // Parallelogram
      return [Offset(cx - 60, cy - 35), Offset(cx + 40, cy - 35), Offset(cx + 60, cy + 35), Offset(cx - 40, cy + 35)];
  }
}

class _QuadPainter extends CustomPainter {
  final String fromType;
  final String toType;
  final Color fromColor;
  final Color toColor;
  final double t;
  _QuadPainter({required this.fromType, required this.toType, required this.fromColor, required this.toColor, required this.t});

  @override
  void paint(Canvas canvas, Size size) {
    final cx = size.width / 2, cy = size.height / 2;
    final fromPts = _pointsFor(fromType, cx, cy);
    final toPts = _pointsFor(toType, cx, cy);
    final pts = List.generate(4, (i) => Offset.lerp(fromPts[i], toPts[i], t)!);
    final color = Color.lerp(fromColor, toColor, t)!;

    final path = Path()..addPolygon(pts, true);
    canvas.drawPath(path, Paint()..color = color.withValues(alpha: 0.35));
    canvas.drawPath(path, Paint()..color = color..style = PaintingStyle.stroke..strokeWidth = 2.5);
  }

  @override
  bool shouldRepaint(covariant _QuadPainter oldDelegate) => true;
}
