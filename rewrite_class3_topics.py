import json
import os
import re

with open('temp_class3_words.json', 'r') as f:
    words = json.load(f)

# Group by topic
topics = {}
for w in words:
    t = w['topic_id']
    if t not in topics:
        topics[t] = []
    topics[t].append(w['word'].upper())

base_dir = "lib/features/learning/school/english/data"

for t, word_list in topics.items():
    file_path = os.path.join(base_dir, f"{t}.dart")
    if not os.path.exists(file_path):
        continue
        
    with open(file_path, "r") as f:
        content = f.read()
        
    # Replace the words array
    # words: [ ... ]
    # We can use regex to replace everything between words: [ and ]; (or similar)
    
    # Let's just generate the file from scratch! It's simpler.
    # We need to find the title, grade.
    title_match = re.search(r"title:\s*'([^']+)'", content)
    grade_match = re.search(r"grade:\s*'([^']+)'", content)
    
    title = title_match.group(1) if title_match else t
    grade = grade_match.group(1) if grade_match else 'Class 3'
    
    var_name = t
    # camelCase var_name
    parts = var_name.split('_')
    var_name = parts[0] + ''.join(x.capitalize() for x in parts[1:])
    
    word_ids = [f"'DICT_ENG_{w}'" for w in word_list]
    word_ids_str = ",\n    ".join(word_ids)
    
    new_content = f"""import '../models/dictionary_word.dart';

const {var_name} = DictionaryTopic(
  id: '{t}',
  title: '{title}',
  grade: '{grade}',
  wordIds: [
    {word_ids_str}
  ],
);
"""
    with open(file_path, "w") as f:
        f.write(new_content)

print("Rewrote class3 topics!")
