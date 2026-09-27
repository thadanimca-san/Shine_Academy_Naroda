/// The five fundamental account categories used to apply the modern
/// classification rules (Assets/Liabilities/Capital/Income/Expenses),
/// which both GSEB and CBSE Class 11 textbooks teach alongside the
/// traditional Personal/Real/Nominal golden rules.
enum AccountCategory { asset, liability, capital, income, expense }

/// The traditional "golden rules" classification GSEB textbooks lead
/// with (Personal/Real/Nominal), as opposed to the Modern
/// Asset/Liability/Capital/Income/Expense classification CBSE/NCERT
/// leads with. Both classify every account correctly and produce
/// identical Dr/Cr conclusions — only the vocabulary used to explain
/// *why* differs.
enum TraditionalAccountType { personal, real, nominal }

/// Which side (Debit/Credit) an entry falls on.
enum EntrySide { debit, credit }

/// A single ledger account, e.g. "Cash", "Furniture", "Ram (Debtor)".
class Account {
  final String name;
  final AccountCategory category;

  /// True for accounts that represent a person, firm, or other entity
  /// (e.g. a named debtor/creditor, or Capital/Drawings which represent
  /// the proprietor) — these are always Personal accounts under the
  /// traditional classification regardless of [category].
  final bool isPersonEntity;

  const Account({required this.name, required this.category, this.isPersonEntity = false});

  /// Whether an *increase* in this account is recorded as a debit.
  /// Assets & Expenses increase on debit; Liabilities, Capital & Income
  /// increase on credit. This single rule drives all journal generation
  /// and is the same rule a teacher states as "Dr what comes in / increases
  /// for Assets & Expenses; Cr what goes out / increases for the rest."
  bool get increasesOnDebit =>
      category == AccountCategory.asset || category == AccountCategory.expense;

  /// The traditional Personal/Real/Nominal classification for this
  /// account, used when explaining an entry via the golden rules
  /// (GSEB's typical starting approach) instead of the modern method.
  TraditionalAccountType get traditionalType {
    if (isPersonEntity || category == AccountCategory.capital || category == AccountCategory.liability) {
      return TraditionalAccountType.personal;
    }
    if (category == AccountCategory.asset) return TraditionalAccountType.real;
    return TraditionalAccountType.nominal; // income & expense
  }

  @override
  String toString() => name;

  @override
  bool operator ==(Object other) =>
      other is Account && other.name == name && other.category == category;

  @override
  int get hashCode => Object.hash(name, category);
}

/// One Dr/Cr line of a journal entry.
class JournalLine {
  final Account account;
  final EntrySide side;
  final double amount;

  const JournalLine({required this.account, required this.side, required this.amount});
}

/// A full journal entry: one transaction, one or more debit lines and
/// one or more credit lines (compound entries supported), plus the
/// narration a student/teacher would write underneath it.
class JournalEntry {
  final String transactionText;
  final List<JournalLine> lines;
  final String narration;

  const JournalEntry({
    required this.transactionText,
    required this.lines,
    required this.narration,
  });

  double get totalDebit => lines
      .where((l) => l.side == EntrySide.debit)
      .fold(0.0, (sum, l) => sum + l.amount);

  double get totalCredit => lines
      .where((l) => l.side == EntrySide.credit)
      .fold(0.0, (sum, l) => sum + l.amount);

  bool get isBalanced => (totalDebit - totalCredit).abs() < 0.005;
}
