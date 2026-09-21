import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/solution_model.dart';
import '../services/localization_service.dart';

class TrialBalanceWidget extends StatelessWidget {
  final TrialBalance trialBalance;
  final Medium medium;

  const TrialBalanceWidget({super.key, required this.trialBalance, this.medium = Medium.english});

  @override
  Widget build(BuildContext context) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(LocalizationService.t('Trial Balance', medium), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const Divider(),
            Table(
              columnWidths: const {0: FlexColumnWidth(3), 1: FlexColumnWidth(1), 2: FlexColumnWidth(1)},
              children: [
                TableRow(children: [
                  Padding(padding: const EdgeInsets.all(4), child: Text(LocalizationService.t('Account', medium), style: TextStyle(fontWeight: FontWeight.bold))),
                  Padding(padding: const EdgeInsets.all(4), child: Text(LocalizationService.t('Debit', medium), style: TextStyle(fontWeight: FontWeight.bold))),
                  Padding(padding: const EdgeInsets.all(4), child: Text(LocalizationService.t('Credit', medium), style: TextStyle(fontWeight: FontWeight.bold))),
                ]),
                for (final row in trialBalance.rows)
                  TableRow(children: [
                    Padding(padding: const EdgeInsets.all(4), child: Text(LocalizationService.t(row.account.name, medium))),
                    Padding(padding: const EdgeInsets.all(4), child: Text(row.debitAmount > 0 ? _fmt(row.debitAmount) : '')),
                    Padding(padding: const EdgeInsets.all(4), child: Text(row.creditAmount > 0 ? _fmt(row.creditAmount) : '')),
                  ]),
                TableRow(children: [
                  Padding(padding: const EdgeInsets.all(4), child: Text(LocalizationService.t('Total', medium), style: TextStyle(fontWeight: FontWeight.bold))),
                  Padding(padding: const EdgeInsets.all(4), child: Text(_fmt(trialBalance.totalDebit), style: TextStyle(fontWeight: FontWeight.bold))),
                  Padding(padding: const EdgeInsets.all(4), child: Text(_fmt(trialBalance.totalCredit), style: TextStyle(fontWeight: FontWeight.bold))),
                ]),
              ],
            ),
            const SizedBox(height: 6),
            Text(
              trialBalance.isBalanced
                  ? '${LocalizationService.t('Trial Balance', medium)} is balanced ✓'
                  : '${LocalizationService.t('Trial Balance', medium)} does NOT balance — check postings',
              style: TextStyle(color: trialBalance.isBalanced ? Colors.green.shade800 : Colors.red.shade800, fontWeight: FontWeight.bold),
            ),
          ],
        ),
      ),
    );
  }

  String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
