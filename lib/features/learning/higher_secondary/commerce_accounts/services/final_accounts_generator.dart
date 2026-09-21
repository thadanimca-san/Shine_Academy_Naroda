import 'dart:math';

import '../models/final_accounts_model.dart';
import '../models/problem_model.dart';
import 'final_accounts_solver.dart';

/// Generates a randomized, always-internally-consistent Final Accounts
/// problem: a trial balance (built so Dr total == Cr total by
/// construction, using Capital as the balancing figure — exactly how
/// real trial balances are presented) plus a small set of adjustments.
class FinalAccountsGenerator {
  FinalAccountsGenerator._();

  static final Random _rand = Random();

  static GeneratedFinalAccountsProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    final openingStock = _round(5000 + _rand.nextDouble() * 15000);
    final purchases = _round(40000 + _rand.nextDouble() * 60000);
    final purchasesReturn = _round(purchases * 0.03);
    final sales = _round(purchases * (1.4 + _rand.nextDouble() * 0.4)); // sold at a markup
    final salesReturn = _round(sales * 0.03);
    final wages = _round(3000 + _rand.nextDouble() * 7000);
    final carriageInwards = _round(500 + _rand.nextDouble() * 2000);
    final carriageOutwards = _round(500 + _rand.nextDouble() * 1500);
    final rent = _round(6000 + _rand.nextDouble() * 6000);
    final salaries = _round(10000 + _rand.nextDouble() * 15000);
    final discountAllowed = _round(200 + _rand.nextDouble() * 800);
    final discountReceived = _round(200 + _rand.nextDouble() * 800);
    final commissionReceived = _round(500 + _rand.nextDouble() * 1500);
    final debtors = _round(10000 + _rand.nextDouble() * 20000);
    final creditors = _round(8000 + _rand.nextDouble() * 15000);
    final drawings = _round(2000 + _rand.nextDouble() * 8000);
    final cash = _round(2000 + _rand.nextDouble() * 8000);
    final bank = _round(10000 + _rand.nextDouble() * 20000);
    final furniture = _round(15000 + _rand.nextDouble() * 25000);
    final machinery = _round(30000 + _rand.nextDouble() * 50000);

    // Every debit-side trial balance item on one side, credit-side items
    // on the other; Capital is the plug that makes the two sides equal —
    // exactly how a real trial balance is given in these problems.
    final totalDebitItems = openingStock +
        purchases +
        wages +
        carriageInwards +
        carriageOutwards +
        rent +
        salaries +
        discountAllowed +
        debtors +
        drawings +
        cash +
        bank +
        furniture +
        machinery;
    // Sales Return is a debit-side trial balance item, so it belongs on
    // the debit total here even though the solver nets it against Sales
    // internally when building the Trading A/c.
    final totalCreditItemsExcludingCapital = purchasesReturn + sales + discountReceived + commissionReceived + creditors;
    final capital = (totalDebitItems + salesReturn) - totalCreditItemsExcludingCapital;

    final input = FinalAccountsInput(
      openingStock: openingStock,
      purchases: purchases,
      purchasesReturn: purchasesReturn,
      sales: sales,
      salesReturn: salesReturn,
      wages: wages,
      carriageInwards: carriageInwards,
      carriageOutwards: carriageOutwards,
      rent: rent,
      salaries: salaries,
      discountAllowed: discountAllowed,
      discountReceived: discountReceived,
      commissionReceived: commissionReceived,
      debtors: debtors,
      creditors: creditors,
      capital: capital,
      drawings: drawings,
      cash: cash,
      bank: bank,
      furniture: furniture,
      machinery: machinery,
    );

    final adjustments = _buildAdjustments(input, difficulty, schoolClass);
    final result = FinalAccountsSolver.solve(input, adjustments);

    return GeneratedFinalAccountsProblem(
      id: 'FA-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      input: input,
      adjustments: adjustments,
      result: result,
    );
  }

  /// Difficulty scales how many adjustments appear, same as before. Class
  /// 12 additionally injects adjustment *combinations* that Class 11 never
  /// sees at any difficulty — bad debts written off feeding into a
  /// provision calculated on the debtors balance net of that write-off
  /// (the classic harder GSEB/CBSE Class 12 twist), plus accrued/advance
  /// income on the same account — so a Class 12 paper is structurally
  /// harder than a Class 11 one at the same difficulty slider position,
  /// not just gated by which topics are visible.
  static List<Adjustment> _buildAdjustments(FinalAccountsInput input, int difficulty, int schoolClass) {
    final adjustments = <Adjustment>[
      Adjustment(
        type: AdjustmentType.closingStock,
        relatedItemName: 'Closing Stock',
        amount: _round(input.openingStock * (0.8 + _rand.nextDouble() * 0.6)),
        description: 'Closing Stock was valued at the year end.',
      ),
    ];

    if (difficulty >= 2) {
      final amt = _round(input.rent * 0.1);
      adjustments.add(Adjustment(
        type: AdjustmentType.outstandingExpense,
        relatedItemName: 'Rent',
        amount: amt,
        description: 'Rent ₹${amt.toStringAsFixed(0)} is outstanding.',
      ));
    }

    if (difficulty >= 3) {
      final amt = _round(input.furniture * 0.1);
      adjustments.add(Adjustment(
        type: AdjustmentType.depreciation,
        relatedItemName: 'Furniture',
        amount: amt,
        description: 'Depreciate Furniture by 10%.',
      ));
    }

    double debtorsAfterWriteOff = input.debtors;

    // Class 12 only: further bad debts written off after the trial
    // balance date, on top of whatever the trial balance already shows —
    // this is the combination that makes the subsequent provision
    // calculation genuinely harder, since it must be based on the
    // post-write-off debtors figure, not the trial balance figure.
    if (schoolClass == 12 && difficulty >= 3) {
      final amt = _round(input.debtors * 0.03);
      debtorsAfterWriteOff -= amt;
      adjustments.add(Adjustment(
        type: AdjustmentType.badDebts,
        relatedItemName: 'Debtors',
        amount: amt,
        description: 'Further Bad Debts of ₹${amt.toStringAsFixed(0)} are to be written off.',
      ));
    }

    if (difficulty >= 4) {
      final amt = _round(debtorsAfterWriteOff * 0.02);
      adjustments.add(Adjustment(
        type: AdjustmentType.provisionForDoubtfulDebts,
        relatedItemName: 'Debtors',
        amount: amt,
        description: schoolClass == 12
            ? 'Create a Provision for Doubtful Debts @ 2% on Debtors (after writing off the further bad debts above).'
            : 'Create a Provision for Doubtful Debts @ 2% on Debtors.',
      ));
    }

    if (difficulty >= 5) {
      final amt = _round(input.salaries * 0.08);
      adjustments.add(Adjustment(
        type: AdjustmentType.prepaidExpense,
        relatedItemName: 'Salaries',
        amount: amt,
        description: 'Salaries ₹${amt.toStringAsFixed(0)} paid in advance.',
      ));
    }

    // Class 12 only: accrued income and income received in advance on the
    // same Commission Received account in the same paper — students must
    // net two opposite adjustments against one figure, a combination
    // Class 11 papers never present.
    if (schoolClass == 12 && difficulty >= 5) {
      final accruedAmt = _round(input.commissionReceived * 0.1);
      final advanceAmt = _round(input.commissionReceived * 0.05);
      adjustments.add(Adjustment(
        type: AdjustmentType.accruedIncome,
        relatedItemName: 'Commission',
        amount: accruedAmt,
        description: 'Commission Received ₹${accruedAmt.toStringAsFixed(0)} is accrued but not yet received.',
      ));
      adjustments.add(Adjustment(
        type: AdjustmentType.incomeReceivedInAdvance,
        relatedItemName: 'Commission',
        amount: advanceAmt,
        description: 'Commission Received includes ₹${advanceAmt.toStringAsFixed(0)} received in advance for next year.',
      ));
    }

    return adjustments;
  }

  static double _round(double v) => (v / 100).round() * 100.0;
}

class GeneratedFinalAccountsProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final FinalAccountsInput input;
  final List<Adjustment> adjustments;
  final FinalAccountsResult result;

  const GeneratedFinalAccountsProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.input,
    required this.adjustments,
    required this.result,
  });
}
