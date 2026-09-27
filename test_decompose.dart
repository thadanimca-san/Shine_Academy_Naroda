import 'dart:convert';
import 'dart:io';
void main() {
  final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary/generated_massive_dict.json');
  final String jsonString = file.readAsStringSync();
  final Map<String, dynamic> dictData = json.decode(jsonString);
  for (var term in dictData['terms']) {
    final en = (term['term']?['english'] ?? '').toString().toLowerCase().trim();
    if (en == 'decompose') {
      print("Found decompose!");
      return;
    }
  }
  print("Decompose NOT found.");
}
