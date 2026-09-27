import json

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch1.json') as f:
    data = json.load(f)

for idx, b in enumerate(data.get('blocks', [])):
    print(f"Block {idx}: type={b.get('type')}, id={b.get('id')}")
