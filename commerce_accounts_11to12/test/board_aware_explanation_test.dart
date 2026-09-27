import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/data/chart_of_accounts.dart';
import 'package:commerce_accounts_11to12/models/account_model.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/accounting_solver.dart';
import 'package:commerce_accounts_11to12/services/problem_generator.dart';

void main() {
  final entry = JournalEntry(
    transactionText: 'Purchased furniture for cash ₹5000',
    lines: [
      const JournalLine(account: ChartOfAccounts.furniture, side: EntrySide.debit, amount: 5000),
      const JournalLine(account: ChartOfAccounts.cash, side: EntrySide.credit, amount: 5000),
    ],
    narration: '(Being furniture purchased for cash)',
  );

  group('Board-aware explainEntry', () {
    test('GSEB explanation uses golden-rules vocabulary (Personal/Real/Nominal)', () {
      final solution = AccountingSolver.explainEntry(entry, board: Board.gseb);
      final reasoningText = solution.steps.map((s) => s.reasoning).join(' ');
      expect(reasoningText, contains('Real'));
      expect(reasoningText, contains('Golden Rule'));
      expect(reasoningText, contains('Debit what comes in'));
    });

    test('CBSE explanation uses modern-method vocabulary (Asset/Liability/etc.)', () {
      final solution = AccountingSolver.explainEntry(entry, board: Board.cbse);
      final reasoningText = solution.steps.map((s) => s.reasoning).join(' ');
      expect(reasoningText, contains('Asset account'));
      expect(reasoningText, isNot(contains('Golden Rule')));
    });

    test('GSEB and CBSE explanations conclude the identical Dr/Cr sides and amounts', () {
      final gseb = AccountingSolver.explainEntry(entry, board: Board.gseb);
      final cbse = AccountingSolver.explainEntry(entry, board: Board.cbse);
      // Same number of steps, same titles (which encode account + Dr/Cr side).
      expect(gseb.steps.length, cbse.steps.length);
      for (var i = 0; i < gseb.steps.length; i++) {
        expect(gseb.steps[i].title, cbse.steps[i].title, reason: 'Step $i title should match regardless of board');
      }
    });

    test('a Personal account (named debtor) explained via golden rules mentions receiver/giver', () {
      final debtorEntry = JournalEntry(
        transactionText: 'Sold goods to Ram on credit ₹3000',
        lines: [
          JournalLine(account: ChartOfAccounts.debtor('Ram'), side: EntrySide.debit, amount: 3000),
          const JournalLine(account: ChartOfAccounts.sales, side: EntrySide.credit, amount: 3000),
        ],
        narration: '(Being goods sold to Ram on credit)',
      );
      final solution = AccountingSolver.explainEntry(debtorEntry, board: Board.gseb);
      final ramStep = solution.steps.firstWhere((s) => s.title.contains('Ram'));
      expect(ramStep.reasoning, contains('Personal'));
      expect(ramStep.reasoning, contains('receiver'));
    });

    test('a Nominal account (expense) explained via golden rules mentions expenses/losses', () {
      final rentEntry = JournalEntry(
        transactionText: 'Paid rent ₹2000',
        lines: [
          const JournalLine(account: ChartOfAccounts.rentExpense, side: EntrySide.debit, amount: 2000),
          const JournalLine(account: ChartOfAccounts.cash, side: EntrySide.credit, amount: 2000),
        ],
        narration: '(Being rent paid)',
      );
      final solution = AccountingSolver.explainEntry(rentEntry, board: Board.gseb);
      final rentStep = solution.steps.firstWhere((s) => s.title.contains('Rent'));
      expect(rentStep.reasoning, contains('Nominal'));
      expect(rentStep.reasoning, contains('expense'));
    });

    test('default board (no argument passed) still works without throwing', () {
      expect(() => AccountingSolver.explainEntry(entry), returnsNormally);
    });
  });

  group('Board differentiation does not affect correctness', () {
    test('generated journal entries balance identically regardless of board', () {
      for (final board in [Board.gseb, Board.cbse]) {
        final problem = ProblemGenerator.generateJournalLedgerTrialBalance(
          board: board,
          schoolClass: 11,
          difficulty: 3,
        );
        for (final e in problem.transactions) {
          expect(e.isBalanced, isTrue, reason: 'Failed for board $board');
        }
      }
    });
  });
}
