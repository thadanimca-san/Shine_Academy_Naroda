#!/usr/bin/env python3
"""
Shine Academy — Class 6, 7, 8 NCERT/CBSE Maths Generator
Generates ALL chapters with full English + Hindi + Gujarati content
following the EduOS 8-Step Gold Learning Cycle.

Maths-specific additions over the Science generator:
  - Worked examples with step-by-step solutions (trilingual)
  - Formula blocks
  - Memory trick blocks for formulas/rules
"""

import json, time, re, os
import google.genai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.5-flash-lite"

OUTPUT_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

# ─── CURRICULUM ──────────────────────────────────────────────────────────────

CURRICULUM = {
    6: [
        (1,  "Knowing Our Numbers"),
        (2,  "Whole Numbers"),
        (3,  "Playing with Numbers"),
        (4,  "Basic Geometrical Ideas"),
        (5,  "Understanding Elementary Shapes"),
        (6,  "Integers"),
        (7,  "Fractions"),
        (8,  "Decimals"),
        (9,  "Data Handling"),
        (10, "Mensuration"),
        (11, "Algebra"),
        (12, "Ratio and Proportion"),
        (13, "Symmetry"),
        (14, "Practical Geometry"),
    ],
    7: [
        (1,  "Integers"),
        (2,  "Fractions and Decimals"),
        (3,  "Data Handling"),
        (4,  "Simple Equations"),
        (5,  "Lines and Angles"),
        (6,  "The Triangle and its Properties"),
        (7,  "Congruence of Triangles"),
        (8,  "Comparing Quantities"),
        (9,  "Rational Numbers"),
        (10, "Practical Geometry"),
        (11, "Perimeter and Area"),
        (12, "Algebraic Expressions"),
        (13, "Exponents and Powers"),
        (14, "Symmetry"),
        (15, "Visualising Solid Shapes"),
    ],
    8: [
        (1,  "Rational Numbers"),
        (2,  "Linear Equations in One Variable"),
        (3,  "Understanding Quadrilaterals"),
        (4,  "Practical Geometry"),
        (5,  "Data Handling"),
        (6,  "Squares and Square Roots"),
        (7,  "Cubes and Cube Roots"),
        (8,  "Comparing Quantities"),
        (9,  "Algebraic Expressions and Identities"),
        (10, "Visualising Solid Shapes"),
        (11, "Mensuration"),
        (12, "Exponents and Powers"),
        (13, "Direct and Inverse Proportions"),
        (14, "Factorisation"),
        (15, "Introduction to Graphs"),
        (16, "Playing with Numbers"),
    ],
}

# ─── PROMPT ──────────────────────────────────────────────────────────────────

def make_prompt(class_num: int, ch_num: int, title: str, ch_id: str) -> str:
    return f"""You are an expert NCERT Mathematics curriculum designer for Shine Academy Naroda (India).
Generate a COMPLETE, RICH chapter JSON for Class {class_num} NCERT Maths — Chapter {ch_num}: "{title}"

CRITICAL RULES:
1. Follow the EduOS 8-Step Learning Cycle: Hook → Socratic → Theory → Worked Example → MCQ → Formula/Tip → Theory → MCQ → Common Mistakes → Summary
2. Every block MUST have English + Hindi (body_hi/question_hi) + Gujarati (body_gu/question_gu) — AT EVERY FIELD
3. Fields at ROOT level — NEVER inside a "content" wrapper
4. At least 15 blocks covering all key sub-topics of this chapter
5. For MATHS: Include worked_example blocks showing step-by-step solutions in all 3 languages
6. Quiz (mcq type) uses correct_index as integer (0-based)
7. Use Indian context: prices in rupees, cricket scores, market examples, festivals
8. Make it feel like an OUTSTANDING maths teacher explaining with patience and clarity

Return this EXACT JSON structure (fill all placeholders with real content for "{title}"):

{{
  "metadata": {{
    "id": "{ch_id}",
    "title": "{title}",
    "title_hi": "<Hindi title>",
    "title_gu": "<Gujarati title>",
    "subject": "Mathematics",
    "subject_hi": "गणित",
    "subject_gu": "ગણિત",
    "grade": "{class_num}",
    "board": "CBSE/NCERT",
    "curriculum": ["CBSE", "NCERT", "GSEB"],
    "difficulty": "Beginner",
    "estimated_minutes": 40,
    "learning_outcomes": ["<outcome1>", "<outcome2>", "<outcome3>"],
    "learning_outcomes_hi": ["<Hindi1>", "<Hindi2>", "<Hindi3>"],
    "learning_outcomes_gu": ["<Gu1>", "<Gu2>", "<Gu3>"],
    "core_concepts": ["<concept1>", "<concept2>", "<concept3>"],
    "ai_context": {{
      "learning_goal": "<string>",
      "common_misconceptions": ["<string>", "<string>"],
      "tutor_hint": "<string>"
    }}
  }},
  "blocks": [
    {{
      "id": "{ch_id}_1",
      "type": "hook",
      "title": "<Curiosity hook>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Real-life story or puzzle that makes students WANT to learn this topic — 3-4 sentences with Indian context>",
      "body_hi": "<Same in Hindi>",
      "body_gu": "<Same in Gujarati>"
    }},
    {{
      "id": "{ch_id}_2",
      "type": "socratic",
      "title": "<Think About It>",
      "title_hi": "सोचो और बताओ",
      "title_gu": "વિચારો અને કહો",
      "body": "<A prediction/logic question students can answer using common sense — NOT a factual trivia question>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_3",
      "type": "theory",
      "title": "<First concept title>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Clear explanation of the first key concept with analogy — 4-6 sentences>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_4",
      "type": "worked_example",
      "title": "<Worked Example 1>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Step-by-step solved example with clear numbered steps. Use Indian context (₹, cricket, market).>",
      "body_hi": "<Same steps in Hindi>",
      "body_gu": "<Same steps in Gujarati>"
    }},
    {{
      "id": "{ch_id}_5",
      "type": "mcq",
      "title": "<Quick Check 1>",
      "title_hi": "त्वरित जांच 1",
      "title_gu": "ઝડપી તપાસ 1",
      "question": "<Question testing the concept just taught>",
      "question_hi": "<Hindi>",
      "question_gu": "<Gujarati>",
      "options": ["<A>", "<B>", "<C>", "<D>"],
      "options_hi": ["<Hindi A>", "<Hindi B>", "<Hindi C>", "<Hindi D>"],
      "options_gu": ["<Gu A>", "<Gu B>", "<Gu C>", "<Gu D>"],
      "correct_index": 0,
      "explanation": "<Why correct — step-by-step if needed>",
      "explanation_hi": "<Hindi>",
      "explanation_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_6",
      "type": "theory",
      "title": "<Second concept>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Next important concept explained clearly>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_7",
      "type": "memory_trick",
      "title": "<Formula/Memory Trick>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<A memorable trick, rhyme, or shortcut to remember a formula or rule>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_8",
      "type": "worked_example",
      "title": "<Worked Example 2>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Another step-by-step solved example on second concept>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_9",
      "type": "mcq",
      "title": "<Quick Check 2>",
      "title_hi": "त्वरित जांच 2",
      "title_gu": "ઝડપી તપાસ 2",
      "question": "<Question on second concept>",
      "question_hi": "<Hindi>",
      "question_gu": "<Gujarati>",
      "options": ["<A>", "<B>", "<C>", "<D>"],
      "options_hi": ["<Hindi A>", "<Hindi B>", "<Hindi C>", "<Hindi D>"],
      "options_gu": ["<Gu A>", "<Gu B>", "<Gu C>", "<Gu D>"],
      "correct_index": 1,
      "explanation": "<Why correct>",
      "explanation_hi": "<Hindi>",
      "explanation_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_10",
      "type": "theory",
      "title": "<Third concept>",
      "title_hi": "<Hindi>",
      "title_gu": "<Gujarati>",
      "body": "<Third key concept of this chapter>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_11",
      "type": "teacher_tip",
      "title": "<Teacher Tip>",
      "title_hi": "शिक्षक सुझाव",
      "title_gu": "શિક્ષક સૂચન",
      "tip": "<A powerful tip that helps students avoid common errors or solve problems faster>",
      "tip_hi": "<Hindi>",
      "tip_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_12",
      "type": "mcq",
      "title": "<Quick Check 3>",
      "title_hi": "त्वरित जांच 3",
      "title_gu": "ઝડપી તપાસ 3",
      "question": "<Application-level question combining concepts>",
      "question_hi": "<Hindi>",
      "question_gu": "<Gujarati>",
      "options": ["<A>", "<B>", "<C>", "<D>"],
      "options_hi": ["<Hindi A>", "<Hindi B>", "<Hindi C>", "<Hindi D>"],
      "options_gu": ["<Gu A>", "<Gu B>", "<Gu C>", "<Gu D>"],
      "correct_index": 2,
      "explanation": "<Detailed explanation>",
      "explanation_hi": "<Hindi>",
      "explanation_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_13",
      "type": "common_mistakes",
      "title": "Common Mistakes",
      "title_hi": "सामान्य गलतियाँ",
      "title_gu": "સામાન્ય ભૂલો",
      "body": "<3 specific common mistakes students make in this chapter + how to fix each one>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_14",
      "type": "mcq",
      "title": "Challenge Question",
      "title_hi": "चुनौती प्रश्न",
      "title_gu": "પડકારજનક પ્રશ્ન",
      "question": "<A slightly harder HOTS-level question>",
      "question_hi": "<Hindi>",
      "question_gu": "<Gujarati>",
      "options": ["<A>", "<B>", "<C>", "<D>"],
      "options_hi": ["<Hindi A>", "<Hindi B>", "<Hindi C>", "<Hindi D>"],
      "options_gu": ["<Gu A>", "<Gu B>", "<Gu C>", "<Gu D>"],
      "correct_index": 3,
      "explanation": "<Detailed solution>",
      "explanation_hi": "<Hindi>",
      "explanation_gu": "<Gujarati>"
    }},
    {{
      "id": "{ch_id}_15",
      "type": "summary",
      "title": "Chapter Summary",
      "title_hi": "अध्याय सारांश",
      "title_gu": "પ્રકરણ સારાંશ",
      "body": "<Complete bullet-point summary: all key concepts, formulas, and rules covered — minimum 6 points>",
      "body_hi": "<Hindi>",
      "body_gu": "<Gujarati>"
    }}
  ]
}}

Generate the COMPLETE, fully trilingual chapter for Class {class_num} Maths Chapter {ch_num}: "{title}"
Return ONLY valid JSON. No markdown fences. No explanation. Just the JSON object."""


# ─── GENERATOR ───────────────────────────────────────────────────────────────

def generate_chapter(class_num: int, ch_num: int, title: str) -> dict | None:
    ch_id = f"cbse_class{class_num}_maths_ch{ch_num}"
    prompt = make_prompt(class_num, ch_num, title, ch_id)

    for attempt in range(3):
        try:
            response = client.models.generate_content(model=MODEL, contents=prompt)
            text = response.text.strip()
            text = re.sub(r'^```json\s*', '', text)
            text = re.sub(r'^```\s*', '', text)
            text = re.sub(r'\s*```$', '', text)
            data = json.loads(text.strip())
            if "metadata" in data and "blocks" in data and len(data["blocks"]) >= 10:
                return data
            else:
                print(f"    ⚠ Attempt {attempt+1}: only {len(data.get('blocks',[]))} blocks, retrying...")
                time.sleep(3)
        except Exception as e:
            if "429" in str(e) or "quota" in str(e).lower():
                print(f"    ⏳ Rate limit. Waiting 60s...")
                time.sleep(60)
            else:
                print(f"    ⚠ Attempt {attempt+1}: {str(e)[:100]}")
                time.sleep(5)
    return None


def save_chapter(data: dict, class_num: int, ch_num: int):
    ch_id = f"cbse_class{class_num}_maths_ch{ch_num}"
    filepath = os.path.join(OUTPUT_DIR, f"{ch_id}.json")
    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def chapter_needs_regen(class_num: int, ch_num: int) -> bool:
    ch_id = f"cbse_class{class_num}_maths_ch{ch_num}"
    filepath = os.path.join(OUTPUT_DIR, f"{ch_id}.json")
    if not os.path.exists(filepath):
        return True
    try:
        with open(filepath) as f:
            data = json.load(f)
        blocks = data.get("blocks", [])
        if not isinstance(blocks, list) or len(blocks) < 8:
            return True
        meta = data.get("metadata", {})
        has_title_hi = bool(meta.get("title_hi"))
        has_body_hi = any(isinstance(b, dict) and (b.get("body_hi") or b.get("question_hi"))
                          for b in blocks)
        return not (has_title_hi and has_body_hi)
    except:
        return True


def main():
    print("=" * 68)
    print(" Shine Academy — Class 6, 7, 8 NCERT/CBSE Maths Generator")
    print(" Generating ALL chapters: English + Hindi + Gujarati")
    print("=" * 68)

    total_done = total_skip = total_fail = 0

    for class_num in [6, 7, 8]:
        chapters = CURRICULUM[class_num]
        print(f"\n{'─'*68}")
        print(f"  CLASS {class_num} MATHS ({len(chapters)} chapters)")
        print(f"{'─'*68}")

        for ch_num, title in chapters:
            if not chapter_needs_regen(class_num, ch_num):
                print(f"  ✓ Ch{ch_num:02d} — {title[:50]} [SKIP]")
                total_skip += 1
                continue

            print(f"  🔄 Ch{ch_num:02d} — {title[:55]}...")
            data = generate_chapter(class_num, ch_num, title)

            if data:
                save_chapter(data, class_num, ch_num)
                blocks = len(data.get("blocks", []))
                hi = sum(1 for b in data["blocks"]
                         if isinstance(b, dict) and (b.get("body_hi") or b.get("question_hi")))
                print(f"  ✅ Ch{ch_num:02d} — {title[:50]} [{blocks} blocks, {hi} with Hindi]")
                total_done += 1
            else:
                print(f"  ❌ Ch{ch_num:02d} — {title[:50]} [FAILED]")
                total_fail += 1

            time.sleep(3)

    print(f"\n{'=' * 68}")
    print(f"  ✅ COMPLETE!")
    print(f"  Generated : {total_done}")
    print(f"  Skipped   : {total_skip}")
    print(f"  Failed    : {total_fail}")
    print(f"{'=' * 68}")


if __name__ == "__main__":
    main()
