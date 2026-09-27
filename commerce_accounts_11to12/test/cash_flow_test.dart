import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/cash_flow_model.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/cash_flow_generator.dart';
import 'package:commerce_accounts_11to12/services/cash_flow_solver.dart';

void main() {
  group('CashFlowSolver', () {
    test('closing cash = opening cash + net increase (arithmetic identity)', () {
      for (var i = 0; i < 30; i++) {
        final problem = CashFlowGenerator.generate(board: Board.gseb, schoolClass: 12, difficulty: (i % 5) + 1);
        final r = problem.result;
        expect(r.closingCash, closeTo(r.openingCash + r.netIncreaseInCash, 0.01), reason: 'Failed for ${problem.id}');
      }
    });

    test('net increase = sum of operating + investing + financing subtotals', () {
      for (var i = 0; i < 30; i++) {
        final problem = CashFlowGenerator.generate(board: Board.cbse, schoolClass: 12, difficulty: (i % 5) + 1);
        final r = problem.result;
        final total = r.netCashFromOperating + r.netCashFromInvesting + r.netCashFromFinancing;
        expect(r.netIncreaseInCash, closeTo(total, 0.01), reason: 'Failed for ${problem.id}');
      }
    });

    test('closing cash is never negative in generated problems', () {
      for (var i = 0; i < 40; i++) {
        final problem = CashFlowGenerator.generate(board: Board.gseb, schoolClass: 12, difficulty: (i % 5) + 1);
        expect(problem.result.closingCash, greaterThanOrEqualTo(0), reason: 'Failed for ${problem.id}');
      }
    });

    test('an increase in Debtors is a cash outflow (subtracted) in Operating Activities', () {
      const data = CashFlowBalanceSheetData(
        netProfitBeforeTax: 50000,
        depreciationForYear: 0,
        debtorsOpening: 10000,
        debtorsClosing: 15000, // increased by 5000
        openingCashAndBank: 20000,
      );
      final result = CashFlowSolver.solve(data);
      final debtorsLine = result.operatingLines.firstWhere((l) => l.particulars.contains('Debtors'));
      expect(debtorsLine.particulars, contains('Increase'));
      expect(debtorsLine.amount, closeTo(-5000, 0.01));
    });

    test('an increase in Creditors is a cash inflow (added) in Operating Activities', () {
      const data = CashFlowBalanceSheetData(
        netProfitBeforeTax: 50000,
        depreciationForYear: 0,
        creditorsOpening: 8000,
        creditorsClosing: 12000, // increased by 4000
        openingCashAndBank: 20000,
      );
      final result = CashFlowSolver.solve(data);
      final creditorsLine = result.operatingLines.firstWhere((l) => l.particulars.contains('Creditors'));
      expect(creditorsLine.particulars, contains('Increase'));
      expect(creditorsLine.amount, closeTo(4000, 0.01));
    });

    test('depreciation is always added back to Net Profit in Operating Activities', () {
      const data = CashFlowBalanceSheetData(
        netProfitBeforeTax: 40000,
        depreciationForYear: 8000,
        openingCashAndBank: 10000,
      );
      final result = CashFlowSolver.solve(data);
      final depLine = result.operatingLines.firstWhere((l) => l.particulars.contains('Depreciation'));
      expect(depLine.amount, closeTo(8000, 0.01));
    });
  });
}
