import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/widgets/function_graph_widget.dart';

void main() {
  test('evaluates polynomials, highest power first', () {
    expect(evaluatePolynomial([1, -3, -4], 4), 0);
    expect(evaluatePolynomial([1, -3, -4], -1), 0);
    expect(evaluatePolynomial([3], 10), 3);
  });

  testWidgets('draws and finishes the animation without errors', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: Scaffold(body: SingleChildScrollView(child: FunctionGraphWidget(data: {
        'polynomial': [1, -3, -4], 'x_range': [-3, 6], 'zeroes': [-1, 4], 'title': 'Two zeroes', 'label': r'y = x^{2} - 3x - 4',
      }))),
    ));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
    expect(find.text('Two zeroes'), findsOneWidget);
  });

  testWidgets('reduced motion shows the finished graph at once', (tester) async {
    await tester.pumpWidget(const MaterialApp(
      home: MediaQuery(
        data: MediaQueryData(disableAnimations: true),
        child: Scaffold(body: SingleChildScrollView(child: FunctionGraphWidget(data: {'polynomial': [1, 0, -4], 'zeroes': [-2, 2]}))),
      ),
    ));
    await tester.pump();
    expect(tester.hasRunningAnimations, isFalse);
  });

  testWidgets('draws a pair of lines with their intersection point', (tester) async {
    const data = {
      'curves': [
        {'polynomial': [-1, 10], 'label': 'x + y = 10'},
        {'polynomial': [1, -4], 'label': 'x - y = 4'},
      ],
      'points': [{'x': 7, 'y': 3, 'label': '(7, 3)', 'on': [0, 1]}],
      'x_range': [-1, 11],
      'title': 'Two lines',
    };
    expect(graphCurves(data), hasLength(2));
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: SingleChildScrollView(child: FunctionGraphWidget(data: data)))));
    await tester.pumpAndSettle();
    expect(tester.takeException(), isNull);
    expect(find.text('Two lines'), findsOneWidget);
  });
}
