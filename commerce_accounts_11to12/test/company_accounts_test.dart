import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/company_accounts_model.dart';
import 'package:commerce_accounts_11to12/services/company_accounts_solver.dart';

void main() {
  group('CompanyAccountsSolver.solveFullySubscribedIssue', () {
    const calls = CallStructure(
      faceValue: 10,
      premiumPerShare: 2,
      applicationAmount: 3,
      allotmentAmount: 4, // includes the 2 premium
      firstCallAmount: 3,
      finalCallAmount: 2,
    );

    test('total capital raised equals shares issued times face value (no forfeiture)', () {
      final result = CompanyAccountsSolver.solveFullySubscribedIssue(
        sharesIssued: 10000,
        calls: calls,
        sharesForfeitedForFinalCallDefault: 0,
        reissuePricePerShare: 10,
      );
      expect(result.totalCapitalRaised, closeTo(100000, 0.01));
    });

    test('securities premium balance equals shares issued times premium per share', () {
      final result = CompanyAccountsSolver.solveFullySubscribedIssue(
        sharesIssued: 10000,
        calls: calls,
        sharesForfeitedForFinalCallDefault: 0,
        reissuePricePerShare: 10,
      );
      expect(result.securitiesPremiumBalance, closeTo(20000, 0.01));
    });

    test('forfeiture debits Share Capital with exactly the called-up amount (excluding final call)', () {
      final result = CompanyAccountsSolver.solveFullySubscribedIssue(
        sharesIssued: 10000,
        calls: calls,
        sharesForfeitedForFinalCallDefault: 100,
        reissuePricePerShare: 8,
      );
      final forfeitureStep = result.steps.firstWhere((s) => s.title == 'Forfeiture of Shares');
      // Called up per share excluding final call = 3+4+3 = 10; x 100 shares = 1000
      expect(forfeitureStep.secondCreditAmount, closeTo(1000, 0.01));
    });

    test('reissue at a loss uses Forfeited Shares A/c to cover the deficiency, never goes negative', () {
      final result = CompanyAccountsSolver.solveFullySubscribedIssue(
        sharesIssued: 10000,
        calls: calls,
        sharesForfeitedForFinalCallDefault: 100,
        reissuePricePerShare: 8, // below face value of 10 -> deficiency of 2/share = 200 total
      );
      expect(result.forfeitedSharesAccountBalance, closeTo(1000, 0.01)); // paid-up amount forfeited
      expect(result.capitalReserveOnReissue, closeTo(1000 - 200, 0.01));
      expect(result.capitalReserveOnReissue, greaterThanOrEqualTo(0));
    });

    test('reissue at exactly face value transfers the full forfeited balance to Capital Reserve', () {
      final result = CompanyAccountsSolver.solveFullySubscribedIssue(
        sharesIssued: 10000,
        calls: calls,
        sharesForfeitedForFinalCallDefault: 100,
        reissuePricePerShare: 10, // exactly face value -> no deficiency
      );
      expect(result.capitalReserveOnReissue, closeTo(result.forfeitedSharesAccountBalance, 0.01));
    });

    test('every step\'s debit (cash) matches its credit total (steps individually balance)', () {
      final result = CompanyAccountsSolver.solveFullySubscribedIssue(
        sharesIssued: 5000,
        calls: calls,
        sharesForfeitedForFinalCallDefault: 50,
        reissuePricePerShare: 9,
      );
      for (final step in result.steps) {
        if (step.title == 'Forfeiture of Shares') continue; // no cash movement, dual capital/forfeited entry
        final totalDebit = step.debitCash + (step.secondDebitAmount ?? 0);
        final totalCredit = step.creditAmount + (step.secondCreditAmount ?? 0);
        expect(totalDebit, closeTo(totalCredit, 0.01), reason: 'Step "${step.title}" does not balance');
      }
    });
  });
}
