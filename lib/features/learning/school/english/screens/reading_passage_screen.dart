import 'package:flutter/material.dart';

import '../../../../../core/engine/local_content_manager.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';
import '../models/practice_question.dart';
import '../models/reading_passage.dart';
import '../theme/app_theme.dart';
import '../widgets/admin_edit_button.dart';
import '../widgets/glossed_text.dart';
import '../widgets/read_aloud_button.dart';
import '../../../../dictionary/dictionary_popup.dart';
import '../../../../common/widgets/tts_interactive_text.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Shows a passage's body first, then flows into its comprehension
/// questions using the same answer → explanation → next pattern as grammar
/// practice, so the two skills feel like one consistent app, not two.
class ReadingPassageScreen extends StatefulWidget {
  final ReadingPassage passage;

  const ReadingPassageScreen({super.key, required this.passage});

  @override
  State<ReadingPassageScreen> createState() => _ReadingPassageScreenState();
}

enum _Stage { active, done }

class _ReadingPassageScreenState extends State<ReadingPassageScreen> {
  _Stage _stage = _Stage.active;
  int _questionIndex = 0;
  int? _selectedOption;
  bool _revealed = false;
  int _correctCount = 0;

  late ReadingPassage _passage;

  @override
  void initState() {
    super.initState();
    _passage = widget.passage;
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

  String get _jsonPath =>
      'app_core/english/reading/${_passage.id}.json';

  Future<void> _tryLoadLocalOverride() async {
    try {
      await LocalContentManager.instance.init();
      final data =
          await LocalContentManager.instance.readLocalJson(_jsonPath);
      if (data != null && mounted && data.containsKey('body')) {
        setState(() {
          _passage = ReadingPassage.fromJson(data);
        });
      }
    } catch (e) {
      debugPrint('ReadingPassageScreen: could not load local override: $e');
    }
  }

  void _selectOption(int index) {
    if (_revealed) return;
    final question = _passage.questions[_questionIndex];
    setState(() {
      _selectedOption = index;
      _revealed = true;
      if (index == question.correctIndex) _correctCount++;
    });
  }

  void _next() {
    if (_questionIndex + 1 < _passage.questions.length) {
      setState(() {
        _questionIndex++;
        _selectedOption = null;
        _revealed = false;
      });
    } else {
      setState(() => _stage = _Stage.done);
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: BrandAppBar(
        title: _passage.title,
        actions: [
          AdminEditButton(
            jsonPath: _jsonPath,
            data: _passage.toJson(),
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
        child: SafeArea(
          child: _stage == _Stage.done 
              ? _buildDone(context) 
              : _buildCombined(context),
        ),
      ),
    );
  }


  Widget _buildCombined(BuildContext context) {
    return SingleChildScrollView(
      child: Column(
        children: [
          _buildReading(context),
          const Divider(height: 1, thickness: 2, color: AppColors.rule),
          _buildQuestion(context),
        ],
      ),
    );
  }

  Widget _buildReading(BuildContext context) {
    final passage = _passage;
    return Padding(
      padding: const EdgeInsets.fromLTRB(16, 12, 16, 16),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Center(
            child: Container(
              width: 56,
              height: 56,
              alignment: Alignment.center,
              decoration: BoxDecoration(color: AppColors.saffronTint, borderRadius: BorderRadius.circular(16)),
              child: Text(passage.emoji, style: TextStyle(fontSize: 28)),
            ),
          ),
          const SizedBox(height: 12),
          Center(child: ReadAloudButton(
            text: TrilingualService.instance.activeViewLanguage == 'hi' && passage.bodyHi != null
                ? passage.bodyHi!
                : TrilingualService.instance.activeViewLanguage == 'gu' && passage.bodyGu != null
                    ? passage.bodyGu!
                    : passage.body,
            label: 'Read the story aloud')),
          const SizedBox(height: 12),
          Padding(
            padding: EdgeInsets.only(bottom: 10),
            child: Text(TrilingualService.instance.getUIText('💡 Tip: Double-tap ANY word to search in the dictionary.'),
              style: TextStyle(fontSize: 12.5, color: AppColors.inkFaint, fontStyle: FontStyle.italic, fontWeight: FontWeight.w600),
            ),
          ),
          if (TrilingualService.instance.activeViewLanguage == 'hi' && passage.bodyHi != null)
            TtsInteractiveText(
              text: passage.bodyHi!,
              style: TextStyle(fontSize: 30, height: 1.6, color: AppColors.ink, fontWeight: FontWeight.w500).adaptToLanguage(),
            )
          else if (TrilingualService.instance.activeViewLanguage == 'gu' && passage.bodyGu != null)
            TtsInteractiveText(
              text: passage.bodyGu!,
              style: TextStyle(fontSize: 30, height: 1.6, color: AppColors.ink, fontWeight: FontWeight.w500).adaptToLanguage(),
            )
          else if (passage.glosses.isEmpty)
            TtsInteractiveText(
              text: passage.body,
              style: TextStyle(fontSize: 24, height: 1.6, color: AppColors.ink).adaptToLanguage(),
            )
          else
            GlossedText(
              text: passage.body,
              glosses: passage.glosses,
              baseStyle: TextStyle(fontSize: 24, height: 1.6, color: AppColors.ink),
            ),

        ],
      ),
    );
  }

  Widget _buildQuestion(BuildContext context) {
    final question = _passage.questions[_questionIndex];
    final total = _passage.questions.length;
    return Padding(
      padding: const EdgeInsets.all(20),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Text('Question ${_questionIndex + 1} of $total',
                  style: TextStyle(color: AppColors.inkFaint, fontSize: 13, fontWeight: FontWeight.w600)),
              const Spacer(),
            ],
          ),
          const SizedBox(height: 6),
          ClipRRect(
            borderRadius: BorderRadius.circular(4),
            child: LinearProgressIndicator(
              value: (_questionIndex + (_revealed ? 1 : 0)) / total,
              minHeight: 6,
              backgroundColor: AppColors.paperRaised,
              valueColor: const AlwaysStoppedAnimation(AppColors.saffron),
            ),
          ),
          const SizedBox(height: 24),
          Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(
                TrilingualService.instance.activeViewLanguage == 'hi' && question.promptHi != null
                    ? question.promptHi!
                    : TrilingualService.instance.activeViewLanguage == 'gu' && question.promptGu != null
                        ? question.promptGu!
                        : question.prompt,
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.w700, color: AppColors.ink, height: 1.35).adaptToLanguage(),
              ),
              const SizedBox(height: 12),
              ReadAloudButton(
                  text: TrilingualService.instance.activeViewLanguage == 'hi' && question.promptHi != null
                      ? question.promptHi!
                      : TrilingualService.instance.activeViewLanguage == 'gu' && question.promptGu != null
                          ? question.promptGu!
                          : question.prompt, 
                  label: 'Listen'),
            ],
          ),
          const SizedBox(height: 20),
          ListView.separated(
            shrinkWrap: true,
            physics: const NeverScrollableScrollPhysics(),
            itemCount: question.options.length,
            separatorBuilder: (_, _) => const SizedBox(height: 10),
            itemBuilder: (context, i) => _ReadingOptionTile(
              text: TrilingualService.instance.activeViewLanguage == 'hi' && question.optionsHi != null
                  ? question.optionsHi![i]
                  : TrilingualService.instance.activeViewLanguage == 'gu' && question.optionsGu != null
                      ? question.optionsGu![i]
                      : question.options[i],
              state: _optionState(question, i),
              onTap: () => _selectOption(i),
            ),
          ),
          if (_revealed) ...[
            _ExplanationCard(
              correct: _selectedOption == question.correctIndex,
              explanation: TrilingualService.instance.activeViewLanguage == 'hi' && question.explanationHi != null
                  ? question.explanationHi!
                  : TrilingualService.instance.activeViewLanguage == 'gu' && question.explanationGu != null
                      ? question.explanationGu!
                      : question.explanation,
            ),
            const SizedBox(height: 14),
            SizedBox(
              width: double.infinity,
              child: FilledButton(
                onPressed: _next,
                style: FilledButton.styleFrom(
                  backgroundColor: AppColors.saffron,
                  padding: const EdgeInsets.symmetric(vertical: 14),
                ),
                child: Text(_questionIndex + 1 < total ? 'Next question' : 'Finish'),
              ),
            ),
          ],
        ],
      ),
    );
  }

  _OptionState _optionState(PracticeQuestion question, int index) {
    if (!_revealed) return _OptionState.neutral;
    if (index == question.correctIndex) return _OptionState.correct;
    if (index == _selectedOption) return _OptionState.incorrect;
    return _OptionState.dimmed;
  }

  Widget _buildDone(BuildContext context) {
    final total = _passage.questions.length;
    return Center(
      child: Padding(
        padding: const EdgeInsets.all(28),
        child: Column(
          mainAxisSize: MainAxisSize.min,
          children: [
            Text(TrilingualService.instance.getUIText('📚'), style: TextStyle(fontSize: 48)),
            const SizedBox(height: 12),
            Text('$_correctCount / $total correct',
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.w800, color: AppColors.ink)),
            const SizedBox(height: 8),
            Text('You finished "${_passage.title}".',
                textAlign: TextAlign.center, style: TextStyle(color: AppColors.inkFaint)),
            const SizedBox(height: 28),
            SizedBox(
              width: double.infinity,
              child: OutlinedButton(
                onPressed: () => Navigator.of(context).pop(),
                style: OutlinedButton.styleFrom(
                  padding: const EdgeInsets.symmetric(vertical: 14),
                  side: const BorderSide(color: AppColors.rule),
                ),
                child: Text(TrilingualService.instance.getUIText('Back to reading list'), style: TextStyle(color: AppColors.inkSoft)),
              ),
            ),
          ],
        ),
      ),
    );
  }

}

enum _OptionState { neutral, correct, incorrect, dimmed }

class _ReadingOptionTile extends StatelessWidget {
  final String text;
  final _OptionState state;
  final VoidCallback onTap;

  const _ReadingOptionTile({required this.text, required this.state, required this.onTap});

  @override
  Widget build(BuildContext context) {
    Color bg;
    Color border;
    Color fg;
    IconData? icon;

    switch (state) {
      case _OptionState.neutral:
        bg = AppColors.paperRaised;
        border = AppColors.rule;
        fg = AppColors.ink;
        icon = null;
      case _OptionState.correct:
        bg = AppColors.success.withValues(alpha: 0.12);
        border = AppColors.success;
        fg = AppColors.success;
        icon = Icons.check_circle;
      case _OptionState.incorrect:
        bg = AppColors.critical.withValues(alpha: 0.10);
        border = AppColors.critical;
        fg = AppColors.critical;
        icon = Icons.cancel;
      case _OptionState.dimmed:
        bg = AppColors.paperRaised.withValues(alpha: 0.5);
        border = AppColors.rule;
        fg = AppColors.inkFaint;
        icon = null;
    }

    return InkWell(
      borderRadius: BorderRadius.circular(10),
      onTap: onTap,
      child: Container(
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
        decoration: BoxDecoration(color: bg, borderRadius: BorderRadius.circular(10), border: Border.all(color: border)),
        child: Row(
          children: [
            Expanded(child: Text(text, style: TextStyle(color: fg, fontSize: 15, fontWeight: FontWeight.w600).adaptToLanguage())),
            if (icon != null) Icon(icon, color: fg, size: 20),
          ],
        ),
      ),
    );
  }
}

class _ExplanationCard extends StatelessWidget {
  final bool correct;
  final String explanation;

  const _ExplanationCard({required this.correct, required this.explanation});

  @override
  Widget build(BuildContext context) {
    final color = correct ? AppColors.success : AppColors.critical;
    return Container(
      margin: const EdgeInsets.only(top: 14),
      padding: const EdgeInsets.all(14),
      decoration: BoxDecoration(
        color: color.withValues(alpha: 0.08),
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: color.withValues(alpha: 0.4)),
      ),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Icon(correct ? Icons.lightbulb : Icons.info_outline, color: color, size: 20),
          const SizedBox(width: 10),
          Expanded(child: Text(explanation, style: TextStyle(color: AppColors.inkSoft, fontSize: 13.5, height: 1.4).adaptToLanguage())),
        ],
      ),
    );
  }
}
