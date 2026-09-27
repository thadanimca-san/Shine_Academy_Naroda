import re

with open('lib/features/learning/school/english/screens/dictionary_search_screen.dart', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace _performSearch
old_search = """    // Fetch all terms from the Universal Dictionary Service directly
    final allTerms = UniversalDictionaryService.instance.getAllTerms();
    
    final matches = allTerms.where((termMap) {
      try {
        var term = termMap['term'];
        var def = termMap['definition'];
        
        String termEn = '';
        String termHi = '';
        String termGu = '';
        
        if (term != null) {
          termEn = (term['english'] ?? '').toString().toLowerCase();
          termHi = (term['hindi'] ?? term['hi'] ?? '').toString().toLowerCase();
          termGu = (term['gujarati'] ?? term['gu'] ?? '').toString().toLowerCase();
        }
        
        String defEn = '';
        String defHi = '';
        String defGu = '';
        
        if (def != null && def['simple'] != null) {
          var simple = def['simple'];
          if (simple is Map) {
            defEn = (simple['en'] ?? '').toString().toLowerCase();
            defHi = (simple['hi'] ?? '').toString().toLowerCase();
            defGu = (simple['gu'] ?? '').toString().toLowerCase();
          } else {
            defEn = simple.toString().toLowerCase();
          }
        }
        
        return termEn.contains(queryLower) ||
               termHi.contains(queryLower) ||
               termGu.contains(queryLower) ||
               defEn.contains(queryLower) ||
               defHi.contains(queryLower) ||
               defGu.contains(queryLower);
      } catch (e) {
        return false;
      }
    }).toList();"""

new_search = """    // Fetch all terms from the Universal Dictionary Service directly
    final matches = await UniversalDictionaryService.instance.searchTerms(queryLower);"""

if "UniversalDictionaryService.instance.searchTerms" not in code:
    code = code.replace(old_search, new_search)

# Make sure _performSearch is async
if "void _performSearch" in code and "async" not in code.split("void _performSearch")[1].split("{")[0]:
    code = code.replace("void _performSearch(String query) {", "Future<void> _performSearch(String query) async {")

with open('lib/features/learning/school/english/screens/dictionary_search_screen.dart', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done search_screen")
