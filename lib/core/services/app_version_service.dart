import 'package:flutter/foundation.dart';
import 'package:package_info_plus/package_info_plus.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Tells other services whether this is the first launch after the app was
/// installed or updated, so they can refresh anything they copied out of the
/// bundled assets (cached content, the dictionary database, ...).
class AppVersionService {
  AppVersionService._();

  static const String _lastLaunchedVersionKey = 'last_launched_app_version';

  static Future<void>? _initFuture;
  static String _currentVersion = 'unknown';
  static bool _isNewVersion = true;

  /// The installed version, e.g. "1.0.3+12".
  static String get currentVersion => _currentVersion;

  /// True on the first launch after install or update.
  /// Stays true for the whole of that launch.
  static bool get isNewVersion => _isNewVersion;

  /// Safe to call many times; the work runs only once per launch.
  static Future<void> init() => _initFuture ??= _detectVersionChange();

  static Future<void> _detectVersionChange() async {
    try {
      final info = await PackageInfo.fromPlatform();
      _currentVersion = '${info.version}+${info.buildNumber}';

      final prefs = await SharedPreferences.getInstance();
      final lastVersion = prefs.getString(_lastLaunchedVersionKey);
      _isNewVersion = lastVersion != _currentVersion;
      if (_isNewVersion) {
        await prefs.setString(_lastLaunchedVersionKey, _currentVersion);
        debugPrint('AppVersionService: new app version $lastVersion -> $_currentVersion');
      }
    } catch (e) {
      // If we cannot tell, assume it is new: refreshing caches is always safe,
      // showing stale content is not.
      _isNewVersion = true;
      debugPrint('AppVersionService: could not read app version, treating as new. Error: $e');
    }
  }
}
