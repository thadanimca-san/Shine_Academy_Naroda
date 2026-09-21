import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../../../../foundation/theme/app_colors.dart';
import '../../../../core/services/trilingual_service.dart';
import '../../../../core/services/tts_service.dart';
import '../../../common/widgets/tts_speed_controller.dart';
import '../../../../core/services/gamification_service.dart';
import '../../../common/widgets/xp_popup.dart';
import '../../../common/widgets/tts_interactive_text.dart';
import '../../../../../foundation/theme/app_typography.dart';
class SocraticWidget extends StatefulWidget {
  final Map<String, dynamic> block;
  const SocraticWidget({super.key, required this.block});

  @override
  State<SocraticWidget> createState() => _SocraticWidgetState();
}

class _SocraticWidgetState extends State<SocraticWidget> {
  int? _selectedIndex;
  bool _hasAnswered = false;
  bool _isPlayingQuestion = false;

  Future<void> _playQuestion(String question) async {
    if (mounted) setState(() => _isPlayingQuestion = true);
    await TTSService.instance.speak(question);
    if (mounted) setState(() => _isPlayingQuestion = false);
  }

  Future<void> _stopQuestion() async {
    await TTSService.instance.stop();
    if (mounted) setState(() => _isPlayingQuestion = false);
  }

  @override
  void dispose() {
    if (_isPlayingQuestion) TTSService.instance.stop();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final lang = TrilingualService.instance.activeViewLanguage;
    String question = widget.block['question'] ?? '';
    if (lang == 'hi' && widget.block['question_hi'] != null && widget.block['question_hi'].toString().isNotEmpty) {
      question = widget.block['question_hi'];
    } else if (lang == 'gu' && widget.block['question_gu'] != null && widget.block['question_gu'].toString().isNotEmpty) {
      question = widget.block['question_gu'];
    }

    List<String> options = List<String>.from(widget.block['options'] ?? []);
    if (lang == 'hi' && widget.block['options_hi'] != null && (widget.block['options_hi'] as List).isNotEmpty && widget.block['options_hi'][0].toString().isNotEmpty) {
      options = List<String>.from(widget.block['options_hi']);
    } else if (lang == 'gu' && widget.block['options_gu'] != null && (widget.block['options_gu'] as List).isNotEmpty && widget.block['options_gu'][0].toString().isNotEmpty) {
      options = List<String>.from(widget.block['options_gu']);
    }

    String correctFeedback = widget.block['explanation'] ?? widget.block['feedback_correct'] ?? 'Correct!';
    if (lang == 'hi' && widget.block['explanation_hi'] != null && widget.block['explanation_hi'].toString().isNotEmpty) {
      correctFeedback = widget.block['explanation_hi'];
    } else if (lang == 'gu' && widget.block['explanation_gu'] != null && widget.block['explanation_gu'].toString().isNotEmpty) {
      correctFeedback = widget.block['explanation_gu'];
    }
    
    String incorrectFeedback = widget.block['feedback_incorrect'] ?? 'Good try, but think again!';

    final correctIndex = widget.block['correct_index'] as int? ?? 0;
    
    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(16),
        boxShadow: [
          BoxShadow(color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.05), blurRadius: 10, offset: const Offset(0, 4))
        ],
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Icon(Icons.help_outline, color: AppColors.primary),
              const SizedBox(width: 8),
              Text(TrilingualService.instance.getUIText(TrilingualService.instance.getUIText('THINK ABOUT IT')), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 12 * AppTypography.scaleFactor(context), color: AppColors.primary)),
            ],
          ),
          const SizedBox(height: 12),
          TtsInteractiveText(
            text: question,
            style: AppTypography.body(context, color: Theme.of(context).colorScheme.onSurface).copyWith(fontWeight: FontWeight.w600),
          ),
          const SizedBox(height: 12),
          // TTS and Hindi Controls
          Wrap(
            spacing: 8,
            runSpacing: 4,
            crossAxisAlignment: WrapCrossAlignment.center,
            children: [
              InkWell(
                onTap: () => _playQuestion(question),
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(
                      Icons.play_circle_fill,
                      size: 20,
                      color: _isPlayingQuestion ? AppColors.primary.withValues(alpha: 0.5) : AppColors.primary,
                    ),
                    const SizedBox(width: 4),
                    Text(
                      TrilingualService.instance.getUIText(TrilingualService.instance.getUIText('Start')),
                      style: TextStyle(
                        fontSize: 12 * AppTypography.scaleFactor(context), 
                        color: _isPlayingQuestion ? AppColors.primary.withValues(alpha: 0.5) : AppColors.primary
                      ),
                    ),
                  ],
                ),
              ),
              const SizedBox(width: 4),
              InkWell(
                onTap: _stopQuestion,
                child: Row(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    Icon(
                      Icons.stop_circle,
                      size: 20,
                      color: Colors.red.shade600,
                    ),
                    const SizedBox(width: 4),
                    Text(TrilingualService.instance.getUIText('Stop'),
                      style: TextStyle(
                        fontSize: 12 * AppTypography.scaleFactor(context), 
                        color: Colors.red.shade600
                      ),
                    ),
                  ],
                ),
              ),
              const TTSSpeedController(),
            ],
          ),
          const SizedBox(height: 16),
          ...List.generate(options.length, (index) {
            final isSelected = _selectedIndex == index;
            final isCorrect = index == correctIndex;
            
            Color getBorderColor() {
              if (!_hasAnswered) return isSelected ? AppColors.primary : Colors.grey.shade300;
              if (isCorrect) return Colors.green;
              if (isSelected && !isCorrect) return Colors.red;
              return Colors.grey.shade300;
            }
            
            Color getBgColor() {
              if (!_hasAnswered) return isSelected ? AppColors.primary.withValues(alpha: 0.1) : Colors.transparent;
              if (isCorrect) return Colors.green.withValues(alpha: 0.1);
              if (isSelected && !isCorrect) return Colors.red.withValues(alpha: 0.1);
              return Colors.transparent;
            }

            Offset? tapPosition;
            return GestureDetector(
              onTapDown: (details) => tapPosition = details.globalPosition,
              onTap: _hasAnswered ? null : () {
                if (index == correctIndex) {
                   if (tapPosition != null) {
                       XpPopup.show(context, position: tapPosition!, amount: 50);
                   }
                   GamificationService.instance.addKnowledgeCheckXp();
                }
                setState(() {
                  _selectedIndex = index;
                  _hasAnswered = true;
                });
              },
              child: Container(
                width: double.infinity,
                margin: const EdgeInsets.only(bottom: 12),
                padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
                decoration: BoxDecoration(
                  color: getBgColor(),
                  border: Border.all(color: getBorderColor(), width: isSelected || _hasAnswered && isCorrect ? 2 : 1),
                  borderRadius: BorderRadius.circular(12),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      options[index],
                      style: AppTypography.bodySmall(context, color: Theme.of(context).colorScheme.onSurface, fontWeight: isSelected ? FontWeight.bold : FontWeight.normal),
                    ),
                  ],
                ),
              ),
            );
          }),
          
          if (_hasAnswered) ...[
            const SizedBox(height: 16),
            Container(
              padding: const EdgeInsets.all(16),
              decoration: BoxDecoration(
                color: _selectedIndex == correctIndex ? Colors.green.shade50 : Colors.orange.shade50,
                borderRadius: BorderRadius.circular(12),
              ),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Icon(
                    _selectedIndex == correctIndex ? Icons.check_circle : Icons.lightbulb,
                    color: _selectedIndex == correctIndex ? Colors.green : Colors.orange,
                  ),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(
                          _selectedIndex == correctIndex 
                              ? correctFeedback
                              : incorrectFeedback,
                          style: AppTypography.bodySmall(context, color: Theme.of(context).colorScheme.onSurface),
                        ),
                      ],
                    ),
                  ),
                ],
              ),
            )
          ]
        ],
      ),
    );
  }
}
