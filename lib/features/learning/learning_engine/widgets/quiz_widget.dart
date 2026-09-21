import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../../core/services/streak_manager_service.dart';
import '../../../../core/widgets/presentation_builder.dart';
import '../../../dictionary/dictionary_popup.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class QuizWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const QuizWidget({super.key, required this.data});

  @override
  State<QuizWidget> createState() => _QuizWidgetState();
}

class _QuizWidgetState extends State<QuizWidget> {
  int? _selectedIndex;
  bool _hasSubmitted = false;

  @override
  Widget build(BuildContext context) {
    String questionText = TrilingualService.instance.getLocalizedText(widget.data, 'question');
    if (questionText.isEmpty) {
      questionText = TrilingualService.instance.getLocalizedText(widget.data, 'question_text');
    }
    
    if (questionText.isEmpty) {
      final rawQuestion = widget.data['question'] ?? widget.data['question_text'];
      if (rawQuestion is Map<String, dynamic>) {
        questionText = rawQuestion[TrilingualService.instance.activeViewLanguage] ?? rawQuestion['en'] ?? rawQuestion['english'] ?? '';
      } else {
        questionText = rawQuestion?.toString() ?? '';
      }
    }
        
    List<dynamic> options = [];
    final lang = TrilingualService.instance.activeViewLanguage;
    if (lang != 'en' && widget.data['options_$lang'] != null && widget.data['options_$lang'] is List && (widget.data['options_$lang'] as List).isNotEmpty) {
       options = widget.data['options_$lang'];
    } else {
       final rawOptions = widget.data['options'];
       if (rawOptions is List) {
         options = rawOptions.map((opt) {
           if (opt is Map) {
             return opt[lang] ?? opt['text'] ?? opt['english'] ?? opt['en'] ?? '';
           }
           return opt;
         }).toList();
       } else if (rawOptions is Map<String, dynamic>) {
         options = rawOptions[lang] ?? rawOptions['en'] ?? rawOptions['english'] ?? [];
       }
    }
        
    int correctIndex = 0;
    if (widget.data['correct_index'] != null) {
      if (widget.data['correct_index'] is int) {
        correctIndex = widget.data['correct_index'];
      } else if (widget.data['correct_index'] is String) {
        correctIndex = int.tryParse(widget.data['correct_index']) ?? 0;
      }
    } else if (widget.data['correct_answer'] != null) {
      final answerStr = widget.data['correct_answer'].toString().trim().toLowerCase();
      final idx = options.indexWhere((opt) => opt.toString().trim().toLowerCase() == answerStr);
      if (idx != -1) {
        correctIndex = idx;
      }
    }

    return PresentationBuilder(
      builder: (context, scale) {
        return Container(
          margin: const EdgeInsets.only(bottom: 24),
          padding: const EdgeInsets.all(24),
          decoration: BoxDecoration(
            color: Colors.white,
            borderRadius: BorderRadius.circular(20),
            border: Border.all(color: Colors.teal.withValues(alpha: 0.1), width: 1.5),
            boxShadow: [
              BoxShadow(
                color: Colors.teal.withValues(alpha: 0.05),
                blurRadius: 20,
                offset: const Offset(0, 10),
              )
            ],
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                children: [
                  Container(
                    padding: const EdgeInsets.all(8),
                    decoration: BoxDecoration(
                      color: Colors.teal.withValues(alpha: 0.1),
                      borderRadius: BorderRadius.circular(8),
                    ),
                    child: Icon(Icons.quiz_rounded, color: Colors.teal),
                  ),
                  const SizedBox(width: 16),
                  Expanded(
                    child: Text(TrilingualService.instance.getUIText("Quick Check"),
                      style: GoogleFonts.poppins(
                        fontSize: 22 * scale,
                        fontWeight: FontWeight.w700,
                        color: Colors.teal[900],
                        letterSpacing: -0.5,
                      ),
                    ),
                  ),
                ],
              ),
              const SizedBox(height: 16),
              SelectionArea(
                contextMenuBuilder: (BuildContext context, SelectableRegionState selectableRegionState) {
                  final List<ContextMenuButtonItem> buttonItems = selectableRegionState.contextMenuButtonItems.toList();
                  
                  buttonItems.insert(0, ContextMenuButtonItem(
                    label: '📖 Dictionary',
                    onPressed: () {
                      final selection = selectableRegionState.textEditingValue.selection;
                      final text = selectableRegionState.textEditingValue.text;
                      if (selection.isValid && !selection.isCollapsed) {
                        String word = selection.textInside(text).trim();
                        word = word.replaceAll(RegExp(r'[.,;!?"()\[\]{}]'), '');
                        ContextMenuController.removeAny();
                        UniversalDictionaryPopup.show(context, word);
                      }
                    },
                  ));
                  
                  return AdaptiveTextSelectionToolbar.buttonItems(
                    anchors: selectableRegionState.contextMenuAnchors,
                    buttonItems: buttonItems,
                  );
                },
                child: Text(
                  questionText,
                  style: GoogleFonts.inter(
                    fontSize: 18 * scale,
                    fontWeight: FontWeight.w600,
                    color: Theme.of(context).colorScheme.onSurface,
                    height: 1.5,
                  ).adaptToLanguage(),
                ),
              ),
              const SizedBox(height: 16),
              ...List.generate(options.length, (index) {
                final isSelected = _selectedIndex == index;
                final isCorrect = index == correctIndex;
                
                Color getBorderColor() {
                  if (!_hasSubmitted) return isSelected ? Colors.teal : Colors.grey[300]!;
                  if (isSelected && isCorrect) return Colors.green;
                  if (isSelected && !isCorrect) return Colors.red;
                  if (isCorrect) return Colors.green;
                  return Colors.grey[300]!;
                }

                Color getBgColor() {
                  if (!_hasSubmitted) return isSelected ? Colors.teal.withValues(alpha: 0.05) : Colors.transparent;
                  if (isSelected && isCorrect) return Colors.green.withValues(alpha: 0.1);
                  if (isSelected && !isCorrect) return Colors.red.withValues(alpha: 0.1);
                  if (isCorrect) return Colors.green.withValues(alpha: 0.05);
                  return Colors.transparent;
                }

                return GestureDetector(
                  onTap: _hasSubmitted ? null : () {
                    setState(() {
                      _selectedIndex = index;
                      _hasSubmitted = true;
                    });
                    if (index == correctIndex) {
                      StreakManagerService.instance.onCorrectAnswer(context);
                    } else {
                      StreakManagerService.instance.onIncorrectAnswer();
                    }
                  },
                  child: Container(
                    margin: const EdgeInsets.only(bottom: 12),
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: getBgColor(),
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: getBorderColor(), width: isSelected || (_hasSubmitted && isCorrect) ? 2 : 1),
                    ),
                    child: Row(
                      children: [
                        Container(
                          width: 24 * scale,
                          height: 24 * scale,
                          decoration: BoxDecoration(
                            shape: BoxShape.circle,
                            color: isSelected ? Colors.teal : Colors.transparent,
                            border: Border.all(color: isSelected ? Colors.teal : Colors.grey[400]!),
                          ),
                          child: isSelected ? Icon(Icons.check, size: 16 * scale, color: Colors.white) : null,
                        ),
                        const SizedBox(width: 16),
                        Expanded(
                          child: Text(
                            options[index].toString(),
                            style: GoogleFonts.inter(fontSize: 15 * scale, color: Theme.of(context).colorScheme.onSurface).adaptToLanguage(),
                          ),
                        ),
                        if (_hasSubmitted && isCorrect)
                          Icon(Icons.check_circle, color: Colors.green),
                        if (_hasSubmitted && isSelected && !isCorrect)
                          Icon(Icons.cancel, color: Colors.red),
                      ],
                    ),
                  ),
                );
              }),
              const SizedBox(height: 12),

            ],
          ),
        );
      }
    );
  }
}
