class QuestionItem {
  final String id;
  final String question; // Contains bracketed options e.g. "[ optionA / optionB ]"
  final String answer;

  QuestionItem({
    required this.id,
    required this.question,
    required this.answer,
  });

  Map<String, dynamic> toJson() => {
        'id': id,
        'question': question,
        'answer': answer,
      };
}

class NumericalProblem {
  final String id;
  final String question;
  final List<String> given; // e.g. "u = 5 m/s", "a = 2 m/s^2", "t = 4 s"
  final List<String> solutionSteps;
  final double numericAnswer;
  final String unit;

  NumericalProblem({
    required this.id,
    required this.question,
    required this.given,
    required this.solutionSteps,
    required this.numericAnswer,
    required this.unit,
  });

  String get formattedAnswer {
    final formatted = numericAnswer == numericAnswer.roundToDouble() && numericAnswer.abs() < 1e6
        ? numericAnswer.toStringAsFixed(0)
        : numericAnswer.toStringAsFixed(2);
    return '$formatted $unit';
  }
}

class FormulaDerivation {
  final String formulaName;
  final String expression;
  final List<String> derivationSteps;

  FormulaDerivation({
    required this.formulaName,
    required this.expression,
    required this.derivationSteps,
  });
}

/// A quick-revision card covering one sub-topic of a chapter: a short title,
/// a handful of exam-ready bullet points, and an icon key naming which
/// small illustration [RevisionNoteIcon] should draw beside it (kept as a
/// string so chapter data files don't need to import Flutter/painting
/// code — see `lib/widgets/revision_notes_section.dart` for the icons).
class RevisionNote {
  final String title;
  final String iconKey;
  final List<String> points;

  RevisionNote({
    required this.title,
    required this.iconKey,
    required this.points,
  });
}

class ChapterModel {
  final int standard; // e.g. 7, 8, 9, 10
  final String subject; // "Physics", "Chemistry", or "Biology"
  final String chapterId;
  final String chapterName;
  final List<String> concepts;
  final List<FormulaDerivation> formulas;
  final List<QuestionItem> fillInTheBlanks;
  final List<NumericalProblem> numericalProblems;
  final List<RevisionNote> revisionNotes;
  final String? imagePath; // NEW: Optional beautiful cover image

  ChapterModel({
    required this.standard,
    required this.subject,
    required this.chapterId,
    required this.chapterName,
    required this.concepts,
    required this.formulas,
    required this.fillInTheBlanks,
    this.numericalProblems = const [],
    this.revisionNotes = const [],
    this.imagePath,
  });
}