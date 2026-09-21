import 'dart:math';

import '../data/question_paper_sources.dart';
import '../models/question_paper.dart';

/// How many questions to pull from one source, and what to call that
/// section on the paper.
class PaperSectionRequest {
  final PaperQuestionSource source;
  final int count;

  const PaperSectionRequest({required this.source, required this.count});
}

/// Assembles a [QuestionPaper] from a set of section requests, picking a
/// random subset of each source's bank so the same topic can be used to
/// generate a fresh paper next time without repeating the last one verbatim.
QuestionPaper buildQuestionPaper({
  required String grade,
  required String title,
  required List<PaperSectionRequest> requests,
  Random? random,
}) {
  final rng = random ?? Random();
  final sections = <PaperSection>[];

  for (final request in requests) {
    final bank = [...request.source.questions]..shuffle(rng);
    final count = request.count.clamp(0, bank.length);
    final chosen = bank.take(count).toList();
    if (chosen.isEmpty) continue;

    sections.add(PaperSection(
      heading: '${request.source.sectionKind}: ${request.source.label}',
      instructions: request.source.sectionKind == 'Reading'
          ? 'Read the passage and answer the questions that follow.'
          : 'Choose the correct option for each question.',
      passageText: request.source.passageText,
      questions: chosen,
    ));
  }

  return QuestionPaper(title: title, grade: grade, sections: sections);
}

/// True if a bank has enough questions to satisfy the requested count
/// without repeats — used by the setup screen to warn a teacher before
/// they ask for more questions than a source can honestly provide.
bool sourceCanSupply(PaperQuestionSource source, int count) => source.questions.length >= count;
