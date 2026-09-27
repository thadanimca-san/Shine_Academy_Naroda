import json
import os

filepath = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch4.json'
if os.path.exists(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    blocks = data.get('blocks', [])
    print(f"Total blocks in Chapter 4: {len(blocks)}")
    # check the last 10 blocks to see if it has NCERT questions
    for i in range(max(0, len(blocks)-10), len(blocks)):
        b = blocks[i]
        title = b.get('title') or b.get('question')
        print(f"Block {i}: {title[:50] if title else 'No Title'}")
else:
    print(f"{filepath} does NOT exist.")
