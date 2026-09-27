import json
import os

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch12.json'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    print("Title:", data.get('metadata', {}).get('title'))
    blocks = data.get('blocks', [])
    print(f"Total blocks in Chapter 12: {len(blocks)}")
else:
    print(f"{filepath} does NOT exist.")
