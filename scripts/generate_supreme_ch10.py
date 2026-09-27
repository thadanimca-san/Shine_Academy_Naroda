import json
import os

def generate_supreme_chapter_10():
    chapter_id = "ncert_class10_science_ch10"
    title = "Chapter 10: The Human Eye and the Colourful World"
    
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
        "tags": ["physics", "human_eye", "optics", "refraction", "dispersion", "board_special", "bilingual"],
        "learning_outcomes": [
            "Understand the structure and working of the human eye.",
            "Identify defects of vision and their corrections.",
            "Understand the refraction of light through a prism.",
            "Explain dispersion of white light and atmospheric refraction phenomena like the twinkling of stars."
        ],
        "ai_context": {
            "learning_goal": "Transform the student from a beginner to a board-exam topper in Human Eye and the Colourful World. Use the 'Socratic Discovery Arc'.",
            "common_misconceptions": [
                "Students think the pupil is a black object (Fact: It's just a hole).",
                "Students confuse myopia (near-sightedness) with hypermetropia (far-sightedness)."
            ]
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: THE HUMAN EYE
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Have you ever wondered how we can see the beautiful colors of a rainbow or the stars at night? It's all thanks to an incredible natural optical instrument: **The Human Eye (मानव नेत्र / માનવ આંખ)**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The Human Eye works like a camera. Its lens system forms an image on a light-sensitive screen called the retina.",
        "image_url": "assets/images/ch10_human_eye.jpg",
        "alt_text": "Detailed diagram of the Human Eye showing cornea, iris, pupil, lens, and retina."
    })

    blocks.append({
        "type": "theory",
        "content": "**Key Parts of the Eye:**\n- **Cornea (कॉर्निया / કોર્નિયા):** The clear front surface where light enters.\n- **Iris (परितारिका / આઇરિસ):** The colored part that controls the pupil's size.\n- **Pupil (पुतली / કીકી):** The dark center that regulates the amount of light.\n- **Retina (दृष्टिपटल / રેટિના):** The screen at the back containing light-sensitive cells (rods and cones).",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "memory_trick",
        "content": "**Power of Accommodation (समंजन क्षमता):** The ability of the eye lens to adjust its focal length. Ciliary muscles help in this!\n- To see **nearby** objects: Muscles contract, lens thickens.\n- To see **distant** objects: Muscles relax, lens becomes thin.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 2: DEFECTS OF VISION
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**1. Myopia (निकट-दृष्टि दोष / લઘુદ્રષ્ટિની ખામી):** Near-sightedness. Can see near objects clearly but distant objects are blurred. Corrected with a **Concave Lens**.\n\n**2. Hypermetropia (दीर्घ-दृष्टि दोष / ગુરુદ્રષ્ટિની ખામી):** Far-sightedness. Can see distant objects clearly but near objects are blurred. Corrected with a **Convex Lens**.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Why do old people suffer from Presbyopia?\n\n**Answer Structure:** Because of the gradual weakening of the ciliary muscles (पक्ष्माभी पेशियाँ) and diminishing flexibility of the eye lens. It is corrected using bi-focal lenses.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    # ==========================================
    # MODULE 3: REFRACTION THROUGH A PRISM & DISPERSION
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "When white light passes through a glass prism, it splits into seven beautiful colors! This is called Dispersion.",
        "image_url": "assets/images/ch10_prism_dispersion.jpg",
        "alt_text": "White light entering a prism and splitting into a VIBGYOR spectrum."
    })

    blocks.append({
        "type": "theory",
        "content": "**Dispersion of Light (प्रकाश का विक्षेपण / પ્રકાશનું વિભાજન):**\nThe splitting of white light into its component colors (VIBGYOR) is called dispersion.\nRed light bends the least, while Violet light bends the most.\n\n**Rainbow Formation:** Raindrops act like tiny prisms in the sky, refracting, dispersing, and internally reflecting sunlight!",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 4: ATMOSPHERIC REFRACTION
    # ==========================================
    blocks.append({
        "type": "diagram",
        "content": "Why do stars twinkle but planets don't? Why does the sun look oval at sunset? Atmospheric refraction holds the answers!",
        "image_url": "assets/images/ch10_atmospheric_refraction.jpg",
        "alt_text": "Diagram showing the starlight bending as it passes through the Earth's atmosphere."
    })

    blocks.append({
        "type": "theory",
        "content": "**Atmospheric Refraction (वायुमंडलीय अपवर्तन / વાતાવરણીય વક્રીભવન):**\nThe refraction of light by the Earth's atmosphere due to varying optical densities.\n\n**Twinkling of Stars:** The starlight, on entering the earth's atmosphere, undergoes continuous refraction before it reaches the earth. The continuously changing atmosphere causes the light to sometimes reach our eye and sometimes not, causing the twinkling effect.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "Students, always remember that planets are much closer to the earth and are thus seen as extended sources (a collection of many point-sized sources). The total variation in the amount of light entering our eye from all the individual point-sized sources averages out to zero, thereby nullifying the twinkling effect.",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 5: SCATTERING OF LIGHT
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "**Tyndall Effect (टिंडल प्रभाव):** The scattering of a beam of light by colloidal particles.\n\n**Why is the sky blue?** The molecules of air and other fine particles in the atmosphere have size smaller than the wavelength of visible light. They are more effective in scattering light of shorter wavelengths at the blue end than light of longer wavelengths at the red end.",
        "difficulty": "Advanced",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT TOPIC:** Why is the color of the clear sky blue but appears dark to an astronaut?\n**Answer:** Because in space, there is no atmosphere (no particles) to scatter the sunlight. Hence, no scattering occurs and the sky appears dark.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    out_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_science_ch10.json"
    os.makedirs(os.path.dirname(out_path), exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_science_ch10.json"
    final_json["metadata"]["id"] = "gseb_class10_science_ch10"
    with open(gseb_path, "w") as f:
        json.dump(final_json, f, indent=2)
        
    print("Supreme Chapter 10 Generated Successfully!")

if __name__ == "__main__":
    generate_supreme_chapter_10()
