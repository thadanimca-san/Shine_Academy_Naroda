import re

path = "lib/features/learning/school/english/widgets/dictionary_word_widgets.dart"
with open(path, "r") as f:
    content = f.read()
    
# Remove import '../models/dictionary_word.dart';
content = content.replace("import '../models/dictionary_word.dart';", "")

content = content.replace("final DictionaryWord word;", "final Map<String, dynamic> word;")

content = content.replace(
"""                  child: word.emoji != null
                      ? Text(word.emoji!, style: const TextStyle(fontSize: 22))
                      : const Icon(Icons.menu_book_outlined, color: AppColors.saffronDeep, size: 22),""",
"""                  child: (word['media'] != null && word['media']['emoji'] != null)
                      ? Text(word['media']['emoji'], style: const TextStyle(fontSize: 22))
                      : const Icon(Icons.menu_book_outlined, color: AppColors.saffronDeep, size: 22),"""
)

content = content.replace("word.word", "(word['term']?['english'] ?? '')")
content = content.replace("word.meaningHi", "(word['term']?['hindi'] ?? '')")

content = content.replace(
"""            Expanded(
              child: Text(
                word.meaningEn,
                maxLines: 3,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(fontSize: 12.5, color: AppColors.inkSoft),
              ),
            ),""",
"""            Expanded(
              child: Text(
                word['definition'] != null && word['definition']['simple'] != null 
                    ? (word['definition']['simple'] is Map ? word['definition']['simple']['en'] ?? '' : word['definition']['simple']) 
                    : '',
                maxLines: 3,
                overflow: TextOverflow.ellipsis,
                style: const TextStyle(fontSize: 12.5, color: AppColors.inkSoft),
              ),
            ),"""
)


content = content.replace(
"""              child: word.emoji != null
                  ? Text(word.emoji!, style: const TextStyle(fontSize: 44))
                  : const Icon(Icons.menu_book_outlined, color: AppColors.saffronDeep, size: 40),""",
"""              child: (word['media'] != null && word['media']['emoji'] != null)
                  ? Text(word['media']['emoji'], style: const TextStyle(fontSize: 44))
                  : const Icon(Icons.menu_book_outlined, color: AppColors.saffronDeep, size: 40),"""
)

content = content.replace(
"""          if (word.emoji == null) ...[""",
"""          if (word['media'] == null || word['media']['emoji'] == null) ...["""
)

content = content.replace(
"""              Text(word.partOfSpeech, style: const TextStyle(fontSize: 12, color: AppColors.inkFaint)),""",
"""              Text(word['part_of_speech'] ?? 'noun', style: const TextStyle(fontSize: 12, color: AppColors.inkFaint)),"""
)

content = content.replace(
"""          Text(
            '${word.meaningHi}  ·  ${word.hiTransliteration}',
            style: const TextStyle(fontSize: 16, color: AppColors.tealDeep),
          ),
          const SizedBox(height: 12),
          Text(word.meaningEn, style: const TextStyle(fontSize: 15, color: AppColors.inkSoft)),
          const SizedBox(height: 10),
          Container(
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: AppColors.paperRaised,
              borderRadius: BorderRadius.circular(8),
            ),
            child: Text('"${word.exampleEn}"', style: const TextStyle(fontStyle: FontStyle.italic, color: AppColors.inkSoft)),
          ),""",
"""          Text(
            '${word['term']?['hindi'] ?? ''}  ·  ${word['term']?['gujarati'] ?? ''}',
            style: const TextStyle(fontSize: 16, color: AppColors.tealDeep),
          ),
          const SizedBox(height: 12),
          Text(word['definition'] != null && word['definition']['simple'] != null 
                    ? (word['definition']['simple'] is Map ? word['definition']['simple']['en'] ?? '' : word['definition']['simple']) 
                    : '', style: const TextStyle(fontSize: 15, color: AppColors.inkSoft)),
          const SizedBox(height: 10),
          
          if (word['examples'] != null && (word['examples'] as List).isNotEmpty)
            ...((word['examples'] as List).map((ex) {
              String exEn = ex is Map ? (ex['en'] ?? '') : ex.toString();
              String exHi = ex is Map ? (ex['hi'] ?? '') : '';
              String exGu = ex is Map ? (ex['gu'] ?? '') : '';
              
              return Container(
                margin: const EdgeInsets.only(bottom: 8),
                width: double.infinity,
                padding: const EdgeInsets.all(12),
                decoration: BoxDecoration(
                  color: AppColors.paperRaised,
                  borderRadius: BorderRadius.circular(8),
                ),
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text('"$exEn"', style: const TextStyle(fontStyle: FontStyle.italic, color: AppColors.inkSoft, fontSize: 14)),
                    if (exHi.isNotEmpty)
                      Padding(
                        padding: const EdgeInsets.only(top: 4),
                        child: Text(exHi, style: const TextStyle(color: AppColors.inkFaint, fontSize: 13)),
                      ),
                    if (exGu.isNotEmpty)
                      Padding(
                        padding: const EdgeInsets.only(top: 2),
                        child: Text(exGu, style: const TextStyle(color: AppColors.inkFaint, fontSize: 13)),
                      ),
                  ],
                ),
              );
            }).toList()),"""
)

with open(path, "w") as f:
    f.write(content)

print("Updated widgets!")
