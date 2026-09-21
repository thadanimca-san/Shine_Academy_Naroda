import 'package:flutter/foundation.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Local-first progress store. Keyed by stable topic ids so the same data
/// shape can later sync to a backend without migration.
class ProgressService extends ChangeNotifier {
  ProgressService._();
  static final ProgressService instance = ProgressService._();

  static const _kVisited = 'progress.visited';
  static const _kLastTopic = 'progress.lastTopic';
  static const _kFirstOpen = 'progress.firstOpenMillis';

  SharedPreferences? _prefs;
  Set<String> _visited = {};
  String? _lastTopicId;

  Future<void> init() async {
    _prefs = await SharedPreferences.getInstance();
    _visited = (_prefs!.getStringList(_kVisited) ?? const []).toSet();
    _lastTopicId = _prefs!.getString(_kLastTopic);
    if (_prefs!.getInt(_kFirstOpen) == null) {
      await _prefs!.setInt(_kFirstOpen, DateTime.now().millisecondsSinceEpoch);
    }
    notifyListeners();
  }

  bool get isFirstSession => _visited.isEmpty;
  String? get lastTopicId => _lastTopicId;
  int get visitedCount => _visited.length;
  bool isVisited(String topicId) => _visited.contains(topicId);

  Future<void> markVisited(String topicId) async {
    _lastTopicId = topicId;
    _visited.add(topicId);
    notifyListeners();
    await _prefs?.setStringList(_kVisited, _visited.toList());
    await _prefs?.setString(_kLastTopic, topicId);
  }

  int visitedInChapter(Iterable<String> topicIds) =>
      topicIds.where(_visited.contains).length;
}
