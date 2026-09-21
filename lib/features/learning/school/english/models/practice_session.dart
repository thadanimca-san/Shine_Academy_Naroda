import 'dart:math';

import 'practice_question.dart';

const int practiceSetSize = 10;

/// Pulls fresh sets of [practiceSetSize] questions from a topic's bank,
/// tracking which questions have already been served in this session so
/// "Practice More" doesn't repeat a question until the whole bank has been
/// used once. Once exhausted, it reshuffles and starts over.
class PracticeSession {
  final PracticeTopic topic;
  final Random _random;
  final List<int> _unseenIndexes;

  PracticeSession(this.topic, {Random? random})
      : _random = random ?? Random(),
        _unseenIndexes = List<int>.generate(topic.bank.length, (i) => i)..shuffle(random ?? Random());

  int get remainingInBank => _unseenIndexes.length;
  int get bankSize => topic.bank.length;

  /// Pulls the next set of questions. Reshuffles from the full bank once
  /// exhausted, so practice never truly runs out.
  List<PracticeQuestion> nextSet() {
    if (_unseenIndexes.isEmpty) {
      _unseenIndexes.addAll(List<int>.generate(topic.bank.length, (i) => i));
      _unseenIndexes.shuffle(_random);
    }
    final take = min(practiceSetSize, _unseenIndexes.length);
    final chosen = _unseenIndexes.sublist(0, take);
    _unseenIndexes.removeRange(0, take);
    return chosen.map((i) => topic.bank[i]).toList(growable: false);
  }
}
