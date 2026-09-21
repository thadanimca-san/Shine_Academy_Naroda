import 'package:flutter/material.dart';

import '../data/figures_of_speech.dart';
import '../data/figures_of_speech_practice.dart';
import '../models/figure_of_speech.dart';
import '../theme/app_theme.dart';
import '../widgets/admin_edit_button.dart';
import '../widgets/read_aloud_button.dart';
import 'practice_session_screen.dart';
import '../../../../dictionary/dictionary_popup.dart';
import '../../../../common/widgets/tts_interactive_text.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

/// Lists every figure of speech (Simile, Metaphor, ...) with its definition
/// and example count, so a student can pick one to study in depth.
class FiguresOfSpeechListScreen extends StatelessWidget {
  const FiguresOfSpeechListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: BrandAppBar(title: TrilingualService.instance.getUIText('Figures of Speech')),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          Card(
            color: AppColors.tealTint,
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
              leading: const CircleAvatar(
                backgroundColor: AppColors.teal,
                child: Icon(Icons.quiz, color: Colors.white, size: 20),
              ),
              title: Text(TrilingualService.instance.getUIText('Identify the Figure of Speech')),
              subtitle: Text('${figuresOfSpeechPractice.bank.length} MCQ questions to test yourself'),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => PracticeSessionScreen(topic: figuresOfSpeechPractice)),
              ),
            ),
          ),
          const SizedBox(height: 20),
          Text(TrilingualService.instance.getUIText('Class 7-10'), style: Theme.of(context).textTheme.titleMedium),
          const SizedBox(height: 10),
          ..._figureCards(context, figuresOfSpeech),
        ],
      ),
    );
  }

  List<Widget> _figureCards(BuildContext context, List<FigureOfSpeech> figures) {
    return figures
        .map((figure) => Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Card(
                child: ListTile(
                  contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
                  leading: CircleAvatar(
                    backgroundColor: AppColors.saffronTint,
                    child: Text(figure.emoji, style: TextStyle(fontSize: 18)),
                  ),
                  title: Text(figure.name, style: Theme.of(context).textTheme.titleMedium),
                  subtitle: Text('${figure.examples.length} examples · ${figure.definitionEn}',
                      maxLines: 2, overflow: TextOverflow.ellipsis),
                  trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
                  onTap: () => Navigator.of(context).push(
                    MaterialPageRoute(builder: (_) => FigureOfSpeechDetailScreen(figure: figure)),
                  ),
                ),
              ),
            ))
        .toList();
  }
}

/// Shows one figure of speech's definition (English + Hindi), a tip for
/// recognising it, and every worked example with its own explanation.
class FigureOfSpeechDetailScreen extends StatelessWidget {
  final FigureOfSpeech figure;

  const FigureOfSpeechDetailScreen({super.key, required this.figure});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: BrandAppBar(
        title: figure.name,
        actions: [
          AdminEditButton(
            jsonPath: 'app_core/english/figures/${figure.id}.json',
            data: {
              'id': figure.id,
              'name': figure.name,
              'emoji': figure.emoji,
              'level': figure.level,
              'definition_en': figure.definitionEn,
              'definition_hi': figure.definitionHi,
              'recognition_tip': figure.recognitionTip,
              'examples': figure.examples
                  .map((e) => {
                        'sentence': e.sentence,
                        'explanation_en': e.explanationEn,
                        'explanation_hi': e.explanationHi,
                        'hi_transliteration': e.hiTransliteration,
                      })
                  .toList(),
            },
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
        child: ListView(
        padding: const EdgeInsets.all(20),
        children: [
          Center(
            child: Container(
              width: 84,
              height: 84,
              alignment: Alignment.center,
              decoration: BoxDecoration(color: AppColors.saffronTint, borderRadius: BorderRadius.circular(16)),
              child: Text(figure.emoji, style: TextStyle(fontSize: 42)),
            ),
          ),
          const SizedBox(height: 10),
          Center(
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
              decoration: BoxDecoration(color: AppColors.tealTint, borderRadius: BorderRadius.circular(8)),
              child: Text(figure.level,
                  style: TextStyle(fontSize: 12, fontWeight: FontWeight.w700, color: AppColors.tealDeep)),
            ),
          ),
          const SizedBox(height: 20),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              color: AppColors.paperRaised,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: AppColors.rule),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Text(TrilingualService.instance.getUIText('Definition'), style: TextStyle(fontWeight: FontWeight.w700, color: AppColors.saffronDeep)),
                const SizedBox(height: 6),
                Text(figure.definitionEn, style: TextStyle(fontSize: 15, height: 1.5, color: AppColors.ink)),
                const SizedBox(height: 10),
                Text('${figure.definitionHi}  ·  ${figure.hiTransliteration}',
                    style: TextStyle(fontSize: 13.5, color: AppColors.tealDeep, height: 1.4)),
              ],
            ),
          ),
          const SizedBox(height: 12),
          Container(
            padding: const EdgeInsets.all(14),
            decoration: BoxDecoration(
              color: AppColors.tealTint,
              borderRadius: BorderRadius.circular(12),
              border: Border.all(color: AppColors.rule),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(Icons.lightbulb_outline, color: AppColors.tealDeep, size: 20),
                const SizedBox(width: 10),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(TrilingualService.instance.getUIText('How to spot it'), style: TextStyle(fontWeight: FontWeight.w700, color: AppColors.tealDeep, fontSize: 13)),
                      const SizedBox(height: 4),
                      Text(figure.recognitionTip, style: TextStyle(fontSize: 13.5, color: AppColors.inkSoft, height: 1.4)),
                    ],
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 24),
          Text('${figure.examples.length} examples', style: Theme.of(context).textTheme.titleMedium),
          const SizedBox(height: 10),
          ...figure.examples.map((example) => Padding(
                padding: const EdgeInsets.only(bottom: 10),
                child: Container(
                  padding: const EdgeInsets.all(14),
                  decoration: BoxDecoration(
                    color: AppColors.paperRaised,
                    borderRadius: BorderRadius.circular(12),
                    border: Border.all(color: AppColors.rule),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          TtsInteractiveText(
                              text: '"${example.sentence}"',
                              fullTtsText: example.sentence,
                              style: TextStyle(
                                  fontSize: 15, fontWeight: FontWeight.w600, color: AppColors.ink, height: 1.4)),
                          const SizedBox(height: 12),
                          ReadAloudButton(text: example.sentence, label: 'Listen', forceLanguage: 'en'),
                        ],
                      ),
                      const SizedBox(height: 8),
                      Text(example.explanationEn, style: TextStyle(fontSize: 13, color: AppColors.inkSoft, height: 1.4)),
                      const SizedBox(height: 6),
                      Text('${example.explanationHi}  ·  ${example.hiTransliteration}',
                          style: TextStyle(fontSize: 12.5, color: AppColors.tealDeep, height: 1.4)),
                    ],
                  ),
                ),
              )),
        ],
      ),
      ),
    );
  }
}
