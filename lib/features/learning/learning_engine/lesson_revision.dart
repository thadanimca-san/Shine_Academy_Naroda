/// Quick Revision: the short version of a chapter for students who are
/// revising, built from the same blocks as the full lesson.

/// Block types that always belong in Quick Revision.
const Set<String> revisionBlockTypes = {
  'summary', 'formula', 'memory_trick', 'exam_tips', 'common_mistakes', 'flashcard', 'mind_map', 'revision',
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
  return result;
}

bool hasRevisionContent(List<dynamic> blocks) => blocks.cast<Map<String, dynamic>>().any(isRevisionBlock);
