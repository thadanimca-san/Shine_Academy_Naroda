import json
import os

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch4.json'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    blocks = data.get('blocks', [])
    for i, b in enumerate(blocks):
        title = b.get('title') or b.get('question')
        print(f"Block {i}: {title}")
else:
    print(f"{filepath} does NOT exist.")
