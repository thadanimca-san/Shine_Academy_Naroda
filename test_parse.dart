import 'dart:convert';
import 'dart:io';

void main() {
  final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch1.json');
  final chapterData = jsonDecode(file.readAsStringSync());
  
  List<dynamic> allQuestions = [];
  
  if (chapterData is List) {
    // If it's a direct list of blocks
    for (var block in chapterData) {
      if (block['type'] == 'quiz' || block['type'] == 'mcq' || block['type'] == 'knowledge_check' || block['type'] == 'socratic' || block['type'] == 'quiz_multiple_choice') {
        if (block['is_deo_challenge'] == true) {
          continue;
        }
        allQuestions.add(block);
      }
    }
  } else if (chapterData['blocks'] != null) {
    // If it's wrapped in a map
    final blocks = chapterData['blocks'] as List;
    for (var block in blocks) {
      if (block['type'] == 'quiz' || block['type'] == 'mcq' || block['type'] == 'knowledge_check' || block['type'] == 'socratic' || block['type'] == 'quiz_multiple_choice') {
        if (block['is_deo_challenge'] == true) {
          continue;
        }
        allQuestions.add(block);
      }
    }
  }
  
  print("Found ${allQuestions.length} standard practice questions.");
  if (allQuestions.length <= 2) {
    for (var q in allQuestions) {
      print("Q: ${q['question'] ?? q['question_text']}");
    }
  }
}
