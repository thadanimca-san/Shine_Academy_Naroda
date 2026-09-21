import 'dart:convert';

import 'package:shared_preferences/shared_preferences.dart';

/// Per-topic practice stats for one student's device: how many questions
/// they've attempted and how many they got right, kept purely on-device
/// (no account/login needed) so it works offline and needs no backend.
class TopicProgress {
  final String topicKey;
  final int attempted;
  final int correct;

  const TopicProgress({required this.topicKey, required this.attempted, required this.correct});

  double get accuracy => attempted == 0 ? 0 : correct / attempted;

  Map<String, dynamic> toJson() => {'topicKey': topicKey, 'attempted': attempted, 'correct': correct};

  factory TopicProgress.fromJson(Map<String, dynamic> json) => TopicProgress(
        topicKey: json['topicKey'] as String,
        attempted: json['attempted'] as int,
        correct: json['correct'] as int,
      );
}

/// Records and reads practice progress per topic, so students can see
/// which topics they're weak in and get pointed back to practice them.
class ProgressService {
  ProgressService._();

  static const _storageKey = 'topic_progress_v1';

  static const topicCentralTendency = 'central_tendency';
  static const topicDispersion = 'dispersion';
  static const topicCorrelation = 'correlation';
  static const topicIndexNumbers = 'index_numbers';
  static const topicRegression = 'regression';

  static const topicLabels = {
    topicCentralTendency: 'Measures of Central Tendency',
    topicDispersion: 'Measures of Dispersion',
    topicCorrelation: 'Correlation',
    topicIndexNumbers: 'Index Numbers',
    topicRegression: 'Regression Analysis',
  };

  static Future<void> recordAttempt({required String topicKey, required bool wasCorrect}) async {
    final prefs = await SharedPreferences.getInstance();
    final all = await _readAll(prefs);
    final existing = all[topicKey] ?? TopicProgress(topicKey: topicKey, attempted: 0, correct: 0);
    all[topicKey] = TopicProgress(
      topicKey: topicKey,
      attempted: existing.attempted + 1,
      correct: existing.correct + (wasCorrect ? 1 : 0),
    );
    await _writeAll(prefs, all);
  }

  static Future<Map<String, TopicProgress>> getAllProgress() async {
    final prefs = await SharedPreferences.getInstance();
    return _readAll(prefs);
  }

  static Future<Map<String, TopicProgress>> _readAll(SharedPreferences prefs) async {
    final raw = prefs.getString(_storageKey);
    if (raw == null) return {};
    final decoded = jsonDecode(raw) as Map<String, dynamic>;
    return decoded.map((key, value) => MapEntry(key, TopicProgress.fromJson(value as Map<String, dynamic>)));
  }

  static Future<void> _writeAll(SharedPreferences prefs, Map<String, TopicProgress> all) async {
    final encoded = jsonEncode(all.map((key, value) => MapEntry(key, value.toJson())));
    await prefs.setString(_storageKey, encoded);
  }
}
