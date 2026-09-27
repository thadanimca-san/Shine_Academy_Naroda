#!/usr/bin/env python3
"""
Shine Academy — Class 6, 7, 8 NCERT/GSEB Science Generator
Generates ALL chapters with full English + Hindi + Gujarati content
following the EduOS 8-Step Gold Learning Cycle.

Each chapter gets ~15-20 blocks:
  Hook → Socratic → Theory → Theory → MCQ → Theory → Theory → MCQ
  → Teacher Tip → Theory → MCQ → Common Mistakes → Summary → MCQ
"""

import json, time, re, os
import google.genai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.5-flash-lite"

OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

# ─── CHAPTER CURRICULUM ──────────────────────────────────────────────────────

CURRICULUM = {
    6: [
        (1,  "Food: Where Does It Come From?",        "food_sources"),
        (2,  "Components of Food",                     "food_components"),
        (3,  "Fibre to Fabric",                        "fibre_fabric"),
        (4,  "Sorting Materials into Groups",          "sorting_materials"),
        (5,  "Separation of Substances",               "separation"),
        (6,  "Changes Around Us",                      "changes"),
        (7,  "Getting to Know Plants",                 "plants"),
        (8,  "Body Movements",                         "body_movements"),
        (9,  "The Living Organisms: Characteristics and Habitats", "living_organisms"),
        (10, "Motion and Measurement of Distances",   "motion_measurement"),
        (11, "Light, Shadows and Reflections",         "light_shadows"),
        (12, "Electricity and Circuits",               "electricity_circuits"),
        (13, "Fun with Magnets",                       "magnets"),
        (14, "Water",                                  "water"),
        (15, "Air Around Us",                          "air"),
        (16, "Garbage In, Garbage Out",               "garbage"),
    ],
    7: [
        (1,  "Nutrition in Plants",                    "nutrition_plants"),
        (2,  "Nutrition in Animals",                   "nutrition_animals"),
        (3,  "Fibre to Fabric",                        "fibre_fabric_7"),
        (4,  "Heat",                                   "heat"),
        (5,  "Acids, Bases and Salts",                 "acids_bases_salts"),
        (6,  "Physical and Chemical Changes",          "physical_chemical_changes"),
        (7,  "Weather, Climate and Adaptations",       "weather_climate"),
        (8,  "Winds, Storms and Cyclones",             "winds_storms"),
        (9,  "Soil",                                   "soil"),
        (10, "Respiration in Organisms",               "respiration"),
        (11, "Transportation in Animals and Plants",   "transportation"),
        (12, "Reproduction in Plants",                 "reproduction_plants"),
        (13, "Motion and Time",                        "motion_time"),
        (14, "Electric Current and its Effects",       "electric_current"),
        (15, "Light",                                  "light_7"),
        (16, "Water: A Precious Resource",             "water_precious"),
        (17, "Forests: Our Lifeline",                  "forests"),
        (18, "Wastewater Story",                       "wastewater"),
    ],
    8: [
        (1,  "Crop Production and Management",         "crop_production"),
        (2,  "Microorganisms: Friend and Foe",         "microorganisms"),
        (3,  "Synthetic Fibres and Plastics",          "synthetic_fibres"),
        (4,  "Materials: Metals and Non-metals",       "metals_nonmetals"),
        (5,  "Coal and Petroleum",                     "coal_petroleum"),
        (6,  "Combustion and Flame",                   "combustion_flame"),
        (7,  "Conservation of Plants and Animals",     "conservation"),
        (8,  "Cell: Structure and Functions",          "cell_structure"),
        (9,  "Reproduction in Animals",                "reproduction_animals"),
        (10, "Reaching the Age of Adolescence",        "adolescence"),
        (11, "Force and Pressure",                     "force_pressure"),
        (12, "Friction",                               "friction"),
        (13, "Sound",                                  "sound"),
        (14, "Chemical Effects of Electric Current",   "chemical_effects"),
        (15, "Some Natural Phenomena",                 "natural_phenomena"),
        (16, "Light",                                  "light_8"),
        (17, "Stars and the Solar System",             "stars_solar"),
        (18, "Pollution of Air and Water",             "pollution"),
    ],
}

# ─── PROMPT ──────────────────────────────────────────────────────────────────

def make_prompt(class_num: int, ch_num: int, title: str, ch_id: str) -> str:
    return f"""You are an expert NCERT Science curriculum designer for Shine Academy Naroda (India).
Generate a COMPLETE, RICH chapter JSON for Class {class_num} NCERT Science — Chapter {ch_num}: "{title}"

CRITICAL RULES:
1. Follow the EduOS 8-Step Gold Learning Cycle: Hook → Socratic → Discovery → Reveal (Theory) → Knowledge Check (MCQ) → Reflection → Connection → Mastery
2. Every block MUST have body/question/options in ENGLISH + HINDI (body_hi) + GUJARATI (body_gu)
3. Use the correct block schema — fields at ROOT level, NOT inside a "content" wrapper
4. Each chapter must have AT LEAST 15 blocks covering all major sub-topics
5. Quiz blocks use "mcq" type with correct_index (integer, 0-based)
6. All explanations must be trilingual
7. Make it feel like sitting with an OUTSTANDING teacher — use analogies, real-life examples, Indian context

EXACT JSON SCHEMA to follow:

{{
  "metadata": {{
    "id": "{ch_id}",
    "title": "{title}",
    "title_hi": "<Hindi translation of title>",
    "title_gu": "<Gujarati translation of title>",
    "subject": "Science",
    "subject_hi": "विज्ञान",
    "subject_gu": "વિજ્ઞાન",
    "grade": "{class_num}",
    "board": "GSEB/NCERT",
    "curriculum": ["GSEB", "NCERT", "CBSE"],
    "difficulty": "Beginner",
    "estimated_minutes": 35,
    "learning_outcomes": ["<outcome 1>", "<outcome 2>", "<outcome 3>"],
    "learning_outcomes_hi": ["<Hindi>", "<Hindi>", "<Hindi>"],
    "learning_outcomes_gu": ["<Gujarati>", "<Gujarati>", "<Gujarati>"],
    "core_concepts": ["<concept1>", "<concept2>"],
    "ai_context": {{
      "learning_goal": "<string>",
      "common_misconceptions": ["<string>"],
      "tutor_hint": "<string>"
    }}
  }},
  "blocks": [
    {{
      "id": "{ch_id}_1",
      "type": "hook",
      "title": "<Curiosity hook title>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Engaging story/mystery/observation to spark curiosity — 3-4 sentences>",
      "body_hi": "<Same in Hindi>",
      "body_gu": "<Same in Gujarati>"
    }},
    {{
      "id": "{ch_id}_2",
      "type": "socratic",
      "title": "<Thinking question title>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<A thought-provoking question based on logic/prediction, NOT factual trivia>",
      "body_hi": "<Same in Hindi>",
      "body_gu": "<Same in Gujarati>"
    }},
    {{
      "id": "{ch_id}_3",
      "type": "theory",
      "title": "<Sub-topic title>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Clear explanation with analogy and Indian context — 4-6 sentences>",
      "body_hi": "<Same in Hindi>",
      "body_gu": "<Same in Gujarati>"
    }},
    {{
      "id": "{ch_id}_4",
      "type": "mcq",
      "title": "<Quiz title>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "question": "<Question based ONLY on what was just taught>",
      "question_hi": "<Hindi>",
      "question_gu": "<Gujarati>",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "options_hi": ["Hindi A", "Hindi B", "Hindi C", "Hindi D"],
      "options_gu": ["Gujarati A", "Gujarati B", "Gujarati C", "Gujarati D"],
      "correct_index": 0,
      "explanation": "<Why the answer is correct — detailed>",
      "explanation_hi": "<Hindi>",
      "explanation_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_5",
      "type": "theory",
      "title": "<Next sub-topic>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Explanation>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_6",
      "type": "teacher_tip",
      "title": "<Tip title>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "tip": "<Helpful teaching tip or memory trick>",
      "tip_hi": "<Hindi>",
      "tip_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_7",
      "type": "theory",
      "title": "<Next sub-topic>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Explanation>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_8",
      "type": "mcq",
      "title": "<Quiz title>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "question": "<Question>",
      "question_hi": "<Hindi>",
      "question_gu": "<Gujarati>",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "options_hi": ["Hindi A", "Hindi B", "Hindi C", "Hindi D"],
      "options_gu": ["Gujarati A", "Gujarati B", "Gujarati C", "Gujarati D"],
      "correct_index": 1,
      "explanation": "<Why correct>",
      "explanation_hi": "<Hindi>",
      "explanation_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_9",
      "type": "theory",
      "title": "<Next sub-topic>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Explanation>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_10",
      "type": "theory",
      "title": "<Next sub-topic>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Explanation>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_11",
      "type": "mcq",
      "title": "<Quiz title>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "question": "<Question>",
      "question_hi": "<Hindi>",
      "question_gu": "<Gujarati>",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "options_hi": ["Hindi A", "Hindi B", "Hindi C", "Hindi D"],
      "options_gu": ["Gujarati A", "Gujarati B", "Gujarati C", "Gujarati D"],
      "correct_index": 2,
      "explanation": "<Why correct>",
      "explanation_hi": "<Hindi>",
      "explanation_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_12",
      "type": "common_mistakes",
      "title": "<Common Mistakes title>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<2-3 common mistakes students make on this topic and how to avoid them>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_13",
      "type": "real_world_example",
      "title": "<Real World title>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<A real-world Indian example that connects the concept to daily life>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_14",
      "type": "mcq",
      "title": "Final Check",
      "title_hi": "अंतिम जांच",
      "title_gu": "અંતિમ તપાસ",
      "question": "<Application-level question>",
      "question_hi": "<Hindi>",
      "question_gu": "<Gujarati>",
      "options": ["Option A", "Option B", "Option C", "Option D"],
      "options_hi": ["Hindi A", "Hindi B", "Hindi C", "Hindi D"],
      "options_gu": ["Gujarati A", "Gujarati B", "Gujarati C", "Gujarati D"],
      "correct_index": 3,
      "explanation": "<Why correct>",
      "explanation_hi": "<Hindi>",
      "explanation_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_15",
      "type": "summary",
      "title": "Chapter Summary",
      "title_hi": "अध्याय सारांश",
      "title_gu": "પ્રકરણ સારાંશ",
      "body": "<Bullet-point summary of all key concepts covered — at least 5 points>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }}
  ]
}}

Generate the COMPLETE chapter for Class {class_num} Science Chapter {ch_num}: "{title}"
Return ONLY valid JSON. No markdown. No explanation. Just the JSON object."""

# ─── GENERATOR ───────────────────────────────────────────────────────────────

def generate_chapter(class_num: int, ch_num: int, title: str, topic_key: str) -> dict | None:
    ch_id = f"gseb_class{class_num}_science_ch{ch_num}"
    prompt = make_prompt(class_num, ch_num, title, ch_id)

    for attempt in range(3):
        try:
            response = client.models.generate_content(model=MODEL, contents=prompt)
            text = response.text.strip()
            text = re.sub(r'^```json\s*', '', text)
            text = re.sub(r'^```\s*', '', text)
            text = re.sub(r'\s*```$', '', text)
            data = json.loads(text.strip())
            # Validate minimum structure
            if "metadata" in data and "blocks" in data and len(data["blocks"]) >= 10:
                return data
            else:
                print(f"    ⚠ Attempt {attempt+1}: insufficient blocks ({len(data.get('blocks',[]))}), retrying...")
        except Exception as e:
            if "429" in str(e) or "quota" in str(e).lower():
                print(f"    ⏳ Rate limit. Waiting 60s...")
                time.sleep(60)
            else:
                print(f"    ⚠ Attempt {attempt+1} error: {str(e)[:100]}")
                time.sleep(5)
    return None

def save_chapter(data: dict, class_num: int, ch_num: int):
    ch_id = f"gseb_class{class_num}_science_ch{ch_num}"
    filepath = os.path.join(OUTPUT_DIR, f"{ch_id}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

def chapter_needs_regen(class_num: int, ch_num: int) -> bool:
    """Returns True if chapter is missing or has no Hindi translations."""
    ch_id = f"gseb_class{class_num}_science_ch{ch_num}"
    filepath = os.path.join(OUTPUT_DIR, f"{ch_id}.json")
    if not os.path.exists(filepath):
        return True
    try:
        with open(filepath) as f:
            data = json.load(f)
        blocks = data.get("blocks", [])
        meta = data.get("metadata", {})
        # Needs regen if: no title_hi, or no blocks with body_hi, or fewer than 8 blocks
        has_title_hi = bool(meta.get("title_hi"))
        has_body_hi = any(b.get("body_hi") or b.get("question_hi") for b in blocks if isinstance(b, dict))
        has_enough = len(blocks) >= 8
        return not (has_title_hi and has_body_hi and has_enough)
    except:
        return True

def main():
    print("=" * 68)
    print(" Shine Academy — Class 6, 7, 8 NCERT Science Generator")
    print(" Generating ALL chapters with English + Hindi + Gujarati")
    print("=" * 68)

    total_done = 0
    total_skip = 0
    total_fail = 0

    for class_num in [6, 7, 8]:
        chapters = CURRICULUM[class_num]
        print(f"\n{'─'*68}")
        print(f"  CLASS {class_num} SCIENCE ({len(chapters)} chapters)")
        print(f"{'─'*68}")

        for ch_num, title, topic_key in chapters:
            ch_id = f"gseb_class{class_num}_science_ch{ch_num}"

            if not chapter_needs_regen(class_num, ch_num):
                print(f"  ✓ Ch{ch_num:02d} — {title[:45]} [SKIP - already good]")
                total_skip += 1
                continue

            print(f"  🔄 Ch{ch_num:02d} — {title[:50]}...")
            data = generate_chapter(class_num, ch_num, title, topic_key)

            if data:
                save_chapter(data, class_num, ch_num)
                blocks = len(data.get("blocks", []))
                hi_count = sum(1 for b in data["blocks"] if isinstance(b, dict) and (b.get("body_hi") or b.get("question_hi")))
                print(f"  ✅ Ch{ch_num:02d} — {title[:45]} [{blocks} blocks, {hi_count} with Hindi]")
                total_done += 1
            else:
                print(f"  ❌ Ch{ch_num:02d} — {title[:45]} [FAILED]")
                total_fail += 1

            time.sleep(3)  # Polite API delay

    print(f"\n{'=' * 68}")
    print(f"  ✅ DONE!")
    print(f"  Generated  : {total_done}")
    print(f"  Skipped    : {total_skip} (already had content)")
    print(f"  Failed     : {total_fail}")
    print(f"{'=' * 68}")

if __name__ == "__main__":
    main()
