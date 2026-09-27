import 'dart:convert';
import 'dart:io';

void main() async {
  String raw = "Food:";
  final String cleaned = raw
      .replaceAll(RegExp(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$'), '')
      .toLowerCase()
      .trim();

  print("Cleaned word: '$cleaned'");
  
  final file = File('/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary/generated_massive_dict.json');
  final String jsonString = file.readAsStringSync();
  final Map<String, dynamic> dictData = json.decode(jsonString);
  
  List<Map<String, dynamic>> allTerms = [];
  if (dictData['terms'] != null) {
    for (var term in dictData['terms']) {
      allTerms.add(term as Map<String, dynamic>);
    }
  }
  
  print("Loaded ${allTerms.length} terms");

  // Pass 2: exact English word match
  for (final t in allTerms) {
    final en = (t['term']?['english'] ?? '').toString().toLowerCase().trim();
    if (en == cleaned) {
      print("MATCH FOUND! ${t['id']}");
      return;
    }
  }
  print("MATCH NOT FOUND!");
}
