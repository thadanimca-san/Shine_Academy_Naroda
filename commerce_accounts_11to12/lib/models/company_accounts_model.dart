/// The stages of money collection on a share issue, in the order they
/// are called — GSEB/CBSE Class 12 covers the standard 4-call structure
/// (Application, Allotment, First Call, Final/Second Call), though not
/// every problem uses all of them.
enum CallStage { application, allotment, firstCall, finalCall }

/// Per-share amount due at each call stage. All amounts are per share,
/// not totals — totals are derived by multiplying by share counts.
class CallStructure {
  final double faceValue;
  final double premiumPerShare;
  final double applicationAmount;
  final double allotmentAmount; // includes any premium collected at allotment
  final double firstCallAmount;
  final double finalCallAmount;

  const CallStructure({
    required this.faceValue,
    this.premiumPerShare = 0,
    required this.applicationAmount,
    required this.allotmentAmount,
    required this.firstCallAmount,
    required this.finalCallAmount,
  });

  double get totalPerShare => applicationAmount + allotmentAmount + firstCallAmount + finalCallAmount;
}

/// One journal entry in the share issue sequence, in the same shape the
/// rest of the app already uses so it can reuse [AccountingSolver]'s
/// explanation and the existing journal display widgets. Supports up to
/// two debit lines and two credit lines, which covers every entry this
/// topic needs (e.g. reissue below face value debits both Bank and the
/// Forfeited Shares A/c for the deficiency).
class ShareIssueStep {
  final String title;
  final String narration;
  final double debitCash;
  final String? secondDebitAccountName;
  final double? secondDebitAmount;
  final String creditAccountName;
  final double creditAmount;
  final double? secondCreditAmount; // e.g. Share Capital + Securities Premium split
  final String? secondCreditAccountName;

  const ShareIssueStep({
    required this.title,
    required this.narration,
    required this.debitCash,
    this.secondDebitAccountName,
    this.secondDebitAmount,
    required this.creditAccountName,
    required this.creditAmount,
    this.secondCreditAmount,
    this.secondCreditAccountName,
  });
}

class ShareIssueResult {
  final int sharesApplied;
  final int sharesAllotted;
  final int sharesForfeited;
  final int sharesReissued;
  final List<ShareIssueStep> steps;
  final double totalCapitalRaised;
  final double securitiesPremiumBalance;
  final double forfeitedSharesAccountBalance;
  final double capitalReserveOnReissue;

  const ShareIssueResult({
    required this.sharesApplied,
    required this.sharesAllotted,
    required this.sharesForfeited,
    required this.sharesReissued,
    required this.steps,
    required this.totalCapitalRaised,
    required this.securitiesPremiumBalance,
    required this.forfeitedSharesAccountBalance,
    required this.capitalReserveOnReissue,
  });
}
