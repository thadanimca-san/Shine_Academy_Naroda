import 'dart:io';
import 'dart:convert';

void main() {
  final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch1.json');
  dynamic chapterData = json.decode(file.readAsStringSync());
  
  List blocks = [];
  if (chapterData is Map && chapterData['blocks'] != null) {
    blocks = chapterData['blocks'] as List;
  } else if (chapterData is List) {
    blocks = chapterData;
  }
  
  int count = 0;
  for (var block in blocks) {
    if (block['type'] == 'quiz' || block['type'] == 'mcq' || block['type'] == 'knowledge_check' || block['type'] == 'socratic' || block['type'] == 'quiz_multiple_choice') {
      if (block['is_deo_challenge'] == true) {
        continue;
      }
      count++;
    }
  }
  print("Found " + count.toString() + " questions!");
}
