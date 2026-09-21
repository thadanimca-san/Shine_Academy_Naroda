import 'dart:math';

import '../models/central_tendency_model.dart';
import '../models/correlation_model.dart';

/// Deterministic solver for Karl Pearson's Coefficient of Correlation
/// using the Direct Method (deviations from actual means) — the
/// standard GSEB/CBSE Class 11 approach:
///
/// r = Σ(dx·dy) / √(Σdx² × Σdy²)
///
/// where dx = X − X̄ and dy = Y − Ȳ.
class CorrelationSolver {
  CorrelationSolver._();

  static CorrelationResult solve(List<XYPair> pairs) {
    final n = pairs.length;
    final meanX = pairs.fold(0.0, (a, p) => a + p.x) / n;
    final meanY = pairs.fold(0.0, (a, p) => a + p.y) / n;

    final deviations = pairs.map((p) => (dx: p.x - meanX, dy: p.y - meanY)).toList();
    final sumDxDy = deviations.fold(0.0, (a, d) => a + d.dx * d.dy);
    final sumDx2 = deviations.fold(0.0, (a, d) => a + d.dx * d.dx);
    final sumDy2 = deviations.fold(0.0, (a, d) => a + d.dy * d.dy);

    final denominator = sqrt(sumDx2 * sumDy2);
    // A zero denominator means X or Y has no variation at all (constant
    // series) -- correlation is undefined in that case; treat as 0 to
    // avoid a NaN reaching the UI, since GSEB/CBSE problems never
    // construct such a degenerate case deliberately.
    final r = denominator == 0 ? 0.0 : sumDxDy / denominator;
    final clampedR = r.clamp(-1.0, 1.0);

    return CorrelationResult(
      coefficient: clampedR,
      interpretation: _interpret(clampedR),
      steps: [
        SolutionStep(title: 'Find the means', reasoning: 'X̄ = ${_fmt(meanX)}, Ȳ = ${_fmt(meanY)}'),
        SolutionStep(
            title: 'Find the deviations dx = X − X̄ and dy = Y − Ȳ',
            reasoning: 'Calculate dx and dy for every pair, then dx·dy, dx² and dy².'),
        SolutionStep(title: 'Σ(dx·dy)', reasoning: 'Sum of the products of deviations = ${_fmt(sumDxDy)}'),
        SolutionStep(title: 'Σdx² and Σdy²', reasoning: 'Σdx² = ${_fmt(sumDx2)}, Σdy² = ${_fmt(sumDy2)}'),
        SolutionStep(
          title: 'r = Σ(dx·dy) / √(Σdx² × Σdy²)',
          reasoning: 'r = ${_fmt(sumDxDy)} / √(${_fmt(sumDx2)} × ${_fmt(sumDy2)}) = ${_fmt(clampedR)}',
        ),
      ],
    );
  }

  static String _interpret(double r) {
    final abs = r.abs();
    final direction = r > 0 ? 'positive' : (r < 0 ? 'negative' : 'no');
    if (abs >= 0.85) return 'Very strong $direction correlation';
    if (abs >= 0.6) return 'Strong $direction correlation';
    if (abs >= 0.3) return 'Moderate $direction correlation';
    if (abs > 0) return 'Weak $direction correlation';
    return 'No correlation';
  }

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(3);
  }
}
