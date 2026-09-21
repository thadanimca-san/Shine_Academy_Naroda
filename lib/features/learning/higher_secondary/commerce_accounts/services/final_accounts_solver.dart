import '../models/final_accounts_model.dart';

/// Fixed shape of trial balance items this solver understands — matches
/// how GSEB/CBSE Class 11 "Final Accounts of Sole Proprietorship"
/// problems are actually set (a small, standard set of ledger balances),
/// rather than trying to be a fully generic trial-balance-to-statement
/// engine. Every item is optional (defaults to 0) so a problem can pick
/// whichever subset it needs.
class FinalAccountsInput {
  final double openingStock;
  final double purchases;
  final double purchasesReturn;
  final double sales;
  final double salesReturn;
  final double wages;
  final double carriageInwards;
  final double carriageOutwards;
  final double rent;
  final double salaries;
  final double discountAllowed;
  final double discountReceived;
  final double commissionReceived;
  final double debtors;
  final double creditors;
  final double capital;
  final double drawings;
  final double cash;
  final double bank;
  final double furniture;
  final double machinery;

  const FinalAccountsInput({
    this.openingStock = 0,
    this.purchases = 0,
    this.purchasesReturn = 0,
    this.sales = 0,
    this.salesReturn = 0,
    this.wages = 0,
    this.carriageInwards = 0,
    this.carriageOutwards = 0,
    this.rent = 0,
    this.salaries = 0,
    this.discountAllowed = 0,
    this.discountReceived = 0,
    this.commissionReceived = 0,
    this.debtors = 0,
    this.creditors = 0,
    this.capital = 0,
    this.drawings = 0,
    this.cash = 0,
    this.bank = 0,
    this.furniture = 0,
    this.machinery = 0,
  });
}

/// Deterministic solver for Final Accounts of a sole proprietorship:
/// Trading A/c -> Gross Profit, P&L A/c -> Net Profit, Balance Sheet.
/// Adjustments are applied via their well-defined dual/triple effect —
/// e.g. Closing Stock credits Trading A/c AND appears as a Balance Sheet
/// asset; Outstanding Expense adds to the P&L expense AND appears as a
/// Balance Sheet liability. This dual-effect handling is exactly what
/// the topic is teaching, so each adjustment case below *is* the
/// worked-out rule for that adjustment.
class FinalAccountsSolver {
  FinalAccountsSolver._();

  static FinalAccountsResult solve(FinalAccountsInput input, List<Adjustment> adjustments) {
    double closingStock = 0;
    double depreciationFurniture = 0;
    double depreciationMachinery = 0;
    double badDebtsExtra = 0;
    double provisionForDoubtfulDebts = 0;
    final outstandingExpenses = <String, double>{};
    final prepaidExpenses = <String, double>{};
    final accruedIncomes = <String, double>{};
    final incomeReceivedInAdvance = <String, double>{};

    for (final adj in adjustments) {
      switch (adj.type) {
        case AdjustmentType.closingStock:
          closingStock += adj.amount;
        case AdjustmentType.depreciation:
          if (adj.relatedItemName == 'Furniture') {
            depreciationFurniture += adj.amount;
          } else {
            depreciationMachinery += adj.amount;
          }
        case AdjustmentType.badDebts:
          badDebtsExtra += adj.amount;
        case AdjustmentType.provisionForDoubtfulDebts:
          provisionForDoubtfulDebts += adj.amount;
        case AdjustmentType.outstandingExpense:
          outstandingExpenses[adj.relatedItemName] = (outstandingExpenses[adj.relatedItemName] ?? 0) + adj.amount;
        case AdjustmentType.prepaidExpense:
          prepaidExpenses[adj.relatedItemName] = (prepaidExpenses[adj.relatedItemName] ?? 0) + adj.amount;
        case AdjustmentType.accruedIncome:
          accruedIncomes[adj.relatedItemName] = (accruedIncomes[adj.relatedItemName] ?? 0) + adj.amount;
        case AdjustmentType.incomeReceivedInAdvance:
          incomeReceivedInAdvance[adj.relatedItemName] =
              (incomeReceivedInAdvance[adj.relatedItemName] ?? 0) + adj.amount;
      }
    }

    // ---- Trading Account ----
    final netPurchases = input.purchases - input.purchasesReturn;
    final netSales = input.sales - input.salesReturn;
    final wagesTotal = input.wages + (outstandingExpenses['Wages'] ?? 0);

    final tradingDebit = <StatementLine>[
      if (input.openingStock > 0) StatementLine(particulars: 'Opening Stock', amount: input.openingStock),
      StatementLine(particulars: 'Purchases (net)', amount: netPurchases),
      if (wagesTotal > 0) StatementLine(particulars: 'Wages', amount: wagesTotal),
      if (input.carriageInwards > 0) StatementLine(particulars: 'Carriage Inwards', amount: input.carriageInwards),
    ];
    final costSide = tradingDebit.fold(0.0, (s, l) => s + l.amount);
    final tradingCredit = <StatementLine>[
      StatementLine(particulars: 'Sales (net)', amount: netSales),
      if (closingStock > 0) StatementLine(particulars: 'Closing Stock', amount: closingStock),
    ];
    final revenueSide = tradingCredit.fold(0.0, (s, l) => s + l.amount);
    final grossProfit = revenueSide - costSide;

    // ---- Profit & Loss Account ----
    final rentTotal = input.rent + (outstandingExpenses['Rent'] ?? 0) - (prepaidExpenses['Rent'] ?? 0);
    final salariesTotal = input.salaries + (outstandingExpenses['Salaries'] ?? 0) - (prepaidExpenses['Salaries'] ?? 0);
    final netDebtorsForProvision = input.debtors - badDebtsExtra;
    final provisionAmount = provisionForDoubtfulDebts;

    final plDebit = <StatementLine>[
      if (grossProfit < 0) StatementLine(particulars: 'Gross Loss b/d', amount: -grossProfit),
      if (rentTotal > 0) StatementLine(particulars: 'Rent', amount: rentTotal),
      if (salariesTotal > 0) StatementLine(particulars: 'Salaries', amount: salariesTotal),
      if (input.carriageOutwards > 0) StatementLine(particulars: 'Carriage Outwards', amount: input.carriageOutwards),
      if (input.discountAllowed > 0) StatementLine(particulars: 'Discount Allowed', amount: input.discountAllowed),
      if (depreciationFurniture > 0) StatementLine(particulars: 'Depreciation on Furniture', amount: depreciationFurniture),
      if (depreciationMachinery > 0) StatementLine(particulars: 'Depreciation on Machinery', amount: depreciationMachinery),
      if (badDebtsExtra > 0) StatementLine(particulars: 'Bad Debts (additional)', amount: badDebtsExtra),
      if (provisionAmount > 0) StatementLine(particulars: 'Provision for Doubtful Debts', amount: provisionAmount),
    ];
    final expenseSide = plDebit.fold(0.0, (s, l) => s + l.amount);

    final commissionTotal =
        input.commissionReceived + (accruedIncomes['Commission'] ?? 0) - (incomeReceivedInAdvance['Commission'] ?? 0);
    final plCredit = <StatementLine>[
      if (grossProfit > 0) StatementLine(particulars: 'Gross Profit b/d', amount: grossProfit),
      if (input.discountReceived > 0) StatementLine(particulars: 'Discount Received', amount: input.discountReceived),
      if (commissionTotal > 0) StatementLine(particulars: 'Commission Received', amount: commissionTotal),
    ];
    final incomeSide = plCredit.fold(0.0, (s, l) => s + l.amount);
    final netProfit = incomeSide - expenseSide;

    // ---- Balance Sheet ----
    final capitalAfterProfit = input.capital + netProfit - input.drawings;
    final furnitureNet = input.furniture - depreciationFurniture;
    final machineryNet = input.machinery - depreciationMachinery;
    final debtorsNet = netDebtorsForProvision - provisionAmount;

    final liabilities = <StatementLine>[
      StatementLine(particulars: 'Capital', amount: capitalAfterProfit),
      if (input.creditors > 0) StatementLine(particulars: 'Creditors', amount: input.creditors),
      for (final e in outstandingExpenses.entries)
        if (e.value > 0) StatementLine(particulars: 'Outstanding ${e.key}', amount: e.value),
      for (final e in incomeReceivedInAdvance.entries)
        if (e.value > 0) StatementLine(particulars: '${e.key} Received in Advance', amount: e.value),
    ];

    final assets = <StatementLine>[
      if (furnitureNet > 0) StatementLine(particulars: 'Furniture', amount: furnitureNet),
      if (machineryNet > 0) StatementLine(particulars: 'Machinery', amount: machineryNet),
      if (closingStock > 0) StatementLine(particulars: 'Closing Stock', amount: closingStock),
      if (debtorsNet > 0) StatementLine(particulars: 'Debtors', amount: debtorsNet),
      for (final e in prepaidExpenses.entries)
        if (e.value > 0) StatementLine(particulars: 'Prepaid ${e.key}', amount: e.value),
      for (final e in accruedIncomes.entries)
        if (e.value > 0) StatementLine(particulars: 'Accrued ${e.key}', amount: e.value),
      if (input.cash > 0) StatementLine(particulars: 'Cash', amount: input.cash),
      if (input.bank > 0) StatementLine(particulars: 'Bank', amount: input.bank),
    ];

    return FinalAccountsResult(
      tradingAccountDebit: tradingDebit,
      tradingAccountCredit: tradingCredit,
      grossProfit: grossProfit,
      profitLossDebit: plDebit,
      profitLossCredit: plCredit,
      netProfit: netProfit,
      balanceSheetLiabilities: liabilities,
      balanceSheetAssets: assets,
    );
  }
}
