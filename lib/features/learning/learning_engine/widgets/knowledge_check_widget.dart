import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../../../../core/services/gamification_service.dart';
import '../../../common/widgets/xp_popup.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/foundation/theme/app_typography.dart';

class KnowledgeCheckWidget extends StatefulWidget {
  final Map<String, dynamic> block;
  const KnowledgeCheckWidget({super.key, required this.block});

  @override
  State<KnowledgeCheckWidget> createState() => _KnowledgeCheckWidgetState();
}

class _KnowledgeCheckWidgetState extends State<KnowledgeCheckWidget> with AutomaticKeepAliveClientMixin {
  int? _selectedIndex;
  bool _hasAnswered = false;

  @override
  bool get wantKeepAlive => true;

  @override
  Widget build(BuildContext context) {
    super.build(context);
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

    String correctFeedback = widget.block['explanation'] ?? widget.block['feedback_correct'] ?? 'Excellent!';
    if (lang == 'hi' && widget.block['explanation_hi'] != null && widget.block['explanation_hi'].toString().isNotEmpty) {
      correctFeedback = widget.block['explanation_hi'];
    } else if (lang == 'gu' && widget.block['explanation_gu'] != null && widget.block['explanation_gu'].toString().isNotEmpty) {
      correctFeedback = widget.block['explanation_gu'];
    }
    
    String incorrectFeedback = widget.block['feedback_incorrect'] ?? 'Incorrect!';

    final correctIndex = widget.block['correct_index'] as int? ?? 0;
    
    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      padding: const EdgeInsets.all(20),
      decoration: BoxDecoration(
        color: Colors.blue.shade50,
        borderRadius: BorderRadius.circular(16),
        border: Border.all(color: Colors.blue.shade200),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(Icons.quiz, color: Colors.blue),
              const SizedBox(width: 8),
              Text(TrilingualService.instance.getUIText('KNOWLEDGE CHECK'), style: GoogleFonts.inter(fontWeight: FontWeight.bold, fontSize: 12 * AppTypography.scaleFactor(context), color: Colors.blue.shade700)),
            ],
          ),
          const SizedBox(height: 12),
          Text(question, style: GoogleFonts.poppins(fontSize: 16 * AppTypography.scaleFactor(context), fontWeight: FontWeight.w600, color: Theme.of(context).colorScheme.onSurface)),
          const SizedBox(height: 20),
          ...List.generate(options.length, (index) {
            final isSelected = _selectedIndex == index;
            final isCorrect = index == correctIndex;
            
            Color getBorderColor() {
              if (!_hasAnswered) return isSelected ? Colors.blue : Colors.white;
              if (isCorrect) return Colors.green;
              if (isSelected && !isCorrect) return Colors.red;
              return Colors.white;
            }
            
            Color getBgColor() {
              if (!_hasAnswered) return isSelected ? Colors.blue.withValues(alpha: 0.1) : Colors.white;
              if (isCorrect) return Colors.green.withValues(alpha: 0.1);
              if (isSelected && !isCorrect) return Colors.red.withValues(alpha: 0.1);
              return Colors.white;
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
                  boxShadow: _hasAnswered ? [] : [
                    BoxShadow(color: Theme.of(context).colorScheme.onSurface.withValues(alpha: 0.02), blurRadius: 4, offset: const Offset(0, 2))
                  ],
                ),
                child: Row(
                  children: [
                    CircleAvatar(
                      radius: 12,
                      backgroundColor: getBorderColor().withValues(alpha: 0.2),
                      child: Text(
                        String.fromCharCode(65 + index),
                        style: GoogleFonts.inter(fontSize: 12 * AppTypography.scaleFactor(context), fontWeight: FontWeight.bold, color: getBorderColor() == Colors.white ? Colors.grey : getBorderColor()),
                      ),
                    ),
                    const SizedBox(width: 12),
                    Expanded(
                      child: Column(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text(
                            options[index],
                            style: GoogleFonts.inter(fontSize: 14 * AppTypography.scaleFactor(context), color: Theme.of(context).colorScheme.onSurface, fontWeight: isSelected ? FontWeight.bold : FontWeight.normal),
                          ),
                        ],
                      ),
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
                color: _selectedIndex == correctIndex ? Colors.green.shade50 : Colors.red.shade50,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: _selectedIndex == correctIndex ? Colors.green.shade200 : Colors.red.shade200),
              ),
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  Icon(
                    _selectedIndex == correctIndex ? Icons.check_circle : Icons.cancel,
                    color: _selectedIndex == correctIndex ? Colors.green : Colors.red,
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
                          style: GoogleFonts.inter(fontSize: 14 * AppTypography.scaleFactor(context), color: Theme.of(context).colorScheme.onSurface),
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
