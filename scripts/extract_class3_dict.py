import os
import re
import json

base_dir = "lib/features/learning/school/english/data"
class3_files = [f for f in os.listdir(base_dir) if f.startswith("class3_") and f.endswith(".dart")]

extracted_words = []

word_pattern = re.compile(r"DictionaryWord\((.*?)\)", re.DOTALL)

for f in class3_files:
    filepath = os.path.join(base_dir, f)
    with open(filepath, "r") as file:
        content = file.read()
        
    topic_match = re.search(r"id:\s*'([^']+)'", content)
    topic_id = topic_match.group(1) if topic_match else f.replace(".dart", "")
    
    matches = word_pattern.findall(content)
    for m in matches:
        word_data = {}
        # Parse fields
        fields = ["word", "partOfSpeech", "emoji", "imagePath", "meaningEn", "meaningHi", "meaningGu", "exampleEn", "exampleHi", "exampleGu", "category"]
        for field in fields:
            # Match field: 'value' or field: "value"
            match = re.search(rf"{field}:\s*['\"](.*?)['\"]", m)
            if match:
                word_data[field] = match.group(1)
        
        word_data['topic_id'] = topic_id
        extracted_words.append(word_data)

with open("temp_class3_words.json", "w") as out:
    json.dump(extracted_words, out, indent=2)

print(f"Extracted {len(extracted_words)} words to temp_class3_words.json")
