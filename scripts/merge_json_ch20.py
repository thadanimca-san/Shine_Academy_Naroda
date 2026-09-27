import json
import os

parts = [
    '/home/ubuntu/.gemini/antigravity/brain/f9616b5a-963e-4aee-bfa3-160c4d5736f2/scratch/part1.json',
    '/home/ubuntu/.gemini/antigravity/brain/18340c09-0e5f-4425-9030-f252d452539b/scratch/part2.json',
    '/home/ubuntu/.gemini/antigravity/brain/4c7198c5-52f8-4a7e-a41a-9bc1c77a08b1/scratch/part3.json',
    '/home/ubuntu/.gemini/antigravity/brain/a79dfdfd-723f-4256-86ac-a2e5d4f3f5fe/scratch/part4.json'
]

all_blocks = []
for p in parts:
    try:
        with open(p, 'r', encoding='utf-8') as f:
            data = json.load(f)
            all_blocks.extend(data)
    except Exception as e:
        print(f"Error reading {p}: {e}")

target_file = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class7_social_science_ch20.json'

with open(target_file, 'r', encoding='utf-8') as f:
    chapter_data = json.load(f)

chapter_data['blocks'].extend(all_blocks)

with open(target_file, 'w', encoding='utf-8') as f:
    json.dump(chapter_data, f, indent=2, ensure_ascii=False)

print(f"Successfully merged {len(all_blocks)} blocks into {target_file}")
