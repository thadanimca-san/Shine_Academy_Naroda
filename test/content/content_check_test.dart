// Content checker for the new content format (docs/CONTENT_FORMAT_DESIGN.md).
//
// Run before every release and after every content change:
//   flutter test test/content/content_check_test.dart
//
// For a release build, also refuse anything a teacher has not approved:
//   RELEASE_CHECK=1 flutter test test/content/content_check_test.dart
import 'dart:convert';
import 'dart:io';

import 'package:flutter_math_fork/flutter_math.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/core/engine/block_registry.dart';
import 'package:shine_academy_naroda/core/engine/default_blocks.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/widgets/geometry_figure_widget.dart';

const contentRoot = 'app_core/content';
const statuses = {'draft', 'reviewed', 'approved'};

/// Board-paper marks for each question type (CBSE pattern).
const marksByQuestionType = {
  'mcq': 1,
  'assertion_reason': 1,
  'true_false': 1,
  'fill_blank': 1,
  'very_short_answer': 2,
  'short_answer': 3,
  'long_answer': 5,
  'case_based': 4,
};

/// Subjects whose board paper weights a type differently. English (184) asks
/// 5-mark extracts and 6-mark long answers.
const marksOverridesBySubject = {
  'english_literature': {'case_based': 5, 'long_answer': 6},
};

int? marksFor(String subject, Object? type) => marksOverridesBySubject[subject]?[type] ?? marksByQuestionType[type];

const objectiveTypes = {'mcq', 'assertion_reason', 'true_false'};
const sourceKinds = {'ncert_exercise', 'ncert_intext', 'ncert_example', 'ncert_theorem', 'pyq', 'sample_paper', 'shine'};

/// Block types that ask a question with options and must carry a valid answer.
const optionBlockTypes = {'mcq', 'quiz', 'knowledge_check', 'socratic_question', 'true_false'};

Map<String, dynamic> readJson(String path) => json.decode(File(path).readAsStringSync()) as Map<String, dynamic>;

/// Collects every problem instead of stopping at the first, so one run shows
/// the whole list to fix.
class Problems {
  final List<String> _items = [];
  void add(String where, String what) => _items.add('$where: $what');
  void expectAll() => expect(_items, isEmpty, reason: '\n${_items.join('\n')}\n');
}

/// Visits every string inside [value] with a readable path to it.
void forEachString(Object? value, String path, void Function(String text, String path) visit) {
  if (value is String) {
    visit(value, path);
  } else if (value is List) {
    for (var i = 0; i < value.length; i++) {
      forEachString(value[i], '$path[$i]', visit);
    }
  } else if (value is Map) {
    value.forEach((key, child) => forEachString(child, '$path.$key', visit));
  }
}

final _formula = RegExp(r'\$\$([\s\S]+?)\$\$|\$([^$]+?)\$');
final _damagedEscape = RegExp('[\t\f\b\r]');

/// Checks that every `$...$` and `$$...$$` formula in [text] renders.
void checkFormulas(String text, String where, Problems problems) {
  final dollarCount = RegExp(r'(?<!\\)\$').allMatches(text).length;
  if (dollarCount.isOdd) {
    problems.add(where, 'unbalanced \$ (a formula is not closed)');
    return;
  }
  for (final match in _formula.allMatches(text)) {
    final tex = match.group(1) ?? match.group(2)!;
    if (_damagedEscape.hasMatch(tex)) {
      problems.add(where, 'formula "$tex" has a broken backslash (write \\\\ in JSON)');
      continue;
    }
    if (RegExp('[\u0900-\u0AFF]').hasMatch(tex)) {
      problems.add(where, 'formula "$tex" contains Hindi/Gujarati letters; keep words outside \$...\$');
      continue;
    }
    final error = Math.tex(tex).parseError;
    if (error != null) problems.add(where, 'formula "$tex" does not render: ${error.message}');
  }
}

/// Figures and graph blocks must be registered blocks, and every zero marked
/// on a graph must really be a zero of its polynomial.
void checkVisual(Map<String, dynamic> block, String where, Problems problems) {
  final type = block['type'];
  if (type is! String || !BlockRegistry.instance.hasBlock(type)) {
    problems.add(where, 'figure type "$type" is not registered in default_blocks.dart');
  }
  if (type == 'function_graph') {
    double eval(List coefficients, double x) => coefficients.fold(0.0, (v, c) => v * x + (c as num).toDouble());
    final curves = block['curves'] is List
        ? (block['curves'] as List).map((c) => (c as Map)['polynomial'] as List).toList()
        : [block['polynomial'] as List? ?? const []];
    for (final zero in (block['zeroes'] as List? ?? const []).map((z) => (z as num).toDouble())) {
      final value = eval(curves.first, zero);
      if (value.abs() > 1e-9) problems.add(where, 'graph marks $zero as a zero, but p($zero) = $value');
    }
    // Each marked point must lie on the curves it names in "on" (e.g. both lines for an intersection).
    for (final point in (block['points'] as List? ?? const []).cast<Map<String, dynamic>>()) {
      final x = (point['x'] as num).toDouble(), y = (point['y'] as num).toDouble();
      for (final index in (point['on'] as List? ?? const []).cast<int>()) {
        if (index >= curves.length || (eval(curves[index], x) - y).abs() > 1e-9) {
          problems.add(where, 'point (${point['x']}, ${point['y']}) is not on curve $index');
        }
      }
    }
  }
  if (type == 'geometry_figure') checkGeometry(block, where, problems);
}

/// A figure must show what it claims: every named point exists, and segments
/// marked parallel or at right angles really are, so the picture never misleads.
void checkGeometry(Map<String, dynamic> block, String where, Problems problems) {
  final points = geometryPoints(block);
  bool known(Iterable<String> names) {
    final missing = names.where((n) => !points.containsKey(n)).toList();
    if (missing.isNotEmpty) problems.add(where, 'figure uses unknown points $missing');
    return missing.isEmpty;
  }

  for (final s in geometrySegments(block)) {
    known([s.from, s.to]);
  }
  for (final group in (block['parallel'] as List? ?? const []).map((g) => (g as List).cast<String>())) {
    if (!known(group) || group.length < 4 || group.length.isOdd) continue;
    for (var k = 2; k + 1 < group.length; k += 2) {
      if (!segmentsParallel(points[group[0]]!, points[group[1]]!, points[group[k]]!, points[group[k + 1]]!)) {
        problems.add(where, '${group[0]}${group[1]} is marked parallel to ${group[k]}${group[k + 1]} but is not');
      }
    }
  }
  for (final r in (block['right_angles'] as List? ?? const []).map((g) => (g as List).cast<String>())) {
    if (known(r) && !isRightAngle(points[r[0]]!, points[r[1]]!, points[r[2]]!)) {
      problems.add(where, 'angle ${r.join()} is marked 90° but is not');
    }
  }
  for (final a in (block['angles'] as List? ?? const []).cast<Map>()) {
    known((a['points'] as List).cast<String>());
  }
  for (final c in geometryCircles(block)) {
    if (!known([c.centre, ...c.through])) continue;
    for (final name in c.through) {
      final distance = (points[name]! - points[c.centre]!).distance;
      if ((distance - c.radius).abs() > 1e-6 * c.radius) {
        problems.add(where, '$name is marked on the circle with centre ${c.centre} but is $distance from it, not ${c.radius}');
      }
    }
  }
  for (final r in geometryRegions(block)) {
    if (!known([r.centre, r.from, r.to])) continue;
    if (!const {'sector', 'segment', 'arc'}.contains(r.kind)) problems.add(where, 'shaded region kind must be sector, segment or arc, not ${r.kind}');
    final ra = (points[r.from]! - points[r.centre]!).distance, rb = (points[r.to]! - points[r.centre]!).distance;
    if ((ra - rb).abs() > 1e-6 * ra) problems.add(where, 'shaded ${r.kind} ${r.from}${r.to}: the two points are not the same distance from ${r.centre}');
  }
}

void checkOptions(Map<String, dynamic> item, String where, Problems problems, {bool needsFeedback = true}) {
  final options = item['options'];
  final correct = item['correct_index'];
  if (options is! List || options.length < 2) {
    problems.add(where, 'needs at least 2 options');
    return;
  } else if (correct is! int || correct < 0 || correct >= options.length) {
    problems.add(where, 'correct_index must be a whole number from 0 to ${options.length - 1}');
  }
  if (!needsFeedback) return;
  // Game-style quizzes teach through one explanation per option.
  for (final key in ['option_feedback', 'option_feedback_hi', 'option_feedback_gu']) {
    final feedback = item[key];
    if (feedback == null && key != 'option_feedback') continue;
    if (feedback is! List || feedback.length != options.length || feedback.any((f) => f is! String || f.trim().isEmpty)) {
      problems.add(where, '$key needs one explanation for each of the ${options.length} options');
    }
  }
}

const translatableTextFields = {
  'title', 'body', 'question', 'explanation', 'problem', 'given', 'formula', 'answer', 'front', 'back',
  'person', 'quote', 'future', 'feedback_incorrect', 'statement',
};
const translatableListFields = {'options', 'option_feedback', 'steps', 'answer_steps', 'marking_scheme'};

int formulaCount(String text) => _formula.allMatches(text).length;

/// For every language the chapter promises, each translatable field needs a
/// translation, lists must keep their length, and formulas must not be lost.
void checkTranslations(Map<String, dynamic> item, List<String> languages, String where, Problems problems) {
  for (final lang in languages.where((l) => l != 'en')) {
    for (final field in translatableTextFields) {
      final english = item[field];
      if (english is! String || english.trim().isEmpty) continue;
      final translated = item['${field}_$lang'];
      if (translated is! String || translated.trim().isEmpty) {
        problems.add(where, 'missing ${field}_$lang');
      } else if (formulaCount(translated) != formulaCount(english)) {
        problems.add(where, '${field}_$lang has ${formulaCount(translated)} formulas, English has ${formulaCount(english)}');
      }
    }
    for (final field in translatableListFields) {
      final english = item[field];
      if (english is! List || english.isEmpty) continue;
      final translated = item['${field}_$lang'];
      if (translated is! List || translated.length != english.length) {
        problems.add(where, '${field}_$lang must have ${english.length} entries');
        continue;
      }
      for (var i = 0; i < english.length; i++) {
        if (english[i] is String && formulaCount(translated[i] as String) != formulaCount(english[i] as String)) {
          problems.add(where, '${field}_$lang[$i] lost or added a formula');
        }
      }
    }
  }
}

void checkChapter(Map<String, dynamic> entry, Problems problems) {
  final file = '${entry['path']}/chapter.json';
  final chapter = readJson(file);

  for (final field in ['schema_version', 'id', 'title', 'book', 'board', 'class', 'subject', 'chapter_number', 'status']) {
    if (chapter[field] == null) problems.add(file, 'missing "$field"');
  }
  if (chapter['id'] != entry['id']) problems.add(file, 'id "${chapter['id']}" does not match the index "${entry['id']}"');
  if (!statuses.contains(chapter['status'])) problems.add(file, 'status must be one of $statuses');

  final languages = List<String>.from(chapter['languages'] ?? const ['en']);
  checkTranslations(chapter, languages, '$file#metadata', problems);

  final ids = <String>{};
  final sections = chapter['sections'] as List? ?? const [];
  if (sections.isEmpty) problems.add(file, 'has no sections');

  for (final section in sections.cast<Map<String, dynamic>>()) {
    final sectionId = section['id'];
    if (sectionId is! String || !ids.add(sectionId)) problems.add(file, 'section id "$sectionId" is missing or repeated');
    checkTranslations(section, languages, '$file#$sectionId', problems);
    for (final block in (section['blocks'] as List? ?? const []).cast<Map<String, dynamic>>()) {
      final id = block['id'];
      final where = '$file#$id';
      if (id is! String || !ids.add(id)) problems.add(where, 'block id is missing or repeated');
      final type = block['type'];
      if (type is! String || !BlockRegistry.instance.hasBlock(type)) {
        problems.add(where, 'block type "$type" is not registered in default_blocks.dart');
      }
      // Socratic questions are for thinking, not marking; they explain once.
      if (optionBlockTypes.contains(type)) checkOptions(block, where, problems, needsFeedback: type != 'socratic_question');
      if (type == 'function_graph' || type == 'geometry_figure') checkVisual(block, where, problems);
      checkTranslations(block, languages, where, problems);
      final image = block['image_url'];
      if (image is String && !File(image).existsSync()) problems.add(where, 'image $image not found');
      if (block.containsKey('content') && block['content'] is Map) {
        problems.add(where, 'fields must be at the top level, not inside "content"');
      }
    }
  }
  forEachString(chapter, file, (text, path) => checkFormulas(text, path, problems));
}

void checkQuestions(Map<String, dynamic> entry, Problems problems) {
  final file = '${entry['path']}/questions.json';
  final bank = readJson(file);
  if (bank['chapter_id'] != entry['id']) problems.add(file, 'chapter_id must be "${entry['id']}"');

  final languages = List<String>.from(readJson('${entry['path']}/chapter.json')['languages'] ?? const ['en']);
  final ids = <String>{};
  for (final q in (bank['questions'] as List? ?? const []).cast<Map<String, dynamic>>()) {
    final id = q['id'];
    final where = '$file#$id';
    checkTranslations(q, languages, where, problems);
    if (id is! String || !ids.add(id)) problems.add(where, 'question id is missing or repeated');

    final type = q['type'];
    final marks = marksFor(entry['subject'] as String? ?? '', type);
    if (marks == null) {
      problems.add(where, 'unknown type "$type"');
    } else if (q['marks'] != marks) {
      problems.add(where, '"$type" questions carry $marks marks, not ${q['marks']}');
    }
    if ((q['question'] as String? ?? '').trim().isEmpty) problems.add(where, 'question text is empty');
    if (!statuses.contains(q['status'])) problems.add(where, 'status must be one of $statuses');
    if ((q['concepts'] as List? ?? const []).isEmpty) problems.add(where, 'list at least one concept');

    final source = q['source'];
    if (source is! Map || !sourceKinds.contains(source['kind'])) {
      problems.add(where, 'source.kind must be one of $sourceKinds');
    } else if (source['kind'] == 'ncert_exercise' && (source['exercise'] == null || source['question'] == null)) {
      problems.add(where, 'NCERT exercise questions need source.exercise and source.question');
    }

    if (q['figure'] is Map<String, dynamic>) checkVisual(q['figure'] as Map<String, dynamic>, where, problems);
    if (objectiveTypes.contains(type)) {
      checkOptions(q, where, problems);
      if ((q['explanation'] as String? ?? '').trim().isEmpty) problems.add(where, 'needs an explanation');
    } else if ((q['answer_steps'] as List? ?? const []).isEmpty) {
      problems.add(where, 'written questions need answer_steps (the model answer)');
    }
    if (!objectiveTypes.contains(type) && type != 'fill_blank' && (q['marking_scheme'] as List? ?? const []).isEmpty) {
      problems.add(where, 'needs a marking_scheme');
    }
  }
  forEachString(bank, file, (text, path) => checkFormulas(text, path, problems));
}

void checkBlueprint(File file, Problems problems) {
  final blueprint = readJson(file.path);
  var total = 0;
  for (final section in (blueprint['sections'] as List? ?? const []).cast<Map<String, dynamic>>()) {
    final types = (section['types'] as List? ?? const []).cast<String>();
    for (final type in types) {
      if (marksByQuestionType[type] != section['marks_each']) {
        problems.add(file.path, 'section ${section['name']}: "$type" is not a ${section['marks_each']}-mark type');
      }
    }
    total += (section['count'] as int) * (section['marks_each'] as int);
  }
  if (total != blueprint['total_marks']) {
    problems.add(file.path, 'sections add up to $total marks, but total_marks is ${blueprint['total_marks']}');
  }
}

void main() {
  setUpAll(registerDefaultBlocks);

  final index = readJson('$contentRoot/index.json');
  final entries = (index['chapters'] as List).cast<Map<String, dynamic>>();
  final pubspec = File('pubspec.yaml').readAsStringSync();

  test('index lists each chapter once and every chapter is bundled', () {
    final problems = Problems();
    final ids = <String>{};
    final aliases = <String>{};
    for (final entry in entries) {
      final id = entry['id'];
      if (!ids.add(id)) problems.add('index.json', 'chapter "$id" listed twice');
      for (final alias in (entry['aliases'] as List? ?? const []).cast<String>()) {
        if (!aliases.add(alias)) problems.add('index.json', 'alias "$alias" used by two chapters');
      }
      for (final file in ['chapter.json', 'questions.json']) {
        if (!File('${entry['path']}/$file').existsSync()) problems.add('index.json', '$id: ${entry['path']}/$file not found');
      }
      if (!pubspec.contains('    - ${entry['path']}/\n')) {
        problems.add('pubspec.yaml', 'add "- ${entry['path']}/" under assets, or the app cannot load $id');
      }
    }
    problems.expectAll();
  });

  for (final entry in entries) {
    group(entry['id'], () {
      test('chapter.json', () {
        final problems = Problems();
        checkChapter(entry, problems);
        problems.expectAll();
      });
      test('questions.json', () {
        final problems = Problems();
        checkQuestions(entry, problems);
        problems.expectAll();
      });
    });
  }

  test('paper blueprints add up', () {
    final problems = Problems();
    final dir = Directory('$contentRoot/paper_blueprints');
    if (dir.existsSync()) {
      for (final file in dir.listSync().whereType<File>().where((f) => f.path.endsWith('.json'))) {
        checkBlueprint(file, problems);
      }
    }
    problems.expectAll();
  });

  test('release builds contain only approved content', () {
    if (Platform.environment['RELEASE_CHECK'] != '1') {
      markTestSkipped('Set RELEASE_CHECK=1 to enforce before a release build.');
      return;
    }
    final problems = Problems();
    for (final entry in entries) {
      final chapter = readJson('${entry['path']}/chapter.json');
      if (chapter['status'] != 'approved') problems.add(entry['id'], 'chapter is "${chapter['status']}", not approved');
    }
    problems.expectAll();
  });
}
