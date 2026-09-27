import json
with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch2.json') as f:
    data = json.load(f)
for idx, b in enumerate(data.get('blocks', [])):
    print(f"Block {idx}: type={b.get('type')}, id={b.get('id')}, title={b.get('title')}")
print(f"Total blocks: {len(data.get('blocks', []))}")
