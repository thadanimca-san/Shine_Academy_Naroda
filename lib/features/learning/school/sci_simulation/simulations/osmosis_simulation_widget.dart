import 'dart:math' as math;
import 'package:flutter/material.dart';
import 'common/sim_frame.dart';

enum _Solution { pure, isotonic, salt }

/// Drop a cell into pure water, an isotonic solution, or a salt (hypertonic)
/// solution and watch it swell, stay the same, or shrink — visualising
/// osmosis the way Activity 2.2 (the potato-in-salt-water experiment) does
/// in the NCERT Class 9 Cell chapter.
class OsmosisSimulationWidget extends StatefulWidget {
  const OsmosisSimulationWidget({super.key});

  @override
  State<OsmosisSimulationWidget> createState() => _OsmosisSimulationWidgetState();
}

class _OsmosisSimulationWidgetState extends State<OsmosisSimulationWidget>
    with SingleTickerProviderStateMixin {
  _Solution _solution = _Solution.pure;
  late final AnimationController _controller;

  static const _targetSize = {
    _Solution.pure: 0.92,
    _Solution.isotonic: 0.62,
    _Solution.salt: 0.36,
  };

  static const _bgColor = {
    _Solution.pure: Color(0xFFE4ECF5),
    _Solution.isotonic: Color(0xFFE3EFE6),
    _Solution.salt: Color(0xFFFBE8DC),
  };

  static const _cellColor = {
    _Solution.pure: Color(0xFF3F6A9C),
    _Solution.isotonic: Color(0xFF2D7D5F),
    _Solution.salt: Color(0xFFD9622A),
  };

  static const _label = {
    _Solution.pure:
        'Water rushes IN — the cell SWELLS. The outside has less solute than inside (hypotonic solution).',
    _Solution.isotonic:
        'Equal solute inside and outside — NO net water movement. The cell stays the same size (isotonic solution).',
    _Solution.salt:
        'Water rushes OUT — the cell SHRINKS. The outside has more solute than inside (hypertonic solution).',
  };

  double _size = _targetSize[_Solution.pure]!;

  @override
  void initState() {
    super.initState();
    _controller = AnimationController(vsync: this, duration: const Duration(milliseconds: 900))
      ..addListener(() {
        setState(() {
          final from = _size;
          final to = _targetSize[_solution]!;
          _size = from + (to - from) * Curves.easeInOut.transform(_controller.value);
        });
      });
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  void _select(_Solution s) {
    if (s == _solution) return;
    setState(() => _solution = s);
    _controller.forward(from: 0);
  }

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Osmosis Simulator',
      icon: Icons.opacity,
      accent: const Color(0xFF3F6A9C),
      description: 'Pick a surrounding liquid and watch water move in or out of the cell.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 6,
            runSpacing: 6,
            children: [
              _solutionChip('Pure Water', _Solution.pure, const Color(0xFF3F6A9C)),
              _solutionChip('Isotonic', _Solution.isotonic, const Color(0xFF2D7D5F)),
              _solutionChip('Salt Solution', _Solution.salt, const Color(0xFFD9622A)),
            ],
          ),
          const SizedBox(height: 14),
          AnimatedContainer(
            duration: const Duration(milliseconds: 400),
            height: 190,
            width: double.infinity,
            decoration: BoxDecoration(
              color: _bgColor[_solution],
              borderRadius: BorderRadius.circular(14),
              border: Border.all(color: Colors.grey.shade300),
            ),
            child: Center(
              child: Container(
                width: 160 * _size,
                height: 160 * _size,
                decoration: BoxDecoration(
                  shape: BoxShape.circle,
                  color: _cellColor[_solution]!.withValues(alpha: 0.85),
                  boxShadow: [
                    BoxShadow(color: _cellColor[_solution]!.withValues(alpha: 0.25), blurRadius: 14, spreadRadius: 4),
                  ],
                ),
              ),
            ),
          ),
          const SizedBox(height: 12),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(color: Colors.grey.shade50, borderRadius: BorderRadius.circular(10), border: Border.all(color: Colors.grey.shade200)),
            child: Text(_label[_solution]!, style: TextStyle(fontSize: 13)),
          ),
        ],
      ),
    );
  }

  Widget _solutionChip(String label, _Solution s, Color color) {
    final isSelected = _solution == s;
    return ChoiceChip(
      label: Text(label, style: TextStyle(fontSize: 11.5, color: isSelected ? Colors.white : Colors.black87)),
      selected: isSelected,
      selectedColor: color,
      backgroundColor: color.withValues(alpha: 0.18),
      onSelected: (_) => _select(s),
    );
  }
}

// Kept for potential future use (e.g. tests wanting a deterministic curve).
double easeOsmosis(double t) => math.sin(t * math.pi / 2);
