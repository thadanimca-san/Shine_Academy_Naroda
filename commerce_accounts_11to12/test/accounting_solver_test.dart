import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/account_model.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/accounting_solver.dart';
import 'package:commerce_accounts_11to12/services/problem_generator.dart';

void main() {
  group('AccountingSolver', () {
    test('every generated journal entry is balanced', () {
      for (var i = 0; i < 30; i++) {
        final problem = ProblemGenerator.generateJournalLedgerTrialBalance(
          board: Board.gseb,
          schoolClass: 11,
          difficulty: (i % 5) + 1,
        );
        for (final entry in problem.transactions) {
          expect(entry.isBalanced, isTrue, reason: 'Unbalanced: ${entry.transactionText}');
        }
      }
    });

    test('ledger posting totals match journal totals for every account', () {
      final problem = ProblemGenerator.generateJournalLedgerTrialBalance(
        board: Board.cbse,
        schoolClass: 12,
        difficulty: 4,
        transactionCount: 8,
      );
      final ledgers = AccountingSolver.postToLedger(problem.transactions);

      final expectedDebitByAccount = <String, double>{};
      final expectedCreditByAccount = <String, double>{};
      for (final entry in problem.transactions) {
        for (final line in entry.lines) {
          final key = '${line.account.name}|${line.account.category}';
          if (line.side == EntrySide.debit) {
            expectedDebitByAccount[key] = (expectedDebitByAccount[key] ?? 0) + line.amount;
          } else {
            expectedCreditByAccount[key] = (expectedCreditByAccount[key] ?? 0) + line.amount;
          }
        }
      }

      for (final ledger in ledgers) {
        final key = '${ledger.account.name}|${ledger.account.category}';
        expect(ledger.totalDebit, closeTo(expectedDebitByAccount[key] ?? 0, 0.01));
        expect(ledger.totalCredit, closeTo(expectedCreditByAccount[key] ?? 0, 0.01));
      }
    });

    test('trial balance always balances (Dr total == Cr total)', () {
      for (var i = 0; i < 30; i++) {
        final problem = ProblemGenerator.generateJournalLedgerTrialBalance(
          board: Board.gseb,
          schoolClass: 11,
          difficulty: (i % 5) + 1,
        );
        final ledgers = AccountingSolver.postToLedger(problem.transactions);
        final tb = AccountingSolver.buildTrialBalance(ledgers);
        expect(tb.isBalanced, isTrue,
            reason: 'TB mismatch: Dr ${tb.totalDebit} vs Cr ${tb.totalCredit}');
      }
    });

    test('explainEntry produces one reasoning step per line plus a check step', () {
      final problem = ProblemGenerator.generateJournalLedgerTrialBalance(
        board: Board.gseb,
        schoolClass: 11,
        difficulty: 1,
        transactionCount: 4,
      );
      final entry = problem.transactions.first;
      final solution = AccountingSolver.explainEntry(entry);
      expect(solution.steps.length, entry.lines.length + 1);
    });

    test('Class 12 generates at least as many transactions as Class 11 at the same difficulty, and always balances', () {
      for (var i = 0; i < 20; i++) {
        final difficulty = (i % 5) + 1;
        final class11 = ProblemGenerator.generateJournalLedgerTrialBalance(
          board: Board.gseb,
          schoolClass: 11,
          difficulty: difficulty,
        );
        final class12 = ProblemGenerator.generateJournalLedgerTrialBalance(
          board: Board.gseb,
          schoolClass: 12,
          difficulty: difficulty,
        );
        expect(class12.transactions.length, greaterThanOrEqualTo(class11.transactions.length),
            reason: 'difficulty $difficulty: Class 12 had fewer transactions than Class 11');

        for (final entry in class12.transactions) {
          expect(entry.isBalanced, isTrue);
        }
        final ledgers = AccountingSolver.postToLedger(class12.transactions);
        expect(AccountingSolver.buildTrialBalance(ledgers).isBalanced, isTrue);
      }
    });
  });
}
