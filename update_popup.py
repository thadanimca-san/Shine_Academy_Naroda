import re

with open('lib/features/dictionary/dictionary_popup.dart', 'r', encoding='utf-8') as f:
    code = f.read()

# Replace _lookup
new_lookup = """  static Future<_LookupResult> _lookup(String raw) async {
    final service = UniversalDictionaryService.instance;
    await service.init();

    final String cleaned = raw
        .replaceAll(RegExp(r'^[^a-zA-Z0-9]+|[^a-zA-Z0-9]+$'), '')
        .trim();

    if (cleaned.isEmpty) {
      return _LookupResult(query: raw);
    }
    
    // Pass 1: ID Match
    var term = await service.getTermById(raw);
    if (term == null && raw.toUpperCase() != raw) {
        term = await service.getTermById(raw.toUpperCase());
    }
    
    if (term != null) {
      return _LookupResult(query: raw, term: term);
    }
    
    // Pass 2: Search word match
    final results = await service.searchTerms(cleaned);
    if (results.isNotEmpty) {
      // Find exact match if possible
      for (final t in results) {
         final en = (t['term']?['english'] ?? '').toString().toLowerCase().trim();
         if (en == cleaned.toLowerCase()) return _LookupResult(query: raw, term: t);
      }
      return _LookupResult(query: raw, term: results.first);
    }
    
    // If not found at all
    return _LookupResult(query: raw);
  }"""

# Use regex to find and replace the _lookup method
code = re.sub(r'  static Future<_LookupResult> _lookup\(String raw\) async \{.*?(?=  static void show)', new_lookup + '\n\n', code, flags=re.DOTALL)

with open('lib/features/dictionary/dictionary_popup.dart', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done")
