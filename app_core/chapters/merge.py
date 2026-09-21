import json
import os

files = ['chunk1.json', 'chunk2.json', 'chunk3.json', 'chunk4.json', 'chunk5.json']
combined = []
base_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'

for f in files:
    path = os.path.join(base_dir, f)
    if os.path.exists(path):
        with open(path, 'r', encoding='utf-8') as fp:
            try:
                data = json.load(fp)
                if isinstance(data, list):
                    combined.extend(data)
                elif isinstance(data, dict):
                    combined.append(data)
            except Exception as e:
                print(f"Error loading {f}: {e}")

out_path = os.path.join(base_dir, 'gseb_class12_accounts_ch1.json')
with open(out_path, 'w', encoding='utf-8') as fp:
    json.dump(combined, fp, indent=2, ensure_ascii=False)

print(f"Merged successfully into {out_path}")
