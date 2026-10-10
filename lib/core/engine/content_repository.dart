import 'package:flutter/foundation.dart';
import 'local_content_manager.dart';
import 'paper_generator.dart';

/// One chapter listed in `app_core/content/index.json`.
class ContentIndexEntry {
  final String id;
  final String path;
  final String board;
  final int classNumber;
  final String subject;
  final int chapterNumber;
  final String title;

  /// Older module ids (e.g. `ncert_class10_maths_ch1`) that now resolve here,
  /// so existing curriculum files and routes keep working unchanged.
  final List<String> aliases;

  const ContentIndexEntry({
    required this.id,
    required this.path,
    required this.board,
    required this.classNumber,
    required this.subject,
    required this.chapterNumber,
    required this.title,
    required this.aliases,
  });

  factory ContentIndexEntry.fromJson(Map<String, dynamic> json) => ContentIndexEntry(
        id: json['id'] as String,
        path: json['path'] as String,
        board: json['board'] as String,
        classNumber: json['class'] as int,
        subject: json['subject'] as String,
        chapterNumber: json['chapter_number'] as int,
        title: json['title'] as String,
        aliases: List<String>.from(json['aliases'] ?? const []),
      );

  String get chapterFile => '$path/chapter.json';
  String get questionsFile => '$path/questions.json';
}

/// A chapter from the new content format, flattened for the block renderer.
class ChapterContent {
  final ContentIndexEntry entry;
  final Map<String, dynamic> metadata;

  /// Section headings followed by their blocks, in reading order.
  final List<Map<String, dynamic>> blocks;

  const ChapterContent({required this.entry, required this.metadata, required this.blocks});

  String get status => metadata['status'] as String? ?? 'draft';
}

/// Single entry point for content stored in the new format under
/// `app_core/content/` (see docs/CONTENT_FORMAT_DESIGN.md).
///
/// Callers try this first and fall back to the legacy locations when it
/// returns null, so chapters move over one at a time without breaking anything.
class ContentRepository {
  ContentRepository._();
  static final ContentRepository instance = ContentRepository._();

  static const String indexPath = 'app_core/content/index.json';

  /// Only teacher-approved content reaches students. Debug and profile builds
  /// also show draft and reviewed content so it can be checked before approval.
  static bool get showUnapprovedContent => !kReleaseMode;

  Future<List<ContentIndexEntry>>? _indexFuture;

  Future<List<ContentIndexEntry>> get index => _indexFuture ??= _loadIndex();

  /// Forgets the loaded index so it is read again (after content edits, and in tests).
  void clearCache() => _indexFuture = null;

  Future<List<ContentIndexEntry>> _loadIndex() async {
    try {
      final data = await LocalContentManager.instance.readLocalJson(indexPath);
      if (data is! Map || data['chapters'] is! List) return const [];
      return (data['chapters'] as List)
          .cast<Map<String, dynamic>>()
          .map(ContentIndexEntry.fromJson)
          .toList(growable: false);
    } catch (e) {
      debugPrint('ContentRepository: could not read $indexPath: $e');
      return const [];
    }
  }

  /// Finds a chapter by its id or by any of its legacy aliases.
  Future<ContentIndexEntry?> findChapter(String idOrAlias) async {
    for (final entry in await index) {
      if (entry.id == idOrAlias || entry.aliases.contains(idOrAlias)) return entry;
    }
    return null;
  }

  Future<List<ContentIndexEntry>> chaptersFor({
    required String board,
    required int classNumber,
    required String subject,
  }) async {
    final matches = (await index)
        .where((e) => e.board == board && e.classNumber == classNumber && e.subject == subject)
        .toList()
      ..sort((a, b) => a.chapterNumber.compareTo(b.chapterNumber));
    return matches;
  }

  /// Returns null when the chapter is not in the new format yet, or is not
  /// approved in a release build. The caller then uses the legacy content.
  Future<ChapterContent?> loadChapter(String idOrAlias) async {
    final entry = await findChapter(idOrAlias);
    if (entry == null) return null;

    final data = await LocalContentManager.instance.readLocalJson(entry.chapterFile);
    if (data is! Map<String, dynamic>) {
      debugPrint('ContentRepository: ${entry.chapterFile} is missing or invalid.');
      return null;
    }

    final metadata = Map<String, dynamic>.from(data)..remove('sections');
    if (!_isVisible(metadata['status'] as String?)) return null;

    final blocks = <Map<String, dynamic>>[];
    for (final section in (data['sections'] as List? ?? const []).cast<Map<String, dynamic>>()) {
      final sectionTitle = section['title'] as String?;
      if (sectionTitle != null && sectionTitle.isNotEmpty) {
        blocks.add({'id': '${section['id']}.heading', 'type': 'heading', 'title': sectionTitle});
      }
      blocks.addAll((section['blocks'] as List? ?? const []).cast<Map<String, dynamic>>());
    }
    return ChapterContent(entry: entry, metadata: metadata, blocks: blocks);
  }

  /// The chapter's question bank, or null if it has none in the new format.
  /// Unapproved questions are left out of release builds.
  Future<List<Map<String, dynamic>>?> loadQuestions(String idOrAlias) async {
    final entry = await findChapter(idOrAlias);
    if (entry == null) return null;

    final data = await LocalContentManager.instance.readLocalJson(entry.questionsFile);
    if (data is! Map || data['questions'] is! List) {
      debugPrint('ContentRepository: ${entry.questionsFile} is missing or invalid.');
      return null;
    }
    return (data['questions'] as List)
        .cast<Map<String, dynamic>>()
        .where((q) => _isVisible(q['status'] as String?))
        .toList();
  }

  /// The board paper pattern for a curriculum subject (e.g. `cbse_class10_math`),
  /// or null if none is defined yet.
  Future<PaperBlueprint?> blueprintForSubject(String subjectId) async {
    try {
      final data = await LocalContentManager.instance.readLocalJson(indexPath);
      for (final entry in (data?['paper_blueprints'] as List? ?? const []).cast<Map<String, dynamic>>()) {
        if ((entry['subject_ids'] as List).contains(subjectId)) {
          final blueprint = await LocalContentManager.instance.readLocalJson(entry['path'] as String);
          return PaperBlueprint.fromJson(blueprint as Map<String, dynamic>);
        }
      }
    } catch (e) {
      debugPrint('ContentRepository: could not load paper blueprint for $subjectId: $e');
    }
    return null;
  }

  bool _isVisible(String? status) => status == 'approved' || showUnapprovedContent;
}
