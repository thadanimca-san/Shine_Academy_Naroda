import 'dart:math';

import 'assessment_engine.dart';

/// A board's question paper pattern, read from `app_core/content/paper_blueprints/`.
class PaperBlueprint {
  final String id;
  final String title;
  final int totalMarks;
  final int durationMinutes;
  final List<String> instructions;
  final List<BlueprintSection> sections;

  const PaperBlueprint({
    required this.id,
    required this.title,
    required this.totalMarks,
    required this.durationMinutes,
    required this.instructions,
    required this.sections,
  });

  factory PaperBlueprint.fromJson(Map<String, dynamic> json) => PaperBlueprint(
        id: json['id'] as String,
        title: json['title'] as String,
        totalMarks: json['total_marks'] as int,
        durationMinutes: json['duration_minutes'] as int,
        instructions: List<String>.from(json['general_instructions'] ?? const []),
        sections: (json['sections'] as List)
            .cast<Map<String, dynamic>>()
            .map(BlueprintSection.fromJson)
            .toList(growable: false),
      );
}

class BlueprintSection {
  final String name;
  final String title;
  final Set<String> questionTypes;
  final int count;
  final int marksEach;

  const BlueprintSection({
    required this.name,
    required this.title,
    required this.questionTypes,
    required this.count,
    required this.marksEach,
  });

  factory BlueprintSection.fromJson(Map<String, dynamic> json) => BlueprintSection(
        name: json['name'] as String,
        title: json['title'] as String,
        questionTypes: Set<String>.from(json['types'] as List),
        count: json['count'] as int,
        marksEach: json['marks_each'] as int,
      );
}

/// A question from a chapter's question bank, tagged with the chapter it came from.
class BankQuestion {
  final String moduleId;
  final Map<String, dynamic> data;
  const BankQuestion(this.moduleId, this.data);

  String get id => data['id'] as String;
  String get type => data['type'] as String;
}

/// A section that could not be filled because the chosen chapters do not
/// have enough questions of the right type yet.
class SectionShortfall {
  final String section;
  final int wanted;
  final int found;
  const SectionShortfall(this.section, this.wanted, this.found);
}

class GeneratedPaper {
  final PaperBlueprint blueprint;

  /// Section headers followed by their questions, in paper order.
  final List<AssessmentQuestion> items;
  final List<SectionShortfall> shortfalls;

  const GeneratedPaper({required this.blueprint, required this.items, required this.shortfalls});

  int get totalMarks => items.where((q) => q.type != 'section_header').fold(0, (sum, q) => sum + q.marks);
  bool get isComplete => shortfalls.isEmpty;
}

/// Builds a question paper that follows a [PaperBlueprint].
///
/// Questions are spread across the chosen chapters in turn, so a paper on
/// five chapters does not draw all its MCQs from one of them. A seeded
/// [Random] gives the same paper for the same seed, so a teacher can
/// recreate "Set A" or make a new set.
class PaperGenerator {
  const PaperGenerator._();

  static GeneratedPaper generate({
    required PaperBlueprint blueprint,
    required List<BankQuestion> pool,
    required Random random,
  }) {
    final usedIds = <String>{};
    final items = <AssessmentQuestion>[];
    final shortfalls = <SectionShortfall>[];

    for (final section in blueprint.sections) {
      final picked = _pickSpreadAcrossChapters(
        pool.where((q) => section.questionTypes.contains(q.type) && !usedIds.contains(q.id)).toList(),
        section.count,
        random,
      );
      usedIds.addAll(picked.map((q) => q.id));

      if (picked.length < section.count) {
        shortfalls.add(SectionShortfall(section.name, section.count, picked.length));
      }
      if (picked.isEmpty) continue;

      items.add(AssessmentQuestion(
        moduleId: 'header',
        type: 'section_header',
        question: 'SECTION ${section.name}: ${section.title} '
            '(${picked.length} × ${section.marksEach} = ${picked.length * section.marksEach} marks)',
        options: const [],
        correctIndexOrAnswer: '',
        marks: 0,
        section: section.name,
      ));
      items.addAll(picked.map((q) => AssessmentQuestion.fromBankQuestion(q.data, q.moduleId)
          .copyWith(marks: section.marksEach, section: section.name)));
    }

    return GeneratedPaper(blueprint: blueprint, items: items, shortfalls: shortfalls);
  }

  static List<BankQuestion> _pickSpreadAcrossChapters(List<BankQuestion> candidates, int count, Random random) {
    final byChapter = <String, List<BankQuestion>>{};
    for (final q in candidates) {
      byChapter.putIfAbsent(q.moduleId, () => []).add(q);
    }
    final queues = byChapter.values.map((list) => list..shuffle(random)).toList()..shuffle(random);

    final picked = <BankQuestion>[];
    while (picked.length < count && queues.any((q) => q.isNotEmpty)) {
      for (final queue in queues) {
        if (queue.isNotEmpty && picked.length < count) picked.add(queue.removeLast());
      }
    }
    return picked;
  }
}
