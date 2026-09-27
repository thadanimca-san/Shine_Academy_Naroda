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

def upgrade_class1_maths():
    print("Generating Gold Standard Class 1 Maths...")
    
    # 1. Numbers 1-100
    ch1 = load_json("app_core/chapters/class1_maths_ch1.json")
    if ch1:
        ch1["blocks"] = [
            {"id": "KOBJ_C1_MAT_1_01", "type": "hook", "title": "The Biggest Number You Know!", "body": "How many fingers do you have? 10! How many stars are in the sky? So many! Let's count to 100!"},
            {"id": "KOBJ_C1_MAT_1_02", "type": "quiz", "question": "What comes after 9?", "options": ["8", "10", "11"], "correct_index": 1, "explanation": "After 9 comes 10!"},
            {"id": "KOBJ_C1_MAT_1_03", "type": "flashcard", "front": "Let's skip count by 10s!", "back": "10, 20, 30, 40, 50...", "color": "0xFF2196F3"},
            {"id": "KOBJ_C1_MAT_1_04", "type": "theory", "title": "The Number Grid", "body": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10,\n11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\n21, 22, 23, 24, 25, 26, 27, 28, 29, 30,\n31, 32, 33, 34, 35, 36, 37, 38, 39, 40,\n41, 42, 43, 44, 45, 46, 47, 48, 49, 50,\n51, 52, 53, 54, 55, 56, 57, 58, 59, 60,\n61, 62, 63, 64, 65, 66, 67, 68, 69, 70,\n71, 72, 73, 74, 75, 76, 77, 78, 79, 80,\n81, 82, 83, 84, 85, 86, 87, 88, 89, 90,\n91, 92, 93, 94, 95, 96, 97, 98, 99, 100"},
            {"id": "KOBJ_C1_MAT_1_05", "type": "quiz", "question": "What comes after 99?", "options": ["100", "98", "10"], "correct_index": 0, "explanation": "100 is the first 3-digit number!"},
            {"id": "KOBJ_C1_MAT_1_06", "type": "teacher_tip", "title": "Counting Trick", "body": "Whenever a number ends in 9, the next number changes the first digit! (Like 19 -> 20)."},
            {"id": "KOBJ_C1_MAT_1_07", "type": "theory", "title": "Real World Numbers", "body": "Numbers are everywhere! On houses, phones, and money!"},
            {"id": "KOBJ_C1_MAT_1_08", "type": "quiz", "question": "If you have 40 and add 10, what do you get?", "options": ["41", "50", "30"], "correct_index": 1, "explanation": "40 + 10 = 50!"}
        ]
        save_json("app_core/chapters/class1_maths_ch1.json", ch1)

    # 2. Addition (1-digit)
    ch2 = load_json("app_core/chapters/class1_maths_ch2.json")
    if ch2:
        ch2["blocks"] = [
            {"id": "KOBJ_C1_MAT_2_01", "type": "hook", "title": "Putting Things Together", "body": "If you have 2 apples and your friend gives you 3 more, how many do you have?"},
            {"id": "KOBJ_C1_MAT_2_02", "type": "quiz", "question": "What happens when we ADD numbers?", "options": ["They get smaller", "They get bigger", "They stay the same"], "correct_index": 1, "explanation": "Adding makes things bigger!"},
            {"id": "KOBJ_C1_MAT_2_03", "type": "flashcard", "front": "2 + 3 = ?", "back": "5", "color": "0xFF4CAF50"},
            {"id": "KOBJ_C1_MAT_2_04", "type": "theory", "title": "What is Addition?", "body": "Addition is finding the total, or sum, by combining two or more numbers. We use the plus symbol (+)."},
            {"id": "KOBJ_C1_MAT_2_05", "type": "quiz", "question": "What is 4 + 4?", "options": ["7", "8", "9"], "correct_index": 1, "explanation": "Four and Four make Eight!"},
            {"id": "KOBJ_C1_MAT_2_06", "type": "teacher_tip", "title": "Use your fingers!", "body": "Hold up 4 fingers on one hand, and 4 on the other. Count them all!"},
            {"id": "KOBJ_C1_MAT_2_07", "type": "theory", "title": "Adding Zero", "body": "When you add 0 to a number, the number stays the same! (5 + 0 = 5)"},
            {"id": "KOBJ_C1_MAT_2_08", "type": "quiz", "question": "You have 5 candies. You buy 4 more. How many now?", "options": ["8", "9", "10"], "correct_index": 1, "explanation": "5 + 4 = 9 candies!"}
        ]
        save_json("app_core/chapters/class1_maths_ch2.json", ch2)

    # 3. Subtraction (1-digit)
    ch3 = load_json("app_core/chapters/class1_maths_ch3.json")
    if ch3:
        ch3["blocks"] = [
            {"id": "KOBJ_C1_MAT_3_01", "type": "hook", "title": "Taking Away", "body": "Imagine you have 5 chocolates. You eat 2. How many are left?"},
            {"id": "KOBJ_C1_MAT_3_02", "type": "quiz", "question": "What happens when we SUBTRACT?", "options": ["Numbers get bigger", "Numbers get smaller"], "correct_index": 1, "explanation": "Subtraction takes away, making the number smaller."},
            {"id": "KOBJ_C1_MAT_3_03", "type": "flashcard", "front": "5 - 2 = ?", "back": "3", "color": "0xFFF44336"},
            {"id": "KOBJ_C1_MAT_3_04", "type": "theory", "title": "What is Subtraction?", "body": "Subtraction is taking one number away from another. We use the minus symbol (-)."},
            {"id": "KOBJ_C1_MAT_3_05", "type": "quiz", "question": "What is 8 - 4?", "options": ["2", "4", "6"], "correct_index": 1, "explanation": "Half of 8 is 4, so 8 - 4 = 4!"},
            {"id": "KOBJ_C1_MAT_3_06", "type": "common_mistakes", "title": "Watch the sign!", "body": "Make sure you check if it is a PLUS (+) or a MINUS (-). Don't mix them up!"},
            {"id": "KOBJ_C1_MAT_3_07", "type": "theory", "title": "Subtracting Zero", "body": "If you take away 0, you lose nothing! (7 - 0 = 7)"},
            {"id": "KOBJ_C1_MAT_3_08", "type": "quiz", "question": "There are 9 birds on a tree. 3 fly away. How many are left?", "options": ["5", "6", "7"], "correct_index": 1, "explanation": "9 - 3 = 6 birds left!"}
        ]
        save_json("app_core/chapters/class1_maths_ch3.json", ch3)

    # 4. Shapes Around Us
    ch4 = load_json("app_core/chapters/class1_maths_ch4.json")
    if ch4:
        ch4["blocks"] = [
            {"id": "KOBJ_C1_MAT_4_01", "type": "hook", "title": "Look Around You!", "body": "What shape is your screen? What shape is a pizza?"},
            {"id": "KOBJ_C1_MAT_4_02", "type": "quiz", "question": "What shape has no corners?", "options": ["Square", "Circle", "Triangle"], "correct_index": 1, "explanation": "A circle is perfectly round!"},
            {"id": "KOBJ_C1_MAT_4_03", "type": "flashcard", "front": "Pizza Slice", "back": "Triangle (3 sides)", "color": "0xFFFF9800"},
            {"id": "KOBJ_C1_MAT_4_04", "type": "theory", "title": "Basic Shapes", "body": "Circle: Round, no corners.\nSquare: 4 equal sides.\nTriangle: 3 sides.\nRectangle: 4 sides (2 long, 2 short)."},
            {"id": "KOBJ_C1_MAT_4_05", "type": "quiz", "question": "A door is usually what shape?", "options": ["Square", "Rectangle", "Circle"], "correct_index": 1, "explanation": "Doors are tall and have 4 sides (Rectangle)."},
            {"id": "KOBJ_C1_MAT_4_06", "type": "teacher_tip", "title": "Counting Sides", "body": "To identify a shape, just count its straight sides and corners!"},
            {"id": "KOBJ_C1_MAT_4_07", "type": "theory", "title": "Shapes in Nature", "body": "The sun is a circle. Pine trees look like triangles!"},
            {"id": "KOBJ_C1_MAT_4_08", "type": "quiz", "question": "If you put two squares side by side, what new shape do they make?", "options": ["A bigger square", "A rectangle", "A triangle"], "correct_index": 1, "explanation": "They make a rectangle because it becomes longer on one side!"}
        ]
        save_json("app_core/chapters/class1_maths_ch4.json", ch4)

    # 5. Time
    ch5 = load_json("app_core/chapters/class1_maths_ch5.json")
    if ch5:
        ch5["blocks"] = [
            {"id": "KOBJ_C1_MAT_5_01", "type": "hook", "title": "Tick Tock", "body": "When do you wake up? When do you sleep? Time never stops!"},
            {"id": "KOBJ_C1_MAT_5_02", "type": "quiz", "question": "Which hand on the clock moves the fastest?", "options": ["Hour hand", "Minute hand", "Second hand"], "correct_index": 2, "explanation": "The second hand ticks every single second!"},
            {"id": "KOBJ_C1_MAT_5_03", "type": "flashcard", "front": "Short hand on a clock?", "back": "Hour Hand", "color": "0xFF9C27B0"},
            {"id": "KOBJ_C1_MAT_5_04", "type": "theory", "title": "Reading a Clock", "body": "The small hand shows the Hour.\nThe big hand shows the Minutes.\nIf the big hand is on 12, it is exactly that hour (e.g., 3 O'Clock)."},
            {"id": "KOBJ_C1_MAT_5_05", "type": "quiz", "question": "If the short hand is on 4, and the long hand is on 12, what time is it?", "options": ["12 O'Clock", "4 O'Clock", "4:12"], "correct_index": 1, "explanation": "It is exactly 4 O'Clock!"},
            {"id": "KOBJ_C1_MAT_5_06", "type": "teacher_tip", "title": "Morning and Night", "body": "We say 'AM' for morning time, and 'PM' for afternoon and night!"},
            {"id": "KOBJ_C1_MAT_5_07", "type": "theory", "title": "Days of the Week", "body": "Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday!"},
            {"id": "KOBJ_C1_MAT_5_08", "type": "quiz", "question": "What day comes after Friday?", "options": ["Thursday", "Saturday", "Sunday"], "correct_index": 1, "explanation": "Saturday is the weekend!"}
        ]
        save_json("app_core/chapters/class1_maths_ch5.json", ch5)

    # 6. Money
    ch6 = load_json("app_core/chapters/class1_maths_ch6.json")
    if ch6:
        ch6["blocks"] = [
            {"id": "KOBJ_C1_MAT_6_01", "type": "hook", "title": "Buying Toys!", "body": "How do we buy things from a shop? We use money!"},
            {"id": "KOBJ_C1_MAT_6_02", "type": "quiz", "question": "What do we use in India to buy things?", "options": ["Dollars", "Rupees", "Pounds"], "correct_index": 1, "explanation": "We use Indian Rupees (₹)!"},
            {"id": "KOBJ_C1_MAT_6_03", "type": "flashcard", "front": "Coins vs Notes", "back": "Coins are metal, Notes are paper!", "color": "0xFF607D8B"},
            {"id": "KOBJ_C1_MAT_6_04", "type": "theory", "title": "Rupees (₹)", "body": "Money comes in different values. We have ₹1, ₹2, ₹5, ₹10 coins. We also have notes for ₹10, ₹20, ₹50, ₹100, and more!"},
            {"id": "KOBJ_C1_MAT_6_05", "type": "quiz", "question": "If you have a ₹10 note and a ₹5 coin, how much do you have?", "options": ["₹10", "₹15", "₹50"], "correct_index": 1, "explanation": "10 + 5 = 15!"},
            {"id": "KOBJ_C1_MAT_6_06", "type": "teacher_tip", "title": "Piggy Bank", "body": "Saving small coins in a piggy bank can add up to a lot of money!"},
            {"id": "KOBJ_C1_MAT_6_07", "type": "theory", "title": "Paying Exactly", "body": "If a toy costs ₹15, you can give the shopkeeper a ₹10 note and a ₹5 coin."},
            {"id": "KOBJ_C1_MAT_6_08", "type": "quiz", "question": "A pen costs ₹10. You give a ₹20 note. How much change will you get back?", "options": ["₹5", "₹10", "₹20"], "correct_index": 1, "explanation": "20 - 10 = ₹10 change!"}
        ]
        save_json("app_core/chapters/class1_maths_ch6.json", ch6)

    # 7. Measurement
    ch7 = load_json("app_core/chapters/class1_maths_ch7.json")
    if ch7:
        ch7["blocks"] = [
            {"id": "KOBJ_C1_MAT_7_01", "type": "hook", "title": "Big, Small, Heavy, Light!", "body": "Is an elephant heavier than a mouse? Are you taller than your bag?"},
            {"id": "KOBJ_C1_MAT_7_02", "type": "quiz", "question": "Which is longer?", "options": ["A pencil", "A school bus"], "correct_index": 1, "explanation": "A school bus is much longer!"},
            {"id": "KOBJ_C1_MAT_7_03", "type": "flashcard", "front": "Heavy vs Light", "back": "A rock is Heavy. A feather is Light.", "color": "0xFFE91E63"},
            {"id": "KOBJ_C1_MAT_7_04", "type": "theory", "title": "Measuring Length", "body": "We can measure how long things are using rulers, handspans, or footsteps. We use words like Long, Short, Tall, and Short."},
            {"id": "KOBJ_C1_MAT_7_05", "type": "quiz", "question": "Which is the tallest?", "options": ["A dog", "A giraffe", "A cat"], "correct_index": 1, "explanation": "Giraffes have very long necks and are very tall!"},
            {"id": "KOBJ_C1_MAT_7_06", "type": "teacher_tip", "title": "Capacity", "body": "We also measure how much a container can hold. A bucket holds MORE water than a cup!"},
            {"id": "KOBJ_C1_MAT_7_07", "type": "theory", "title": "Comparing Weight", "body": "A watermelon is Heavy. An apple is Light."},
            {"id": "KOBJ_C1_MAT_7_08", "type": "quiz", "question": "Which holds more water?", "options": ["A spoon", "A swimming pool", "A glass"], "correct_index": 1, "explanation": "A swimming pool holds a massive amount of water!"}
        ]
        save_json("app_core/chapters/class1_maths_ch7.json", ch7)

if __name__ == "__main__":
    upgrade_class1_maths()
