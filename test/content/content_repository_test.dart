import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/core/engine/assessment_engine.dart';
import 'package:shine_academy_naroda/core/engine/content_repository.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('legacy module id resolves to the new-format chapter', () async {
    final chapter = await ContentRepository.instance.loadChapter('ncert_class10_maths_ch1');
    expect(chapter, isNotNull);
    expect(chapter!.entry.id, 'cbse.c10.maths.ncert_rationalised.ch01');
    expect(chapter.blocks.first['type'], 'heading');
    expect(chapter.blocks.where((b) => b['type'] == 'factor_tree'), hasLength(1));
  });

  test('unknown ids fall back to legacy content', () async {
    expect(await ContentRepository.instance.loadChapter('ncert_class10_maths_ch9'), isNull);
    expect(await ContentRepository.instance.loadQuestions('ncert_class10_maths_ch9'), isNull);
  });

  test('question bank converts for the practice screens', () async {
    final questions = await ContentRepository.instance.loadQuestions('ncert_class10_maths_ch1');
    expect(questions, isNotEmpty);
    final converted = questions!.map((q) => AssessmentQuestion.fromBankQuestion(q, 'ncert_class10_maths_ch1')).toList();
    final mcq = converted.firstWhere((q) => q.type == 'quiz');
    expect(mcq.options.length, greaterThanOrEqualTo(2));
    expect(mcq.correctIndexOrAnswer, isA<int>());
    expect(converted.where((q) => q.type == 'descriptive').every((q) => (q.correctIndexOrAnswer as String).isNotEmpty), isTrue);
  });

  test('chapters are listed for the paper generator', () async {
    final chapters = await ContentRepository.instance.chaptersFor(board: 'CBSE', classNumber: 10, subject: 'maths');
    expect(chapters.map((c) => c.chapterNumber), contains(1));
  });
}
