import 'practice_question.dart' show Difficulty;
// Re-export Difficulty so data files that previously imported it via this file
// continue to work unchanged.
export 'practice_question.dart' show Difficulty;


/// A picture-description writing prompt.
class WritingPrompt {
  final String id;
  final String title;
  final String sceneEmoji;
  final String sceneDescription;
  final List<String> wordBank;
  final String modelAnswer;
  final List<String> modelAnswerHighlights;
  final Difficulty difficulty;

  const WritingPrompt({
    required this.id,
    required this.title,
    required this.sceneEmoji,
    required this.sceneDescription,
    required this.wordBank,
    required this.modelAnswer,
    required this.modelAnswerHighlights,
    this.difficulty = Difficulty.medium,
  });

  Map<String, dynamic> toJson() => {
        'id': id,
        'title': title,
        'scene_emoji': sceneEmoji,
        'scene_description': sceneDescription,
        'word_bank': wordBank,
        'model_answer': modelAnswer,
        'model_answer_highlights': modelAnswerHighlights,
        'difficulty': difficulty.name,
      };

  factory WritingPrompt.fromJson(Map<String, dynamic> j) {
    final diffStr = j['difficulty'] as String? ?? 'medium';
    final diff = Difficulty.values.firstWhere(
      (d) => d.name == diffStr,
      orElse: () => Difficulty.medium,
    );
    return WritingPrompt(
      id: j['id'] ?? '',
      title: j['title'] ?? '',
      sceneEmoji: j['scene_emoji'] ?? '🖼️',
      sceneDescription: j['scene_description'] ?? '',
      wordBank: List<String>.from(j['word_bank'] ?? []),
      modelAnswer: j['model_answer'] ?? '',
      modelAnswerHighlights:
          List<String>.from(j['model_answer_highlights'] ?? []),
      difficulty: diff,
    );
  }
}

/// A themed collection of writing prompts for one grade.
class WritingLibrary {
  final String id;
  final String title;
  final String grade;
  final List<WritingPrompt> prompts;

  const WritingLibrary({
    required this.id,
    required this.title,
    required this.grade,
    required this.prompts,
  });
}
