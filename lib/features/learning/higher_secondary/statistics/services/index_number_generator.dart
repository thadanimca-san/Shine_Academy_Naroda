import 'dart:math';

import '../models/board_model.dart';
import '../models/index_number_model.dart';
import 'index_number_solver.dart';

/// Generates randomized Index Number problems. Difficulty controls
/// whether quantity data is included: 1-2 -> Simple methods only
/// (prices alone), 3-5 -> quantities included so Laspeyres'/Paasche's
/// weighted methods are also examinable.
class IndexNumberGenerator {
  IndexNumberGenerator._();

  static final Random _rand = Random();

  static const _commodityNames = ['Rice', 'Wheat', 'Sugar', 'Milk', 'Oil', 'Tea', 'Coffee'];

  static GeneratedIndexNumberProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    final includeQuantities = difficulty >= 3;
    final commodityCount = 3 + _rand.nextInt(3); // 3-5 commodities
    final shuffledNames = List.of(_commodityNames)..shuffle(_rand);

    final commodities = List.generate(commodityCount, (i) {
      final basePrice = (5 + _rand.nextInt(45)).toDouble();
      // Current price fluctuates realistically around the base price,
      // sometimes up sometimes down, so the index isn't always > 100.
      final changeFactor = 0.7 + _rand.nextDouble() * 0.7;
      final currentPrice = (basePrice * changeFactor).roundToDouble().clamp(1, 500).toDouble();

      return CommodityPrice(
        name: shuffledNames[i],
        basePrice: basePrice,
        currentPrice: currentPrice,
        baseQuantity: includeQuantities ? (5 + _rand.nextInt(20)).toDouble() : 0,
        currentQuantity: includeQuantities ? (5 + _rand.nextInt(20)).toDouble() : 0,
      );
    });

    final result = IndexNumberSolver.solve(commodities);

    return GeneratedIndexNumberProblem(
      id: 'IDX-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      commodities: commodities,
      includeQuantities: includeQuantities,
      result: result,
    );
  }
}

class GeneratedIndexNumberProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final List<CommodityPrice> commodities;
  final bool includeQuantities;
  final IndexNumberResult result;

  const GeneratedIndexNumberProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.commodities,
    required this.includeQuantities,
    required this.result,
  });
}
