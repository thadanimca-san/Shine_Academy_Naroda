enum DepreciationMethod { straightLine, writtenDownValue }

/// One year's depreciation calculation row, shown to the student/teacher
/// exactly as it would appear worked out on paper: opening balance for
/// the year, the depreciation charged, and the closing balance carried
/// to next year.
class DepreciationYearRow {
  final int year;
  final double openingBalance;
  final double depreciationAmount;
  final double closingBalance;

  const DepreciationYearRow({
    required this.year,
    required this.openingBalance,
    required this.depreciationAmount,
    required this.closingBalance,
  });
}

/// A full depreciation schedule for one asset over its useful/practice
/// period, plus the reasoning needed to explain each year's figure.
class DepreciationSchedule {
  final String assetName;
  final DepreciationMethod method;
  final double originalCost;
  final double ratePercent;
  final int years;
  final List<DepreciationYearRow> rows;

  const DepreciationSchedule({
    required this.assetName,
    required this.method,
    required this.originalCost,
    required this.ratePercent,
    required this.years,
    required this.rows,
  });

  double get totalDepreciation => rows.fold(0.0, (s, r) => s + r.depreciationAmount);
  double get finalBookValue => rows.isEmpty ? originalCost : rows.last.closingBalance;
}
