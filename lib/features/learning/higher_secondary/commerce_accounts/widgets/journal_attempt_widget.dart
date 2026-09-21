import 'package:flutter/material.dart';

import '../data/chart_of_accounts.dart';
import '../models/account_model.dart';
import '../models/medium_model.dart';
import '../services/localization_service.dart';

/// One student attempt at a single journal entry: pick the account and
/// side (Dr/Cr) for each line the entry actually needs. Checked against
/// the real [JournalEntry] via [onCheck] so feedback always comes from
/// the same solver-derived truth used everywhere else in the app.
class JournalAttemptWidget extends StatefulWidget {
  final JournalEntry correctEntry;
  final int lineCount;
  final void Function(bool allCorrect) onSubmit;
  final Medium medium;

  const JournalAttemptWidget({
    super.key,
    required this.correctEntry,
    required this.lineCount,
    required this.onSubmit,
    this.medium = Medium.english,
  });

  @override
  State<JournalAttemptWidget> createState() => _JournalAttemptWidgetState();
}

class _JournalAttemptWidgetState extends State<JournalAttemptWidget> {
  late List<Account?> _chosenAccounts;
  late List<EntrySide?> _chosenSides;
  late List<String?> _chosenAmounts;
  bool _checked = false;

  @override
  void initState() {
    super.initState();
    final n = widget.correctEntry.lines.length;
    _chosenAccounts = List<Account?>.filled(n, null);
    _chosenSides = List<EntrySide?>.filled(n, null);
    _chosenAmounts = List<String?>.filled(n, null);
  }

  bool _lineCorrect(int i) {
    final correct = widget.correctEntry.lines[i];
    final acc = _chosenAccounts[i];
    final side = _chosenSides[i];
    final amtText = _chosenAmounts[i];
    final amt = double.tryParse(amtText ?? '');
    return acc == correct.account &&
        side == correct.side &&
        amt != null &&
        (amt - correct.amount).abs() < 0.5;
  }

  void _check() {
    setState(() => _checked = true);
    final allCorrect = List.generate(widget.correctEntry.lines.length, _lineCorrect).every((v) => v);
    widget.onSubmit(allCorrect);
  }

  @override
  Widget build(BuildContext context) {
    final n = widget.correctEntry.lines.length;
    return Card(
      margin: const EdgeInsets.symmetric(vertical: 8, horizontal: 4),
      child: Padding(
        padding: const EdgeInsets.all(12),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(LocalizationService.translatePhrase(widget.correctEntry.transactionText, widget.medium),
                style: TextStyle(fontWeight: FontWeight.bold, fontSize: 15)),
            const SizedBox(height: 10),
            for (var i = 0; i < n; i++) _buildLineRow(i),
            const SizedBox(height: 8),
            if (!_checked)
              ElevatedButton(onPressed: _check, child: Text(LocalizationService.t('Check My Entry', widget.medium))),
            if (_checked) _buildFeedback(),
          ],
        ),
      ),
    );
  }

  Widget _buildLineRow(int i) {
    final correct = _checked ? _lineCorrect(i) : null;
    return Padding(
      padding: const EdgeInsets.symmetric(vertical: 4),
      child: Row(
        children: [
          Expanded(
            flex: 3,
            child: DropdownButtonFormField<Account>(
              isExpanded: true,
              decoration: InputDecoration(labelText: LocalizationService.t('Account', widget.medium), isDense: true),
              initialValue: _chosenAccounts[i],
              items: _accountOptions()
                  .map((a) => DropdownMenuItem(
                      value: a,
                      child: Text(LocalizationService.t(a.name, widget.medium), overflow: TextOverflow.ellipsis)))
                  .toList(),
              onChanged: _checked ? null : (v) => setState(() => _chosenAccounts[i] = v),
            ),
          ),
          const SizedBox(width: 6),
          Expanded(
            flex: 2,
            child: DropdownButtonFormField<EntrySide>(
              decoration: const InputDecoration(labelText: 'Dr/Cr', isDense: true),
              initialValue: _chosenSides[i],
              items: [
                DropdownMenuItem(value: EntrySide.debit, child: Text(LocalizationService.t('Debit', widget.medium))),
                DropdownMenuItem(value: EntrySide.credit, child: Text(LocalizationService.t('Credit', widget.medium))),
              ],
              onChanged: _checked ? null : (v) => setState(() => _chosenSides[i] = v),
            ),
          ),
          const SizedBox(width: 6),
          Expanded(
            flex: 2,
            child: TextFormField(
              decoration: InputDecoration(labelText: LocalizationService.t('Amount', widget.medium), isDense: true),
              keyboardType: TextInputType.number,
              enabled: !_checked,
              onChanged: (v) => _chosenAmounts[i] = v,
            ),
          ),
          if (_checked) ...[
            const SizedBox(width: 6),
            Icon(correct! ? Icons.check_circle : Icons.cancel,
                color: correct ? Colors.green : Colors.red),
          ],
        ],
      ),
    );
  }

  /// The dropdown offers the full standard chart of accounts (not just
  /// the correct entry's own accounts), so a student can't get the right
  /// answer by elimination from a short, hand-picked list — they have to
  /// actually recognise which account the transaction affects among
  /// realistic look-alikes (e.g. Machinery vs Furniture, Commission
  /// Received vs Interest Received).
  List<Account> _accountOptions() {
    final options = <Account>{
      ChartOfAccounts.cash,
      ChartOfAccounts.bank,
      ChartOfAccounts.goods,
      ChartOfAccounts.sales,
      ChartOfAccounts.purchasesReturn,
      ChartOfAccounts.salesReturn,
      ChartOfAccounts.capital,
      ChartOfAccounts.drawings,
      ...ChartOfAccounts.assetPurchaseOptions,
      ...ChartOfAccounts.expenseOptions,
      ...ChartOfAccounts.incomeOptions,
      ChartOfAccounts.interestPaid,
      ChartOfAccounts.discountAllowed,
      ChartOfAccounts.discountReceived,
      ChartOfAccounts.badDebts,
      ChartOfAccounts.carriageInwards,
      ChartOfAccounts.loanFromBank,
      ...widget.correctEntry.lines.map((l) => l.account),
    };
    return options.toList()..sort((a, b) => a.name.compareTo(b.name));
  }

  Widget _buildFeedback() {
    final allCorrect = List.generate(widget.correctEntry.lines.length, _lineCorrect).every((v) => v);
    return Container(
      padding: const EdgeInsets.all(8),
      decoration: BoxDecoration(
        color: allCorrect ? Colors.green.withValues(alpha: 0.1) : Colors.orange.withValues(alpha: 0.1),
        borderRadius: BorderRadius.circular(6),
      ),
      child: Text(
        allCorrect
            ? '${LocalizationService.t('Correct', widget.medium)}! Well done.'
            : '${LocalizationService.t('Not quite', widget.medium)} — check the account, Dr/Cr side, or amount above. '
                'Tap "${LocalizationService.t('Show Solution', widget.medium)}" below for the full reasoning.',
        style: TextStyle(color: allCorrect ? Colors.green.shade800 : Colors.orange.shade800),
      ),
    );
  }
}
