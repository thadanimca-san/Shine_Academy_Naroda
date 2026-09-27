import json
import os

def generate_supreme_maths_ch15():
    chapter_id = "ncert_class10_maths_ch15"
    title = "Chapter 15: Probability"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "Maths",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-MATHS",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["maths", "probability", "coins", "dice", "cards", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the theoretical probability of an event.",
            "Solve problems based on tossing coins and throwing dice.",
            "Solve problems based on drawing cards from a well-shuffled deck.",
            "Apply logic to real-world scenarios."
        ],
        "ai_context": {
            "learning_goal": "Make abstract probability feel real. Use the 'Socratic Discovery Arc' to build intuition before giving formulas.",
            "common_misconceptions": [
                "Students think the probability of an event can be greater than 1.",
                "Students get confused with the sample space of tossing 2 or 3 coins.",
                "Students struggle with the composition of a standard deck of cards."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine you are playing a board game with your friends. You need exactly a 6 on the dice to win. What are your chances? Is it pure luck, or is there a mathematical way to predict it? Welcome to the fascinating world of **Probability (प्रायिकता / સંભાવના)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Probability Scale: Probability always lies between 0 and 1. 0 means impossible, 1 means certain.",
        "image_url": "assets/images/maths_ch15_probability_scale.jpg",
        "alt_text": "A glowing scale from 0 to 1 showing Impossible, Unlikely, Even Chance, Likely, and Certain."
    })

    # ==========================================
    # MODULE 2: FORMULA & COINS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Theoretical Probability (सैद्धांतिक प्रायिकता):**\nThe probability of an event E, written as P(E), is defined as:\nP(E) = (Number of outcomes favorable to E) / (Number of all possible outcomes of the experiment)\n\n*Example - Tossing a Coin (सिक्का उछालना):* When you toss a fair coin, possible outcomes are Head (H) or Tail (T). So, P(Head) = 1/2.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** When tossing **2 coins**, the sample space is {HH, HT, TH, TT}. When tossing **3 coins**, it is {HHH, HHT, HTH, HTT, THH, THT, TTH, TTT}. A quick formula for total outcomes is **2ⁿ**, where n is the number of coins!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 3: DICE
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Throwing Two Dice (दो पासे फेंकना)\n\nWhen you throw 2 dice, the total number of outcomes is **6 × 6 = 36**. \n*Board Trick:* They often ask for the sum of numbers on the two dice. Remember, the sum ranges from 2 (1+1) to 12 (6+6). Draw a 6x6 table in rough work if you get confused!",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 4: CARDS
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "A standard deck of 52 playing cards (ताश के पत्ते).",
        "image_url": "assets/images/maths_ch15_cards_deck.jpg",
        "alt_text": "A visual breakdown of 52 cards into 4 suits: Spades, Hearts, Diamonds, Clubs."
    })

    blocks.append({
        "type": "memory_trick",
        "content": "**The Card Deck Breakdown:**\nTotal 52 cards = 26 Red + 26 Black.\n4 Suits (13 cards each): Spades (♠ Black), Clubs (♣ Black), Hearts (♥ Red), Diamonds (♦ Red).\nEach suit has: Ace, 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King.\n**Face Cards:** Jack, Queen, King. Total face cards = 3 × 4 = 12.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch15.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_maths_ch15.json"
    final_json["metadata"]["id"] = "gseb_class10_maths_ch15"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Maths Chapter 15 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_maths_ch15()
