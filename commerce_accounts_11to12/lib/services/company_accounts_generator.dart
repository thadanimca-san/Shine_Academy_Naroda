import 'dart:math';

import '../models/company_accounts_model.dart';
import '../models/problem_model.dart';
import 'company_accounts_solver.dart';

/// Generates randomized Share Capital problems: issue of shares at par
/// or premium, fully subscribed, with optional forfeiture and reissue
/// of a small number of defaulting shareholders' shares.
class CompanyAccountsGenerator {
  CompanyAccountsGenerator._();

  static final Random _rand = Random();

  static const _faceValueOptions = [10.0, 100.0];

  static GeneratedShareIssueProblem generate({
    required Board board,
    required int schoolClass,
    required int difficulty,
  }) {
    final faceValue = _faceValueOptions[_rand.nextInt(_faceValueOptions.length)];
    final atPremium = difficulty >= 2 && _rand.nextBool();
    final premiumPerShare = atPremium ? _roundToFace(faceValue * 0.2) : 0.0;

    // Split face value + premium across the 4 call stages using
    // syllabus-typical round fractions (e.g. face 10 -> App 3, Allot 3,
    // First Call 2, Final Call 2), with premium collected at allotment.
    final perShareTotal = faceValue + premiumPerShare;
    final applicationAmount = _roundToFace(faceValue * 0.3);
    final firstCallAmount = difficulty >= 2 ? _roundToFace(faceValue * 0.3) : 0.0;
    final finalCallAmount = difficulty >= 3 ? _roundToFace(faceValue * 0.2) : 0.0;
    final allotmentAmount = perShareTotal - applicationAmount - firstCallAmount - finalCallAmount;

    final calls = CallStructure(
      faceValue: faceValue,
      premiumPerShare: premiumPerShare,
      applicationAmount: applicationAmount,
      allotmentAmount: allotmentAmount,
      firstCallAmount: firstCallAmount,
      finalCallAmount: finalCallAmount,
    );

    final sharesIssued = (5 + _rand.nextInt(16)) * 1000; // 5,000 - 20,000 shares
    final forfeitPortion = difficulty >= 4 ? 0.01 + _rand.nextDouble() * 0.02 : 0.0; // 1-3% forfeited
    final sharesForfeited = finalCallAmount > 0 ? (sharesIssued * forfeitPortion).round() : 0;
    final reissuePrice = _roundToFace(faceValue * (0.7 + _rand.nextDouble() * 0.5)); // 70%-120% of face value

    final result = CompanyAccountsSolver.solveFullySubscribedIssue(
      sharesIssued: sharesIssued,
      calls: calls,
      sharesForfeitedForFinalCallDefault: sharesForfeited,
      reissuePricePerShare: reissuePrice,
    );

    return GeneratedShareIssueProblem(
      id: 'SHR-${DateTime.now().millisecondsSinceEpoch}-${_rand.nextInt(9999)}',
      board: board,
      schoolClass: schoolClass,
      difficulty: difficulty,
      sharesIssued: sharesIssued,
      calls: calls,
      sharesForfeited: sharesForfeited,
      reissuePricePerShare: reissuePrice,
      result: result,
    );
  }

  static double _roundToFace(double v) => (v / 1).roundToDouble();
}

class GeneratedShareIssueProblem {
  final String id;
  final Board board;
  final int schoolClass;
  final int difficulty;
  final int sharesIssued;
  final CallStructure calls;
  final int sharesForfeited;
  final double reissuePricePerShare;
  final ShareIssueResult result;

  const GeneratedShareIssueProblem({
    required this.id,
    required this.board,
    required this.schoolClass,
    required this.difficulty,
    required this.sharesIssued,
    required this.calls,
    required this.sharesForfeited,
    required this.reissuePricePerShare,
    required this.result,
  });
}
