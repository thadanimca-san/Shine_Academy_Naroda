import '../models/central_tendency_model.dart';
import '../models/index_number_model.dart';

/// Deterministic solver for Index Numbers — the four standard GSEB/CBSE
/// Class 11 methods:
/// - Simple Aggregative Method: P01 = (ΣP1 / ΣP0) × 100
/// - Simple Average of Price Relatives: P01 = Σ(P1/P0 × 100) / N
/// - Laspeyres' Method (base-year quantities as weights):
///     P01 = (ΣP1Q0 / ΣP0Q0) × 100
/// - Paasche's Method (current-year quantities as weights):
///     P01 = (ΣP1Q1 / ΣP0Q1) × 100
///
/// Laspeyres' and Paasche's are only computed (non-null) when quantity
/// data is actually supplied, since without it those methods aren't
/// examinable — the problem generator controls this by difficulty.
class IndexNumberSolver {
  IndexNumberSolver._();

  static IndexNumberResult solve(List<CommodityPrice> commodities) {
    final hasQuantities = commodities.every((c) => c.baseQuantity > 0 && c.currentQuantity > 0);

    final (aggIndex, aggSteps) = _solveSimpleAggregative(commodities);
    final (avgIndex, avgSteps) = _solveSimpleAveragePriceRelative(commodities);
    final laspeyres = hasQuantities ? _solveLaspeyres(commodities) : null;
    final paasche = hasQuantities ? _solvePaasche(commodities) : null;

    return IndexNumberResult(
      simpleAggregativeIndex: aggIndex,
      simpleAggregativeSteps: aggSteps,
      simpleAveragePriceRelativeIndex: avgIndex,
      simpleAverageSteps: avgSteps,
      laspeyresIndex: laspeyres?.$1,
      laspeyresSteps: laspeyres?.$2 ?? const [],
      paascheIndex: paasche?.$1,
      paascheSteps: paasche?.$2 ?? const [],
    );
  }

  static (double, List<SolutionStep>) _solveSimpleAggregative(List<CommodityPrice> commodities) {
    final sumP0 = commodities.fold(0.0, (a, c) => a + c.basePrice);
    final sumP1 = commodities.fold(0.0, (a, c) => a + c.currentPrice);
    final index = (sumP1 / sumP0) * 100;
    return (
      index,
      [
        SolutionStep(title: 'ΣP0 (sum of base year prices)', reasoning: 'ΣP0 = ${_fmt(sumP0)}'),
        SolutionStep(title: 'ΣP1 (sum of current year prices)', reasoning: 'ΣP1 = ${_fmt(sumP1)}'),
        SolutionStep(
          title: 'P01 = (ΣP1 / ΣP0) × 100',
          reasoning: 'P01 = (${_fmt(sumP1)} / ${_fmt(sumP0)}) × 100 = ${_fmt(index)}',
        ),
      ],
    );
  }

  static (double, List<SolutionStep>) _solveSimpleAveragePriceRelative(List<CommodityPrice> commodities) {
    final n = commodities.length;
    final relatives = commodities.map((c) => (c.currentPrice / c.basePrice) * 100).toList();
    final sumRelatives = relatives.fold(0.0, (a, r) => a + r);
    final index = sumRelatives / n;
    return (
      index,
      [
        SolutionStep(
          title: 'Find the Price Relative for each commodity',
          reasoning: 'Price Relative = (P1/P0) × 100 for each commodity.',
        ),
        SolutionStep(title: 'Σ(Price Relatives)', reasoning: 'Sum of all price relatives = ${_fmt(sumRelatives)}'),
        SolutionStep(
          title: 'P01 = Σ(Price Relatives) / N',
          reasoning: 'P01 = ${_fmt(sumRelatives)} / $n = ${_fmt(index)}',
        ),
      ],
    );
  }

  static (double, List<SolutionStep>) _solveLaspeyres(List<CommodityPrice> commodities) {
    final sumP0Q0 = commodities.fold(0.0, (a, c) => a + c.basePrice * c.baseQuantity);
    final sumP1Q0 = commodities.fold(0.0, (a, c) => a + c.currentPrice * c.baseQuantity);
    final index = (sumP1Q0 / sumP0Q0) * 100;
    return (
      index,
      [
        SolutionStep(
          title: "Laspeyres' Method uses base-year quantities (Q0) as weights",
          reasoning: 'Multiply base and current prices by base-year quantity for each commodity.',
        ),
        SolutionStep(title: 'Σ(P0 × Q0) and Σ(P1 × Q0)', reasoning: 'ΣP0Q0 = ${_fmt(sumP0Q0)}, ΣP1Q0 = ${_fmt(sumP1Q0)}'),
        SolutionStep(
          title: 'P01 = (ΣP1Q0 / ΣP0Q0) × 100',
          reasoning: 'P01 = (${_fmt(sumP1Q0)} / ${_fmt(sumP0Q0)}) × 100 = ${_fmt(index)}',
        ),
      ],
    );
  }

  static (double, List<SolutionStep>) _solvePaasche(List<CommodityPrice> commodities) {
    final sumP0Q1 = commodities.fold(0.0, (a, c) => a + c.basePrice * c.currentQuantity);
    final sumP1Q1 = commodities.fold(0.0, (a, c) => a + c.currentPrice * c.currentQuantity);
    final index = (sumP1Q1 / sumP0Q1) * 100;
    return (
      index,
      [
        SolutionStep(
          title: "Paasche's Method uses current-year quantities (Q1) as weights",
          reasoning: 'Multiply base and current prices by current-year quantity for each commodity.',
        ),
        SolutionStep(title: 'Σ(P0 × Q1) and Σ(P1 × Q1)', reasoning: 'ΣP0Q1 = ${_fmt(sumP0Q1)}, ΣP1Q1 = ${_fmt(sumP1Q1)}'),
        SolutionStep(
          title: 'P01 = (ΣP1Q1 / ΣP0Q1) × 100',
          reasoning: 'P01 = (${_fmt(sumP1Q1)} / ${_fmt(sumP0Q1)}) × 100 = ${_fmt(index)}',
        ),
      ],
    );
  }

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
