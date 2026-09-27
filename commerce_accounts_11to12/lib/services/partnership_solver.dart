import '../models/partnership_model.dart';

/// Deterministic solver for Partnership Accounts: Admission and
/// Retirement/Death of a Partner, using the capital-account-adjustment
/// method for goodwill (not raising a separate Goodwill A/c) — the more
/// commonly examined approach in GSEB/CBSE Class 12.
///
/// Core rule applied throughout: when a partner's share of the firm
/// changes, whoever GAINS share must compensate whoever SACRIFICES
/// share, in proportion to the gain/sacrifice, valued at the firm's
/// total goodwill. This single rule is what both Admission and
/// Retirement/Death boil down to — only the direction of the flow
/// differs (new partner pays in vs. remaining partners pay the outgoing
/// one).
class PartnershipSolver {
  PartnershipSolver._();

  /// Admission of a new partner for [newPartnerShare] of the firm,
  /// where all existing partners sacrifice proportionally to their
  /// existing ratio (the standard "old ratio" sacrifice assumption used
  /// when the problem doesn't specify a different sacrificing ratio).
  static AdmissionResult solveAdmission({
    required List<Partner> existingPartners,
    required String newPartnerName,
    required double newPartnerShare,
    required double newPartnerCapital,
    required GoodwillInfo goodwill,
  }) {
    // Each existing partner's new share = old share * (1 - newPartnerShare),
    // i.e. they each give up newPartnerShare of their own share
    // proportionally -- the standard "old ratio" sacrifice.
    final newRatios = <String, double>{};
    final sacrificingRatios = <String, double>{};
    for (final p in existingPartners) {
      final newShare = p.profitShareRatio * (1 - newPartnerShare);
      newRatios[p.name] = newShare;
      sacrificingRatios[p.name] = p.profitShareRatio - newShare;
    }
    newRatios[newPartnerName] = newPartnerShare;

    // New partner's goodwill contribution = their share of total firm
    // goodwill, credited to existing partners in their sacrificing ratio.
    final goodwillBroughtIn = goodwill.totalFirmGoodwill * newPartnerShare;

    final capitalRows = <CapitalAccountRow>[];
    for (final p in existingPartners) {
      final sacrifice = sacrificingRatios[p.name]!;
      // Each existing partner's share of the goodwill credited to them is
      // proportional to their sacrifice relative to total sacrifice.
      final creditShare = goodwillBroughtIn * (sacrifice / newPartnerShare);
      capitalRows.add(CapitalAccountRow(
        partnerName: p.name,
        openingBalance: p.capital,
        goodwillDebit: 0,
        goodwillCredit: creditShare,
        closingBalance: p.capital + creditShare,
      ));
    }
    capitalRows.add(CapitalAccountRow(
      partnerName: newPartnerName,
      openingBalance: newPartnerCapital,
      goodwillDebit: goodwillBroughtIn,
      goodwillCredit: 0,
      // The new partner brings in capital AND goodwill separately in cash;
      // their capital account itself is only credited with their stated
      // capital contribution, not the goodwill (which goes straight to
      // the existing partners' capital accounts as cash, not through the
      // new partner's capital account) -- so closing = opening capital.
      closingBalance: newPartnerCapital,
    ));

    return AdmissionResult(
      newPartner: Partner(name: newPartnerName, capital: newPartnerCapital, profitShareRatio: newPartnerShare),
      newPartnerShare: newPartnerShare,
      newProfitSharingRatios: newRatios,
      sacrificingRatios: sacrificingRatios,
      capitalAccounts: capitalRows,
    );
  }

  /// Retirement or death of [departingPartnerName]: their share is
  /// absorbed by the remaining partners in their existing ratio (the
  /// standard assumption when the problem doesn't specify a different
  /// gaining ratio), and they must compensate the departing partner for
  /// goodwill in proportion to what they gain.
  static DepartureResult solveDeparture({
    required List<Partner> allPartners,
    required String departingPartnerName,
    required DepartureReason reason,
    required GoodwillInfo goodwill,
  }) {
    final departing = allPartners.firstWhere((p) => p.name == departingPartnerName);
    final remaining = allPartners.where((p) => p.name != departingPartnerName).toList();
    final remainingOldRatioTotal = remaining.fold(0.0, (s, p) => s + p.profitShareRatio);

    // Remaining partners absorb the departing partner's share
    // proportionally to their own existing ratios among themselves.
    final newRatios = <String, double>{};
    final gainingRatios = <String, double>{};
    for (final p in remaining) {
      final gain = departing.profitShareRatio * (p.profitShareRatio / remainingOldRatioTotal);
      newRatios[p.name] = p.profitShareRatio + gain;
      gainingRatios[p.name] = gain;
    }

    // Departing partner is compensated for their share of goodwill,
    // funded by remaining partners in their gaining ratio.
    final departingPartnerGoodwillShare = goodwill.totalFirmGoodwill * departing.profitShareRatio;

    final capitalRows = <CapitalAccountRow>[];
    for (final p in remaining) {
      final gain = gainingRatios[p.name]!;
      final debitShare = departingPartnerGoodwillShare * (gain / departing.profitShareRatio);
      capitalRows.add(CapitalAccountRow(
        partnerName: p.name,
        openingBalance: p.capital,
        goodwillDebit: debitShare,
        goodwillCredit: 0,
        closingBalance: p.capital - debitShare,
      ));
    }
    final amountPayable = departing.capital + departingPartnerGoodwillShare;
    capitalRows.add(CapitalAccountRow(
      partnerName: departing.name,
      openingBalance: departing.capital,
      goodwillDebit: 0,
      goodwillCredit: departingPartnerGoodwillShare,
      closingBalance: amountPayable,
    ));

    return DepartureResult(
      departingPartnerName: departingPartnerName,
      reason: reason,
      newProfitSharingRatios: newRatios,
      gainingRatios: gainingRatios,
      capitalAccounts: capitalRows,
      amountPayableToDepartingPartner: amountPayable,
    );
  }
}
