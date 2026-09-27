import '../models/cash_book_model.dart';

/// Deterministic solver for the Double Column Cash Book: totals both
/// sides and derives the closing Cash and Bank balances that are carried
/// down. Same single-source-of-truth principle as [AccountingSolver] —
/// this is what backs both the student's checked attempt and the
/// teacher's printed answer key.
class CashBookSolver {
  CashBookSolver._();

  static CashBookTotals solve(List<CashBookTransaction> transactions, {double openingCash = 0, double openingBank = 0}) {
    double cashReceipts = openingCash;
    double bankReceipts = openingBank;
    double discountAllowed = 0;
    double cashPayments = 0;
    double bankPayments = 0;
    double discountReceived = 0;

    for (final tx in transactions) {
      final r = tx.receiptRow;
      final p = tx.paymentRow;
      if (r != null) {
        cashReceipts += r.cashAmount ?? 0;
        bankReceipts += r.bankAmount ?? 0;
        discountAllowed += r.discountAmount ?? 0;
      }
      if (p != null) {
        cashPayments += p.cashAmount ?? 0;
        bankPayments += p.bankAmount ?? 0;
        discountReceived += p.discountAmount ?? 0;
      }
    }

    return CashBookTotals(
      totalCashReceipts: cashReceipts,
      totalBankReceipts: bankReceipts,
      totalDiscountAllowed: discountAllowed,
      totalCashPayments: cashPayments,
      totalBankPayments: bankPayments,
      totalDiscountReceived: discountReceived,
      closingCashBalance: cashReceipts - cashPayments,
      closingBankBalance: bankReceipts - bankPayments,
    );
  }
}
