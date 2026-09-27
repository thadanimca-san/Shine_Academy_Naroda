import 'dart:io';
import 'dart:convert';
import 'package:shine_academy_naroda/core/engine/assessment_engine.dart'; // assuming this path is wrong for a script but let's just mock the class

class AssessmentQuestion {
  final String moduleId;
  final String type;
  final String question;
  final String? questionHi;
  final List<String> options;
  final List<String>? optionsHi;
  final dynamic correctIndexOrAnswer;
  final String? explanationEn;
  final String? explanationHi;
  final String? distractorRationaleEn;
  final String? distractorRationaleHi;
  final String? bloomTaxonomy;
  final String? aiHint;
  final int marks;
  final String? section;

  AssessmentQuestion({
    required this.moduleId,
    required this.type,
    required this.question,
    this.questionHi,
    required this.options,
    this.optionsHi,
    required this.correctIndexOrAnswer,
    this.explanationEn,
    this.explanationHi,
    this.distractorRationaleEn,
    this.distractorRationaleHi,
    this.bloomTaxonomy,
    this.aiHint,
    this.marks = 1,
    this.section,
  });
}

void main() {
  try {
    final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch1.json');
    dynamic chapterData = json.decode(file.readAsStringSync());
    List blocks = chapterData as List;
    List<AssessmentQuestion> allQuestions = [];
    
    for (var block in blocks) {
      if (block['type'] == 'quiz' || block['type'] == 'mcq' || block['type'] == 'knowledge_check' || block['type'] == 'socratic' || block['type'] == 'quiz_multiple_choice') {
        if (block['is_deo_challenge'] == true) {
          continue;
        }
        final opts = block['options'] as List?;
        List<String> optionTexts = [];
        if (opts != null) {
          for (var opt in opts) {
            optionTexts.add(opt.toString());
          }
        }
        
        dynamic correctAns = block['correct_index'] ?? 0;
        
        allQuestions.add(AssessmentQuestion(
          moduleId: 'cbse_class10_maths_ch1',
          type: 'quiz',
          question: block['question_text'] ?? block['question'] ?? '',
          questionHi: block['question_text_hi'] ?? block['question_hi'],
          options: optionTexts,
          optionsHi: block['options_hi'] != null ? List<String>.from(block['options_hi']) : null,
          correctIndexOrAnswer: correctAns,
          explanationEn: block['explanation'],
          explanationHi: block['explanation_hi'],
        ));
      }
    }
    print("SUCCESS: Added " + allQuestions.length.toString() + " questions");
  } catch (e) {
    print("EXCEPTION: " + e.toString());
  }
}
