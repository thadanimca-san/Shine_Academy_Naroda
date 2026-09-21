import 'package:flutter/material.dart';

import '../models/medium_model.dart';
import '../models/problem_model.dart';
import '../services/cash_book_generator.dart';
import '../services/localization_service.dart';
import '../services/progress_service.dart';
import '../widgets/cash_book_table_widget.dart';
import '../widgets/self_check_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Student practice for the Double Column Cash Book: shows the
/// transactions to journalise mentally, lets the student attempt it on
/// paper, then reveals the fully solved cash book for self-checking.
/// (Full per-cell input/check, like the journal screen, is a natural
/// follow-up once this reveal-based flow is validated with real students.)
class CashBookPracticeScreen extends StatefulWidget {
  final Board board;
  final int schoolClass;
  final int difficulty;
  final Medium medium;

  const CashBookPracticeScreen({
    super.key,
    required this.board,
    required this.schoolClass,
    this.difficulty = 2,
    this.medium = Medium.english,
  });

  @override
  State<CashBookPracticeScreen> createState() => _CashBookPracticeScreenState();
}

class _CashBookPracticeScreenState extends State<CashBookPracticeScreen> {
  late GeneratedCashBookProblem _problem;
  bool _revealed = false;

  @override
  void initState() {
    super.initState();
    _generateNewProblem();
  }

  void _generateNewProblem() {
    setState(() {
      _problem = CashBookGenerator.generate(
        board: widget.board,
        schoolClass: widget.schoolClass,
        difficulty: widget.difficulty,
      );
      _revealed = false;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Cash Book — Practice')),
        actions: [
          IconButton(icon: Icon(Icons.refresh), tooltip: 'New Problem', onPressed: _generateNewProblem),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(12),
        children: [
          Text(
            LocalizationService.translatePhrase(
                'Prepare a Double Column Cash Book from the following transactions. '
                'Work it out on paper, then reveal the solution to check yourself.',
                widget.medium),
            style: TextStyle(fontSize: 15),
          ),
          const SizedBox(height: 8),
          Text('${LocalizationService.t('Opening Cash Balance', widget.medium)}: ₹${_problem.openingCash.toStringAsFixed(0)}',
              style: TextStyle(fontWeight: FontWeight.bold)),
          Text('${LocalizationService.t('Opening Bank Balance', widget.medium)}: ₹${_problem.openingBank.toStringAsFixed(0)}',
              style: TextStyle(fontWeight: FontWeight.bold)),
          const SizedBox(height: 10),
          for (final tx in _problem.transactions)
            Padding(
              padding: const EdgeInsets.symmetric(vertical: 2),
              child: Text('• ${LocalizationService.translatePhrase(tx.transactionText, widget.medium)}'),
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
            CashBookTableWidget(
              transactions: _problem.transactions,
              openingCash: _problem.openingCash,
              openingBank: _problem.openingBank,
              medium: widget.medium,
            ),
            SelfCheckWidget(key: ValueKey(_problem.id), topicKey: ProgressService.topicCashBook),
          ],
        ],
      ),
    );
  }
}
