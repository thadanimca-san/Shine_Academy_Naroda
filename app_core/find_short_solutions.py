import json

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch2.json', 'r') as f:
    data = json.load(f)

for block in data.get('blocks', []):
    if block.get('type') in ('practice_question', 'mcq'):
        sol = block.get('solution', '')
        if len(sol) < 100:  # arbitrary short length
            print(f"ID: {block.get('id')}, Solution: {sol}")
