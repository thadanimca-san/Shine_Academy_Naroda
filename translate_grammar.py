import os
import glob
import re
try:
    from deep_translator import GoogleTranslator
except ImportError:
    os.system("pip install deep-translator")
    from deep_translator import GoogleTranslator

translator = GoogleTranslator(source='en', target='hi')

def translate_str(s):
    if not s.strip(): return s
    try:
        t = translator.translate(s)
        return t.replace("'", "\\'")
    except:
        return s

def process_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        lines = f.readlines()
        
    out_lines = []
    skip = False
    
    # Simple state to check if we already processed this file
    if any("promptHi:" in l for l in lines):
        print(f"Skipping {filepath}, already translated.")
        return

    for line in lines:
        out_lines.append(line)
        
        # prompt
        m_prompt = re.match(r"^(\s*)prompt:\s*'((?:\\.|[^'\\])*)',?\s*$", line)
        if m_prompt:
            indent, text = m_prompt.groups()
            text_unesc = text.replace("\\'", "'").replace("\\n", "\n")
            t = translate_str(text_unesc).replace("\n", "\\n")
            out_lines.append(f"{indent}promptHi: '{t}',\n")
            
        # explanation
        m_expl = re.match(r"^(\s*)explanation:\s*'((?:\\.|[^'\\])*)',?\s*$", line)
        if m_expl:
            indent, text = m_expl.groups()
            text_unesc = text.replace("\\'", "'").replace("\\n", "\n")
            t = translate_str(text_unesc).replace("\n", "\\n")
            out_lines.append(f"{indent}explanationHi: '{t}',\n")
            
        # options
        m_opts = re.match(r"^(\s*)options:\s*\[(.*)\],?\s*$", line)
        if m_opts:
            indent, opts_str = m_opts.groups()
            opt_matches = re.findall(r"'((?:\\.|[^'\\])*)'", opts_str)
            translated_opts = []
            for opt in opt_matches:
                opt_unesc = opt.replace("\\'", "'")
                t = translate_str(opt_unesc)
                translated_opts.append(f"'{t}'")
            out_lines.append(f"{indent}optionsHi: [{', '.join(translated_opts)}],\n")
            
    with open(filepath, 'w', encoding='utf-8') as f:
        f.writelines(out_lines)
    print(f"Translated {filepath}")

paths = glob.glob("lib/features/learning/school/english3to6/data/practice_*.dart")
paths += glob.glob("lib/features/learning/school/english_simulation/data/practice_*.dart")

for p in paths:
    process_file(p)

print("Done translating grammar!")
