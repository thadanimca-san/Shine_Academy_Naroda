import 'dart:convert';
import 'dart:io';

void main() {
  final dir = Directory('app_core/learning_modules');
  int total = 0;
  int failed = 0;
  for (var entity in dir.listSync()) {
    if (entity is Directory) {
      final name = entity.path.split('/').last;
      if (name.contains('science')) {
        final file = File('${entity.path}/blocks.json');
        if (file.existsSync()) {
          total++;
          try {
            final content = file.readAsStringSync();
            final json = jsonDecode(content);
            if (json is! List) {
              print('FAIL: $name is not a List!');
              failed++;
            }
          } catch (e) {
            print('FAIL: $name - $e');
            failed++;
          }
        }
      }
    }
  }
  print('Total science chapters checked: $total. Failed: $failed');
}
