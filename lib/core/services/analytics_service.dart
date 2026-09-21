import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

class AnalyticsService {
  static final AnalyticsService instance = AnalyticsService._internal();

  AnalyticsService._internal();

  // Observable state for UI updates
  final ValueNotifier<int> dailyActiveMinutesNotifier = ValueNotifier<int>(0);
  final ValueNotifier<Map<String, int>> timeSpentPerSubjectNotifier = ValueNotifier<Map<String, int>>({});
  final ValueNotifier<Map<String, List<double>>> examScoresNotifier = ValueNotifier<Map<String, List<double>>>({});

  // Keys
  static const String _dailyMinutesKeyPrefix = 'analytics_daily_mins_';
  static const String _subjectTimeKey = 'analytics_subject_time';
  static const String _examScoresKey = 'analytics_exam_scores';

  String _getTodayKey() {
    final now = DateTime.now();
    return '$_dailyMinutesKeyPrefix${now.year}_${now.month}_${now.day}';
  }

  Future<void> init() async {
    try {
      final prefs = await SharedPreferences.getInstance();
      
      // Load daily active minutes
      dailyActiveMinutesNotifier.value = prefs.getInt(_getTodayKey()) ?? 0;
      
      // Load subject time
      final subjectTimeStr = prefs.getString(_subjectTimeKey);
      if (subjectTimeStr != null) {
        final Map<String, dynamic> decoded = json.decode(subjectTimeStr);
        timeSpentPerSubjectNotifier.value = decoded.map((k, v) => MapEntry(k, v as int));
      }

      // Load exam scores
      final scoresStr = prefs.getString(_examScoresKey);
      if (scoresStr != null) {
        final Map<String, dynamic> decoded = json.decode(scoresStr);
        final Map<String, List<double>> parsedScores = {};
        for (var entry in decoded.entries) {
          final List<dynamic> listData = entry.value;
          parsedScores[entry.key] = listData.map((e) => (e as num).toDouble()).toList();
        }
        examScoresNotifier.value = parsedScores;
      }
      
      debugPrint("AnalyticsService initialized.");
    } catch (e) {
      debugPrint("AnalyticsService init error: $e");
    }
  }

  /// Logs time spent learning, which adds to both the daily total and the subject total.
  Future<void> logTimeSpent(String subject, int minutes) async {
    if (minutes <= 0) return;
    
    final prefs = await SharedPreferences.getInstance();
    
    // Update daily total
    final todayKey = _getTodayKey();
    int currentDaily = prefs.getInt(todayKey) ?? 0;
    currentDaily += minutes;
    await prefs.setInt(todayKey, currentDaily);
    dailyActiveMinutesNotifier.value = currentDaily;

    // Update subject total
    final Map<String, int> subjectMap = Map.from(timeSpentPerSubjectNotifier.value);
    subjectMap[subject] = (subjectMap[subject] ?? 0) + minutes;
    await prefs.setString(_subjectTimeKey, json.encode(subjectMap));
    timeSpentPerSubjectNotifier.value = subjectMap;
  }

  /// Logs a score (percentage 0.0 to 100.0) for a specific exam or assessment type.
  Future<void> logAssessmentScore(String examType, double percentage) async {
    final prefs = await SharedPreferences.getInstance();
    
    final Map<String, List<double>> scoresMap = Map.from(examScoresNotifier.value);
    if (!scoresMap.containsKey(examType)) {
      scoresMap[examType] = [];
    }
    
    scoresMap[examType]!.add(percentage);
    
    // Keep only the last 10 scores per type to prevent local storage bloat
    if (scoresMap[examType]!.length > 10) {
      scoresMap[examType]!.removeAt(0);
    }
    
    await prefs.setString(_examScoresKey, json.encode(scoresMap));
    examScoresNotifier.value = scoresMap;
  }
}
