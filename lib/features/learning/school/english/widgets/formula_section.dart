import 'package:flutter/material.dart';
import '../models/chapter_model.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Displays a chapter's formula derivations as expandable cards: the
/// formula name and expression are always visible, and tapping reveals
/// the full step-by-step derivation — useful for a teacher walking
/// through the logic on a board, not just handing students the result.
class FormulaSection extends StatelessWidget {
  final List<FormulaDerivation> formulas;

  const FormulaSection({super.key, required this.formulas});

  @override
  Widget build(BuildContext context) {
    if (formulas.isEmpty) return const SizedBox.shrink();

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: formulas.map((f) => _FormulaCard(formula: f)).toList(),
    );
  }
}

class _FormulaCard extends StatelessWidget {
  final FormulaDerivation formula;

  const _FormulaCard({required this.formula});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.only(bottom: 10),
      color: Colors.amber.shade50,
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(10), side: BorderSide(color: Colors.amber.shade200)),
      child: Theme(
        data: Theme.of(context).copyWith(dividerColor: Colors.transparent),
        child: ExpansionTile(
          tilePadding: const EdgeInsets.symmetric(horizontal: 14, vertical: 2),
          childrenPadding: const EdgeInsets.fromLTRB(14, 0, 14, 12),
          expandedCrossAxisAlignment: CrossAxisAlignment.start,
          leading: Icon(Icons.functions, color: Colors.amber.shade800),
          title: Text(formula.formulaName, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
          subtitle: Padding(
            padding: const EdgeInsets.only(top: 4),
            child: Text(
              formula.expression,
              style: TextStyle(fontFamily: 'monospace', fontSize: 15, fontWeight: FontWeight.w600, color: Colors.brown.shade800),
            ),
          ),
          children: [
            Align(alignment: Alignment.centerLeft, child: Text(TrilingualService.instance.getUIText('Derivation'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12, color: Theme.of(context).colorScheme.onSurfaceVariant))),
            const SizedBox(height: 6),
            ...formula.derivationSteps.asMap().entries.map((e) => Padding(
                  padding: const EdgeInsets.only(bottom: 6),
                  child: Row(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text('${e.key + 1}. ', style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
                      Expanded(child: Text(e.value, style: TextStyle(fontSize: 13))),
                    ],
                  ),
                )),
          ],
        ),
      ),
    );
  }
}
