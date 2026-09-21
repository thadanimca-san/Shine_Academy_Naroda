import '../models/board_model.dart';
import '../models/correlation_model.dart';
import '../models/regression_model.dart';
import 'correlation_generator.dart';
import 'regression_solver.dart';

/// Generates randomized Regression problems, reusing
/// [CorrelationGenerator]'s paired (X, Y) data generation since both
/// topics use the identical data shape and the same controlled-strength
/// linear relationship makes for well-posed regression questions too.
class RegressionGenerator {
  RegressionGenerator._();

  static GeneratedRegressionProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    final correlationProblem = CorrelationGenerator.generate(board: board, schoolClass: schoolClass, difficulty: difficulty);
    final result = RegressionSolver.solve(correlationProblem.pairs);

    return GeneratedRegressionProblem(
      id: 'REG-${correlationProblem.id}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      pairs: correlationProblem.pairs,
      result: result,
    );
  }
}

class GeneratedRegressionProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final List<XYPair> pairs;
  final RegressionResult result;

  const GeneratedRegressionProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.pairs,
    required this.result,
  });
}
