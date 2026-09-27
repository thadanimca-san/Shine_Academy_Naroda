import '../models/dissolution_model.dart';
import '../models/partnership_model.dart';

/// Deterministic solver for Dissolution of Partnership Firm via the
/// Realisation Account method — the standard GSEB/CBSE Class 12 approach.
///
/// Core rules encoded here, exactly what the topic tests:
/// - All assets (at book value) are transferred to the debit of
///   Realisation A/c; all outside liabilities (at book value) are
///   transferred to its credit.
/// - Cash actually realised from selling assets is credited to
///   Realisation A/c; cash actually paid to settle liabilities is
///   debited to it.
/// - Whatever balance remains on Realisation A/c is profit (if credit
///   side is bigger) or loss (if debit side is bigger), shared among
///   partners in their profit-sharing ratio.
/// - Each partner's final settlement = their capital balance +/- their
///   share of realisation profit/loss.
class DissolutionSolver {
  DissolutionSolver._();

  static DissolutionResult solve({
    required List<Partner> partners,
    required List<AssetRealisation> assets,
    required List<LiabilityPayment> liabilities,
    double dissolutionExpenses = 0,
  }) {
    final debit = <RealisationLine>[
      for (final a in assets) RealisationLine(particulars: '${a.assetName} A/c (book value)', amount: a.bookValue),
      for (final l in liabilities) RealisationLine(particulars: 'Cash — Payment of ${l.liabilityName}', amount: l.amountPaid),
      if (dissolutionExpenses > 0) RealisationLine(particulars: 'Cash — Realisation Expenses', amount: dissolutionExpenses),
    ];

    final credit = <RealisationLine>[
      for (final l in liabilities) RealisationLine(particulars: '${l.liabilityName} A/c (book value)', amount: l.bookValue),
      for (final a in assets) RealisationLine(particulars: 'Cash — Sale of ${a.assetName}', amount: a.realisedAmount),
    ];

    final totalDebit = debit.fold(0.0, (s, l) => s + l.amount);
    final totalCredit = credit.fold(0.0, (s, l) => s + l.amount);
    final profitOrLoss = totalCredit - totalDebit;

    final settlements = partners.map((p) {
      final share = profitOrLoss * p.profitShareRatio;
      return PartnerSettlement(
        partnerName: p.name,
        capitalBalance: p.capital,
        shareOfRealisationProfit: share,
        finalAmountReceived: p.capital + share,
      );
    }).toList();

    return DissolutionResult(
      realisationDebit: debit,
      realisationCredit: credit,
      realisationProfitOrLoss: profitOrLoss,
      partnerSettlements: settlements,
    );
  }
}
