import 'dart:math';

import '../models/brs_model.dart';
import '../models/problem_model.dart';
import 'brs_solver.dart';

/// Generates randomized BRS problems using the standard set of
/// reconciling items GSEB/CBSE Class 11 covers. Each item pattern here
/// encodes its own correct Cash-Book-to-Pass-Book adjustment direction —
/// that direction rule is exactly what the topic tests, so, as with
/// Rectification, the template *is* the worked-out logic.
class BrsGenerator {
  BrsGenerator._();

  static final Random _rand = Random();

  static final List<BrsItem Function(double)> _itemPatterns = [
    // Cheques issued but not yet presented for payment: Cash Book already
    // shows them paid out (lower balance); bank hasn't cleared them yet
    // (still higher there) -> add back when going Cash Book -> Pass Book.
    (amt) => BrsItem(
          description: 'Cheques issued but not yet presented for payment ₹${_fmt(amt)}',
          amount: amt,
          effectOnPassBookBalance: BrsAdjustment.add,
        ),
    // Cheques deposited but not yet collected/credited by the bank: Cash
    // Book already shows them received (higher balance); bank hasn't
    // credited yet -> subtract when going Cash Book -> Pass Book.
    (amt) => BrsItem(
          description: 'Cheques deposited into bank but not yet collected ₹${_fmt(amt)}',
          amount: amt,
          effectOnPassBookBalance: BrsAdjustment.subtract,
        ),
    // Bank charges debited directly by the bank, not yet entered in Cash
    // Book -> Cash Book balance is overstated relative to Pass Book ->
    // subtract when going Cash Book -> Pass Book.
    (amt) => BrsItem(
          description: 'Bank charges debited by the bank but not recorded in Cash Book ₹${_fmt(amt)}',
          amount: amt,
          effectOnPassBookBalance: BrsAdjustment.subtract,
        ),
    // Interest allowed by the bank, not yet entered in Cash Book -> Cash
    // Book balance is understated -> add when going Cash Book -> Pass Book.
    (amt) => BrsItem(
          description: 'Interest allowed by the bank but not recorded in Cash Book ₹${_fmt(amt)}',
          amount: amt,
          effectOnPassBookBalance: BrsAdjustment.add,
        ),
    // A customer's cheque directly deposited by them into the firm's bank
    // account, not yet entered in Cash Book -> add when going
    // Cash Book -> Pass Book.
    (amt) => BrsItem(
          description: "A customer directly deposited ₹${_fmt(amt)} into the firm's bank account, not yet recorded in Cash Book",
          amount: amt,
          effectOnPassBookBalance: BrsAdjustment.add,
        ),
    // A dishonoured cheque (customer's cheque bounced) debited by the
    // bank but not yet recorded in Cash Book -> subtract when going
    // Cash Book -> Pass Book.
    (amt) => BrsItem(
          description: "A customer's cheque for ₹${_fmt(amt)} was dishonoured by the bank but not yet recorded in Cash Book",
          amount: amt,
          effectOnPassBookBalance: BrsAdjustment.subtract,
        ),
  ];

  static GeneratedBrsProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
    int? itemCount,
  }) {
    final count = itemCount ?? (2 + difficulty).clamp(2, 6);
    final cashBookBalance = _round(10000 + _rand.nextDouble() * 90000);

    final shuffled = List.of(_itemPatterns)..shuffle(_rand);
    final items = shuffled.take(count).map((pattern) {
      final amt = _round(200 + _rand.nextDouble() * 4800);
      return pattern(amt);
    }).toList();

    final passBookBalance = BrsSolver.computePassBookBalanceFromCashBook(cashBookBalance, items);

    return GeneratedBrsProblem(
      id: 'BRS-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      cashBookBalance: cashBookBalance,
      items: items,
      passBookBalance: passBookBalance,
    );
  }

  static double _round(double v) => (v / 10).round() * 10.0;

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}

class GeneratedBrsProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final double cashBookBalance;
  final List<BrsItem> items;
  final double passBookBalance;

  const GeneratedBrsProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.cashBookBalance,
    required this.items,
    required this.passBookBalance,
  });
}
