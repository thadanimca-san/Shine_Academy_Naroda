import 'dart:convert';
import 'dart:io';

void main() {
  final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class7_science_ch1.json');
  final jsonString = file.readAsStringSync();
  final data = json.decode(jsonString);
  final contentBlocks = (data['content'] ?? data['blocks']) as List? ?? [];

  for (var rawBlock in contentBlocks) {
    final block = Map<String, dynamic>.from(rawBlock);
    
    if (block['content'] is Map) {
      final contentMap = block['content'] as Map<String, dynamic>;
      block.addAll(contentMap);
      
      if (contentMap.containsKey('text')) {
        if (!block.containsKey('body')) block['body'] = contentMap['text'];
        if (!block.containsKey('question')) block['question'] = contentMap['text'];
      }
      
      if (contentMap.containsKey('explanation') && !block.containsKey('feedback_correct')) {
        block['feedback_correct'] = contentMap['explanation'];
      }
    } else if (block['content'] is String) {
      if (!block.containsKey('body')) block['body'] = block['content'];
      if (!block.containsKey('question')) block['question'] = block['content'];
    }

    if (!block.containsKey('correct_index') && block.containsKey('correct_answer') && block.containsKey('options')) {
      final options = List<String>.from(block['options']);
      final correctAns = block['correct_answer'].toString();
      final idx = options.indexOf(correctAns);
      if (idx != -1) {
        block['correct_index'] = idx;
      }
    }

    print("--- TYPE: ${block['type']} ---");
    print("BODY: ${block['body']}");
    print("QUESTION: ${block['question']}");
    print("OPTIONS: ${block['options']}");
  }
}
