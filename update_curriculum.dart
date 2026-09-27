import 'dart:convert';
import 'dart:io';

import 'package:shine_academy_naroda/features/learning/school/sci_simulation/data/sample_chapters.dart';
import 'package:shine_academy_naroda/features/learning/school/sci_simulation/models/chapter_model.dart';

void updateClassJson(int classNumber, List<ChapterModel> chapters) {
  final file = File('app_core/curriculum/gseb_class$classNumber.json');
  if (!file.existsSync()) {
    print('File not found: ${file.path}');
    return;
  }
  
  final content = file.readAsStringSync();
  final Map<String, dynamic> data = jsonDecode(content);
  
  final subjects = data['subjects'] as List<dynamic>;
  Map<String, dynamic>? scienceSubject;
  for (var subject in subjects) {
    if (subject['name'].toString().toLowerCase().contains('science')) {
      scienceSubject = subject;
      break;
    }
  }
  
  if (scienceSubject == null) {
    print('Science subject not found in class $classNumber');
    return;
  }
  
  final chapterList = scienceSubject['chapters'] as List<dynamic>;
  
  for (var simChapter in chapters) {
    final moduleId = 'sci_sim:${simChapter.chapterId}';
    
    // Check if already exists
    bool exists = false;
    for (var existing in chapterList) {
      if (existing['module_id'] == moduleId) {
        exists = true;
        break;
      }
    }
    
    if (!exists) {
      chapterList.add({
        'chapter_id': simChapter.chapterId,
        'title': '[Simulation] ${simChapter.chapterName}',
        'module_id': moduleId
      });
      print('Added ${simChapter.chapterName} to Class $classNumber');
    }
  }
  
  file.writeAsStringSync(jsonEncode(data));
  print('Successfully updated gseb_class$classNumber.json');
}

void main() {
  updateClassJson(7, allClass7Chapters);
  updateClassJson(8, allClass8Chapters);
  updateClassJson(9, allClass9Chapters);
  updateClassJson(10, allClass10Chapters);
}
