import json
import os
import re

def title_case(text):
    # Simple title case, keeping short words lowercase unless they are the first word
    words = text.split()
    lower_words = {'a', 'an', 'the', 'and', 'but', 'or', 'for', 'nor', 'on', 'at', 'to', 'from', 'by', 'with', 'of', 'in'}
    capitalized = []
    for i, w in enumerate(words):
        w = w.lower()
        if i == 0 or w not in lower_words:
            w = w.capitalize()
        capitalized.append(w)
    return ' '.join(capitalized)

def fix_title(old_title):
    # Match "LESSON X SOME TITLE TEXT123"
    match = re.match(r'^LESSON (\d+)\s+(.+?)(\d*)$', old_title, re.IGNORECASE)
    if match:
        num = match.group(1)
        text = match.group(2).strip()
        # Clean up the text
        clean_text = title_case(text)
        return f"Chapter No {num}: {clean_text}"
    return old_title

# 1. Update curriculum file
curr_path = 'app_core/curriculum/govindsir_english.json'
with open(curr_path, 'r') as f:
    curr_data = json.load(f)

for subject in curr_data.get('subjects', []):
    for chapter in subject.get('chapters', []):
        old_title = chapter.get('title', '')
        new_title = fix_title(old_title)
        if new_title != old_title:
            print(f"Curriculum: {old_title} -> {new_title}")
            chapter['title'] = new_title

with open(curr_path, 'w') as f:
    json.dump(curr_data, f, indent=2)

# 2. Update individual chapter files
chapters_dir = 'app_core/chapters'
for filename in os.listdir(chapters_dir):
    if filename.startswith('govindsir_english_ch') and filename.endswith('.json'):
        filepath = os.path.join(chapters_dir, filename)
        with open(filepath, 'r') as f:
            try:
                ch_data = json.load(f)
            except json.JSONDecodeError:
                print(f"Error reading {filepath}")
                continue
        
        if 'metadata' in ch_data and 'title' in ch_data['metadata']:
            old_title = ch_data['metadata']['title']
            new_title = fix_title(old_title)
            if new_title != old_title:
                print(f"Chapter File ({filename}): {old_title} -> {new_title}")
                ch_data['metadata']['title'] = new_title
                with open(filepath, 'w') as f:
                    json.dump(ch_data, f, indent=2)

print("Done fixing titles.")
