import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:flutter_math_fork/flutter_math.dart';
import '../../../core/services/tts_service.dart';
import '../../../foundation/theme/app_typography.dart';

class TtsInteractiveText extends StatefulWidget {
  final String text;
  final String? fullTtsText;
  final TextStyle? style;
  final Color highlightColor;
  final TextAlign textAlign;
  final void Function(String word, String meaning)? onInlineGlossTap;
  final bool isPdfMode;

  const TtsInteractiveText({
    super.key,
    required this.text,
    this.fullTtsText,
    this.style,
    this.highlightColor = Colors.yellow,
    this.textAlign = TextAlign.start,
    this.onInlineGlossTap,
    this.isPdfMode = false,
  });

  @override
  State<TtsInteractiveText> createState() => _TtsInteractiveTextState();
}

class _TtsInteractiveTextState extends State<TtsInteractiveText> {
  List<InlineSpan> _spans = [];
  String _cleanText = '';
  String currentWord = '';

  @override
  void didChangeDependencies() {
    super.didChangeDependencies();
    // Parsing needs the theme and MediaQuery for the default text style,
    // which are not available yet in initState.
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
                TTSService.instance.stop();
                if (startOffset < _cleanText.length) {
                  String remainingText = _cleanText.substring(startOffset);
                  await TTSService.instance.speak(remainingText);
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
    final text = normalizeMarkdownLines(widget.text);

    for (int i = 0; i < text.length; i++) {
      String char = text[i];

      if (char == '\$') {
        _commitWord(isBold, isItalic);
        bool isBlock = false;
        int j = i + 1;
        if (j < text.length && text[j] == '\$') {
           isBlock = true;
           j++;
        }
        int start = j;
        int end = -1;
        while (j < text.length) {
           if (text[j] == '\$') {
              if (isBlock && j + 1 < text.length && text[j+1] == '\$') {
                  end = j;
                  j += 2;
                  break;
              } else if (!isBlock) {
                  end = j;
                  j++;
                  break;
              }
           }
           j++;
        }
        
        if (end != -1) {
           final tex = repairLatexEscapes(text.substring(start, end));
           _cleanText += ' '; // TTS skips formulas
           if (isBlock) _spans.add(TextSpan(text: '\n', style: widget.style));
           _spans.add(WidgetSpan(
              alignment: PlaceholderAlignment.middle,
              child: _buildMath(tex, isDisplay: isBlock),
           ));
           if (isBlock) _spans.add(TextSpan(text: '\n', style: widget.style));
           i = j - 1; // Advance outer loop
           continue;
        }
      }

      if (char == '*') {
        if (i + 1 < text.length && text[i+1] == '*') {
          _commitWord(isBold, isItalic);
          isBold = !isBold;
          i++;
        } else {
          _commitWord(isBold, isItalic);
          isItalic = !isItalic;
        }
      } else if (char == '_' && (i + 1 < text.length && text[i+1] == '_')) {
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

  Widget _buildMath(String tex, {required bool isDisplay}) {
    final style = widget.style ?? AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface);
    return MediaQuery(
      // AppTypography already scales the font size; avoid scaling twice.
      data: MediaQuery.of(context).copyWith(textScaler: TextScaler.noScaling),
      child: Math.tex(
        tex,
        mathStyle: isDisplay ? MathStyle.display : MathStyle.text,
        textStyle: style,
        onErrorFallback: (error) {
          debugPrint('TtsInteractiveText: cannot render formula "$tex": ${error.message}');
          return Text(tex, style: style);
        },
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    if (widget.isPdfMode) {
      List<InlineSpan> builtSpans = [];
      for (var span in _spans) {
        if (span is TextSpan) {
          builtSpans.add(TextSpan(
            text: span.text,
            style: span.style,
          ));
        } else {
          builtSpans.add(span);
        }
      }
      return RichText(
        textAlign: widget.textAlign,
        text: TextSpan(
          style: DefaultTextStyle.of(context).style.merge(widget.style),
          children: builtSpans,
        ),
      );
    }

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
          if (span is TextSpan) {
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
          } else {
            // Forward WidgetSpan directly
            builtSpans.add(span);
          }
        }

        return RichText(
          textAlign: widget.textAlign,
          text: TextSpan(
            style: DefaultTextStyle.of(context).style.merge(widget.style),
            children: builtSpans,
          ),
        );
      },
    );
  }
}


final _markdownHeading = RegExp(r'^\s{0,3}#{1,6}\s+(.+)$');
final _markdownBullet = RegExp(r'^(\s*)[-*+]\s+');

/// Turns line-level Markdown that this widget cannot draw into text it can:
/// headings become bold lines and `-`, `*` or `+` bullets become "•".
/// Lines inside `$$ ... $$` formulas are left untouched.
String normalizeMarkdownLines(String text) {
  var insideDisplayMath = false;
  return text.split('\n').map((line) {
    final wasInsideDisplayMath = insideDisplayMath;
    if ('\$\$'.allMatches(line).length.isOdd) {
      insideDisplayMath = !insideDisplayMath;
    }
    if (wasInsideDisplayMath) return line;

    final heading = _markdownHeading.firstMatch(line);
    if (heading != null) return '**${heading.group(1)!.trim()}**';
    return line.replaceFirstMapped(_markdownBullet, (m) => '${m.group(1)}• ');
  }).join('\n');
}

final _brokenNewlineCommand = RegExp(r'\n(?=(eq|e|ot|abla|eg|u|i|mid|exists|ewline|leq|geq|parallel|subseteq|subset)(?![a-z]))');
final _brokenReturnCommand = RegExp(r'\r(?=[a-z])');

/// Repairs LaTeX that was damaged by JSON escaping: when content is written
/// with a single backslash, `\frac` becomes a form feed + "rac", `\times` a
/// tab + "imes", `\neq` a newline + "eq", and so on.
String repairLatexEscapes(String tex) {
  var repaired = tex
      .replaceAll('\t', r'\t')
      .replaceAll('\f', r'\f')
      .replaceAll('\b', r'\b')
      .replaceAll(_brokenNewlineCommand, r'\n')
      .replaceAll(_brokenReturnCommand, r'\r');
  // flutter_math_fork cannot negate \implies.
  repaired = repaired.replaceAll(RegExp(r'\\not\s*\\implies'), r'\not\Rightarrow');
  return repaired;
}
