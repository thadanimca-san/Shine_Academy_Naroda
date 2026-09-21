import 'dart:math';

import '../models/board_model.dart';
import '../models/data_series_model.dart';
import '../models/dispersion_model.dart';
import 'dispersion_solver.dart';

/// Generates randomized Measures of Dispersion problems, reusing the
/// same three-shape generation logic as Central Tendency (kept
/// independent here rather than importing that generator, since
/// dispersion problems benefit from tighter/more varied spreads to make
/// Range and SD meaningfully different across difficulty levels).
class DispersionGenerator {
  DispersionGenerator._();

  static final Random _rand = Random();

  static GeneratedDispersionProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    final DataSeries series;
    if (difficulty <= 2) {
      series = _generateIndividual();
    } else if (difficulty == 3) {
      series = _generateDiscrete();
    } else {
      series = _generateContinuous();
    }

    final result = DispersionSolver.solve(series);

    return GeneratedDispersionProblem(
      id: 'DISP-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      series: series,
      result: result,
    );
  }

  static DataSeries _generateIndividual() {
    final count = 5 + _rand.nextInt(6); // 5-10 observations
    final values = List.generate(count, (_) => (5 + _rand.nextInt(95)).toDouble());
    return DataSeries.individual(values);
  }

  static DataSeries _generateDiscrete() {
    final distinctCount = 4 + _rand.nextInt(3); // 4-6 distinct values
    final usedValues = <double>{};
    while (usedValues.length < distinctCount) {
      usedValues.add((1 + _rand.nextInt(30)).toDouble());
    }
    final sortedValues = usedValues.toList()..sort();
    final entries = sortedValues.map((v) => DiscreteValue(value: v, frequency: 2 + _rand.nextInt(10))).toList();
    return DataSeries.discrete(entries);
  }

  static DataSeries _generateContinuous() {
    final classCount = 5 + _rand.nextInt(3); // 5-7 classes
    final classWidth = [5, 10, 20][_rand.nextInt(3)].toDouble();
    final start = [0, 10, 20][_rand.nextInt(3)].toDouble();

    final intervals = <ClassInterval>[];
    var lower = start;
    for (var i = 0; i < classCount; i++) {
      final freq = 3 + _rand.nextInt(15);
      intervals.add(ClassInterval(lowerBound: lower, upperBound: lower + classWidth, frequency: freq));
      lower += classWidth;
    }
    return DataSeries.continuous(intervals);
  }
}

class GeneratedDispersionProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final DataSeries series;
  final DispersionResult result;

  const GeneratedDispersionProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.series,
    required this.result,
  });
}
