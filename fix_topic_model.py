import re

path = "lib/features/learning/school/english/models/dictionary_word.dart"
with open(path, "r") as f:
    content = f.read()

# I am completely wiping out DictionaryWord and changing DictionaryTopic.
content = """class DictionaryTopic {
  final String id;
  final String title;
  final String grade;
  final List<String> wordIds;

  const DictionaryTopic({
    required this.id,
    required this.title,
    required this.grade,
    required this.wordIds,
  });
}
"""

with open(path, "w") as f:
    f.write(content)

print("Updated topic model!")
