/// The three activity classifications every cash flow item falls under —
/// the core skill this topic tests.
enum CashFlowActivity { operating, investing, financing }

/// One line of the finished Cash Flow Statement.
class CashFlowLine {
  final String particulars;
  final double amount; // negative = cash outflow
  final bool isSubtotal;

  const CashFlowLine({required this.particulars, required this.amount, this.isSubtotal = false});
}

/// Balance Sheet extract for two consecutive years — only the handful of
/// items GSEB/CBSE Class 12 Cash Flow problems actually use. Every field
/// is the year-end balance (not the movement); the solver derives
/// movements itself.
class CashFlowBalanceSheetData {
  final double netProfitBeforeTax;
  final double depreciationForYear;

  final double debtorsOpening;
  final double debtorsClosing;
  final double stockOpening;
  final double stockClosing;
  final double creditorsOpening;
  final double creditorsClosing;
  final double outstandingExpensesOpening;
  final double outstandingExpensesClosing;

  final double machineryPurchased;
  final double machinerySold;

  final double loanRaised;
  final double loanRepaid;
  final double sharesIssuedForCash;

  final double openingCashAndBank;

  const CashFlowBalanceSheetData({
    required this.netProfitBeforeTax,
    required this.depreciationForYear,
    this.debtorsOpening = 0,
    this.debtorsClosing = 0,
    this.stockOpening = 0,
    this.stockClosing = 0,
    this.creditorsOpening = 0,
    this.creditorsClosing = 0,
    this.outstandingExpensesOpening = 0,
    this.outstandingExpensesClosing = 0,
    this.machineryPurchased = 0,
    this.machinerySold = 0,
    this.loanRaised = 0,
    this.loanRepaid = 0,
    this.sharesIssuedForCash = 0,
    required this.openingCashAndBank,
  });
}

class CashFlowResult {
  final List<CashFlowLine> operatingLines;
  final double netCashFromOperating;
  final List<CashFlowLine> investingLines;
  final double netCashFromInvesting;
  final List<CashFlowLine> financingLines;
  final double netCashFromFinancing;
  final double netIncreaseInCash;
  final double openingCash;
  final double closingCash;

  const CashFlowResult({
    required this.operatingLines,
    required this.netCashFromOperating,
    required this.investingLines,
    required this.netCashFromInvesting,
    required this.financingLines,
    required this.netCashFromFinancing,
    required this.netIncreaseInCash,
    required this.openingCash,
    required this.closingCash,
  });
}
