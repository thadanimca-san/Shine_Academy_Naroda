import 'dart:math';

import '../models/central_tendency_model.dart';
import '../models/data_series_model.dart';
import '../models/dispersion_model.dart';
import 'central_tendency_solver.dart';

/// Deterministic solver for Measures of Dispersion — Range, Mean
/// Deviation (about the mean), Standard Deviation, and Coefficient of
/// Variation — across all three data shapes. Reuses
/// [CentralTendencySolver]'s Mean computation as the base for Mean
/// Deviation and Standard Deviation, so there is exactly one source of
/// truth for "what is the mean of this series" across both topics.
class DispersionSolver {
  DispersionSolver._();

  static DispersionResult solve(DataSeries series) {
    final mean = CentralTendencySolver.solve(series).mean.mean;
    final range = _solveRange(series);
    final meanDeviation = _solveMeanDeviation(series, mean);
    final sd = _solveStandardDeviation(series, mean);
    final cv = _solveCoefficientOfVariation(sd.standardDeviation, mean);

    return DispersionResult(
      range: range,
      meanDeviation: meanDeviation,
      standardDeviation: sd,
      coefficientOfVariation: cv,
    );
  }

  // ---------------- RANGE ----------------

  static RangeResult _solveRange(DataSeries s) {
    final (lowest, highest) = switch (s.type) {
      SeriesType.individual => (
          s.individualValues.reduce(min),
          s.individualValues.reduce(max),
        ),
      SeriesType.discrete => (
          s.discreteValues.map((d) => d.value).reduce(min),
          s.discreteValues.map((d) => d.value).reduce(max),
        ),
      SeriesType.continuous => (
          s.classIntervals.map((c) => c.lowerBound).reduce(min),
          s.classIntervals.map((c) => c.upperBound).reduce(max),
        ),
    };
    final range = highest - lowest;
    return RangeResult(range: range, steps: [
      SolutionStep(title: 'Identify the highest and lowest values', reasoning: 'Highest = ${_fmt(highest)}, Lowest = ${_fmt(lowest)}'),
      SolutionStep(title: 'Range = Highest − Lowest', reasoning: 'Range = ${_fmt(highest)} − ${_fmt(lowest)} = ${_fmt(range)}'),
    ]);
  }

  // ---------------- MEAN DEVIATION (about the mean) ----------------

  static MeanDeviationResult _solveMeanDeviation(DataSeries s, double mean) {
    switch (s.type) {
      case SeriesType.individual:
        final n = s.individualValues.length;
        final sumAbsDev = s.individualValues.fold(0.0, (a, v) => a + (v - mean).abs());
        final md = sumAbsDev / n;
        return MeanDeviationResult(meanDeviation: md, steps: [
          SolutionStep(title: 'Find |X − Mean| for each value', reasoning: 'Take the absolute deviation of every observation from the Mean (${_fmt(mean)}).'),
          SolutionStep(title: 'Σ|X − Mean|', reasoning: 'Sum of absolute deviations = ${_fmt(sumAbsDev)}'),
          SolutionStep(title: 'Mean Deviation = Σ|X − Mean| / N', reasoning: 'MD = ${_fmt(sumAbsDev)} / $n = ${_fmt(md)}'),
        ]);

      case SeriesType.discrete:
        final sumF = s.discreteValues.fold(0, (a, d) => a + d.frequency);
        final sumFAbsDev = s.discreteValues.fold(0.0, (a, d) => a + d.frequency * (d.value - mean).abs());
        final md = sumFAbsDev / sumF;
        return MeanDeviationResult(meanDeviation: md, steps: [
          SolutionStep(title: 'Find |X − Mean| for each value', reasoning: 'Take the absolute deviation of every value from the Mean (${_fmt(mean)}).'),
          SolutionStep(title: 'Σf|X − Mean|', reasoning: 'Multiply each absolute deviation by its frequency and sum = ${_fmt(sumFAbsDev)}'),
          SolutionStep(title: 'Mean Deviation = Σf|X − Mean| / Σf', reasoning: 'MD = ${_fmt(sumFAbsDev)} / $sumF = ${_fmt(md)}'),
        ]);

      case SeriesType.continuous:
        final sumF = s.classIntervals.fold(0, (a, c) => a + c.frequency);
        final sumFAbsDev = s.classIntervals.fold(0.0, (a, c) => a + c.frequency * (c.midpoint - mean).abs());
        final md = sumFAbsDev / sumF;
        return MeanDeviationResult(meanDeviation: md, steps: [
          SolutionStep(title: 'Find the mid-point of each class', reasoning: 'Mid-point m = (lower + upper) / 2 for each class interval.'),
          SolutionStep(title: 'Find |m − Mean| for each class', reasoning: 'Take the absolute deviation of every mid-point from the Mean (${_fmt(mean)}).'),
          SolutionStep(title: 'Σf|m − Mean|', reasoning: 'Multiply each absolute deviation by its class frequency and sum = ${_fmt(sumFAbsDev)}'),
          SolutionStep(title: 'Mean Deviation = Σf|m − Mean| / Σf', reasoning: 'MD = ${_fmt(sumFAbsDev)} / $sumF = ${_fmt(md)}'),
        ]);
    }
  }

  // ---------------- STANDARD DEVIATION ----------------

  static StandardDeviationResult _solveStandardDeviation(DataSeries s, double mean) {
    switch (s.type) {
      case SeriesType.individual:
        final n = s.individualValues.length;
        final sumSqDev = s.individualValues.fold(0.0, (a, v) => a + pow(v - mean, 2));
        final variance = sumSqDev / n;
        final sd = sqrt(variance);
        return StandardDeviationResult(standardDeviation: sd, variance: variance, steps: [
          SolutionStep(title: 'Find (X − Mean)² for each value', reasoning: 'Square the deviation of every observation from the Mean (${_fmt(mean)}).'),
          SolutionStep(title: 'Σ(X − Mean)²', reasoning: 'Sum of squared deviations = ${_fmt(sumSqDev)}'),
          SolutionStep(title: 'Variance = Σ(X − Mean)² / N', reasoning: 'Variance = ${_fmt(sumSqDev)} / $n = ${_fmt(variance)}'),
          SolutionStep(title: 'Standard Deviation = √Variance', reasoning: 'SD = √${_fmt(variance)} = ${_fmt(sd)}'),
        ]);

      case SeriesType.discrete:
        final sumF = s.discreteValues.fold(0, (a, d) => a + d.frequency);
        final sumFSqDev = s.discreteValues.fold(0.0, (a, d) => a + d.frequency * pow(d.value - mean, 2));
        final variance = sumFSqDev / sumF;
        final sd = sqrt(variance);
        return StandardDeviationResult(standardDeviation: sd, variance: variance, steps: [
          SolutionStep(title: 'Find (X − Mean)² for each value', reasoning: 'Square the deviation of every value from the Mean (${_fmt(mean)}).'),
          SolutionStep(title: 'Σf(X − Mean)²', reasoning: 'Multiply each squared deviation by its frequency and sum = ${_fmt(sumFSqDev)}'),
          SolutionStep(title: 'Variance = Σf(X − Mean)² / Σf', reasoning: 'Variance = ${_fmt(sumFSqDev)} / $sumF = ${_fmt(variance)}'),
          SolutionStep(title: 'Standard Deviation = √Variance', reasoning: 'SD = √${_fmt(variance)} = ${_fmt(sd)}'),
        ]);

      case SeriesType.continuous:
        final sumF = s.classIntervals.fold(0, (a, c) => a + c.frequency);
        final sumFSqDev = s.classIntervals.fold(0.0, (a, c) => a + c.frequency * pow(c.midpoint - mean, 2));
        final variance = sumFSqDev / sumF;
        final sd = sqrt(variance);
        return StandardDeviationResult(standardDeviation: sd, variance: variance, steps: [
          SolutionStep(title: 'Find the mid-point of each class', reasoning: 'Mid-point m = (lower + upper) / 2 for each class interval.'),
          SolutionStep(title: 'Find (m − Mean)² for each class', reasoning: 'Square the deviation of every mid-point from the Mean (${_fmt(mean)}).'),
          SolutionStep(title: 'Σf(m − Mean)²', reasoning: 'Multiply each squared deviation by its class frequency and sum = ${_fmt(sumFSqDev)}'),
          SolutionStep(title: 'Variance = Σf(m − Mean)² / Σf', reasoning: 'Variance = ${_fmt(sumFSqDev)} / $sumF = ${_fmt(variance)}'),
          SolutionStep(title: 'Standard Deviation = √Variance', reasoning: 'SD = √${_fmt(variance)} = ${_fmt(sd)}'),
        ]);
    }
  }

  // ---------------- COEFFICIENT OF VARIATION ----------------

  static CoefficientOfVariationResult _solveCoefficientOfVariation(double sd, double mean) {
    final cv = (sd / mean) * 100;
    return CoefficientOfVariationResult(coefficientOfVariation: cv, steps: [
      SolutionStep(
        title: 'C.V. = (Standard Deviation / Mean) × 100',
        reasoning: 'C.V. = (${_fmt(sd)} / ${_fmt(mean)}) × 100 = ${_fmt(cv)}%',
      ),
    ]);
  }

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
