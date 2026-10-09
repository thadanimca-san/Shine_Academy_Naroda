import json

with open('app_core/chapters/ncert_class10_maths_ch2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for block in data.get('blocks', []):
    block_id = block.get('id', '')
    
    # Fix Exercise 2.3 Question 1 options (Quotient and Remainder text)
    if 'EX2.3_Q1' in block_id:
        for lang, target in [('options_hi', 'भागफल'), ('options_gu', 'ભાગફળ')]:
            new_opts = []
            for opt in block[lang]:
                new_opt = opt.replace('Quotient', target)
                new_opt = new_opt.replace('Remainder', 'शेषफल' if lang == 'options_hi' else 'શેષ')
                new_opts.append(new_opt)
            block[lang] = new_opts

        # Also fix explanation translations to replace Quotient/Remainder
        block['explanation_hi'] = block['explanation_hi'].replace('Quotient', 'भागफल').replace('Remainder', 'शेषफल')
        block['explanation_gu'] = block['explanation_gu'].replace('Quotient', 'ભાગફળ').replace('Remainder', 'શેષ')
        
    # Fix Exercise 2.3 Question 2 options ("Yes, Remainder is 0" etc.)
    elif 'EX2.3_Q2' in block_id:
        for lang in ['options_hi', 'options_gu']:
            new_opts = []
            for opt in block[lang]:
                if opt == "Yes, Remainder is 0":
                    new_opts.append("हाँ, शेषफल 0 है" if lang == 'options_hi' else "હા, શેષ 0 છે")
                elif opt == "No, Remainder is 2":
                    new_opts.append("नहीं, शेषफल 2 है" if lang == 'options_hi' else "ના, શેષ 2 છે")
                else:
                    new_opts.append(opt)
            block[lang] = new_opts
            
        block['explanation_hi'] = block['explanation_hi'].replace('Yes, Remainder is 0', 'हाँ, शेषफल 0 है').replace('No, Remainder is 2', 'नहीं, शेषफल 2 है')
        block['explanation_gu'] = block['explanation_gu'].replace('Yes, Remainder is 0', 'હા, શેષ 0 છે').replace('No, Remainder is 2', 'ના, શેષ 2 છે')

with open('app_core/chapters/ncert_class10_maths_ch2.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("Fixed Chapter 2 English leak in Gujarati/Hindi options!")
