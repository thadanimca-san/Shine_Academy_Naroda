import 'dart:math';

import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/core/engine/assessment_engine.dart';
import 'package:shine_academy_naroda/core/engine/content_repository.dart';
import 'package:shine_academy_naroda/core/engine/paper_generator.dart';

PaperBlueprint _blueprint() => PaperBlueprint.fromJson({
      'id': 'test', 'title': 'Test', 'total_marks': 7, 'duration_minutes': 60,
      'sections': [
        {'name': 'A', 'title': 'MCQ', 'types': ['mcq'], 'count': 3, 'marks_each': 1},
        {'name': 'B', 'title': 'Short', 'types': ['short_answer'], 'count': 2, 'marks_each': 2},
      ],
    });

BankQuestion _q(String chapter, String id, String type) => BankQuestion(chapter, {
      'id': id, 'type': type, 'question': id, 'options': ['a', 'b'], 'correct_index': 0,
      'answer_steps': ['step'], 'marking_scheme': ['1 mark'],
    });

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('fills each section and never repeats a question', () {
    final pool = [for (var i = 0; i < 5; i++) _q('ch1', 'm$i', 'mcq'), for (var i = 0; i < 3; i++) _q('ch1', 's$i', 'short_answer')];
    final paper = PaperGenerator.generate(blueprint: _blueprint(), pool: pool, random: Random(1));
    final questions = paper.items.where((q) => q.type != 'section_header').toList();
    expect(questions, hasLength(5));
    expect(questions.map((q) => q.question).toSet(), hasLength(5));
    expect(paper.totalMarks, 7);
    expect(paper.isComplete, isTrue);
    expect(paper.items.where((q) => q.type == 'section_header'), hasLength(2));
  });

  test('spreads questions across chapters', () {
    final pool = [for (var i = 0; i < 5; i++) _q('ch1', 'a$i', 'mcq'), for (var i = 0; i < 5; i++) _q('ch2', 'b$i', 'mcq')];
    final paper = PaperGenerator.generate(blueprint: _blueprint(), pool: pool, random: Random(2));
    final chapters = paper.items.where((q) => q.type == 'quiz').map((q) => q.moduleId).toSet();
    expect(chapters, {'ch1', 'ch2'});
  });

  test('reports sections that cannot be filled yet', () {
    final paper = PaperGenerator.generate(blueprint: _blueprint(), pool: [_q('ch1', 'm0', 'mcq')], random: Random(3));
    expect(paper.isComplete, isFalse);
    expect(paper.shortfalls.map((s) => '${s.section}:${s.found}/${s.wanted}'), ['A:1/3', 'B:0/2']);
  });

  test('same seed gives the same paper', () {
    final pool = [for (var i = 0; i < 9; i++) _q('ch1', 'm$i', 'mcq')];
    List<String> ids(int seed) => PaperGenerator.generate(blueprint: _blueprint(), pool: pool, random: Random(seed))
        .items.map((q) => q.question).toList();
    expect(ids(7), ids(7));
  });

  test('real CBSE Class 10 Maths blueprint builds from Chapter 1', () async {
    final blueprint = await ContentRepository.instance.blueprintForSubject('cbse_class10_math');
    expect(blueprint, isNotNull);
    expect(blueprint!.sections.fold<int>(0, (sum, s) => sum + s.count * s.marksEach), 80);

    final paper = await AssessmentEngine.instance.generateFromBlueprint(['ncert_class10_maths_ch1'], 'cbse_class10_math', random: Random(1));
    expect(paper!.items.where((q) => q.section == 'A' && q.type == 'quiz'), hasLength(20));
    expect(paper.shortfalls.map((s) => s.section), contains('D')); // Chapter 1 has no 5-mark questions
  });
}
