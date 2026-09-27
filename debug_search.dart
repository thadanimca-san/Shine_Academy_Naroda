import 'dart:convert';
import 'dart:io';

void main() async {
  print('Loading index...');
  String indexString = await File('app_core/universal_dictionary/dictionary_index.json').readAsString();
  Map<String, dynamic> indexData = json.decode(indexString);
  List<dynamic> indexList = indexData['index'] ?? [];

  List<Map<String, dynamic>> allTerms = [];

  for (var entry in indexList) {
    try {
      String filePath = entry['file'];
      String jsonString = await File(filePath).readAsString();
      Map<String, dynamic> dictData = json.decode(jsonString);
      if (dictData['terms'] != null) {
        for (var term in dictData['terms']) {
          if (term['id'] != null) {
            allTerms.add(term as Map<String, dynamic>);
          }
        }
      }
    } catch (e) {}
  }
  print('Loaded ${allTerms.length} terms.');

  String query = 'ear';
  List<Map<String, dynamic>> matches = allTerms.where((termMap) {
    try {
      var term = termMap['term'];
      var def = termMap['definition'];
      String termEn = '';
      String termHi = '';
      String termGu = '';
      String defEn = '';
      if (term is Map) {
        termEn = term['english']?.toString().toLowerCase() ?? '';
        termHi = (term['hindi'] ?? term['hi'])?.toString() ?? '';
        termGu = (term['gujarati'] ?? term['gu'])?.toString() ?? '';
      }
      if (def is Map) {
        var simple = def['simple'];
        if (simple is Map) {
          defEn = simple['en']?.toString().toLowerCase() ?? '';
        }
      }
      return termEn.contains(query) || termHi.contains(query) || termGu.contains(query) || defEn.contains(query);
    } catch (e) {
      return false;
    }
  }).toList();
  
  print('Found ${matches.length} matches for "school"');
  if (matches.isNotEmpty) {
    print('First match: ${matches[0]['term']['english']}');
  }
}
