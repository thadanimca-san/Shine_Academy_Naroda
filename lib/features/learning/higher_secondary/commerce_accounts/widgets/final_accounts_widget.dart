import 'package:flutter/material.dart';

import '../models/final_accounts_model.dart';
import '../models/medium_model.dart';
import '../services/localization_service.dart';

/// Renders the Trading A/c, Profit & Loss A/c, and Balance Sheet as three
/// classic two-sided statements, exactly how a student would lay them
/// out on paper.
class FinalAccountsWidget extends StatelessWidget {
  final FinalAccountsResult result;
  final Medium medium;

  const FinalAccountsWidget({super.key, required this.result, this.medium = Medium.english});

  @override
  Widget build(BuildContext context) {
    String t(String s) => LocalizationService.t(s, medium);
    return Column(
      children: [
        _statementCard(
          title: t('Trading Account'),
          leftLabel: t('Debit'),
          rightLabel: t('Credit'),
          leftLines: result.tradingAccountDebit,
          rightLines: result.tradingAccountCredit,
          leftBalancingLabel: result.grossProfit > 0 ? t('Gross Profit c/d') : null,
          leftBalancingAmount: result.grossProfit > 0 ? result.grossProfit : null,
          rightBalancingLabel: result.grossProfit < 0 ? t('Gross Loss c/d') : null,
          rightBalancingAmount: result.grossProfit < 0 ? -result.grossProfit : null,
        ),
        _statementCard(
          title: t('Profit & Loss Account'),
          leftLabel: t('Debit'),
          rightLabel: t('Credit'),
          leftLines: result.profitLossDebit,
          rightLines: result.profitLossCredit,
          leftBalancingLabel: result.netProfit > 0 ? t('Net Profit (to Capital)') : null,
          leftBalancingAmount: result.netProfit > 0 ? result.netProfit : null,
          rightBalancingLabel: result.netProfit < 0 ? t('Net Loss (to Capital)') : null,
          rightBalancingAmount: result.netProfit < 0 ? -result.netProfit : null,
        ),
        _statementCard(
          title: t('Balance Sheet'),
          leftLabel: t('Liabilities'),
          rightLabel: t('Assets'),
          leftLines: result.balanceSheetLiabilities,
          rightLines: result.balanceSheetAssets,
        ),
        Padding(
          padding: const EdgeInsets.only(top: 8),
          child: Text(
            result.balanceSheetTallies ? '${t('Balance Sheet tallies')} ✓' : t('Balance Sheet does NOT tally'),
            style: TextStyle(
                color: result.balanceSheetTallies ? Colors.green.shade800 : Colors.red.shade800,
                fontWeight: FontWeight.bold),
          ),
        ),
      ],
    );
  }

  Widget _statementCard({
    required String title,
    required String leftLabel,
    required String rightLabel,
    required List<StatementLine> leftLines,
    required List<StatementLine> rightLines,
    String? leftBalancingLabel,
    double? leftBalancingAmount,
    String? rightBalancingLabel,
    double? rightBalancingAmount,
  }) {
    final leftTotal = leftLines.fold(0.0, (s, l) => s + l.amount) + (leftBalancingAmount ?? 0);
    final rightTotal = rightLines.fold(0.0, (s, l) => s + l.amount) + (rightBalancingAmount ?? 0);
    final grandTotal = leftTotal > rightTotal ? leftTotal : rightTotal;

    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(title, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const Divider(),
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                  child: _side(leftLabel, leftLines, leftBalancingLabel, leftBalancingAmount, grandTotal),
                ),
                const VerticalDivider(),
                Expanded(
                  child: _side(rightLabel, rightLines, rightBalancingLabel, rightBalancingAmount, grandTotal),
                ),
              ],
            ),
          ],
        ),
      ),
    );
  }

  Widget _side(String label, List<StatementLine> lines, String? balancingLabel, double? balancingAmount, double grandTotal) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Text(label, style: TextStyle(fontWeight: FontWeight.bold)),
        for (final line in lines)
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 2),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Expanded(child: Text(LocalizationService.t(line.particulars, medium), style: TextStyle(fontSize: 13))),
                Text(_fmt(line.amount), style: TextStyle(fontSize: 13)),
              ],
            ),
          ),
        if (balancingLabel != null && balancingAmount != null)
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 2),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Expanded(child: Text(balancingLabel, style: TextStyle(fontSize: 13, fontStyle: FontStyle.italic))),
                Text(_fmt(balancingAmount), style: TextStyle(fontSize: 13, fontStyle: FontStyle.italic)),
              ],
            ),
          ),
        const Divider(),
        Text(_fmt(grandTotal), style: TextStyle(fontWeight: FontWeight.bold)),
      ],
    );
  }

  String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return '₹${isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2)}';
  }
}
