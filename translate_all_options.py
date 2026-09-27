import json

translations = {
    "an integer": "એક પૂર્ણાંક",
    "a natural number": "એક પ્રાકૃતિક સંખ્યા",
    "an odd integer": "એક વિષમ પૂર્ણાંક",
    "an even integer": "એક સમ પૂર્ણાંક",
    "always irrational": "હંમેશા અતાર્કિક",
    "always rational": "હંમેશા પરિમેય",
    "rational or irrational": "પરિમેય અથવા અતાર્કિક",
    "one": "એક",
    "m": "m",
    "m + 1": "m + 1",
    "2m": "2m",
    "2m + 1": "2m + 1",
    "q": "q",
    "q + 1": "q + 1",
    "2q": "2q",
    "2q + 1": "2q + 1",
    "xy": "xy",
    "xy²": "xy²",
    "x³y³": "x³y³",
    "x²y²": "x²y²",
    "ab": "ab",
    "a²b²": "a²b²",
    "a³b²": "a³b²",
    "a³b³": "a³b³",
    "10": "10",
    "100": "100",
    "504": "504",
    "2520": "2520",
    "3": "3",
    "4": "4",
    "5": "5",
    "2": "2",
    "26": "26",
    "52": "52",
    "338": "338",
    "13": "13",
    "2 + √3": "2 + √3",
    "√2 - 3": "√2 - 3",
    "√9": "√9",
    "√11": "√11",
    "0": "0",
    "1": "1",
    "product of numbers": "સંખ્યાઓનો ગુણાકાર",
    "one decimal place": "એક દશાંશ સ્થાન",
    "two decimal places": "બે દશાંશ સ્થાન",
    "three decimal places": "ત્રણ દશાંશ સ્થાન",
    "four decimal places": "ચાર દશાંશ સ્થાન",
    "Because (a - 3b)/2b is an integer.": "કારણ કે (a - 3b)/2b પૂર્ણાંક છે.",
    "Because it implies √5 is rational, but we know √5 is irrational.": "કારણ કે આ સૂચવે છે કે √5 પરિમેય છે, પરંતુ આપણે જાણીએ છીએ કે √5 અતાર્કિક છે.",
    "Because 2b cannot be zero.": "કારણ કે 2b શૂન્ય હોઈ શકતું નથી.",
    "Because 3 is a prime number.": "કારણ કે 3 અવિભાજ્ય સંખ્યા છે.",
    "Multiply both sides by √2": "બંને બાજુ √2 વડે ગુણાકાર કરો",
    "Reverse the fractions to get √2/1 = b/a": "અપૂર્ણાંકને ઉલટાવી √2/1 = b/a મેળવો",
    "Square both sides directly to get 1/2 = a²/b²": "બંને બાજુનો સીધો વર્ગ કરી 1/2 = a²/b² મેળવો",
    "Add 1 to both sides": "બંને બાજુ 1 ઉમેરો",
    "5 = a/b": "5 = a/b",
    "5b² = a²": "5b² = a²",
    "25b² = a²": "25b² = a²",
    "b² = 5a²": "b² = 5a²"
}

def translate_options(en_options):
    gu_options = []
    for opt in en_options:
        opt_str = str(opt)
        if opt_str in translations:
            gu_options.append(translations[opt_str])
        else:
            gu_options.append(opt_str)
    return gu_options

def main():
    with open('app_core/chapters/ncert_class10_maths_ch1.json', 'r', encoding='utf-8') as f:
        data = json.load(f)
    
    blocks = data.get('blocks', [])
    for block in blocks:
        if block.get('type') == 'quiz':
            if 'options' in block:
                block['options_gu'] = translate_options(block['options'])

    with open('app_core/chapters/ncert_class10_maths_ch1.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

if __name__ == "__main__":
    main()
