import 'dart:math';

import '../data/chart_of_accounts.dart';
import '../models/account_model.dart';
import '../models/problem_model.dart';
import '../models/rectification_model.dart';

/// Generates randomized Rectification of Errors problems. Each error
/// pattern below is hand-derived (the rectifying entry logic is baked
/// into the pattern itself, not computed generically), because
/// rectification genuinely has distinct fix-logic per error type — that
/// is exactly what the topic is teaching, so the template *is* the
/// worked-out rule for that pattern.
class RectificationGenerator {
  RectificationGenerator._();

  static final Random _rand = Random();

  static final _suspense = const Account(name: 'Suspense', category: AccountCategory.asset);

  static GeneratedRectificationProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
    int? caseCount,
  }) {
    final count = caseCount ?? (2 + difficulty).clamp(2, 8);
    final patterns = difficulty <= 2 ? _basicPatterns : _allPatterns;

    final cases = List.generate(count, (_) {
      final pattern = patterns[_rand.nextInt(patterns.length)];
      final amt = _round(500 + _rand.nextDouble() * 9500);
      return pattern(amt);
    });

    return GeneratedRectificationProblem(
      id: 'RECT-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      cases: cases,
    );
  }

  static List<RectificationCase Function(double)> get _basicPatterns => [
        _omittedSalePosting,
        _wrongAmountPosting,
      ];

  static List<RectificationCase Function(double)> get _allPatterns => [
        _omittedSalePosting,
        _wrongAmountPosting,
        _principleError,
        _compensatingSuggestingOnlyOneShown,
        _wrongSideePosting,
      ];

  // One-sided: the Sales Book total itself was undercast, so only the
  // Sales A/c (via the ledger total) is short — no individual debtor's
  // personal account is affected, and the trial balance is thrown out of
  // agreement, so the fix is routed through Suspense A/c.
  static RectificationCase _omittedSalePosting(double amt) {
    return RectificationCase(
      errorDescription: 'Sales Book was undercast by ₹${_fmt(amt)}.',
      errorType: ErrorType.omission,
      effect: ErrorEffect.oneSided,
      rectifyingEntry: JournalEntry(
        transactionText: 'Rectify undercast Sales Book',
        lines: [
          JournalLine(account: _suspense, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.sales, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being undercasting of Sales Book now corrected through Suspense A/c)',
      ),
    );
  }

  // One-sided: Furniture purchase posted to Furniture A/c correctly on
  // debit, but wrong amount credited to Cash — this imbalance can only be
  // caught and fixed via Suspense since only one side was mis-posted.
  static RectificationCase _wrongAmountPosting(double amt) {
    final diff = _round(amt * 0.1 + 100);
    return RectificationCase(
      errorDescription:
          'Furniture purchased for ₹${_fmt(amt)} was posted to the Furniture A/c as ₹${_fmt(amt - diff)}.',
      errorType: ErrorType.commission,
      effect: ErrorEffect.oneSided,
      rectifyingEntry: JournalEntry(
        transactionText: 'Rectify short posting to Furniture A/c',
        lines: [
          JournalLine(account: ChartOfAccounts.furniture, side: EntrySide.debit, amount: diff),
          JournalLine(account: _suspense, side: EntrySide.credit, amount: diff),
        ],
        narration: '(Being under-posting to Furniture A/c now corrected through Suspense A/c)',
      ),
    );
  }

  // Two-sided, error of principle: revenue expenditure (repairs) wrongly
  // debited to an asset account (Machinery) instead of Repairs.
  static RectificationCase _principleError(double amt) {
    return RectificationCase(
      errorDescription: 'Repairs to Machinery ₹${_fmt(amt)} were wrongly debited to Machinery A/c.',
      errorType: ErrorType.principle,
      effect: ErrorEffect.twoSided,
      rectifyingEntry: JournalEntry(
        transactionText: 'Rectify repairs wrongly capitalised',
        lines: [
          JournalLine(account: ChartOfAccounts.commissionPaid, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.machinery, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being repairs wrongly debited to Machinery A/c now corrected)',
      ),
    );
  }

  // Two-sided compensating: Purchases overcast by [amt] exactly offset by
  // Sales overcast by the same [amt] — trial balance still tallied, but
  // both figures need separate correction.
  static RectificationCase _compensatingSuggestingOnlyOneShown(double amt) {
    return RectificationCase(
      errorDescription:
          'Purchases Book was overcast by ₹${_fmt(amt)}, which was compensated by an equal overcast in the Sales Book.',
      errorType: ErrorType.compensating,
      effect: ErrorEffect.twoSided,
      rectifyingEntry: JournalEntry(
        transactionText: 'Rectify compensating overcasts',
        lines: [
          JournalLine(account: ChartOfAccounts.sales, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.goods, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being compensating errors in Purchases and Sales Books now corrected)',
      ),
    );
  }

  // One-sided: Discount allowed posted to the wrong side of Discount
  // Allowed A/c (credited instead of debited) — needs double the amount
  // to reverse, routed through Suspense.
  static RectificationCase _wrongSideePosting(double amt) {
    return RectificationCase(
      errorDescription: 'Discount allowed ₹${_fmt(amt)} was posted to the credit side of Discount Allowed A/c.',
      errorType: ErrorType.commission,
      effect: ErrorEffect.oneSided,
      rectifyingEntry: JournalEntry(
        transactionText: 'Rectify discount allowed posted to wrong side',
        lines: [
          JournalLine(account: ChartOfAccounts.discountAllowed, side: EntrySide.debit, amount: amt * 2),
          JournalLine(account: _suspense, side: EntrySide.credit, amount: amt * 2),
        ],
        narration: '(Being wrong-side posting of Discount Allowed now corrected through Suspense A/c)',
      ),
    );
  }

  static double _round(double v) => (v / 10).round() * 10.0;

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}

class GeneratedRectificationProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final List<RectificationCase> cases;

  const GeneratedRectificationProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.cases,
  });
}
