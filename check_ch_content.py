import json
import os
import glob

files = glob.glob('app_core/chapters/gseb_class8_science_ch*.json')
files.sort(key=lambda x: int(x.split('_ch')[1].split('.')[0]))

for f in files:
    with open(f, 'r') as fp:
        try:
            data = json.load(fp)
            title = data.get('metadata', {}).get('title', 'Unknown')
            first_q = 'No questions'
            for b in data.get('blocks', []):
                if b.get('type') == 'knowledge_check' and 'question' in b.get('content', {}):
                    first_q = b['content']['question']
                    break
            print(f"{os.path.basename(f)} - Title: {title} | Q1: {first_q}")
        except Exception as e:
            print(f"Error in {f}: {e}")
