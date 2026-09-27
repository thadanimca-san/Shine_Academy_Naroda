import '../models/brs_model.dart';
import '../models/solution_model.dart';

/// Deterministic solver for Bank Reconciliation Statements. Given a Cash
/// Book balance and a list of reconciling items, derives the Pass Book
/// balance (or vice versa) — a pure arithmetic reconciliation, so the
/// same computation backs student hints and the printed answer key.
class BrsSolver {
  BrsSolver._();

  static double computePassBookBalanceFromCashBook(double cashBookBalance, List<BrsItem> items) {
    var balance = cashBookBalance;
    for (final item in items) {
      balance += item.effectOnPassBookBalance == BrsAdjustment.add ? item.amount : -item.amount;
    }
    return balance;
  }

  static double computeCashBookBalanceFromPassBook(double passBookBalance, List<BrsItem> items) {
    var balance = passBookBalance;
    for (final item in items) {
      balance += item.effectOnCashBookBalance == BrsAdjustment.add ? item.amount : -item.amount;
    }
    return balance;
  }

  static List<SolutionStep> explainStartingFromCashBook(double cashBookBalance, List<BrsItem> items) {
    final steps = <SolutionStep>[
      SolutionStep(title: 'Start', reasoning: 'Balance as per Cash Book = ${_fmt(cashBookBalance)}'),
    ];
    var running = cashBookBalance;
    for (final item in items) {
      final isAdd = item.effectOnPassBookBalance == BrsAdjustment.add;
      running += isAdd ? item.amount : -item.amount;
      steps.add(SolutionStep(
        title: item.description,
        reasoning: '${isAdd ? "Add" : "Less"} ${_fmt(item.amount)} '
            '(running balance: ${_fmt(running)})',
      ));
    }
    steps.add(SolutionStep(title: 'Result', reasoning: 'Balance as per Pass Book = ${_fmt(running)}'));
    return steps;
  }

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return '₹${isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2)}';
  }
}
