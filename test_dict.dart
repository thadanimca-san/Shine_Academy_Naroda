import 'dart:convert';
void main() {
  Map<String, dynamic> termMap = {
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
  
  final term = termMap['term'] as Map<String, dynamic>?;
  final def = termMap['definition']?['simple'] as Map<String, dynamic>?;
  
  final termEn = term?['english']?.toString().toLowerCase() ?? '';
  final termHi = (term?['hindi'] ?? term?['hi'])?.toString() ?? '';
  final termGu = (term?['gujarati'] ?? term?['gu'])?.toString() ?? '';
  
  final defEn = def?['en']?.toString().toLowerCase() ?? '';
  
  bool match = termEn.contains(query) ||
               termHi.contains(_query.trim()) ||
               termGu.contains(_query.trim()) ||
               defEn.contains(query);
               
  print("termEn: $termEn, termHi: $termHi, termGu: $termGu, defEn: $defEn, query: $query, match: $match");
}
