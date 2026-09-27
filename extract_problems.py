import json

with open('/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_accounts_ch11.json', 'r') as f:
    data = json.load(f)

count = 0
for block in data.get('blocks', []):
    sol = block.get('solution', '')
    if sol in ["Student should practice this question.", "", "Solution involves interpreting the provided balance sheet data.", "Students need to calculate the missing values based on the given totals and percentages."]:
        print(f"--- ID: {block['id']} ---")
        q = block.get('question') or block.get('body_en') or block.get('table_markdown')
        print(q)
        count += 1

print(f"Total found: {count}")
