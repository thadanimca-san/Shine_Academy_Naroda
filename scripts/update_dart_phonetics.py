import os
import sys
sys.path.append('.')
from scripts.fix_all_phonetics_perfect import CUSTOM_WORDS

sorted_items = sorted(CUSTOM_WORDS.items())
dart_map_entries = []
for k, v in sorted_items:
    k_escaped = k.replace("'", "\\'")
    v_escaped = v.replace("'", "\\'")
    dart_map_entries.append(f"    '{k_escaped}': '{v_escaped}',")

map_code = '\n'.join(dart_map_entries)

dart_content = f"""/// Helper service to generate natural Hindi Devanagari pronunciation (उच्चारण)
/// for English words and sentences to assist adult learners, homemakers, and beginners.
class EnglishPhoneticsHelper {{
  EnglishPhoneticsHelper._();

  static final Map<String, String> _wordMap = {{
{map_code}
  }};

  /// Converts English text into a readable Hindi Devanagari pronunciation.
  static String toDevanagari(String text) {{
    if (text.trim().isEmpty) return '';

    // Clean markdown links e.g. [DICT_WORD|Word] -> Word
    var cleaned = text.replaceAllMapped(
      RegExp(r'\\[(?:DICT_[A-Z0-9_]+\\|)?([^\\]]+)\\]'),
      (m) => m.group(1) ?? '',
    );
    // Remove formatting stars, hashes, etc.
    cleaned = cleaned.replaceAll(RegExp(r'[*_#`~]'), '');

    final words = cleaned.split(RegExp(r'\\s+'));
    final devanagariWords = <String>[];

    for (final rawWord in words) {{
      if (rawWord.isEmpty) continue;
      // Extract punctuation and surrounding quotes
      final match = RegExp(r'^([^\\w]*)(.*?)([^\\w]*)$').firstMatch(rawWord);
      final prePunct = match?.group(1) ?? '';
      final coreWord = (match?.group(2) ?? rawWord).toLowerCase().trim();
      final postPunct = match?.group(3) ?? '';

      if (coreWord.isEmpty) {{
        devanagariWords.add(rawWord);
        continue;
      }}

      // Handle possessive 's
      if (coreWord.endsWith(\"'s\")) {{
        final base = coreWord.substring(0, coreWord.length - 2);
        final baseP = _wordMap[base] ?? _ruleBasedTransliterate(base);
        devanagariWords.add('$prePunct$baseP\\'स$postPunct');
        continue;
      }}

      String devanagari;
      if (_wordMap.containsKey(coreWord)) {{
        devanagari = _wordMap[coreWord]!;
      }} else {{
        devanagari = _ruleBasedTransliterate(coreWord);
      }}

      var cleanPost = postPunct;
      if (cleanPost == '.') cleanPost = '।';

      devanagariWords.add('$prePunct$devanagari$cleanPost');
    }}

    return devanagariWords.join(' ');
  }}

  static String _ruleBasedTransliterate(String word) {{
    var w = word.toLowerCase();

    // Suffix replacements
    if (w.endsWith('tion')) return _ruleBasedTransliterate(w.substring(0, w.length - 4)) + 'शन';
    if (w.endsWith('sion')) return _ruleBasedTransliterate(w.substring(0, w.length - 4)) + 'शन';
    if (w.endsWith('ment')) return _ruleBasedTransliterate(w.substring(0, w.length - 4)) + 'मेंट';
    if (w.endsWith('able')) return _ruleBasedTransliterate(w.substring(0, w.length - 4)) + 'एबल';
    if (w.endsWith('ing')) return _ruleBasedTransliterate(w.substring(0, w.length - 3)) + 'िंग';

    // Digraphs & consonant clusters
    final replacements = [
      ['ph', 'फ़'],
      ['th', 'थ'],
      ['sh', 'श'],
      ['ch', 'च'],
      ['ck', 'क'],
      ['wh', 'व्ह'],
      ['qu', 'क्व'],
      ['kn', 'न'],
      ['wr', 'र'],
      ['ee', 'ी'],
      ['oo', 'ू'],
      ['ea', 'ी'],
      ['ai', 'ै'],
      ['ay', 'े'],
      ['ou', 'ाउ'],
      ['b', 'ब'],
      ['c', 'क'],
      ['d', 'ड'],
      ['f', 'फ़'],
      ['g', 'ग'],
      ['h', 'ह'],
      ['j', 'ज'],
      ['k', 'क'],
      ['l', 'ल'],
      ['m', 'म'],
      ['n', 'न'],
      ['p', 'प'],
      ['q', 'क'],
      ['r', 'र'],
      ['s', 'स'],
      ['t', 'ट'],
      ['v', 'व'],
      ['w', 'व'],
      ['x', 'क्स'],
      ['y', 'य'],
      ['z', 'ज़'],
      ['a', 'ा'],
      ['e', 'े'],
      ['i', 'ि'],
      ['o', 'ो'],
      ['u', 'ु'],
    ];

    var result = w;
    for (final pair in replacements) {{
      result = result.replaceAll(pair[0], pair[1]);
    }}
    return result;
  }}
}}
"""

with open('lib/core/services/english_phonetics_helper.dart', 'w', encoding='utf-8') as f:
    f.write(dart_content)

print(f"Updated lib/core/services/english_phonetics_helper.dart with {len(CUSTOM_WORDS)} words.")
