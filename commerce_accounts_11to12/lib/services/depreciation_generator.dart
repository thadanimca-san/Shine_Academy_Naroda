import 'dart:math';

import '../models/depreciation_model.dart';
import '../models/problem_model.dart';
import 'depreciation_solver.dart';

/// Generates randomized-but-realistic depreciation problems: an asset,
/// original cost, a syllabus-typical rate, and a number of years,
/// producing a schedule via [DepreciationSolver]. Rates and asset names
/// are kept within ranges Class 11 textbooks actually use so generated
/// numbers always look like real exam questions.
class DepreciationGenerator {
  DepreciationGenerator._();

  static final Random _rand = Random();

  static const _assetNames = ['Machinery', 'Furniture', 'Computer', 'Vehicle', 'Plant'];
  static const _slmRates = [5.0, 10.0, 15.0, 20.0];
  static const _wdvRates = [10.0, 15.0, 20.0, 25.0];

  static GeneratedDepreciationProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    final method = _rand.nextBool() ? DepreciationMethod.straightLine : DepreciationMethod.writtenDownValue;
    final assetName = _assetNames[_rand.nextInt(_assetNames.length)];
    final cost = _round(50000 + _rand.nextDouble() * 450000);
    final rate = method == DepreciationMethod.straightLine
        ? _slmRates[_rand.nextInt(_slmRates.length)]
        : _wdvRates[_rand.nextInt(_wdvRates.length)];
    final years = (2 + (difficulty / 2).ceil()).clamp(2, 5);

    final schedule = DepreciationSolver.computeSchedule(
      assetName: assetName,
      method: method,
      originalCost: cost,
      ratePercent: rate,
      years: years,
    );

    return GeneratedDepreciationProblem(
      id: 'DEP-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      schedule: schedule,
    );
  }

  static double _round(double v) => (v / 100).round() * 100.0;
}

class GeneratedDepreciationProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final DepreciationSchedule schedule;

  const GeneratedDepreciationProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.schedule,
  });
}
