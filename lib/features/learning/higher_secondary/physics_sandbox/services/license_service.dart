import 'dart:convert';
import 'dart:math';

import 'package:crypto/crypto.dart';
import 'package:shared_preferences/shared_preferences.dart';

class LicenseService {
  // Singleton pattern matching your app structure
  static final LicenseService instance = LicenseService._internal();
  LicenseService._internal();

  // ⚠️ Must match the MASTER_SECRET in your Python script exactly!
  static const String _masterSecret = "ShineAcademySuperSecretKey2026";
  static const String _activationKey = "is_app_activated";
  static const String _deviceIdKey = "device_id";

  bool _isActivated = false;
  bool get isActivated => true; // _isActivated;

  String _deviceId = '';

  /// Stable per-install code the student reads out to the administrator.
  String get deviceId => _deviceId;

  /// Initializes the service and checks if the app was previously activated
  Future<void> init() async {
    final prefs = await SharedPreferences.getInstance();
    _isActivated = prefs.getBool(_activationKey) ?? false;

    // Generated once per install and kept, so the unlock code stays valid.
    var stored = prefs.getString(_deviceIdKey);
    if (stored == null || stored.isEmpty) {
      stored = _generateDeviceId();
      await prefs.setString(_deviceIdKey, stored);
    }
    _deviceId = stored;
  }

  /// Builds a random 8-character device code (Crockford-style alphabet, so
  /// students never have to distinguish O from 0 or I from 1 over the phone).
  String _generateDeviceId() {
    const alphabet = '23456789ABCDEFGHJKMNPQRSTVWXYZ';
    final rng = Random.secure();
    return List.generate(8, (_) => alphabet[rng.nextInt(alphabet.length)]).join();
  }

  /// Generates the expected activation code for a given device ID using HMAC-SHA256
  String generateCodeForDevice(String deviceId) {
    final keyBytes = utf8.encode(_masterSecret);
    final deviceBytes = utf8.encode(deviceId.trim());

    final hmac = Hmac(sha256, keyBytes);
    final digest = hmac.convert(deviceBytes);

    // Take the first 8 characters and convert to uppercase (matching your Python script)
    return digest.toString().substring(0, 8).toUpperCase();
  }

  /// Validates the input activation code against this device's ID
  Future<bool> validateAndActivate(String inputCode) async {
    final expectedCode = generateCodeForDevice(_deviceId);


    if (expectedCode == inputCode.trim().toUpperCase()) {
      _isActivated = true;
      
      // Save activation state permanently on the device
      final prefs = await SharedPreferences.getInstance();
      await prefs.setBool(_activationKey, true);
      
      return true;
    }
    return false;
  }
}