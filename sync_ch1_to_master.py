import json

with open('app_core/chapters/ncert_class10_maths_ch1.json', 'r', encoding='utf-8') as f:
    ch1_data = json.load(f)

blocks_map = {b['id']: b for b in ch1_data['blocks'] if 'id' in b}

with open('app_core/learning_modules/master_curriculum.json', 'r', encoding='utf-8') as f:
    master_data = json.load(f)

updated = 0
for module_id, module_data in master_data.items():
    if 'blocks' in module_data:
        for idx, block in enumerate(module_data['blocks']):
            if 'id' in block and block['id'] in blocks_map:
                src_block = blocks_map[block['id']]
                for field in ['title_gu', 'body_gu', 'question_gu', 'options_gu', 'explanation_gu']:
                    if field in src_block and field not in block:
                        block[field] = src_block[field]
                        updated += 1

if updated > 0:
    with open('app_core/learning_modules/master_curriculum.json', 'w', encoding='utf-8') as f:
        json.dump(master_data, f, ensure_ascii=False, indent=2)
    print(f"Updated {updated} fields in master curriculum.")
else:
    print("No updates needed in master curriculum.")
