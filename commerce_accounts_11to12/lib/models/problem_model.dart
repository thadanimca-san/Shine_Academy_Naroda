import 'account_model.dart';

enum Board { gseb, cbse }

enum PaperPatternType { mcq, short, long }

/// Where a generated problem sits in the syllabus, used for both student
/// topic navigation and teacher paper-topic selection.
class TopicRef {
  final Board board;
  final int schoolClass; // 11 or 12
  final String chapter; // e.g. "Journal Entries"
  final String subtopic; // e.g. "Compound Entries"

  const TopicRef({
    required this.board,
    required this.schoolClass,
    required this.chapter,
    required this.subtopic,
  });
}

/// A fully generated practice/exam problem: the question as shown to the
/// student, the underlying structured data (journal entries) the solver
/// engine will use, and metadata for paper assembly.
class GeneratedProblem {
  final String id;
  final TopicRef topic;
  final int difficulty; // 1 (easy) .. 5 (hard)
  final PaperPatternType patternType;
  final double marks;
  final String questionText;
  final List<JournalEntry> transactions;

  const GeneratedProblem({
    required this.id,
    required this.topic,
    required this.difficulty,
    required this.patternType,
    required this.marks,
    required this.questionText,
    required this.transactions,
  });
}
