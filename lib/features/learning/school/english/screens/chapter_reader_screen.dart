import 'package:flutter/material.dart';

import '../../../../../core/engine/local_content_manager.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';
import '../models/chapter.dart';
import '../theme/app_theme.dart';
import '../widgets/admin_edit_button.dart';
import '../widgets/glossed_text.dart';
import '../widgets/read_aloud_button.dart';
import '../../../../dictionary/dictionary_popup.dart';
import '../../../../common/widgets/tts_interactive_text.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Renders a chapter's English text with its difficult words glossed
/// inline: tapping a glossed word shows its Hindi meaning right where it
/// occurs, instead of sending the student to a separate dictionary lookup.
///
/// Language switcher: English (always visible) / Hindi / Gujarati.
/// Students can always see how to return to English — no hidden toggle.
///
/// Admin: tap the 🟠 edit icon → PIN 9999 → opens the same ContentEditorScreen
/// used everywhere else in the app. Edits are saved locally via
/// LocalContentManager and reloaded immediately when the editor closes.
class ChapterReaderScreen extends StatefulWidget {
  final Chapter chapter;

  const ChapterReaderScreen({super.key, required this.chapter});

  @override
  State<ChapterReaderScreen> createState() => _ChapterReaderScreenState();
}


class _ChapterReaderScreenState extends State<ChapterReaderScreen> {

  /// The live chapter data — starts as the Dart const, may be overridden by
  /// a locally-edited JSON file after the admin saves changes.
  late Chapter _chapter;

  @override
  void initState() {
    super.initState();
    _chapter = widget.chapter;
    _tryLoadLocalOverride();
    TrilingualService.instance.addListener(_onLangChange);
  }

  void _onLangChange() {
    if (mounted) setState(() {});
  }

  @override
  void dispose() {
    TrilingualService.instance.removeListener(_onLangChange);
    super.dispose();
  }

  /// Try to load an admin-edited JSON override from LocalContentManager.
  /// If one exists (the admin has saved at least once), use it instead of
  /// the bundled Dart const so edits are reflected without a rebuild.
  Future<void> _tryLoadLocalOverride() async {
    try {
      await LocalContentManager.instance.init();
      final jsonPath = _jsonPathFor(_chapter.id);
      final data = await LocalContentManager.instance.readLocalJson(jsonPath);
      if (data != null && mounted) {
        // Only use it if it looks like a valid chapter override
        if (data.containsKey('chapter_text') || data.containsKey('title')) {
          setState(() => _chapter = Chapter.fromJson(data));
        }
      }
    } catch (e) {
      debugPrint('ChapterReaderScreen: could not load local override: $e');
    }
  }

  String _jsonPathFor(String id) =>
      'app_core/english/chapters/$id.json';

  @override
  Widget build(BuildContext context) {
    final chapter = _chapter;
    final hasHindi = chapter.hindiSummary.isNotEmpty;
    final hasGujarati =
        chapter.gujaratiSummary != null && chapter.gujaratiSummary!.isNotEmpty;

    return Scaffold(
      appBar: BrandAppBar(
        title: chapter.title,
        actions: [
          AdminEditButton(
            jsonPath: _jsonPathFor(chapter.id),
            data: chapter.toJson(),
            onEditorClosed: _tryLoadLocalOverride, // reload after editing
          ),
        ],
      ),
      body: SelectionArea(
        contextMenuBuilder:
            (BuildContext context, SelectableRegionState selectableRegionState) {
          final buttonItems =
              selectableRegionState.contextMenuButtonItems.toList();
          final selectedText = selectableRegionState.textEditingValue.selection
              .textInside(selectableRegionState.textEditingValue.text);

          if (selectedText.trim().isNotEmpty) {
            buttonItems.insert(
                0,
                ContextMenuButtonItem(
                  label: '📖 Dictionary',
                  onPressed: () {
                    selectableRegionState.hideToolbar();
                    UniversalDictionaryPopup.show(
                        context, selectedText.trim());
                  },
                ));
          }

          return AdaptiveTextSelectionToolbar.buttonItems(
            anchors: selectableRegionState.contextMenuAnchors,
            buttonItems: buttonItems,
          );
        },
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // ── Emoji icon ────────────────────────────────────────────────
              Center(
                child: Container(
                  width: 80,
                  height: 80,
                  alignment: Alignment.center,
                  decoration: BoxDecoration(
                    color: AppColors.saffronTint,
                    borderRadius: BorderRadius.circular(16),
                  ),
                  child:
                      Text(chapter.emoji, style: TextStyle(fontSize: 40)),
                ),
              ),
              const SizedBox(height: 8),
              Center(
                child: Text(chapter.grade,
                    style: TextStyle(
                        color: AppColors.inkFaint, fontSize: 12.5)),
              ),
              const SizedBox(height: 20),

              // ── Content ───────────────────────────────────────────────────
              if (TrilingualService.instance.activeViewLanguage == 'hi' && hasHindi) ...[
                Center(child: ReadAloudButton(text: chapter.hindiText ?? chapter.hindiSummary, label: 'सुनें (Listen)')),
                const SizedBox(height: 12),
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: AppColors.tealTint,
                    borderRadius: BorderRadius.circular(10),
                    border: Border.all(color: AppColors.rule),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(children: [
                        Text(TrilingualService.instance.getUIText('🇮🇳'), style: TextStyle(fontSize: 16)),
                        SizedBox(width: 8),
                        Text(TrilingualService.instance.getUIText('हिंदी में पाठ'),
                            style: TextStyle(
                                fontWeight: FontWeight.w700,
                                fontSize: 14,
                                color: AppColors.tealDeep)),
                      ]),
                      const SizedBox(height: 12),
                      TtsInteractiveText(
                        text: chapter.hindiText ?? chapter.hindiSummary,
                        style: TextStyle(
                            fontSize: 30,
                            height: 1.7,
                            color: AppColors.ink,
                            fontWeight: FontWeight.w500).adaptToLanguage(),
                      ),
                    ],
                  ),
                ),
              ] else if (TrilingualService.instance.activeViewLanguage == 'gu' && hasGujarati) ...[
                Center(child: ReadAloudButton(text: chapter.gujaratiText ?? chapter.gujaratiSummary!, label: 'સાંભળો (Listen)')),
                const SizedBox(height: 12),
                Container(
                  width: double.infinity,
                  padding: const EdgeInsets.all(16),
                  decoration: BoxDecoration(
                    color: const Color(0xFFFFF3E0),
                    borderRadius: BorderRadius.circular(10),
                    border: Border.all(color: const Color(0xFFFFB74D)),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Row(children: [
                        Text(TrilingualService.instance.getUIText('🏛️'), style: TextStyle(fontSize: 16)),
                        SizedBox(width: 8),
                        Text(TrilingualService.instance.getUIText('ગુજરાતીમાં પાઠ'),
                            style: TextStyle(
                                fontWeight: FontWeight.w700,
                                fontSize: 14,
                                color: Color(0xFFE65100))),
                      ]),
                      const SizedBox(height: 12),
                      TtsInteractiveText(
                        text: chapter.gujaratiText ?? chapter.gujaratiSummary!,
                        style: TextStyle(
                            fontSize: 30,
                            height: 1.7,
                            color: AppColors.ink,
                            fontWeight: FontWeight.w500).adaptToLanguage(),
                      ),
                    ],
                  ),
                ),
              ] else ...[
                Center(
                    child: ReadAloudButton(
                        text: chapter.chapterText,
                        label: 'Read the chapter aloud')),
                const SizedBox(height: 12),
                Text(TrilingualService.instance.getUIText('Tap any underlined word for its meaning.'),
                  style: TextStyle(
                      fontSize: 11.5,
                      color: AppColors.inkFaint,
                      fontStyle: FontStyle.italic),
                ),
                const SizedBox(height: 12),
                GlossedText(text: chapter.chapterText, glosses: chapter.glosses, baseStyle: const TextStyle(fontSize: 24, height: 1.7, color: AppColors.ink).adaptToLanguage()),
              ],
            ],
          ),
        ),
      ),
    );
  }

}
