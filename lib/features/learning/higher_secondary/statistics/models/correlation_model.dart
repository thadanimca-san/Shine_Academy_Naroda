import 'central_tendency_model.dart';

/// One paired observation (X, Y) for correlation analysis.
class XYPair {
  final double x;
  final double y;

  const XYPair({required this.x, required this.y});
}

class CorrelationResult {
  final double coefficient; // Karl Pearson's r, between -1 and +1
  final String interpretation; // e.g. "Strong positive correlation"
  final List<SolutionStep> steps;

  const CorrelationResult({required this.coefficient, required this.interpretation, required this.steps});
}
