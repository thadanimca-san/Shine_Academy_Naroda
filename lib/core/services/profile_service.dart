import 'package:shared_preferences/shared_preferences.dart';

class ProfileService {
  static const String _keyIsProfileSet = 'isProfileSet';
  static const String _keyRole = 'userRole'; // Student, Teacher, Parent
  static const String _keyStage = 'educationalStage'; // Primary, Secondary, Higher Secondary, Competitive
  static const String _keyClass = 'userClass'; // e.g., Class 10, Class 12 Commerce
  static const String _keyBoard = 'userBoard'; // NCERT, GSEB

  static Future<bool> isProfileSet() async {
    final prefs = await SharedPreferences.getInstance();
    return prefs.getBool(_keyIsProfileSet) ?? false;
  }

  static Future<void> saveProfile({
    required String role,
    required String stage,
    required String userClass,
    required String board,
  }) async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.setString(_keyRole, role);
    await prefs.setString(_keyStage, stage);
    await prefs.setString(_keyClass, userClass);
    await prefs.setString(_keyBoard, board);
    await prefs.setBool(_keyIsProfileSet, true);
  }

  static Future<Map<String, String>> getProfile() async {
    final prefs = await SharedPreferences.getInstance();
    return {
      'role': prefs.getString(_keyRole) ?? '',
      'stage': prefs.getString(_keyStage) ?? '',
      'class': prefs.getString(_keyClass) ?? '',
      'board': prefs.getString(_keyBoard) ?? '',
    };
  }

  static Future<void> clearProfile() async {
    final prefs = await SharedPreferences.getInstance();
    await prefs.clear();
  }
}
