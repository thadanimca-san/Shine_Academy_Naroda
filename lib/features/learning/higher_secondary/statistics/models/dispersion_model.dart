import 'central_tendency_model.dart';

class RangeResult {
  final double range;
  final List<SolutionStep> steps;

  const RangeResult({required this.range, required this.steps});
}

class MeanDeviationResult {
  final double meanDeviation; // about the mean
  final List<SolutionStep> steps;

  const MeanDeviationResult({required this.meanDeviation, required this.steps});
}

class StandardDeviationResult {
  final double standardDeviation;
  final double variance;
  final List<SolutionStep> steps;

  const StandardDeviationResult({required this.standardDeviation, required this.variance, required this.steps});
}

class CoefficientOfVariationResult {
  final double coefficientOfVariation; // as a percentage
  final List<SolutionStep> steps;

  const CoefficientOfVariationResult({required this.coefficientOfVariation, required this.steps});
}

class DispersionResult {
  final RangeResult range;
  final MeanDeviationResult meanDeviation;
  final StandardDeviationResult standardDeviation;
  final CoefficientOfVariationResult coefficientOfVariation;

  const DispersionResult({
    required this.range,
    required this.meanDeviation,
    required this.standardDeviation,
    required this.coefficientOfVariation,
  });
}
