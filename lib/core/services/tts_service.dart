import 'package:flutter/foundation.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

enum TTSSpeed {
  verySlow,
  slow,
  medium,
}

class TtsProgress {
  final String text;
  final int startOffset;
  final int endOffset;
  final String word;

  const TtsProgress({
    required this.text,
    required this.startOffset,
    required this.endOffset,
    required this.word,
  });

  static const TtsProgress empty = TtsProgress(text: '', startOffset: 0, endOffset: 0, word: '');
}

/// TTSService — Shine Academy Naroda
/// Version 4.0 — Digital Panel Bulletproof Edition
///
/// Used by: DictionaryScreen, DictionaryPopup, TtsSpeedController
///
/// ROOT CAUSE FIX: FlutterTts was created at class-field level, meaning it
/// was instantiated at app startup before Google TTS had registered itself
/// with Android. Now created lazily inside init(), after engines are available.
class TTSService {
  static final TTSService instance = TTSService._internal();
  TTSService._internal();

  // ✅ CRITICAL FIX: Lazy — created inside init(), not at field level.
  FlutterTts? _flutterTts;
  bool _isInitialized = false;
  bool _isInitializing = false;

  final ValueNotifier<TTSSpeed> currentSpeed = ValueNotifier<TTSSpeed>(TTSSpeed.medium);
  final ValueNotifier<TtsProgress> progress = ValueNotifier<TtsProgress>(TtsProgress.empty);
  final ValueNotifier<bool> isPlayingGlobal = ValueNotifier<bool>(false);

  final Map<TTSSpeed, double> _speedMap = {
    TTSSpeed.verySlow: 0.18,
    TTSSpeed.slow: 0.30,
    TTSSpeed.medium: 0.50,
  };

  String _resolvedLanguage = 'en-IN';
  String _resolvedEngine = '';

  void _log(String message) {
    debugPrint('[TTSService] $message');
  }

  Future<void> init() async {
    if (_isInitialized) return;
    if (_isInitializing) {
      // Wait for the ongoing init instead of double-running
      int waited = 0;
      while (_isInitializing && waited < 5000) {
        await Future.delayed(const Duration(milliseconds: 100));
        waited += 100;
      }
      return;
    }
    _isInitializing = true;
    _log('=== TTSService Init START ===');

    // 1. Create FlutterTts lazily
    try {
      _flutterTts = FlutterTts();
      _log('FlutterTts instance created');
    } catch (e) {
      _log('FATAL: FlutterTts() constructor threw: $e');
      _isInitializing = false;
      return;
    }

    // 2. Bind best engine (Google TTS preferred)
    await _bindBestEngine();

    // 3. Bind best language
    await _bindBestLanguage();

    // 4. Apply default speech params
    await _applyDefaultSettings();

    // 5. Callbacks
    try {
      _flutterTts!.setErrorHandler((msg) => _log('Engine error: $msg'));
      _flutterTts!.setStartHandler(() {
        _log('speak() started');
        isPlayingGlobal.value = true;
      });
      _flutterTts!.setCompletionHandler(() {
        _log('speak() completed');
        isPlayingGlobal.value = false;
        progress.value = TtsProgress.empty;
      });
      _flutterTts!.setCancelHandler(() {
        _log('speak() cancelled');
        isPlayingGlobal.value = false;
        progress.value = TtsProgress.empty;
      });
      _flutterTts!.setProgressHandler((String text, int startOffset, int endOffset, String word) {
        progress.value = TtsProgress(
          text: text,
          startOffset: startOffset,
          endOffset: endOffset,
          word: word,
        );
      });
    } catch (e) {
      _log('Callback setup error: $e');
    }

    // 6. Listen to speed changes
    currentSpeed.addListener(() => _applySpeed(currentSpeed.value));

    _isInitialized = true;
    _isInitializing = false;
    _log('=== TTSService Init COMPLETE. Engine: "$_resolvedEngine" | Lang: "$_resolvedLanguage" ===');
  }

  Future<void> _bindBestEngine() async {
    if (_flutterTts == null) return;

    // Retry up to 3 times — handles freshly installed Google TTS APK
    for (int attempt = 1; attempt <= 3; attempt++) {
      try {
        _log('Engine detection attempt $attempt...');
        final List<dynamic>? engines = await _flutterTts!.getEngines;

        if (engines == null || engines.isEmpty) {
          _log('Attempt $attempt: No engines found. Waiting...');
          if (attempt < 3) await Future.delayed(Duration(seconds: attempt));
          continue;
        }

        _log('Attempt $attempt: Found engines: $engines');

        final preferredEngines = [
          'com.google.android.tts',
          'com.samsung.SMT',
          'com.svox.pico',
          'com.huawei.hiai.tts.engine',
        ];

        String? chosenEngine;
        for (final preferred in preferredEngines) {
          final match = engines.firstWhere(
            (e) => e.toString() == preferred || e.toString().startsWith(preferred),
            orElse: () => null,
          );
          if (match != null) {
            chosenEngine = match.toString();
            break;
          }
        }
        chosenEngine ??= engines.first.toString();

        try {
          await _flutterTts!.setEngine(chosenEngine);
          _resolvedEngine = chosenEngine;
          _log('Engine set: "$chosenEngine"');
          return;
        } catch (e) {
          _log('Failed to set engine "$chosenEngine": $e');
        }
      } catch (e) {
        _log('Attempt $attempt getEngines() threw: $e');
        if (attempt < 3) await Future.delayed(Duration(seconds: attempt));
      }
    }
    _log('WARNING: Using system default engine');
    _resolvedEngine = 'system_default';
  }

  Future<void> _bindBestLanguage() async {
    if (_flutterTts == null) return;
    
    _log('Attempting to force Indian English (en-IN) offline voice...');
    
    // Step 1: Force Language (often ignored by basic Android engines if not explicitly set via Voice)
    try {
      await _flutterTts!.setLanguage('en-IN');
    } catch (e) {
      _log('Exception forcing en-IN language: $e');
    }

    // Step 2: Aggressively hunt for the actual Indian Voice in the installed voice list
    try {
      final voices = await _flutterTts!.getVoices;
      if (voices != null) {
        final List<Map<Object?, Object?>> voiceList = List<Map<Object?, Object?>>.from(voices);
        
        // Find all Indian English voices
        final indianVoices = voiceList.where((v) {
          final locale = (v['locale']?.toString() ?? '').toLowerCase();
          return locale.contains('en-in') || locale.contains('en_in') || locale.contains('ind');
        }).toList();

        if (indianVoices.isNotEmpty) {
          // Prioritize offline voices since the digital panel has no internet
          final offlineIndianVoices = indianVoices.where((v) {
            final name = (v['name']?.toString() ?? '').toLowerCase();
            return !name.contains('network') && !name.contains('online');
          }).toList();

          // Prefer female voices for a sweeter sound
          final femaleVoices = offlineIndianVoices.where((v) {
            final name = (v['name']?.toString() ?? '').toLowerCase();
            return name.contains('female');
          }).toList();

          final selectedVoice = femaleVoices.isNotEmpty 
            ? femaleVoices.first 
            : (offlineIndianVoices.isNotEmpty ? offlineIndianVoices.first : indianVoices.first);
          
          final voiceMap = {
            "name": selectedVoice['name']?.toString() ?? '',
            "locale": selectedVoice['locale']?.toString() ?? ''
          };
          
          await _flutterTts!.setVoice(voiceMap);
          _resolvedLanguage = voiceMap['locale']!;
          _log('HARD FORCED offline Indian voice: ${voiceMap['name']}');
          return; // Success! We found and forced an Indian voice.
        } else {
          _log('CRITICAL: No Indian English (en-IN) voice is installed on this device!');
        }
      }
    } catch (e) {
      _log('Exception while scanning getVoices: $e');
    }

    // Step 3: Absolute worst-case fallback if NO Indian voices are installed on the device at all
    _log('Falling back to basic language search...');
    try {
      final List<dynamic>? languages = await _flutterTts!.getLanguages;
      if (languages == null || languages.isEmpty) return;

      final preferred = ['en-gb', 'en-au', 'en-us', 'en'];
      String? chosen;
      for (final lang in preferred) {
        final match = languages.cast<String>().firstWhere(
          (l) => l.replaceAll('_', '-').toLowerCase().startsWith(lang),
          orElse: () => '',
        );
        if (match.isNotEmpty) {
          chosen = match;
          break;
        }
      }
      
      chosen ??= languages.first.toString();
      await _flutterTts!.setLanguage(chosen);
      _resolvedLanguage = chosen;
      _log('Fallback Language set to "$chosen"');
    } catch (e) {
      _log('Fallback language detection failed: $e');
    }
  }
Future<void> _applyDefaultSettings() async {
    if (_flutterTts == null) return;
    try {
      await _flutterTts!.setVolume(1.0);
      _log('Volume: 1.0');
    } catch (e) {
      _log('setVolume error: $e');
    }
    try {
      await _flutterTts!.setPitch(1.0);
      _log('Pitch: 1.0');
    } catch (e) {
      _log('setPitch error: $e');
    }
    try {
      await _flutterTts!.setSpeechRate(_speedMap[currentSpeed.value] ?? 0.45);
      _log('SpeechRate: ${_speedMap[currentSpeed.value] ?? 0.45}');
    } catch (e) {
      _log('setSpeechRate error: $e');
    }
  }

  Future<void> _applySpeed(TTSSpeed speed) async {
    if (_flutterTts == null) return;
    final rate = _speedMap[speed] ?? 0.45;
    try {
      await _flutterTts!.setSpeechRate(rate);
      _log('Speed changed to $speed ($rate)');
    } catch (e) {
      _log('_applySpeed error: $e');
    }
  }

  void setSpeed(TTSSpeed speed) {
    currentSpeed.value = speed;
  }

  /// Speak [text] in Hindi (hi-IN locale) with sweet, soft voice settings.
  /// Pitch 0.9 gives a warmer, less harsh tone compared to default 1.0.
  /// Used by Hindi translation panels in ReadAloudButton.
  Future<void> speakHindi(String text) async {
    if (text.trim().isEmpty) return;
    if (!_isInitialized) await init();
    if (_flutterTts == null) return;
    try {
      await _flutterTts!.stop();
      await _flutterTts!.setLanguage('hi-IN');

      // Scan for a soft offline Hindi voice for a sweeter sound
      try {
        final voices = await _flutterTts!.getVoices;
        if (voices != null) {
          final List<Map<Object?, Object?>> voiceList =
              List<Map<Object?, Object?>>.from(voices);
          final hindiVoices = voiceList.where((v) {
            final locale = (v['locale']?.toString() ?? '').toLowerCase();
            return locale.contains('hi-in') || locale.contains('hi_in');
          }).toList();
          if (hindiVoices.isNotEmpty) {
            final offline = hindiVoices.where((v) {
              final name = (v['name']?.toString() ?? '').toLowerCase();
              return !name.contains('network') && !name.contains('online');
            }).toList();
            final chosen = offline.isNotEmpty ? offline.first : hindiVoices.first;
            await _flutterTts!.setVoice({
              'name': chosen['name']?.toString() ?? '',
              'locale': chosen['locale']?.toString() ?? '',
            });
            _log('speakHindi: using voice ${chosen["name"]}');
          }
        }
      } catch (e) {
        _log('speakHindi voice scan error (non-fatal): $e');
      }

      // Softer pitch for Hindi — warmer, less harsh than default 1.0
      await _flutterTts!.setPitch(0.9);
      await _flutterTts!.speak(text);
      // Restore pitch and language after playback completes
      await _flutterTts!.setPitch(1.0);
      await _flutterTts!.setLanguage(_resolvedLanguage);
    } catch (e) {
      _log('speakHindi() error: $e');
    }
  }

  Future<void> speak(String text, {String? forceLanguage}) async {
    if (text.trim().isEmpty) return;
    if (!_isInitialized) await init();

    if (_flutterTts == null) {
      _log('speak() aborted: FlutterTts is null (engine unavailable)');
      return;
    }

    // Clean Markdown so TTS doesn't say "star star" or "underscore"
    final cleanText = text.replaceAll(RegExp(r'(\*\*|\*|__|_|#)'), '');

    _log('speak() | text: "${cleanText.substring(0, cleanText.length.clamp(0, 60))}..."');

    try {
      await _flutterTts!.stop();
      isPlayingGlobal.value = false;
      progress.value = TtsProgress.empty;

      // 🌐 DYNAMIC LANGUAGE SWITCHING based on currently active UI language
      // If forceLanguage is provided, use it. Otherwise fallback to UI language.
      String targetLangCode = forceLanguage ?? TrilingualService.instance.activeViewLanguage;
      
      if (targetLangCode == 'hi' || targetLangCode == 'hi-IN') {
        await _flutterTts!.setLanguage('hi-IN');
        // 🎶 Softer pitch for Hindi — warmer, sweeter sound
        await _flutterTts!.setPitch(0.9);
        _log('Switching TTS language to hi-IN (pitch: 0.9) for Hindi');
      } else if (targetLangCode == 'gu' || targetLangCode == 'gu-IN') {
        await _flutterTts!.setLanguage('gu-IN');
        // Slightly softer pitch for Gujarati
        await _flutterTts!.setPitch(0.95);
        _log('Switching TTS language to gu-IN (pitch: 0.95) for Gujarati');
      } else {
        await _flutterTts!.setLanguage(_resolvedLanguage); // Fallback to detected English
        // Slightly higher pitch for English for a sweeter, friendly sound
        await _flutterTts!.setPitch(1.1);
        _log('Switching TTS language to $_resolvedLanguage (pitch: 1.1) for English');
      }
    } catch (e) {
      _log('stop/setLanguage before speak threw: $e');
    }

    // Removed redundant awaits for rate and language to eliminate massive network/JNI delays.
    // They are set globally in init() and _applySpeed().

    try {
      final result = await _flutterTts!.speak(cleanText);
      _log('speak() returned: $result');

      // Android returns 0 on failure — reinit and retry
      if (result != null && result == 0) {
        _log('speak() returned 0 (engine failure). Reinitializing...');
        await _reinit();
        if (_flutterTts != null) {
          try {
            await _flutterTts!.speak(text);
            _log('Retry after reinit succeeded');
          } catch (e2) {
            _log('Retry after reinit also failed: $e2');
          }
        }
      }
      
      // Speed is deliberately NOT reset — the user's chosen speed persists for
      // the entire session so they don't have to re-select after each paragraph.
    } catch (e) {
      _log('speak() threw: $e. Reinitializing...');
      await _reinit();
      if (_flutterTts != null) {
        try {
          await _flutterTts!.speak(text);
        } catch (e2) {
          _log('Final retry failed: $e2');
          _log('TTS is not functional. Check Settings > Accessibility > TTS Output on this panel.');
        }
      }
    }
  }

  Future<void> _reinit() async {
    _log('--- REINIT triggered ---');
    _isInitialized = false;
    _isInitializing = false;
    try {
      await _flutterTts?.stop();
    } catch (_) {}
    _flutterTts = null;
    await init();
  }

  Future<void> stop() async {
    try {
      await _flutterTts?.stop();
      isPlayingGlobal.value = false;
      progress.value = TtsProgress.empty;
    } catch (e) {
      _log('stop() error: $e');
    }
  }

  /// Full diagnostic report — useful for debugging classroom panels.
  Future<void> printDiagnosticReport() async {
    _log('=== TTSService DIAGNOSTIC REPORT ===');
    _log('isInitialized: $_isInitialized');
    _log('resolvedEngine: "$_resolvedEngine"');
    _log('resolvedLanguage: "$_resolvedLanguage"');
    _log('currentSpeed: ${currentSpeed.value}');

    if (_flutterTts == null) {
      _log('FlutterTts: NULL — call init() first');
      return;
    }

    try {
      _log('Engines: ${await _flutterTts!.getEngines}');
    } catch (e) {
      _log('getEngines() failed: $e');
    }
    try {
      _log('Languages: ${await _flutterTts!.getLanguages}');
    } catch (e) {
      _log('getLanguages() failed: $e');
    }
    try {
      final voices = await _flutterTts!.getVoices;
      _log('Voices (first 5): ${voices?.take(5).toList()}');
    } catch (e) {
      _log('getVoices() failed: $e');
    }
    _log('=== END REPORT ===');
  }
}
