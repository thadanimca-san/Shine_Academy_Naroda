enum Difficulty { easy, medium, hard }

/// One multiple-choice practice question. Every question carries its own
/// explanation so an answer is never just marked right/wrong — the student
/// always sees why.
class PracticeQuestion {
  final String prompt;
  final String? promptHi;
  final String? promptGu;
  final String? emoji;
  final List<String> options;
  final List<String>? optionsHi;
  final List<String>? optionsGu;
  final int correctIndex;
  final String explanation;
  final String? explanationHi;
  final String? explanationGu;
  final Difficulty difficulty;

  const PracticeQuestion({
    required this.prompt,
    this.promptHi,
    this.promptGu,
    this.emoji,
    required this.options,
    this.optionsHi,
    this.optionsGu,
    required this.correctIndex,
    required this.explanation,
    this.explanationHi,
    this.explanationGu,
    this.difficulty = Difficulty.medium,
  });

  String get correctAnswer => options[correctIndex];

  Map<String, dynamic> toJson() => {
        'prompt': prompt,
        if (promptHi != null) 'prompt_hi': promptHi,
        if (promptGu != null) 'prompt_gu': promptGu,
        if (emoji != null) 'emoji': emoji,
        'options': options,
        if (optionsHi != null) 'options_hi': optionsHi,
        if (optionsGu != null) 'options_gu': optionsGu,
        'correct_index': correctIndex,
        'explanation': explanation,
        if (explanationHi != null) 'explanation_hi': explanationHi,
        if (explanationGu != null) 'explanation_gu': explanationGu,
        'difficulty': difficulty.name,
      };

  factory PracticeQuestion.fromJson(Map<String, dynamic> j) {
    final diffStr = j['difficulty'] as String? ?? 'medium';
    final diff = Difficulty.values.firstWhere(
      (d) => d.name == diffStr,
      orElse: () => Difficulty.medium,
    );
    return PracticeQuestion(
      prompt: j['prompt'] ?? '',
      promptHi: j['prompt_hi'],
      promptGu: j['prompt_gu'],
      emoji: j['emoji'],
      options: List<String>.from(j['options'] ?? []),
      optionsHi: j['options_hi'] != null
          ? List<String>.from(j['options_hi'])
          : null,
      optionsGu: j['options_gu'] != null
          ? List<String>.from(j['options_gu'])
          : null,
      correctIndex: j['correct_index'] ?? 0,
      explanation: j['explanation'] ?? '',
      explanationHi: j['explanation_hi'],
      explanationGu: j['explanation_gu'],
      difficulty: diff,
    );
  }
}

/// A large bank of questions for one grammar/skill topic, e.g. "Nouns" or
/// "Prepositions". The bank is meant to be big (100+ questions) and served
/// to students in small sets rather than all at once.
class PracticeTopic {
  final String id;
  final String title;
  final String grade;
  final String skill; // e.g. "Grammar", "Reading"
  final List<PracticeQuestion> bank;

  const PracticeTopic({
    required this.id,
    required this.title,
    required this.grade,
    required this.skill,
    required this.bank,
  });

  Map<String, dynamic> toJson() => {
        'id': id,
        'title': title,
        'grade': grade,
        'skill': skill,
        'bank': bank.map((q) => q.toJson()).toList(),
      };

  factory PracticeTopic.fromJson(Map<String, dynamic> j) => PracticeTopic(
        id: j['id'] ?? '',
        title: j['title'] ?? '',
        grade: j['grade'] ?? '',
        skill: j['skill'] ?? '',
        bank: (j['bank'] as List<dynamic>? ?? [])
            .map((q) => PracticeQuestion.fromJson(q as Map<String, dynamic>))
            .toList(),
      );
}

