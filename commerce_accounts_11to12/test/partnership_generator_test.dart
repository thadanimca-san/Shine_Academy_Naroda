import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/partnership_generator.dart';

void main() {
  group('PartnershipGenerator', () {
    test('generated admission problems always produce ratios summing to 1', () {
      for (var i = 0; i < 40; i++) {
        final problem = PartnershipGenerator.generateAdmission(
          board: Board.gseb,
          schoolClass: 12,
          difficulty: (i % 5) + 1,
        );
        final total = problem.result.newProfitSharingRatios.values.fold(0.0, (s, v) => s + v);
        expect(total, closeTo(1.0, 0.001), reason: 'Failed for ${problem.id}');
      }
    });

    test('generated departure problems always produce remaining ratios summing to 1', () {
      for (var i = 0; i < 40; i++) {
        final problem = PartnershipGenerator.generateDeparture(
          board: Board.cbse,
          schoolClass: 12,
          difficulty: (i % 5) + 1,
        );
        final total = problem.result.newProfitSharingRatios.values.fold(0.0, (s, v) => s + v);
        expect(total, closeTo(1.0, 0.001), reason: 'Failed for ${problem.id}');
      }
    });

    test('departing partner is never left in the remaining ratios', () {
      final problem = PartnershipGenerator.generateDeparture(board: Board.gseb, schoolClass: 12, difficulty: 3);
      expect(problem.result.newProfitSharingRatios.containsKey(problem.departingPartnerName), isFalse);
    });

    test('amount payable to departing partner is always positive', () {
      for (var i = 0; i < 20; i++) {
        final problem = PartnershipGenerator.generateDeparture(board: Board.gseb, schoolClass: 12, difficulty: 3);
        expect(problem.result.amountPayableToDepartingPartner, greaterThan(0));
      }
    });
  });
}
