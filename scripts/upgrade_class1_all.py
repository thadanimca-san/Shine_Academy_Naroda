import json
import glob

def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading {filepath}: {e}")
        return None

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def upgrade_maths():
    print("Upgrading Class 1 Maths...")
    
    # Chapter 1: Numbers 1-100
    ch1 = load_json("app_core/chapters/class1_maths_ch1.json")
    if ch1:
        ch1["blocks"] = [
            {"id": "KOBJ_C1_MAT_1_01", "type": "hook", "title": "Counting is Fun!", "body": "Let's count from 1 to 100!"},
            {"id": "KOBJ_C1_MAT_1_02", "type": "theory", "title": "1 to 100", "body": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10,\n11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\n21, 22, 23, 24, 25, 26, 27, 28, 29, 30,\n31, 32, 33, 34, 35, 36, 37, 38, 39, 40,\n41, 42, 43, 44, 45, 46, 47, 48, 49, 50,\n51, 52, 53, 54, 55, 56, 57, 58, 59, 60,\n61, 62, 63, 64, 65, 66, 67, 68, 69, 70,\n71, 72, 73, 74, 75, 76, 77, 78, 79, 80,\n81, 82, 83, 84, 85, 86, 87, 88, 89, 90,\n91, 92, 93, 94, 95, 96, 97, 98, 99, 100"}
        ]
        save_json("app_core/chapters/class1_maths_ch1.json", ch1)

    # Chapter 2: Addition (1-digit)
    ch2 = load_json("app_core/chapters/class1_maths_ch2.json")
    if ch2:
        ch2["blocks"] = [
            {"id": "KOBJ_C1_MAT_2_01", "type": "hook", "title": "Adding Things Together", "body": "When we put things together, we add them!"},
            {"id": "KOBJ_C1_MAT_2_02", "type": "flashcard", "front": "2 + 3 = ?", "back": "2 + 3 = 5", "color": "0xFF4CAF50"},
            {"id": "KOBJ_C1_MAT_2_03", "type": "flashcard", "front": "4 + 1 = ?", "back": "4 + 1 = 5", "color": "0xFF2196F3"},
            {"id": "KOBJ_C1_MAT_2_04", "type": "quiz", "question": "What is 3 + 3?", "options": ["5", "6", "7"], "correct_index": 1, "explanation": "3 and 3 make 6!"}
        ]
        save_json("app_core/chapters/class1_maths_ch2.json", ch2)

    # Chapter 3: Subtraction (1-digit)
    ch3 = load_json("app_core/chapters/class1_maths_ch3.json")
    if ch3:
        ch3["blocks"] = [
            {"id": "KOBJ_C1_MAT_3_01", "type": "hook", "title": "Taking Away", "body": "When we take things away, we subtract!"},
            {"id": "KOBJ_C1_MAT_3_02", "type": "flashcard", "front": "5 - 2 = ?", "back": "5 - 2 = 3", "color": "0xFFF44336"},
            {"id": "KOBJ_C1_MAT_3_03", "type": "flashcard", "front": "4 - 1 = ?", "back": "4 - 1 = 3", "color": "0xFFFF9800"},
            {"id": "KOBJ_C1_MAT_3_04", "type": "quiz", "question": "What is 6 - 3?", "options": ["2", "3", "4"], "correct_index": 1, "explanation": "6 minus 3 leaves 3!"}
        ]
        save_json("app_core/chapters/class1_maths_ch3.json", ch3)

    # Chapter 4: Shapes Around Us
    ch4 = load_json("app_core/chapters/class1_maths_ch4.json")
    if ch4:
        ch4["blocks"] = [
            {"id": "KOBJ_C1_MAT_4_01", "type": "hook", "title": "Shapes are Everywhere!", "body": "Look around! What shapes do you see?"},
            {"id": "KOBJ_C1_MAT_4_02", "type": "flashcard", "front": "Round like a Pizza", "back": "Circle", "color": "0xFFE91E63"},
            {"id": "KOBJ_C1_MAT_4_03", "type": "flashcard", "front": "Four equal sides like a Window", "back": "Square", "color": "0xFF9C27B0"},
            {"id": "KOBJ_C1_MAT_4_04", "type": "flashcard", "front": "Three sides like a Samosa", "back": "Triangle", "color": "0xFF00BCD4"},
            {"id": "KOBJ_C1_MAT_4_05", "type": "quiz", "question": "A coin is what shape?", "options": ["Square", "Circle", "Triangle"], "correct_index": 1, "explanation": "A coin is completely round!"}
        ]
        save_json("app_core/chapters/class1_maths_ch4.json", ch4)

    # Chapter 5: Time
    ch5 = load_json("app_core/chapters/class1_maths_ch5.json")
    if ch5:
        ch5["blocks"] = [
            {"id": "KOBJ_C1_MAT_5_01", "type": "hook", "title": "Tick Tock", "body": "When do you wake up? When do you sleep? Let's learn about Time!"},
            {"id": "KOBJ_C1_MAT_5_02", "type": "theory", "title": "Parts of the Day", "body": "Morning: The sun rises.\nAfternoon: The sun is high.\nEvening: The sun sets.\nNight: The stars come out!"},
            {"id": "KOBJ_C1_MAT_5_03", "type": "quiz", "question": "When do you go to sleep?", "options": ["Morning", "Afternoon", "Night"], "correct_index": 2, "explanation": "We sleep at night!"}
        ]
        save_json("app_core/chapters/class1_maths_ch5.json", ch5)

    # Chapter 6: Money
    ch6 = load_json("app_core/chapters/class1_maths_ch6.json")
    if ch6:
        ch6["blocks"] = [
            {"id": "KOBJ_C1_MAT_6_01", "type": "hook", "title": "Buying Toys!", "body": "How do you buy a toy? You use money!"},
            {"id": "KOBJ_C1_MAT_6_02", "type": "theory", "title": "Rupees and Paise", "body": "In India, our money is in Rupees (₹) and Paise. We have notes and coins."},
            {"id": "KOBJ_C1_MAT_6_03", "type": "quiz", "question": "What is the symbol for Rupee?", "options": ["$", "₹", "£"], "correct_index": 1, "explanation": "The symbol for Indian Rupee is ₹."}
        ]
        save_json("app_core/chapters/class1_maths_ch6.json", ch6)

    # Chapter 7: Measurement
    ch7 = load_json("app_core/chapters/class1_maths_ch7.json")
    if ch7:
        ch7["blocks"] = [
            {"id": "KOBJ_C1_MAT_7_01", "type": "hook", "title": "Long or Short?", "body": "Are you taller than your friend? Let's measure!"},
            {"id": "KOBJ_C1_MAT_7_02", "type": "flashcard", "front": "The opposite of Tall is...", "back": "Short!", "color": "0xFF8BC34A"},
            {"id": "KOBJ_C1_MAT_7_03", "type": "flashcard", "front": "The opposite of Heavy is...", "back": "Light!", "color": "0xFFFFEB3B"},
            {"id": "KOBJ_C1_MAT_7_04", "type": "quiz", "question": "Which is heavier?", "options": ["A feather", "An elephant"], "correct_index": 1, "explanation": "An elephant is very heavy!"}
        ]
        save_json("app_core/chapters/class1_maths_ch7.json", ch7)

def upgrade_evs():
    print("Upgrading Class 1 EVS...")
    files = sorted(glob.glob("app_core/chapters/class1_evs_ch*.json"), key=lambda x: int(x.split('_ch')[1].split('.json')[0]))
    for count, filepath in enumerate(files):
        data = load_json(filepath)
        if not data: continue
        title = data["metadata"]["title"]
        blocks = [
            {"id": f"KOBJ_C1_EVS_{count+1}_01", "type": "hook", "title": f"Let's learn about {title}!", "body": "Are you ready?"},
            {"id": f"KOBJ_C1_EVS_{count+1}_02", "type": "theory", "title": title, "body": f"In this chapter, we explore {title}. It is important to understand the world around us."},
            {"id": f"KOBJ_C1_EVS_{count+1}_03", "type": "quiz", "question": f"Do you like learning about {title}?", "options": ["Yes", "No"], "correct_index": 0, "explanation": "Learning is fun!"}
        ]
        data["blocks"] = blocks
        save_json(filepath, data)

def upgrade_hindi():
    print("Upgrading Class 1 Hindi...")
    # 7 Chapters
    
    # Ch1: Varnamala (Swar)
    ch1 = load_json("app_core/chapters/class1_hindi_ch1.json")
    if ch1:
        ch1["blocks"] = [
            {"id": "KOBJ_C1_HIN_1_01", "type": "hook", "title": "Varnamala Swar", "body": "Let's learn Hindi vowels!"},
            {"id": "KOBJ_C1_HIN_1_02", "type": "trace_alphabet", "letter": "अ"},
            {"id": "KOBJ_C1_HIN_1_03", "type": "flashcard", "front": "अ से...", "back": "अनार (Pomegranate)", "color": "0xFFE91E63"},
            {"id": "KOBJ_C1_HIN_1_04", "type": "trace_alphabet", "letter": "आ"},
            {"id": "KOBJ_C1_HIN_1_05", "type": "flashcard", "front": "आ से...", "back": "आम (Mango)", "color": "0xFFFFC107"}
        ]
        save_json("app_core/chapters/class1_hindi_ch1.json", ch1)

    # Ch2: Varnamala (Vyanjan)
    ch2 = load_json("app_core/chapters/class1_hindi_ch2.json")
    if ch2:
        ch2["blocks"] = [
            {"id": "KOBJ_C1_HIN_2_01", "type": "hook", "title": "Varnamala Vyanjan", "body": "Let's learn Hindi consonants!"},
            {"id": "KOBJ_C1_HIN_2_02", "type": "trace_alphabet", "letter": "क"},
            {"id": "KOBJ_C1_HIN_2_03", "type": "flashcard", "front": "क से...", "back": "कबूतर (Pigeon)", "color": "0xFF2196F3"},
            {"id": "KOBJ_C1_HIN_2_04", "type": "trace_alphabet", "letter": "ख"},
            {"id": "KOBJ_C1_HIN_2_05", "type": "flashcard", "front": "ख से...", "back": "खरगोश (Rabbit)", "color": "0xFF4CAF50"}
        ]
        save_json("app_core/chapters/class1_hindi_ch2.json", ch2)

    # Ch3: Bina Matra Wale Shabd
    ch3 = load_json("app_core/chapters/class1_hindi_ch3.json")
    if ch3:
        ch3["blocks"] = [
            {"id": "KOBJ_C1_HIN_3_01", "type": "hook", "title": "Simple Words", "body": "Let's read words without any Matras!"},
            {"id": "KOBJ_C1_HIN_3_02", "type": "flashcard", "front": "ज + ल =", "back": "जल (Water)", "color": "0xFF00BCD4"},
            {"id": "KOBJ_C1_HIN_3_03", "type": "flashcard", "front": "घ + र =", "back": "घर (House)", "color": "0xFF8BC34A"}
        ]
        save_json("app_core/chapters/class1_hindi_ch3.json", ch3)

    # Ch4: Aa Ki Matra
    ch4 = load_json("app_core/chapters/class1_hindi_ch4.json")
    if ch4:
        ch4["blocks"] = [
            {"id": "KOBJ_C1_HIN_4_01", "type": "hook", "title": "Aa Ki Matra", "body": "Let's add 'Aa' to words!"},
            {"id": "KOBJ_C1_HIN_4_02", "type": "flashcard", "front": "म + ा + ल + ा =", "back": "माला (Garland)", "color": "0xFF9C27B0"}
        ]
        save_json("app_core/chapters/class1_hindi_ch4.json", ch4)

    # Ch5: I & Ee Ki Matra
    ch5 = load_json("app_core/chapters/class1_hindi_ch5.json")
    if ch5:
        ch5["blocks"] = [
            {"id": "KOBJ_C1_HIN_5_01", "type": "hook", "title": "I & Ee Matra", "body": "Let's learn small and big ee sounds!"},
            {"id": "KOBJ_C1_HIN_5_02", "type": "flashcard", "front": "द + ि + न =", "back": "दिन (Day)", "color": "0xFFFF9800"},
            {"id": "KOBJ_C1_HIN_5_03", "type": "flashcard", "front": "प + ा + न + ी =", "back": "पानी (Water)", "color": "0xFF03A9F4"}
        ]
        save_json("app_core/chapters/class1_hindi_ch5.json", ch5)

    # Ch6: Fruits & Vegetables
    ch6 = load_json("app_core/chapters/class1_hindi_ch6.json")
    if ch6:
        ch6["blocks"] = [
            {"id": "KOBJ_C1_HIN_6_01", "type": "hook", "title": "Fruits & Veggies", "body": "Let's learn their names in Hindi!"},
            {"id": "KOBJ_C1_HIN_6_02", "type": "flashcard", "front": "Apple", "back": "सेब (Seb)", "color": "0xFFF44336"},
            {"id": "KOBJ_C1_HIN_6_03", "type": "flashcard", "front": "Potato", "back": "आलू (Aloo)", "color": "0xFF795548"}
        ]
        save_json("app_core/chapters/class1_hindi_ch6.json", ch6)

    # Ch7: Animals & Birds
    ch7 = load_json("app_core/chapters/class1_hindi_ch7.json")
    if ch7:
        ch7["blocks"] = [
            {"id": "KOBJ_C1_HIN_7_01", "type": "hook", "title": "Animals", "body": "Let's learn animal names in Hindi!"},
            {"id": "KOBJ_C1_HIN_7_02", "type": "flashcard", "front": "Dog", "back": "कुत्ता (Kutta)", "color": "0xFF607D8B"},
            {"id": "KOBJ_C1_HIN_7_03", "type": "flashcard", "front": "Cat", "back": "बिल्ली (Billi)", "color": "0xFFFF5722"}
        ]
        save_json("app_core/chapters/class1_hindi_ch7.json", ch7)


if __name__ == "__main__":
    upgrade_maths()
    upgrade_evs()
    upgrade_hindi()
    print("Class 1 interactive upgrade complete!")
