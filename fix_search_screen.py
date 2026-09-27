import re

path = "lib/features/learning/school/english/screens/dictionary_search_screen.dart"
with open(path, "r") as f:
    content = f.read()

# Add service import
content = content.replace("import '../widgets/dictionary_word_widgets.dart';", "import '../widgets/dictionary_word_widgets.dart';\nimport '../../../../core/services/universal_dictionary_service.dart';")

content = content.replace("final DictionaryWord word;", "final Map<String, dynamic> word;")

# Replace _allWordsFlattened
old_flatten = """  List<_MatchedWord> get _allWordsFlattened {
    final result = <_MatchedWord>[];
    for (final entry in dictionaryTopicsByGrade.entries) {
      for (final topic in entry.value) {
        for (final word in topic.words) {
          result.add(_MatchedWord(word: word, grade: entry.key, topicTitle: topic.title));
        }
      }
    }
    return result;
  }"""

new_flatten = """  List<_MatchedWord> get _allWordsFlattened {
    final result = <_MatchedWord>[];
    final service = UniversalDictionaryService.instance;
    
    for (final entry in dictionaryTopicsByGrade.entries) {
      for (final topic in entry.value) {
        if (topic.words.isNotEmpty) {
          for (final w in topic.words) {
            final wordMap = {
              'term': {'english': w.word, 'hindi': w.meaningHi, 'gujarati': w.meaningGu ?? ''},
              'definition': {'simple': {'en': w.meaningEn, 'hi': w.meaningHi, 'gu': w.meaningGu ?? ''}},
              'examples': [{'en': w.exampleEn, 'hi': w.exampleHi ?? '', 'gu': w.exampleGu ?? ''}],
              'media': {'emoji': w.emoji, 'imagePath': w.imagePath},
              'part_of_speech': w.partOfSpeech,
              'category': w.category,
            };
            result.add(_MatchedWord(word: wordMap, grade: entry.key, topicTitle: topic.title));
          }
        } else if (topic.wordIds != null) {
          for (final id in topic.wordIds!) {
            final term = service.getTermById(id);
            if (term != null) {
              result.add(_MatchedWord(word: term, grade: entry.key, topicTitle: topic.title));
            }
          }
        }
      }
    }
    return result;
  }"""

content = content.replace(old_flatten, new_flatten)

# Replace matches
old_matches = """            final matchesGrade = _gradeFilter == null || m.grade == _gradeFilter;
            final matchesQuery = m.word.word.toLowerCase().contains(query) ||
                m.word.meaningHi.contains(_query.trim()) ||
                m.word.meaningEn.toLowerCase().contains(query);
            return matchesGrade && matchesQuery;"""

new_matches = """            final matchesGrade = _gradeFilter == null || m.grade == _gradeFilter;
            final termEn = m.word['term']?['english']?.toString().toLowerCase() ?? '';
            final termHi = m.word['term']?['hindi']?.toString() ?? '';
            final defEn = m.word['definition']?['simple']?['en']?.toString().toLowerCase() ?? '';
            
            final matchesQuery = termEn.contains(query) ||
                termHi.contains(_query.trim()) ||
                defEn.contains(query);
            return matchesGrade && matchesQuery;"""

content = content.replace(old_matches, new_matches)

with open(path, "w") as f:
    f.write(content)

print("Fixed search screen!")
