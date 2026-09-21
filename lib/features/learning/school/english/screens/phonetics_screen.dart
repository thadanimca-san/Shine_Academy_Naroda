import 'package:flutter/material.dart';

import '../data/phonetics_topics.dart';
import '../models/phonetics.dart';
import '../services/speech_service.dart';
import '../theme/app_theme.dart';
import '../widgets/admin_edit_button.dart';
import '../../../../dictionary/dictionary_popup.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

/// Grade picker for Phonetics — sounds, minimal pairs, and letter-sound
/// rules, one library per grade.
class PhoneticsGradeListScreen extends StatelessWidget {
  const PhoneticsGradeListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final grades = phoneticsLibraryByGrade.keys.toList();
    return Scaffold(
      appBar: BrandAppBar(title: TrilingualService.instance.getUIText('Phonetics')),
      body: ListView.separated(
        padding: const EdgeInsets.all(16),
        itemCount: grades.length,
        separatorBuilder: (_, _) => const SizedBox(height: 10),
        itemBuilder: (context, index) {
          final grade = grades[index];
          final library = phoneticsLibraryByGrade[grade]!;
          return Card(
            child: ListTile(
              contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
              leading: CircleAvatar(
                backgroundColor: AppColors.saffronTint,
                child: Text(TrilingualService.instance.getUIText('🔊'), style: TextStyle(fontSize: 18)),
              ),
              title: Text(grade, style: Theme.of(context).textTheme.titleMedium),
              subtitle: Text(
                '${library.phonemes.length} sounds · ${library.minimalPairs.length} word pairs · ${library.letterSoundRules.length} spelling rules',
              ),
              trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
              onTap: () => Navigator.of(context).push(
                MaterialPageRoute(builder: (_) => PhoneticsLibraryScreen(library: library)),
              ),
            ),
          );
        },
      ),
    );
  }
}

class PhoneticsLibraryScreen extends StatelessWidget {
  final PhoneticsLibrary library;

  const PhoneticsLibraryScreen({super.key, required this.library});

  @override
  Widget build(BuildContext context) {
    return DefaultTabController(
      length: 3,
      child: Scaffold(
        appBar: BrandAppBar(
          title: '${library.grade} Phonetics',
          actions: [
            AdminEditButton(
              jsonPath: 'app_core/english/phonetics/${library.id}.json',
              data: {
                'id': library.id,
                'grade': library.grade,
                'title': library.title,
                'phoneme_count': library.phonemes.length,
                'note': 'Phonetics data is in lib/features/learning/school/english/data/phonetics_${library.grade.toLowerCase().replaceAll(' ', '')}.dart',
              },
            ),
          ],
          bottom: const TabBar(
            labelColor: AppColors.saffronDeep,
            unselectedLabelColor: AppColors.inkFaint,
            indicatorColor: AppColors.saffron,
            tabs: [
              Tab(text: 'Sounds'),
              Tab(text: 'Word Pairs'),
              Tab(text: 'Spelling Rules'),
            ],
          ),
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
          child: TabBarView(
            children: [
              _PhonemeList(phonemes: library.phonemes),
              _MinimalPairList(pairs: library.minimalPairs),
              _LetterSoundRuleList(rules: library.letterSoundRules),
            ],
          ),
        ),
      ),
    );
  }
}

class _PhonemeList extends StatelessWidget {
  final List<PhonemeEntry> phonemes;

  const _PhonemeList({required this.phonemes});

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      padding: const EdgeInsets.all(16),
      itemCount: phonemes.length,
      separatorBuilder: (_, _) => const SizedBox(height: 10),
      itemBuilder: (context, index) => _PhonemeCard(phoneme: phonemes[index]),
    );
  }
}

class _PhonemeCard extends StatelessWidget {
  final PhonemeEntry phoneme;

  const _PhonemeCard({required this.phoneme});

  @override
  Widget build(BuildContext context) {
    return Container(
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: AppColors.paperRaised,
        borderRadius: BorderRadius.circular(12),
        border: Border.all(color: AppColors.rule),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Container(
                width: 48,
                height: 48,
                alignment: Alignment.center,
                decoration: BoxDecoration(color: AppColors.saffronTint, borderRadius: BorderRadius.circular(10)),
                child: Text(phoneme.ipaSymbol, style: TextStyle(fontSize: 18, fontWeight: FontWeight.w700, color: AppColors.saffronDeep)),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(phoneme.label, style: TextStyle(fontWeight: FontWeight.w700, fontSize: 15, color: AppColors.ink)),
                    Text(phoneme.soundsLike, style: TextStyle(fontSize: 12.5, color: AppColors.inkFaint)),
                  ],
                ),
              ),
              _SoundButton(
                onPressed: phoneme.exampleWords.isEmpty
                    ? null
                    : () => SpeechService.instance.speak(phoneme.exampleWords.first),
              ),
            ],
          ),
          const SizedBox(height: 10),
          Text(phoneme.mouthTip, style: TextStyle(fontSize: 13, color: AppColors.inkSoft, height: 1.4)),
          const SizedBox(height: 8),
          Wrap(
            spacing: 8,
            runSpacing: 6,
            children: phoneme.exampleWords
                .map((w) => InkWell(
                      borderRadius: BorderRadius.circular(20),
                      onTap: () => SpeechService.instance.speak(w),
                      child: Container(
                        padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                        decoration: BoxDecoration(color: AppColors.tealTint, borderRadius: BorderRadius.circular(20)),
                        child: Row(
                          mainAxisSize: MainAxisSize.min,
                          children: [
                            Icon(Icons.volume_up, size: 13, color: AppColors.tealDeep),
                            const SizedBox(width: 4),
                            Text(w, style: TextStyle(fontSize: 12.5, color: AppColors.tealDeep, fontWeight: FontWeight.w600)),
                          ],
                        ),
                      ),
                    ))
                .toList(),
          ),
        ],
      ),
    );
  }
}

class _MinimalPairList extends StatelessWidget {
  final List<MinimalPair> pairs;

  const _MinimalPairList({required this.pairs});

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      padding: const EdgeInsets.all(16),
      itemCount: pairs.length,
      separatorBuilder: (_, _) => const SizedBox(height: 10),
      itemBuilder: (context, index) {
        final pair = pairs[index];
        return Container(
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(
            color: AppColors.paperRaised,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(color: AppColors.rule),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Expanded(
                    child: Row(
                      children: [
                        Expanded(
                          child: Text(pair.wordA,
                              style: TextStyle(fontWeight: FontWeight.w700, fontSize: 16, color: AppColors.ink)),
                        ),
                        _SoundButton(onPressed: () => SpeechService.instance.speak(pair.wordA)),
                      ],
                    ),
                  ),
                  Padding(
                    padding: EdgeInsets.symmetric(horizontal: 8),
                    child: Text(TrilingualService.instance.getUIText('vs'), style: TextStyle(color: AppColors.inkFaint, fontSize: 12)),
                  ),
                  Expanded(
                    child: Row(
                      children: [
                        Expanded(
                          child: Text(pair.wordB,
                              style: TextStyle(fontWeight: FontWeight.w700, fontSize: 16, color: AppColors.ink)),
                        ),
                        _SoundButton(onPressed: () => SpeechService.instance.speak(pair.wordB)),
                      ],
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 8),
              Text(pair.contrastExplanation, style: TextStyle(fontSize: 12.5, color: AppColors.inkSoft, height: 1.4)),
            ],
          ),
        );
      },
    );
  }
}

class _LetterSoundRuleList extends StatelessWidget {
  final List<LetterSoundRule> rules;

  const _LetterSoundRuleList({required this.rules});

  @override
  Widget build(BuildContext context) {
    return ListView.separated(
      padding: const EdgeInsets.all(16),
      itemCount: rules.length,
      separatorBuilder: (_, _) => const SizedBox(height: 10),
      itemBuilder: (context, index) {
        final rule = rules[index];
        return Container(
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(
            color: AppColors.paperRaised,
            borderRadius: BorderRadius.circular(12),
            border: Border.all(color: AppColors.rule),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
                    decoration: BoxDecoration(color: AppColors.saffronTint, borderRadius: BorderRadius.circular(8)),
                    child: Text('"${rule.letters}"',
                        style: TextStyle(fontWeight: FontWeight.w700, fontSize: 15, color: AppColors.saffronDeep)),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Text(rule.soundDescription, style: TextStyle(fontSize: 13, color: AppColors.inkSoft)),
                  ),
                ],
              ),
              const SizedBox(height: 8),
              Wrap(
                spacing: 8,
                runSpacing: 6,
                children: rule.exampleWords
                    .map((w) => InkWell(
                          borderRadius: BorderRadius.circular(20),
                          onTap: () => SpeechService.instance.speak(w),
                          child: Container(
                            padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 5),
                            decoration: BoxDecoration(color: AppColors.tealTint, borderRadius: BorderRadius.circular(20)),
                            child: Row(
                              mainAxisSize: MainAxisSize.min,
                              children: [
                                Icon(Icons.volume_up, size: 13, color: AppColors.tealDeep),
                                const SizedBox(width: 4),
                                Text(w, style: TextStyle(fontSize: 12.5, color: AppColors.tealDeep, fontWeight: FontWeight.w600)),
                              ],
                            ),
                          ),
                        ))
                    .toList(),
              ),
            ],
          ),
        );
      },
    );
  }
}

/// Tap-to-hear button, speaks aloud via device text-to-speech.
class _SoundButton extends StatelessWidget {
  final VoidCallback? onPressed;

  const _SoundButton({required this.onPressed});

  @override
  Widget build(BuildContext context) {
    final hasAudio = onPressed != null;
    return IconButton(
      icon: Icon(Icons.volume_up, size: 20, color: hasAudio ? AppColors.tealDeep : AppColors.inkFaint),
      tooltip: hasAudio ? 'Play sound' : 'No sound available',
      onPressed: onPressed,
    );
  }
}
