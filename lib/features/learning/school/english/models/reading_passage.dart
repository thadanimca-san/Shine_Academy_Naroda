import 'chapter.dart' show InlineGloss;
import 'practice_question.dart';

/// A short illustrated reading passage with comprehension questions.
class ReadingPassage {
  final String id;
  final String title;
  final String emoji;
  final String grade;
  final Difficulty difficulty;
  final String body;
  final String? bodyHi;
  final String? bodyGu;
  final List<PracticeQuestion> questions;
  final List<InlineGloss> glosses;

  const ReadingPassage({
    required this.id,
    required this.title,
    required this.emoji,
    required this.grade,
    required this.difficulty,
    required this.body,
    this.bodyHi,
    this.bodyGu,
    required this.questions,
    this.glosses = const [],
  });

  Map<String, dynamic> toJson() => {
        'id': id,
        'title': title,
        'emoji': emoji,
        'grade': grade,
        'difficulty': difficulty.name,
        'body': body,
        if (bodyHi != null) 'body_hi': bodyHi,
        if (bodyGu != null) 'body_gu': bodyGu,
        'questions': questions.map((q) => q.toJson()).toList(),
        'glosses': glosses.map((g) => g.toJson()).toList(),
      };

  factory ReadingPassage.fromJson(Map<String, dynamic> j) {
    final diffStr = j['difficulty'] as String? ?? 'medium';
    final diff = Difficulty.values.firstWhere(
      (d) => d.name == diffStr,
      orElse: () => Difficulty.medium,
    );
    return ReadingPassage(
      id: j['id'] ?? '',
      title: j['title'] ?? '',
      emoji: j['emoji'] ?? '📖',
      grade: j['grade'] ?? '',
      difficulty: diff,
      body: j['body'] ?? '',
      bodyHi: j['body_hi'],
      bodyGu: j['body_gu'],
      questions: (j['questions'] as List<dynamic>? ?? [])
          .map((q) => PracticeQuestion.fromJson(q as Map<String, dynamic>))
          .toList(),
      glosses: (j['glosses'] as List<dynamic>? ?? [])
          .map((g) => InlineGloss.fromJson(g as Map<String, dynamic>))
          .toList(),
    );
  }
}

/// A themed collection of reading passages for one grade.
class ReadingLibrary {
  final String id;
  final String title;
  final String grade;
  final List<ReadingPassage> passages;

  const ReadingLibrary({
    required this.id,
    required this.title,
    required this.grade,
    required this.passages,
  });
}
