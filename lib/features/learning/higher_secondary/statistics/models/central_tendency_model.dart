/// One explained step of a worked solution, shown to students as a
/// reveal and to teachers as an answer-key line — same shape used
/// throughout for consistency.
class SolutionStep {
  final String title;
  final String reasoning;

  const SolutionStep({required this.title, required this.reasoning});
}

class MeanResult {
  final double mean;
  final List<SolutionStep> steps;

  const MeanResult({required this.mean, required this.steps});
}

class MedianResult {
  final double median;
  final List<SolutionStep> steps;

  const MedianResult({required this.median, required this.steps});
}

class ModeResult {
  final double? mode; // null if no mode exists (all frequencies equal)
  final List<SolutionStep> steps;

  const ModeResult({required this.mode, required this.steps});
}

class CentralTendencyResult {
  final MeanResult mean;
  final MedianResult median;
  final ModeResult mode;

  const CentralTendencyResult({required this.mean, required this.median, required this.mode});
}
