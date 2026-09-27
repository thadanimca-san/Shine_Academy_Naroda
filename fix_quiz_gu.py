import json

def translate_options(en_options):
    gu_options = []
    for opt in en_options:
        opt = str(opt)
        if opt == "product of numbers":
            gu_options.append("સંખ્યાઓનો ગુણાકાર")
        elif opt == "one decimal place":
            gu_options.append("એક દશાંશ સ્થાન")
        elif opt == "two decimal places":
            gu_options.append("બે દશાંશ સ્થાન")
        elif opt == "three decimal places":
            gu_options.append("ત્રણ દશાંશ સ્થાન")
        elif opt == "four decimal places":
            gu_options.append("ચાર દશાંશ સ્થાન")
        elif opt == "Because (a - 3b)/2b is an integer.":
            gu_options.append("કારણ કે (a - 3b)/2b પૂર્ણાંક છે.")
        elif opt == "Because it implies √5 is rational, but we know √5 is irrational.":
            gu_options.append("કારણ કે આ સૂચવે છે કે √5 તર્કસંગત છે, પરંતુ આપણે જાણીએ છીએ કે √5 અતાર્કિક છે.")
        elif opt == "Because 2b cannot be zero.":
            gu_options.append("કારણ કે 2b શૂન્ય હોઈ શકતું નથી.")
        elif opt == "Because 3 is a prime number.":
            gu_options.append("કારણ કે 3 અવિભાજ્ય સંખ્યા છે.")
        elif opt == "Multiply both sides by √2":
            gu_options.append("બંને બાજુ √2 વડે ગુણાકાર કરો")
        elif opt == "Reverse the fractions to get √2/1 = b/a":
            gu_options.append("અપૂર્ણાંકને ઉલટાવી √2/1 = b/a મેળવો")
        elif opt == "Square both sides directly to get 1/2 = a²/b²":
            gu_options.append("બંને બાજુનો સીધો વર્ગ કરી 1/2 = a²/b² મેળવો")
        elif opt == "Add 1 to both sides":
            gu_options.append("બંને બાજુ 1 ઉમેરો")
        else:
            gu_options.append(opt)
    return gu_options

def main():
    with open('app_core/chapters/ncert_class10_maths_ch1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    blocks = data.get('blocks', [])
    for block in blocks:
        if block.get('type') == 'quiz':
            if 'options' in block:
                block['options_gu'] = translate_options(block['options'])
            if 'explanation' in block and 'explanation_gu' not in block:
                # Add a dummy translation for explanation if we can't easily translate it, or just use English as a fallback for now.
                # Since the user specifically complained about options, this is the main issue.
                # Actually, I'll just use the Hindi one prefixed with (Gu) or just English, but wait, I can use a generic "Explanation in Gujarati" placeholder or just skip it if not requested, but let's copy the English one for now if no Gu is present.
                # Wait, I'll just leave explanation_gu out or set it to English, since options were the immediate bug breaking the UI.
                block['explanation_gu'] = block.get('explanation')

    with open('app_core/chapters/ncert_class10_maths_ch1.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
