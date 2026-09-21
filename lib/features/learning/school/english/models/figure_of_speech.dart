/// One example sentence showing a figure of speech in use, with Hindi help
/// explaining exactly what is being compared/exaggerated/imitated so a
/// student can see the mechanism, not just the label.
class FigureExample {
  final String sentence;
  final String explanationEn;
  final String explanationHi;
  final String hiTransliteration;

  const FigureExample({
    required this.sentence,
    required this.explanationEn,
    required this.explanationHi,
    required this.hiTransliteration,
  });
}

/// One figure of speech (Simile, Metaphor, Personification, ...), taught
/// with a plain-English definition, an emoji, and worked examples —
/// mirrors the sister Chapters/Dictionary content depth.
///
/// [level] marks which grade band the figure is taught at. This app uses a
/// single 'Class 7-10' tier throughout.
class FigureOfSpeech {
  final String id;
  final String name;
  final String emoji;
  final String level;
  final String definitionEn;
  final String definitionHi;
  final String hiTransliteration;
  final String recognitionTip; // how to spot it in a sentence
  final List<FigureExample> examples;

  const FigureOfSpeech({
    required this.id,
    required this.name,
    required this.emoji,
    this.level = 'Class 7-10',
    required this.definitionEn,
    required this.definitionHi,
    required this.hiTransliteration,
    required this.recognitionTip,
    required this.examples,
  });
}
