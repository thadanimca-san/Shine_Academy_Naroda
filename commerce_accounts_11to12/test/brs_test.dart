import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/brs_generator.dart';
import 'package:commerce_accounts_11to12/services/brs_solver.dart';

void main() {
  group('BrsSolver', () {
    test('reversing Cash Book -> Pass Book -> Cash Book returns the original balance', () {
      for (var i = 0; i < 30; i++) {
        final problem = BrsGenerator.generate(board: Board.gseb, schoolClass: 11, difficulty: (i % 5) + 1);
        final roundTrip = BrsSolver.computeCashBookBalanceFromPassBook(problem.passBookBalance, problem.items);
        expect(roundTrip, closeTo(problem.cashBookBalance, 0.01),
            reason: 'Round-trip mismatch for problem ${problem.id}');
      }
    });

    test('generated passBookBalance matches solver recomputation', () {
      final problem = BrsGenerator.generate(board: Board.cbse, schoolClass: 11, difficulty: 4, itemCount: 5);
      final recomputed = BrsSolver.computePassBookBalanceFromCashBook(problem.cashBookBalance, problem.items);
      expect(recomputed, closeTo(problem.passBookBalance, 0.01));
    });

    test('explainStartingFromCashBook produces one step per item plus start/result', () {
      final problem = BrsGenerator.generate(board: Board.gseb, schoolClass: 11, difficulty: 3, itemCount: 4);
      final steps = BrsSolver.explainStartingFromCashBook(problem.cashBookBalance, problem.items);
      expect(steps.length, problem.items.length + 2);
    });
  });
}
