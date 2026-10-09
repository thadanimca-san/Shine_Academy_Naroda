import json
import os

def build_ss_all():
    os.makedirs("app_core/chapters", exist_ok=True)
    os.makedirs("app_core/assessment", exist_ok=True)

    ss_titles = {
        1: "Arrival of Europeans to India",
        2: "First World War and Russian Revolution",
        3: "Movement Towards a New World",
        4: "National Movements in India",
        5: "Movement Towards Independence",
        6: "World After 1945",
        7: "Post-Independence India",
        8: "Framing of Constitution and its Features",
        9: "Fundamental Rights, Duties and Directive Principles",
        10: "Organs of Government",
        11: "Judiciary",
        12: "Indian Democracy",
        13: "India: Location, Geological Structure and Physiography - I",
        14: "India: Location, Geological Structure and Physiography - II",
        15: "Drainage System",
        16: "Climate",
        17: "Natural Vegetation",
        18: "Wild Life",
        19: "India: Human Life",
        20: "Disaster Management"
    }

    for ch_num in range(1, 21):
        mod_path = f"app_core/learning_modules/gseb_class9_social_science_ch{ch_num}/blocks.json"
        if not os.path.exists(mod_path):
            print(f"SS Ch {ch_num}: Module file not found at {mod_path}")
            continue

        with open(mod_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        if isinstance(raw_data, dict):
            if "blocks" in raw_data and isinstance(raw_data["blocks"], list):
                blocks = raw_data["blocks"]
                print(f"SS Ch {ch_num:2d}: Unwrapped {{'blocks': [...]}} dict to list ({len(blocks)} blocks).")
            else:
                blocks = [raw_data]
        else:
            blocks = raw_data

        quizzes = []

        for b in blocks:
            if not isinstance(b, dict):
                continue

            # Ensure title trilingual fields
            if "title" in b:
                if "title_hi" not in b or not b["title_hi"]:
                    b["title_hi"] = b["title"]
                if "title_gu" not in b or not b["title_gu"]:
                    b["title_gu"] = b["title"]

            # Ensure body trilingual fields
            body_val = b.get("body") or b.get("text") or b.get("problem") or ""
            if body_val:
                if "body_hi" not in b and "text_hi" not in b and "problem_hi" not in b:
                    b["body_hi"] = body_val
                if "body_gu" not in b and "text_gu" not in b and "problem_gu" not in b:
                    b["body_gu"] = body_val

            # Extract quiz if block type is quiz or mcq
            if b.get("type") in ["quiz", "mcq", "practice_question"]:
                quizzes.append({
                    "id": b.get("id", f"KOBJ_CLASS9_SS_CH{ch_num}_{len(quizzes)+1}"),
                    "question": b.get("question", b.get("title", "")),
                    "question_hi": b.get("question_hi", b.get("title_hi", "")),
                    "question_gu": b.get("question_gu", b.get("title_gu", "")),
                    "options": b.get("options", []),
                    "options_hi": b.get("options_hi", b.get("options", [])),
                    "options_gu": b.get("options_gu", b.get("options", [])),
                    "correct_index": b.get("correct_index", 0),
                    "explanation": b.get("explanation", ""),
                    "explanation_hi": b.get("explanation_hi", b.get("explanation", "")),
                    "explanation_gu": b.get("explanation_gu", b.get("explanation", ""))
                })

        # If no quiz blocks found, create standard chapter assessment quiz
        if not quizzes:
            ch_title = ss_titles.get(ch_num, f"Chapter {ch_num}")
            quizzes.append({
                "id": f"KOBJ_CLASS9_SS_CH{ch_num}_EX1",
                "question": f"Which core historical/geographical topic is covered in Chapter {ch_num}: {ch_title}?",
                "question_hi": f"अध्याय {ch_num}: {ch_title} में किस मुख्य विषय को शामिल किया गया है?",
                "question_gu": f"પ્રકરણ {ch_num}: {ch_title} માં કયા મુખ્ય વિષયનો સમાવેશ કરવામાં આવ્યો છે?",
                "options": [ch_title, "Ancient Civilizations", "World Geography", "None of these"],
                "options_hi": [ch_title, "प्राचीन सभ्यताएं", "विश्व भूगोल", "इनमें से कोई नहीं"],
                "options_gu": [ch_title, "પ્રાચીન સંસ્કૃતિઓ", "વિશ્વ ભૂગોળ", "આમાંથી એક પણ નહીં"],
                "correct_index": 0,
                "explanation": f"Chapter {ch_num} focuses on {ch_title}.",
                "explanation_hi": f"अध्याय {ch_num} {ch_title} पर केंद्रित है।",
                "explanation_gu": f"પ્રકરણ {ch_num} {ch_title} પર ધ્યાન કેન્દ્રિત કરે છે."
            })

        # Save module JSON
        with open(mod_path, "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        # Save NCERT chapter JSON
        ch_file = f"app_core/chapters/ncert_class9_social_science_ch{ch_num}.json"
        with open(ch_file, "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        # Save assessment bank JSON
        assess_file = f"app_core/assessment/gseb_class9_social_science_ch{ch_num}_questions.json"
        with open(assess_file, "w", encoding="utf-8") as f:
            json.dump(quizzes, f, ensure_ascii=False, indent=2)

        print(f"SS Ch {ch_num:2d}: {len(blocks):2d} blocks, {len(quizzes):2d} quizzes synced to learning module, NCERT chapter JSON, and assessment bank.")

if __name__ == "__main__":
    build_ss_all()
