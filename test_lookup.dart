import 'dart:convert';
void main() {
  String raw = "Food:";
  final String cleaned = raw
      .replaceAll(RegExp(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$'), '')
      .toLowerCase()
      .trim();
      
  List<Map<String, dynamic>> allTerms = [
    {
      "id": "DICT_ENG_FOOD",
      "term": {
        "english": "food",
        "hindi": "भोजन / खाना",
        "gu": "ખોરાક / ખાવાનું"
      }
    }
  ];
  
  for (final t in allTerms) {
    final en = (t['term']?['english'] ?? '').toString().toLowerCase().trim();
    if (en == cleaned) {
      print("MATCH FOUND!");
      return;
    }
  }
  print("MATCH NOT FOUND!");
}
