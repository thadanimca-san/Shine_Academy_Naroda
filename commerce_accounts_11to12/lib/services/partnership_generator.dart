import 'dart:math';

import '../models/partnership_model.dart';
import '../models/problem_model.dart';
import 'partnership_solver.dart';

/// Generates randomized Partnership Admission and Retirement/Death
/// problems with realistic capitals, shares, and goodwill figures.
class PartnershipGenerator {
  PartnershipGenerator._();

  static final Random _rand = Random();

  static const _names = ['Ram', 'Shyam', 'Mohan', 'Sohan', 'Kiran', 'Nisha', 'Amit', 'Priya'];

  static GeneratedAdmissionProblem generateAdmission({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    final shuffled = List.of(_names)..shuffle(_rand);
    final existingCount = difficulty <= 2 ? 2 : (2 + _rand.nextInt(2));
    final existingNames = shuffled.take(existingCount).toList();
    final newPartnerName = shuffled[existingCount];

    // Existing partners split the whole firm (ratio sums to 1) in a
    // simple round-number split appropriate for Class 12 problems.
    final ratios = _splitEvenly(existingCount);
    final existingPartners = List.generate(
      existingCount,
      (i) => Partner(
        name: existingNames[i],
        capital: _round(60000 + _rand.nextDouble() * 80000),
        profitShareRatio: ratios[i],
      ),
    );

    final newPartnerShareOptions = [0.2, 0.25, 1 / 3, 0.2, 0.25];
    final newPartnerShare = newPartnerShareOptions[_rand.nextInt(newPartnerShareOptions.length)];
    final newPartnerCapital = _round(40000 + _rand.nextDouble() * 60000);
    final goodwill = GoodwillInfo(totalFirmGoodwill: _round(30000 + _rand.nextDouble() * 90000));

    final result = PartnershipSolver.solveAdmission(
      existingPartners: existingPartners,
      newPartnerName: newPartnerName,
      newPartnerShare: newPartnerShare,
      newPartnerCapital: newPartnerCapital,
      goodwill: goodwill,
    );

    return GeneratedAdmissionProblem(
      id: 'ADM-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      existingPartners: existingPartners,
      newPartnerName: newPartnerName,
      newPartnerShare: newPartnerShare,
      newPartnerCapital: newPartnerCapital,
      goodwill: goodwill,
      result: result,
    );
  }

  static GeneratedDepartureProblem generateDeparture({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    final shuffled = List.of(_names)..shuffle(_rand);
    final partnerCount = difficulty <= 2 ? 3 : (3 + _rand.nextInt(2));
    final names = shuffled.take(partnerCount).toList();
    final ratios = _splitEvenly(partnerCount);

    final partners = List.generate(
      partnerCount,
      (i) => Partner(
        name: names[i],
        capital: _round(60000 + _rand.nextDouble() * 80000),
        profitShareRatio: ratios[i],
      ),
    );

    final departingPartner = names[_rand.nextInt(partnerCount)];
    final reason = _rand.nextBool() ? DepartureReason.retirement : DepartureReason.death;
    final goodwill = GoodwillInfo(totalFirmGoodwill: _round(40000 + _rand.nextDouble() * 100000));

    final result = PartnershipSolver.solveDeparture(
      allPartners: partners,
      departingPartnerName: departingPartner,
      reason: reason,
      goodwill: goodwill,
    );

    return GeneratedDepartureProblem(
      id: 'DEP-PARTNER-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      allPartners: partners,
      departingPartnerName: departingPartner,
      reason: reason,
      goodwill: goodwill,
      result: result,
    );
  }

  /// Splits 1.0 into [n] round-fraction shares that sum exactly to 1 —
  /// e.g. 2 partners -> [0.6, 0.4]; 3 partners -> [0.4, 0.35, 0.25].
  static List<double> _splitEvenly(int n) {
    if (n == 2) {
      final options = [
        [0.6, 0.4],
        [0.5, 0.5],
        [0.7, 0.3],
      ];
      return options[_rand.nextInt(options.length)];
    }
    final options = [
      [0.4, 0.35, 0.25],
      [0.5, 0.3, 0.2],
      [1 / 3, 1 / 3, 1 / 3],
      [0.3, 0.3, 0.2, 0.2],
    ];
    final candidates = options.where((o) => o.length == n).toList();
    return candidates.isNotEmpty ? candidates[_rand.nextInt(candidates.length)] : List.filled(n, 1 / n);
  }

  static double _round(double v) => (v / 100).round() * 100.0;
}

class GeneratedAdmissionProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final List<Partner> existingPartners;
  final String newPartnerName;
  final double newPartnerShare;
  final double newPartnerCapital;
  final GoodwillInfo goodwill;
  final AdmissionResult result;

  const GeneratedAdmissionProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.existingPartners,
    required this.newPartnerName,
    required this.newPartnerShare,
    required this.newPartnerCapital,
    required this.goodwill,
    required this.result,
  });
}

class GeneratedDepartureProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final List<Partner> allPartners;
  final String departingPartnerName;
  final DepartureReason reason;
  final GoodwillInfo goodwill;
  final DepartureResult result;

  const GeneratedDepartureProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.allPartners,
    required this.departingPartnerName,
    required this.reason,
    required this.goodwill,
    required this.result,
  });
}
