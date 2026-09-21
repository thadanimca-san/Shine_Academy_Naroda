import 'package:flutter/material.dart';

import '../models/cash_flow_model.dart';
import '../models/medium_model.dart';
import '../services/localization_service.dart';

/// Renders the finished Cash Flow Statement as three sections
/// (Operating, Investing, Financing) plus the opening/closing
/// reconciliation, matching the standard exam-answer layout.
class CashFlowStatementWidget extends StatelessWidget {
  final CashFlowResult result;
  final Medium medium;

  const CashFlowStatementWidget({super.key, required this.result, this.medium = Medium.english});

  @override
  Widget build(BuildContext context) {
    String t(String s) => LocalizationService.t(s, medium);
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 6),
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(t('Cash Flow Statement'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 16)),
            const Divider(),
            _section(t('A. Cash Flow from Operating Activities'), result.operatingLines),
            _section(t('B. Cash Flow from Investing Activities'), result.investingLines),
            _section(t('C. Cash Flow from Financing Activities'), result.financingLines),
            const Divider(),
            _row(t('Net Increase/Decrease in Cash (A+B+C)'), result.netIncreaseInCash, bold: true),
            _row(t('Add: Opening Cash and Bank Balance'), result.openingCash),
            _row(t('Closing Cash and Bank Balance'), result.closingCash, bold: true),
          ],
        ),
      ),
    );
  }

  Widget _section(String title, List<CashFlowLine> lines) {
    return Padding(
      padding: const EdgeInsets.only(top: 8, bottom: 4),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(title, style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13)),
          for (final line in lines)
            _row(LocalizationService.translatePhrase(line.particulars, medium), line.amount, bold: line.isSubtotal),
        ],
      ),
    );
  }

  Widget _row(String label, double amount, {bool bold = false}) {
    final style = TextStyle(fontSize: 13, fontWeight: bold ? FontWeight.bold : FontWeight.normal);
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 2),
      child: Row(
        mainAxisAlignment: MainAxisAlignment.spaceBetween,
        children: [
          Expanded(child: Text(label, style: style)),
          Text(_fmt(amount), style: style),
        ],
      ),
    );
  }

  String _fmt(double v) {
    final isNeg = v < 0;
    final abs = v.abs();
    final isWhole = abs == abs.roundToDouble();
    final formatted = isWhole ? abs.toStringAsFixed(0) : abs.toStringAsFixed(2);
    return isNeg ? '(₹$formatted)' : '₹$formatted';
  }
}
