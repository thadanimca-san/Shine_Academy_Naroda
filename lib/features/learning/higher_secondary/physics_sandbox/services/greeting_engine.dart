import 'profile_service.dart';
import 'progress_service.dart';

/// Generates the home-screen greeting: personal, physics-flavored, and
/// different depending on when you show up — never a generic "Hello user".
class GreetingEngine {
  const GreetingEngine._();

  static ({String headline, String subline}) compose({
    required ProfileService profile,
    required ProgressService progress,
    String? lastTopicTitle,
    DateTime? now,
  }) {
    final t = now ?? DateTime.now();
    final name = profile.isOnboarded ? profile.firstName : 'physicist';
    final pool = _headlines(t.hour, name);
    final headline = pool[t.day % pool.length];

    final String subline;
    if (progress.isFirstSession) {
      subline =
          'Everything here is a lab, not a lecture. Poke it, break it, ask it why.';
    } else if (lastTopicTitle != null) {
      subline = _continuations(lastTopicTitle, profile.examLabel)[
          t.day % _continuations(lastTopicTitle, profile.examLabel).length];
    } else {
      subline =
          '${progress.visitedCount} topics down. ${profile.examLabel} won\'t know what hit it.';
    }
    return (headline: headline, subline: subline);
  }

  static List<String> _headlines(int hour, String name) {
    if (hour >= 4 && hour < 12) {
      return [
        'Rise and accelerate, $name',
        'Fresh coffee, fresh frames of reference, $name',
        'Morning, $name — the universe kept moving all night',
        '$name, today has excellent initial conditions',
      ];
    }
    if (hour >= 12 && hour < 17) {
      return [
        'Peak momentum hours, $name',
        'Afternoon, $name — entropy can wait',
        '$name, the day\'s at max amplitude',
        'Back at the bench, $name?',
      ];
    }
    if (hour >= 17 && hour < 22) {
      return [
        'Golden hour physics, $name',
        'Evening, $name — prime time for problem solving',
        '$name, the best derivations happen after sunset',
        'Sun\'s down, curiosity\'s up, $name',
      ];
    }
    return [
      'Burning the midnight photons, $name?',
      '$name, the stars are out — good company for gravitation',
      'Quiet hours, deep focus, $name',
      'Night shift at the lab, $name',
    ];
  }

  static List<String> _continuations(String topic, String exam) {
    return [
      'You left $topic mid-experiment. It\'s still waiting on the bench.',
      '$topic isn\'t finished with you yet — one more run?',
      'Last session: $topic. Nail it today and it\'s one less surprise in $exam.',
    ];
  }
}
