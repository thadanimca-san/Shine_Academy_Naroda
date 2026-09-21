import 'central_tendency_model.dart';

class RegressionLineResult {
  final double coefficient; // byx (Y on X) or bxy (X on Y)
  final double intercept; // 'a' in Y = a + bX, or the X-on-Y equivalent
  final String equation; // human-readable, e.g. "Y = 12.5 + 0.8X"
  final List<SolutionStep> steps;

  const RegressionLineResult({
    required this.coefficient,
    required this.intercept,
    required this.equation,
    required this.steps,
  });
}

class RegressionResult {
  final RegressionLineResult yOnX; // predicts Y from X
  final RegressionLineResult xOnY; // predicts X from Y
  final double impliedR; // sqrt(byx * bxy), signed to match the coefficients' sign

  const RegressionResult({required this.yOnX, required this.xOnY, required this.impliedR});
}
