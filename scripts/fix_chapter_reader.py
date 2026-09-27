import re

filepath = "/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school/english/screens/chapter_reader_screen.dart"

with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add listener to TrilingualService
init_state_replacement = """  @override
  void initState() {
    super.initState();
    _chapter = widget.chapter;
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
    r'  @override\s+void initState\(\) \{\s+super\.initState\(\);\s+_chapter = widget\.chapter;\s+_tryLoadLocalOverride\(\);\s+\}',
    init_state_replacement,
    content
)

# 2. Remove _Lang enum and _lang variable
content = re.sub(r'enum _Lang \{ english, hindi, gujarati \}\n', '', content)
content = re.sub(r'\s*_Lang _lang = _Lang\.english;\n', '\n', content)

# 3. Replace _lang checks with TrilingualService checks
content = content.replace('_lang == _Lang.hindi', "TrilingualService.instance.activeViewLanguage == 'hi'")
content = content.replace('_lang == _Lang.gujarati', "TrilingualService.instance.activeViewLanguage == 'gu'")

# 4. Remove _buildLanguageChips from body
content = re.sub(
    r'\s*// ── Language chip bar ──[\s\S]*?if \(hasHindi \|\| hasGujarati\)\s*Padding\(\s*padding: const EdgeInsets\.only\(bottom: 16\),\s*child: _buildLanguageChips\(\s*hasHindi: hasHindi, hasGujarati: hasGujarati\),\s*\),',
    '',
    content
)

# 5. Remove the _buildLanguageChips function completely
content = re.sub(r'  Widget _buildLanguageChips\(\{\s*required bool hasHindi,\s*required bool hasGujarati,\s*\}\) \{[\s\S]*?  \}\n', '', content)

# 6. Add .adaptToLanguage() to TextStyles
# 6a. Hindi TtsHighlightText style
content = re.sub(
    r'(TtsHighlightText\(\s*text: chapter\.hindiText \?\? chapter\.hindiSummary,\s*style: TextStyle\(\s*fontSize: 16,\s*height: 1\.7,\s*color: AppColors\.ink,\s*fontWeight: FontWeight\.w500\))(?!\.adaptToLanguage)',
    r'\1.adaptToLanguage()',
    content
)

# 6b. Gujarati TtsHighlightText style
content = re.sub(
    r'(TtsHighlightText\(\s*text: chapter\.gujaratiText \?\? chapter\.gujaratiSummary!,\s*style: TextStyle\(\s*fontSize: 16,\s*height: 1\.7,\s*color: AppColors\.ink,\s*fontWeight: FontWeight\.w500\))(?!\.adaptToLanguage)',
    r'\1.adaptToLanguage()',
    content
)

# 6c. English TtsHighlightText style (Wait, it is GlossedText)
# We don't have .adaptToLanguage on GlossedText here yet? Wait, GlossedText takes a baseStyle but in this file it doesn't pass one!
# In chapter_reader_screen.dart: `GlossedText(text: chapter.chapterText, glosses: chapter.glosses),`
# Let's add it: `GlossedText(text: chapter.chapterText, glosses: chapter.glosses, baseStyle: TextStyle(fontSize: 16, height: 1.7, color: AppColors.ink).adaptToLanguage()),`
content = re.sub(
    r'GlossedText\(\s*text: chapter\.chapterText,\s*glosses: chapter\.glosses\)',
    r'GlossedText(text: chapter.chapterText, glosses: chapter.glosses, baseStyle: const TextStyle(fontSize: 16, height: 1.7, color: AppColors.ink).adaptToLanguage())',
    content
)

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated chapter_reader_screen.dart successfully")
