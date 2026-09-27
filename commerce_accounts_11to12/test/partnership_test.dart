import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/partnership_model.dart';
import 'package:commerce_accounts_11to12/services/partnership_solver.dart';

void main() {
  group('PartnershipSolver.solveAdmission', () {
    final partners = [
      const Partner(name: 'Ram', capital: 100000, profitShareRatio: 0.6),
      const Partner(name: 'Shyam', capital: 80000, profitShareRatio: 0.4),
    ];

    test('new profit sharing ratios sum to 1', () {
      final result = PartnershipSolver.solveAdmission(
        existingPartners: partners,
        newPartnerName: 'Mohan',
        newPartnerShare: 0.2,
        newPartnerCapital: 50000,
        goodwill: const GoodwillInfo(totalFirmGoodwill: 60000),
      );
      final total = result.newProfitSharingRatios.values.fold(0.0, (s, v) => s + v);
      expect(total, closeTo(1.0, 0.0001));
    });

    test('total goodwill credited to old partners equals goodwill debited to new partner', () {
      final result = PartnershipSolver.solveAdmission(
        existingPartners: partners,
        newPartnerName: 'Mohan',
        newPartnerShare: 0.25,
        newPartnerCapital: 50000,
        goodwill: const GoodwillInfo(totalFirmGoodwill: 80000),
      );
      final totalCredited = result.capitalAccounts
          .where((r) => r.partnerName != 'Mohan')
          .fold(0.0, (s, r) => s + r.goodwillCredit);
      final newPartnerRow = result.capitalAccounts.firstWhere((r) => r.partnerName == 'Mohan');
      expect(totalCredited, closeTo(newPartnerRow.goodwillDebit, 0.01));
    });

    test('sacrificing ratios sum to the new partner\'s share', () {
      final result = PartnershipSolver.solveAdmission(
        existingPartners: partners,
        newPartnerName: 'Mohan',
        newPartnerShare: 0.3,
        newPartnerCapital: 40000,
        goodwill: const GoodwillInfo(totalFirmGoodwill: 50000),
      );
      final totalSacrifice = result.sacrificingRatios.values.fold(0.0, (s, v) => s + v);
      expect(totalSacrifice, closeTo(0.3, 0.0001));
    });

    test('old partners\' capital account closing balance = opening + goodwill credited', () {
      final result = PartnershipSolver.solveAdmission(
        existingPartners: partners,
        newPartnerName: 'Mohan',
        newPartnerShare: 0.2,
        newPartnerCapital: 50000,
        goodwill: const GoodwillInfo(totalFirmGoodwill: 60000),
      );
      for (final row in result.capitalAccounts) {
        if (row.partnerName == 'Mohan') continue;
        expect(row.closingBalance, closeTo(row.openingBalance + row.goodwillCredit, 0.01));
      }
    });
  });

  group('PartnershipSolver.solveDeparture', () {
    final partners = [
      const Partner(name: 'Ram', capital: 100000, profitShareRatio: 0.4),
      const Partner(name: 'Shyam', capital: 90000, profitShareRatio: 0.35),
      const Partner(name: 'Mohan', capital: 70000, profitShareRatio: 0.25),
    ];

    test('remaining partners\' new ratios sum to 1', () {
      final result = PartnershipSolver.solveDeparture(
        allPartners: partners,
        departingPartnerName: 'Mohan',
        reason: DepartureReason.retirement,
        goodwill: const GoodwillInfo(totalFirmGoodwill: 100000),
      );
      final total = result.newProfitSharingRatios.values.fold(0.0, (s, v) => s + v);
      expect(total, closeTo(1.0, 0.0001));
    });

    test('gaining ratios sum to the departing partner\'s old share', () {
      final result = PartnershipSolver.solveDeparture(
        allPartners: partners,
        departingPartnerName: 'Mohan',
        reason: DepartureReason.retirement,
        goodwill: const GoodwillInfo(totalFirmGoodwill: 100000),
      );
      final totalGain = result.gainingRatios.values.fold(0.0, (s, v) => s + v);
      expect(totalGain, closeTo(0.25, 0.0001));
    });

    test('departing partner is paid exactly capital + their goodwill share', () {
      final result = PartnershipSolver.solveDeparture(
        allPartners: partners,
        departingPartnerName: 'Mohan',
        reason: DepartureReason.death,
        goodwill: const GoodwillInfo(totalFirmGoodwill: 100000),
      );
      // Mohan's share = 0.25, goodwill = 100000 -> owed goodwill = 25000
      expect(result.amountPayableToDepartingPartner, closeTo(70000 + 25000, 0.01));
    });

    test('total goodwill debited to remaining partners equals goodwill credited to departing partner', () {
      final result = PartnershipSolver.solveDeparture(
        allPartners: partners,
        departingPartnerName: 'Mohan',
        reason: DepartureReason.retirement,
        goodwill: const GoodwillInfo(totalFirmGoodwill: 100000),
      );
      final totalDebited = result.capitalAccounts
          .where((r) => r.partnerName != 'Mohan')
          .fold(0.0, (s, r) => s + r.goodwillDebit);
      final departingRow = result.capitalAccounts.firstWhere((r) => r.partnerName == 'Mohan');
      expect(totalDebited, closeTo(departingRow.goodwillCredit, 0.01));
    });
  });
}
