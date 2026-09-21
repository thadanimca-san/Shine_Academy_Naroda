import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:flutter/gestures.dart';
import '../services/universal_dictionary_service.dart';

class DictionaryEngine {
  static final DictionaryEngine instance = DictionaryEngine._internal();
  DictionaryEngine._internal();

  Map<String, String> _dictionaryIndex = {};
  bool _isInitialized = false;

  Future<void> init() async {
    if (_isInitialized) return;
    try {
      final jsonStr = await rootBundle.loadString('app_core/knowledge_graph/dictionary_index.json');
      final Map<String, dynamic> rawMap = json.decode(jsonStr);
      _dictionaryIndex = rawMap.map((key, value) => MapEntry(key.toLowerCase(), value.toString()));
      
      // We NO LONGER load all terms from UniversalDictionaryService into _dictionaryIndex
      // This prevents the "everything is blue" issue where 22,000 common words would be auto-highlighted.
      // Instead, only the core concepts from the knowledge graph (loaded above) will be auto-highlighted.
      final service = UniversalDictionaryService.instance;
      await service.init();

      _isInitialized = true;
      debugPrint("DictionaryEngine initialized with ${_dictionaryIndex.length} terms.");
    } catch (e) {
      debugPrint("DictionaryEngine failed to initialize: $e");
    }
  }

  Map<String, String> get index => _dictionaryIndex;

  /// Parses text and returns a list of TextSpans where dictionary words and inline glosses `[word|meaning]` are clickable.
  List<TextSpan> parseTextForLinks(String text, TextStyle defaultStyle, Function(String termId) onLinkTap, {Function(String word, String meaning)? onInlineGlossTap}) {
    List<TextSpan> spans = [];
    
    // First, split the text by the inline gloss syntax [word|meaning]
    final RegExp glossRegex = RegExp(r'\[([^\|\]]+)\|([^\]]+)\]');
    int currentIndex = 0;

    for (final match in glossRegex.allMatches(text)) {
      final preText = text.substring(currentIndex, match.start);
      if (preText.isNotEmpty) {
        spans.addAll(_parseDictionaryWords(preText, defaultStyle, onLinkTap));
      }

      final word = match.group(1)!;
      final meaning = match.group(2)!;

      spans.add(
        TextSpan(
          text: word,
          style: defaultStyle.copyWith(
            color: Colors.pink[700],
            decoration: TextDecoration.underline,
            decorationStyle: TextDecorationStyle.dashed,
            fontWeight: FontWeight.bold,
          ),
          recognizer: TapGestureRecognizer()..onTap = () {
            if (onInlineGlossTap != null) {
              onInlineGlossTap(word, meaning);
            }
          },
        ),
      );

      currentIndex = match.end;
    }

    // Process remaining text
    if (currentIndex < text.length) {
      spans.addAll(_parseDictionaryWords(text.substring(currentIndex), defaultStyle, onLinkTap));
    }

    return spans;
  }

  List<TextSpan> _parseDictionaryWords(String text, TextStyle defaultStyle, Function(String termId) onLinkTap) {
    if (!_isInitialized || _dictionaryIndex.isEmpty) {
      return [TextSpan(text: text, style: defaultStyle)];
    }

    List<TextSpan> spans = [];
    final RegExp tokenizer = RegExp(r'([a-zA-Z]+)|([^a-zA-Z]+)');
    final matches = tokenizer.allMatches(text);

    for (var match in matches) {
      final word = match.group(0)!;
      final isWord = match.group(1) != null;
      
      if (isWord) {
        final cleanWord = word.toLowerCase();
        if (_dictionaryIndex.containsKey(cleanWord)) {
          final termId = _dictionaryIndex[cleanWord]!;
          spans.add(
            TextSpan(
              text: word,
              style: defaultStyle.copyWith(
                color: Colors.blue[700],
                decoration: TextDecoration.underline,
                fontWeight: FontWeight.bold,
              ),
              recognizer: TapGestureRecognizer()..onTap = () => onLinkTap(termId),
            ),
          );
          continue;
        }
      }
      
      if (isWord) {
        spans.add(TextSpan(
          text: word, 
          style: defaultStyle,
          recognizer: DoubleTapGestureRecognizer()..onDoubleTap = () => onLinkTap(word),
        ));
      } else {
        spans.add(TextSpan(text: word, style: defaultStyle));
      }
    }

    return spans;
  }
}
