import json
import re

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch8.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Hardcoded solutions to inject
solutions = {
    "KOBJ_ACC_CH8_9_5": {
        "solution": "",
        "solution_hi": "",
        "solution_gu": ""
    }
}

count = 0
for block in data['blocks']:
    if block.get('id') in solutions:
        block['solution'] = solutions[block['id']]['solution']
        block['solution_hi'] = solutions[block['id']]['solution_hi']
        block['solution_gu'] = solutions[block['id']]['solution_gu']
        count += 1

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print(f"Injected {count} solutions.")
