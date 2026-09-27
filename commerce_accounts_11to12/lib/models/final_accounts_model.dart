/// A single trial-balance-style balance feeding into Final Accounts:
/// e.g. "Opening Stock", "Purchases", "Wages" on the debit side, or
/// "Sales", "Discount Received" on the credit side. Kept as plain
/// name+amount (not the full [Account] model) since Final Accounts
/// problems are given as a trial balance extract, not journal entries.
class TrialBalanceItem {
  final String name;
  final double debitAmount;
  final double creditAmount;

  const TrialBalanceItem({required this.name, this.debitAmount = 0, this.creditAmount = 0});
}

/// The handful of adjustment types GSEB/CBSE Class 11-12 syllabus covers.
/// Each has a well-defined dual effect (it always touches at least two of
/// Trading A/c, P&L A/c, Balance Sheet), which is exactly why adjustments
/// are the hard part of this topic for students.
enum AdjustmentType {
  closingStock,
  outstandingExpense,
  prepaidExpense,
  accruedIncome,
  incomeReceivedInAdvance,
  depreciation,
  badDebts,
  provisionForDoubtfulDebts,
}

class Adjustment {
  final AdjustmentType type;
  final String relatedItemName;
  final double amount;
  final String description;

  const Adjustment({
    required this.type,
    required this.relatedItemName,
    required this.amount,
    required this.description,
  });
}

/// One line of a prepared statement (Trading A/c, P&L A/c, or Balance
/// Sheet), kept generic so all three statements can reuse the same
/// rendering widget/PDF table.
class StatementLine {
  final String particulars;
  final double amount;
  final bool isTotal;

  const StatementLine({required this.particulars, required this.amount, this.isTotal = false});
}

class FinalAccountsResult {
  final List<StatementLine> tradingAccountDebit;
  final List<StatementLine> tradingAccountCredit;
  final double grossProfit; // negative = gross loss

  final List<StatementLine> profitLossDebit;
  final List<StatementLine> profitLossCredit;
  final double netProfit; // negative = net loss

  final List<StatementLine> balanceSheetLiabilities;
  final List<StatementLine> balanceSheetAssets;

  const FinalAccountsResult({
    required this.tradingAccountDebit,
    required this.tradingAccountCredit,
    required this.grossProfit,
    required this.profitLossDebit,
    required this.profitLossCredit,
    required this.netProfit,
    required this.balanceSheetLiabilities,
    required this.balanceSheetAssets,
  });

  double get totalLiabilities => balanceSheetLiabilities.fold(0.0, (s, l) => s + l.amount);
  double get totalAssets => balanceSheetAssets.fold(0.0, (s, l) => s + l.amount);
  bool get balanceSheetTallies => (totalLiabilities - totalAssets).abs() < 0.5;
}
