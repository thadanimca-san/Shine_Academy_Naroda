import json
import os

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch3.json'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    blocks = data.get('blocks', [])
    print(f"{filepath} exists.")
    print(f"Total blocks: {len(blocks)}")
    for i, b in enumerate(blocks):
        print(f"Block {i}: {b.get('id')} - {b.get('title')}")
else:
    print(f"{filepath} does NOT exist.")
