import json

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch8.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

count = 0
for block in data['blocks']:
    if block.get('type') == 'practice_question' or block.get('type') == 'worked_example':
        sol = block.get('solution', '')
        if sol and '|' not in sol and 'Self-study' not in sol:
            print(f"ID: {block['id']}, Question: {block['question'][:50]}")
            count += 1

print(f"Total found: {count}")
