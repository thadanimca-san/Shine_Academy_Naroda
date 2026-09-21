import 'practice_question.dart';

/// One section of a question paper — a labelled group of questions drawn
/// from one source (a grammar topic, a reading passage, or a chapter),
/// with simple marks-per-question so the paper shows a total.
class PaperSection {
  final String heading;
  final String instructions;
  final String? passageText;
  final List<PracticeQuestion> questions;
  final int marksPerQuestion;

  const PaperSection({
    required this.heading,
    required this.instructions,
    this.passageText,
    required this.questions,
    this.marksPerQuestion = 1,
  });

  int get totalMarks => questions.length * marksPerQuestion;
}

/// A full assembled question paper: a title/grade header and any number of
/// sections. Rendered as an on-screen preview and exportable as two
/// separate PDFs — the paper itself, and a matching answer key.
class QuestionPaper {
  final String title;
  final String grade;
  final List<PaperSection> sections;

  const QuestionPaper({
    required this.title,
    required this.grade,
    required this.sections,
  });

  int get totalMarks => sections.fold(0, (sum, s) => sum + s.totalMarks);
  int get totalQuestions => sections.fold(0, (sum, s) => sum + s.questions.length);
}
