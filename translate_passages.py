import os
import re

# We will install deep-translator if not present
try:
    from deep_translator import GoogleTranslator
except ImportError:
    os.system("pip install deep-translator")
    from deep_translator import GoogleTranslator

paths = [
    "lib/features/learning/school/english3to6/data/reading_class3.dart",
    "lib/features/learning/school/english3to6/data/reading_class4.dart",
    "lib/features/learning/school/english3to6/data/reading_class5.dart",
    "lib/features/learning/school/english3to6/data/reading_class6.dart",
    "lib/features/learning/school/english_simulation/data/reading_class7.dart",
    "lib/features/learning/school/english_simulation/data/reading_class8.dart",
    "lib/features/learning/school/english_simulation/data/reading_class9.dart",
    "lib/features/learning/school/english_simulation/data/reading_class10.dart",
]

translator = GoogleTranslator(source='en', target='hi')

def translate_and_inject(filepath):
    if not os.path.exists(filepath):
        print(f"File not found: {filepath}")
        return

    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()

    out_lines = []
    in_body = False
    body_text = ""
    
    i = 0
    while i < len(lines):
        line = lines[i]
        out_lines.append(line)
        
        if line.strip().startswith("body:"):
            in_body = True
            
        if in_body:
            # Extract string content between single quotes handling escaped quotes
            matches = re.findall(r"'((?:\\.|[^'\\])*)'", line)
            for m in matches:
                # unescape for translation
                m_unescaped = m.replace("\\'", "'")
                body_text += m_unescaped
            
            if line.strip().endswith(","):
                in_body = False
                
                # Now translate
                try:
                    translated = translator.translate(body_text)
                    # escape single quotes
                    translated = translated.replace("'", "\\'")
                    # inject bodyHi
                    out_lines.append(f"      bodyHi: '{translated}',\n")
                    print(f"Translated chunk of length {len(body_text)} in {filepath}")
                except Exception as e:
                    print(f"Error translating: {e}")
                
                body_text = ""
        i += 1
        
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)

for p in paths:
    translate_and_inject(p)

print("Done!")
