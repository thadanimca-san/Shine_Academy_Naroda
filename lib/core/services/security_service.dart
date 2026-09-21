import 'dart:io';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';

class SecurityService {
  static const MethodChannel _channel = MethodChannel('shine.academy/security');

  /// Private constructor
  SecurityService._();

  /// Singleton instance
  static final SecurityService instance = SecurityService._();

  bool _isProtectionEnabled = false;

  bool get isProtectionEnabled => _isProtectionEnabled;

  /// Initializes the security service and optionally enables screen protection.
  /// Defaults to true for production, but can be set to false for testing.
  Future<void> init({bool enableProtection = true}) async {
    if (kIsWeb) return; // Not supported on Web
    if (!Platform.isAndroid && !Platform.isIOS) return;

    if (enableProtection) {
      await enableScreenProtection();
    } else {
      await disableScreenProtection();
    }
  }

  /// Enables screen protection (blocks screenshots and screen recording)
  Future<void> enableScreenProtection() async {
    if (kIsWeb || (!Platform.isAndroid && !Platform.isIOS)) return;
    
    try {
      await _channel.invokeMethod('setScreenProtection', {'enabled': true});
      _isProtectionEnabled = true;
      debugPrint("🔒 SecurityService: Screen protection ENABLED.");
    } on PlatformException catch (e) {
      debugPrint("🔒 SecurityService ERROR: Failed to enable screen protection: ${e.message}");
    }
  }

  /// Disables screen protection (allows screenshots and screen recording)
  Future<void> disableScreenProtection() async {
    if (kIsWeb || (!Platform.isAndroid && !Platform.isIOS)) return;

    try {
      await _channel.invokeMethod('setScreenProtection', {'enabled': false});
      _isProtectionEnabled = false;
      debugPrint("🔓 SecurityService: Screen protection DISABLED.");
    } on PlatformException catch (e) {
      debugPrint("🔓 SecurityService ERROR: Failed to disable screen protection: ${e.message}");
    }
  }
}
