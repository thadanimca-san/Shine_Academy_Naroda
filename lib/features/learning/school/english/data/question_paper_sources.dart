import '../models/practice_question.dart';
import 'figures_of_speech_practice.dart';
import 'practice_topics.dart';
import 'reading_topics.dart';

/// One selectable source of exam questions — a grammar topic or a reading
/// passage, both already expressed as [PracticeQuestion] banks elsewhere in
/// the app. The Question Paper Generator draws from these.
class PaperQuestionSource {
  final String id;
  final String label;
  final String grade;
  final String sectionKind; // 'Grammar' or 'Reading'
  final String? passageText;
  final List<PracticeQuestion> questions;

  const PaperQuestionSource({
    required this.id,
    required this.label,
    required this.grade,
    required this.sectionKind,
    this.passageText,
    required this.questions,
  });
}

/// All grades that have question-paper-ready content, derived from the same
/// per-grade grammar and reading registries used elsewhere in the app —
/// Class 7-10 all have both today, and any future grade added to those
/// registries is picked up here automatically.
final List<String> gradesWithPaperContent = _sourcesByGrade.keys.toList();

final Map<String, List<PaperQuestionSource>> _sourcesByGrade = {
  for (final grade in practiceTopicsByGrade.keys)
    grade: [
      for (final topic in practiceTopicsByGrade[grade]!)
        PaperQuestionSource(
          id: topic.id,
          label: topic.title,
          grade: topic.grade,
          sectionKind: 'Grammar',
          questions: topic.bank,
        ),
      for (final passage in (readingLibraryByGrade[grade]?.passages ?? const []))
        PaperQuestionSource(
          id: passage.id,
          label: passage.title,
          grade: passage.grade,
          sectionKind: 'Reading',
          passageText: passage.body,
          questions: passage.questions,
        ),
      // Figures of Speech is a single grade-agnostic bank (Class 7-10), so
      // every grade gets it offered as an extra selectable source.
      PaperQuestionSource(
        id: figuresOfSpeechPractice.id,
        label: figuresOfSpeechPractice.title,
        grade: grade,
        sectionKind: 'Figures of Speech',
        questions: figuresOfSpeechPractice.bank,
      ),
    ],
};

List<PaperQuestionSource> paperSourcesForGrade(String grade) => _sourcesByGrade[grade] ?? const [];
