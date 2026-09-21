import 'package:flutter/material.dart';

import '../models/dissolution_model.dart';
import '../models/medium_model.dart';
import '../services/localization_service.dart';

/// Renders the Realisation Account as a two-sided table, the standard
/// format for showing Dissolution of Partnership workings.
class RealisationAccountWidget extends StatelessWidget {
  final DissolutionResult result;
  final Medium medium;

  const RealisationAccountWidget({super.key, required this.result, this.medium = Medium.english});

  @override
  Widget build(BuildContext context) {
    final isProfit = result.realisationProfitOrLoss >= 0;
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(LocalizationService.t('Realisation Account', medium), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const Divider(),
            Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Expanded(
                    child: _side(LocalizationService.t('Debit', medium), result.realisationDebit,
                        isProfit ? result.realisationProfitOrLoss : null,
                        LocalizationService.t('Profit transferred to Capital A/cs', medium))),
                const VerticalDivider(),
                Expanded(
                    child: _side(LocalizationService.t('Credit', medium), result.realisationCredit,
                        !isProfit ? -result.realisationProfitOrLoss : null,
                        LocalizationService.t('Loss transferred to Capital A/cs', medium))),
              ],
            ),
            const SizedBox(height: 8),
            for (final s in result.partnerSettlements)
              Text('${s.partnerName}: ${LocalizationService.t('Capital', medium)} ₹${s.capitalBalance.toStringAsFixed(0)} '
                  '${s.shareOfRealisationProfit >= 0 ? '+' : '-'} ₹${s.shareOfRealisationProfit.abs().toStringAsFixed(0)} '
                  '= ₹${s.finalAmountReceived.toStringAsFixed(0)} ${s.finalAmountReceived >= 0 ? "received" : "payable by partner"}'),
          ],
        ),
      ),
    );
  }

  Widget _side(String label, List<RealisationLine> lines, double? balancingAmount, String balancingLabel) {
    final total = lines.fold(0.0, (s, l) => s + l.amount) + (balancingAmount ?? 0);
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
                Expanded(child: Text(LocalizationService.translatePhrase(line.particulars, medium), style: TextStyle(fontSize: 12))),
                Text(line.amount.toStringAsFixed(0), style: TextStyle(fontSize: 12)),
              ],
            ),
          ),
        if (balancingAmount != null && balancingAmount > 0.005)
          Padding(
            padding: const EdgeInsets.symmetric(vertical: 2),
            child: Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Expanded(child: Text(balancingLabel, style: TextStyle(fontSize: 12, fontStyle: FontStyle.italic))),
                Text(balancingAmount.toStringAsFixed(0), style: TextStyle(fontSize: 12, fontStyle: FontStyle.italic)),
              ],
            ),
          ),
        const Divider(),
        Text(total.toStringAsFixed(0), style: TextStyle(fontWeight: FontWeight.bold)),
      ],
    );
  }
}
