import re

path = "lib/features/learning/school/english/screens/dictionary_words_screen.dart"
with open(path, "r") as f:
    content = f.read()

content = content.replace("import '../widgets/dictionary_word_widgets.dart';", "import '../widgets/dictionary_word_widgets.dart';\nimport '../../../../core/services/universal_dictionary_service.dart';")

# Replace the words list generation inside build
old_words = """    final words = widget.topic.words.where((w) {
      final matchesCategory = _selectedCategory == null || w.category == _selectedCategory;
      final matchesQuery = _query.isEmpty ||
          w.word.toLowerCase().contains(_query.toLowerCase()) ||
          w.meaningHi.contains(_query);
      return matchesCategory && matchesQuery;
    }).toList();"""

new_words = """    List<Map<String, dynamic>> words = [];
    
    // Legacy support
    if (widget.topic.words.isNotEmpty) {
      words = widget.topic.words.map((w) => {
        'term': {'english': w.word, 'hindi': w.meaningHi, 'gujarati': w.meaningGu ?? ''},
        'definition': {'simple': {'en': w.meaningEn, 'hi': w.meaningHi, 'gu': w.meaningGu ?? ''}},
        'examples': [
          {'en': w.exampleEn, 'hi': w.exampleHi ?? '', 'gu': w.exampleGu ?? ''}
        ],
        'media': {'emoji': w.emoji, 'imagePath': w.imagePath},
        'part_of_speech': w.partOfSpeech,
        'category': w.category,
      }).toList();
    } 
    // New JSON support
    else if (widget.topic.wordIds != null) {
      final service = UniversalDictionaryService.instance;
      for (String id in widget.topic.wordIds!) {
        final term = service.getTermById(id);
        if (term != null) {
          words.add(term);
        }
      }
    }

    words = words.where((w) {
      final category = w['category'] as String?;
      final termEn = w['term']?['english']?.toString().toLowerCase() ?? '';
      final termHi = w['term']?['hindi']?.toString() ?? '';
      
      final matchesCategory = _selectedCategory == null || category == _selectedCategory;
      final matchesQuery = _query.isEmpty ||
          termEn.contains(_query.toLowerCase()) ||
          termHi.contains(_query);
      return matchesCategory && matchesQuery;
    }).toList();"""

content = content.replace(old_words, new_words)

# Replace widget.topic.categories with a dynamic extract
old_cats = """                ...widget.topic.categories.map("""
new_cats = """                ...words.map((w) => w['category'] as String?).where((c) => c != null).toSet().cast<String>().map("""
content = content.replace(old_cats, new_cats)

with open(path, "w") as f:
    f.write(content)

print("Fixed words screen!")
