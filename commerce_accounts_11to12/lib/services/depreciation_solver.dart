import '../models/depreciation_model.dart';
import '../models/solution_model.dart';

/// Deterministic solver for Straight Line Method (SLM) and Written Down
/// Value (WDV) depreciation — the two methods GSEB/CBSE Class 11 syllabus
/// covers. Pure calculation, no randomness, so the same schedule is used
/// for student hints and the teacher's printed answer key.
class DepreciationSolver {
  DepreciationSolver._();

  static DepreciationSchedule computeSchedule({
    required String assetName,
    required DepreciationMethod method,
    required double originalCost,
    required double ratePercent,
    required int years,
  }) {
    final rows = <DepreciationYearRow>[];
    double opening = originalCost;

    for (var y = 1; y <= years; y++) {
      final depreciation = method == DepreciationMethod.straightLine
          ? originalCost * ratePercent / 100
          : opening * ratePercent / 100;
      final closing = opening - depreciation;
      rows.add(DepreciationYearRow(
        year: y,
        openingBalance: opening,
        depreciationAmount: depreciation,
        closingBalance: closing,
      ));
      opening = closing;
    }

    return DepreciationSchedule(
      assetName: assetName,
      method: method,
      originalCost: originalCost,
      ratePercent: ratePercent,
      years: years,
      rows: rows,
    );
  }

  /// Step-by-step reasoning for one year's depreciation, matching how a
  /// teacher explains SLM ("always on original cost") vs WDV ("always on
  /// the reducing book value").
  static List<SolutionStep> explainYear(DepreciationSchedule schedule, int yearIndex) {
    final row = schedule.rows[yearIndex];
    final methodLabel = schedule.method == DepreciationMethod.straightLine
        ? 'Straight Line Method — depreciation is always calculated on the Original Cost'
        : 'Written Down Value Method — depreciation is calculated on the Opening (book) Value of that year';
    final baseAmount = schedule.method == DepreciationMethod.straightLine ? schedule.originalCost : row.openingBalance;

    return [
      SolutionStep(
        title: 'Year ${row.year}: Depreciation',
        reasoning: '$methodLabel. '
            'Depreciation = ${_fmt(baseAmount)} × ${schedule.ratePercent}% = ${_fmt(row.depreciationAmount)}.',
      ),
      SolutionStep(
        title: 'Year ${row.year}: Closing Balance',
        reasoning: 'Closing Balance = Opening Balance − Depreciation = '
            '${_fmt(row.openingBalance)} − ${_fmt(row.depreciationAmount)} = ${_fmt(row.closingBalance)}.',
      ),
    ];
  }

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return '₹${isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2)}';
  }
}
