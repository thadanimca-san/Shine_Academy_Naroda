import json

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch1.json') as f:
    data = json.load(f)

blocks = data.get('blocks', [])
print(f"Total blocks: {len(blocks)}")
types = {}
for b in blocks:
    t = b.get('type', 'unknown')
    types[t] = types.get(t, 0) + 1

print(types)
