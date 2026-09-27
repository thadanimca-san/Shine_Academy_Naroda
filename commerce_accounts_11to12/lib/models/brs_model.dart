/// Whether a reconciling item should be added or subtracted when starting
/// from the given balance (Cash Book or Pass Book) to arrive at the
/// other book's balance — the two standard BRS approaches taught in
/// GSEB/CBSE Class 11.
enum BrsAdjustment { add, subtract }

/// One reconciling item, e.g. "Cheques issued but not presented for
/// payment ₹5,000". [effectOnPassBookBalance] captures how this item
/// should be treated *when starting from the Cash Book balance* — the
/// far more commonly examined direction — and the reverse item (starting
/// from Pass Book) is simply the opposite adjustment.
class BrsItem {
  final String description;
  final double amount;
  final BrsAdjustment effectOnPassBookBalance;

  const BrsItem({
    required this.description,
    required this.amount,
    required this.effectOnPassBookBalance,
  });

  /// The opposite-direction adjustment, for a BRS starting from the Pass
  /// Book balance instead of the Cash Book balance.
  BrsAdjustment get effectOnCashBookBalance =>
      effectOnPassBookBalance == BrsAdjustment.add ? BrsAdjustment.subtract : BrsAdjustment.add;
}

class BrsResult {
  final double cashBookBalance;
  final List<BrsItem> items;
  final double passBookBalance;

  const BrsResult({
    required this.cashBookBalance,
    required this.items,
    required this.passBookBalance,
  });
}
