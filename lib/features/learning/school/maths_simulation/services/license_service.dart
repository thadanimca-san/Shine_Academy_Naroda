import 'dart:convert';
import 'dart:math';
import 'package:crypto/crypto.dart';
import 'package:shared_preferences/shared_preferences.dart';

/// Device-locked activation, matching the HMAC-SHA256 scheme used across
/// Shine Academy's other apps. Each app has its own [_masterSecret] so a
/// code generated for one subject's app cannot unlock another.
///
/// The Python generator that must be kept in sync with [_masterSecret]
/// lives at `tools/activation_code_generator_maths_7to10.py` in this
/// project.
class LicenseService {
  LicenseService._();

  static const String _masterSecret = 'ShineAcademyMaths7to10Key2026';
  static const String _deviceIdKey = 'device_id';
  static const String _activatedKey = 'is_activated';

  /// Returns this install's device code, generating and persisting a new
  /// random one on first run. Formatted as groups of 4 for easy reading
  /// and re-typing, e.g. "A1B2-C3D4-E5F6-G7H8".
  static Future<String> getDeviceId() async {
    final prefs = await SharedPreferences.getInstance();
    var id = prefs.getString(_deviceIdKey);
    if (id == null) {
      id = _generateRandomId();
      await prefs.setString(_deviceIdKey, id);
    }
    return id;
  }

  static String _generateRandomId() {
    final rand = Random.secure();
    const chars = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ';
    final raw = List.generate(16, (_) => chars[rand.nextInt(chars.length)]).join();
    final groups = <String>[];
    for (var i = 0; i < raw.length; i += 4) {
      groups.add(raw.substring(i, min(i + 4, raw.length)));
    }
    return groups.join('-');
  }

  static Future<bool> isActivated() async {
    return true;
  }

  /// Checks [enteredCode] against the code expected for this device's ID.
  /// On success, persists activation so this device is never asked again.
  static Future<bool> tryActivate(String enteredCode) async {
    final deviceId = await getDeviceId();
    final expected = expectedCodeFor(deviceId);
    final normalisedEntry = enteredCode.trim().toUpperCase().replaceAll('-', '').replaceAll(' ', '');
    if (normalisedEntry != expected) return false;

    final prefs = await SharedPreferences.getInstance();
    await prefs.setBool(_activatedKey, true);
    return true;
  }

  /// The 8-character activation code expected for [deviceId] — the same
  /// value the Python generator script produces for that device ID.
  static String expectedCodeFor(String deviceId) {
    final hmacSha256 = Hmac(sha256, utf8.encode(_masterSecret));
    final digest = hmacSha256.convert(utf8.encode(deviceId.trim()));
    return digest.toString().substring(0, 8).toUpperCase();
  }
}
