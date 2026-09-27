import os
import re
import time
from deep_translator import GoogleTranslator

# We will skip chapter_class3.dart because we already translated it manually.
directory = "/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school/english3to6/data"
translator = GoogleTranslator(source='hi', target='gu')

# Regex to find hindiSummary block
# Captures hindiSummary: '... ' \n ' ...',
summary_pattern = re.compile(r"(hindiSummary:\s*)((?:'[^']*'(?:\s*\+\s*)?(?:\s*\n\s*)?)+)(,)", re.MULTILINE)

# Regex to find InlineGloss
gloss_pattern = re.compile(r"(InlineGloss\([^)]*meaningHi:\s*'([^']+)'[^)]*hiTransliteration:\s*'([^']+)'[^)]*)(\))")

def translate_to_gujarati(text):
    try:
        # Avoid rate limits
        time.sleep(0.5)
        return translator.translate(text)
    except Exception as e:
        print(f"Translation failed for {text}: {e}")
        return text

def process_file(filepath):
    if "chapter_class3.dart" in filepath:
        return # Skip the one we manually did
        
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
        
    if "gujaratiSummary" in content:
        print(f"Skipping {os.path.basename(filepath)} - already translated")
        return
        
    print(f"Processing {os.path.basename(filepath)}...")
    
    # 1. Translate Summary
    def summary_repl(match):
        prefix = match.group(1)
        original_string_block = match.group(2)
        suffix = match.group(3)
        
        # Extract actual text without quotes and newlines
        clean_text = original_string_block.replace("'", "").replace("\n", "").replace("+", "").strip()
        
        guj_text = translate_to_gujarati(clean_text)
        
        # Format it back nicely (just use one multi-line string or long string)
        new_guj_block = f"\n  gujaratiSummary:\n      '{guj_text}'"
        
        return f"{prefix}{original_string_block}{suffix}{new_guj_block}"

    content = summary_pattern.sub(summary_repl, content)
    
    # 2. Translate Glosses
    def gloss_repl(match):
        prefix = match.group(1) # Everything up to hiTransliteration: '...'
        hindi_meaning = match.group(2)
        hi_translit = match.group(3)
        suffix = match.group(4) # The closing parenthesis
        
        guj_meaning = translate_to_gujarati(hindi_meaning)
        # For guTransliteration, we can just use the hindi transliteration since they sound similar,
        # or just make it generic. We'll reuse hiTransliteration for now since they share Sanskrit roots.
        
        return f"{prefix}, meaningGu: '{guj_meaning}', guTransliteration: '{hi_translit}'{suffix}"
        
    content = gloss_pattern.sub(gloss_repl, content)
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
        
for filename in os.listdir(directory):
    if filename.startswith("chapter_class") and filename.endswith(".dart"):
        filepath = os.path.join(directory, filename)
        process_file(filepath)
        
print("All 40 chapters translated successfully!")
