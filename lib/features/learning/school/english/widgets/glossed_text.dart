import 'package:flutter/gestures.dart';
import 'package:flutter/material.dart';

import '../models/chapter.dart' show InlineGloss;
import '../theme/app_theme.dart';
import '../../../../../core/services/tts_service.dart';

/// Renders paragraphs of English text with difficult words glossed inline:
/// tapping a glossed word shows its Hindi meaning right where it occurs,
/// instead of sending the student to a separate dictionary lookup. Shared
/// between Chapters and Reading Passages so both use the same tap-to-reveal
/// behavior.
class GlossedText extends StatelessWidget {
  final String text;
  final List<InlineGloss> glosses;
  final TextStyle? baseStyle;

  const GlossedText({super.key, required this.text, required this.glosses, this.baseStyle});

  @override
  Widget build(BuildContext context) {
    if (glosses.isEmpty) {
      return Text(text, style: baseStyle ?? TextStyle(fontSize: 16, height: 1.65, color: AppColors.ink));
    }

    // Sort glosses longest-word-first so multi-word glosses like "banyan tree"
    // are matched before a shorter overlapping single word would be.
    final glossesByLength = [...glosses]..sort((a, b) => b.word.length.compareTo(a.word.length));

    final paragraphs = text.split('\n\n');

    return Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        for (final paragraph in paragraphs) ...[
          _buildParagraph(context, paragraph, glossesByLength),
          const SizedBox(height: 14),
        ],
      ],
    );
  }

  Widget _buildParagraph(BuildContext context, String paragraph, List<InlineGloss> sortedGlosses) {
    return ValueListenableBuilder<TtsProgress>(
      valueListenable: TTSService.instance.progress,
      builder: (context, progress, child) {
        int globalStart = -1;
        int globalEnd = -1;
        
        final searchTarget = text.toLowerCase();
        final searchProgress = progress.text.toLowerCase().trim();
        
        if (progress.text.isNotEmpty && searchTarget.contains(searchProgress)) {
          int chunkOffsetInFull = searchTarget.indexOf(searchProgress);
          if (chunkOffsetInFull != -1) {
            globalStart = chunkOffsetInFull + progress.startOffset;
            globalEnd = chunkOffsetInFull + progress.endOffset;
          }
        }
        
        int paraOffset = text.indexOf(paragraph);
        int localStart = globalStart - paraOffset;
        int localEnd = globalEnd - paraOffset;
        
        // If out of bounds of this paragraph, just render normal glosses
        bool hasHighlight = localStart >= 0 && localEnd <= paragraph.length && localStart < localEnd;

        final spans = <InlineSpan>[];
        var remaining = paragraph;
        int currentIndex = 0;

        while (remaining.isNotEmpty) {
          InlineGloss? match;
          int matchIndex = -1;

          for (final gloss in sortedGlosses) {
            final idx = remaining.toLowerCase().indexOf(gloss.word.toLowerCase());
            if (idx != -1 && (matchIndex == -1 || idx < matchIndex)) {
              matchIndex = idx;
              match = gloss;
            }
          }

          if (match == null) {
            _addTtsSpans(spans, remaining, currentIndex, localStart, localEnd, false, null);
            break;
          }

          if (matchIndex > 0) {
            String beforeMatch = remaining.substring(0, matchIndex);
            _addTtsSpans(spans, beforeMatch, currentIndex, localStart, localEnd, false, null);
            currentIndex += beforeMatch.length;
          }

          final matchedText = remaining.substring(matchIndex, matchIndex + match.word.length);
          _addTtsSpans(spans, matchedText, currentIndex, localStart, localEnd, true, () => _showGlossPopup(context, match!));
          
          currentIndex += matchedText.length;
          remaining = remaining.substring(matchIndex + match.word.length);
        }

        return RichText(
          textScaler: MediaQuery.textScalerOf(context),
          text: TextSpan(
            style: baseStyle ?? TextStyle(fontSize: 16, height: 1.65, color: AppColors.ink),
            children: spans,
          ),
        );
      },
    );
  }

  void _addTtsSpans(List<InlineSpan> spans, String text, int textStartIndex, int hlStart, int hlEnd, bool isGloss, VoidCallback? onTap) {
    TextStyle style = isGloss
        ? TextStyle(
            color: AppColors.tealDeep,
            fontWeight: FontWeight.w700,
            decoration: TextDecoration.underline,
            decorationStyle: TextDecorationStyle.dotted,
          )
        : TextStyle();

    int textEndIndex = textStartIndex + text.length;

    // No overlap
    if (hlEnd <= textStartIndex || hlStart >= textEndIndex) {
      spans.add(TextSpan(text: text, style: style, recognizer: isGloss ? (TapGestureRecognizer()..onTap = onTap) : null));
      return;
    }

    // Full overlap
    if (hlStart <= textStartIndex && hlEnd >= textEndIndex) {
      spans.add(TextSpan(
        text: text,
        style: style.copyWith(backgroundColor: Colors.yellow, color: Colors.black87),
        recognizer: isGloss ? (TapGestureRecognizer()..onTap = onTap) : null,
      ));
      return;
    }

    // Partial overlap - split into up to 3 parts
    int relStart = (hlStart > textStartIndex) ? (hlStart - textStartIndex) : 0;
    int relEnd = (hlEnd < textEndIndex) ? (hlEnd - textStartIndex) : text.length;

    if (relStart > 0) {
      spans.add(TextSpan(text: text.substring(0, relStart), style: style, recognizer: isGloss ? (TapGestureRecognizer()..onTap = onTap) : null));
    }
    
    spans.add(TextSpan(
      text: text.substring(relStart, relEnd),
      style: style.copyWith(backgroundColor: Colors.yellow, color: Colors.black87),
      recognizer: isGloss ? (TapGestureRecognizer()..onTap = onTap) : null,
    ));
    
    if (relEnd < text.length) {
      spans.add(TextSpan(text: text.substring(relEnd), style: style, recognizer: isGloss ? (TapGestureRecognizer()..onTap = onTap) : null));
    }
  }

  void _showGlossPopup(BuildContext context, InlineGloss gloss) {
    showModalBottomSheet(
      context: context,
      showDragHandle: true,
      builder: (_) => Padding(
        padding: const EdgeInsets.fromLTRB(24, 8, 24, 32),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Text(gloss.word, style: TextStyle(fontSize: 20, fontWeight: FontWeight.w800, color: AppColors.ink)),
            const SizedBox(height: 6),
            Text(
              '${gloss.meaningHi}  ·  ${gloss.hiTransliteration}',
              style: TextStyle(fontSize: 17, color: AppColors.tealDeep),
            ),
            if (gloss.meaningGu != null) ...[
              const SizedBox(height: 4),
              Text(
                '${gloss.meaningGu}  ·  ${gloss.guTransliteration}',
                style: TextStyle(fontSize: 17, color: AppColors.saffron),
              ),
            ],
          ],
        ),
      ),
    );
  }
}
