import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Postulate {
  final String title;
  final String description;

  const _Postulate(this.title, this.description);
}

/// A tap-to-explore gallery of Euclid's five postulates: each postulate
/// card animates in with a slide-and-fade so switching between them
/// feels like turning a page, not an instant swap.
class EuclidsGeometrySimulationWidget extends StatefulWidget {
  const EuclidsGeometrySimulationWidget({super.key});

  @override
  State<EuclidsGeometrySimulationWidget> createState() => _EuclidsGeometrySimulationWidgetState();
}

class _EuclidsGeometrySimulationWidgetState extends State<EuclidsGeometrySimulationWidget> with SingleTickerProviderStateMixin {
  static const _postulates = [
    _Postulate('Postulate 1', 'A straight line may be drawn from any one point to any other point.'),
    _Postulate('Postulate 2', 'A terminated line (segment) can be produced indefinitely to form a line.'),
    _Postulate('Postulate 3', 'A circle can be drawn with any centre and any radius.'),
    _Postulate('Postulate 4', 'All right angles are equal to one another.'),
    _Postulate('Postulate 5', 'If a straight line falling on two straight lines makes interior angles on the same side summing to less than 180°, the two lines meet on that side if extended far enough.'),
  ];

  int _index = 0;
  late AnimationController _controller;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 400));
    _controller.forward();
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _select(int i) {
    if (i == _index) return;
    setState(() => _index = i);
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    final p = _postulates[_index];

    return SimFrame(
      title: "Euclid's Five Postulates",
      icon: Icons.architecture,
      accent: Colors.brown.shade600,
      description: 'Tap through each postulate to see what it says.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          AnimatedBuilder(
            animation: _controller,
            builder: (context, _) {
              final eased = Curves.easeOutCubic.transform(_controller.value);
              return Opacity(
                opacity: eased,
                child: Transform.translate(
                  offset: Offset(0, (1 - eased) * 14),
                  child: Container(
                    width: double.infinity,
                    padding: const EdgeInsets.all(18),
                    decoration: BoxDecoration(color: Colors.brown.shade50, borderRadius: BorderRadius.circular(12)),
                    child: Column(
                      children: [
                        Text(p.title, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16, color: Colors.brown.shade800)),
                        const SizedBox(height: 10),
                        Text(p.description, textAlign: TextAlign.center, style: TextStyle(fontSize: 13)),
                      ],
                    ),
                  ),
                ),
              );
            },
          ),
          const SizedBox(height: 12),
          Wrap(
            spacing: 8,
            children: _postulates.asMap().entries.map((e) {
              final isSelected = e.key == _index;
              return ChoiceChip(
                label: Text('${e.key + 1}', style: TextStyle(color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: Colors.brown.shade600,
                backgroundColor: Colors.brown.shade50,
                onSelected: (_) => _select(e.key),
              );
            }).toList(),
          ),
        ],
      ),
    );
  }
}
