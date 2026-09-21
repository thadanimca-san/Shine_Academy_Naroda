import 'block_registry.dart';
import 'block_validator.dart';

import '../../features/learning/learning_engine/widgets/flashcard_widget.dart';
import '../../features/learning/learning_engine/widgets/teacher_tip_widget.dart';
import '../../features/learning/learning_engine/widgets/dictionary_link_widget.dart';
import '../../features/learning/learning_engine/widgets/cross_subject_link_widget.dart';
import '../../features/learning/learning_engine/widgets/theory_widget.dart';
import '../../features/learning/learning_engine/widgets/trilingual_card_widget.dart';
import '../../features/learning/learning_engine/widgets/example_widget.dart';
import '../../features/learning/learning_engine/widgets/media_widget.dart';
import '../../features/learning/learning_engine/widgets/activity_widget.dart';
import '../../features/learning/learning_engine/widgets/quiz_widget.dart';
import '../../features/learning/learning_engine/widgets/nursery_rhyme_widget.dart';
import '../../features/learning/learning_engine/widgets/trace_alphabet_widget.dart';
import '../../features/learning/learning_engine/widgets/counting_game_widget.dart';
import '../../features/learning/learning_engine/widgets/color_canvas_widget.dart';
import '../../features/learning/learning_engine/widgets/presentation_widget.dart';
import '../../features/learning/learning_engine/widgets/animated_diagram_widget.dart';
import '../../features/learning/learning_engine/widgets/dialogue_widget.dart';
import '../../features/learning/learning_engine/widgets/worked_example_widget.dart';
import '../../features/learning/learning_engine/widgets/phonics_blender_widget.dart';
import '../../features/learning/learning_engine/widgets/abacus_simulation_widget.dart';

// Pedagogy Arc Widgets
import '../../features/learning/learning_engine/widgets/hook_widget.dart';
import '../../features/learning/learning_engine/widgets/socratic_widget.dart';
import '../../features/learning/learning_engine/widgets/discovery_widget.dart';
import '../../features/learning/learning_engine/widgets/reflection_widget.dart';
import '../../features/learning/learning_engine/widgets/mastery_widget.dart';

void registerDefaultBlocks() {
  final registry = BlockRegistry.instance;

  // ─────────────────────────────────────────────────────────────────
  // THEORY-LIKE BLOCKS → TheoryWidget
  // All these types display rich text/body content.
  // Validator is intentionally soft (no crash on missing fields).
  // ─────────────────────────────────────────────────────────────────
  final theoryLikeTypes = [
    // Core content types
    'theory', 'formula', 'real_world_example', 'definition',
    'history', 'summary', 'memory_trick',
    // Remaining Gold Pedagogy types mapped to theory for now
    'reveal', 'connection', 'match_column',
    // Visual / media fallback types
    'simulation', 'project', 'diagram', 'image', 'visual',
    'animation', 'revision',
    // Knowledge / research types
    'etymology', 'timeline', 'mind_map', 'board_questions',
    'calculator', 'analogy',
  ];

  for (final type in theoryLikeTypes) {
    registry.register(
      BlockDefinition(
        type: type,
        validator: (block) {}, // Soft: accept any block, let widget handle gracefully
        builder: (block) => TheoryWidget(block: block, type: type),
      ),
    );
  }

  // ─────────────────────────────────────────────────────────────────
  // MCQ / KNOWLEDGE CHECK → QuizWidget
  // All question-answer types use the same quiz widget.
  // ─────────────────────────────────────────────────────────────────
  final quizLikeTypes = [
    'quiz', 'mcq', 'knowledge_check', 'true_false', 'quiz_multiple_choice',
    'practice_question', 'challenge_question',
  ];

  for (final type in quizLikeTypes) {
    registry.register(
      BlockDefinition(
        type: type,
        validator: (block) {}, // Soft: QuizWidget handles missing fields with fallbacks
        builder: (block) => QuizWidget(data: block),
      ),
    );
  }

  // ─────────────────────────────────────────────────────────────────
  // AI DISCUSSION / SOCRATIC → TeacherTipWidget
  // ─────────────────────────────────────────────────────────────────
  final aiTypes = ['ai_discussion', 'ai_tutor_prompt'];

  for (final type in aiTypes) {
    registry.register(
      BlockDefinition(
        type: type,
        validator: (block) {},
        builder: (block) => TeacherTipWidget(block: block),
      ),
    );
  }

  // ─────────────────────────────────────────────────────────────────
  // PEDAGOGY 8-STEP ARC WIDGETS
  // ─────────────────────────────────────────────────────────────────

  registry.register(BlockDefinition(
    type: 'hook',
    validator: (block) {},
    builder: (block) => HookWidget(block: block),
  ));

  registry.register(BlockDefinition(
    type: 'socratic_question',
    validator: (block) {},
    builder: (block) => SocraticWidget(block: block),
  ));

  registry.register(BlockDefinition(
    type: 'discovery',
    validator: (block) {},
    builder: (block) => DiscoveryWidget(block: block),
  ));

  registry.register(BlockDefinition(
    type: 'reflection',
    validator: (block) {},
    builder: (block) => ReflectionWidget(block: block),
  ));

  registry.register(BlockDefinition(
    type: 'mastery',
    validator: (block) {},
    builder: (block) => MasteryWidget(block: block),
  ));

  // ─────────────────────────────────────────────────────────────────
  // EXAMPLE
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'example',
      validator: (block) {},
      builder: (block) => ExampleWidget(data: block),
    ),
  );

  // CASE STUDY → ExampleWidget (structured content)
  registry.register(
    BlockDefinition(
      type: 'case_study',
      validator: (block) {},
      builder: (block) => ExampleWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // WORKED EXAMPLE
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'worked_example',
      validator: (block) {},
      builder: (block) => WorkedExampleWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // TRILINGUAL CARD
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'trilingual_card',
      validator: (block) {},
      builder: (block) => TrilingualCardWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // MEDIA
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'media',
      validator: (block) {},
      builder: (block) => MediaWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // ACTIVITY
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'activity',
      validator: (block) {},
      builder: (block) => ActivityWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // FLASHCARD
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'flashcard',
      validator: (block) {},
      builder: (block) => FlashcardWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // TEACHER TIP / COMMON MISTAKES / EXAM TIPS
  // ─────────────────────────────────────────────────────────────────
  final tipTypes = ['teacher_tip', 'common_mistakes', 'exam_tips'];

  for (final type in tipTypes) {
    registry.register(
      BlockDefinition(
        type: type,
        validator: (block) {},
        builder: (block) => TeacherTipWidget(block: block),
      ),
    );
  }

  // ─────────────────────────────────────────────────────────────────
  // DICTIONARY LINK
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'dictionary_link',
      validator: (block) {},
      builder: (block) => DictionaryLinkWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // NURSERY RHYME
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'nursery_rhyme',
      validator: (block) {},
      builder: (block) => NurseryRhymeWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // TRACE ALPHABET
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'trace_alphabet',
      validator: (block) => BlockValidationUtils.requireLegacy(block, 'letter', 'character', String),
      builder: (block) => TraceAlphabetWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // COUNTING GAME
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'counting_game',
      validator: (block) => BlockValidationUtils.require(block, 'target_number', int),
      builder: (block) => CountingGameWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // COLOR CANVAS
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'color_canvas',
      validator: (block) => BlockValidationUtils.requireLegacy(block, 'svg_path', 'shape', String),
      builder: (block) => ColorCanvasWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // PRESENTATION
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'presentation',
      validator: (block) {},
      builder: (block) => PresentationWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // ANIMATED DIAGRAM
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'animated_diagram',
      validator: (block) {},
      builder: (block) => AnimatedDiagramWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // DIALOGUE
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'dialogue',
      validator: (block) {},
      builder: (block) => DialogueWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // CROSS SUBJECT LINK
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'cross_subject_link',
      validator: (block) => BlockValidationUtils.require(block, 'target_chapter_id', String),
      builder: (block) => CrossSubjectLinkWidget(block: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // PHONICS BLENDER
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'phonics_blender',
      validator: (block) => BlockValidationUtils.require(block, 'parts', List),
      builder: (block) => PhonicsBlenderWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // ABACUS SIMULATION
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'abacus_simulation',
      validator: (block) {},
      builder: (block) => AbacusSimulationWidget(block: block),
    ),
  );
}
