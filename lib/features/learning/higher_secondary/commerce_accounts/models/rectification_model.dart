import 'account_model.dart';

/// The four traditional error categories taught in GSEB/CBSE Class 11:
/// omission (transaction never recorded), commission (wrong amount/
/// account of the right type), principle (posted to the wrong type of
/// account, e.g. capital expenditure treated as revenue), and
/// compensating (two errors that cancel each other's effect on the
/// trial balance).
enum ErrorType { omission, commission, principle, compensating }

/// Whether an error affects the trial balance (one-sided — a Suspense
/// A/c entry is needed to fix it) or doesn't (two-sided — a normal
/// rectifying journal entry balances on its own).
enum ErrorEffect { oneSided, twoSided }

/// One error scenario: what went wrong, and the single correcting
/// journal entry that fixes it — including a Suspense A/c line when the
/// error is one-sided.
class RectificationCase {
  final String errorDescription;
  final ErrorType errorType;
  final ErrorEffect effect;
  final JournalEntry rectifyingEntry;

  const RectificationCase({
    required this.errorDescription,
    required this.errorType,
    required this.effect,
    required this.rectifyingEntry,
  });
}
