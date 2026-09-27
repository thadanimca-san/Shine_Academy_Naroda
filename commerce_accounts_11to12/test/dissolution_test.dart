import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/dissolution_model.dart';
import 'package:commerce_accounts_11to12/models/partnership_model.dart';
import 'package:commerce_accounts_11to12/services/dissolution_solver.dart';

void main() {
  group('DissolutionSolver', () {
    final partners = [
      const Partner(name: 'Ram', capital: 60000, profitShareRatio: 0.6),
      const Partner(name: 'Shyam', capital: 40000, profitShareRatio: 0.4),
    ];

    test('realisation profit/loss equals total credit minus total debit', () {
      final result = DissolutionSolver.solve(
        partners: partners,
        assets: const [
          AssetRealisation(assetName: 'Machinery', bookValue: 30000, realisedAmount: 35000),
        ],
        liabilities: const [
          LiabilityPayment(liabilityName: 'Creditors', bookValue: 10000, amountPaid: 10000),
        ],
      );
      final totalDebit = result.realisationDebit.fold(0.0, (s, l) => s + l.amount);
      final totalCredit = result.realisationCredit.fold(0.0, (s, l) => s + l.amount);
      expect(result.realisationProfitOrLoss, closeTo(totalCredit - totalDebit, 0.01));
      // Machinery 30000 debit, Creditors payment 10000 debit -> 40000 debit
      // Creditors 10000 credit, Machinery sale 35000 credit -> 45000 credit
      // Profit = 5000
      expect(result.realisationProfitOrLoss, closeTo(5000, 0.01));
    });

    test('realisation profit is shared among partners exactly in their ratio', () {
      final result = DissolutionSolver.solve(
        partners: partners,
        assets: const [
          AssetRealisation(assetName: 'Machinery', bookValue: 30000, realisedAmount: 40000),
        ],
        liabilities: const [],
      );
      final ramShare = result.partnerSettlements.firstWhere((s) => s.partnerName == 'Ram');
      final shyamShare = result.partnerSettlements.firstWhere((s) => s.partnerName == 'Shyam');
      // Profit = 10000; Ram 60% = 6000, Shyam 40% = 4000
      expect(ramShare.shareOfRealisationProfit, closeTo(6000, 0.01));
      expect(shyamShare.shareOfRealisationProfit, closeTo(4000, 0.01));
    });

    test('a realisation loss reduces each partner\'s final settlement below their capital', () {
      final result = DissolutionSolver.solve(
        partners: partners,
        assets: const [
          AssetRealisation(assetName: 'Furniture', bookValue: 30000, realisedAmount: 15000), // sold at a big loss
        ],
        liabilities: const [],
      );
      expect(result.realisationProfitOrLoss, lessThan(0));
      for (final s in result.partnerSettlements) {
        expect(s.finalAmountReceived, lessThan(s.capitalBalance));
      }
    });

    test('final amount received = capital balance + share of realisation profit/loss', () {
      final result = DissolutionSolver.solve(
        partners: partners,
        assets: const [
          AssetRealisation(assetName: 'Stock', bookValue: 20000, realisedAmount: 18000),
        ],
        liabilities: const [
          LiabilityPayment(liabilityName: 'Bills Payable', bookValue: 5000, amountPaid: 5000),
        ],
        dissolutionExpenses: 1000,
      );
      for (final s in result.partnerSettlements) {
        expect(s.finalAmountReceived, closeTo(s.capitalBalance + s.shareOfRealisationProfit, 0.01));
      }
    });

    test('sum of all partners\' shares of profit/loss equals the total realisation profit/loss', () {
      final result = DissolutionSolver.solve(
        partners: partners,
        assets: const [
          AssetRealisation(assetName: 'Investments', bookValue: 25000, realisedAmount: 27000),
        ],
        liabilities: const [
          LiabilityPayment(liabilityName: 'Bank Loan', bookValue: 8000, amountPaid: 8500),
        ],
      );
      final totalShares = result.partnerSettlements.fold(0.0, (s, p) => s + p.shareOfRealisationProfit);
      expect(totalShares, closeTo(result.realisationProfitOrLoss, 0.01));
    });
  });
}
