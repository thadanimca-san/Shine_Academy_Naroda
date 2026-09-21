import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

class GamificationService {
  static final GamificationService instance = GamificationService._internal();

  GamificationService._internal();

  // Observable state for UI updates
  final ValueNotifier<int> xpNotifier = ValueNotifier<int>(0);
  final ValueNotifier<int> levelNotifier = ValueNotifier<int>(1);
  final ValueNotifier<int> coinsNotifier = ValueNotifier<int>(0);
  final ValueNotifier<int> streakNotifier = ValueNotifier<int>(0);

  // Constants
  static const int xpPerLevel = 1000;
  static const String _xpKey = 'gamification_xp';
  static const String _levelKey = 'gamification_level';
  static const String _coinsKey = 'gamification_coins';
  static const String _lastActiveKey = 'gamification_last_active';
  static const String _streakKey = 'gamification_streak';

  Future<void> init() async {
    final prefs = await SharedPreferences.getInstance();
    xpNotifier.value = prefs.getInt(_xpKey) ?? 0;
    levelNotifier.value = prefs.getInt(_levelKey) ?? 1;
    coinsNotifier.value = prefs.getInt(_coinsKey) ?? 0;
    
    // Streak calculation
    _calculateStreak(prefs);
  }

  void _calculateStreak(SharedPreferences prefs) {
    final lastActiveStr = prefs.getString(_lastActiveKey);
    final now = DateTime.now();
    final today = DateTime(now.year, now.month, now.day);
    
    int currentStreak = prefs.getInt(_streakKey) ?? 0;

    if (lastActiveStr != null) {
      final lastActiveDate = DateTime.parse(lastActiveStr);
      final lastActiveDay = DateTime(lastActiveDate.year, lastActiveDate.month, lastActiveDate.day);
      
      final difference = today.difference(lastActiveDay).inDays;
      
      if (difference == 1) {
        // Active yesterday, streak continues
        currentStreak += 1;
      } else if (difference > 1) {
        // Missed a day, reset streak
        currentStreak = 1;
      }
      // If difference == 0, they already played today, streak remains the same
    } else {
      // First time playing
      currentStreak = 1;
    }

    prefs.setString(_lastActiveKey, today.toIso8601String());
    prefs.setInt(_streakKey, currentStreak);
    streakNotifier.value = currentStreak;
  }

  /// Adds XP and returns true if the user leveled up!
  Future<bool> addXp(int amount) async {
    final prefs = await SharedPreferences.getInstance();
    
    // Apply streak multiplier
    int multiplier = 1;
    if (streakNotifier.value >= 30) {
      multiplier = 2;
    } else if (streakNotifier.value >= 7) {
      amount = (amount * 1.5).round();
    } else {
      amount = amount * multiplier;
    }

    int newXp = xpNotifier.value + amount;
    
    // Check for level up
    int oldLevel = levelNotifier.value;
    int newLevel = (newXp ~/ xpPerLevel) + 1; // e.g. 0-999 is Lvl 1. 1000 is Lvl 2.
    
    bool leveledUp = newLevel > oldLevel;

    xpNotifier.value = newXp;
    levelNotifier.value = newLevel;

    await prefs.setInt(_xpKey, newXp);
    if (leveledUp) {
      await prefs.setInt(_levelKey, newLevel);
    }
    
    return leveledUp;
  }

  // --- Specific XP Triggers ---

  /// 50 XP for getting a question right on the first try
  Future<bool> addKnowledgeCheckXp() async {
    return await addXp(50);
  }

  /// 10 XP for viewing/reading a block (not yet triggered automatically to avoid spam)
  Future<bool> addBlockReadXp() async {
    return await addXp(10);
  }

  /// 500 XP and 50 Coins for finishing a chapter
  Future<bool> addChapterCompleteXp() async {
    await addCoins(50);
    return await addXp(500);
  }

  Future<void> addCoins(int amount) async {
    final prefs = await SharedPreferences.getInstance();
    int newCoins = coinsNotifier.value + amount;
    coinsNotifier.value = newCoins;
    await prefs.setInt(_coinsKey, newCoins);
  }
}
