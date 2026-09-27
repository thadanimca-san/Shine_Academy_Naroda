import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/dissolution_generator.dart';

void main() {
  group('DissolutionGenerator', () {
    test('every generated problem has partner shares summing to the total realisation profit/loss', () {
      for (var i = 0; i < 40; i++) {
        final problem = DissolutionGenerator.generate(board: Board.gseb, schoolClass: 12, difficulty: (i % 5) + 1);
        final totalShares = problem.result.partnerSettlements.fold(0.0, (s, p) => s + p.shareOfRealisationProfit);
        expect(totalShares, closeTo(problem.result.realisationProfitOrLoss, 0.01), reason: 'Failed for ${problem.id}');
      }
    });

    test('every generated problem produces at least one asset and one liability entry', () {
      for (var i = 0; i < 20; i++) {
        final problem = DissolutionGenerator.generate(board: Board.cbse, schoolClass: 12, difficulty: 3);
        expect(problem.assets, isNotEmpty);
        expect(problem.liabilities, isNotEmpty);
      }
    });
  });
}
