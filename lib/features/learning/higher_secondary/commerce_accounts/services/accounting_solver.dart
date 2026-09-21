import '../models/account_model.dart';
import '../models/problem_model.dart';
import '../models/solution_model.dart';

/// Deterministic, rules-based solver for the Journal -> Ledger -> Trial
/// Balance chain. Every method here is pure (no randomness, no I/O) so the
/// exact same output is produced whether it is used to give a student a
/// hint, mark a student's attempt, or print a teacher's answer key —
/// there is only one source of truth for "the correct answer."
class AccountingSolver {
  AccountingSolver._();

  /// Explains a single journal entry the way a teacher would. GSEB
  /// textbooks typically lead with the traditional Personal/Real/Nominal
  /// golden rules; CBSE/NCERT typically leads with the Modern method
  /// (Asset/Liability/Capital/Income/Expense). Both are correct and
  /// produce identical Dr/Cr conclusions — only the explanation
  /// vocabulary changes based on [board], matching what each board's
  /// students are actually taught first.
  static JournalEntrySolution explainEntry(JournalEntry entry, {Board board = Board.cbse}) {
    final steps = <SolutionStep>[];

    for (final line in entry.lines) {
      steps.add(board == Board.gseb ? _explainLineTraditional(line) : _explainLineModern(line));
    }

    steps.add(SolutionStep(
      title: 'Check: Debit = Credit',
      reasoning: 'Total Debit ₹${_fmt(entry.totalDebit)} = Total Credit '
          '₹${_fmt(entry.totalCredit)}. ${entry.isBalanced ? "Entry balances." : "ERROR: entry does not balance."}',
    ));

    return JournalEntrySolution(entry: entry, steps: steps);
  }

  static SolutionStep _explainLineModern(JournalLine line) {
    final acc = line.account;
    final categoryLabel = _categoryLabel(acc.category);
    final ruleLabel = acc.increasesOnDebit
        ? 'increases in ${acc.name} are recorded on the Debit side'
        : 'increases in ${acc.name} are recorded on the Credit side';
    final concludedSide = line.side == EntrySide.debit ? 'Debit' : 'Credit';

    return SolutionStep(
      title: '${acc.name} — $concludedSide',
      reasoning: '${acc.name} is a $categoryLabel account. Rule: $ruleLabel. '
          'This transaction ${_directionPhrase(acc, line.side)}, so ${acc.name} is '
          '$concludedSide-ed with ₹${_fmt(line.amount)}.',
    );
  }

  static SolutionStep _explainLineTraditional(JournalLine line) {
    final acc = line.account;
    final concludedSide = line.side == EntrySide.debit ? 'Debit' : 'Credit';
    final (typeLabel, goldenRule) = switch (acc.traditionalType) {
      TraditionalAccountType.personal => ('Personal', 'Debit the receiver, Credit the giver'),
      TraditionalAccountType.real => ('Real', 'Debit what comes in, Credit what goes out'),
      TraditionalAccountType.nominal => ('Nominal', 'Debit all expenses and losses, Credit all incomes and gains'),
    };
    final isIncrease = (line.side == EntrySide.debit && acc.increasesOnDebit) ||
        (line.side == EntrySide.credit && !acc.increasesOnDebit);
    final directionNote = switch (acc.traditionalType) {
      TraditionalAccountType.personal => isIncrease ? '${acc.name} is the receiver here' : '${acc.name} is the giver here',
      TraditionalAccountType.real => isIncrease ? 'value is coming in' : 'value is going out',
      TraditionalAccountType.nominal =>
        acc.category == AccountCategory.expense ? 'this is an expense/loss' : 'this is an income/gain',
    };

    return SolutionStep(
      title: '${acc.name} — $concludedSide',
      reasoning: '${acc.name} is a $typeLabel account. Golden Rule: $goldenRule. '
          'Here, $directionNote, so ${acc.name} is $concludedSide-ed with ₹${_fmt(line.amount)}.',
    );
  }

  static String _directionPhrase(Account acc, EntrySide side) {
    final isIncrease =
        (side == EntrySide.debit && acc.increasesOnDebit) || (side == EntrySide.credit && !acc.increasesOnDebit);
    return isIncrease ? 'increases this account' : 'decreases this account';
  }

  static String _categoryLabel(AccountCategory c) {
    switch (c) {
      case AccountCategory.asset:
        return 'Asset';
      case AccountCategory.liability:
        return 'Liability';
      case AccountCategory.capital:
        return 'Capital';
      case AccountCategory.income:
        return 'Income/Revenue';
      case AccountCategory.expense:
        return 'Expense';
    }
  }

  /// Posts a list of journal entries into individual T-accounts, in the
  /// order the entries were passed. Every posting keeps a reference back
  /// to the transaction narration it came from, which is what lets the
  /// UI/answer-key show "posted from: [transaction]" against each line.
  static List<LedgerAccount> postToLedger(List<JournalEntry> entries) {
    final debitPostings = <Account, List<LedgerPosting>>{};
    final creditPostings = <Account, List<LedgerPosting>>{};
    final accountsInOrder = <Account>[];

    void ensureTracked(Account acc) {
      if (!accountsInOrder.contains(acc)) {
        accountsInOrder.add(acc);
        debitPostings[acc] = [];
        creditPostings[acc] = [];
      }
    }

    for (final entry in entries) {
      final debitLines = entry.lines.where((l) => l.side == EntrySide.debit).toList();
      final creditLines = entry.lines.where((l) => l.side == EntrySide.credit).toList();

      for (final dLine in debitLines) {
        ensureTracked(dLine.account);
        final counterpart = creditLines.length == 1 ? creditLines.first.account.name : 'Sundries';
        debitPostings[dLine.account]!.add(LedgerPosting(
          particulars: 'To $counterpart',
          amount: dLine.amount,
          sourceTransaction: entry.transactionText,
        ));
      }

      for (final cLine in creditLines) {
        ensureTracked(cLine.account);
        final counterpart = debitLines.length == 1 ? debitLines.first.account.name : 'Sundries';
        creditPostings[cLine.account]!.add(LedgerPosting(
          particulars: 'By $counterpart',
          amount: cLine.amount,
          sourceTransaction: entry.transactionText,
        ));
      }
    }

    return accountsInOrder
        .map((acc) => LedgerAccount(
              account: acc,
              debitPostings: debitPostings[acc]!,
              creditPostings: creditPostings[acc]!,
            ))
        .toList();
  }

  /// Builds the trial balance from posted ledger accounts — each
  /// account's closing balance placed on whichever side (Dr/Cr) it sits.
  static TrialBalance buildTrialBalance(List<LedgerAccount> ledgers) {
    final rows = ledgers
        .where((l) => l.balanceAmount > 0.005)
        .map((l) => TrialBalanceRow(
              account: l.account,
              debitAmount: l.balanceSide == EntrySide.debit ? l.balanceAmount : 0,
              creditAmount: l.balanceSide == EntrySide.credit ? l.balanceAmount : 0,
            ))
        .toList();
    return TrialBalance(rows: rows);
  }

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
