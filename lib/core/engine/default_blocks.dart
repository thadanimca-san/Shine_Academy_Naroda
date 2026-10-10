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
import '../../features/learning/learning_engine/widgets/game_quiz_card.dart';
import '../../features/learning/learning_engine/widgets/inspiration_widget.dart';
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
import '../../features/learning/learning_engine/widgets/markdown_table_widget.dart';
import '../../features/learning/learning_engine/widgets/factor_tree_widget.dart';
import '../../features/learning/learning_engine/widgets/function_graph_widget.dart';

// Pedagogy Arc Widgets
import '../../features/learning/learning_engine/widgets/hook_widget.dart';
import '../../features/learning/learning_engine/widgets/socratic_widget.dart';
import '../../features/learning/learning_engine/widgets/discovery_widget.dart';
import '../../features/learning/learning_engine/widgets/reflection_widget.dart';
import '../../features/learning/learning_engine/widgets/mastery_widget.dart';
import '../../features/learning/learning_engine/widgets/heading_widget.dart';

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
    'history', 'summary', 'memory_trick', 'short_note',
    // Remaining Gold Pedagogy types mapped to theory for now
    'reveal', 'connection', 'match_column',
    // Visual / media fallback types
    'simulation', 'project', 'diagram', 'image', 'visual',
    'animation', 'revision',
    // Knowledge / research types
    'etymology', 'timeline', 'mind_map', 'board_questions',
    'calculator', 'analogy', 'knowledge_connection', 'story',
    'story_hook',
    // Fallback for AI-generated unregistered types
    'concept', 'vocabulary', 'task', 'confidence_task', 'practice_speaking',
    'practical', 'practice', 'translation_exercise', 'exercise', 'example_sentences',
    'paragraph', 'dictionary_term', 'examples', 'table', 'vocabulary_table', 'faqs'
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
  // MARKDOWN TABLE BLOCK → MarkdownTableWidget
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'markdown_table',
      validator: (block) {}, // Soft validator
      builder: (block) => MarkdownTableWidget(block: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // MCQ / KNOWLEDGE CHECK → QuizWidget
  // All question-answer types use the same quiz widget.
  // ─────────────────────────────────────────────────────────────────
  final quizLikeTypes = [
    'quiz', 'mcq', 'knowledge_check', 'true_false', 'quiz_multiple_choice',
    'practice_question', 'challenge_question', 'challenge', 'mastery_challenge',
    'quiz_mcq', 'quiz_question', 'numerical',
    // AI-generated unregistered types
    'subjective', 'fill_blank', 'question'
  ];

  for (final type in quizLikeTypes) {
    registry.register(
      BlockDefinition(
        type: type,
        validator: (block) {}, // Soft: QuizWidget handles missing fields with fallbacks
        // Questions with plain options are played as a game with per-option
        // explanations; older formats keep the classic quiz widget.
        builder: (block) => GameQuizBlock.canHandle(block) ? GameQuizBlock(block: block) : QuizWidget(data: block),
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

  final socraticTypes = ['socratic', 'socratic_question', 'socratic_thinking', 'question_socratic'];
  for (final type in socraticTypes) {
    registry.register(BlockDefinition(
      type: type,
      validator: (block) {},
      builder: (block) => SocraticWidget(block: block),
    ));
  }

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
  final activityTypes = ['activity', 'interactive_activity'];
  for (final type in activityTypes) {
    registry.register(
      BlockDefinition(
        type: type,
        validator: (block) {},
        builder: (block) => ActivityWidget(data: block),
      ),
    );
  }

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
  final tipTypes = ['teacher_tip', 'common_mistakes', 'exam_tips', 'teacher_tp', 'tip'];

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
  // HEADING
  // ─────────────────────────────────────────────────────────────────
  final headingTypes = ['heading', 'chapter_title'];
  for (final type in headingTypes) {
    registry.register(
      BlockDefinition(
        type: type,
        validator: (block) => BlockValidationUtils.require(block, 'title', String),
        builder: (block) => HeadingWidget(data: block),
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
  // FACTOR TREE (animated prime factorisation)
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'factor_tree',
      validator: (block) => BlockValidationUtils.require(block, 'number', int),
      builder: (block) => FactorTreeWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // FUNCTION GRAPH (animated polynomial plot with zeroes)
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'function_graph',
      validator: (block) => BlockValidationUtils.require(block, 'polynomial', List),
      builder: (block) => FunctionGraphWidget(data: block),
    ),
  );

  // ─────────────────────────────────────────────────────────────────
  // INSPIRATION (true story + where the topic leads)
  // ─────────────────────────────────────────────────────────────────
  registry.register(
    BlockDefinition(
      type: 'inspiration',
      validator: (block) {},
      builder: (block) => InspirationWidget(data: block),
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
