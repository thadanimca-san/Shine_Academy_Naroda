import '../models/cash_flow_model.dart';

/// Deterministic solver for the Cash Flow Statement (Indirect Method) —
/// the method GSEB/CBSE Class 12 syllabus focuses on. Core rules
/// encoded here, each of which is exactly what the topic is teaching:
///
/// Operating Activities: start from Net Profit, add back non-cash
/// expenses (Depreciation), then adjust for changes in working capital —
/// an INCREASE in a current asset (Debtors, Stock) is a cash OUTFLOW
/// (cash tied up in it), a DECREASE is an inflow; an INCREASE in a
/// current liability (Creditors, Outstanding Expenses) is a cash INFLOW
/// (paying later frees up cash now), a DECREASE is an outflow.
///
/// Investing Activities: purchase of fixed assets is an outflow, sale
/// is an inflow.
///
/// Financing Activities: raising a loan or issuing shares is an inflow,
/// repaying a loan is an outflow.
class CashFlowSolver {
  CashFlowSolver._();

  static CashFlowResult solve(CashFlowBalanceSheetData d) {
    // --- Operating Activities ---
    final operating = <CashFlowLine>[
      CashFlowLine(particulars: 'Net Profit before Tax', amount: d.netProfitBeforeTax),
      if (d.depreciationForYear > 0)
        CashFlowLine(particulars: 'Add: Depreciation', amount: d.depreciationForYear),
    ];

    final debtorsChange = d.debtorsClosing - d.debtorsOpening;
    if (debtorsChange != 0) {
      operating.add(CashFlowLine(
        particulars: debtorsChange > 0 ? 'Less: Increase in Debtors' : 'Add: Decrease in Debtors',
        amount: -debtorsChange,
      ));
    }

    final stockChange = d.stockClosing - d.stockOpening;
    if (stockChange != 0) {
      operating.add(CashFlowLine(
        particulars: stockChange > 0 ? 'Less: Increase in Stock' : 'Add: Decrease in Stock',
        amount: -stockChange,
      ));
    }

    final creditorsChange = d.creditorsClosing - d.creditorsOpening;
    if (creditorsChange != 0) {
      operating.add(CashFlowLine(
        particulars: creditorsChange > 0 ? 'Add: Increase in Creditors' : 'Less: Decrease in Creditors',
        amount: creditorsChange,
      ));
    }

    final outstandingChange = d.outstandingExpensesClosing - d.outstandingExpensesOpening;
    if (outstandingChange != 0) {
      operating.add(CashFlowLine(
        particulars: outstandingChange > 0 ? 'Add: Increase in Outstanding Expenses' : 'Less: Decrease in Outstanding Expenses',
        amount: outstandingChange,
      ));
    }

    final netOperating = operating.fold(0.0, (s, l) => s + l.amount);
    operating.add(CashFlowLine(particulars: 'Net Cash from Operating Activities', amount: netOperating, isSubtotal: true));

    // --- Investing Activities ---
    final investing = <CashFlowLine>[
      if (d.machineryPurchased > 0) CashFlowLine(particulars: 'Purchase of Machinery', amount: -d.machineryPurchased),
      if (d.machinerySold > 0) CashFlowLine(particulars: 'Sale of Machinery', amount: d.machinerySold),
    ];
    final netInvesting = investing.fold(0.0, (s, l) => s + l.amount);
    investing.add(CashFlowLine(particulars: 'Net Cash used in Investing Activities', amount: netInvesting, isSubtotal: true));

    // --- Financing Activities ---
    final financing = <CashFlowLine>[
      if (d.loanRaised > 0) CashFlowLine(particulars: 'Proceeds from Loan', amount: d.loanRaised),
      if (d.loanRepaid > 0) CashFlowLine(particulars: 'Repayment of Loan', amount: -d.loanRepaid),
      if (d.sharesIssuedForCash > 0) CashFlowLine(particulars: 'Proceeds from Issue of Shares', amount: d.sharesIssuedForCash),
    ];
    final netFinancing = financing.fold(0.0, (s, l) => s + l.amount);
    financing.add(CashFlowLine(particulars: 'Net Cash from Financing Activities', amount: netFinancing, isSubtotal: true));

    final netIncrease = netOperating + netInvesting + netFinancing;
    final closingCash = d.openingCashAndBank + netIncrease;

    return CashFlowResult(
      operatingLines: operating,
      netCashFromOperating: netOperating,
      investingLines: investing,
      netCashFromInvesting: netInvesting,
      financingLines: financing,
      netCashFromFinancing: netFinancing,
      netIncreaseInCash: netIncrease,
      openingCash: d.openingCashAndBank,
      closingCash: closingCash,
    );
  }
}
