import 'dart:convert';
import 'dart:io';

void main() async {
  final dir = Directory('app_core/learning_modules');
  if (!await dir.exists()) return;
  int successCount = 0;
  
  await for (final entity in dir.list()) {
    if (entity is Directory && entity.path.contains('class2_evs_ch')) {
      final file = File('${entity.path}/blocks.json');
      if (await file.exists()) {
        try {
          final content = await file.readAsString();
          final data = jsonDecode(content);
          if (data is List && data.isNotEmpty) {
            print('${entity.path.split('/').last}: OK (${data.length} blocks)');
            successCount++;
          } else {
            print('${entity.path.split('/').last}: ERROR (Not a List or Empty)');
          }
        } catch (e) {
          print('${entity.path.split('/').last}: JSON ERROR - $e');
        }
      } else {
        print('${entity.path.split('/').last}: ERROR (Missing blocks.json)');
      }
    }
  }
  print('Total Class 2 Success: $successCount');
}
