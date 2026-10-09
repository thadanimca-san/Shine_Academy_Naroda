import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:flutter_markdown/flutter_markdown.dart';
import 'package:flutter_markdown_latex/flutter_markdown_latex.dart';
import 'package:markdown/markdown.dart' as md;
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

    for (int i = 0; i < widget.text.length; i++) {
      String char = widget.text[i];

      if (char == '\$') {
        _commitWord(isBold, isItalic);
        bool isBlock = false;
        int j = i + 1;
        if (j < widget.text.length && widget.text[j] == '\$') {
           isBlock = true;
           j++;
        }
        int start = j;
        int end = -1;
        while (j < widget.text.length) {
           if (widget.text[j] == '\$') {
              if (isBlock && j + 1 < widget.text.length && widget.text[j+1] == '\$') {
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
           String mathContent = widget.text.substring(start, end);
           // Fix JSON parsing bug where \not becomes a newline + ot
           mathContent = mathContent.replaceAll('\n', '\\n');
           
           // Fix flutter_math_fork crash when \not is used with \implies
           mathContent = mathContent.replaceAll(r'\not\implies', r'\not\Rightarrow');
           mathContent = mathContent.replaceAll(r'\not \implies', r'\not \Rightarrow');
           
           if (widget.isPdfMode) {
              _cleanText += ' ';
              // In PDF mode, MarkdownBody with flutter_math_fork hangs the offstage renderer
              // because KaTeX fonts aren't globally pre-loaded. We fallback to plain text.
              _spans.add(TextSpan(
                 text: ' ' + mathContent + ' ', 
                 style: widget.style?.copyWith(fontWeight: FontWeight.bold) ?? const TextStyle(fontWeight: FontWeight.bold),
              ));
              i = j - 1;
              continue;
           }

           String fullMathString = isBlock ? '\$\$$mathContent\$\$' : '\$$mathContent\$';
           
           _cleanText += ' '; // Add space for TTS to skip it smoothly
           
           _spans.add(WidgetSpan(
              alignment: PlaceholderAlignment.middle,
              child: Builder(
                builder: (context) {
                  return MediaQuery(
                    data: MediaQuery.of(context).copyWith(
                      // Prevent double scaling (AppTypography already scales)
                      textScaler: TextScaler.noScaling,
                    ),
                    child: MarkdownBody(
                      data: fullMathString,
                      builders: {
                        'latex': LatexElementBuilder(
                           textStyle: widget.style ?? AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface),
                        ),
                      },
                      extensionSet: md.ExtensionSet(
                        [LatexBlockSyntax()],
                        [LatexInlineSyntax()],
                      ),
                      styleSheet: MarkdownStyleSheet(
                         p: widget.style ?? AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface),
                         pPadding: EdgeInsets.zero,
                      ),
                  ),
                  );
                }
              ),
           ));
           i = j - 1; // Advance outer loop
           continue;
        }
      }

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
