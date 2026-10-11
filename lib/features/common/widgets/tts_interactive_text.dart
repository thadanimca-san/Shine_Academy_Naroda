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

  /// Double-tap a word to read aloud from there. Turn off when the text sits
  /// inside something tappable (an answer option, a flashcard) so taps reach it.
  final bool enableWordTap;

  const TtsInteractiveText({
    super.key,
    required this.text,
    this.fullTtsText,
    this.style,
    this.highlightColor = Colors.yellow,
    this.textAlign = TextAlign.start,
    this.onInlineGlossTap,
    this.isPdfMode = false,
    this.enableWordTap = true,
  });

  @override
  State<TtsInteractiveText> createState() => _TtsInteractiveTextState();
}

class _SpanEntry {
  final InlineSpan span;
  final int startOffset;
  final int endOffset;
  final bool isWord;
  final int wordIndex;

  _SpanEntry({
    required this.span,
    required this.startOffset,
    required this.endOffset,
    required this.isWord,
    this.wordIndex = -1,
  });
}

class _TtsInteractiveTextState extends State<TtsInteractiveText> {
  final List<_SpanEntry> _entries = [];
  String _cleanText = '';
  String currentWord = '';
  int _wordCounter = 0;
  String _blockKey = '  ';

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
        final int endOffset = _cleanText.length;
        final int assignedWordIndex = _wordCounter++;

        GestureRecognizer? recognizer;
        if (wordToCommit.trim().isNotEmpty && widget.enableWordTap) {
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

        _entries.add(_SpanEntry(
          span: TextSpan(
            text: wordToCommit,
            style: spanStyle,
            recognizer: recognizer,
          ),
          startOffset: startOffset,
          endOffset: endOffset,
          isWord: true,
          wordIndex: assignedWordIndex,
        ));
      }
      currentWord = '';
    }
  }

  void _parseText() {
    _entries.clear();
    _cleanText = '';
    currentWord = '';
    _wordCounter = 0;

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
           final startOffset = _cleanText.length;
           _cleanText += ' '; // TTS skips formulas
           final endOffset = _cleanText.length;
           if (isBlock) {
             _entries.add(_SpanEntry(
               span: TextSpan(text: '\n', style: widget.style),
               startOffset: startOffset,
               endOffset: startOffset,
               isWord: false,
             ));
           }
           _entries.add(_SpanEntry(
             span: WidgetSpan(
               alignment: PlaceholderAlignment.middle,
               child: _buildMath(tex, isDisplay: isBlock),
             ),
             startOffset: startOffset,
             endOffset: endOffset,
             isWord: false,
           ));
           if (isBlock) {
             _entries.add(_SpanEntry(
               span: TextSpan(text: '\n', style: widget.style),
               startOffset: endOffset,
               endOffset: endOffset,
               isWord: false,
             ));
           }
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
      } else if (char.trim().isEmpty) {
        _commitWord(isBold, isItalic);
        final startOffset = _cleanText.length;
        _cleanText += char;
        final endOffset = _cleanText.length;
        _entries.add(_SpanEntry(
          span: TextSpan(text: char, style: widget.style),
          startOffset: startOffset,
          endOffset: endOffset,
          isWord: false,
        ));
      } else if (isTtsWordSeparator(char)) {
        // Same word boundaries as TTSService, so the spoken word index matches..
        _commitWord(isBold, isItalic);
        final startOffset = _cleanText.length;
        _cleanText += char;
        final endOffset = _cleanText.length;
        _entries.add(_SpanEntry(
          span: TextSpan(text: char, style: widget.style),
          startOffset: startOffset,
          endOffset: endOffset,
          isWord: false,
          wordIndex: -1,
        ));
      } else {
        currentWord += char;
      }
    }
    _commitWord(isBold, isItalic, force: true);
    _blockKey = ' ${ttsWordKey(_cleanText)} ';
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

  /// Maps the index of the word being spoken in [spokenText] to the index of
  /// the same word in this block, or -1 if this block is not being read.
  /// Texts are compared word by word, so bullets, punctuation and Markdown
  /// differences between the spoken and the shown text do not matter. This also
  /// covers reading that starts mid-block (double-tap) or spans several blocks.
  int _localWordIndex(String spokenText, int spokenWordIndex) {
    if (widget.fullTtsText != null && ttsWordKey(widget.fullTtsText!) != ttsWordKey(spokenText)) return -1;
    final spoken = ' ${ttsWordKey(spokenText)} ';
    final block = _blockKey;
    if (block.trim().isEmpty) return -1;
    int wordsBefore(String text, int at) => ' '.allMatches(text.substring(0, at + 1)).length - 1;
    final blockAt = spoken.indexOf(block);
    if (blockAt >= 0) {
      final local = spokenWordIndex - wordsBefore(spoken, blockAt);
      return local < _wordCounter ? local : -1;
    }
    final spokenAt = block.indexOf(spoken);
    if (spokenAt >= 0) return spokenWordIndex + wordsBefore(block, spokenAt);
    return -1;
  }

  @override
  Widget build(BuildContext context) {
    if (widget.isPdfMode) {
      List<InlineSpan> builtSpans = [];
      for (var entry in _entries) {
        if (entry.span is TextSpan) {
          final s = entry.span as TextSpan;
          builtSpans.add(TextSpan(
            text: s.text,
            style: s.style,
          ));
        } else {
          builtSpans.add(entry.span);
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
        // Which of this block's words is being spoken right now (-1: none).
        final activeWord = progress.wordIndex >= 0 && TTSService.instance.isPlayingGlobal.value
            ? _localWordIndex(progress.text, progress.wordIndex)
            : -1;

        List<InlineSpan> builtSpans = [];

        for (final entry in _entries) {
          if (entry.span is TextSpan) {
            final textSpan = entry.span as TextSpan;
            TextStyle? spanStyle = textSpan.style;

            if (entry.isWord && entry.wordIndex == activeWord) {
              spanStyle = (spanStyle ?? widget.style)?.copyWith(
                backgroundColor: widget.highlightColor,
                color: Colors.black, // High contrast black on yellow highlight
              );
            }

            builtSpans.add(TextSpan(
              text: textSpan.text,
              style: spanStyle,
              recognizer: textSpan.recognizer,
            ));
          } else {
            builtSpans.add(entry.span);
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
