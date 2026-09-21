import '../models/central_tendency_model.dart';
import '../models/data_series_model.dart';

/// Deterministic solver for Mean, Median and Mode across all three data
/// shapes (individual, discrete, continuous) — the standard GSEB/CBSE
/// Class 11 "Measures of Central Tendency" formulas, using the Direct
/// Method throughout (not Step-Deviation/Assumed Mean, which is a
/// natural follow-up variant).
class CentralTendencySolver {
  CentralTendencySolver._();

  static CentralTendencyResult solve(DataSeries series) {
    return CentralTendencyResult(
      mean: _solveMean(series),
      median: _solveMedian(series),
      mode: _solveMode(series),
    );
  }

  // ---------------- MEAN ----------------

  static MeanResult _solveMean(DataSeries s) {
    switch (s.type) {
      case SeriesType.individual:
        final n = s.individualValues.length;
        final sum = s.individualValues.fold(0.0, (a, b) => a + b);
        final mean = sum / n;
        return MeanResult(mean: mean, steps: [
          SolutionStep(title: 'Sum of observations (ΣX)', reasoning: 'ΣX = ${_fmt(sum)}'),
          SolutionStep(title: 'Number of observations (N)', reasoning: 'N = $n'),
          SolutionStep(
              title: 'Mean = ΣX / N',
              reasoning: 'Mean = ${_fmt(sum)} / $n = ${_fmt(mean)}'),
        ]);

      case SeriesType.discrete:
        final sumFX = s.discreteValues.fold(0.0, (a, d) => a + d.value * d.frequency);
        final sumF = s.discreteValues.fold(0, (a, d) => a + d.frequency);
        final mean = sumFX / sumF;
        return MeanResult(mean: mean, steps: [
          SolutionStep(
              title: 'Σ(f × X)',
              reasoning: 'Multiply each value by its frequency and sum: Σ(fX) = ${_fmt(sumFX)}'),
          SolutionStep(title: 'Σf (total frequency)', reasoning: 'Σf = $sumF'),
          SolutionStep(
              title: 'Mean = Σ(fX) / Σf',
              reasoning: 'Mean = ${_fmt(sumFX)} / $sumF = ${_fmt(mean)}'),
        ]);

      case SeriesType.continuous:
        final sumFM = s.classIntervals.fold(0.0, (a, c) => a + c.midpoint * c.frequency);
        final sumF = s.classIntervals.fold(0, (a, c) => a + c.frequency);
        final mean = sumFM / sumF;
        return MeanResult(mean: mean, steps: [
          SolutionStep(
              title: 'Find the mid-point of each class',
              reasoning: 'Mid-point m = (lower + upper) / 2 for each class interval.'),
          SolutionStep(
              title: 'Σ(f × m)',
              reasoning: 'Multiply each mid-point by its class frequency and sum: Σ(fm) = ${_fmt(sumFM)}'),
          SolutionStep(title: 'Σf (total frequency)', reasoning: 'Σf = $sumF'),
          SolutionStep(
              title: 'Mean = Σ(fm) / Σf',
              reasoning: 'Mean = ${_fmt(sumFM)} / $sumF = ${_fmt(mean)}'),
        ]);
    }
  }

  // ---------------- MEDIAN ----------------

  static MedianResult _solveMedian(DataSeries s) {
    switch (s.type) {
      case SeriesType.individual:
        final sorted = [...s.individualValues]..sort();
        final n = sorted.length;
        final double median;
        final String workingNote;
        if (n.isOdd) {
          final pos = (n + 1) / 2;
          median = sorted[pos.floor() - 1];
          workingNote = 'N is odd, so Median = value at position (N+1)/2 = position ${_fmt(pos)} = ${_fmt(median)}';
        } else {
          final a = sorted[n ~/ 2 - 1];
          final b = sorted[n ~/ 2];
          median = (a + b) / 2;
          workingNote =
              'N is even, so Median = average of the two middle values (positions ${n ~/ 2} and ${n ~/ 2 + 1}) '
              '= (${_fmt(a)} + ${_fmt(b)}) / 2 = ${_fmt(median)}';
        }
        return MedianResult(median: median, steps: [
          SolutionStep(title: 'Arrange data in ascending order', reasoning: sorted.map(_fmt).join(', ')),
          SolutionStep(title: 'Locate the middle value', reasoning: workingNote),
        ]);

      case SeriesType.discrete:
        final sortedEntries = [...s.discreteValues]..sort((a, b) => a.value.compareTo(b.value));
        final n = sortedEntries.fold(0, (a, d) => a + d.frequency);
        final targetPos = (n + 1) / 2;
        var cumulative = 0;
        double? median;
        final cfSteps = <String>[];
        for (final entry in sortedEntries) {
          cumulative += entry.frequency;
          cfSteps.add('Value ${_fmt(entry.value)}: f=${entry.frequency}, cf=$cumulative');
          median ??= cumulative >= targetPos ? entry.value : null;
        }
        median ??= sortedEntries.isNotEmpty ? sortedEntries.last.value : 0;
        return MedianResult(median: median, steps: [
          SolutionStep(title: 'Build the cumulative frequency (cf) column', reasoning: cfSteps.join(' | ')),
          SolutionStep(
              title: 'Locate the (N+1)/2-th observation',
              reasoning: 'N = $n, so target position = ${_fmt(targetPos)}. '
                  'The first cf reaching this position gives Median = ${_fmt(median)}.'),
        ]);

      case SeriesType.continuous:
        final sortedIntervals = [...s.classIntervals]..sort((a, b) => a.lowerBound.compareTo(b.lowerBound));
        final n = sortedIntervals.fold(0, (a, c) => a + c.frequency);
        final targetPos = n / 2;
        var cumulative = 0;
        ClassInterval? medianClass;
        int cfBeforeMedianClass = 0;
        final cfSteps = <String>[];
        for (final interval in sortedIntervals) {
          final prevCumulative = cumulative;
          cumulative += interval.frequency;
          cfSteps.add('${_fmt(interval.lowerBound)}-${_fmt(interval.upperBound)}: f=${interval.frequency}, cf=$cumulative');
          if (medianClass == null && cumulative >= targetPos) {
            medianClass = interval;
            cfBeforeMedianClass = prevCumulative;
          }
        }
        final mc = medianClass!;
        final median = mc.lowerBound + ((targetPos - cfBeforeMedianClass) / mc.frequency) * mc.width;
        return MedianResult(median: median, steps: [
          SolutionStep(title: 'Build the cumulative frequency (cf) column', reasoning: cfSteps.join(' | ')),
          SolutionStep(
              title: 'Locate the Median class',
              reasoning: 'N/2 = ${_fmt(targetPos)}. The class whose cf first reaches or exceeds this is '
                  '${_fmt(mc.lowerBound)}-${_fmt(mc.upperBound)} (cf before this class = $cfBeforeMedianClass).'),
          SolutionStep(
              title: 'Apply the Median formula',
              reasoning: 'Median = L + [(N/2 − cf) / f] × h\n'
                  '= ${_fmt(mc.lowerBound)} + [(${_fmt(targetPos)} − $cfBeforeMedianClass) / ${mc.frequency}] × ${_fmt(mc.width)}\n'
                  '= ${_fmt(median)}'),
        ]);
    }
  }

  // ---------------- MODE ----------------

  static ModeResult _solveMode(DataSeries s) {
    switch (s.type) {
      case SeriesType.individual:
        final counts = <double, int>{};
        for (final v in s.individualValues) {
          counts[v] = (counts[v] ?? 0) + 1;
        }
        final maxCount = counts.values.fold(0, (a, b) => a > b ? a : b);
        final modes = counts.entries.where((e) => e.value == maxCount).map((e) => e.key).toList();
        final hasMode = maxCount > 1 && modes.length == 1;
        return ModeResult(
          mode: hasMode ? modes.first : null,
          steps: [
            SolutionStep(
                title: 'Count the frequency of each value',
                reasoning: counts.entries.map((e) => '${_fmt(e.key)}: ${e.value} time(s)').join(', ')),
            SolutionStep(
                title: 'Identify the most frequent value',
                reasoning: hasMode
                    ? 'Mode = ${_fmt(modes.first)} (appears $maxCount times, more than any other value)'
                    : 'No single value repeats more than the others, so this data set has no clear mode.'),
          ],
        );

      case SeriesType.discrete:
        final maxFreq = s.discreteValues.fold(0, (a, d) => a > d.frequency ? a : d.frequency);
        final modalEntries = s.discreteValues.where((d) => d.frequency == maxFreq).toList();
        final hasMode = modalEntries.length == 1;
        return ModeResult(
          mode: hasMode ? modalEntries.first.value : null,
          steps: [
            SolutionStep(
                title: 'Identify the highest frequency',
                reasoning: 'The highest frequency in the table is $maxFreq.'),
            SolutionStep(
                title: 'Mode = value with the highest frequency',
                reasoning: hasMode
                    ? 'Mode = ${_fmt(modalEntries.first.value)} (frequency $maxFreq)'
                    : 'More than one value shares the highest frequency, so this data set has no single mode.'),
          ],
        );

      case SeriesType.continuous:
        final maxFreq = s.classIntervals.fold(0, (a, c) => a > c.frequency ? a : c.frequency);
        final modalClasses = s.classIntervals.where((c) => c.frequency == maxFreq).toList();
        if (modalClasses.length != 1) {
          return ModeResult(mode: null, steps: [
            SolutionStep(
                title: 'Identify the modal class',
                reasoning: 'More than one class shares the highest frequency ($maxFreq), so the mode is not well-defined by the simple formula.'),
          ]);
        }
        final modalClass = modalClasses.first;
        final index = s.classIntervals.indexOf(modalClass);
        final f1 = modalClass.frequency;
        final f0 = index > 0 ? s.classIntervals[index - 1].frequency : 0;
        final f2 = index < s.classIntervals.length - 1 ? s.classIntervals[index + 1].frequency : 0;
        final h = modalClass.width;
        final denominator = (2 * f1 - f0 - f2);
        final mode = denominator == 0
            ? modalClass.midpoint
            : modalClass.lowerBound + ((f1 - f0) / denominator) * h;
        return ModeResult(mode: mode, steps: [
          SolutionStep(
              title: 'Identify the modal class',
              reasoning: 'The class with the highest frequency ($maxFreq) is '
                  '${_fmt(modalClass.lowerBound)}-${_fmt(modalClass.upperBound)}.'),
          SolutionStep(
              title: 'Apply the Mode formula',
              reasoning: 'Mode = L + [(f₁ − f₀) / (2f₁ − f₀ − f₂)] × h\n'
                  '= ${_fmt(modalClass.lowerBound)} + [($f1 − $f0) / (2×$f1 − $f0 − $f2)] × ${_fmt(h)}\n'
                  '= ${_fmt(mode)}'),
        ]);
    }
  }

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
