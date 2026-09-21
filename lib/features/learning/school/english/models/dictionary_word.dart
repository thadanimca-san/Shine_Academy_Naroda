class DictionaryWord {
  final String word;
  final String partOfSpeech;
  final String? emoji;
  final String? imagePath;
  final String meaningEn;
  final String meaningHi;
  final String? meaningGu;
  final String hiTransliteration;
  final String? guTransliteration;
  final String exampleEn;
  final String? exampleHi;
  final String? exampleGu;
  final String category;

  const DictionaryWord({
    required this.word,
    required this.partOfSpeech,
    this.emoji,
    this.imagePath,
    required this.meaningEn,
    required this.meaningHi,
    this.meaningGu,
    required this.hiTransliteration,
    this.guTransliteration,
    required this.exampleEn,
    this.exampleHi,
    this.exampleGu,
    required this.category,
  });
}

class DictionaryTopic {
  final String id;
  final String title;
  final String grade;
  final List<DictionaryWord> words;
  final List<String>? wordIds;

  const DictionaryTopic({
    required this.id,
    required this.title,
    required this.grade,
    this.words = const [],
    this.wordIds,
  });

  List<String> get categories =>
      words.map((w) => w.category).toSet().toList(growable: false);
}
