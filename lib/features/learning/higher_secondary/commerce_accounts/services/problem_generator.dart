import 'dart:math';

import '../data/chart_of_accounts.dart';
import '../models/account_model.dart';
import '../models/problem_model.dart';

enum _PersonRole { debtor, creditor }

/// Generates randomized-but-valid transaction sets for the Journal ->
/// Ledger -> Trial Balance topic chain. Every transaction template keeps
/// amounts within sensible ranges and always produces a balanced entry,
/// so whatever comes out is guaranteed solvable by [AccountingSolver].
class ProblemGenerator {
  ProblemGenerator._();

  static final Random _rand = Random();

  /// A single transaction "shape" — knows how to render its own question
  /// text and its own JournalEntry for a given random amount/person.
  static final List<_TransactionTemplate> _basicTemplates = [
    _TransactionTemplate(
      describe: (amt, person) => 'Started business with cash ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Started business with cash ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.capital, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being cash brought in as capital)',
      ),
      minAmt: 20000,
      maxAmt: 200000,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Purchased goods for cash ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Purchased goods for cash ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.goods, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being goods purchased for cash)',
      ),
      minAmt: 2000,
      maxAmt: 40000,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Sold goods to $person for cash ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Sold goods for cash ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.sales, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being goods sold for cash)',
      ),
      minAmt: 2000,
      maxAmt: 40000,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Purchased goods from $person on credit ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Purchased goods from $person on credit ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.goods, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.creditor(person), side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being goods purchased on credit from $person)',
      ),
      minAmt: 3000,
      maxAmt: 60000,
      assignsRole: _PersonRole.creditor,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Sold goods to $person on credit ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Sold goods to $person on credit ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.debtor(person), side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.sales, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being goods sold on credit to $person)',
      ),
      minAmt: 3000,
      maxAmt: 60000,
      assignsRole: _PersonRole.debtor,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Paid rent ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Paid rent ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.rentExpense, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being rent paid)',
      ),
      minAmt: 1000,
      maxAmt: 15000,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Paid salary ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Paid salary ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.salaryExpense, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being salary paid)',
      ),
      minAmt: 5000,
      maxAmt: 30000,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Received commission ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Received commission ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.commissionReceived, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being commission received)',
      ),
      minAmt: 1000,
      maxAmt: 10000,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Purchased furniture for cash ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Purchased furniture for cash ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.furniture, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being furniture purchased for cash)',
      ),
      minAmt: 5000,
      maxAmt: 80000,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Withdrew cash for personal use ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Withdrew cash for personal use ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.drawings, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being cash withdrawn for personal use)',
      ),
      minAmt: 1000,
      maxAmt: 20000,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Received cash from $person ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Received cash from debtor $person ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.debtor(person), side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being cash received from $person)',
      ),
      minAmt: 2000,
      maxAmt: 30000,
      requiresExistingRole: _PersonRole.debtor,
    ),
    _TransactionTemplate(
      describe: (amt, person) => 'Paid cash to $person ₹${_fmt(amt)}',
      build: (amt, person) => JournalEntry(
        transactionText: 'Paid cash to creditor $person ₹${_fmt(amt)}',
        lines: [
          JournalLine(account: ChartOfAccounts.creditor(person), side: EntrySide.debit, amount: amt),
          JournalLine(account: ChartOfAccounts.cash, side: EntrySide.credit, amount: amt),
        ],
        narration: '(Being cash paid to $person)',
      ),
      minAmt: 2000,
      maxAmt: 30000,
      requiresExistingRole: _PersonRole.creditor,
    ),
  ];

  /// Generates one problem containing [transactionCount] journal entries,
  /// suitable for a Journal / Ledger / Trial Balance practice question or
  /// exam question. [difficulty] scales transaction count and complexity:
  /// 1-2 -> straightforward cash transactions; 3+ -> mixes in credit
  /// transactions with named parties (debtors/creditors), which is what
  /// makes ledger posting and trial balance meaningfully harder.
  ///
  /// Class 12 students still practice this topic as revision alongside
  /// harder Class 12 material, not as first exposure — so at the same
  /// difficulty, [schoolClass] 12 adds one extra transaction and reaches
  /// the credit-transaction pool one difficulty level earlier than Class
  /// 11, without changing what a given difficulty number means within a
  /// single class.
  static GeneratedProblem generateJournalLedgerTrialBalance({
    required Board board,
    required int schoolClass,
    required int difficulty,
    int? transactionCount,
    String? idSeed,
  }) {
    final classBonus = schoolClass == 12 ? 1 : 0;
    final count = transactionCount ?? (4 + difficulty + classBonus).clamp(4, 13);
    final creditPoolThreshold = schoolClass == 12 ? 1 : 2;
    final pool = difficulty <= creditPoolThreshold
        ? _basicTemplates.where((t) => !t.describe(0, 'X').contains('credit')).toList()
        : _basicTemplates;

    final entries = <JournalEntry>[];
    // Always start with capital introduction so Cash has an opening balance
    // and every subsequent transaction is realistic (can't pay before having cash).
    final startTemplate = _basicTemplates.first;
    final startAmt = _roundAmount(startTemplate.minAmt, startTemplate.maxAmt);
    entries.add(startTemplate.build(startAmt, ''));

    // Track each person's role for the life of this problem: a person who
    // becomes a debtor (credit sale to them) or creditor (credit purchase
    // from them) must stay that same role throughout — otherwise "Ram" as
    // both a debtor and a creditor would wrongly post to two ledger
    // accounts instead of one, and settlement templates ("received from
    // debtor X" / "paid to creditor X") could reference a relationship
    // that was never actually created.
    final personRole = <String, _PersonRole>{};
    final availablePeople = List<String>.from(ChartOfAccounts.personNames)..shuffle(_rand);

    String pickPersonFor(_TransactionTemplate template) {
      final needsExistingDebtor = template.requiresExistingRole == _PersonRole.debtor;
      final needsExistingCreditor = template.requiresExistingRole == _PersonRole.creditor;

      if (needsExistingDebtor || needsExistingCreditor) {
        final wanted = needsExistingDebtor ? _PersonRole.debtor : _PersonRole.creditor;
        final candidates = personRole.entries.where((e) => e.value == wanted).map((e) => e.key).toList();
        if (candidates.isEmpty) return ''; // caller falls back to a safe template
        return candidates[_rand.nextInt(candidates.length)];
      }

      if (template.assignsRole != null) {
        // Prefer a person with no role yet, or one who already has this
        // same role (so repeat credit deals with the same party are fine).
        final reusable = personRole.entries.where((e) => e.value == template.assignsRole).map((e) => e.key).toList();
        final fresh = availablePeople.where((p) => !personRole.containsKey(p)).toList();
        final pool = [...reusable, ...fresh];
        final person = pool.isNotEmpty
            ? pool[_rand.nextInt(pool.length)]
            : ChartOfAccounts.personNames[_rand.nextInt(ChartOfAccounts.personNames.length)];
        personRole[person] = template.assignsRole!;
        return person;
      }

      return ChartOfAccounts.personNames[_rand.nextInt(ChartOfAccounts.personNames.length)];
    }

    for (var i = 0; i < count - 1; i++) {
      var template = pool[_rand.nextInt(pool.length)];
      var person = pickPersonFor(template);
      if (person.isEmpty) {
        // No eligible debtor/creditor exists yet for a settlement template
        // — fall back to a template that doesn't need a pre-existing role.
        final safePool = pool.where((t) => t.requiresExistingRole == null).toList();
        template = safePool[_rand.nextInt(safePool.length)];
        person = pickPersonFor(template);
      }
      final amt = _roundAmount(template.minAmt, template.maxAmt);
      entries.add(template.build(amt, person));
    }

    final id = idSeed ?? 'JLT-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}';
    final marks = (entries.length * 1.0);

    return GeneratedProblem(
      id: id,
      topic: TopicRef(
        board: board,
        schoolClass: schoolClass,
        chapter: 'Journal, Ledger & Trial Balance',
        subtopic: difficulty <= 2 ? 'Basic Cash Transactions' : 'Cash & Credit Transactions',
      ),
      difficulty: difficulty,
      patternType: PaperPatternType.long,
      marks: marks,
      questionText:
          'Journalise the following transactions in the books of a trader, post them to the ledger, and prepare a Trial Balance as on the closing date:',
      transactions: entries,
    );
  }

  static double _roundAmount(double min, double max) {
    final raw = min + _rand.nextDouble() * (max - min);
    return (raw / 100).round() * 100.0;
  }

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}

class _TransactionTemplate {
  final String Function(double amt, String person) describe;
  final JournalEntry Function(double amt, String person) build;
  final double minAmt;
  final double maxAmt;

  /// Set when this template establishes a new debtor/creditor relationship
  /// (a credit sale/purchase) — the chosen person is tagged with this role.
  final _PersonRole? assignsRole;

  /// Set when this template settles an existing relationship (receiving
  /// from a debtor / paying a creditor) — only a person already holding
  /// this exact role may be picked.
  final _PersonRole? requiresExistingRole;

  const _TransactionTemplate({
    required this.describe,
    required this.build,
    required this.minAmt,
    required this.maxAmt,
    this.assignsRole,
    this.requiresExistingRole,
  });
}
