import json

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/cbse_class10_math_ch1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for i, block in enumerate(data['blocks']):
    for key in block:
        if isinstance(block[key], str):
            if key not in ['id', 'type', 'bloom', 'difficulty', 'answer', 'correct_index']:
                if key + '_hi' not in block:
                    print(f"Missing {key}_hi in block {block['id']}")
                if key + '_gu' not in block:
                    print(f"Missing {key}_gu in block {block['id']}")

