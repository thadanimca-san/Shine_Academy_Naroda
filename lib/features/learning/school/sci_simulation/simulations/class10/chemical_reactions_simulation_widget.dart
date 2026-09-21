import 'package:flutter/material.dart';
import '../common/sim_frame.dart';

class _Reaction {
  final String name;
  final String equation;
  final String explanation;
  final Color color;

  const _Reaction(this.name, this.equation, this.explanation, this.color);
}

/// A tap-to-explore gallery of the four core reaction types, each shown
/// with a simple equation and what actually happens to the atoms.
class ChemicalReactionsSimulationWidget extends StatefulWidget {
  const ChemicalReactionsSimulationWidget({super.key});

  @override
  State<ChemicalReactionsSimulationWidget> createState() => _ChemicalReactionsSimulationWidgetState();
}

class _ChemicalReactionsSimulationWidgetState extends State<ChemicalReactionsSimulationWidget> {
  static const _reactions = [
    _Reaction('Combination', '2Mg + O₂ → 2MgO', 'Two or more reactants combine to form a single product.', Color(0xFF42A5F5)),
    _Reaction('Decomposition', '2FeSO₄ →(heat) Fe₂O₃ + SO₂ + SO₃', 'A single compound breaks down into two or more simpler substances.', Color(0xFFEF5350)),
    _Reaction('Displacement', 'Fe + CuSO₄ → FeSO₄ + Cu', 'A more reactive element displaces a less reactive one from its compound.', Color(0xFF66BB6A)),
    _Reaction('Double Displacement', 'Na₂SO₄ + BaCl₂ → BaSO₄ + 2NaCl', 'Two compounds exchange ions to form two new compounds, often with a precipitate.', Color(0xFFFFA726)),
  ];

  _Reaction _selected = _reactions[0];

  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: 'Types of Chemical Reactions',
      icon: Icons.science,
      accent: Colors.deepPurple.shade400,
      description: 'Tap a reaction type to see its equation and what happens to the reactants.',
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Wrap(
            spacing: 8,
            runSpacing: 8,
            children: _reactions.map((r) {
              final isSelected = _selected.name == r.name;
              return ChoiceChip(
                label: Text(r.name, style: TextStyle(fontSize: 12, color: isSelected ? Colors.white : Colors.black87)),
                selected: isSelected,
                selectedColor: r.color,
                backgroundColor: r.color.withValues(alpha: 0.12),
                onSelected: (_) => setState(() => _selected = r),
              );
            }).toList(),
          ),
          const SizedBox(height: 14),
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(16),
            decoration: BoxDecoration(color: _selected.color.withValues(alpha: 0.08), borderRadius: BorderRadius.circular(12), border: Border.all(color: _selected.color.withValues(alpha: 0.3))),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(_selected.name, style: TextStyle(fontWeight: FontWeight.bold, color: _selected.color, fontSize: 15)),
                const SizedBox(height: 10),
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.symmetric(vertical: 10),
                  decoration: BoxDecoration(color: Colors.white, borderRadius: BorderRadius.circular(8)),
                  alignment: Alignment.center,
                  child: Text(_selected.equation, style: TextStyle(fontSize: 15, fontWeight: FontWeight.w600), textAlign: TextAlign.center),
                ),
                const SizedBox(height: 10),
                Text(_selected.explanation, style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        ],
      ),
    );
  }
}
