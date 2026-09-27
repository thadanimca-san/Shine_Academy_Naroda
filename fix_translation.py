import re

with open("lib/features/learning/learning_engine/learning_engine_screen.dart", "r") as f:
    lines = f.readlines()

# Add _isTranslating and _lastLang to state
for i, line in enumerate(lines):
    if "bool _showBoardQuestions = false;" in line:
        lines.insert(i+1, "  bool _isTranslating = false;\n  late String _lastLang;\n")
        break

# Update initState to set _lastLang and add listener
for i, line in enumerate(lines):
    if "void initState() {" in line:
        # find super.initState()
        for j in range(i, i+10):
            if "super.initState();" in lines[j]:
                lines.insert(j+1, "    _lastLang = TrilingualService.instance.activeViewLanguage;\n    TrilingualService.instance.addListener(_onLanguageChanged);\n")
                break
        break

# Add dispose listener removal
for i, line in enumerate(lines):
    if "void dispose() {" in line:
        for j in range(i, i+10):
            if "super.dispose();" in lines[j]:
                lines.insert(j, "    TrilingualService.instance.removeListener(_onLanguageChanged);\n")
                break
        break

# Add _onLanguageChanged and _translateBlocks methods right before _loadModule
for i, line in enumerate(lines):
    if "Future<void> _loadModule() async {" in line:
        methods = """
  void _onLanguageChanged() {
    final currentLang = TrilingualService.instance.activeViewLanguage;
    if (_lastLang != currentLang) {
      _lastLang = currentLang;
      if (currentLang != 'en') {
        _translateBlocks();
      }
    }
  }

  Future<void> _translateBlocks() async {
    if (!mounted) return;
    setState(() {
      _isTranslating = true;
    });
    
    await TrilingualService.instance.preTranslateBlocks(_blocks, isDictionary: widget.moduleId.contains('DICT'));
    
    if (!mounted) return;
    setState(() {
      _isTranslating = false;
    });
  }
"""
        lines.insert(i, methods)
        break

# Call _translateBlocks inside _loadModule
for i, line in enumerate(lines):
    if "_isLoading = false;" in line and "setState(() {" in lines[i-5:i]:
        # There are multiple _isLoading = false. We want the one for successful block load
        if "_blocks = " in "".join(lines[i-4:i+1]):
            lines.insert(i+2, "          if (TrilingualService.instance.activeViewLanguage != 'en') {\n            _translateBlocks();\n          }\n")

# Finally add a LinearProgressIndicator if _isTranslating is true to the AppBar or Body
for i, line in enumerate(lines):
    if "return Scaffold(" in line:
        for j in range(i, i+30):
            if "appBar: BrandAppBar(" in lines[j]:
                lines[j] = lines[j].replace("appBar: BrandAppBar(", "appBar: BrandAppBar(\n        bottom: _isTranslating ? const PreferredSize(preferredSize: Size.fromHeight(4), child: LinearProgressIndicator(color: Colors.yellow)) : null,")
                break
        break

with open("lib/features/learning/learning_engine/learning_engine_screen.dart", "w") as f:
    f.writelines(lines)
print("Done fixing translations")
