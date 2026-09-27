import re

with open('lib/features/learning/school/english/widgets/dictionary_word_widgets.dart', 'r', encoding='utf-8') as f:
    code = f.read()

old_code = """              if (UniversalDictionaryService.instance.getSourceFileForTerm(word['id']?.toString() ?? '') != null)
                AdminEditButton(
                  jsonPath: UniversalDictionaryService.instance.getSourceFileForTerm(word['id']?.toString() ?? '')!,
                  data: const {},
                ),"""

new_code = """              FutureBuilder<String?>(
                future: UniversalDictionaryService.instance.getSourceFileForTerm(word['id']?.toString() ?? ''),
                builder: (context, snapshot) {
                  if (snapshot.hasData && snapshot.data != null) {
                    return AdminEditButton(
                      jsonPath: snapshot.data!,
                      data: const {},
                    );
                  }
                  return const SizedBox.shrink();
                },
              ),"""

code = code.replace(old_code, new_code)

with open('lib/features/learning/school/english/widgets/dictionary_word_widgets.dart', 'w', encoding='utf-8') as f:
    f.write(code)

print("Done")
