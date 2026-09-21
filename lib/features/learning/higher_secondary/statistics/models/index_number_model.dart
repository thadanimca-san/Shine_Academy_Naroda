import 'central_tendency_model.dart';

/// One commodity's base-year and current-year price (and optionally
/// quantity, needed for the weighted methods) used to build a price
/// index — the standard GSEB/CBSE Class 11 "Index Numbers" data shape.
class CommodityPrice {
  final String name;
  final double basePrice;
  final double currentPrice;
  final double baseQuantity;
  final double currentQuantity;

  const CommodityPrice({
    required this.name,
    required this.basePrice,
    required this.currentPrice,
    this.baseQuantity = 0,
    this.currentQuantity = 0,
  });
}

class IndexNumberResult {
  final double simpleAggregativeIndex;
  final List<SolutionStep> simpleAggregativeSteps;

  final double simpleAveragePriceRelativeIndex;
  final List<SolutionStep> simpleAverageSteps;

  final double? laspeyresIndex; // null if no quantity data supplied
  final List<SolutionStep> laspeyresSteps;

  final double? paascheIndex;
  final List<SolutionStep> paascheSteps;

  const IndexNumberResult({
    required this.simpleAggregativeIndex,
    required this.simpleAggregativeSteps,
    required this.simpleAveragePriceRelativeIndex,
    required this.simpleAverageSteps,
    required this.laspeyresIndex,
    required this.laspeyresSteps,
    required this.paascheIndex,
    required this.paascheSteps,
  });
}
