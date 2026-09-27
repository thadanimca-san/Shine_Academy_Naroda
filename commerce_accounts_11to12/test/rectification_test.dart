import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/models/rectification_model.dart';
import 'package:commerce_accounts_11to12/services/rectification_generator.dart';

void main() {
  group('RectificationGenerator', () {
    test('every rectifying entry is balanced', () {
      for (var i = 0; i < 30; i++) {
        final problem = RectificationGenerator.generate(
          board: Board.gseb,
          schoolClass: 11,
          difficulty: (i % 5) + 1,
        );
        for (final c in problem.cases) {
          expect(c.rectifyingEntry.isBalanced, isTrue,
              reason: 'Unbalanced rectification: ${c.errorDescription}');
        }
      }
    });

    test('one-sided errors use the Suspense account, two-sided errors do not', () {
      final problem = RectificationGenerator.generate(
        board: Board.cbse,
        schoolClass: 11,
        difficulty: 5,
        caseCount: 20,
      );
      for (final c in problem.cases) {
        final usesSuspense = c.rectifyingEntry.lines.any((l) => l.account.name == 'Suspense');
        if (c.effect == ErrorEffect.oneSided) {
          expect(usesSuspense, isTrue, reason: 'One-sided error should use Suspense: ${c.errorDescription}');
        } else {
          expect(usesSuspense, isFalse, reason: 'Two-sided error should not use Suspense: ${c.errorDescription}');
        }
      }
    });
  });
}
