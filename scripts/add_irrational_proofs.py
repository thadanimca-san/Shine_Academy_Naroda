import json
import glob

# Detailed proofs for the Learn section
theory_blocks = [
    {
        "type": "theory",
        "content": "**Proof Type 1: Pure Irrational Numbers (√3, √5, √7)**\nLet's prove √3 is irrational.\n1. Assume √3 is rational, so √3 = a/b (a and b are co-prime).\n2. Squaring both sides: 3 = a²/b²  =>  3b² = a².\n3. This means a² is divisible by 3, so 'a' is divisible by 3 (Let a = 3c).\n4. Substitute a: 3b² = (3c)² = 9c²  =>  b² = 3c².\n5. This means b² is divisible by 3, so 'b' is divisible by 3.\n6. Contradiction! Both a and b are divisible by 3, but we assumed they were co-prime. Hence, √3 is irrational.\n*(The exact same steps apply to √5 and √7!)*",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    },
    {
        "type": "theory",
        "content": "**Proof Type 2: Rational ± Irrational (5 - √3, 6 + √2)**\nLet's prove 5 - √3 is irrational.\n1. Assume 5 - √3 is rational, say p/q (where p,q are integers, q≠0).\n2. Rearrange the equation: √3 = 5 - p/q.\n3. √3 = (5q - p) / q.\n4. Since p and q are integers, (5q - p)/q is a rational number.\n5. This means √3 is rational. But we already know √3 is irrational!\n6. Contradiction! Therefore, 5 - √3 must be irrational.\n*(Same logic for 6 + √2. Just isolate the root!)*",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    },
    {
        "type": "theory",
        "content": "**Proof Type 3: Rational × Irrational (3√2, 7√5)**\nLet's prove 3√2 is irrational.\n1. Assume 3√2 is rational, say a/b (a,b integers, b≠0).\n2. Rearrange to isolate the root: √2 = a / (3b).\n3. Since a, 3, and b are integers, a/(3b) is a rational number.\n4. This implies √2 is rational, which is false (we know it's irrational).\n5. Contradiction! Therefore, 3√2 is irrational.\n*(Apply this exact method for 7√5)*",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    },
    {
        "type": "theory",
        "content": "**Proof Type 4: Mixed Operations (3 + 2√5)**\nLet's prove 3 + 2√5 is irrational.\n1. Assume it is rational: 3 + 2√5 = a/b.\n2. Rearrange: 2√5 = (a/b) - 3 = (a - 3b)/b.\n3. Isolate the root: √5 = (a - 3b) / 2b.\n4. Since a and b are integers, the right side is rational.\n5. This means √5 is rational. Contradiction!\n6. Therefore, 3 + 2√5 is irrational.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    },
    {
        "type": "theory",
        "content": "**Proof Type 5: Fractions (1/√2)**\nLet's prove 1/√2 is irrational.\n1. Assume 1/√2 is rational, say a/b.\n2. Reverse the fraction: √2/1 = b/a.\n3. Since a and b are integers, b/a is a rational number.\n4. This means √2 is rational. Contradiction!\n5. Therefore, 1/√2 is irrational.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    },
    {
        "type": "theory",
        "content": "**Proof Type 6: Irrational + Irrational (2√5 + √3)**\nLet's prove 2√5 + √3 is irrational.\n1. Assume it's rational: 2√5 + √3 = a/b.\n2. Move one root: 2√5 = a/b - √3.\n3. Square both sides: 20 = (a²/b²) - (2a√3)/b + 3.\n4. Rearrange to isolate √3: (2a√3)/b = (a²/b²) - 17.\n5. √3 = [(a² - 17b²) / b²] × [b / 2a] = (a² - 17b²) / 2ab.\n6. The right side is rational, so √3 is rational. Contradiction!\n7. Therefore, 2√5 + √3 is irrational.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    }
]

# Provide Hindi translations for the blocks
theory_blocks[0]['content_hi'] = "**प्रमाण प्रकार 1: शुद्ध अपरिमेय संख्याएँ (√3, √5, √7)**\nआइए सिद्ध करें कि √3 अपरिमेय है।\n1. मान लीजिए √3 एक परिमेय संख्या है, इसलिए √3 = a/b (a और b सह-अभाज्य हैं)।\n2. दोनों पक्षों का वर्ग करने पर: 3 = a²/b² => 3b² = a²।\n3. इसका अर्थ है a², 3 से विभाज्य है, इसलिए 'a' भी 3 से विभाज्य है (मान लें a = 3c)।\n4. a का मान रखने पर: 3b² = (3c)² = 9c² => b² = 3c²।\n5. इसका अर्थ है b², 3 से विभाज्य है, इसलिए 'b' भी 3 से विभाज्य है।\n6. विरोधाभास! a और b दोनों 3 से विभाज्य हैं, लेकिन हमने माना था कि वे सह-अभाज्य हैं। अतः, √3 अपरिमेय है।"

theory_blocks[1]['content_hi'] = "**प्रमाण प्रकार 2: परिमेय ± अपरिमेय (5 - √3, 6 + √2)**\nआइए सिद्ध करें कि 5 - √3 अपरिमेय है।\n1. मान लीजिए 5 - √3 परिमेय है, जैसे p/q।\n2. समीकरण को पुनर्व्यवस्थित करें: √3 = 5 - p/q।\n3. √3 = (5q - p) / q।\n4. चूँकि p और q पूर्णांक हैं, दाईं ओर परिमेय संख्या है।\n5. इसका अर्थ है √3 परिमेय है। विरोधाभास!\n6. अतः, 5 - √3 अपरिमेय है।"

theory_blocks[2]['content_hi'] = "**प्रमाण प्रकार 3: परिमेय × अपरिमेय (3√2, 7√5)**\nआइए सिद्ध करें कि 3√2 अपरिमेय है।\n1. मान लीजिए 3√2 परिमेय है, जैसे a/b।\n2. मूल को अलग करने के लिए पुनर्व्यवस्थित करें: √2 = a / (3b)।\n3. चूँकि a, 3, और b पूर्णांक हैं, a/(3b) एक परिमेय संख्या है।\n4. इसका अर्थ है √2 परिमेय है। विरोधाभास!\n5. अतः, 3√2 अपरिमेय है।"

theory_blocks[3]['content_hi'] = "**प्रमाण प्रकार 4: मिश्रित संक्रियाएँ (3 + 2√5)**\nआइए सिद्ध करें कि 3 + 2√5 अपरिमेय है।\n1. मान लीजिए यह परिमेय है: 3 + 2√5 = a/b।\n2. पुनर्व्यवस्थित करें: 2√5 = (a/b) - 3 = (a - 3b)/b।\n3. मूल को अलग करें: √5 = (a - 3b) / 2b।\n4. दाईं ओर परिमेय है, अतः √5 परिमेय है। विरोधाभास!\n5. इसलिए, 3 + 2√5 अपरिमेय है।"

theory_blocks[4]['content_hi'] = "**प्रमाण प्रकार 5: भिन्न (1/√2)**\nआइए सिद्ध करें कि 1/√2 अपरिमेय है।\n1. मान लीजिए 1/√2 परिमेय है, जैसे a/b।\n2. भिन्न को उल्टा करें: √2/1 = b/a।\n3. चूँकि a और b पूर्णांक हैं, b/a एक परिमेय संख्या है।\n4. इसका अर्थ है √2 परिमेय है। विरोधाभास!\n5. अतः, 1/√2 अपरिमेय है।"

theory_blocks[5]['content_hi'] = "**प्रमाण प्रकार 6: अपरिमेय + अपरिमेय (2√5 + √3)**\nआइए सिद्ध करें कि 2√5 + √3 अपरिमेय है।\n1. मान लीजिए यह परिमेय है: 2√5 + √3 = a/b।\n2. एक मूल को स्थानांतरित करें: 2√5 = a/b - √3।\n3. दोनों पक्षों का वर्ग करें: 20 = (a²/b²) - (2a√3)/b + 3।\n4. √3 को अलग करने के लिए पुनर्व्यवस्थित करें: (2a√3)/b = (a²/b²) - 17।\n5. √3 = (a² - 17b²) / 2ab।\n6. दाईं ओर परिमेय है, इसलिए √3 परिमेय है। विरोधाभास!\n7. अतः, 2√5 + √3 अपरिमेय है।"


# Quiz questions to test these specific proofs
quiz_blocks = [
    {
        "id": "KOBJ_CH1_Q6",
        "type": "quiz",
        "question": "When proving that √5 is irrational by contradiction, if we assume √5 = a/b, what does the equation become after squaring both sides?",
        "question_hi": "विरोधाभास द्वारा √5 को अपरिमेय सिद्ध करते समय, यदि हम मान लें कि √5 = a/b, तो दोनों पक्षों का वर्ग करने के बाद समीकरण क्या हो जाता है?",
        "options": [
            "5 = a/b",
            "5b² = a²",
            "25b² = a²",
            "b² = 5a²"
        ],
        "options_hi": [
            "5 = a/b",
            "5b² = a²",
            "25b² = a²",
            "b² = 5a²"
        ],
        "correct_index": 1,
        "explanation": "Squaring √5 = a/b gives 5 = a²/b², which rearranges to 5b² = a².",
        "explanation_hi": "√5 = a/b का वर्ग करने पर 5 = a²/b² प्राप्त होता है, जिसे पुनर्व्यवस्थित करने पर 5b² = a² प्राप्त होता है।"
    },
    {
        "id": "KOBJ_CH1_Q7",
        "type": "quiz",
        "question": "In the proof of 3 + 2√5 being irrational, we isolate √5 to get √5 = (a - 3b)/2b. Why does this create a contradiction?",
        "question_hi": "3 + 2√5 को अपरिमेय सिद्ध करने में, हम √5 = (a - 3b)/2b प्राप्त करने के लिए √5 को अलग करते हैं। यह विरोधाभास क्यों पैदा करता है?",
        "options": [
            "Because (a - 3b)/2b is an integer.",
            "Because it implies √5 is rational, but we know √5 is irrational.",
            "Because 2b cannot be zero.",
            "Because 3 is a prime number."
        ],
        "options_hi": [
            "क्योंकि (a - 3b)/2b एक पूर्णांक है।",
            "क्योंकि इसका अर्थ है कि √5 परिमेय है, लेकिन हम जानते हैं कि √5 अपरिमेय है।",
            "क्योंकि 2b शून्य नहीं हो सकता।",
            "क्योंकि 3 एक अभाज्य संख्या है।"
        ],
        "correct_index": 1,
        "explanation": "Since a and b are integers, the expression (a - 3b)/2b represents a rational number. If it equals √5, it wrongly implies √5 is rational.",
        "explanation_hi": "चूँकि a और b पूर्णांक हैं, व्यंजक (a - 3b)/2b एक परिमेय संख्या का प्रतिनिधित्व करता है। यदि यह √5 के बराबर है, तो यह गलत रूप से दर्शाता है कि √5 परिमेय है।"
    },
    {
        "id": "KOBJ_CH1_Q8",
        "type": "quiz",
        "question": "If you are asked to prove 1/√2 is irrational, what is the best first step after assuming 1/√2 = a/b?",
        "question_hi": "यदि आपको यह सिद्ध करने के लिए कहा जाए कि 1/√2 अपरिमेय है, तो 1/√2 = a/b मानने के बाद सबसे अच्छा पहला कदम क्या है?",
        "options": [
            "Multiply both sides by √2",
            "Reverse the fractions to get √2/1 = b/a",
            "Square both sides directly to get 1/2 = a²/b²",
            "Add 1 to both sides"
        ],
        "options_hi": [
            "दोनों पक्षों को √2 से गुणा करें",
            "√2/1 = b/a प्राप्त करने के लिए भिन्नों को उल्टा करें",
            "सीधे दोनों पक्षों का वर्ग करके 1/2 = a²/b² प्राप्त करें",
            "दोनों पक्षों में 1 जोड़ें"
        ],
        "correct_index": 1,
        "explanation": "The easiest method is to take the reciprocal of both sides, giving √2 = b/a. Since b/a is rational, it contradicts that √2 is irrational.",
        "explanation_hi": "सबसे आसान तरीका दोनों पक्षों का व्युत्क्रम (reciprocal) लेना है, जिससे √2 = b/a प्राप्त होता है। चूँकि b/a परिमेय है, यह इस तथ्य का खंडन करता है कि √2 अपरिमेय है।"
    }
]

def update_chapter(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if 'blocks' not in data: return
        blocks = data['blocks']
        
        # Check if already added to avoid duplication
        if any('Proof Type 1' in b.get('content', '') for b in blocks):
            print(f"Proofs already exist in {file_path}")
            return
            
        # Find index of Irrational numbers theory block to inject proofs after it
        inject_idx = -1
        for i, b in enumerate(blocks):
            if b.get('type') == 'theory' and 'Irrational Numbers' in b.get('content', ''):
                inject_idx = i
                break
                
        if inject_idx != -1:
            # Insert theory blocks right after the definition of Irrational Numbers
            blocks[inject_idx+1:inject_idx+1] = theory_blocks
            print(f"Added {len(theory_blocks)} proof theory blocks to {file_path}")
        else:
            blocks.extend(theory_blocks)
            
        # Append the new practice questions at the end
        blocks.extend(quiz_blocks)
        print(f"Added {len(quiz_blocks)} proof practice quizzes to {file_path}")
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(f"Error on {file_path}: {e}")

for f in glob.glob('app_core/chapters/*class10_maths_ch1.json'):
    update_chapter(f)
