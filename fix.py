import re

with open('lib/features/dictionary/dictionary_popup.dart', 'r') as f:
    text = f.read()

# 1. Remove the misplaced closing brace for UniversalDictionaryPopup
text = text.replace("""    );
  }
}

  // ─────────────────────────────────────────────────────────────────────────
  // "Not found" panel — shows the query and the nearest alphabetical word""", """    );
  }

  // ─────────────────────────────────────────────────────────────────────────
  // "Not found" panel — shows the query and the nearest alphabetical word""")

# 2. Add the closing brace BEFORE class _DictionaryPopupContent
text = text.replace("""class _DictionaryPopupContent extends StatefulWidget {""", """}

class _DictionaryPopupContent extends StatefulWidget {""")

# 3. Ensure we didn't add duplicate classes at the bottom
if text.count("class _DictionaryPopupContent") > 1:
    idx = text.rfind("class _DictionaryPopupContent")
    text = text[:idx]

with open('lib/features/dictionary/dictionary_popup.dart', 'w') as f:
    f.write(text)
