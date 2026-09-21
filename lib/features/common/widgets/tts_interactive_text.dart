import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../core/services/tts_service.dart';
import '../../../foundation/theme/app_typography.dart';

class TtsInteractiveText extends StatefulWidget {
  final String text;
  final String? fullTtsText;
  final TextStyle? style;
  final Color highlightColor;
  final TextAlign textAlign;
  final void Function(String word, String meaning)? onInlineGlossTap;

  const TtsInteractiveText({
    super.key,
    required this.text,
    this.fullTtsText,
    this.style,
    this.highlightColor = Colors.yellow,
    this.textAlign = TextAlign.start,
    this.onInlineGlossTap,
  });

  @override
  State<TtsInteractiveText> createState() => _TtsInteractiveTextState();
}

class _TtsInteractiveTextState extends State<TtsInteractiveText> {
  List<TextSpan> _spans = [];
  String _cleanText = '';
  String currentWord = '';
  DateTime? _lastTapTime;

  @override
  void initState() {
    super.initState();
    _parseText();
  }

  @override
  void didUpdateWidget(TtsInteractiveText oldWidget) {
    super.didUpdateWidget(oldWidget);
    if (oldWidget.text != widget.text || oldWidget.style != widget.style) {
      _parseText();
    }
  }

  void _commitWord(bool b, bool it, {bool force = false}) {
    if (currentWord.isNotEmpty || force) {
      if (currentWord.isNotEmpty) {
        final baseStyle = widget.style ?? AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface);
        
        TextStyle spanStyle = baseStyle;
        if (b) spanStyle = spanStyle.copyWith(fontWeight: FontWeight.bold);
        if (it) spanStyle = spanStyle.copyWith(fontStyle: FontStyle.italic);

        final String wordToCommit = currentWord;
        final int startOffset = _cleanText.length;
        _cleanText += wordToCommit;

        GestureRecognizer? recognizer;
        if (wordToCommit.trim().isNotEmpty) {
          if (widget.onInlineGlossTap != null) {
            recognizer = TapGestureRecognizer()
              ..onTap = () {
                widget.onInlineGlossTap!(wordToCommit, '');
              };
          } else {
            recognizer = DoubleTapGestureRecognizer()
              ..onDoubleTap = () async {
                final now = DateTime.now();
                if (_lastTapTime != null && now.difference(_lastTapTime!) < const Duration(milliseconds: 500)) {
                  TTSService.instance.stop();
                  if (startOffset < _cleanText.length) {
                    String remainingText = _cleanText.substring(startOffset);
                    await TTSService.instance.speak(remainingText);
                  }
                  _lastTapTime = null;
                } else {
                  _lastTapTime = now;
                }
              };
          }
        }

        _spans.add(TextSpan(
          text: wordToCommit,
          style: spanStyle,
          recognizer: recognizer,
        ));
      }
      currentWord = '';
    }
  }

  void _parseText() {
    _spans.clear();
    _cleanText = '';
    currentWord = '';

    bool isBold = false;
    bool isItalic = false;

    for (int i = 0; i < widget.text.length; i++) {
      String char = widget.text[i];

      if (char == '*') {
        if (i + 1 < widget.text.length && widget.text[i+1] == '*') {
          _commitWord(isBold, isItalic);
          isBold = !isBold;
          i++;
        } else {
          _commitWord(isBold, isItalic);
          isItalic = !isItalic;
        }
      } else if (char == '_' && (i + 1 < widget.text.length && widget.text[i+1] == '_')) {
        _commitWord(isBold, isItalic);
        isBold = !isBold;
        i++;
      } else if (char == ' ' || char == '\n') {
        _commitWord(isBold, isItalic);
        _cleanText += char;
        _spans.add(TextSpan(text: char, style: widget.style));
      } else if (RegExp(r'''[.,!?;:()\[\]"'-]''').hasMatch(char)) {
        _commitWord(isBold, isItalic);
        _cleanText += char;
        _spans.add(TextSpan(text: char, style: widget.style));
      } else {
        currentWord += char;
      }
    }
    _commitWord(isBold, isItalic, force: true);
  }

  @override
  Widget build(BuildContext context) {
    return ValueListenableBuilder<TtsProgress>(
      valueListenable: TTSService.instance.progress,
      builder: (context, progress, child) {
        bool isCurrentlyReadingThisBlock = false;
        
        final String expectedTtsText = widget.fullTtsText != null ? widget.fullTtsText!.toLowerCase().trim() : _cleanText.toLowerCase().trim();

        if (progress.text.isNotEmpty && TTSService.instance.isPlayingGlobal.value) {
           final pText = progress.text.toLowerCase().trim();
           if (pText == expectedTtsText || pText.contains(expectedTtsText) || expectedTtsText.contains(pText)) {
              isCurrentlyReadingThisBlock = true;
           }
        }

        int highlightStart = -1;
        int highlightEnd = -1;

        if (isCurrentlyReadingThisBlock && progress.startOffset != 0 && progress.endOffset != 0) {
           final pTextLower = progress.text.toLowerCase();
           final cTextLower = _cleanText.toLowerCase();
           
           if (pTextLower.contains(cTextLower)) {
              int offsetInSpokenText = pTextLower.indexOf(cTextLower);
              highlightStart = progress.startOffset - offsetInSpokenText;
              highlightEnd = progress.endOffset - offsetInSpokenText;
           } else {
              int chunkOffset = cTextLower.indexOf(pTextLower);
              if (chunkOffset != -1) {
                 highlightStart = chunkOffset + progress.startOffset;
                 highlightEnd = chunkOffset + progress.endOffset;
              }
           }
        }

        List<InlineSpan> builtSpans = [];
        int currentOffset = 0;

        for (var span in _spans) {
          TextStyle? spanStyle = span.style;

          if (span.text != null && span.text!.trim().isNotEmpty && !RegExp(r'''^[.,!?;:()\[\]"'-]+$''').hasMatch(span.text!)) {
            if (highlightStart != -1 && highlightEnd != -1) {
              if (currentOffset >= highlightStart && currentOffset < highlightEnd) {
                spanStyle = (spanStyle ?? widget.style)?.copyWith(
                  backgroundColor: widget.highlightColor,
                  color: Colors.black, // High contrast on yellow
                );
              }
            }
          }

          if (span.text != null) {
            currentOffset += span.text!.length;
          }

          builtSpans.add(TextSpan(
            text: span.text,
            style: spanStyle,
            recognizer: span.recognizer,
          ));
        }

        return RichText(
          textAlign: widget.textAlign,
          text: TextSpan(
            style: widget.style,
            children: builtSpans,
          ),
        );
      },
    );
  }
}
