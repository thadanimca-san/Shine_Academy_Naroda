import 'package:flutter/material.dart';

import '../models/account_model.dart';
import '../models/medium_model.dart';
import '../models/solution_model.dart';
import '../services/localization_service.dart';

/// Renders one ledger account as a classic two-sided T-account table.
class LedgerTableWidget extends StatelessWidget {
  final LedgerAccount ledger;
  final Medium medium;

  const LedgerTableWidget({super.key, required this.ledger, this.medium = Medium.english});

  @override
  Widget build(BuildContext context) {
    final balSide = ledger.balanceSide;
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text('${LocalizationService.t(ledger.account.name, medium)} A/c',
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const Divider(),
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(child: _side(LocalizationService.t('Debit', medium), ledger.debitPostings, ledger.totalDebit,
                    balSide == EntrySide.credit ? ledger.balanceAmount : null)),
                const VerticalDivider(),
                Expanded(child: _side(LocalizationService.t('Credit', medium), ledger.creditPostings, ledger.totalCredit,
                    balSide == EntrySide.debit ? ledger.balanceAmount : null)),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _side(String label, List<LedgerPosting> postings, double total, double? balancingFigure) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(label, style: TextStyle(fontWeight: FontWeight.bold)),
        for (final p in postings)
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 2),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Expanded(child: Text(LocalizationService.translatePhrase(p.particulars, medium), style: TextStyle(fontSize: 13))),
                Text(_fmt(p.amount), style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        if (balancingFigure != null && balancingFigure > 0.005)
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 2),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Expanded(
                    child: Text(LocalizationService.translatePhrase('By Balance c/d', medium),
                        style: TextStyle(fontSize: 13, fontStyle: FontStyle.italic))),
                Text(_fmt(balancingFigure), style: TextStyle(fontSize: 13, fontStyle: FontStyle.italic)),
              ],
            ),
          ),
        const Divider(),
        Text(_fmt(total + (balancingFigure ?? 0)), style: TextStyle(fontWeight: FontWeight.bold)),
      ],
    );
  }

  String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return '₹${isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2)}';
  }
}
