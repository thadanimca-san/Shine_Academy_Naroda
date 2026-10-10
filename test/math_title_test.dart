import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/features/common/widgets/math_title.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/widgets/worked_example_widget.dart';

void main() {
  testWidgets('a title with LaTeX renders the formula, not dollar signs', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: MathTitle(r'Theorem 1.3: $\sqrt{2}$ is irrational'))));
    await tester.pump();
    expect(find.byType(Math), findsOneWidget);
    expect(find.textContaining(r'$', findRichText: true), findsNothing);
  });

  testWidgets('a plain title stays plain text', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: MathTitle('Chapter summary'))));
    expect(find.text('Chapter summary'), findsOneWidget);
    expect(find.byType(Math), findsNothing);
  });

  testWidgets('worked example titles render maths', (tester) async {
    await tester.pumpWidget(const MaterialApp(home: Scaffold(body: SingleChildScrollView(child: WorkedExampleWidget(data: {
      'title': r'Theorem 1.3: $\sqrt{2}$ is irrational', 'problem': r'Prove that $\sqrt{2}$ is irrational.', 'steps': ['Assume the contrary.'], 'answer': 'Proved.',
    })))));
    await tester.pump();
    expect(find.byType(Math), findsWidgets);
    expect(find.textContaining(r'$\sqrt', findRichText: true), findsNothing);
  });
}
