import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';

/// TtsPlatformService — Shine Academy Naroda
/// 
/// Communicates with the native Android side (MainActivity.kt) via
/// MethodChannel to perform operations that require Android SDK access,
/// such as opening the TTS Settings page, querying installed engines,
/// and programmatically setting the default TTS engine.
///
/// This is the ONLY reliable way to reach TTS settings on AOSP-based
/// Android 13 digital classroom panels that have stripped Settings menus.
class TtsPlatformService {
  static final TtsPlatformService instance = TtsPlatformService._();
  TtsPlatformService._();

  static const MethodChannel _channel = MethodChannel('shine.academy/tts_settings');

  void _log(String msg) => debugPrint('[TtsPlatform] $msg');

  // ─────────────────────────────────────────────────────────────────────
  // Open TTS Settings Page directly from the app
  // Works on ALL Android 13 AOSP panels, even without standard Settings path
  // ─────────────────────────────────────────────────────────────────────
  Future<String> openTtsSettings() async {
    try {
      _log('Opening TTS Settings...');
      final result = await _channel.invokeMethod<String>('openTtsSettings');
      _log('openTtsSettings result: $result');
      return result ?? 'unknown';
    } catch (e) {
      _log('openTtsSettings failed: $e');
      return 'error: $e';
    }
  }

  // ─────────────────────────────────────────────────────────────────────
  // Open Language & Input Settings (AOSP path to TTS on many panels)
  // ─────────────────────────────────────────────────────────────────────
  Future<String> openLanguageSettings() async {
    try {
      _log('Opening Language & Input Settings...');
      final result = await _channel.invokeMethod<String>('openLanguageSettings');
      _log('openLanguageSettings result: $result');
      return result ?? 'unknown';
    } catch (e) {
      _log('openLanguageSettings failed: $e');
      return 'error: $e';
    }
  }

  // ─────────────────────────────────────────────────────────────────────
  // Get all installed TTS engines on the device
  // ─────────────────────────────────────────────────────────────────────
  Future<List<String>> getInstalledEngines() async {
    try {
      _log('Getting installed TTS engines...');
      final result = await _channel.invokeListMethod<String>('getInstalledEngines');
      _log('Installed engines: $result');
      return result ?? [];
    } catch (e) {
      _log('getInstalledEngines failed: $e');
      return [];
    }
  }

  // ─────────────────────────────────────────────────────────────────────
  // Get the current default TTS engine package name
  // ─────────────────────────────────────────────────────────────────────
  Future<String> getDefaultEngine() async {
    try {
      final result = await _channel.invokeMethod<String>('getDefaultEngine');
      _log('Default engine: $result');
      return result ?? 'not_set';
    } catch (e) {
      _log('getDefaultEngine failed: $e');
      return 'error: $e';
    }
  }

  // ─────────────────────────────────────────────────────────────────────
  // Try to programmatically set Google TTS as default engine
  // Returns true if succeeded, false if needs manual action (ADB)
  // ─────────────────────────────────────────────────────────────────────
  Future<bool> trySetGoogleTtsEngine() async {
    try {
      _log('Attempting to set Google TTS as default engine...');
      final result = await _channel.invokeMethod<String>('setGoogleTtsEngine');
      _log('setGoogleTtsEngine result: $result');
      return result == 'ENGINE_SET_OK';
    } on PlatformException catch (e) {
      _log('setGoogleTtsEngine PlatformException: ${e.code} — ${e.message}');
      // SECURITY_EXCEPTION means needs ADB — not an app crash
      return false;
    } catch (e) {
      _log('setGoogleTtsEngine error: $e');
      return false;
    }
  }
}
