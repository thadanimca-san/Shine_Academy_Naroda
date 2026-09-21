/// One difficult word glossed inline within a chapter's text, with its
/// Hindi meaning available right at the point it occurs — not a separate
/// dictionary lookup.
class InlineGloss {
  final String word; // must match the word's exact casing as it appears in chapterText
  final String meaningHi;
  final String hiTransliteration;
  final String? meaningGu;
  final String? guTransliteration;

  const InlineGloss({
    required this.word,
    required this.meaningHi,
    required this.hiTransliteration,
    this.meaningGu,
    this.guTransliteration,
  });

  Map<String, dynamic> toJson() => {
        'word': word,
        'meaning_hi': meaningHi,
        'hi_transliteration': hiTransliteration,
        if (meaningGu != null) 'meaning_gu': meaningGu,
        if (guTransliteration != null) 'gu_transliteration': guTransliteration,
      };

  factory InlineGloss.fromJson(Map<String, dynamic> j) => InlineGloss(
        word: j['word'] ?? '',
        meaningHi: j['meaning_hi'] ?? '',
        hiTransliteration: j['hi_transliteration'] ?? '',
        meaningGu: j['meaning_gu'],
        guTransliteration: j['gu_transliteration'],
      );
}

/// A textbook-style chapter: the English chapter text, a short Hindi summary
/// of what it's about, and inline glosses for its difficult words.
///
/// Draft status: chapter text here is originally written to match the style
/// and difficulty of a typical GSEB/CBSE English-medium Class 7-10 reader,
/// not copied from an actual textbook — swap in real chapter text once
/// available, keeping the same gloss/summary structure.
class Chapter {
  final String id;
  final String title;
  final String grade;
  final String emoji;
  final String chapterText;
  final String? hindiText;
  final String? gujaratiText;
  final String hindiSummary;
  final String? gujaratiSummary;
  final List<InlineGloss> glosses;

  const Chapter({
    required this.id,
    required this.title,
    required this.grade,
    required this.emoji,
    required this.chapterText,
    this.hindiText,
    this.gujaratiText,
    required this.hindiSummary,
    this.gujaratiSummary,
    this.glosses = const [],
  });

  Map<String, dynamic> toJson() => {
        'id': id,
        'title': title,
        'grade': grade,
        'emoji': emoji,
        'chapter_text': chapterText,
        if (hindiText != null) 'hindi_text': hindiText,
        if (gujaratiText != null) 'gujarati_text': gujaratiText,
        'hindi_summary': hindiSummary,
        if (gujaratiSummary != null) 'gujarati_summary': gujaratiSummary,
        'glosses': glosses.map((g) => g.toJson()).toList(),
      };

  factory Chapter.fromJson(Map<String, dynamic> j) => Chapter(
        id: j['id'] ?? '',
        title: j['title'] ?? '',
        grade: j['grade'] ?? '',
        emoji: j['emoji'] ?? '📖',
        chapterText: j['chapter_text'] ?? '',
        hindiText: j['hindi_text'],
        gujaratiText: j['gujarati_text'],
        hindiSummary: j['hindi_summary'] ?? '',
        gujaratiSummary: j['gujarati_summary'],
        glosses: (j['glosses'] as List<dynamic>? ?? [])
            .map((g) => InlineGloss.fromJson(g as Map<String, dynamic>))
            .toList(),
      );
}
