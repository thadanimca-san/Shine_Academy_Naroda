import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/cash_book_generator.dart';
import 'package:commerce_accounts_11to12/services/cash_book_solver.dart';

void main() {
  group('CashBookSolver', () {
    test('closing cash and bank balances never go negative', () {
      for (var i = 0; i < 50; i++) {
        final problem = CashBookGenerator.generate(
          board: Board.gseb,
          schoolClass: 11,
          difficulty: (i % 5) + 1,
        );
        final totals = CashBookSolver.solve(
          problem.transactions,
          openingCash: problem.openingCash,
          openingBank: problem.openingBank,
        );
        expect(totals.closingCashBalance, greaterThanOrEqualTo(-0.01),
            reason: 'Negative cash balance for problem ${problem.id}');
        expect(totals.closingBankBalance, greaterThanOrEqualTo(-0.01),
            reason: 'Negative bank balance for problem ${problem.id}');
      }
    });

    test('contra entries post equal amounts to both cash and bank sides', () {
      final problem = CashBookGenerator.generate(
        board: Board.cbse,
        schoolClass: 12,
        difficulty: 5,
        transactionCount: 12,
      );
      for (final tx in problem.transactions) {
        if (tx.receiptRow?.isContra == true || tx.paymentRow?.isContra == true) {
          final receiptAmt = tx.receiptRow?.cashAmount ?? tx.receiptRow?.bankAmount ?? 0;
          final paymentAmt = tx.paymentRow?.cashAmount ?? tx.paymentRow?.bankAmount ?? 0;
          expect(receiptAmt, closeTo(paymentAmt, 0.01), reason: 'Contra mismatch: ${tx.transactionText}');
        }
      }
    });

    test('closing balance equals opening plus receipts minus payments', () {
      final problem = CashBookGenerator.generate(board: Board.gseb, schoolClass: 11, difficulty: 4, transactionCount: 10);
      final totals = CashBookSolver.solve(
        problem.transactions,
        openingCash: problem.openingCash,
        openingBank: problem.openingBank,
      );
      expect(totals.closingCashBalance, closeTo(totals.totalCashReceipts - totals.totalCashPayments, 0.01));
      expect(totals.closingBankBalance, closeTo(totals.totalBankReceipts - totals.totalBankPayments, 0.01));
    });
  });
}
