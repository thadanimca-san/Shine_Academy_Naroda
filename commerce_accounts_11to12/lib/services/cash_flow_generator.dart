import 'dart:math';

import '../models/cash_flow_model.dart';
import '../models/problem_model.dart';
import 'cash_flow_solver.dart';

/// Generates randomized Cash Flow Statement problems. Amounts are kept
/// in ranges that produce a sensible, always-solvable scenario — in
/// particular the closing cash balance is checked to stay non-negative,
/// since a real Balance Sheet could never show negative cash.
class CashFlowGenerator {
  CashFlowGenerator._();

  static final Random _rand = Random();

  static GeneratedCashFlowProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    late CashFlowBalanceSheetData data;
    late var result = _tryGenerate(difficulty);
    data = result.$1;
    var solved = result.$2;

    // Regenerate if closing cash would be negative (rare with these
    // ranges, but guard anyway since a negative cash balance is not a
    // valid real-world Balance Sheet figure).
    var attempts = 0;
    while (solved.closingCash < 0 && attempts < 20) {
      result = _tryGenerate(difficulty);
      data = result.$1;
      solved = result.$2;
      attempts++;
    }

    return GeneratedCashFlowProblem(
      id: 'CF-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      data: data,
      result: solved,
    );
  }

  static (CashFlowBalanceSheetData, CashFlowResult) _tryGenerate(int difficulty) {
    final netProfit = _round(30000 + _rand.nextDouble() * 70000);
    final depreciation = _round(5000 + _rand.nextDouble() * 15000);

    final debtorsOpening = _round(20000 + _rand.nextDouble() * 20000);
    final debtorsClosing = _round(debtorsOpening * (0.7 + _rand.nextDouble() * 0.6));
    final stockOpening = difficulty >= 2 ? _round(15000 + _rand.nextDouble() * 15000) : 0.0;
    final stockClosing = difficulty >= 2 ? _round(stockOpening * (0.7 + _rand.nextDouble() * 0.6)) : 0.0;
    final creditorsOpening = difficulty >= 2 ? _round(10000 + _rand.nextDouble() * 15000) : 0.0;
    final creditorsClosing = difficulty >= 2 ? _round(creditorsOpening * (0.7 + _rand.nextDouble() * 0.6)) : 0.0;
    final outstandingOpening = difficulty >= 4 ? _round(2000 + _rand.nextDouble() * 5000) : 0.0;
    final outstandingClosing = difficulty >= 4 ? _round(outstandingOpening * (0.7 + _rand.nextDouble() * 0.6)) : 0.0;

    final machineryPurchased = difficulty >= 3 ? _round(20000 + _rand.nextDouble() * 40000) : 0.0;
    final machinerySold = difficulty >= 5 ? _round(5000 + _rand.nextDouble() * 10000) : 0.0;

    final loanRaised = difficulty >= 3 && _rand.nextBool() ? _round(20000 + _rand.nextDouble() * 30000) : 0.0;
    final loanRepaid = difficulty >= 4 && !(_rand.nextBool()) ? _round(10000 + _rand.nextDouble() * 15000) : 0.0;
    final sharesIssued = difficulty >= 5 && _rand.nextBool() ? _round(30000 + _rand.nextDouble() * 40000) : 0.0;

    final openingCash = _round(15000 + _rand.nextDouble() * 25000);

    final data = CashFlowBalanceSheetData(
      netProfitBeforeTax: netProfit,
      depreciationForYear: depreciation,
      debtorsOpening: debtorsOpening,
      debtorsClosing: debtorsClosing,
      stockOpening: stockOpening,
      stockClosing: stockClosing,
      creditorsOpening: creditorsOpening,
      creditorsClosing: creditorsClosing,
      outstandingExpensesOpening: outstandingOpening,
      outstandingExpensesClosing: outstandingClosing,
      machineryPurchased: machineryPurchased,
      machinerySold: machinerySold,
      loanRaised: loanRaised,
      loanRepaid: loanRepaid,
      sharesIssuedForCash: sharesIssued,
      openingCashAndBank: openingCash,
    );

    return (data, CashFlowSolver.solve(data));
  }

  static double _round(double v) => (v / 100).round() * 100.0;
}

class GeneratedCashFlowProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final CashFlowBalanceSheetData data;
  final CashFlowResult result;

  const GeneratedCashFlowProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.data,
    required this.result,
  });
}
