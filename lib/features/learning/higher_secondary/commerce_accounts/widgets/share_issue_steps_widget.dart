import 'package:flutter/material.dart';

import '../models/company_accounts_model.dart';
import '../models/medium_model.dart';
import '../services/localization_service.dart';

/// Renders the sequence of share-issue journal entries (application,
/// allotment, calls, forfeiture, reissue) as a simple Dr/Cr list, in the
/// order a student would write them in an exam answer.
class ShareIssueStepsWidget extends StatelessWidget {
  final List<ShareIssueStep> steps;
  final Medium medium;

  const ShareIssueStepsWidget({super.key, required this.steps, this.medium = Medium.english});

  @override
  Widget build(BuildContext context) {
    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [for (final step in steps) _buildStep(step)],
    );
  }

  Widget _buildStep(ShareIssueStep step) {
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 4),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(LocalizationService.translatePhrase(step.title, medium), style: TextStyle(fontWeight: FontWeight.bold)),
            const SizedBox(height: 4),
            _line('${LocalizationService.t('Bank', medium)} A/c', step.debitCash, isDebit: true),
            if (step.secondDebitAccountName != null)
              _line(LocalizationService.t(step.secondDebitAccountName!, medium), step.secondDebitAmount ?? 0, isDebit: true),
            _line(LocalizationService.t(step.creditAccountName, medium), step.creditAmount, isDebit: false),
            if (step.secondCreditAccountName != null)
              _line(LocalizationService.t(step.secondCreditAccountName!, medium), step.secondCreditAmount ?? 0, isDebit: false),
            const SizedBox(height: 4),
            Text(LocalizationService.translatePhrase(step.narration, medium),
                style: TextStyle(fontSize: 11, fontStyle: FontStyle.italic, color: Colors.grey)),
          ],
        ),
      ),
    );
  }

  Widget _line(String account, double amount, {required bool isDebit}) {
    return Padding(
      padding: EdgeInsets.only(left: isDebit ? 0 : 20),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Expanded(child: Text(isDebit ? '$account Dr.' : '${LocalizationService.t('To', medium)} $account')),
          Text('₹${amount.toStringAsFixed(0)}'),
        ],
      ),
    );
  }
}
