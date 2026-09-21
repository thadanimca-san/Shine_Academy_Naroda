/// A partner's capital account balance and profit-sharing share, before
/// any admission/retirement/death adjustment is applied.
class Partner {
  final String name;
  final double capital;
  final double profitShareRatio; // e.g. 0.5 for a 1/2 share

  const Partner({required this.name, required this.capital, required this.profitShareRatio});
}

/// How goodwill brought in by a new/adjusting partner is treated —
/// GSEB/CBSE Class 12 covers both the "goodwill account raised and
/// written off" method and the simpler "adjustment through partners'
/// capital accounts" method. This app implements the capital-account
/// adjustment method, which is the more commonly examined approach.
class GoodwillInfo {
  final double totalFirmGoodwill;

  const GoodwillInfo({required this.totalFirmGoodwill});
}

/// One partner's capital account movement — the standard columnar format
/// (Balance b/d, Goodwill adjustment, Balance c/d) used to present the
/// answer.
class CapitalAccountRow {
  final String partnerName;
  final double openingBalance;
  final double goodwillDebit;
  final double goodwillCredit;
  final double closingBalance;

  const CapitalAccountRow({
    required this.partnerName,
    required this.openingBalance,
    required this.goodwillDebit,
    required this.goodwillCredit,
    required this.closingBalance,
  });
}

class AdmissionResult {
  final Partner newPartner;
  final double newPartnerShare;
  final Map<String, double> newProfitSharingRatios; // partner name -> share, includes new partner
  final Map<String, double> sacrificingRatios; // old partner name -> sacrifice
  final List<CapitalAccountRow> capitalAccounts;

  const AdmissionResult({
    required this.newPartner,
    required this.newPartnerShare,
    required this.newProfitSharingRatios,
    required this.sacrificingRatios,
    required this.capitalAccounts,
  });
}

enum DepartureReason { retirement, death }

class DepartureResult {
  final String departingPartnerName;
  final DepartureReason reason;
  final Map<String, double> newProfitSharingRatios; // remaining partners
  final Map<String, double> gainingRatios; // remaining partner name -> gain
  final List<CapitalAccountRow> capitalAccounts;
  final double amountPayableToDepartingPartner;

  const DepartureResult({
    required this.departingPartnerName,
    required this.reason,
    required this.newProfitSharingRatios,
    required this.gainingRatios,
    required this.capitalAccounts,
    required this.amountPayableToDepartingPartner,
  });
}
