import re

filepath = "/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school/english/screens/reading_passage_screen.dart"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add listener to TrilingualService
init_state_replacement = """  @override
  void initState() {
    super.initState();
    _passage = widget.passage;
    _tryLoadLocalOverride();
    TrilingualService.instance.addListener(_onLangChange);
  }

  void _onLangChange() {
    if (mounted) setState(() {});
  }

  @override
  void dispose() {
    TrilingualService.instance.removeListener(_onLangChange);
    super.dispose();
  }"""

content = re.sub(
    r'  @override\s+void initState\(\) \{\s+super\.initState\(\);\s+_passage = widget\.passage;\s+_tryLoadLocalOverride\(\);\s+\}',
    init_state_replacement,
    content
)

# 2. Remove _Language enum and _lang variable
content = re.sub(r'enum _Language \{ english, hindi, gujarati \}\n', '', content)
content = re.sub(r'\s*_Language _lang = _Language\.english;\n', '\n', content)

# 3. Replace _lang checks with TrilingualService checks
content = content.replace('_lang == _Language.hindi', "TrilingualService.instance.activeViewLanguage == 'hi'")
content = content.replace('_lang == _Language.gujarati', "TrilingualService.instance.activeViewLanguage == 'gu'")

# 4. Remove _buildLanguageChips from _buildReading
content = re.sub(
    r'\s*if \(passage\.bodyHi != null \|\| passage\.bodyGu != null\)\s*Padding\(\s*padding: const EdgeInsets\.only\(bottom: 12\),\s*child: _buildLanguageChips\(\s*hasHindi: passage\.bodyHi != null,\s*hasGujarati: passage\.bodyGu != null,\s*\),\s*\),',
    '',
    content
)

# 5. Remove _buildLanguageChips from _buildQuestion
content = re.sub(
    r'\s*if \(question\.promptHi != null \|\| question\.promptGu != null\)\s*_buildLanguageChips\(\s*hasHindi: question\.promptHi != null,\s*hasGujarati: question\.promptGu != null,\s*compact: true,\s*\),',
    '',
    content
)

# 6. Remove the _buildLanguageChips function completely
content = re.sub(r'  // ─── Language Chip Bar ───[\s\S]*?  \}\n', '', content)

# 7. Add .adaptToLanguage() to TextStyles
# 7a. TtsHighlightText style
content = re.sub(
    r'(style: TextStyle\(fontSize: 18, height: 1.6, color: AppColors.ink, fontWeight: FontWeight.w500\))(?!\.adaptToLanguage)',
    r'\1.adaptToLanguage()',
    content
)
content = re.sub(
    r'(style: TextStyle\(fontSize: 16.5, height: 1.6, color: AppColors.ink\))(?!\.adaptToLanguage)',
    r'\1.adaptToLanguage()',
    content
)

# 7b. Text style for prompt
content = re.sub(
    r'(style: TextStyle\(fontSize: 18, fontWeight: FontWeight.w700, color: AppColors.ink, height: 1.35\))(?!\.adaptToLanguage)',
    r'\1.adaptToLanguage()',
    content
)

# 7c. _ReadingOptionTile Text style
content = re.sub(
    r'(Expanded\(child: Text\(text, style: TextStyle\(color: fg, fontSize: 15, fontWeight: FontWeight.w600\))(?!\.adaptToLanguage)',
    r'\1.adaptToLanguage()',
    content
)

# 7d. _ExplanationCard Text style
content = re.sub(
    r'(Expanded\(child: Text\(explanation, style: TextStyle\(color: AppColors.inkSoft, fontSize: 13.5, height: 1.4\))(?!\.adaptToLanguage)',
    r'\1.adaptToLanguage()',
    content
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated reading_passage_screen.dart successfully")
