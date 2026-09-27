import json

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch9.json'
with open(filepath, 'r') as f:
    data = json.load(f)

blocks = data.get('blocks', [])
for i in range(17, 21):
    if i < len(blocks):
        b = blocks[i]
        print(f"\n--- Block {i}: {b.get('title')} ---")
        print("Options EN:", b.get('options'))
        print("Options HI:", b.get('options_hi'))
        print("Options GU:", b.get('options_gu'))
