import 'account_model.dart';

/// One explained step of a worked solution — the unit shown to students
/// as a hint/reveal, and to teachers as an answer-key line. Kept generic
/// (not journal-specific) so the same shape can later carry ledger,
/// trial-balance, or final-account steps.
class SolutionStep {
  final String title;
  final String reasoning;
  final double? marks;

  const SolutionStep({required this.title, required this.reasoning, this.marks});
}

/// Full worked solution for one journal entry: the golden-rule reasoning
/// for every line, in the order a teacher would explain it on a
/// blackboard (identify accounts -> classify -> apply rule -> conclude).
class JournalEntrySolution {
  final JournalEntry entry;
  final List<SolutionStep> steps;

  const JournalEntrySolution({required this.entry, required this.steps});
}

/// One side (Dr or Cr) of a T-account, i.e. one posted line in a ledger.
class LedgerPosting {
  final String particulars; // e.g. "To Cash" or "By Sales"
  final double amount;
  final String sourceTransaction;

  const LedgerPosting({
    required this.particulars,
    required this.amount,
    required this.sourceTransaction,
  });
}

/// A single T-account fully posted from a set of journal entries.
class LedgerAccount {
  final Account account;
  final List<LedgerPosting> debitPostings;
  final List<LedgerPosting> creditPostings;

  const LedgerAccount({
    required this.account,
    required this.debitPostings,
    required this.creditPostings,
  });

  double get totalDebit => debitPostings.fold(0.0, (s, p) => s + p.amount);
  double get totalCredit => creditPostings.fold(0.0, (s, p) => s + p.amount);

  /// Closing balance and which side it sits on, i.e. the figure carried
  /// down ("c/d") and brought down ("b/d") — what feeds the trial balance.
  EntrySide get balanceSide =>
      totalDebit >= totalCredit ? EntrySide.debit : EntrySide.credit;

  double get balanceAmount => (totalDebit - totalCredit).abs();
}

/// One row of a trial balance: an account and the side its balance sits on.
class TrialBalanceRow {
  final Account account;
  final double debitAmount;
  final double creditAmount;

  const TrialBalanceRow({
    required this.account,
    required this.debitAmount,
    required this.creditAmount,
  });
}

class TrialBalance {
  final List<TrialBalanceRow> rows;

  const TrialBalance({required this.rows});

  double get totalDebit => rows.fold(0.0, (s, r) => s + r.debitAmount);
  double get totalCredit => rows.fold(0.0, (s, r) => s + r.creditAmount);
  bool get isBalanced => (totalDebit - totalCredit).abs() < 0.005;
}
