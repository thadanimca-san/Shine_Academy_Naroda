import json
import glob
import uuid

def generate_id():
    return f"KOBJ_AUTO_{str(uuid.uuid4())[:8].upper()}"

questions = [
    {
        "q": "Prove that √3 is irrational.",
        "q_hi": "सिद्ध कीजिए कि √3 एक अपरिमेय संख्या है।",
        "steps": "1. Let us assume, to the contrary, that √3 is rational.\n2. Then, there exist co-prime integers 'a' and 'b' (b ≠ 0) such that √3 = a/b.\n3. Squaring both sides, we get: 3 = a²/b²  =>  3b² = a².\n4. This means a² is divisible by 3. Therefore, 'a' is also divisible by 3. (Let a = 3c for some integer c).\n5. Substitute a = 3c into the equation: 3b² = (3c)²  =>  3b² = 9c²  =>  b² = 3c².\n6. This means b² is divisible by 3, so 'b' is also divisible by 3.\n7. Since both 'a' and 'b' are divisible by 3, they are not co-prime. This contradicts our initial assumption.\n8. Hence, our assumption was wrong, and √3 is irrational.",
        "steps_hi": "1. मान लीजिए, इसके विपरीत, कि √3 एक परिमेय संख्या है।\n2. तब, सह-अभाज्य पूर्णांक 'a' और 'b' (b ≠ 0) मौजूद हैं ताकि √3 = a/b हो।\n3. दोनों पक्षों का वर्ग करने पर, हमें मिलता है: 3 = a²/b² => 3b² = a²।\n4. इसका अर्थ है कि a², 3 से विभाज्य है। इसलिए, 'a' भी 3 से विभाज्य है। (मान लें कि किसी पूर्णांक c के लिए a = 3c है)।\n5. समीकरण में a = 3c प्रतिस्थापित करें: 3b² = (3c)² => 3b² = 9c² => b² = 3c²।\n6. इसका अर्थ है कि b², 3 से विभाज्य है, इसलिए 'b' भी 3 से विभाज्य है।\n7. चूँकि 'a' और 'b' दोनों 3 से विभाज्य हैं, वे सह-अभाज्य नहीं हैं। यह हमारी प्रारंभिक मान्यता का खंडन करता है।\n8. अतः, हमारी मान्यता गलत थी, और √3 अपरिमेय है।"
    },
    {
        "q": "Prove that 5 - √3 is irrational.",
        "q_hi": "सिद्ध कीजिए कि 5 - √3 एक अपरिमेय संख्या है।",
        "steps": "1. Let us assume that 5 - √3 is a rational number.\n2. So, we can find co-prime integers a and b (b ≠ 0) such that 5 - √3 = a/b.\n3. Rearranging this equation to isolate √3, we get: √3 = 5 - a/b.\n4. Therefore, √3 = (5b - a) / b.\n5. Since 'a' and 'b' are integers, (5b - a)/b is a rational number.\n6. This implies that √3 is rational.\n7. However, this contradicts the fact that √3 is an irrational number.\n8. This contradiction has arisen because of our incorrect assumption. Therefore, 5 - √3 is irrational.",
        "steps_hi": "1. मान लीजिए कि 5 - √3 एक परिमेय संख्या है।\n2. इसलिए, हम सह-अभाज्य पूर्णांक a और b (b ≠ 0) पा सकते हैं ताकि 5 - √3 = a/b हो।\n3. √3 को अलग करने के लिए इस समीकरण को पुनर्व्यवस्थित करने पर, हमें मिलता है: √3 = 5 - a/b।\n4. इसलिए, √3 = (5b - a) / b।\n5. चूँकि 'a' और 'b' पूर्णांक हैं, (5b - a)/b एक परिमेय संख्या है।\n6. इसका तात्पर्य यह है कि √3 परिमेय है।\n7. हालाँकि, यह इस तथ्य का खंडन करता है कि √3 एक अपरिमेय संख्या है।\n8. यह विरोधाभास हमारी गलत मान्यता के कारण उत्पन्न हुआ है। इसलिए, 5 - √3 अपरिमेय है।"
    },
    {
        "q": "Prove that 3√2 is irrational.",
        "q_hi": "सिद्ध कीजिए कि 3√2 एक अपरिमेय संख्या है।",
        "steps": "1. Let us assume that 3√2 is rational.\n2. Then we can express it in the form a/b, where a and b are co-prime integers (b ≠ 0).\n3. So, 3√2 = a/b.\n4. Rearranging to isolate the square root, we get: √2 = a / (3b).\n5. Since 3, a, and b are integers, a/(3b) is a rational number.\n6. This implies that √2 is a rational number.\n7. But this contradicts the universal fact that √2 is irrational.\n8. Hence, our assumption is false, and 3√2 is irrational.",
        "steps_hi": "1. मान लीजिए कि 3√2 परिमेय है।\n2. तब हम इसे a/b के रूप में व्यक्त कर सकते हैं, जहाँ a और b सह-अभाज्य पूर्णांक हैं (b ≠ 0)।\n3. इसलिए, 3√2 = a/b।\n4. वर्गमूल को अलग करने के लिए पुनर्व्यवस्थित करने पर, हमें मिलता है: √2 = a / (3b)।\n5. चूँकि 3, a, और b पूर्णांक हैं, a/(3b) एक परिमेय संख्या है।\n6. इसका तात्पर्य यह है कि √2 एक परिमेय संख्या है।\n7. लेकिन यह इस सार्वभौमिक तथ्य का खंडन करता है कि √2 अपरिमेय है।\n8. अतः, हमारी मान्यता गलत है, और 3√2 अपरिमेय है।"
    },
    {
        "q": "Prove that √5 is irrational.",
        "q_hi": "सिद्ध कीजिए कि √5 एक अपरिमेय संख्या है।",
        "steps": "1. Let us assume, to the contrary, that √5 is rational.\n2. Then √5 = p/q, where p and q are co-prime integers and q ≠ 0.\n3. Squaring both sides: 5 = p²/q² => p² = 5q².\n4. This shows p² is divisible by 5, meaning 'p' is also divisible by 5. Let p = 5m.\n5. Substitute p: (5m)² = 5q² => 25m² = 5q² => q² = 5m².\n6. This shows q² is divisible by 5, meaning 'q' is also divisible by 5.\n7. Since both p and q are divisible by 5, they are not co-prime. Contradiction!\n8. Therefore, √5 is an irrational number.",
        "steps_hi": "1. मान लीजिए, इसके विपरीत, कि √5 परिमेय है।\n2. तब √5 = p/q, जहाँ p और q सह-अभाज्य पूर्णांक हैं और q ≠ 0।\n3. दोनों पक्षों का वर्ग करने पर: 5 = p²/q² => p² = 5q²।\n4. यह दर्शाता है कि p², 5 से विभाज्य है, जिसका अर्थ है 'p' भी 5 से विभाज्य है। माना p = 5m।\n5. p प्रतिस्थापित करें: (5m)² = 5q² => 25m² = 5q² => q² = 5m²।\n6. यह दर्शाता है कि q², 5 से विभाज्य है, जिसका अर्थ है 'q' भी 5 से विभाज्य है।\n7. चूँकि p और q दोनों 5 से विभाज्य हैं, वे सह-अभाज्य नहीं हैं। विरोधाभास!\n8. इसलिए, √5 एक अपरिमेय संख्या है।"
    },
    {
        "q": "Prove that 3 + 2√5 is irrational.",
        "q_hi": "सिद्ध कीजिए कि 3 + 2√5 एक अपरिमेय संख्या है।",
        "steps": "1. Let us assume that 3 + 2√5 is rational.\n2. Therefore, 3 + 2√5 = a/b (where a and b are co-prime integers, b ≠ 0).\n3. Rearranging the terms, we get: 2√5 = (a/b) - 3 = (a - 3b)/b.\n4. Further isolating √5, we get: √5 = (a - 3b) / (2b).\n5. Since a and b are integers, (a - 3b)/(2b) is a rational number.\n6. This implies that √5 is rational.\n7. However, this contradicts the fact that √5 is irrational.\n8. Therefore, our assumption was incorrect. 3 + 2√5 is irrational.",
        "steps_hi": "1. मान लीजिए कि 3 + 2√5 परिमेय है।\n2. इसलिए, 3 + 2√5 = a/b (जहाँ a और b सह-अभाज्य पूर्णांक हैं, b ≠ 0)।\n3. पदों को पुनर्व्यवस्थित करने पर, हमें मिलता है: 2√5 = (a/b) - 3 = (a - 3b)/b।\n4. √5 को और अलग करने पर, हमें मिलता है: √5 = (a - 3b) / (2b)।\n5. चूँकि a और b पूर्णांक हैं, (a - 3b)/(2b) एक परिमेय संख्या है।\n6. इसका तात्पर्य यह है कि √5 परिमेय है।\n7. हालाँकि, यह इस तथ्य का खंडन करता है कि √5 अपरिमेय है।\n8. इसलिए, हमारी मान्यता गलत थी। 3 + 2√5 अपरिमेय है।"
    },
    {
        "q": "Prove that 1/√2 is irrational.",
        "q_hi": "सिद्ध कीजिए कि 1/√2 एक अपरिमेय संख्या है।",
        "steps": "1. Let us assume that 1/√2 is a rational number.\n2. So, 1/√2 = a/b, where a and b are co-prime integers (a, b ≠ 0).\n3. Reversing the fractions (taking reciprocals) on both sides: √2/1 = b/a.\n4. Therefore, √2 = b/a.\n5. Since a and b are integers, b/a is a rational number.\n6. This implies that √2 is rational.\n7. But we know this contradicts the fact that √2 is irrational.\n8. Hence, 1/√2 must be irrational.",
        "steps_hi": "1. मान लीजिए कि 1/√2 एक परिमेय संख्या है।\n2. इसलिए, 1/√2 = a/b, जहाँ a और b सह-अभाज्य पूर्णांक हैं (a, b ≠ 0)।\n3. दोनों पक्षों पर भिन्नों को उलटने (व्युत्क्रम लेने) पर: √2/1 = b/a।\n4. इसलिए, √2 = b/a।\n5. चूँकि a और b पूर्णांक हैं, b/a एक परिमेय संख्या है।\n6. इसका तात्पर्य यह है कि √2 परिमेय है।\n7. लेकिन हम जानते हैं कि यह इस तथ्य का खंडन करता है कि √2 अपरिमेय है।\n8. अतः, 1/√2 अपरिमेय होना चाहिए।"
    },
    {
        "q": "Prove that 7√5 is irrational.",
        "q_hi": "सिद्ध कीजिए कि 7√5 एक अपरिमेय संख्या है।",
        "steps": "1. Let us assume that 7√5 is rational.\n2. Then 7√5 = a/b (where a and b are co-prime integers, b ≠ 0).\n3. Rearranging to isolate the root: √5 = a / (7b).\n4. Since a, 7, and b are integers, the fraction a/(7b) is rational.\n5. This implies √5 is a rational number.\n6. This contradicts the established fact that √5 is irrational.\n7. Our assumption was incorrect. Therefore, 7√5 is irrational.",
        "steps_hi": "1. मान लीजिए कि 7√5 परिमेय है।\n2. तब 7√5 = a/b (जहाँ a और b सह-अभाज्य पूर्णांक हैं, b ≠ 0)।\n3. मूल को अलग करने के लिए पुनर्व्यवस्थित करें: √5 = a / (7b)।\n4. चूँकि a, 7, और b पूर्णांक हैं, भिन्न a/(7b) परिमेय है।\n5. इसका तात्पर्य है कि √5 एक परिमेय संख्या है।\n6. यह स्थापित तथ्य का खंडन करता है कि √5 अपरिमेय है।\n7. हमारी मान्यता गलत थी। इसलिए, 7√5 अपरिमेय है।"
    },
    {
        "q": "Prove that 6 + √2 is irrational.",
        "q_hi": "सिद्ध कीजिए कि 6 + √2 एक अपरिमेय संख्या है।",
        "steps": "1. Let us assume that 6 + √2 is rational.\n2. So, 6 + √2 = p/q (where p, q are integers and q ≠ 0).\n3. Rearranging the equation: √2 = p/q - 6.\n4. Taking the LCM: √2 = (p - 6q) / q.\n5. Since p and q are integers, (p - 6q)/q represents a rational number.\n6. This implies that √2 is rational.\n7. This contradicts the fact that √2 is irrational.\n8. Therefore, 6 + √2 is irrational.",
        "steps_hi": "1. मान लीजिए कि 6 + √2 परिमेय है।\n2. इसलिए, 6 + √2 = p/q (जहाँ p, q पूर्णांक हैं और q ≠ 0)।\n3. समीकरण को पुनर्व्यवस्थित करें: √2 = p/q - 6।\n4. LCM लेने पर: √2 = (p - 6q) / q।\n5. चूँकि p और q पूर्णांक हैं, (p - 6q)/q एक परिमेय संख्या को दर्शाता है।\n6. इसका तात्पर्य है कि √2 परिमेय है।\n7. यह इस तथ्य का खंडन करता है कि √2 अपरिमेय है।\n8. इसलिए, 6 + √2 अपरिमेय है।"
    },
    {
        "q": "Prove that √7 is irrational.",
        "q_hi": "सिद्ध कीजिए कि √7 एक अपरिमेय संख्या है।",
        "steps": "1. Let us assume, to the contrary, that √7 is rational.\n2. Then √7 = a/b, where a and b are co-prime integers (b ≠ 0).\n3. Squaring both sides: 7 = a²/b² => a² = 7b².\n4. This implies a² is divisible by 7, so 'a' is also divisible by 7. (Let a = 7c).\n5. Substitute a = 7c: (7c)² = 7b² => 49c² = 7b² => b² = 7c².\n6. This implies b² is divisible by 7, so 'b' is also divisible by 7.\n7. Since a and b are both divisible by 7, they are not co-prime. Contradiction!\n8. Therefore, √7 is an irrational number.",
        "steps_hi": "1. मान लीजिए, इसके विपरीत, कि √7 परिमेय है।\n2. तब √7 = a/b, जहाँ a और b सह-अभाज्य पूर्णांक हैं (b ≠ 0)।\n3. दोनों पक्षों का वर्ग करने पर: 7 = a²/b² => a² = 7b²।\n4. इसका तात्पर्य है कि a², 7 से विभाज्य है, इसलिए 'a' भी 7 से विभाज्य है। (मान लें a = 7c)।\n5. a = 7c प्रतिस्थापित करें: (7c)² = 7b² => 49c² = 7b² => b² = 7c²।\n6. इसका तात्पर्य है कि b², 7 से विभाज्य है, इसलिए 'b' भी 7 से विभाज्य है।\n7. चूँकि a और b दोनों 7 से विभाज्य हैं, वे सह-अभाज्य नहीं हैं। विरोधाभास!\n8. इसलिए, √7 एक अपरिमेय संख्या है।"
    },
    {
        "q": "Prove that 2√5 + √3 is irrational.",
        "q_hi": "सिद्ध कीजिए कि 2√5 + √3 एक अपरिमेय संख्या है।",
        "steps": "1. Let us assume that 2√5 + √3 is rational, say 'x'. So, 2√5 + √3 = x.\n2. Rearrange to isolate one root: 2√5 = x - √3.\n3. Square both sides: (2√5)² = (x - √3)².\n4. 20 = x² - 2x√3 + 3.\n5. Rearrange to isolate √3: 2x√3 = x² + 3 - 20 = x² - 17.\n6. √3 = (x² - 17) / 2x.\n7. Since x is assumed to be rational, (x² - 17) / 2x is a rational number.\n8. This implies √3 is rational, which contradicts the fact that √3 is irrational.\n9. Therefore, our assumption was false, and 2√5 + √3 is irrational.",
        "steps_hi": "1. मान लीजिए कि 2√5 + √3 परिमेय है, जैसे 'x'। इसलिए, 2√5 + √3 = x।\n2. एक मूल को अलग करने के लिए पुनर्व्यवस्थित करें: 2√5 = x - √3।\n3. दोनों पक्षों का वर्ग करें: (2√5)² = (x - √3)²।\n4. 20 = x² - 2x√3 + 3।\n5. √3 को अलग करने के लिए पुनर्व्यवस्थित करें: 2x√3 = x² + 3 - 20 = x² - 17।\n6. √3 = (x² - 17) / 2x।\n7. चूँकि x को परिमेय माना गया है, (x² - 17) / 2x एक परिमेय संख्या है।\n8. इसका तात्पर्य है कि √3 परिमेय है, जो इस तथ्य का खंडन करता है कि √3 अपरिमेय है।\n9. इसलिए, हमारी मान्यता गलत थी, और 2√5 + √3 अपरिमेय है।"
    }
]

def update_chapter(file_path):
    # Skip the non-standard file structure
    if "real_numbers" in file_path:
        return
        
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        blocks = data.get('blocks', [])
        
        # Remove old proof type blocks
        new_blocks = []
        for b in blocks:
            content = b.get('content', '')
            if isinstance(content, str) and 'Proof Type' in content:
                continue # Skip this block
            new_blocks.append(b)
            
        # Find where to inject
        inject_idx = -1
        for i, b in enumerate(new_blocks):
            content = b.get('content', '')
            if isinstance(content, str) and 'Irrational Numbers' in content:
                inject_idx = i
                break
                
        theory_blocks = []
        for i, q in enumerate(questions):
            block = {
                "type": "theory",
                "title": f"Practice Question {i+1}",
                "title_hi": f"अभ्यास प्रश्न {i+1}",
                "body": f"**Q: {q['q']}**\n\n**Detailed Solution:**\n{q['steps']}",
                "body_hi": f"**प्रश्न: {q['q_hi']}**\n\n**विस्तृत समाधान:**\n{q['steps_hi']}",
                "difficulty": "Advanced",
                "bloom": "Analyze",
                "id": generate_id()
            }
            theory_blocks.append(block)
            
        if inject_idx != -1:
            new_blocks[inject_idx+1:inject_idx+1] = theory_blocks
        else:
            new_blocks.extend(theory_blocks)
            
        data['blocks'] = new_blocks
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
        print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error {file_path}: {e}")

for f in glob.glob('app_core/chapters/*class10_maths_ch1.json'):
    update_chapter(f)
