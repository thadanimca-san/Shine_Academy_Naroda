import 'package:flutter/foundation.dart';
import 'package:audioplayers/audioplayers.dart';
import 'package:flutter_tts/flutter_tts.dart';

/// SpeechService — Shine Academy Naroda
/// Version 4.0 — Digital Panel Bulletproof Edition
///
/// ROOT CAUSE FIX (August 2026):
/// The previous version created FlutterTts() at class-field level, which means
/// the TTS object was instantiated at app startup — BEFORE the Google TTS APK
/// (com.google.android.tts) had fully registered its service with Android 13.
/// On digital panels where Google TTS was freshly installed, getEngines() would
/// return an empty list, the engine binding would silently fail, and all speak()
/// calls would produce no output.
///
/// FIX: FlutterTts is now created LAZILY inside _init(), allowing the Android
/// TTS manager to fully register the Google TTS service first.
///
/// ADDITIONAL FIXES:
/// - Multi-attempt engine detection (retries after 1s and 3s delays)
/// - Auto-reinit on speak() failure (disposed/stale TTS instance recovery)
/// - Full diagnostic logging at every step for classroom debugging
/// - Fallback chain: Google TTS → Samsung TTS → any available engine → system default
/// - setAwaitSpeakCompletion(false) to prevent stream lock on AOSP panels
class SpeechService {
  SpeechService._();
  static final SpeechService instance = SpeechService._();

  final AudioPlayer _player = AudioPlayer();

  // ✅ CRITICAL FIX: FlutterTts is NOT created at field level.
  // It is created lazily inside _init() after the engine is ready.
  FlutterTts? _tts;

  VoidCallback? _onComplete;
  bool _isInit = false;
  bool _isInitializing = false;

  // The final resolved language/locale used for all TTS calls.
  String _resolvedLanguage = 'en-IN';
  String _resolvedEngine = '';

  // ============================================================
  // DIAGNOSTIC LOGGER
  // All messages tagged [TTS] so you can grep logcat for them:
  //   adb logcat | grep TTS
  // ============================================================
  void _log(String message) {
    debugPrint('[TTS] $message');
  }

  // ============================================================
  // LAZY INIT — safe to call multiple times
  // ============================================================
  Future<void> _init() async {
    if (_isInit) return;
    if (_isInitializing) {
      // Wait for the ongoing init to finish instead of running twice
      int waited = 0;
      while (_isInitializing && waited < 5000) {
        await Future.delayed(const Duration(milliseconds: 100));
        waited += 100;
      }
      return;
    }
    _isInitializing = true;

    _log('=== SpeechService Init START ===');

    // ---- 1. AudioPlayer setup ----
    try {
      _player.onPlayerComplete.listen((_) => _onComplete?.call());
      _log('AudioPlayer initialized OK');
    } catch (e) {
      _log('AudioPlayer init error: $e');
    }

    // ---- 2. Create FlutterTts LAZILY (the core fix) ----
    try {
      _tts = FlutterTts();
      _log('FlutterTts instance created');
    } catch (e) {
      _log('FATAL: FlutterTts() constructor threw: $e');
      _isInitializing = false;
      return;
    }

    // ---- 3. Detect and bind the best available TTS engine ----
    await _bindBestEngine();

    // ---- 4. Detect and set the best available language ----
    await _bindBestLanguage();

    // ---- 5. Set speech parameters ----
    await _applyDefaultSettings();

    // ---- 6. Set callbacks ----
    try {
      _tts!.setCompletionHandler(() {
        _log('TTS: speak() completed');
        _onComplete?.call();
      });
      _tts!.setErrorHandler((msg) {
        _log('TTS ERROR from engine: $msg');
      });
      _tts!.setStartHandler(() {
        _log('TTS: speak() started successfully');
      });
      _tts!.setCancelHandler(() {
        _log('TTS: speak() was cancelled');
      });
    } catch (e) {
      _log('Error setting TTS callbacks: $e');
    }

    _isInit = true;
    _isInitializing = false;
    _log('=== SpeechService Init COMPLETE. Engine: "$_resolvedEngine" | Language: "$_resolvedLanguage" ===');
  }

  // ============================================================
  // ENGINE BINDING — tries Google TTS, fallback to any engine
  // ============================================================
  Future<void> _bindBestEngine() async {
    if (_tts == null) return;

    // Try up to 3 times with increasing delays.
    // This handles the case where Google TTS APK was just installed
    // and the Android TTS service manager hasn't fully registered it yet.
    for (int attempt = 1; attempt <= 3; attempt++) {
      try {
        _log('Engine detection attempt $attempt...');
        final List<dynamic>? engines = await _tts!.getEngines;

        if (engines == null || engines.isEmpty) {
          _log('Attempt $attempt: No TTS engines reported. Waiting...');
          if (attempt < 3) await Future.delayed(Duration(seconds: attempt));
          continue;
        }

        _log('Attempt $attempt: Found ${engines.length} engine(s): $engines');

        // Priority order of engines to try
        final preferredEngines = [
          'com.google.android.tts',           // Google TTS (your installed APK)
          'com.samsung.SMT',                  // Samsung TTS
          'com.svox.pico',                    // SVOX Pico (built-in AOSP)
          'com.huawei.hiai.tts.engine',       // Huawei
        ];

        String? chosenEngine;
        for (final preferred in preferredEngines) {
          if (engines.any((e) => e.toString().startsWith(preferred) ||
              e.toString() == preferred)) {
            chosenEngine = engines.firstWhere(
              (e) => e.toString().startsWith(preferred) || e.toString() == preferred,
            ).toString();
            break;
          }
        }

        // If no preferred engine found, just use the first available
        chosenEngine ??= engines.first.toString();

        _log('Binding to engine: "$chosenEngine"');
        try {
          await _tts!.setEngine(chosenEngine);
          _resolvedEngine = chosenEngine;
          _log('Engine set successfully: "$chosenEngine"');
          return; // Success — stop retrying
        } catch (e) {
          _log('Failed to set engine "$chosenEngine": $e');
          // On failure, try the next engine in the list (fallback)
          for (final eng in engines) {
            if (eng.toString() != chosenEngine) {
              try {
                _log('Trying fallback engine: "${eng.toString()}"');
                await _tts!.setEngine(eng.toString());
                _resolvedEngine = eng.toString();
                _log('Fallback engine set: "${eng.toString()}"');
                return;
              } catch (e2) {
                _log('Fallback engine "${eng.toString()}" also failed: $e2');
              }
            }
          }
        }
      } catch (e) {
        _log('Attempt $attempt: getEngines() threw: $e');
        if (attempt < 3) await Future.delayed(Duration(seconds: attempt));
      }
    }

    _log('WARNING: Could not set any specific engine. Using system default.');
    _resolvedEngine = 'system_default';
  }

  // ============================================================
  // LANGUAGE BINDING — tries en-IN, en-US, any English, then any language
  // ============================================================
  Future<void> _bindBestLanguage() async {
    if (_tts == null) return;

    try {
      _log('Detecting available languages...');
      final List<dynamic>? languages = await _tts!.getLanguages;

      if (languages == null || languages.isEmpty) {
        _log('WARNING: No languages returned. Attempting blind en-US set...');
        try {
          await _tts!.setLanguage('en-US');
          _resolvedLanguage = 'en-US';
          _log('Blind en-US set succeeded');
        } catch (e) {
          _log('Blind en-US set also failed: $e');
        }
        return;
      }

      _log('Available languages (${languages.length}): $languages');

      // Priority order of languages
      final preferredLanguages = ['en-IN', 'en-GB', 'en-US', 'en-AU', 'en-CA'];

      String? chosen;
      for (final lang in preferredLanguages) {
        final match = languages.cast<String>().firstWhere(
          (l) => l.replaceAll('_', '-').toLowerCase() == lang.toLowerCase(),
          orElse: () => '',
        );
        if (match.isNotEmpty) {
          chosen = match;
          break;
        }
      }

      // If no preferred language, find any English
      if (chosen == null) {
        final anyEnglish = languages
            .where((l) => l.toString().toLowerCase().startsWith('en'))
            .toList();
        if (anyEnglish.isNotEmpty) {
          chosen = anyEnglish.first.toString();
          _log('No preferred English found, using: "$chosen"');
        }
      }

      // Last resort: use the first available language
      chosen ??= languages.first.toString();

      _log('Setting language to: "$chosen"');
      await _tts!.setLanguage(chosen);
      _resolvedLanguage = chosen;
      _log('Language set successfully: "$_resolvedLanguage"');
    } catch (e) {
      _log('Language detection failed: $e. Attempting blind en-US...');
      try {
        await _tts!.setLanguage('en-US');
        _resolvedLanguage = 'en-US';
        _log('Blind en-US fallback succeeded');
      } catch (e2) {
        _log('Blind en-US fallback also failed: $e2');
      }
    }
  }

  // ============================================================
  // DEFAULT SETTINGS
  // ============================================================
  Future<void> _applyDefaultSettings() async {
    if (_tts == null) return;
    try {
      await _tts!.setVolume(1.0);
      _log('Volume set to 1.0');
    } catch (e) {
      _log('setVolume error: $e');
    }
    try {
      await _tts!.setSpeechRate(0.45);
      _log('SpeechRate set to 0.45');
    } catch (e) {
      _log('setSpeechRate error: $e');
    }
    try {
      await _tts!.setPitch(1.0);
      _log('Pitch set to 1.0');
    } catch (e) {
      _log('setPitch error: $e');
    }
    // IMPORTANT: Do NOT call setAwaitSpeakCompletion(true) on AOSP panels.
    // Many Android 13 digital panel firmwares do not fire the completion
    // callback, causing speak() to hang indefinitely.
    try {
      await _tts!.setSharedInstance(true);
      _log('SharedInstance set to true');
    } catch (e) {
      _log('setSharedInstance error (harmless on non-iOS): $e');
    }
  }

  // ============================================================
  // REINIT — called when speak() silently fails
  // ============================================================
  Future<void> _reinit() async {
    _log('--- REINIT triggered ---');
    _isInit = false;
    _isInitializing = false;
    try {
      await _tts?.stop();
    } catch (_) {}
    _tts = null;
    await _init();
  }

  // ============================================================
  // PUBLIC API
  // ============================================================

  /// Play an MP3 file bundled in the assets directory.
  Future<void> playAudio(String assetPath) async {
    await _init();
    try {
      await _player.stop();
      try {
        await _tts?.stop();
      } catch (_) {}

      String sourcePath = assetPath;
      if (sourcePath.startsWith('assets/')) {
        sourcePath = sourcePath.substring(7);
      }

      _log('Playing audio asset: $sourcePath');
      await _player.play(AssetSource(sourcePath));
    } catch (e) {
      _log('playAudio failed for "$assetPath": $e');
    }
  }

  /// Speak text using the best available TTS engine.
  /// Falls back to reinit and retry once if the first attempt fails.
  Future<void> speak(String text) async {
    if (text.trim().isEmpty) {
      _log('speak() called with empty text, ignoring');
      return;
    }

    await _init();

    if (_tts == null) {
      _log('speak() aborted: _tts is null after init (engine not available)');
      return;
    }

    _log('speak() called. Engine: "$_resolvedEngine" | Lang: "$_resolvedLanguage" | Text: "${text.substring(0, text.length.clamp(0, 60))}..."');

    try {
      await _player.stop();
    } catch (_) {}

    try {
      await _tts!.stop();
    } catch (e) {
      _log('stop() before speak threw: $e');
    }

    // Re-apply language before every speak() call.
    // Some Android 13 panel firmware resets TTS state between calls.
    try {
      await _tts!.setLanguage(_resolvedLanguage);
    } catch (e) {
      _log('setLanguage before speak failed: $e');
    }
    
    // ALWAYS reset speech rate to default (0.45) before standard speak
    // to prevent bleed-over from speakWithSettings
    try {
      await _tts!.setSpeechRate(0.45);
    } catch (e) {
      _log('setSpeechRate before speak failed: $e');
    }

    try {
      final result = await _tts!.speak(text);
      _log('speak() returned: $result (1=success, 0=fail on Android)');

      // On Android, flutter_tts.speak() returns 1 on success, 0 on failure.
      // If it returns 0, the engine is in a bad state — reinit and retry once.
      if (result != null && result == 0) {
        _log('speak() returned 0 (failure). Triggering reinit + retry...');
        await _reinit();
        if (_tts != null) {
          try {
            final result2 = await _tts!.speak(text);
            _log('Retry speak() returned: $result2');
          } catch (e2) {
            _log('Retry speak() also threw: $e2');
          }
        }
      }
    } catch (e) {
      _log('speak() threw exception: $e. Triggering reinit + retry...');
      await _reinit();
      if (_tts != null) {
        try {
          await _tts!.speak(text);
          _log('Retry speak() after exception succeeded');
        } catch (e2) {
          _log('Retry speak() after exception ALSO failed: $e2');
          _log('FINAL FAILURE: TTS is not working on this device/panel.');
          _log('Please check: 1) Google TTS APK is installed & enabled in Settings > Apps');
          _log('              2) Settings > Accessibility > Text-to-Speech Output');
          _log('              3) Try rebooting the panel after installing Google TTS');
        }
      }
    }
  }

  /// Speak text with custom pitch, speech rate, and language.
  /// All parameters are optional — defaults to normal Indian English.
  Future<void> speakWithSettings({
    required String text,
    double pitch = 1.0,
    double speechRate = 0.45,
    String? language,
  }) async {
    if (text.trim().isEmpty) return;
    await _init();
    if (_tts == null) {
      _log('speakWithSettings() aborted: _tts is null');
      return;
    }

    final targetLang = language ?? _resolvedLanguage;
    _log('speakWithSettings() | pitch=$pitch | rate=$speechRate | lang=$targetLang');

    try {
      await _player.stop();
    } catch (_) {}

    try {
      await _tts!.stop();
    } catch (_) {}

    try {
      await _tts!.setLanguage(targetLang);
    } catch (e) {
      _log('speakWithSettings setLanguage error: $e');
    }
    try {
      await _tts!.setPitch(pitch);
    } catch (e) {
      _log('speakWithSettings setPitch error: $e');
    }
    try {
      await _tts!.setSpeechRate(speechRate);
    } catch (e) {
      _log('speakWithSettings setSpeechRate error: $e');
    }

    try {
      final result = await _tts!.speak(text);
      _log('speakWithSettings speak() returned: $result');
    } catch (e) {
      _log('speakWithSettings speak() threw: $e');
    }
    
    // We intentionally DO NOT restore defaults immediately here.
    // Restoring them immediately causes race conditions on Android TTS since 
    // speak() returns immediately without awaiting completion. 
    // Instead, other speak() methods will set their required rates before speaking.
  }

  /// Stop any currently playing TTS or audio.
  Future<void> stop() async {
    try {
      await _player.stop();
    } catch (e) {
      _log('stop() player error: $e');
    }
    try {
      await _tts?.stop();
    } catch (e) {
      _log('stop() tts error: $e');
    }
  }

  void setOnComplete(VoidCallback callback) {
    _onComplete = callback;
    _init(); // Ensure init runs so the callback gets registered
  }

  /// Prints a full diagnostic report to the console.
  /// Call this from a debug button in the app to diagnose panel TTS issues.
  Future<void> printDiagnosticReport() async {
    _log('=== TTS DIAGNOSTIC REPORT ===');
    _log('isInit: $_isInit');
    _log('resolvedEngine: "$_resolvedEngine"');
    _log('resolvedLanguage: "$_resolvedLanguage"');

    if (_tts == null) {
      _log('FlutterTts instance: NULL (not yet initialized)');
      _log('Run init() first.');
      return;
    }

    try {
      final engines = await _tts!.getEngines;
      _log('Available engines: $engines');
    } catch (e) {
      _log('getEngines() failed: $e');
    }

    try {
      final languages = await _tts!.getLanguages;
      _log('Available languages: $languages');
    } catch (e) {
      _log('getLanguages() failed: $e');
    }

    try {
      final voices = await _tts!.getVoices;
      _log('Available voices (first 10): ${voices?.take(10).toList()}');
    } catch (e) {
      _log('getVoices() failed: $e');
    }

    _log('=== END DIAGNOSTIC REPORT ===');
  }
}
