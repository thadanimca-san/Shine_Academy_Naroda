import 'package:flutter/material.dart';


import '../services/speech_service.dart';
import '../theme/app_theme.dart';
import '../../../../dictionary/dictionary_popup.dart';
import '../../../../../core/services/universal_dictionary_service.dart';
import 'admin_edit_button.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
/// Shared word-card tile used by both the per-topic dictionary browser and
/// the global cross-grade search screen, so a word looks the same wherever
/// it's found.
class DictionaryWordCard extends StatelessWidget {
  final Map<String, dynamic> word;
  final String? gradeLabel;

  const DictionaryWordCard({super.key, required this.word, this.gradeLabel});

  @override
  Widget build(BuildContext context) {
    return InkWell(
      borderRadius: BorderRadius.circular(12),
      onTap: () => showModalBottomSheet(
        context: context,
        showDragHandle: true,
        builder: (_) => DictionaryWordDetailSheet(word: word),
      ),
      child: Container(
        padding: const EdgeInsets.all(12),
        decoration: BoxDecoration(
          color: AppColors.paperRaised,
          borderRadius: BorderRadius.circular(12),
          border: Border.all(color: AppColors.rule),
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
            Row(
              children: [
                Container(
                  width: 44,
                  height: 44,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    color: AppColors.saffronTint,
                    borderRadius: BorderRadius.circular(8),
                  ),
                  child: (word['media'] != null && word['media']['emoji'] != null)
                      ? Text(word['media']['emoji'], style: TextStyle(fontSize: 22))
                      : Icon(Icons.menu_book_outlined, color: AppColors.saffronDeep, size: 22),
                ),
                const SizedBox(width: 10),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text(((word['term'] as Map?)?['english'] ?? ''),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(fontWeight: FontWeight.w700, fontSize: 15, color: AppColors.ink)),
                      Text(((word['term'] as Map?)?['hindi'] ?? (word['term'] as Map?)?['hi'] ?? ''),
                          maxLines: 1,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(color: AppColors.tealDeep, fontSize: 13)),
                    ],
                  ),
                ),
                if (gradeLabel != null)
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 7, vertical: 3),
                    decoration: BoxDecoration(
                      color: AppColors.tealTint,
                      borderRadius: BorderRadius.circular(6),
                    ),
                    child: Text(gradeLabel!, style: TextStyle(fontSize: 10, color: AppColors.tealDeep, fontWeight: FontWeight.w600)),
                  ),
              ],
            ),
            const SizedBox(height: 8),
            Expanded(
              child: Text(
                word['definition'] != null && word['definition']['simple'] != null 
                    ? (word['definition']['simple'] is Map ? word['definition']['simple']['en'] ?? '' : word['definition']['simple']) 
                    : '',
                maxLines: 3,
                overflow: TextOverflow.ellipsis,
                style: TextStyle(fontSize: 12.5, color: AppColors.inkSoft),
              ),
            ),
          ],
        ),
      ),
    );
  }
}

class DictionaryWordDetailSheet extends StatelessWidget {
  final Map<String, dynamic> word;

  const DictionaryWordDetailSheet({super.key, required this.word});

  @override
  Widget build(BuildContext context) {
    return SelectionArea(
      contextMenuBuilder: (BuildContext context, SelectableRegionState selectableRegionState) {
        final buttonItems = selectableRegionState.contextMenuButtonItems.toList();
        final selectedText = selectableRegionState.textEditingValue.selection.textInside(selectableRegionState.textEditingValue.text);
        
        if (selectedText.trim().isNotEmpty) {
          buttonItems.insert(0, ContextMenuButtonItem(
            label: '📖 Dictionary',
            onPressed: () {
              selectableRegionState.hideToolbar();
              UniversalDictionaryPopup.show(context, selectedText.trim());
            },
          ));
        }

        return AdaptiveTextSelectionToolbar.buttonItems(
          anchors: selectableRegionState.contextMenuAnchors,
          buttonItems: buttonItems,
        );
      },
      child: SingleChildScrollView(
        child: Padding(
          padding: const EdgeInsets.fromLTRB(24, 8, 24, 32),
          child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          mainAxisSize: MainAxisSize.min,
          children: [
          Center(
            child: Container(
              width: 88,
              height: 88,
              alignment: Alignment.center,
              decoration: BoxDecoration(
                color: AppColors.saffronTint,
                borderRadius: BorderRadius.circular(16),
              ),
              child: (word['media'] != null && word['media']['emoji'] != null)
                  ? Text(word['media']['emoji'], style: TextStyle(fontSize: 44))
                  : Icon(Icons.menu_book_outlined, color: AppColors.saffronDeep, size: 40),
            ),
          ),
          if (word['media'] == null || word['media']['emoji'] == null) ...[
            const SizedBox(height: 6),
            Center(
              child: Text(TrilingualService.instance.getUIText('No picture available for this word yet.'),
                  style: TextStyle(fontSize: 11, color: AppColors.inkFaint, fontStyle: FontStyle.italic)),
            ),
          ],
          const SizedBox(height: 16),
          Row(
            crossAxisAlignment: CrossAxisAlignment.end,
            children: [
              Text(((word['term'] as Map?)?['english'] ?? ''), style: TextStyle(fontSize: 24, fontWeight: FontWeight.w800, color: AppColors.ink)),
              const SizedBox(width: 8),
              Text(word['part_of_speech'] ?? 'noun', style: TextStyle(fontSize: 12, color: AppColors.inkFaint)),
              const Spacer(),
              FutureBuilder<String?>(
                future: UniversalDictionaryService.instance.getSourceFileForTerm(word['id']?.toString() ?? ''),
                builder: (context, snapshot) {
                  if (snapshot.hasData && snapshot.data != null) {
                    return AdminEditButton(
                      jsonPath: snapshot.data!,
                      data: const {},
                    );
                  }
                  return const SizedBox.shrink();
                },
              ),
              IconButton(
                icon: Icon(Icons.volume_up, color: AppColors.tealDeep),
                tooltip: 'Hear pronunciation',
                onPressed: () => SpeechService.instance.speak(((word['term'] as Map?)?['english'] ?? '')),
              ),
            ],
          ),
          Text(
            '${(word['term'] as Map?)?['hindi'] ?? (word['term'] as Map?)?['hi'] ?? ''}  ·  ${(word['term'] as Map?)?['gujarati'] ?? (word['term'] as Map?)?['gu'] ?? ''}',
            style: TextStyle(fontSize: 16, color: AppColors.tealDeep),
          ),
          const SizedBox(height: 12),
          Text(word['definition'] != null && word['definition']['simple'] != null 
                    ? (word['definition']['simple'] is Map ? word['definition']['simple']['en'] ?? '' : word['definition']['simple']) 
                    : '', style: TextStyle(fontSize: 15, color: AppColors.inkSoft)),
          const SizedBox(height: 10),
          
          if (word['examples'] != null && (word['examples'] as List).isNotEmpty)
            ...((word['examples'] as List).map((ex) {
              String exEn = ex is Map ? (ex['en'] ?? '') : ex.toString();
              String exHi = ex is Map ? (ex['hi'] ?? '') : '';
              String exGu = ex is Map ? (ex['gu'] ?? '') : '';
              
              return Container(
                margin: const EdgeInsets.only(bottom: 8),
                width: double.infinity,
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: AppColors.paperRaised,
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('"$exEn"', style: TextStyle(fontStyle: FontStyle.italic, color: AppColors.inkSoft, fontSize: 14)),
                    if (exHi.isNotEmpty)
                      Padding(
                        padding: const EdgeInsets.only(top: 4),
                        child: Text(exHi, style: TextStyle(color: AppColors.inkFaint, fontSize: 13)),
                      ),
                    if (exGu.isNotEmpty)
                      Padding(
                        padding: const EdgeInsets.only(top: 2),
                        child: Text(exGu, style: TextStyle(color: AppColors.inkFaint, fontSize: 13)),
                      ),
                  ],
                ),
              );
            }).toList()),
        ],
      ),
    )));
  }
}
