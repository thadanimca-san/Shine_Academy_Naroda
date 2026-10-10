import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/widgets/game_quiz_card.dart';

void main() {
  setUp(() => SharedPreferences.setMockInitialValues({}));

  Future<List<QuizAnswerResult>> pump(WidgetTester tester, {List<String> options = const ['A', 'B', 'C', 'D']}) async {
    final results = <QuizAnswerResult>[];
    await tester.pumpWidget(MaterialApp(
      home: Scaffold(
        body: SingleChildScrollView(
          child: GameQuizCard(
            question: 'Pick B',
            options: options,
            correctIndex: 1,
            explanation: 'B is right.',
            optionFeedback: [for (final o in options) o == 'B' ? 'Correct! because B.' : 'Not $o: think again.'],
            onAnswered: results.add,
          ),
        ),
      ),
    ));
    return results;
  }

  testWidgets('explains a wrong choice, allows a retry, then rewards', (tester) async {
    final results = await pump(tester);
    await tester.tap(find.text('C', findRichText: true));
    await tester.pump(const Duration(milliseconds: 500));
    expect(find.text('Not C: think again.', findRichText: true), findsOneWidget);
    expect(results, isEmpty);

    await tester.tap(find.text('B', findRichText: true));
    await tester.pumpAndSettle(const Duration(seconds: 2));
    expect(find.text('Correct! because B.', findRichText: true), findsOneWidget);
    expect(results.single.correct, isTrue);
    expect(results.single.attempts, 2);
    expect(results.single.xpEarned, 20);
  });

  testWidgets('two wrong answers reveal the answer with its explanation', (tester) async {
    final results = await pump(tester);
    await tester.tap(find.text('A', findRichText: true));
    await tester.pump(const Duration(milliseconds: 500));
    await tester.tap(find.text('D', findRichText: true));
    await tester.pumpAndSettle();
    expect(results.single.correct, isFalse);
    expect(find.text('Correct! because B.', findRichText: true), findsOneWidget);
    expect(find.text('Not D: think again.', findRichText: true), findsOneWidget);
  });

  testWidgets('true/false gets no retry', (tester) async {
    final results = await pump(tester, options: const ['A', 'B']);
    await tester.tap(find.text('A', findRichText: true));
    await tester.pumpAndSettle();
    expect(results.single.correct, isFalse);
  });

  testWidgets('first-try correct earns full XP', (tester) async {
    final results = await pump(tester);
    await tester.tap(find.text('B', findRichText: true));
    await tester.pumpAndSettle(const Duration(seconds: 2));
    expect(results.single.xpEarned, 50);
  });
}
