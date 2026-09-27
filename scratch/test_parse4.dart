import 'dart:io';
import 'dart:convert';

void main() {
  try {
    final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch1.json');
    dynamic chapterData = json.decode(file.readAsStringSync());
    List blocks = chapterData as List;
    
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
        
        var optionsHi = block['options_hi'] != null ? List<String>.from(block['options_hi']) : null;
      }
    }
    print("SUCCESS!");
  } catch (e) {
    print("EXCEPTION: " + e.toString());
  }
}
