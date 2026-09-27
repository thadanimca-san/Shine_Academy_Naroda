import json

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch9.json'
with open(filepath, 'r') as f:
    data = json.load(f)

blocks = data.get('blocks', [])
for i, b in enumerate(blocks[:8]):
    print(f"\n--- Block {i}: {b.get('title')} ---")
    print(b.get('body') or b.get('question'))
