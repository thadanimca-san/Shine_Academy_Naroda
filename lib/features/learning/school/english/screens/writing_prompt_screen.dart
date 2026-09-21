import 'package:flutter/material.dart';

import '../../../../../core/engine/local_content_manager.dart';
import '../models/writing_prompt.dart';
import '../theme/app_theme.dart';
import '../widgets/admin_edit_button.dart';
import '../widgets/read_aloud_button.dart';
import '../../../../dictionary/dictionary_popup.dart';
import '../../../../common/widgets/tts_interactive_text.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

/// A student writes their own picture description in a free-text box, then
/// reveals a model answer to compare against — self-assessed, not
/// auto-graded, since scoring free text well needs more than this app does.
class WritingPromptScreen extends StatefulWidget {
  final WritingPrompt prompt;
  final String? grade;

  const WritingPromptScreen({super.key, required this.prompt, this.grade});

  @override
  State<WritingPromptScreen> createState() => _WritingPromptScreenState();
}

class _WritingPromptScreenState extends State<WritingPromptScreen> {
  final _controller = TextEditingController();
  bool _revealed = false;
  late WritingPrompt _prompt;

  @override
  void initState() {
    super.initState();
    _prompt = widget.prompt;
    _tryLoadLocalOverride();
  }

  String get _jsonPath => 'app_core/english/writing/${_prompt.id}.json';

  Future<void> _tryLoadLocalOverride() async {
    try {
      await LocalContentManager.instance.init();
      final data = await LocalContentManager.instance.readLocalJson(_jsonPath);
      if (data != null && mounted && data.containsKey('title')) {
        setState(() => _prompt = WritingPrompt.fromJson(data));
      }
    } catch (e) {
      debugPrint('WritingPromptScreen: could not load local override: $e');
    }
  }

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final prompt = _prompt;
    return Scaffold(
      appBar: BrandAppBar(
        title: prompt.title,
        actions: [
          AdminEditButton(
            jsonPath: _jsonPath,
            data: _prompt.toJson(),
            onEditorClosed: _tryLoadLocalOverride,
          ),
        ],
      ),
      body: SelectionArea(
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
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            Center(
              child: Container(
                width: double.infinity,
                padding: const EdgeInsets.symmetric(vertical: 24),
                decoration: BoxDecoration(color: AppColors.saffronTint, borderRadius: BorderRadius.circular(16)),
                child: Text(prompt.sceneEmoji, style: TextStyle(fontSize: 40), textAlign: TextAlign.center),
              ),
            ),
            const SizedBox(height: 12),
            Text(prompt.sceneDescription, style: TextStyle(fontSize: 14.5, color: AppColors.inkSoft, height: 1.5)),
            const SizedBox(height: 18),
            Text(TrilingualService.instance.getUIText('Word bank'), style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: 8),
            Wrap(
              spacing: 8,
              runSpacing: 8,
              children: prompt.wordBank
                  .map((w) => Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                        decoration: BoxDecoration(color: AppColors.tealTint, borderRadius: BorderRadius.circular(20)),
                        child: Text(w, style: TextStyle(fontSize: 12.5, color: AppColors.tealDeep, fontWeight: FontWeight.w600)),
                      ))
                  .toList(),
            ),
            const SizedBox(height: 20),
            Text(TrilingualService.instance.getUIText('Write your description (3-5 sentences)'), style: Theme.of(context).textTheme.titleMedium),
            const SizedBox(height: 8),
            TextField(
              controller: _controller,
              maxLines: 6,
              decoration: InputDecoration(
                hintText: 'Start writing here...',
                filled: true,
                fillColor: AppColors.paperRaised,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(10),
                  borderSide: const BorderSide(color: AppColors.rule),
                ),
                contentPadding: const EdgeInsets.all(14),
              ),
            ),
            const SizedBox(height: 16),
            if (!_revealed)
              SizedBox(
                width: double.infinity,
                child: FilledButton(
                  onPressed: () => setState(() => _revealed = true),
                  style: FilledButton.styleFrom(
                    backgroundColor: AppColors.saffron,
                    padding: const EdgeInsets.symmetric(vertical: 14),
                  ),
                  child: Text(TrilingualService.instance.getUIText('Compare with a model answer')),
                ),
              ),
            if (_revealed) ...[
              Container(
                width: double.infinity,
                padding: const EdgeInsets.all(16),
                decoration: BoxDecoration(
                  color: AppColors.tealTint,
                  borderRadius: BorderRadius.circular(12),
                  border: Border.all(color: AppColors.rule),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(TrilingualService.instance.getUIText('Model answer'), style: TextStyle(fontWeight: FontWeight.w700, color: AppColors.tealDeep)),
                        const SizedBox(height: 12),
                        ReadAloudButton(text: prompt.modelAnswer, label: 'Listen', forceLanguage: 'en'),
                      ],
                    ),
                    const SizedBox(height: 8),
                    TtsInteractiveText(text: prompt.modelAnswer, style: TextStyle(fontSize: 14.5, height: 1.6, color: AppColors.ink)),
                  ],
                ),
              ),
              const SizedBox(height: 14),
              Text(TrilingualService.instance.getUIText('What makes this a good description'), style: TextStyle(fontWeight: FontWeight.w700, fontSize: 13.5)),
              const SizedBox(height: 8),
              ...prompt.modelAnswerHighlights.map((h) => Padding(
                    padding: const EdgeInsets.only(bottom: 6),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Icon(Icons.check_circle_outline, size: 16, color: AppColors.success),
                        const SizedBox(width: 8),
                        Expanded(child: Text(h, style: TextStyle(fontSize: 13, color: AppColors.inkSoft))),
                      ],
                    ),
                  )),
            ],
          ],
        ),
      ),
      ),
    );
  }
}
