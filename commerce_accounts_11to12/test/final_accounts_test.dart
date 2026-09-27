import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/final_accounts_model.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/final_accounts_generator.dart';

void main() {
  group('FinalAccountsSolver via generator', () {
    test('Balance Sheet always tallies (Liabilities == Assets)', () {
      for (var i = 0; i < 50; i++) {
        final problem = FinalAccountsGenerator.generate(
          board: Board.gseb,
          schoolClass: 11,
          difficulty: (i % 5) + 1,
        );
        expect(problem.result.balanceSheetTallies, isTrue,
            reason: 'BS mismatch for ${problem.id}: '
                'Liabilities ${problem.result.totalLiabilities} vs Assets ${problem.result.totalAssets} '
                '(diff ${problem.result.totalLiabilities - problem.result.totalAssets})');
      }
    });

    test('Gross Profit correctly carries into P&L Account', () {
      final problem = FinalAccountsGenerator.generate(board: Board.cbse, schoolClass: 12, difficulty: 3);
      final r = problem.result;
      if (r.grossProfit > 0) {
        final creditLine = r.profitLossCredit.firstWhere((l) => l.particulars == 'Gross Profit b/d');
        expect(creditLine.amount, closeTo(r.grossProfit, 0.01));
      } else {
        final debitLine = r.profitLossDebit.firstWhere((l) => l.particulars == 'Gross Loss b/d');
        expect(debitLine.amount, closeTo(-r.grossProfit, 0.01));
      }
    });

    test('Net Profit correctly flows into Capital on the Balance Sheet', () {
      final problem = FinalAccountsGenerator.generate(board: Board.gseb, schoolClass: 11, difficulty: 2);
      final expectedCapital = problem.input.capital + problem.result.netProfit - problem.input.drawings;
      final capitalLine = problem.result.balanceSheetLiabilities.firstWhere((l) => l.particulars == 'Capital');
      expect(capitalLine.amount, closeTo(expectedCapital, 0.01));
    });

    test('closing stock appears in both Trading A/c credit and Balance Sheet assets with the same amount', () {
      final problem = FinalAccountsGenerator.generate(board: Board.gseb, schoolClass: 11, difficulty: 1);
      final tradingStock = problem.result.tradingAccountCredit.firstWhere((l) => l.particulars == 'Closing Stock');
      final bsStock = problem.result.balanceSheetAssets.firstWhere((l) => l.particulars == 'Closing Stock');
      expect(tradingStock.amount, closeTo(bsStock.amount, 0.01));
    });

    test('depreciation reduces the asset on the Balance Sheet and appears as a P&L expense', () {
      final problem = FinalAccountsGenerator.generate(board: Board.cbse, schoolClass: 11, difficulty: 3);
      final depAdjustment = problem.adjustments.firstWhere((a) => a.type.toString().contains('depreciation'));
      final plLine = problem.result.profitLossDebit.firstWhere((l) => l.particulars.contains('Depreciation'));
      expect(plLine.amount, closeTo(depAdjustment.amount, 0.01));

      final bsFurniture = problem.result.balanceSheetAssets.firstWhere((l) => l.particulars == 'Furniture');
      expect(bsFurniture.amount, closeTo(problem.input.furniture - depAdjustment.amount, 0.01));
    });

    test('Class 12 produces structurally harder adjustment combinations than Class 11 at the same difficulty', () {
      for (var i = 0; i < 30; i++) {
        final class11 = FinalAccountsGenerator.generate(board: Board.gseb, schoolClass: 11, difficulty: 5);
        final class12 = FinalAccountsGenerator.generate(board: Board.gseb, schoolClass: 12, difficulty: 5);

        // Class 11 at max difficulty never sees Bad Debts written off or
        // accrued/advance income — those are Class-12-only complexity.
        expect(class11.adjustments.any((a) => a.type == AdjustmentType.badDebts), isFalse);
        expect(class11.adjustments.any((a) => a.type == AdjustmentType.accruedIncome), isFalse);
        expect(class11.adjustments.any((a) => a.type == AdjustmentType.incomeReceivedInAdvance), isFalse);

        // Class 12 at the same difficulty does present them.
        expect(class12.adjustments.any((a) => a.type == AdjustmentType.badDebts), isTrue);
        expect(class12.adjustments.any((a) => a.type == AdjustmentType.accruedIncome), isTrue);
        expect(class12.adjustments.any((a) => a.type == AdjustmentType.incomeReceivedInAdvance), isTrue);

        // Both remain internally consistent regardless of the extra
        // complexity — correctness must never depend on class.
        expect(class12.result.balanceSheetTallies, isTrue);
      }
    });

    test('Class 12 provision for doubtful debts is based on debtors net of the further bad debts written off', () {
      final problem = FinalAccountsGenerator.generate(board: Board.gseb, schoolClass: 12, difficulty: 5);
      final badDebts = problem.adjustments.firstWhere((a) => a.type == AdjustmentType.badDebts);
      final provision = problem.adjustments.firstWhere((a) => a.type == AdjustmentType.provisionForDoubtfulDebts);
      final bsDebtors = problem.result.balanceSheetAssets.firstWhere((l) => l.particulars == 'Debtors');
      expect(bsDebtors.amount, closeTo(problem.input.debtors - badDebts.amount - provision.amount, 0.01));
    });
  });
}
