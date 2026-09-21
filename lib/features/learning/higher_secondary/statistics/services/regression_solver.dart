import 'dart:math';

import '../models/central_tendency_model.dart';
import '../models/correlation_model.dart';
import '../models/regression_model.dart';

/// Deterministic solver for Regression Analysis using the Deviation
/// Method (deviations from actual means) — the standard GSEB/CBSE
/// Class 12 approach, computing both regression lines:
///
/// Regression of Y on X:  byx = Σ(dx·dy) / Σdx²   →  (Y − Ȳ) = byx(X − X̄)
/// Regression of X on Y:  bxy = Σ(dx·dy) / Σdy²   →  (X − X̄) = bxy(Y − Ȳ)
///
/// Reuses the same deviation sums as [CorrelationSolver] conceptually
/// (same underlying dx/dy pairs), computed independently here so this
/// topic's tests remain self-contained.
class RegressionSolver {
  RegressionSolver._();

  static RegressionResult solve(List<XYPair> pairs) {
    final n = pairs.length;
    final meanX = pairs.fold(0.0, (a, p) => a + p.x) / n;
    final meanY = pairs.fold(0.0, (a, p) => a + p.y) / n;

    final deviations = pairs.map((p) => (dx: p.x - meanX, dy: p.y - meanY)).toList();
    final sumDxDy = deviations.fold(0.0, (a, d) => a + d.dx * d.dy);
    final sumDx2 = deviations.fold(0.0, (a, d) => a + d.dx * d.dx);
    final sumDy2 = deviations.fold(0.0, (a, d) => a + d.dy * d.dy);

    final byx = sumDx2 == 0 ? 0.0 : sumDxDy / sumDx2;
    final bxy = sumDy2 == 0 ? 0.0 : sumDxDy / sumDy2;

    // Y = a + byx*X, where a = Ȳ - byx*X̄ (rearranged from Y-Ȳ = byx(X-X̄))
    final yOnXIntercept = meanY - byx * meanX;
    // X = a' + bxy*Y, where a' = X̄ - bxy*Ȳ
    final xOnYIntercept = meanX - bxy * meanY;

    final rSquared = byx * bxy;
    final impliedR = (byx >= 0 ? 1 : -1) * (rSquared < 0 ? 0.0 : sqrt(rSquared));

    return RegressionResult(
      yOnX: RegressionLineResult(
        coefficient: byx,
        intercept: yOnXIntercept,
        equation: 'Y = ${_fmt(yOnXIntercept)} + ${_fmt(byx)}X',
        steps: [
          SolutionStep(title: 'Find the means', reasoning: 'X̄ = ${_fmt(meanX)}, Ȳ = ${_fmt(meanY)}'),
          SolutionStep(
              title: 'Find Σ(dx·dy) and Σdx²',
              reasoning: 'Σ(dx·dy) = ${_fmt(sumDxDy)}, Σdx² = ${_fmt(sumDx2)}'),
          SolutionStep(
            title: 'byx = Σ(dx·dy) / Σdx²',
            reasoning: 'byx = ${_fmt(sumDxDy)} / ${_fmt(sumDx2)} = ${_fmt(byx)}',
          ),
          SolutionStep(
            title: 'Regression line of Y on X: (Y − Ȳ) = byx(X − X̄)',
            reasoning: 'Y − ${_fmt(meanY)} = ${_fmt(byx)}(X − ${_fmt(meanX)}), i.e. Y = ${_fmt(yOnXIntercept)} + ${_fmt(byx)}X',
          ),
        ],
      ),
      xOnY: RegressionLineResult(
        coefficient: bxy,
        intercept: xOnYIntercept,
        equation: 'X = ${_fmt(xOnYIntercept)} + ${_fmt(bxy)}Y',
        steps: [
          SolutionStep(title: 'Find the means', reasoning: 'X̄ = ${_fmt(meanX)}, Ȳ = ${_fmt(meanY)}'),
          SolutionStep(
              title: 'Find Σ(dx·dy) and Σdy²',
              reasoning: 'Σ(dx·dy) = ${_fmt(sumDxDy)}, Σdy² = ${_fmt(sumDy2)}'),
          SolutionStep(
            title: 'bxy = Σ(dx·dy) / Σdy²',
            reasoning: 'bxy = ${_fmt(sumDxDy)} / ${_fmt(sumDy2)} = ${_fmt(bxy)}',
          ),
          SolutionStep(
            title: 'Regression line of X on Y: (X − X̄) = bxy(Y − Ȳ)',
            reasoning: 'X − ${_fmt(meanX)} = ${_fmt(bxy)}(Y − ${_fmt(meanY)}), i.e. X = ${_fmt(xOnYIntercept)} + ${_fmt(bxy)}Y',
          ),
        ],
      ),
      impliedR: impliedR,
    );
  }

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(3);
  }
}
