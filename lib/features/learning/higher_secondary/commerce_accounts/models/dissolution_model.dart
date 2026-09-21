/// One asset realized (sold) on dissolution — book value vs. what it
/// actually fetched in cash.
class AssetRealisation {
  final String assetName;
  final double bookValue;
  final double realisedAmount;

  const AssetRealisation({required this.assetName, required this.bookValue, required this.realisedAmount});
}

/// One liability paid off on dissolution — book value vs. what was
/// actually paid to settle it (may differ if settled at a discount or
/// premium).
class LiabilityPayment {
  final String liabilityName;
  final double bookValue;
  final double amountPaid;

  const LiabilityPayment({required this.liabilityName, required this.bookValue, required this.amountPaid});
}

/// One line of the Realisation Account, in the standard two-sided format.
class RealisationLine {
  final String particulars;
  final double amount;

  const RealisationLine({required this.particulars, required this.amount});
}

class PartnerSettlement {
  final String partnerName;
  final double capitalBalance;
  final double shareOfRealisationProfit; // negative if loss
  final double finalAmountReceived; // negative if the partner owes the firm

  const PartnerSettlement({
    required this.partnerName,
    required this.capitalBalance,
    required this.shareOfRealisationProfit,
    required this.finalAmountReceived,
  });
}

class DissolutionResult {
  final List<RealisationLine> realisationDebit;
  final List<RealisationLine> realisationCredit;
  final double realisationProfitOrLoss; // positive = profit
  final List<PartnerSettlement> partnerSettlements;

  const DissolutionResult({
    required this.realisationDebit,
    required this.realisationCredit,
    required this.realisationProfitOrLoss,
    required this.partnerSettlements,
  });
}
