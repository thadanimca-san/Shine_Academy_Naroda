/// The three data shapes GSEB/CBSE Class 11 Statistics distinguishes,
/// each with its own Mean/Median/Mode formulas:
/// - individual: a plain list of raw observations (no repeats grouped)
/// - discrete: distinct values each with a frequency
/// - continuous: class intervals (e.g. 10-20, 20-30) each with a frequency
enum SeriesType { individual, discrete, continuous }

/// One class interval in a continuous frequency distribution, e.g.
/// 10-20 with frequency 5. Intervals are assumed continuous and
/// non-overlapping (exclusive method) as GSEB/CBSE textbooks present them.
class ClassInterval {
  final double lowerBound;
  final double upperBound;
  final int frequency;

  const ClassInterval({required this.lowerBound, required this.upperBound, required this.frequency});

  double get midpoint => (lowerBound + upperBound) / 2;
  double get width => upperBound - lowerBound;
}

/// One distinct value and its frequency in a discrete series, e.g.
/// value 5 occurring 3 times.
class DiscreteValue {
  final double value;
  final int frequency;

  const DiscreteValue({required this.value, required this.frequency});
}

/// A single data series in whichever shape the problem uses. Exactly one
/// of [individualValues], [discreteValues], [classIntervals] is
/// populated, matching [type].
class DataSeries {
  final SeriesType type;
  final List<double> individualValues;
  final List<DiscreteValue> discreteValues;
  final List<ClassInterval> classIntervals;

  const DataSeries.individual(this.individualValues)
      : type = SeriesType.individual,
        discreteValues = const [],
        classIntervals = const [];

  const DataSeries.discrete(this.discreteValues)
      : type = SeriesType.discrete,
        individualValues = const [],
        classIntervals = const [];

  const DataSeries.continuous(this.classIntervals)
      : type = SeriesType.continuous,
        individualValues = const [],
        discreteValues = const [];

  int get totalFrequency => switch (type) {
        SeriesType.individual => individualValues.length,
        SeriesType.discrete => discreteValues.fold(0, (s, d) => s + d.frequency),
        SeriesType.continuous => classIntervals.fold(0, (s, c) => s + c.frequency),
      };
}
