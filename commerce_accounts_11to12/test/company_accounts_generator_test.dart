import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/company_accounts_generator.dart';

void main() {
  group('CompanyAccountsGenerator', () {
    test('generated problems always have non-negative capital reserve and forfeited balance', () {
      for (var i = 0; i < 50; i++) {
        final problem = CompanyAccountsGenerator.generate(
          board: Board.gseb,
          schoolClass: 12,
          difficulty: (i % 5) + 1,
        );
        expect(problem.result.forfeitedSharesAccountBalance, greaterThanOrEqualTo(0),
            reason: 'Failed for ${problem.id}');
        expect(problem.result.capitalReserveOnReissue, greaterThanOrEqualTo(0), reason: 'Failed for ${problem.id}');
      }
    });

    test('all call amounts per share sum to face value + premium', () {
      for (var i = 0; i < 20; i++) {
        final problem = CompanyAccountsGenerator.generate(board: Board.cbse, schoolClass: 12, difficulty: 3);
        final c = problem.calls;
        expect(c.totalPerShare, closeTo(c.faceValue + c.premiumPerShare, 0.01));
      }
    });

    test('every generated step has a non-negative debit and credit', () {
      for (var i = 0; i < 20; i++) {
        final problem = CompanyAccountsGenerator.generate(board: Board.gseb, schoolClass: 12, difficulty: 5);
        for (final step in problem.result.steps) {
          expect(step.debitCash, greaterThanOrEqualTo(0));
          expect(step.creditAmount, greaterThanOrEqualTo(0));
        }
      }
    });
  });
}
