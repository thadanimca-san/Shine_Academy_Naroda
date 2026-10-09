import json
import os

def fix_and_sync_maths():
    os.makedirs("app_core/chapters", exist_ok=True)
    os.makedirs("app_core/assessment", exist_ok=True)

    for ch_num in range(1, 13):
        mod_path = f"app_core/learning_modules/gseb_class9_maths_ch{ch_num}/blocks.json"
        if not os.path.exists(mod_path):
            print(f"Maths Ch {ch_num}: Module file not found at {mod_path}")
            continue

        with open(mod_path, "r", encoding="utf-8") as f:
            raw_data = json.load(f)

        # Fix root dict issue if present (e.g. Ch 8 {"blocks": [...]})
        if isinstance(raw_data, dict):
            if "blocks" in raw_data and isinstance(raw_data["blocks"], list):
                blocks = raw_data["blocks"]
                print(f"Maths Ch {ch_num}: Unwrapped {{'blocks': [...]}} dict to list ({len(blocks)} blocks).")
            else:
                blocks = [raw_data]
        else:
            blocks = raw_data

        # Ensure all trilingual fields exist across blocks
        missing_hi = 0
        missing_gu = 0
        quizzes = []

        for b in blocks:
            if not isinstance(b, dict):
                continue

            # Check/fill title
            if "title" in b:
                if "title_hi" not in b or not b["title_hi"]:
                    b["title_hi"] = b["title"]
                    missing_hi += 1
                if "title_gu" not in b or not b["title_gu"]:
                    b["title_gu"] = b["title"]
                    missing_gu += 1

            # Check/fill body or text or problem/solution
            body_val = b.get("body") or b.get("text") or b.get("problem") or ""
            if body_val:
                if "body_hi" not in b and "text_hi" not in b and "problem_hi" not in b:
                    b["body_hi"] = body_val
                if "body_gu" not in b and "text_gu" not in b and "problem_gu" not in b:
                    b["body_gu"] = body_val

            # If quiz, extract to assessment bank and ensure options/explanations
            if b.get("type") == "quiz":
                quizzes.append({
                    "id": b.get("id", f"BLK_MATHS_CH{ch_num}_{len(quizzes)+1}"),
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

        # Save fixed module file
        with open(mod_path, "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        # Save synced chapter file
        ch_file = f"app_core/chapters/ncert_class9_maths_ch{ch_num}.json"
        with open(ch_file, "w", encoding="utf-8") as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)

        # Save assessment bank file
        assess_file = f"app_core/assessment/gseb_class9_maths_ch{ch_num}_questions.json"
        with open(assess_file, "w", encoding="utf-8") as f:
            json.dump(quizzes, f, ensure_ascii=False, indent=2)

        print(f"Maths Ch {ch_num:2d}: {len(blocks):2d} blocks, {len(quizzes):2d} quizzes synced to learning module, NCERT chapter JSON, and assessment bank.")

if __name__ == "__main__":
    fix_and_sync_maths()
