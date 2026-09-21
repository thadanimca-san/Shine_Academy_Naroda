enum Difficulty { easy, medium, hard }

/// One step in a worked solution, optionally paired with a diagram. Maths
/// needs a full worked explanation, not a one-line reason like a grammar
/// question does — a wrong answer should let a student see exactly where
/// their own working diverged.
class SolutionStep {
  final String text;
  final String? emoji; // stands in for a diagram/illustration until real art exists

  const SolutionStep({required this.text, this.emoji});
}

/// One multiple-choice maths question with a full worked solution.
class MathQuestion {
  final String prompt;
  final String? emoji; // a visual for the question itself, e.g. a shape or diagram
  final List<String> options;
  final int correctIndex;
  final List<SolutionStep> solutionSteps;
  final Difficulty difficulty;

  const MathQuestion({
    required this.prompt,
    this.emoji,
    required this.options,
    required this.correctIndex,
    required this.solutionSteps,
    this.difficulty = Difficulty.medium,
  });

  String get correctAnswer => options[correctIndex];
}

/// A large bank of questions for one maths topic, e.g. "Addition" or
/// "Fractions". Mirrors english3to6's PracticeTopic: big bank, served to
/// students in small sets rather than all at once.
class MathTopic {
  final String id;
  final String title;
  final String grade;
  final List<MathQuestion> bank;

  const MathTopic({
    required this.id,
    required this.title,
    required this.grade,
    required this.bank,
  });
}
