import 'dart:math';
import 'dart:convert';
import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'curriculum_database.dart';
import 'content_repository.dart';
import 'paper_generator.dart';

class CurriculumChapter {
  final String id;
  final String title;
  final String moduleId;

  CurriculumChapter({
    required this.id,
    required this.title,
    required this.moduleId,
  });
}

class CurriculumSubject {
  final String id;
  final String title;
  final List<CurriculumChapter> chapters;

  CurriculumSubject({
    required this.id,
    required this.title,
    required this.chapters,
  });
}

class AssessmentQuestion {
  final String moduleId;
  final String type; // 'quiz', 'fill_blank', 'short_note', 'true_false'
  final String question; // English text
  final String? questionHi; // Hindi text
  final String? questionGu; // Gujarati text
  final String? paragraph; // English paragraph/comprehension text
  final String? paragraphHi; // Hindi paragraph/comprehension text
  final String? paragraphGu; // Gujarati paragraph/comprehension text
  final List<String> options; // English options
  final List<String>? optionsHi; // Hindi options
  final List<String>? optionsGu; // Gujarati options
  final dynamic
  correctIndexOrAnswer; // int for quiz, string for fill_blank/short_note
  final String? explanationEn;
  final String? explanationHi;
  final String? explanationGu;
  final String? distractorRationaleEn;
  final String? distractorRationaleHi;
  final String? distractorRationaleGu;
  final String? bloomTaxonomy;
  final String? aiHint;
  final int marks;
  final String? section;

  /// Optional block (e.g. a `function_graph`) drawn below the question text.
  final Map<String, dynamic>? figure;

  /// One explanation per option: why that choice is right or wrong.
  final List<String>? optionFeedback;
  final List<String>? optionFeedbackHi;
  final List<String>? optionFeedbackGu;

  AssessmentQuestion({
    required this.moduleId,
    required this.type,
    required this.question,
    this.questionHi,
    this.questionGu,
    this.paragraph,
    this.paragraphHi,
    this.paragraphGu,
    required this.options,
    this.optionsHi,
    this.optionsGu,
    required this.correctIndexOrAnswer,
    this.explanationEn,
    this.explanationHi,
    this.explanationGu,
    this.distractorRationaleEn,
    this.distractorRationaleHi,
    this.distractorRationaleGu,
    this.bloomTaxonomy,
    this.aiHint,
    this.marks = 1,
    this.section,
    this.figure,
    this.optionFeedback,
    this.optionFeedbackHi,
    this.optionFeedbackGu,
  });

  /// Question types in the new question bank that have options to choose from.
  static const Set<String> objectiveBankTypes = {'mcq', 'assertion_reason', 'true_false'};

  /// Converts a question from a new-format `questions.json`
  /// (see docs/CONTENT_FORMAT_DESIGN.md) into the model the practice and
  /// paper screens use. Objective questions become `quiz`; written ones become
  /// `descriptive` with the model answer as the expected answer.
  factory AssessmentQuestion.fromBankQuestion(Map<String, dynamic> q, String moduleId) {
    final type = q['type'] as String? ?? '';
    final marks = (q['marks'] as num?)?.toInt() ?? 1;
    final markingScheme = (q['marking_scheme'] as List?)?.join('\n');

    List<String>? list(String key) => (q[key] as List?)?.cast<String>();

    if (objectiveBankTypes.contains(type)) {
      return AssessmentQuestion(
        moduleId: moduleId,
        type: 'quiz',
        question: q['question'] as String? ?? '',
        questionHi: q['question_hi'] as String?,
        questionGu: q['question_gu'] as String?,
        options: List<String>.from(q['options'] ?? const []),
        optionsHi: list('options_hi'),
        optionsGu: list('options_gu'),
        correctIndexOrAnswer: q['correct_index'] ?? 0,
        explanationEn: q['explanation'] as String?,
        explanationHi: q['explanation_hi'] as String?,
        explanationGu: q['explanation_gu'] as String?,
        marks: marks,
        figure: q['figure'] as Map<String, dynamic>?,
        optionFeedback: list('option_feedback'),
        optionFeedbackHi: list('option_feedback_hi'),
        optionFeedbackGu: list('option_feedback_gu'),
      );
    }

    final steps = (q['answer_steps'] as List?)?.join('\n');
    return AssessmentQuestion(
      moduleId: moduleId,
      type: 'descriptive',
      question: q['question'] as String? ?? '',
      questionHi: q['question_hi'] as String?,
      questionGu: q['question_gu'] as String?,
      options: const [],
      correctIndexOrAnswer: steps ?? q['answer'] ?? '',
      explanationEn: markingScheme,
      explanationHi: (q['marking_scheme_hi'] as List?)?.join('\n'),
      explanationGu: (q['marking_scheme_gu'] as List?)?.join('\n'),
      marks: marks,
      figure: q['figure'] as Map<String, dynamic>?,
    );
  }

  AssessmentQuestion copyWith({
    String? moduleId,
    String? type,
    String? question,
    String? questionHi,
    String? questionGu,
    String? paragraph,
    String? paragraphHi,
    String? paragraphGu,
    List<String>? options,
    List<String>? optionsHi,
    List<String>? optionsGu,
    dynamic correctIndexOrAnswer,
    String? explanationEn,
    String? explanationHi,
    String? explanationGu,
    String? distractorRationaleEn,
    String? distractorRationaleHi,
    String? distractorRationaleGu,
    String? bloomTaxonomy,
    String? aiHint,
    int? marks,
    String? section,
    Map<String, dynamic>? figure,
    List<String>? optionFeedback,
    List<String>? optionFeedbackHi,
    List<String>? optionFeedbackGu,
  }) {
    return AssessmentQuestion(
      moduleId: moduleId ?? this.moduleId,
      type: type ?? this.type,
      question: question ?? this.question,
      questionHi: questionHi ?? this.questionHi,
      questionGu: questionGu ?? this.questionGu,
      paragraph: paragraph ?? this.paragraph,
      paragraphHi: paragraphHi ?? this.paragraphHi,
      paragraphGu: paragraphGu ?? this.paragraphGu,
      options: options ?? this.options,
      optionsHi: optionsHi ?? this.optionsHi,
      optionsGu: optionsGu ?? this.optionsGu,
      correctIndexOrAnswer: correctIndexOrAnswer ?? this.correctIndexOrAnswer,
      explanationEn: explanationEn ?? this.explanationEn,
      explanationHi: explanationHi ?? this.explanationHi,
      explanationGu: explanationGu ?? this.explanationGu,
      distractorRationaleEn: distractorRationaleEn ?? this.distractorRationaleEn,
      distractorRationaleHi: distractorRationaleHi ?? this.distractorRationaleHi,
      distractorRationaleGu: distractorRationaleGu ?? this.distractorRationaleGu,
      bloomTaxonomy: bloomTaxonomy ?? this.bloomTaxonomy,
      aiHint: aiHint ?? this.aiHint,
      marks: marks ?? this.marks,
      section: section ?? this.section,
      figure: figure ?? this.figure,
      optionFeedback: optionFeedback ?? this.optionFeedback,
      optionFeedbackHi: optionFeedbackHi ?? this.optionFeedbackHi,
      optionFeedbackGu: optionFeedbackGu ?? this.optionFeedbackGu,
    );
  }
}

class AssessmentEngine {
  static final AssessmentEngine instance = AssessmentEngine._internal();
  AssessmentEngine._internal();

  /// Parses the curriculum JSON to return available subjects and chapters
  Future<List<CurriculumSubject>> fetchCurriculumSubjects(
    String curriculumId,
  ) async {
    List<CurriculumSubject> subjects = [];
    try {
      final String jsonString = await rootBundle.loadString(
        'app_core/curriculum/$curriculumId.json',
      );
      final Map<String, dynamic> curriculumData = json.decode(jsonString);

      if (curriculumData['subjects'] != null) {
        for (var subjectData in curriculumData['subjects']) {
          List<CurriculumChapter> chapters = [];
          if (subjectData['chapters'] != null) {
            for (var chapterData in subjectData['chapters']) {
              if (chapterData['module_id'] != null) {
                chapters.add(
                  CurriculumChapter(
                    id: chapterData['chapter_id'] ?? 'unknown',
                    title: chapterData['title'] ?? 'Unnamed Chapter',
                    moduleId: chapterData['module_id'],
                  ),
                );
              }
            }
          }
          subjects.add(
            CurriculumSubject(
              id: subjectData['id'] ?? subjectData['subject_id'] ?? 'unknown',
              title:
                  subjectData['name'] ??
                  subjectData['title'] ??
                  'Unnamed Subject',
              chapters: chapters,
            ),
          );
        }
      }
    } catch (e) {
      debugPrint("Error loading curriculum subjects: $e");
    }
    return subjects;
  }

  /// Extracts specific question types from specific modules
  Future<List<AssessmentQuestion>> generateCustomPaper({
    required List<String> targetModuleIds,
    required List<String> allowedQuestionTypes,
    required int totalQuestions,
  }) async {
    List<AssessmentQuestion> allQuestions = [];

    for (String moduleId in targetModuleIds) {
      final questions = await extractQuestionsForModule(
        moduleId,
        allowedQuestionTypes,
      );
      allQuestions.addAll(questions);
    }

    allQuestions.shuffle();
    return allQuestions.take(totalQuestions).toList();
  }

  /// Builds a paper following the board blueprint for [subjectId] from the
  /// new-format question banks of [moduleIds]. Returns null when the subject
  /// has no blueprint, so callers can use the older pattern instead.
  Future<GeneratedPaper?> generateFromBlueprint(List<String> moduleIds, String subjectId, {Random? random}) async {
    final blueprint = await ContentRepository.instance.blueprintForSubject(subjectId);
    if (blueprint == null) return null;

    final pool = <BankQuestion>[];
    for (final moduleId in moduleIds) {
      final questions = await ContentRepository.instance.loadQuestions(moduleId);
      pool.addAll((questions ?? const []).map((q) => BankQuestion(moduleId, q)));
    }
    return PaperGenerator.generate(blueprint: blueprint, pool: pool, random: random ?? Random());
  }

  /// Generates a structured 10th Standard Board Pattern Paper
  Future<List<AssessmentQuestion>> generateBoardPatternPaper(
    List<String> targetModuleIds, {
    int targetSecA = 16,
    int targetSecB = 8,
    int targetSecC = 6,
    int targetSecD = 5,
  }) async {
    try {
      List<AssessmentQuestion> allObjectives = []; // 1 mark
      List<AssessmentQuestion> allSubjectives = []; // multi-mark

    for (String moduleId in targetModuleIds) {
      // Fetch all questions from the module
      final questions = await extractQuestionsForModule(moduleId, [
        'quiz',
        'true_false',
        'fill_blank',
        'short_note',
        'long_answer',
        'descriptive',
      ]);

      for (var q in questions) {
        if (q.type == 'quiz' ||
            q.type == 'true_false' ||
            q.type == 'fill_blank') {
          allObjectives.add(q);
        } else {
          allSubjectives.add(q);
        }
      }
    }

    allObjectives.shuffle();
    allSubjectives.shuffle();

    List<AssessmentQuestion> paper = [];

    // SECTION A: 1 Mark (Objectives)
    int secACount = allObjectives.length > targetSecA ? targetSecA : allObjectives.length;
    if (secACount > 0) {
      paper.add(
        AssessmentQuestion(
          moduleId: 'header',
          type: 'section_header',
          question: 'SECTION A - Objective (1 Mark each)',
          options: [],
          correctIndexOrAnswer: '',
          section: 'A',
        ),
      );
      paper.addAll(
        allObjectives
            .take(secACount)
            .map(
              (q) => q.copyWith(
                marks: 1,
                section: 'A',
              ),
            ),
      );
    }

    // Since we don't have deep taxonomy data yet, we distribute the available subjective questions
    // randomly among Sections B (2m), C (3m), and D (4/5m).
    int remainingSubj = allSubjectives.length;

    // SECTION B: 2 Marks (Very Short Answer)
    int secBCount = remainingSubj > targetSecB
        ? targetSecB
        : (remainingSubj > 2 ? (remainingSubj ~/ 3) : remainingSubj);
    if (secBCount > 0) {
      paper.add(
        AssessmentQuestion(
          moduleId: 'header',
          type: 'section_header',
          question: 'SECTION B - Very Short Answer (2 Marks each)',
          options: [],
          correctIndexOrAnswer: '',
          section: 'B',
        ),
      );
      paper.addAll(
        allSubjectives
            .take(secBCount)
            .map(
              (q) => q.copyWith(
                marks: 2,
                section: 'B',
              ),
            ),
      );
      allSubjectives.removeRange(0, secBCount);
      remainingSubj = allSubjectives.length;
    }

    // SECTION C: 3 Marks (Short Answer)
    int secCCount = remainingSubj > targetSecC
        ? targetSecC
        : (remainingSubj > 1 ? (remainingSubj ~/ 2) : remainingSubj);
    if (secCCount > 0) {
      paper.add(
        AssessmentQuestion(
          moduleId: 'header',
          type: 'section_header',
          question: 'SECTION C - Short Answer (3 Marks each)',
          options: [],
          correctIndexOrAnswer: '',
          section: 'C',
        ),
      );
      paper.addAll(
        allSubjectives
            .take(secCCount)
            .map(
              (q) => q.copyWith(
                marks: 3,
                section: 'C',
              ),
            ),
      );
      allSubjectives.removeRange(0, secCCount);
      remainingSubj = allSubjectives.length;
    }

    // SECTION D: 4/5 Marks (Long Answer)
    int secDCount = remainingSubj > targetSecD ? targetSecD : remainingSubj;
    if (secDCount > 0) {
      paper.add(
        AssessmentQuestion(
          moduleId: 'header',
          type: 'section_header',
          question: 'SECTION D - Long Answer (4 Marks each)',
          options: [],
          correctIndexOrAnswer: '',
          section: 'D',
        ),
      );
      paper.addAll(
        allSubjectives
            .take(secDCount)
            .map(
              (q) => q.copyWith(
                marks: 4,
                section: 'D',
              ),
            ),
      );
    }

    return paper;
    } catch (e, stackTrace) {
      debugPrint('Error generating board pattern paper: $e');
      debugPrint(stackTrace.toString());
      return [];
    }
  }

  /// Loads a single module's blocks.json and extracts allowed blocks
  Future<List<AssessmentQuestion>> extractQuestionsForModule(
    String moduleId,
    List<String> allowedTypes,
  ) async {
    List<AssessmentQuestion> questions = [];
    try {
      // New-format question bank takes priority over questions found in blocks.
      final bankQuestions = await ContentRepository.instance.loadQuestions(moduleId);
      if (bankQuestions != null && bankQuestions.isNotEmpty) {
        return bankQuestions
            .map((q) => AssessmentQuestion.fromBankQuestion(q, moduleId))
            .where((q) => allowedTypes.contains(q.type) ||
                (q.type == 'descriptive' && allowedTypes.contains('short_note')))
            .toList();
      }

      List<dynamic>? rawBlocks;
      
      // 1. Try local file system for newly generated chapters
      try {
        final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/$moduleId.json');
        if (file.existsSync()) {
          final data = json.decode(file.readAsStringSync());
          if (data is Map && data['blocks'] != null) {
            rawBlocks = data['blocks'];
          } else if (data is List) {
            rawBlocks = data;
          }
        }
      } catch (_) {}

      // 2. Try root bundle for bundled chapters
      if (rawBlocks == null) {
        try {
          final jsonString = await rootBundle.loadString('app_core/chapters/$moduleId.json');
          final data = json.decode(jsonString);
          if (data is Map && data['blocks'] != null) {
            rawBlocks = data['blocks'];
          } else if (data is List) {
            rawBlocks = data;
          }
        } catch (_) {}
      }
      
      // 3. Fallback to master curriculum
      if (rawBlocks == null) {
        rawBlocks = CurriculumDatabase.instance.getModuleBlocks(moduleId);
      }

      if (rawBlocks != null) {
        for (var block in rawBlocks) {
          String originalType = block['type'] ?? '';

          final contentMap = block['content'] != null
              ? block['content']
              : block;

          bool hasOptions = contentMap['options'] != null && (contentMap['options'] as List).isNotEmpty;

          String blockType = originalType;
          if (originalType == 'knowledge_check' || originalType == 'mcq' || originalType == 'socratic') {
            blockType = 'quiz';
          } else if (originalType == 'practice_question' || originalType == 'challenge_question') {
            if (hasOptions) {
              blockType = 'quiz';
            } else {
              blockType = 'descriptive';
            }
          } else if (originalType == 'flashcard') {
            blockType = 'short_note';
          }

          // If the mapped type is in allowedTypes or the original type is
          if (allowedTypes.contains(blockType) || allowedTypes.contains(originalType)) {
            // Extract options based on block type
            List<String> options = [];
            if (blockType == 'quiz' && contentMap['options'] != null) {
              options = List<String>.from(contentMap['options']);
            }

            // Extract correct answer
            dynamic correctAns;
            if (blockType == 'quiz') {
              if (contentMap['correct_index'] != null) {
                correctAns = contentMap['correct_index'];
              } else if (contentMap['correct_answer'] != null) {
                // If answer is provided as a string, find its index in the options array
                final ansStr = contentMap['correct_answer'].toString();
                int idx = options.indexOf(ansStr);
                correctAns = idx != -1 ? idx : 0;
              } else {
                correctAns = 0;
              }
            } else if (blockType == 'fill_blank') {
              correctAns = contentMap['answer'] ?? '';
            }

            int parsedMarks = 1;
            if (contentMap['marks'] != null) {
              parsedMarks = int.tryParse(contentMap['marks'].toString()) ?? 1;
            }

            questions.add(
              AssessmentQuestion(
                moduleId: moduleId,
                type: blockType,
                question:
                    contentMap['question_en'] ??
                    contentMap['question_text'] ??
                    contentMap['question'] ??
                    contentMap['front'] ??
                    contentMap['body'] ??
                    'Missing Question',
                questionHi:
                    contentMap['question_hi'] ??
                    contentMap['question_text_hi'] ??
                    contentMap['front_hi'] ??
                    contentMap['body_hi'],
                questionGu:
                    contentMap['question_gu'] ??
                    contentMap['question_text_gu'] ??
                    contentMap['front_gu'] ??
                    contentMap['body_gu'],
                paragraph: contentMap['paragraph'],
                paragraphHi: contentMap['paragraph_hi'],
                paragraphGu: contentMap['paragraph_gu'],
                options: options,
                optionsHi: contentMap['options_hi'] != null
                    ? List<String>.from(contentMap['options_hi'])
                    : null,
                optionsGu: contentMap['options_gu'] != null
                    ? List<String>.from(contentMap['options_gu'])
                    : null,
                correctIndexOrAnswer: (blockType == 'short_note' || blockType == 'descriptive' || blockType == 'practice_question' || blockType == 'challenge_question')
                    ? (contentMap['answer_en'] ?? contentMap['answer'] ?? contentMap['back'])
                    : correctAns,
                explanationEn: contentMap['explanation_en'] ?? contentMap['explanation'] ?? contentMap['solution'] ?? contentMap['answer_description'],
                explanationHi: contentMap['explanation_hi'] ?? contentMap['solution_hi'],
                explanationGu: contentMap['explanation_gu'] ?? contentMap['solution_gu'],
                marks: parsedMarks,
              ),
            );
          }
        }
      }
    } catch (e) {
      debugPrint("Error extracting questions for module $moduleId: $e");
    }
    return questions;
  }
}
