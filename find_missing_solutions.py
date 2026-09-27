import json

files = [
    '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch7.json',
    '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch12.json'
]

for file in files:
    with open(file, 'r') as f:
        data = json.load(f)
    print(f"--- {file} ---")
    for block in data.get('blocks', []):
        if block.get('type') == 'worked_example' or block.get('type') == 'exercise':
            # Check if solution is missing or empty
            if 'solution' not in block or block.get('solution') is None or str(block.get('solution')).strip() == "":
                print(f"Missing solution in block ID: {block.get('id')}")
                print(f"Question: {block.get('question')}")
