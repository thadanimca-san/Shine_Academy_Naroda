import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/widgets/factor_tree_widget.dart';

void main() {
  test('splits off the smallest prime at each level', () {
    expect(factorTreeLevels(140), [(2, 70), (2, 35), (5, 7)]);
    expect(factorTreeLevels(7429), [(17, 437), (19, 23)]);
    expect(factorTreeLevels(13), isEmpty);
  });

  test('writes the factorisation in power form', () {
    expect(primePowerTex(140), r'2^{2} \times 5 \times 7');
    expect(primePowerTex(3825), r'3^{2} \times 5^{2} \times 17');
  });

  testWidgets('animates to the full tree without errors', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: Scaffold(body: FactorTreeWidget(data: {'number': 140, 'title': 'Factor tree of 140'})),
    ));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
    expect(find.text('Factor tree of 140'), findsOneWidget);
  });
}
