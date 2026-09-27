import 'dart:convert';
import 'dart:io';

void main() {
  final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json');
  final db = json.decode(file.readAsStringSync());
  for (var subject in db['subjects']) {
    if (subject['title'].toString().contains('Math')) {
      for (var chapter in subject['chapters']) {
        if (chapter['title'].toString().contains('Real Numbers')) {
          print("Found Real Numbers! Subject: " + subject['title'] + " Module ID: " + chapter['module_id']);
        }
      }
    }
  }
}
