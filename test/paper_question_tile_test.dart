import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/core/engine/assessment_engine.dart';
import 'package:shine_academy_naroda/features/assessment/widgets/paper_question_tile.dart';

void main() {
  final items = [
    AssessmentQuestion(moduleId: 'h', type: 'section_header', question: 'SECTION A', options: const [], correctIndexOrAnswer: '', marks: 0),
    AssessmentQuestion(moduleId: 'c', type: 'quiz', question: r'HCF of $2^{3}$ and $2^{2}$', options: const [r'$4$', r'$8$'],
        correctIndexOrAnswer: 0, explanationEn: 'Smallest power.', marks: 1),
    AssessmentQuestion(moduleId: 'c', type: 'descriptive', question: r'Prove that $\sqrt{5}$ is irrational.', options: const [],
        correctIndexOrAnswer: 'Assume rational\nContradiction', explanationEn: '1 mark: assumption', marks: 3),
  ];

  Future<void> pump(WidgetTester tester, {required bool answers}) => tester.pumpWidget(MaterialApp(
      home: Scaffold(body: ListView(children: buildPaperTiles(items, showAnswers: answers, isPdfMode: true)))));

  testWidgets('numbers questions, skips headers, renders formulas', (tester) async {
    await pump(tester, answers: false);
    expect(tester.takeException(), isNull);
    expect(find.text('Q1. '), findsOneWidget);
    expect(find.text('Q2. '), findsOneWidget);
    expect(find.text('[3]'), findsOneWidget);
    expect(find.byType(Math), findsWidgets);
    expect(find.text('Model answer:'), findsNothing);
  });

  testWidgets('answer key shows answers and marking scheme', (tester) async {
    await pump(tester, answers: true);
    expect(tester.takeException(), isNull);
    expect(find.text('Model answer:'), findsOneWidget);
    expect(find.text('Marking scheme:'), findsOneWidget);
    expect(find.text('Explanation:'), findsOneWidget);
  });
}
