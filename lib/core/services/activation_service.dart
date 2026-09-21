import 'dart:io';
import 'dart:math';
import 'dart:convert';
import 'package:crypto/crypto.dart';
import 'package:shared_preferences/shared_preferences.dart';

class ActivationService {
  static const String _keyActivated = 'is_activated';
  static const String _keyDeviceCode = 'device_code';
  static const String _secretSalt = 'ShineAcademyEduOSKey2026'; // Match Passmaker Key

  static bool _isActivated = false;
  static String _deviceCode = '';

  static bool get isActivated => _isActivated;
  static String get deviceCode => _deviceCode;

  static Future<void> initialize() async {
    // 1. Bypass completely on Desktop OS (Development Mode)
    if (Platform.isLinux || Platform.isWindows || Platform.isMacOS) {
      _isActivated = true;
      return;
    }

    // 2. Android/iOS Logic
    final prefs = await SharedPreferences.getInstance();
    _isActivated = prefs.getBool(_keyActivated) ?? false;
    
    _deviceCode = prefs.getString(_keyDeviceCode) ?? '';
    if (_deviceCode.isEmpty) {
      _deviceCode = _generateRandomDeviceCode();
      await prefs.setString(_keyDeviceCode, _deviceCode);
    }
  }

  static String _generateRandomDeviceCode() {
    const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789';
    final random = Random();
    return String.fromCharCodes(Iterable.generate(
      8, (_) => chars.codeUnitAt(random.nextInt(chars.length))));
  }

  static Future<bool> activate(String enteredCode) async {
    final expectedCode = _generateActivationCode(_deviceCode);
    if (enteredCode.trim().toUpperCase() == expectedCode) {
      final prefs = await SharedPreferences.getInstance();
      await prefs.setBool(_keyActivated, true);
      _isActivated = true;
      return true;
    }
    return false;
  }

  // The logic that generates the activation code based on the device code.
  static String _generateActivationCode(String deviceCode) {
    final keyBytes = utf8.encode(_secretSalt);
    final messageBytes = utf8.encode(deviceCode);
    
    final hmacSha256 = Hmac(sha256, keyBytes);
    final digest = hmacSha256.convert(messageBytes);
    
    // Take the first 8 characters of the hex hash and make it uppercase
    return digest.toString().substring(0, 8).toUpperCase();
  }
}
