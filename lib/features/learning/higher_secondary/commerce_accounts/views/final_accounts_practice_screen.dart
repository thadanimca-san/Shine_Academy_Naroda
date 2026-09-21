import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../services/final_accounts_generator.dart';
import '../services/localization_service.dart';
import '../services/progress_service.dart';
import '../widgets/final_accounts_widget.dart';
import '../widgets/self_check_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for Final Accounts: shows a trial balance extract
/// plus adjustments, lets the student work out the Trading A/c, P&L A/c
/// and Balance Sheet on paper, then reveals the fully solved statements.
class FinalAccountsPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;
  final Medium medium;

  const FinalAccountsPracticeScreen({
    super.key,
    required this.board,
    required this.schoolClass,
    this.difficulty = 3,
    this.medium = Medium.english,
  });

  @override
  State<FinalAccountsPracticeScreen> createState() => _FinalAccountsPracticeScreenState();
}

class _FinalAccountsPracticeScreenState extends State<FinalAccountsPracticeScreen> {
  late GeneratedFinalAccountsProblem _problem;
  bool _revealed = false;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  void _generateNewProblem() {
    setState(() {
      _problem = FinalAccountsGenerator.generate(
        board: widget.board,
        schoolClass: widget.schoolClass,
        difficulty: widget.difficulty,
      );
      _revealed = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    final i = _problem.input;
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Final Accounts — Practice')),
        actions: [IconButton(icon: Icon(Icons.refresh), onPressed: _generateNewProblem)],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(
            LocalizationService.t(
                'From the following Trial Balance and adjustments, prepare the Trading Account, '
                'Profit & Loss Account, and Balance Sheet:',
                widget.medium),
            style: TextStyle(fontSize: 15),
          ),
          const SizedBox(height: 10),
          Text('${LocalizationService.t('Trial Balance', widget.medium)}:', style: TextStyle(fontWeight: FontWeight.bold)),
          _tbRow('Opening Stock', i.openingStock, true),
          _tbRow('Purchases', i.purchases, true),
          _tbRow('Purchases Return', i.purchasesReturn, false),
          _tbRow('Sales', i.sales, false),
          _tbRow('Sales Return', i.salesReturn, true),
          _tbRow('Wages', i.wages, true),
          _tbRow('Carriage Inwards', i.carriageInwards, true),
          _tbRow('Carriage Outwards', i.carriageOutwards, true),
          _tbRow('Rent', i.rent, true),
          _tbRow('Salaries', i.salaries, true),
          _tbRow('Discount Allowed', i.discountAllowed, true),
          _tbRow('Discount Received', i.discountReceived, false),
          _tbRow('Commission Received', i.commissionReceived, false),
          _tbRow('Debtors', i.debtors, true),
          _tbRow('Creditors', i.creditors, false),
          _tbRow('Capital', i.capital, false),
          _tbRow('Drawings', i.drawings, true),
          _tbRow('Cash', i.cash, true),
          _tbRow('Bank', i.bank, true),
          _tbRow('Furniture', i.furniture, true),
          _tbRow('Machinery', i.machinery, true),
          const SizedBox(height: 10),
          Text('${LocalizationService.t('Adjustments', widget.medium)}:', style: TextStyle(fontWeight: FontWeight.bold)),
          for (final adj in _problem.adjustments)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 2),
              child: Text('• ${LocalizationService.translatePhrase(adj.description, widget.medium)}'),
            ),
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
            FinalAccountsWidget(result: _problem.result, medium: widget.medium),
            SelfCheckWidget(key: ValueKey(_problem.id), topicKey: ProgressService.topicFinalAccounts),
          ],
        ],
      ),
    );
  }

  Widget _tbRow(String label, double amount, bool isDebit) {
    if (amount <= 0) return const SizedBox.shrink();
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 1),
      child: Row(
        children: [
          Expanded(flex: 3, child: Text(LocalizationService.t(label, widget.medium))),
          Expanded(flex: 1, child: Text(isDebit ? amount.toStringAsFixed(0) : '', textAlign: TextAlign.right)),
          Expanded(flex: 1, child: Text(!isDebit ? amount.toStringAsFixed(0) : '', textAlign: TextAlign.right)),
        ],
      ),
    );
  }
}
