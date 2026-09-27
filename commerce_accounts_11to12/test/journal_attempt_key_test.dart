import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/data/chart_of_accounts.dart';
import 'package:commerce_accounts_11to12/models/account_model.dart';
import 'package:commerce_accounts_11to12/widgets/journal_attempt_widget.dart';

/// Mimics a practice screen: one StatefulWidget holding "the current
/// question", swappable via setState — the same shape
/// student_practice_screen.dart / rectification_practice_screen.dart use
/// when "New Problem" regenerates _problem and rebuilds in place (NOT a
/// fresh pumpWidget, which would trivially reset everything and hide
/// this bug).
class _HostScreen extends StatefulWidget {
  const _HostScreen();

  @override
  State<_HostScreen> createState() => _HostScreenState();
}

class _HostScreenState extends State<_HostScreen> {
  String problemId = 'problem-1';
  JournalEntry entry = JournalEntry(
    transactionText: 'Purchased furniture for cash ₹5000',
    lines: const [
      JournalLine(account: ChartOfAccounts.furniture, side: EntrySide.debit, amount: 5000),
      JournalLine(account: ChartOfAccounts.cash, side: EntrySide.credit, amount: 5000),
    ],
    narration: '(Being furniture purchased for cash)',
  );

  void swapToSecondQuestion() {
    setState(() {
      problemId = 'problem-2';
      entry = JournalEntry(
        transactionText: 'Paid rent ₹2000',
        lines: const [
          JournalLine(account: ChartOfAccounts.rentExpense, side: EntrySide.debit, amount: 2000),
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.credit, amount: 2000),
        ],
        narration: '(Being rent paid)',
      );
    });
  }

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        body: JournalAttemptWidget(
          key: ValueKey('$problemId-${entry.transactionText}'),
          correctEntry: entry,
          lineCount: entry.lines.length,
          onSubmit: (_) {},
        ),
      ),
    );
  }
}

void main() {
  testWidgets(
    'swapping to a new question via setState (same widget tree, in-place rebuild) does not carry over stale checked state',
    (tester) async {
      await tester.pumpWidget(const _HostScreen());

      await tester.tap(find.text('Check My Entry'));
      await tester.pumpAndSettle();
      expect(find.text('Check My Entry'), findsNothing, reason: 'first question should be checked');

      final state = tester.state<_HostScreenState>(find.byType(_HostScreen));
      state.swapToSecondQuestion();
      await tester.pumpAndSettle();

      expect(find.text('Check My Entry'), findsOneWidget,
          reason: 'new question must start fresh, not inherit the previous question\'s checked state');
      expect(find.text('Paid rent ₹2000'), findsOneWidget);
      expect(find.text('Purchased furniture for cash ₹5000'), findsNothing);
    },
  );
}
