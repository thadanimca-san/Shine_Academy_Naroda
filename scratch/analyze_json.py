import json

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_maths_ch1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

blocks = data.get('blocks', [])
print(f"Total blocks: {len(blocks)}")
unique_titles = set()
duplicates = 0
for b in blocks:
    title = b.get('title') or b.get('question')
    if title:
        if title in unique_titles:
            duplicates += 1
        else:
            unique_titles.add(title)

print(f"Duplicate titles/questions: {duplicates}")

questions = [b for b in blocks if b.get('type') in ('mcq', 'practice_question', 'worked_example')]
print(f"Total questions/examples: {len(questions)}")
