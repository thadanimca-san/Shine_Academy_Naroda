import json

def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def upgrade_class1_hindi():
    print("Generating Gold Standard Class 1 Hindi...")
    
    # 1. Varnamala (Swar)
    ch1 = load_json("app_core/chapters/class1_hindi_ch1.json")
    if ch1:
        ch1["blocks"] = [
            {"id": "KOBJ_C1_HIN_1_01", "type": "hook", "title": "Hindi Swar", "body": "Just like English has vowels, Hindi has Swar! They are the soul of Hindi words."},
            {"id": "KOBJ_C1_HIN_1_02", "type": "quiz", "question": "What is the first Swar in Hindi?", "options": ["इ", "अ", "क"], "correct_index": 1, "explanation": "The very first letter is अ (a)."},
            {"id": "KOBJ_C1_HIN_1_03", "type": "trace_alphabet", "letter": "अ"},
            {"id": "KOBJ_C1_HIN_1_04", "type": "flashcard", "front": "अ से...", "back": "अनार (Pomegranate)", "color": "0xFFE91E63"},
            {"id": "KOBJ_C1_HIN_1_05", "type": "trace_alphabet", "letter": "आ"},
            {"id": "KOBJ_C1_HIN_1_06", "type": "flashcard", "front": "आ से...", "back": "आम (Mango)", "color": "0xFFFFC107"},
            {"id": "KOBJ_C1_HIN_1_07", "type": "teacher_tip", "title": "Sing it!", "body": "अ आ इ ई उ ऊ ऋ ए ऐ ओ औ अं अः - Sing them like a song!"},
            {"id": "KOBJ_C1_HIN_1_08", "type": "quiz", "question": "Which letter comes after अ?", "options": ["इ", "आ", "उ"], "correct_index": 1, "explanation": "It is आ (aa)!"}
        ]
        save_json("app_core/chapters/class1_hindi_ch1.json", ch1)

    # 2. Varnamala (Vyanjan)
    ch2 = load_json("app_core/chapters/class1_hindi_ch2.json")
    if ch2:
        ch2["blocks"] = [
            {"id": "KOBJ_C1_HIN_2_01", "type": "hook", "title": "The Consonants of Hindi", "body": "Now that we know Swar, let's learn Vyanjan! There are 33 main consonants."},
            {"id": "KOBJ_C1_HIN_2_02", "type": "quiz", "question": "What is the first Vyanjan?", "options": ["च", "त", "क"], "correct_index": 2, "explanation": "The first letter is क (Ka)."},
            {"id": "KOBJ_C1_HIN_2_03", "type": "trace_alphabet", "letter": "क"},
            {"id": "KOBJ_C1_HIN_2_04", "type": "flashcard", "front": "क से...", "back": "कबूतर (Pigeon)", "color": "0xFF2196F3"},
            {"id": "KOBJ_C1_HIN_2_05", "type": "trace_alphabet", "letter": "ख"},
            {"id": "KOBJ_C1_HIN_2_06", "type": "flashcard", "front": "ख से...", "back": "खरगोश (Rabbit)", "color": "0xFF4CAF50"},
            {"id": "KOBJ_C1_HIN_2_07", "type": "teacher_tip", "title": "Groups of 5", "body": "Vyanjan are learned in groups of 5! (क, ख, ग, घ, ङ)."},
            {"id": "KOBJ_C1_HIN_2_08", "type": "quiz", "question": "Which animal starts with ख?", "options": ["खरगोश (Rabbit)", "कबूतर (Pigeon)"], "correct_index": 0, "explanation": "ख से खरगोश!"}
        ]
        save_json("app_core/chapters/class1_hindi_ch2.json", ch2)

    # 3. Bina Matra Wale Shabd
    ch3 = load_json("app_core/chapters/class1_hindi_ch3.json")
    if ch3:
        ch3["blocks"] = [
            {"id": "KOBJ_C1_HIN_3_01", "type": "hook", "title": "Building Words!", "body": "We don't need any special marks (matras) to make our first Hindi words!"},
            {"id": "KOBJ_C1_HIN_3_02", "type": "quiz", "question": "What happens when you join ज and ल?", "options": ["कल", "जल", "फल"], "correct_index": 1, "explanation": "ज + ल = जल (Water)!"},
            {"id": "KOBJ_C1_HIN_3_03", "type": "flashcard", "front": "ज + ल =", "back": "जल (Water)", "color": "0xFF00BCD4"},
            {"id": "KOBJ_C1_HIN_3_04", "type": "theory", "title": "Two-letter words", "body": "Just say the sounds together.\nघ + र = घर (House)\nफ + ल = फल (Fruit)"},
            {"id": "KOBJ_C1_HIN_3_05", "type": "flashcard", "front": "घ + र =", "back": "घर (House)", "color": "0xFF8BC34A"},
            {"id": "KOBJ_C1_HIN_3_06", "type": "teacher_tip", "title": "No extra sounds", "body": "When you read a bina matra word, don't stretch the sounds. Just say them quickly!"},
            {"id": "KOBJ_C1_HIN_3_07", "type": "theory", "title": "Three-letter words", "body": "क + म + ल = कमल (Lotus)\nम + ट + र = मटर (Peas)"},
            {"id": "KOBJ_C1_HIN_3_08", "type": "quiz", "question": "Join these: क + म + ल", "options": ["कमल", "मटर", "कलम"], "correct_index": 0, "explanation": "It makes कमल (Lotus)!"}
        ]
        save_json("app_core/chapters/class1_hindi_ch3.json", ch3)

    # 4. Aa Ki Matra
    ch4 = load_json("app_core/chapters/class1_hindi_ch4.json")
    if ch4:
        ch4["blocks"] = [
            {"id": "KOBJ_C1_HIN_4_01", "type": "hook", "title": "Opening your mouth wide!", "body": "When you go to the doctor, they say 'Say Aaaah!'. That's the sound of the Aa ki Matra!"},
            {"id": "KOBJ_C1_HIN_4_02", "type": "quiz", "question": "What does Aa ki Matra look like?", "options": ["A dot", "A straight line ( ा )", "A circle"], "correct_index": 1, "explanation": "It looks like a straight line standing next to the letter!"},
            {"id": "KOBJ_C1_HIN_4_03", "type": "theory", "title": "Aa Ki Matra ( ा )", "body": "When you add ' ा ' to a letter, it makes the 'Aa' sound.\nक + ा = का (Kaa)"},
            {"id": "KOBJ_C1_HIN_4_04", "type": "flashcard", "front": "म + ा + ल + ा =", "back": "माला (Garland)", "color": "0xFF9C27B0"},
            {"id": "KOBJ_C1_HIN_4_05", "type": "flashcard", "front": "छ + ा + त + ा =", "back": "छाता (Umbrella)", "color": "0xFF3F51B5"},
            {"id": "KOBJ_C1_HIN_4_06", "type": "teacher_tip", "title": "Stretch it!", "body": "Whenever you see ' ा ', stretch your mouth and the sound!"},
            {"id": "KOBJ_C1_HIN_4_07", "type": "theory", "title": "Reading sentences", "body": "राम छाता ला। (Ram, bring the umbrella.)"},
            {"id": "KOBJ_C1_HIN_4_08", "type": "quiz", "question": "Which word has Aa ki Matra?", "options": ["जल", "कान", "घर"], "correct_index": 1, "explanation": "कान (Kaan - Ear) has the Aa ki matra!"}
        ]
        save_json("app_core/chapters/class1_hindi_ch4.json", ch4)

    # 5. I & Ee Ki Matra
    ch5 = load_json("app_core/chapters/class1_hindi_ch5.json")
    if ch5:
        ch5["blocks"] = [
            {"id": "KOBJ_C1_HIN_5_01", "type": "hook", "title": "Short 'i' and Long 'ee'", "body": "Some sounds are quick like a mouse (i), and some stretch out (ee)!"},
            {"id": "KOBJ_C1_HIN_5_02", "type": "quiz", "question": "Which Matra comes BEFORE the letter?", "options": ["Badi Ee ( ी )", "Chhoti i ( ि )"], "correct_index": 1, "explanation": "Chhoti 'i' comes before the letter!"},
            {"id": "KOBJ_C1_HIN_5_03", "type": "theory", "title": "Chhoti i ( ि )", "body": "It makes a quick 'i' sound.\nद + ि + न = दिन (Day)"},
            {"id": "KOBJ_C1_HIN_5_04", "type": "flashcard", "front": "द + ि + न =", "back": "दिन (Day)", "color": "0xFFFF9800"},
            {"id": "KOBJ_C1_HIN_5_05", "type": "theory", "title": "Badi Ee ( ी )", "body": "It makes a long 'ee' sound and comes AFTER the letter.\nप + ा + न + ी = पानी (Water)"},
            {"id": "KOBJ_C1_HIN_5_06", "type": "flashcard", "front": "प + ा + न + ी =", "back": "पानी (Water)", "color": "0xFF03A9F4"},
            {"id": "KOBJ_C1_HIN_5_07", "type": "teacher_tip", "title": "Front or Back?", "body": "Chhoti i stands IN FRONT of the letter. Badi Ee stands BEHIND it!"},
            {"id": "KOBJ_C1_HIN_5_08", "type": "quiz", "question": "Which word has Badi Ee ( ी )?", "options": ["किताब (Book)", "हाथी (Elephant)"], "correct_index": 1, "explanation": "हाथी ends with a long ee sound!"}
        ]
        save_json("app_core/chapters/class1_hindi_ch5.json", ch5)

    # 6. Fruits & Vegetables
    ch6 = load_json("app_core/chapters/class1_hindi_ch6.json")
    if ch6:
        ch6["blocks"] = [
            {"id": "KOBJ_C1_HIN_6_01", "type": "hook", "title": "Yummy Words!", "body": "What is your favorite fruit? Do you know what it is called in Hindi?"},
            {"id": "KOBJ_C1_HIN_6_02", "type": "quiz", "question": "What is 'Apple' in Hindi?", "options": ["आम", "सेब", "केला"], "correct_index": 1, "explanation": "Apple is called सेब (Seb)."},
            {"id": "KOBJ_C1_HIN_6_03", "type": "flashcard", "front": "Mango", "back": "आम (Aam)", "color": "0xFFFFC107"},
            {"id": "KOBJ_C1_HIN_6_04", "type": "flashcard", "front": "Banana", "back": "केला (Kela)", "color": "0xFFFFEB3B"},
            {"id": "KOBJ_C1_HIN_6_05", "type": "flashcard", "front": "Potato", "back": "आलू (Aloo)", "color": "0xFF795548"},
            {"id": "KOBJ_C1_HIN_6_06", "type": "flashcard", "front": "Tomato", "back": "टमाटर (Tamatar)", "color": "0xFFF44336"},
            {"id": "KOBJ_C1_HIN_6_07", "type": "theory", "title": "Eating Healthy", "body": "Fal (Fruits) and Sabzi (Vegetables) keep us strong and healthy!"},
            {"id": "KOBJ_C1_HIN_6_08", "type": "quiz", "question": "Which of these is a vegetable?", "options": ["सेब", "आलू"], "correct_index": 1, "explanation": "आलू (Potato) is a vegetable!"}
        ]
        save_json("app_core/chapters/class1_hindi_ch6.json", ch6)

    # 7. Animals & Birds
    ch7 = load_json("app_core/chapters/class1_hindi_ch7.json")
    if ch7:
        ch7["blocks"] = [
            {"id": "KOBJ_C1_HIN_7_01", "type": "hook", "title": "Animals of the Jungle!", "body": "Lions, Tigers, Bears! Let's learn their names in Hindi."},
            {"id": "KOBJ_C1_HIN_7_02", "type": "quiz", "question": "What is a 'Dog' called in Hindi?", "options": ["बिल्ली", "कुत्ता", "गाय"], "correct_index": 1, "explanation": "A dog is कुत्ता (Kutta)."},
            {"id": "KOBJ_C1_HIN_7_03", "type": "flashcard", "front": "Cat", "back": "बिल्ली (Billi)", "color": "0xFFFF9800"},
            {"id": "KOBJ_C1_HIN_7_04", "type": "flashcard", "front": "Cow", "back": "गाय (Gaay)", "color": "0xFFE0E0E0"},
            {"id": "KOBJ_C1_HIN_7_05", "type": "flashcard", "front": "Lion", "back": "शेर (Sher)", "color": "0xFFFFC107"},
            {"id": "KOBJ_C1_HIN_7_06", "type": "flashcard", "front": "Peacock", "back": "मोर (Mor)", "color": "0xFF3F51B5"},
            {"id": "KOBJ_C1_HIN_7_07", "type": "theory", "title": "Jaanvar aur Pakshi", "body": "Animals are called 'Jaanvar' (जानवर). Birds are called 'Pakshi' (पक्षी)."},
            {"id": "KOBJ_C1_HIN_7_08", "type": "quiz", "question": "Which of these is a bird (Pakshi)?", "options": ["मोर (Mor)", "शेर (Sher)"], "correct_index": 0, "explanation": "मोर (Peacock) is a beautiful bird!"}
        ]
        save_json("app_core/chapters/class1_hindi_ch7.json", ch7)

if __name__ == "__main__":
    upgrade_class1_hindi()
