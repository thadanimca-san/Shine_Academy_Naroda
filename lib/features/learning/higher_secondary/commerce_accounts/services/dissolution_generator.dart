import 'dart:math';

import '../models/dissolution_model.dart';
import '../models/partnership_model.dart';
import '../models/problem_model.dart';
import 'dissolution_solver.dart';

/// Generates randomized Dissolution of Partnership problems: 2-3
/// partners, a handful of assets realized at above/below book value, and
/// outside liabilities settled at (near) book value.
class DissolutionGenerator {
  DissolutionGenerator._();

  static final Random _rand = Random();

  static const _names = ['Ram', 'Shyam', 'Mohan', 'Sohan', 'Kiran', 'Nisha'];
  static const _assetNames = ['Machinery', 'Furniture', 'Stock', 'Debtors', 'Investments'];
  static const _liabilityNames = ['Creditors', 'Bills Payable', 'Bank Loan'];

  static GeneratedDissolutionProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    final partnerCount = difficulty <= 2 ? 2 : (2 + _rand.nextInt(2));
    final shuffledNames = List.of(_names)..shuffle(_rand);
    final ratios = _splitEvenly(partnerCount);
    final partners = List.generate(
      partnerCount,
      (i) => Partner(
        name: shuffledNames[i],
        capital: _round(50000 + _rand.nextDouble() * 60000),
        profitShareRatio: ratios[i],
      ),
    );

    final assetCount = difficulty <= 2 ? 2 : (2 + _rand.nextInt(2));
    final shuffledAssets = List.of(_assetNames)..shuffle(_rand);
    final assets = List.generate(assetCount, (i) {
      final bookValue = _round(15000 + _rand.nextDouble() * 35000);
      final realisedFactor = 0.6 + _rand.nextDouble() * 0.7; // 60%-130% of book value
      return AssetRealisation(
        assetName: shuffledAssets[i],
        bookValue: bookValue,
        realisedAmount: _round(bookValue * realisedFactor),
      );
    });

    final liabilityCount = difficulty <= 2 ? 1 : (1 + _rand.nextInt(2));
    final shuffledLiabilities = List.of(_liabilityNames)..shuffle(_rand);
    final liabilities = List.generate(liabilityCount, (i) {
      final bookValue = _round(10000 + _rand.nextDouble() * 20000);
      final paidFactor = difficulty >= 4 ? 0.9 + _rand.nextDouble() * 0.2 : 1.0; // settled at book value unless advanced
      return LiabilityPayment(
        liabilityName: shuffledLiabilities[i],
        bookValue: bookValue,
        amountPaid: _round(bookValue * paidFactor),
      );
    });

    final dissolutionExpenses = difficulty >= 3 ? _round(500 + _rand.nextDouble() * 2000) : 0.0;

    final result = DissolutionSolver.solve(
      partners: partners,
      assets: assets,
      liabilities: liabilities,
      dissolutionExpenses: dissolutionExpenses,
    );

    return GeneratedDissolutionProblem(
      id: 'DISS-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      partners: partners,
      assets: assets,
      liabilities: liabilities,
      dissolutionExpenses: dissolutionExpenses,
      result: result,
    );
  }

  static List<double> _splitEvenly(int n) {
    if (n == 2) {
      final options = [
        [0.6, 0.4],
        [0.5, 0.5],
      ];
      return options[_rand.nextInt(options.length)];
    }
    final options = [
      [0.4, 0.35, 0.25],
      [1 / 3, 1 / 3, 1 / 3],
    ];
    return options[_rand.nextInt(options.length)];
  }

  static double _round(double v) => (v / 100).round() * 100.0;
}

class GeneratedDissolutionProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final List<Partner> partners;
  final List<AssetRealisation> assets;
  final List<LiabilityPayment> liabilities;
  final double dissolutionExpenses;
  final DissolutionResult result;

  const GeneratedDissolutionProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.partners,
    required this.assets,
    required this.liabilities,
    required this.dissolutionExpenses,
    required this.result,
  });
}
