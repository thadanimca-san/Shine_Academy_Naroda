import json

file_path = 'app_core/learning_modules/master_curriculum.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

puzzle_title_gu = "ભૂતકાળમાંથી એક કોયડો"
puzzle_body_gu = "કલ્પના કરો કે તમારી પાસે ઈંડાની એક ટોપલી છે. જો તમે તેમને બબ્બેની ગણતરી કરો, તો 1 બાકી રહે છે. જો તમે ત્રણની ગણતરી કરો, તો 2 બાકી રહે છે. જો તમે ચારની ગણતરી કરો, તો 3 બાકી રહે છે... છેલ્લે સાતની ગણતરી કરતા 0 બાકી રહે છે. કુલ કેટલા ઈંડા છે? આ એક પ્રાચીન કોયડો છે. આપણે તેને ઉકેલવાની શરૂઆત કેવી રીતે કરીશું?"

division_title_gu = "ભાગાકાર વિશે વિચારો"
division_body_gu = "અત્યાર સુધી તમે ભાગાકારની પ્રક્રિયા કરતા આવ્યા છો. પરંતુ ભાગાકાર વાસ્તવમાં શું છે? તે કોઈ સંખ્યાને સમાન ભાગોમાં વહેંચવાની પ્રક્રિયા છે."  # Will replace with exact if body matches

def update_blocks(blocks):
    if not isinstance(blocks, list): return
    for b in blocks:
        if b.get('title') == "A Puzzle from the Past":
            b['title_gu'] = puzzle_title_gu
            b['body_gu'] = puzzle_body_gu
        elif b.get('title') == "Think About Division":
            b['title_gu'] = division_title_gu
            # For division body we should ideally let the translator handle or provide generic. We'll let script do body if it's there.
        # Recursively update if needed, but they are flat.

for key, val in data.items():
    if isinstance(val, dict) and 'blocks' in val:
        update_blocks(val['blocks'])

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Updated specific blocks in master_curriculum.json")
