import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../services/cash_flow_generator.dart';
import '../services/localization_service.dart';
import '../services/progress_service.dart';
import '../widgets/cash_flow_statement_widget.dart';
import '../widgets/self_check_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for the Cash Flow Statement (Indirect Method): shows
/// Net Profit, depreciation, and the working-capital / investing /
/// financing movements, lets the student work it out, then reveals the
/// fully classified statement.
class CashFlowPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;
  final Medium medium;

  const CashFlowPracticeScreen({
    super.key,
    required this.board,
    required this.schoolClass,
    this.difficulty = 3,
    this.medium = Medium.english,
  });

  @override
  State<CashFlowPracticeScreen> createState() => _CashFlowPracticeScreenState();
}

class _CashFlowPracticeScreenState extends State<CashFlowPracticeScreen> {
  late GeneratedCashFlowProblem _problem;
  bool _revealed = false;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  void _generateNewProblem() {
    setState(() {
      _problem = CashFlowGenerator.generate(
        board: widget.board,
        schoolClass: widget.schoolClass,
        difficulty: widget.difficulty,
      );
      _revealed = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final d = _problem.data;
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Cash Flow Statement — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(
            LocalizationService.t('From the following information, prepare a Cash Flow Statement (Indirect Method) for the year:', widget.medium),
            style: TextStyle(fontSize: 15),
          ),
          const SizedBox(height: 8),
          _fact('Net Profit before Tax', d.netProfitBeforeTax),
          _fact('Depreciation for the year', d.depreciationForYear),
          if (d.debtorsOpening > 0 || d.debtorsClosing > 0)
            _fact('Debtors (Opening ₹${d.debtorsOpening.toStringAsFixed(0)} → Closing)', d.debtorsClosing),
          if (d.stockOpening > 0 || d.stockClosing > 0)
            _fact('Stock (Opening ₹${d.stockOpening.toStringAsFixed(0)} → Closing)', d.stockClosing),
          if (d.creditorsOpening > 0 || d.creditorsClosing > 0)
            _fact('Creditors (Opening ₹${d.creditorsOpening.toStringAsFixed(0)} → Closing)', d.creditorsClosing),
          if (d.outstandingExpensesOpening > 0 || d.outstandingExpensesClosing > 0)
            _fact('Outstanding Expenses (Opening ₹${d.outstandingExpensesOpening.toStringAsFixed(0)} → Closing)',
                d.outstandingExpensesClosing),
          if (d.machineryPurchased > 0) _fact('Machinery Purchased', d.machineryPurchased),
          if (d.machinerySold > 0) _fact('Machinery Sold', d.machinerySold),
          if (d.loanRaised > 0) _fact('Loan Raised', d.loanRaised),
          if (d.loanRepaid > 0) _fact('Loan Repaid', d.loanRepaid),
          if (d.sharesIssuedForCash > 0) _fact('Shares Issued for Cash', d.sharesIssuedForCash),
          _fact('Opening Cash and Bank Balance', d.openingCashAndBank),
          const SizedBox(height: 16),
          Center(
            child: ElevatedButton.icon(
              onPressed: () => setState(() => _revealed = !_revealed),
              icon: Icon(_revealed ? Icons.visibility_off : Icons.lightbulb_outline),
              label: Text(_revealed
                  ? LocalizationService.t('Hide Solution', widget.medium)
                  : LocalizationService.t('Show Solution', widget.medium)),
            ),
          ),
          if (_revealed) ...[
            CashFlowStatementWidget(result: _problem.result, medium: widget.medium),
            SelfCheckWidget(key: ValueKey(_problem.id), topicKey: ProgressService.topicCashFlow),
          ],
        ],
      ),
    );
  }

  Widget _fact(String label, double amount) {
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 2),
      child: Text('• ${LocalizationService.translatePhrase(label, widget.medium)}: ₹${amount.toStringAsFixed(0)}'),
    );
  }
}
