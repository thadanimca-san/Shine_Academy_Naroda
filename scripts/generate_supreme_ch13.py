import json
import os

def generate_supreme_chapter_13():
    chapter_id = "ncert_class10_science_ch13"
    title = "Chapter 13: Our Environment"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "Science",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-VISUAL",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["biology", "environment", "food_chain", "ecosystem", "ozone", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the components of an Ecosystem.",
            "Analyze Food Chains and Food Webs in nature.",
            "Understand the importance of the Ozone Layer and its depletion.",
            "Solve CBSE/State Board HOTS questions about waste management and 10% law."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Our Environment. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students think energy can be completely transferred between trophic levels. (Fact: Only 10% is transferred).",
                "Students confuse ozone depletion with global warming."
            ]
        }
    }
    
    blocks = []
    
    # MODULE 1: INTRODUCTION TO ECOSYSTEM
    blocks.append({
        "type": "hook",
        "content": "Have you ever visited a garden and noticed insects, birds, and plants living together in harmony (सद्भाव / સુમેળ)? This beautiful interaction between living and non-living things forms what we call an **Ecosystem (पारिस्थितिक तंत्र / નિવસનતંત્ર)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "An ecosystem consists of biotic (living) and abiotic (non-living) components.",
        "image_url": "assets/images/ch13_ecosystem.jpg",
        "alt_text": "A beautiful ecosystem with plants, animals, water, and sunlight"
    })

    blocks.append({
        "type": "theory",
        "content": "An **Ecosystem** includes all living organisms (plants, animals, microorganisms) interacting with each other and their non-living environment (weather, earth, sun, soil, climate, atmosphere).\n\nComponents:\n- **Biotic Components (जैविक घटक / જૈવિક ઘટકો):** Producers, Consumers, Decomposers.\n- **Abiotic Components (अजैविक घटक / અજૈવિક ઘટકો):** Temperature, Rainfall, Wind, Soil, Minerals.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # MODULE 2: FOOD CHAINS AND FOOD WEBS
    blocks.append({
        "type": "theory",
        "content": "Who eats whom? A **Food Chain (खाद्य श्रृंखला / આહાર શૃંખલા)** is a series of organisms in which one organism eats another to transfer food energy.\n\nExample: **Grass ⟶ Deer ⟶ Lion**",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "A food chain showing energy flow from producers to top carnivores.",
        "image_url": "assets/images/ch13_food_chain.jpg",
        "alt_text": "Food chain from grass to grasshopper to frog to snake to eagle"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC: The 10% Law**\n\nOnly 10% of the energy is transferred from one trophic level to the next. The rest is lost as heat. This is why food chains usually have only 3 or 4 steps!",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # MODULE 3: OZONE LAYER
    blocks.append({
        "type": "theory",
        "content": "The **Ozone Layer (ओजोन परत / ઓઝોન સ્તર)** acts like a protective shield for the Earth. It absorbs harmful Ultraviolet (UV) radiations from the Sun, protecting us from skin cancer.\n\n*Formula:* **O₃**",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "diagram",
        "content": "Ozone layer protecting Earth from UV rays.",
        "image_url": "assets/images/ch13_ozone_layer.jpg",
        "alt_text": "Earth shielded by ozone layer blocking UV rays"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "Students, Chlorofluorocarbons (CFCs) used in refrigerators and fire extinguishers are the main chemicals causing Ozone depletion. Memorize this for 1-mark questions!",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    os.makedirs("/home/ubuntu/Shine_Academy_Naroda/app_core/chapters", exist_ok=True)
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch13.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch13.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch13"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 13 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_13()
