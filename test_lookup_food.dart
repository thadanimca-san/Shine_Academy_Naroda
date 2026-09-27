import 'dart:convert';
import 'dart:io';

void main() async {
  final file = File('app_core/universal_dictionary/generated_massive_dict.json');
  final jsonStr = await file.readAsString();
  final data = json.decode(jsonStr) as Map;
  
  if (data.containsKey('terms')) {
    final list = data['terms'] as List;
    bool foundFood = false;
    for (var t in list) {
      final en = (t['term']?['english'] ?? '').toString().toLowerCase().trim();
      if (en == 'food' || en == 'decompose') {
        print('Found: ${t['id']} -> $en');
        foundFood = true;
      }
    }
    print('Found Food/Decompose: $foundFood');
  }
}
