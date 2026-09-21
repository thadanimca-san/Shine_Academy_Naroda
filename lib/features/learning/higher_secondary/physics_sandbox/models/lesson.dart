import 'package:flutter/widgets.dart';

/// Content models for data-driven lessons.
///
/// Lessons are pure data (text, formulas, questions) plus one injected
/// sandbox widget. Keeping content out of widgets is what will later let
/// lessons live in Supabase without rewriting screens.

enum BlockKind { paragraph, bullets, formula, realLife, mistake, jeeTip, neetNote, example }

class ContentBlock {
  final BlockKind kind;
  final String? title;
  final String? text;
  final List<String> items;

  const ContentBlock.paragraph(this.text, {this.title})
      : kind = BlockKind.paragraph,
        items = const [];
  const ContentBlock.bullets(this.items, {this.title})
      : kind = BlockKind.bullets,
        text = null;
  const ContentBlock.formula(this.text, {this.title})
      : kind = BlockKind.formula,
        items = const [];
  const ContentBlock._(this.kind, {this.title, this.text, this.items = const []});

  const factory ContentBlock.realLife(String text, {String? title}) = _RealLife;
  const factory ContentBlock.mistake(String text, {String? title}) = _Mistake;
  const factory ContentBlock.jeeTip(String text, {String? title}) = _JeeTip;
  const factory ContentBlock.neetNote(String text, {String? title}) = _NeetNote;
  const factory ContentBlock.example(String text, {String? title}) = _Example;
}

class _RealLife extends ContentBlock {
  const _RealLife(String text, {super.title}) : super._(BlockKind.realLife, text: text);
}

class _Mistake extends ContentBlock {
  const _Mistake(String text, {super.title}) : super._(BlockKind.mistake, text: text);
}

class _JeeTip extends ContentBlock {
  const _JeeTip(String text, {super.title}) : super._(BlockKind.jeeTip, text: text);
}

class _NeetNote extends ContentBlock {
  const _NeetNote(String text, {super.title}) : super._(BlockKind.neetNote, text: text);
}

class _Example extends ContentBlock {
  const _Example(String text, {super.title}) : super._(BlockKind.example, text: text);
}

/// The commit-before-you-see prompt shown before the sandbox opens.
class PredictionPrompt {
  final String scenario;
  final List<String> options;
  final int correctIndex;
  final String reveal; // shown after the student experiments

  const PredictionPrompt({
    required this.scenario,
    required this.options,
    required this.correctIndex,
    required this.reveal,
  });
}

class DerivationStep {
  final String title;
  final String math;
  final String? note;
  const DerivationStep({required this.title, required this.math, this.note});
}

enum ExamTrack { neet, jee, both }

enum Difficulty { basic, exam, advanced }

class PracticeQuestion {
  final ExamTrack track;
  final Difficulty difficulty;
  final String question;
  final List<String> options;
  final int correctIndex;
  final String solution;

  const PracticeQuestion({
    required this.track,
    required this.difficulty,
    required this.question,
    required this.options,
    required this.correctIndex,
    required this.solution,
  });
}

class FormulaEntry {
  final String label;
  final String expression;
  final String? condition;
  const FormulaEntry(this.label, this.expression, {this.condition});
}

class Lesson {
  final String topicId;
  final String title;

  /// The curiosity hook — a question a student genuinely wonders about.
  final String bigQuestion;
  final String whyItMatters;

  final PredictionPrompt prediction;

  /// Things to actively try in the sandbox (guided observation).
  final List<String> experiments;

  final List<ContentBlock> concept;
  final List<DerivationStep> derivation;
  final List<FormulaEntry> formulas;
  final List<PracticeQuestion> questions;
  final List<String> revision;

  /// The interactive sandbox injected into the Lab stage. Nullable — lessons
  /// without a sandbox simply skip that stage.
  final WidgetBuilder? sandboxBuilder;

  /// Chapter accent for the lesson's top nav (falls back to the app primary).
  final Color? accentColor;

  const Lesson({
    required this.topicId,
    required this.title,
    required this.bigQuestion,
    required this.whyItMatters,
    required this.prediction,
    required this.experiments,
    required this.concept,
    required this.derivation,
    required this.formulas,
    required this.questions,
    required this.revision,
    this.sandboxBuilder,
    this.accentColor,
  });
}
