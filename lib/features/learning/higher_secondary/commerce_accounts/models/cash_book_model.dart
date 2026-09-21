/// One side (receipts or payments) of one row in a Double Column Cash
/// Book. A "contra" entry (cash deposited into bank / cash withdrawn from
/// bank for office use) hits both the Cash and Bank columns of the same
/// side pairing and is marked with [isContra] so it can be flagged "C" in
/// the L.F. column, per how GSEB/CBSE textbooks present it.
class CashBookRow {
  final String particulars;
  final double? cashAmount;
  final double? bankAmount;
  final double? discountAmount;
  final bool isContra;

  const CashBookRow({
    required this.particulars,
    this.cashAmount,
    this.bankAmount,
    this.discountAmount,
    this.isContra = false,
  });
}

/// A transaction as given in the question, before being split into its
/// receipts-side and/or payments-side cash book rows. Kept separate from
/// [CashBookRow] because one transaction (e.g. a contra entry) produces
/// rows on both sides.
class CashBookTransaction {
  final String transactionText;
  final CashBookRow? receiptRow;
  final CashBookRow? paymentRow;

  const CashBookTransaction({
    required this.transactionText,
    this.receiptRow,
    this.paymentRow,
  });
}

class CashBookTotals {
  final double totalCashReceipts;
  final double totalBankReceipts;
  final double totalDiscountAllowed;
  final double totalCashPayments;
  final double totalBankPayments;
  final double totalDiscountReceived;
  final double closingCashBalance;
  final double closingBankBalance;

  const CashBookTotals({
    required this.totalCashReceipts,
    required this.totalBankReceipts,
    required this.totalDiscountAllowed,
    required this.totalCashPayments,
    required this.totalBankPayments,
    required this.totalDiscountReceived,
    required this.closingCashBalance,
    required this.closingBankBalance,
  });
}
