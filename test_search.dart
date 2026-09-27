import 'dart:convert';
void main() {
  var termMap = {
      "id": "DICT_ENG_SCHOOL",
      "term": {
        "english": "School",
        "hindi": "स्कूल",
        "gujarati": "શાળા"
      },
      "definition": {
        "simple": {
          "en": "A place where children go to learn.",
          "hi": "वह स्थान जहाँ बच्चे पढ़ने जाते हैं।",
          "gu": "એવું સ્થાન જ્યાં બાળકો ભણવા જાય છે."
        }
      }
  };
  
  String _query = "school";
  String query = _query.trim().toLowerCase();
  
  final termEn = termMap['term']?['english']?.toString().toLowerCase() ?? '';
  final termHi = (termMap['term']?['hindi'] ?? termMap['term']?['hi'])?.toString() ?? '';
  final termGu = (termMap['term']?['gujarati'] ?? termMap['term']?['gu'])?.toString() ?? '';
            
  final def = termMap['definition']?['simple'];
  final defEn = (def is Map ? def['en'] : def)?.toString().toLowerCase() ?? '';
            
  bool match = termEn.contains(query) ||
               termHi.contains(_query.trim()) ||
               termGu.contains(_query.trim()) ||
               defEn.contains(query);
               
  print("termEn: $termEn, query: $query, match: $match");
}
