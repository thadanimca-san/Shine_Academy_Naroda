/// One maths term in the concept glossary — the maths equivalent of the
/// sister English app's picture dictionary. [emoji] stands in for a real
/// diagram/illustration until dedicated art exists.
class Concept {
  final String term;
  final String emoji;
  final String meaningEn;
  final String meaningHi;
  final String hiTransliteration;
  final String exampleEn;
  final String category;

  const Concept({
    required this.term,
    required this.emoji,
    required this.meaningEn,
    required this.meaningHi,
    required this.hiTransliteration,
    required this.exampleEn,
    required this.category,
  });
}

/// A themed collection of concept-glossary terms for one grade.
class ConceptTopic {
  final String id;
  final String title;
  final String grade;
  final List<Concept> concepts;

  const ConceptTopic({
    required this.id,
    required this.title,
    required this.grade,
    required this.concepts,
  });

  List<String> get categories => concepts.map((c) => c.category).toSet().toList(growable: false);
}
