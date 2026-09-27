import 'dart:convert';
import 'dart:io';

void main() {
  final basePath = 'app_core/learning_modules';
  final pattern = RegExp(r'^class1_evs_ch\d+$');
  
  final dir = Directory(basePath);
  if (!dir.existsSync()) {
    print('Directory $basePath does not exist.');
    return;
  }
  
  bool allValid = true;
  for (var entity in dir.listSync()) {
    if (entity is Directory) {
      final name = entity.path.split('/').last;
      if (pattern.hasMatch(name)) {
        final file = File('${entity.path}/blocks.json');
        if (file.existsSync()) {
          try {
            final content = file.readAsStringSync();
            final json = jsonDecode(content);
            if (json is List) {
              print('OK: $name');
            } else {
              print('FAIL: $name is not a List!');
              allValid = false;
            }
          } catch (e) {
            print('FAIL: $name - $e');
            allValid = false;
          }
        } else {
          print('MISSING: $name/blocks.json');
          allValid = false;
        }
      }
    }
  }
  
  if (allValid) {
    print('ALL CLASS 1 JSON FILES ARE VALID!');
  } else {
    print('SOME JSON FILES FAILED VALIDATION.');
  }
}
