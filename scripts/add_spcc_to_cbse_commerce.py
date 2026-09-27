import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/cbse_class11_commerce.json'

try:
    with open(file_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        
    spcc_subject = {
        'id': 'spcc',
        'name': 'SPCC (Secretarial Practice)',
        'icon': 'assignment',
        'color_hex': '0xFF795548',
        'chapters': [
            {
                'chapter_number': 1,
                'title': 'Part 1 Chapter 3: Physical Appearance of Business Letter',
                'module_id': 'gseb_class11_spcc_part1_ch3'
            },
            {
                'chapter_number': 2,
                'title': 'Part 1 Chapter 4: Layout of Business Letter',
                'module_id': 'gseb_class11_spcc_part1_ch4'
            },
            {
                'chapter_number': 3,
                'title': 'Part 1 Chapter 5: Inquiry Letters and their Replies',
                'module_id': 'gseb_class11_spcc_part1_ch5'
            },
            {
                'chapter_number': 4,
                'title': 'Part 2 Chapter 1: Meaning and Types of Secretary',
                'module_id': 'gseb_class11_spcc_part2_ch1'
            },
            {
                'chapter_number': 5,
                'title': 'Part 2 Chapter 3: Incorporation of a Company',
                'module_id': 'gseb_class11_spcc_part2_ch3'
            },
            {
                'chapter_number': 6,
                'title': 'Part 2 Chapter 4: Memorandum of Association',
                'module_id': 'gseb_class11_spcc_part2_ch4'
            }
        ]
    }

    found = False
    for subject in data.get('subjects', []):
        if subject.get('id') == 'spcc':
            found = True
            break

    if not found:
        data['subjects'].append(spcc_subject)
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        print('SPCC added to cbse_class11_commerce.json')
    else:
        print('SPCC already exists in cbse_class11_commerce.json')
except FileNotFoundError:
    print('cbse_class11_commerce.json not found.')
