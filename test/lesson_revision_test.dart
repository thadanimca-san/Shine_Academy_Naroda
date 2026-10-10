import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/lesson_revision.dart';

void main() {
  test('keeps summary-type and marked blocks under their headings', () {
    final blocks = [
      {'id': 'h1', 'type': 'heading', 'title': 'Intro'},
      {'id': 'hook', 'type': 'hook'},
      {'id': 'h2', 'type': 'heading', 'title': 'Theorem'},
      {'id': 'theory', 'type': 'theory', 'revision': true},
      {'id': 'quiz', 'type': 'knowledge_check'},
      {'id': 'h3', 'type': 'heading', 'title': 'End'},
      {'id': 'sum', 'type': 'summary'},
      {'id': 'card', 'type': 'flashcard'},
    ];
    expect(revisionBlocks(blocks).map((b) => b['id']), ['h2', 'theory', 'h3', 'sum', 'card']);
    expect(hasRevisionContent(blocks), isTrue);
    expect(hasRevisionContent([{'id': 'x', 'type': 'hook'}]), isFalse);
  });
}
