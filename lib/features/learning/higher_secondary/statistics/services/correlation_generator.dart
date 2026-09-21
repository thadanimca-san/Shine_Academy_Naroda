import 'dart:math';

import '../models/board_model.dart';
import '../models/correlation_model.dart';
import 'correlation_solver.dart';

/// Generates randomized Correlation problems: a set of paired (X, Y)
/// observations with a controlled relationship strength/direction so
/// the resulting coefficient is meaningfully interpretable, not just
/// noise. Difficulty scales pair count (more pairs -> more arithmetic).
class CorrelationGenerator {
  CorrelationGenerator._();

  static final Random _rand = Random();

  static GeneratedCorrelationProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    final pairCount = 5 + (difficulty - 1); // 5-9 pairs
    final positiveDirection = _rand.nextBool();
    // A moderate/strong linear relationship with some noise, so the
    // coefficient isn't trivially exactly +-1 (too easy to guess) nor
    // near-zero (uninterpretable for a "state the correlation" question).
    final slopeMagnitude = 1.5 + _rand.nextDouble() * 2;
    final noiseSpread = 3 + _rand.nextInt(5);

    final pairs = List.generate(pairCount, (i) {
      final x = (10 + i * 5 + _rand.nextInt(5)).toDouble();
      final trendY = 20 + (positiveDirection ? 1 : -1) * slopeMagnitude * (x - 10);
      final noisyY = trendY + (_rand.nextInt(noiseSpread * 2) - noiseSpread);
      return (x: x, y: noisyY.roundToDouble().clamp(1, 500).toDouble());
    }).map((p) => XYPair(x: p.x, y: p.y)).toList();

    final result = CorrelationSolver.solve(pairs);

    return GeneratedCorrelationProblem(
      id: 'CORR-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      pairs: pairs,
      result: result,
    );
  }
}

class GeneratedCorrelationProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final List<XYPair> pairs;
  final CorrelationResult result;

  const GeneratedCorrelationProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.pairs,
    required this.result,
  });
}
