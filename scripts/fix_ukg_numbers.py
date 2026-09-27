import json

def update_ukg_numbers():
    print("Fixing UKG Numbers Chapters...")
    
    # Chapter 1: Counting by 10s
    ch1 = {
        "metadata": {
            "id": "ukg_numbers_ch1",
            "title": "Counting by 10s",
            "subject": "Numbers",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_UKG_NUM_1_01", "type": "hook", "title": "Let's count by 10s!", "body": "Skip counting is fun!"}
        ]
    }
    for i, num in enumerate([10, 20, 30, 40, 50, 60, 70, 80, 90, 100]):
        ch1["blocks"].append({
            "id": f"KOBJ_UKG_NUM_1_0{i+2}",
            "type": "flashcard",
            "front": str(num),
            "back": f"{num}!",
            "color": "0xFF4CAF50"
        })
        
    # Chapter 2: Counting to 100
    ch2 = {
        "metadata": {
            "id": "ukg_numbers_ch2",
            "title": "Counting to 100",
            "subject": "Numbers",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_UKG_NUM_2_01", "type": "hook", "title": "Big Numbers!", "body": "Let's count all the way to 100!"},
            {"id": "KOBJ_UKG_NUM_2_02", "type": "theory", "title": "Numbers 1 to 100", "body": "1, 2, 3, 4, 5, 6, 7, 8, 9, 10,\n11, 12, 13, 14, 15, 16, 17, 18, 19, 20,\n21, 22, 23, 24, 25, 26, 27, 28, 29, 30,\n31, 32, 33, 34, 35, 36, 37, 38, 39, 40,\n41, 42, 43, 44, 45, 46, 47, 48, 49, 50,\n51, 52, 53, 54, 55, 56, 57, 58, 59, 60,\n61, 62, 63, 64, 65, 66, 67, 68, 69, 70,\n71, 72, 73, 74, 75, 76, 77, 78, 79, 80,\n81, 82, 83, 84, 85, 86, 87, 88, 89, 90,\n91, 92, 93, 94, 95, 96, 97, 98, 99, 100"}
        ]
    }
    
    # Chapter 3: Simple Addition (+1)
    ch3 = {
        "metadata": {
            "id": "ukg_numbers_ch3",
            "title": "Simple Addition (+1)",
            "subject": "Numbers",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_UKG_NUM_3_01", "type": "hook", "title": "Adding 1", "body": "What happens when you add 1 apple?"}
        ]
    }
    for i in range(1, 6):
        ch3["blocks"].append({
            "id": f"KOBJ_UKG_NUM_3_0{i+1}",
            "type": "flashcard",
            "front": f"{i} + 1 = ?",
            "back": f"{i} + 1 = {i+1}",
            "color": "0xFFFF9800"
        })
        
    # Chapter 4: Simple Addition (+2)
    ch4 = {
        "metadata": {
            "id": "ukg_numbers_ch4",
            "title": "Simple Addition (+2)",
            "subject": "Numbers",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_UKG_NUM_4_01", "type": "hook", "title": "Adding 2", "body": "What happens when you add 2 apples?"}
        ]
    }
    for i in range(1, 6):
        ch4["blocks"].append({
            "id": f"KOBJ_UKG_NUM_4_0{i+1}",
            "type": "flashcard",
            "front": f"{i} + 2 = ?",
            "back": f"{i} + 2 = {i+2}",
            "color": "0xFFFF9800"
        })

    # Chapter 5: Simple Subtraction (-1)
    ch5 = {
        "metadata": {
            "id": "ukg_numbers_ch5",
            "title": "Simple Subtraction (-1)",
            "subject": "Numbers",
            "difficulty": "Beginner",
            "estimated_minutes": 15
        },
        "blocks": [
            {"id": "KOBJ_UKG_NUM_5_01", "type": "hook", "title": "Subtracting 1", "body": "What happens when you take away 1 apple?"}
        ]
    }
    for i in range(2, 7):
        ch5["blocks"].append({
            "id": f"KOBJ_UKG_NUM_5_0{i}",
            "type": "flashcard",
            "front": f"{i} - 1 = ?",
            "back": f"{i} - 1 = {i-1}",
            "color": "0xFFF44336"
        })

    chapters = [ch1, ch2, ch3, ch4, ch5]
    
    for i, ch in enumerate(chapters):
        filepath = f"app_core/chapters/ukg_numbers_ch{i+1}.json"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(ch, f, indent=2, ensure_ascii=False)
            
    print("Successfully fixed UKG Numbers!")

if __name__ == "__main__":
    update_ukg_numbers()
