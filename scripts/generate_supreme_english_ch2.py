import json
import os

def generate_supreme_english_ch2():
    chapter_id = "ncert_class10_english_ch2"
    title = "Chapter 2: Nelson Mandela: Long Walk to Freedom"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "English",
        "grade": "10",
        "board": "NCERT/CBSE",
        "curriculum": ["Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 120,
        "version": "3.0.0-SUPREME-ENGLISH",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": ["english", "first_flight", "nelson_mandela", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the historical significance of the anti-apartheid movement.",
            "Master the difficult vocabulary (Apartheid, Inauguration, Oppressor).",
            "Analyze Mandela's views on freedom and courage.",
            "Solve CBSE/State Board HOTS questions related to twin obligations."
        ],
        "ai_context": {
            "learning_goal": "Make literature emotional and easy to understand for ESL (English as a Second Language) students. Use Bilingual translations for tough words.",
            "common_misconceptions": [
                "Students think courage is the absence of fear. (Fact: Mandela says it's the triumph over it!).",
                "Students misspell 'Apartheid' and 'Inauguration' in exams."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: INTRODUCTION & HOOK
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine being treated as a criminal in your own country just because of your skin color, and spending 27 years in prison! But when you finally come out, you don't seek revenge; instead, you become the President of a united nation. This is the true, epic story of **Nelson Mandela**. Let's witness history!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Nelson Mandela taking the oath as the first black President of South Africa.",
        "image_url": "assets/images/eng_ch2_mandela_oath.jpg",
        "alt_text": "Nelson Mandela raising his hand taking oath at the Union Buildings."
    })

    # ==========================================
    # MODULE 2: VOCABULARY & TRANSLATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Master These Difficult Words:**\n1. **Apartheid (रंगभेद / રંગભેદ):** A political system that separates people according to their race.\n2. **Inauguration (उद्घाटन / ઉદ્ઘાટન):** A formal ceremony to mark the beginning of a leader's term.\n3. **Oppressor (अत्याचारी / જુલમી):** A person or group that treats people in a cruel and unfair way.\n4. **Resilience (लचीलापन / સ્થિતિસ્થાપકતા):** The ability to deal with any kind of hardship and recover from it.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 3: THE PLOT & SOCRATIC DISCOVERY
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "On 10th May 1994, the world's leaders gathered in Pretoria, South Africa. It was the inauguration of South Africa's first democratic, non-racial government. Mandela took the oath and pledged to liberate all his people from poverty and discrimination.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "South African jets and helicopters flying in formation over the Union Buildings.",
        "image_url": "assets/images/eng_ch2_jets_formation.jpg",
        "alt_text": "Military jets leaving a smoke trail of the new South African flag colors."
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Teacher's Secret:** Pay attention to how Mandela redefines 'Courage'. He says courage is not the *absence* of fear, but the *triumph* over it. The brave man is not he who does not feel afraid, but he who conquers that fear!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 4: TWIN OBLIGATIONS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "Mandela mentions that every man has **Twin Obligations (दो कर्तव्य / બે ફરજો)**:\n1. Obligation to his family, parents, wife, and children.\n2. Obligation to his people, his community, and his country.\n\nIn apartheid South Africa, it was impossible for a black man to fulfill both. If he tried to live as a human being, he was punished and isolated.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 5: BOARD EXAM HOTS
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** What does freedom mean to Mandela at different stages of life?\n\n**Answer Structure:** \n1. **As a boy:** Freedom to run in the fields, swim in the stream, and roast mealies.\n2. **As a student:** Freedom to stay out at night, read what he pleased, and go where he chose.\n3. **As an adult:** He realized his boyhood freedom was an illusion. True freedom meant the freedom of his entire community from oppression.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_english_ch2.json"
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_english_ch2.json"
    final_json["metadata"]["id"] = "gseb_class10_english_ch2"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme English Chapter 2 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_english_ch2()
