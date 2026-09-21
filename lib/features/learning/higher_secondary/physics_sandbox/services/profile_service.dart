import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

enum ExamTarget { jee, neet, both }

enum ClassLevel { eleven, twelve, dropper }

/// Who is learning. Local-first; same shape syncs to a backend later.
class ProfileService extends ChangeNotifier {
  ProfileService._();
  static final ProfileService instance = ProfileService._();

  static const _kName = 'profile.name';
  static const _kExam = 'profile.exam';
  static const _kClass = 'profile.class';

  SharedPreferences? _prefs;
  String? _name;
  ExamTarget _exam = ExamTarget.both;
  ClassLevel _classLevel = ClassLevel.eleven;

  Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();
    _name = _prefs!.getString(_kName);
    _exam = ExamTarget.values[_prefs!.getInt(_kExam) ?? ExamTarget.both.index];
    _classLevel =
        ClassLevel.values[_prefs!.getInt(_kClass) ?? ClassLevel.eleven.index];
    notifyListeners();
  }

  bool get isOnboarded => _name != null && _name!.trim().isNotEmpty;
  String get name => _name ?? '';
  String get firstName => name.trim().split(RegExp(r'\s+')).first;
  ExamTarget get exam => _exam;
  ClassLevel get classLevel => _classLevel;

  String get examLabel => switch (_exam) {
        ExamTarget.jee => 'JEE',
        ExamTarget.neet => 'NEET',
        ExamTarget.both => 'JEE + NEET',
      };

  Future<void> save({
    required String name,
    required ExamTarget exam,
    required ClassLevel classLevel,
  }) async {
    _name = name.trim();
    _exam = exam;
    _classLevel = classLevel;
    notifyListeners();
    await _prefs?.setString(_kName, _name!);
    await _prefs?.setInt(_kExam, exam.index);
    await _prefs?.setInt(_kClass, classLevel.index);
  }
}
