import 'dart:math';

import '../data/chart_of_accounts.dart';
import '../models/cash_book_model.dart';
import '../models/problem_model.dart';

/// Generates a randomized, always-solvable Double Column Cash Book
/// problem. Opening balances and every payment are kept within what's
/// available so the running Cash/Bank balance never goes negative —
/// otherwise the "answer" would be an impossible real-world cash book.
class CashBookGenerator {
  CashBookGenerator._();

  static final Random _rand = Random();

  static GeneratedCashBookProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
    int? transactionCount,
  }) {
    final count = transactionCount ?? (5 + difficulty).clamp(5, 12);
    final openingCash = _round(5000 + _rand.nextDouble() * 15000);
    final openingBank = _round(10000 + _rand.nextDouble() * 40000);

    double runningCash = openingCash;
    double runningBank = openingBank;
    final transactions = <CashBookTransaction>[];

    for (var i = 0; i < count; i++) {
      final kind = _pickKind(difficulty, runningCash, runningBank);
      final tx = _buildTransaction(kind, runningCash, runningBank);
      transactions.add(tx);
      runningCash += (tx.receiptRow?.cashAmount ?? 0) - (tx.paymentRow?.cashAmount ?? 0);
      runningBank += (tx.receiptRow?.bankAmount ?? 0) - (tx.paymentRow?.bankAmount ?? 0);
    }

    return GeneratedCashBookProblem(
      id: 'CB-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      openingCash: openingCash,
      openingBank: openingBank,
      transactions: transactions,
    );
  }

  static _TxKind _pickKind(int difficulty, double cash, double bank) {
    final basicKinds = [_TxKind.cashSale, _TxKind.cashPurchase, _TxKind.cashExpense];
    final advancedKinds = [..._TxKind.values];
    final kinds = difficulty <= 2 ? basicKinds : advancedKinds;

    while (true) {
      final kind = kinds[_rand.nextInt(kinds.length)];
      if (kind == _TxKind.depositToBank && cash < 2000) continue;
      if (kind == _TxKind.withdrawFromBank && bank < 2000) continue;
      if (kind == _TxKind.payByCheque && bank < 2000) continue;
      if ((kind == _TxKind.cashExpense) && cash < 500) continue;
      return kind;
    }
  }

  static CashBookTransaction _buildTransaction(_TxKind kind, double cash, double bank) {
    final person = ChartOfAccounts.personNames[_rand.nextInt(ChartOfAccounts.personNames.length)];
    switch (kind) {
      case _TxKind.cashSale:
        final amt = _round(2000 + _rand.nextDouble() * 10000);
        return CashBookTransaction(
          transactionText: 'Sold goods for cash ₹${_fmt(amt)}',
          receiptRow: CashBookRow(particulars: 'Sales A/c', cashAmount: amt),
        );
      case _TxKind.cashPurchase:
        final amt = _round((1000 + _rand.nextDouble() * 8000).clamp(0, cash * 0.6));
        return CashBookTransaction(
          transactionText: 'Purchased goods for cash ₹${_fmt(amt)}',
          paymentRow: CashBookRow(particulars: 'Purchases A/c', cashAmount: amt),
        );
      case _TxKind.cashExpense:
        final amt = _round((500 + _rand.nextDouble() * 3000).clamp(0, cash * 0.4));
        return CashBookTransaction(
          transactionText: 'Paid rent ₹${_fmt(amt)}',
          paymentRow: CashBookRow(particulars: 'Rent A/c', cashAmount: amt),
        );
      case _TxKind.chequeReceiptFromDebtor:
        final gross = _round(3000 + _rand.nextDouble() * 12000);
        final discount = _round(gross * 0.02);
        final net = gross - discount;
        return CashBookTransaction(
          transactionText: 'Received a cheque from $person ₹${_fmt(net)} in full settlement of ₹${_fmt(gross)}',
          receiptRow: CashBookRow(particulars: person, bankAmount: net, discountAmount: discount),
        );
      case _TxKind.payByCheque:
        final gross = _round((3000 + _rand.nextDouble() * 10000).clamp(0, bank * 0.6));
        final discount = _round(gross * 0.02);
        final net = gross - discount;
        return CashBookTransaction(
          transactionText: 'Paid $person by cheque ₹${_fmt(net)} in full settlement of ₹${_fmt(gross)}',
          paymentRow: CashBookRow(particulars: person, bankAmount: net, discountAmount: discount),
        );
      case _TxKind.depositToBank:
        final amt = _round((1000 + _rand.nextDouble() * 5000).clamp(0, cash * 0.5));
        return CashBookTransaction(
          transactionText: 'Cash deposited into bank ₹${_fmt(amt)}',
          receiptRow: CashBookRow(particulars: 'Bank A/c (Contra)', bankAmount: amt, isContra: true),
          paymentRow: CashBookRow(particulars: 'Cash A/c (Contra)', cashAmount: amt, isContra: true),
        );
      case _TxKind.withdrawFromBank:
        final amt = _round((1000 + _rand.nextDouble() * 5000).clamp(0, bank * 0.5));
        return CashBookTransaction(
          transactionText: 'Cash withdrawn from bank for office use ₹${_fmt(amt)}',
          receiptRow: CashBookRow(particulars: 'Cash A/c (Contra)', cashAmount: amt, isContra: true),
          paymentRow: CashBookRow(particulars: 'Bank A/c (Contra)', bankAmount: amt, isContra: true),
        );
    }
  }

  static double _round(double v) => (v / 100).round() * 100.0;

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}

enum _TxKind { cashSale, cashPurchase, cashExpense, chequeReceiptFromDebtor, payByCheque, depositToBank, withdrawFromBank }

class GeneratedCashBookProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final double openingCash;
  final double openingBank;
  final List<CashBookTransaction> transactions;

  const GeneratedCashBookProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.openingCash,
    required this.openingBank,
    required this.transactions,
  });
}
