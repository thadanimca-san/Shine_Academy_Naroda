library;

/// Quick Revision: the short version of a chapter for students who are
/// revising, built from the same blocks as the full lesson.

/// Block types that always belong in Quick Revision.
const Set<String> revisionBlockTypes = {
  'summary', 'formula', 'memory_trick', 'exam_tips', 'common_mistakes', 'flashcard', 'mind_map', 'revision',
  'rule_card', 'sentence_puzzle', 'pronunciation_drill', 'vocabulary', 'key_points',
};

bool isRevisionBlock(Map<String, dynamic> block) =>
    revisionBlockTypes.contains(block['type']) || block['revision'] == true;

/// The revision blocks of [blocks], each under its section heading. Headings
/// whose section has no revision blocks are left out.
List<dynamic> revisionBlocks(List<dynamic> blocks) {
  final result = <dynamic>[];
  Map<String, dynamic>? pendingHeading;
  for (final block in blocks.cast<Map<String, dynamic>>()) {
    if (block['type'] == 'heading') {
      pendingHeading = block;
    } else if (isRevisionBlock(block)) {
      if (pendingHeading != null) {
        result.add(pendingHeading);
        pendingHeading = null;
      }
      result.add(block);
    }
  }

  // If no explicit revision blocks matched, extract core high-yield blocks
  if (result.isEmpty && blocks.isNotEmpty) {
    for (final block in blocks.cast<Map<String, dynamic>>()) {
      final t = block['type'];
      if (t == 'dialogue' || t == 'example' || t == 'teacher_tip' || t == 'mcq' || t == 'quiz') {
        result.add(block);
      }
    }
    // Final fallback: first 5 blocks so revision mode is never empty
    if (result.isEmpty) {
      result.addAll(blocks.take(5));
    }
  }

  return result;
}

bool hasRevisionContent(List<dynamic> blocks) => blocks.isNotEmpty;
