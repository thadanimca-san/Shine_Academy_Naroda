import 'dart:async';
import 'package:flutter/foundation.dart';
import 'package:flutter_tts/flutter_tts.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

enum TTSSpeed {
  verySlow, // Word by Word (one word at a time with child-like deliberate pause)
  slow,     // Slow educational pace
  medium;   // Medium conversational pace

  static const TTSSpeed wordByWord = TTSSpeed.verySlow;
}

/// Characters (besides whitespace) that separate spoken words. The highlighter
/// (TtsInteractiveText) splits on the same set, so word N in the speech is
/// word N on screen.
const String ttsWordSeparatorChars = '.,!?;:()[]"\'—–-•*#';

bool isTtsWordSeparator(String char) => char.trim().isEmpty || ttsWordSeparatorChars.contains(char);

/// The words of [text] as (start, end) offsets, in reading order.
List<({int start, int end})> ttsWordSpans(String text) {
  final spans = <({int start, int end})>[];
  int? start;
  for (var i = 0; i < text.length; i++) {
    if (isTtsWordSeparator(text[i])) {
      if (start != null) spans.add((start: start, end: i));
      start = null;
    } else {
      start ??= i;
    }
  }
  if (start != null) spans.add((start: start, end: text.length));
  return spans;
}

/// The words of [text], lower-cased and joined by single spaces: two texts with
/// the same key are read aloud as the same words.
String ttsWordKey(String text) =>
    ttsWordSpans(text).map((w) => text.substring(w.start, w.end).toLowerCase()).join(' ');

class TtsProgress {
  final String text;
  final int startOffset;
  final int endOffset;
  final String word;
  final int wordIndex;

  const TtsProgress({
    required this.text,
    required this.startOffset,
    required this.endOffset,
    required this.word,
    this.wordIndex = -1,
  });

  static const TtsProgress empty = TtsProgress(text: '', startOffset: 0, endOffset: 0, word: '', wordIndex: -1);
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

  int _playbackGeneration = 0;

  /// True while speak() is reading a sequence of utterances (words or
  /// sentences); the engine's completion of one utterance must not end it.
  bool _sequenceActive = false;
  Completer<void>? _utteranceStarted;

  /// Learnt ratio of real speaking time to the word-duration estimate, per
  /// speed. Starts at 1 and adapts after every sentence, so the highlight
  /// keeps pace on any device, engine or voice.
  final Map<TTSSpeed, double> _paceCalibration = {TTSSpeed.slow: 1.0, TTSSpeed.medium: 1.0};
  VoidCallback? _onWordComplete;
  Timer? _progressDelayTimer;
  String _lastSpokenText = '';
  String? _lastForceLanguage;

  final Map<TTSSpeed, double> _speedMap = {
    TTSSpeed.verySlow: 0.35, // Rate for individual words in word-by-word mode
    TTSSpeed.slow: 0.33,     // Calm, steady, clear educational pace
    TTSSpeed.medium: 0.45,   // Natural, fluent conversational pace
  };

  String _resolvedLanguage = 'en-IN';
  String _resolvedEngine = '';
  Map<String, String>? _activeMaleVoice;

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
    try {
      await _flutterTts!.awaitSpeakCompletion(true);
    } catch (e) {
      _log('awaitSpeakCompletion not supported: $e');
    }

    // 5. Callbacks
    try {
      _flutterTts!.setErrorHandler((msg) => _log('Engine error: $msg'));
      _flutterTts!.setStartHandler(() {
        _log('speak() started');
        isPlayingGlobal.value = true;
        final started = _utteranceStarted;
        if (started != null && !started.isCompleted) started.complete();
      });
      _flutterTts!.setCompletionHandler(() {
        _log('speak() completed');
        _onWordComplete?.call();
        // Inside a word or sentence sequence, one utterance ending is not the end of
        // reading. Only speak() and stop() change _playbackGeneration: a late
        // completion or cancel from an earlier utterance must not cut off a new one.
        if (!_sequenceActive) {
          isPlayingGlobal.value = false;
          progress.value = TtsProgress.empty;
        }
      });
      _flutterTts!.setCancelHandler(() {
        _log('speak() cancelled');
        _onWordComplete?.call();
        if (!_sequenceActive) {
          isPlayingGlobal.value = false;
          progress.value = TtsProgress.empty;
        }
      });
      _flutterTts!.setProgressHandler((String text, int startOffset, int endOffset, String word) {
        // Discard native Android onRangeStart synthesis burst.
        // Word progression is synchronously paced in Dart in lockstep with speech playback.
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

    // Step 2: Aggressively hunt for a sweet, impressive MALE voice
    try {
      final voices = await _flutterTts!.getVoices;
      if (voices != null) {
        final List<Map<Object?, Object?>> voiceList = List<Map<Object?, Object?>>.from(voices);
        
        bool isMaleVoice(Map<Object?, Object?> v) {
          final name = (v['name']?.toString() ?? '').toLowerCase();
          final gender = (v['gender']?.toString() ?? '').toLowerCase();
          
          // Definitively reject female voices
          if (name.contains('female') || gender == 'female' ||
              name.contains('ena-') || name.contains('enc-') ||
              name.contains('cxx') || name.contains('#female')) {
            return false;
          }
          
          // Male markers across Google TTS, Samsung TTS, and system engines
          return name.contains('male') || gender == 'male' ||
                 name.contains('end-local') || name.contains('ene-local') || name.contains('enf-local') ||
                 name.contains('end-network') || name.contains('ene-network') ||
                 name.contains('rjs') || name.contains('gbc') || name.contains('gbb') || name.contains('gbf') ||
                 name.contains('sfg#male') || name.contains('iom') || name.contains('iol') ||
                 name.contains('-m-') || name.contains('_m_');
        }

        // Priority 1: Indian English (en-IN) Male Voice
        final indianMaleVoices = voiceList.where((v) {
          final locale = (v['locale']?.toString() ?? '').toLowerCase();
          final isIndian = locale.contains('en-in') || locale.contains('en_in') || locale.contains('ind');
          return isIndian && isMaleVoice(v);
        }).toList();

        // Priority 2: British English (en-GB) Male Voice (Classic sweet teacher tone)
        final britishMaleVoices = voiceList.where((v) {
          final locale = (v['locale']?.toString() ?? '').toLowerCase();
          final isBritish = locale.contains('en-gb') || locale.contains('en_gb');
          return isBritish && isMaleVoice(v);
        }).toList();

        // Priority 3: American English (en-US) Male Voice
        final usMaleVoices = voiceList.where((v) {
          final locale = (v['locale']?.toString() ?? '').toLowerCase();
          final isUs = locale.contains('en-us') || locale.contains('en_us');
          return isUs && isMaleVoice(v);
        }).toList();

        // Priority 4: Any English Male Voice
        final anyEnglishMaleVoices = voiceList.where((v) {
          final locale = (v['locale']?.toString() ?? '').toLowerCase();
          return locale.startsWith('en') && isMaleVoice(v);
        }).toList();

        Map<Object?, Object?>? selectedVoice;
        if (indianMaleVoices.isNotEmpty) {
          // Prefer high-fidelity studio/network Indian male voice if available, then local
          final network = indianMaleVoices.where((v) => (v['name']?.toString() ?? '').toLowerCase().contains('network')).toList();
          selectedVoice = network.isNotEmpty ? network.first : indianMaleVoices.first;
          _log('Selected Indian English Male voice: ${selectedVoice['name']}');
        } else if (britishMaleVoices.isNotEmpty) {
          selectedVoice = britishMaleVoices.first;
          _log('Selected British English Male voice: ${selectedVoice['name']}');
        } else if (usMaleVoices.isNotEmpty) {
          selectedVoice = usMaleVoices.first;
          _log('Selected US English Male voice: ${selectedVoice['name']}');
        } else if (anyEnglishMaleVoices.isNotEmpty) {
          selectedVoice = anyEnglishMaleVoices.first;
          _log('Selected English Male voice: ${selectedVoice['name']}');
        }

        if (selectedVoice != null) {
          final voiceMap = {
            "name": selectedVoice['name']?.toString() ?? '',
            "locale": selectedVoice['locale']?.toString() ?? ''
          };
          
          _activeMaleVoice = voiceMap;
          await _flutterTts!.setVoice(voiceMap);
          _resolvedLanguage = voiceMap['locale']!;
          _log('HARD FORCED Sweet Male Indian voice: ${voiceMap['name']} (${voiceMap['locale']})');
          return;
        } else {
          _log('Warning: No explicit Male voice tag identified in getVoices, attempting language fallback');
        }
      }
    } catch (e) {
      _log('Exception while scanning getVoices for male voice: $e');
    }

    // Step 3: Fallback if no specific male voice found in list
    _log('Falling back to basic language search...');
    try {
      final List<dynamic>? languages = await _flutterTts!.getLanguages;
      if (languages == null || languages.isEmpty) return;

      final preferred = ['en-in', 'en-gb', 'en-au', 'en-us', 'en'];
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
      // 1.0 is the natural studio tone (avoids robotic distortion caused by pitch-shifting)
      await _flutterTts!.setPitch(1.0);
      _log('Pitch: 1.0 (Natural Studio Male Voice)');
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
    if (currentSpeed.value == speed) return;
    currentSpeed.value = speed;
    if (isPlayingGlobal.value && _lastSpokenText.isNotEmpty) {
      final textToResume = _lastSpokenText;
      final langToResume = _lastForceLanguage;
      stop().then((_) {
        speak(textToResume, forceLanguage: langToResume);
      });
    }
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

      // Natural studio pitch 1.0 ensures fluent, undistorted Hindi pronunciation
      await _flutterTts!.setPitch(1.0);
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
    _lastSpokenText = text;
    _lastForceLanguage = forceLanguage;
    if (!_isInitialized) await init();

    if (_flutterTts == null) {
      _log('speak() aborted: FlutterTts is null (engine unavailable)');
      return;
    }

    // Clean Markdown and LaTeX formulas so TTS doesn't say "star star" or "backslash frac"
    final cleanText = text
        .replaceAll(RegExp(r'\$\$[\s\S]*?\$\$'), ' ')
        .replaceAll(RegExp(r'\$[^\$]*?\$'), ' ')
        .replaceAll(RegExp(r'(\*\*|\*|__|_|#)'), '');

    _log('speak() | text: "${cleanText.substring(0, cleanText.length.clamp(0, 60))}..."');

    _playbackGeneration++;
    final generation = _playbackGeneration;
    // Mark the sequence before stopping the previous utterance, so its cancel
    // callback does not clear this reading's highlight.
    _sequenceActive = true;

    try {
      await _flutterTts!.stop();
      isPlayingGlobal.value = false;
      progress.value = TtsProgress.empty;

      // 🌐 DYNAMIC LANGUAGE SWITCHING based on currently active UI language
      // If forceLanguage is provided, use it. Otherwise fallback to UI language.
      String targetLangCode = forceLanguage ?? TrilingualService.instance.activeViewLanguage;
      
      if (targetLangCode == 'hi' || targetLangCode == 'hi-IN') {
        await _flutterTts!.setLanguage('hi-IN');
        await _flutterTts!.setPitch(1.0);
        // Prioritize natural studio Hindi male voice
        try {
          final candidates = [
            {"name": "hi-in-x-hie-network", "locale": "hi-IN"},
            {"name": "hi-in-x-hid-network", "locale": "hi-IN"},
            {"name": "hi-in-x-hie-local", "locale": "hi-IN"},
            {"name": "hi-in-x-hid-local", "locale": "hi-IN"},
          ];
          for (final c in candidates) {
            try {
              await _flutterTts!.setVoice(c);
              break;
            } catch (_) {}
          }
        } catch (_) {}
        _log('Switching TTS language to hi-IN (pitch: 1.0) for Hindi');
      } else if (targetLangCode == 'gu' || targetLangCode == 'gu-IN') {
        await _flutterTts!.setLanguage('gu-IN');
        await _flutterTts!.setPitch(1.0);
        _log('Switching TTS language to gu-IN (pitch: 1.0) for Gujarati');
      } else {
        // For English: DO NOT call setLanguage (it resets Android engine to default female voice!)
        // Instead, re-apply the cached Indian Male voice
        if (_activeMaleVoice != null && _activeMaleVoice!.isNotEmpty) {
          await _flutterTts!.setVoice(_activeMaleVoice!);
          _log('Using verified Indian Male voice: ${_activeMaleVoice!["name"]}');
        } else {
          // If no voice was cached, proactively bind to Indian male candidate voices (network first)
          bool voiceFound = false;
          final candidates = [
            {"name": "en-in-x-end-network", "locale": "en-IN"},
            {"name": "en-in-x-ene-network", "locale": "en-IN"},
            {"name": "en-in-x-ahp-network", "locale": "en-IN"},
            {"name": "en-in-x-end-local", "locale": "en-IN"},
            {"name": "en-in-x-ene-local", "locale": "en-IN"},
            {"name": "en-in-x-ahp-local", "locale": "en-IN"},
            {"name": "en-in-x-iip-local", "locale": "en-IN"},
            {"name": "en_IN_#male", "locale": "en-IN"},
          ];
          for (final cand in candidates) {
            try {
              await _flutterTts!.setVoice(cand);
              _activeMaleVoice = cand;
              voiceFound = true;
              _log('Enforced Indian male candidate voice: ${cand["name"]}');
              break;
            } catch (_) {}
          }
          if (!voiceFound) {
            await _flutterTts!.setLanguage('en-IN');
          }
        }
        // Studio quality natural pitch (eliminates robotic pitch distortion)
        await _flutterTts!.setPitch(1.0);
        _log('Set English speaking pitch to 1.0 (Natural Studio Male Voice)');
      }
    } catch (e) {
      _log('stop/setLanguage before speak threw: $e');
    }

    isPlayingGlobal.value = true;
    final words = ttsWordSpans(cleanText);
    if (words.isEmpty) {
      if (generation == _playbackGeneration) _sequenceActive = false;
      isPlayingGlobal.value = false;
      return;
    }

    try {
      if (currentSpeed.value == TTSSpeed.verySlow) {
        await _speakWordByWord(cleanText, words, generation);
      } else {
        await _speakBySentence(cleanText, words, generation, currentSpeed.value);
      }
    } finally {
      if (generation == _playbackGeneration) {
        _sequenceActive = false;
        isPlayingGlobal.value = false;
        progress.value = TtsProgress.empty;
      }
    }
  }

  void _showWord(String text, ({int start, int end}) w, int index) {
    progress.value = TtsProgress(
      text: text,
      startOffset: w.start,
      endOffset: w.end,
      word: text.substring(w.start, w.end),
      wordIndex: index,
    );
  }

  /// The punctuation right after a word: a sentence end, a comma-like pause, or none.
  ({bool sentenceEnd, bool comma}) _pauseAfter(String text, int end) {
    final next = text.substring(end, (end + 4).clamp(end, text.length));
    return (sentenceEnd: RegExp(r'^\s*[.?!]').hasMatch(next), comma: RegExp(r'^\s*[,;:]').hasMatch(next));
  }

  /// Speaks [utterance] and returns how long it took. With awaitSpeakCompletion
  /// the call ends when the audio ends; the timeout guards engines that never
  /// report completion.
  Future<int> _speakUtterance(String utterance, int timeoutMs) async {
    final watch = Stopwatch()..start();
    try {
      final result = await _flutterTts!.speak(utterance).timeout(Duration(milliseconds: timeoutMs), onTimeout: () => null);
      if (result == 0) {
        _log('speak() returned 0 (engine failure). Reinitializing...');
        await _reinit();
        if (_flutterTts != null) {
          await _flutterTts!.setSpeechRate(_speedMap[currentSpeed.value] ?? 0.45);
          await _flutterTts!.speak(utterance).timeout(Duration(milliseconds: timeoutMs), onTimeout: () => null);
        }
      }
    } catch (e) {
      _log('speak() threw: $e. Reinitializing...');
      await _reinit();
    }
    return watch.elapsedMilliseconds;
  }

  // ===========================================================================
  // 👶 WORD BY WORD (TTSSpeed.verySlow): one word per utterance, then a pause
  // (longer at commas and sentence ends), e.g. "i ... am ... a ... boy."
  // ===========================================================================
  Future<void> _speakWordByWord(String text, List<({int start, int end})> words, int generation) async {
    await _flutterTts!.setSpeechRate(_speedMap[TTSSpeed.verySlow]!);
    for (var i = 0; i < words.length; i++) {
      if (generation != _playbackGeneration) return;
      final w = words[i];
      final word = text.substring(w.start, w.end);
      _showWord(text, w, i);
      // Keep the classroom pace: a short word still holds the highlight for 700 ms or more.
      final minimumMs = (580 + word.length * 60).clamp(700, 1600);
      final spokenMs = await _speakUtterance(word, minimumMs + 5000);
      if (spokenMs < minimumMs) await Future.delayed(Duration(milliseconds: minimumMs - spokenMs));
      if (generation != _playbackGeneration) return;
      final pause = _pauseAfter(text, w.end);
      await Future.delayed(Duration(milliseconds: pause.sentenceEnd ? 950 : (pause.comma ? 750 : 650)));
    }
  }

  // ===========================================================================
  // 🎧 SLOW / MEDIUM: one sentence per utterance. The highlight moves through the
  // sentence's words on estimated timings, starting when the audio starts, and
  // re-synchronises at every sentence. After each sentence the estimate is
  // corrected by the real speaking time, so drift cannot build up.
  // ===========================================================================
  Future<void> _speakBySentence(String text, List<({int start, int end})> words, int generation, TTSSpeed speed) async {
    final rate = _speedMap[speed] ?? 0.45;
    try {
      await _flutterTts!.setSpeechRate(rate);
    } catch (e) {
      _log('setSpeechRate before speak error: $e');
    }

    for (final sentence in _sentences(text, words)) {
      if (generation != _playbackGeneration) return;
      final sentenceWords = words.sublist(sentence.firstWord, sentence.lastWord + 1);
      final estimates = [
        for (final w in sentenceWords) _estimateWordMs(text, w, speed),
      ];
      final estimateMs = estimates.fold<int>(0, (a, b) => a + b);
      final scale = _paceCalibration[speed] ?? 1.0;

      _utteranceStarted = Completer<void>();
      var sentenceDone = false;
      final pacer = () async {
        // Start highlighting when the engine starts playing (or after 1.5 s if it never says so).
        await _utteranceStarted!.future.timeout(const Duration(milliseconds: 1500), onTimeout: () {});
        for (var k = 0; k < sentenceWords.length; k++) {
          if (sentenceDone || generation != _playbackGeneration) return;
          _showWord(text, sentenceWords[k], sentence.firstWord + k);
          // The last word stays lit until the sentence's audio really ends.
          if (k < sentenceWords.length - 1) {
            await Future.delayed(Duration(milliseconds: (estimates[k] * scale).round()));
          }
        }
      }();

      final spokenMs = await _speakUtterance(text.substring(sentence.start, sentence.end), (estimateMs * scale * 3).round() + 5000);
      sentenceDone = true;
      await pacer;
      if (generation != _playbackGeneration) return;

      // Learn the device's real pace from sentences long enough to be reliable.
      if (sentenceWords.length >= 3 && estimateMs > 0 && spokenMs > 300) {
        final ratio = (spokenMs / estimateMs).clamp(0.4, 2.5);
        _paceCalibration[speed] = (0.6 * scale + 0.4 * ratio).clamp(0.4, 2.5);
      }
    }
  }

  /// Splits [text] into sentences at . ? ! and line breaks, as word-index ranges.
  List<({int start, int end, int firstWord, int lastWord})> _sentences(String text, List<({int start, int end})> words) {
    final result = <({int start, int end, int firstWord, int lastWord})>[];
    var first = 0;
    for (var i = 0; i < words.length; i++) {
      final isLast = i == words.length - 1;
      final gap = isLast ? '' : text.substring(words[i].end, words[i + 1].start);
      if (isLast || RegExp(r'[.?!\n]').hasMatch(gap)) {
        final end = isLast ? text.length : words[i].end + gap.indexOf(RegExp(r'[.?!\n]')) + 1;
        result.add((start: words[first].start, end: end, firstWord: first, lastWord: i));
        first = i + 1;
      }
    }
    return result;
  }

  /// Rough time to say one word at [speed], before calibration.
  int _estimateWordMs(String text, ({int start, int end}) w, TTSSpeed speed) {
    final len = w.end - w.start;
    final pause = _pauseAfter(text, w.end);
    if (speed == TTSSpeed.slow) {
      // Rate 0.33, about 105 words per minute.
      return (380 + len * 35).clamp(420, 1100) + (pause.sentenceEnd ? 380 : (pause.comma ? 180 : 0));
    }
    // Rate 0.45, about 145 words per minute.
    return (280 + len * 25).clamp(320, 850) + (pause.sentenceEnd ? 280 : (pause.comma ? 140 : 0));
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
    _playbackGeneration++;
    _sequenceActive = false;
    _progressDelayTimer?.cancel();
    _onWordComplete?.call();
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
