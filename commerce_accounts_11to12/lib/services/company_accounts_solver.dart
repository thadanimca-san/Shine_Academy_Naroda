import '../models/company_accounts_model.dart';

/// Deterministic solver for Share Capital transactions: issue at par or
/// premium (fully subscribed, no oversubscription — that variant is a
/// natural follow-up), followed by forfeiture of shares on which a
/// shareholder defaulted on a call, and reissue of the forfeited shares.
///
/// Core rules encoded here, each of which is exactly what the topic
/// tests:
/// - Application & Allotment money is credited straight to Share Capital
///   (and Securities Premium, if issued at a premium) as it's called.
/// - On forfeiture: Share Capital is debited with the amount *called up*
///   on the forfeited shares (not the face value paid so far only —
///   the called-up amount), the shareholder's unpaid calls are
///   cancelled, and whatever they DID pay is credited to a Forfeited
///   Shares A/c.
/// - On reissue: any deficiency in the reissue price (reissued below
///   face value) is met first from the Forfeited Shares A/c; any
///   surplus remaining in Forfeited Shares A/c after that is transferred
///   to Capital Reserve.
class CompanyAccountsSolver {
  CompanyAccountsSolver._();

  static ShareIssueResult solveFullySubscribedIssue({
    required int sharesIssued,
    required CallStructure calls,
    required int sharesForfeitedForFinalCallDefault,
    required double reissuePricePerShare,
  }) {
    final steps = <ShareIssueStep>[];

    void addCallStep(String title, String narration, double amountPerShare, int shareCount, {double premiumPortion = 0}) {
      final total = amountPerShare * shareCount;
      if (premiumPortion > 0) {
        final capitalPortion = (amountPerShare - premiumPortion) * shareCount;
        final premiumTotal = premiumPortion * shareCount;
        steps.add(ShareIssueStep(
          title: title,
          narration: narration,
          debitCash: total,
          creditAccountName: 'Share Capital A/c',
          creditAmount: capitalPortion,
          secondCreditAccountName: 'Securities Premium A/c',
          secondCreditAmount: premiumTotal,
        ));
      } else {
        steps.add(ShareIssueStep(
          title: title,
          narration: narration,
          debitCash: total,
          creditAccountName: 'Share Capital A/c',
          creditAmount: total,
        ));
      }
    }

    addCallStep('Application Money Received', '(Being application money received on $sharesIssued shares)',
        calls.applicationAmount, sharesIssued);
    addCallStep('Allotment Money Due & Received',
        '(Being allotment money received on $sharesIssued shares, including premium)', calls.allotmentAmount,
        sharesIssued, premiumPortion: calls.premiumPerShare);
    if (calls.firstCallAmount > 0) {
      addCallStep('First Call Money Received', '(Being first call money received on $sharesIssued shares)',
          calls.firstCallAmount, sharesIssued);
    }

    // Final call: sharesForfeitedForFinalCallDefault shareholders did not
    // pay, so only (sharesIssued - forfeited) pay the final call.
    final payingShares = sharesIssued - sharesForfeitedForFinalCallDefault;
    if (calls.finalCallAmount > 0 && payingShares > 0) {
      addCallStep('Final Call Money Received', '(Being final call money received on $payingShares shares)',
          calls.finalCallAmount, payingShares);
    }

    double forfeitedSharesBalance = 0;
    double capitalReserve = 0;

    if (sharesForfeitedForFinalCallDefault > 0) {
      // Amount called up per share on the forfeited shares = everything
      // except the final call (that's what they defaulted on); since
      // they paid every earlier call in full, amount paid == amount
      // called up for these shares.
      final calledUpPerShare = calls.totalPerShare - calls.finalCallAmount;
      final capitalDebited = calledUpPerShare * sharesForfeitedForFinalCallDefault;
      forfeitedSharesBalance = calledUpPerShare * sharesForfeitedForFinalCallDefault;

      steps.add(ShareIssueStep(
        title: 'Forfeiture of Shares',
        narration: '(Being $sharesForfeitedForFinalCallDefault shares forfeited for non-payment of final call)',
        debitCash: 0,
        creditAccountName: 'Share Forfeited A/c',
        creditAmount: forfeitedSharesBalance,
        secondCreditAccountName: 'Share Capital A/c (Dr)',
        secondCreditAmount: capitalDebited,
      ));

      // Reissue of the forfeited shares.
      final reissueTotal = reissuePricePerShare * sharesForfeitedForFinalCallDefault;
      final faceValueTotal = calls.faceValue * sharesForfeitedForFinalCallDefault;
      final deficiency = faceValueTotal - reissueTotal;
      final forfeitedUsedForDeficiency = deficiency > 0 ? deficiency.clamp(0, forfeitedSharesBalance).toDouble() : 0.0;
      capitalReserve = forfeitedSharesBalance - forfeitedUsedForDeficiency;

      steps.add(ShareIssueStep(
        title: 'Reissue of Forfeited Shares',
        narration: '(Being $sharesForfeitedForFinalCallDefault forfeited shares reissued at '
            '₹${reissuePricePerShare.toStringAsFixed(2)} per share, fully paid, deficiency met from Forfeited Shares A/c)',
        debitCash: reissueTotal,
        secondDebitAccountName: forfeitedUsedForDeficiency > 0 ? 'Share Forfeited A/c' : null,
        secondDebitAmount: forfeitedUsedForDeficiency > 0 ? forfeitedUsedForDeficiency : null,
        creditAccountName: 'Share Capital A/c',
        creditAmount: faceValueTotal,
      ));
    }

    final totalCapitalRaised = sharesIssued * calls.faceValue;
    final securitiesPremium = sharesIssued * calls.premiumPerShare;

    return ShareIssueResult(
      sharesApplied: sharesIssued,
      sharesAllotted: sharesIssued,
      sharesForfeited: sharesForfeitedForFinalCallDefault,
      sharesReissued: sharesForfeitedForFinalCallDefault,
      steps: steps,
      totalCapitalRaised: totalCapitalRaised,
      securitiesPremiumBalance: securitiesPremium,
      forfeitedSharesAccountBalance: forfeitedSharesBalance,
      capitalReserveOnReissue: capitalReserve,
    );
  }
}
