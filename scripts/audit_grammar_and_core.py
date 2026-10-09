import os
import json

def audit():
    print("======================================================================")
    print("  AUDITING CLASS 9 & 10 ENGLISH GRAMMAR & CORE CONCEPTS")
    print("======================================================================")

    # 1. Grammar Chapters check
    c9_g = [f"ncert_class9_grammar_ch{i}.json" for i in range(1, 11)]
    c10_g = [f"ncert_class10_grammar_ch{i}.json" for i in range(1, 11)]

    all_grammar = c9_g + c10_g
    missing_files = []
    wrapped_files = []
    missing_hi = 0
    missing_gu = 0
    total_blocks = 0
    total_mcqs = 0

    for gf in all_grammar:
        ch_path = f"app_core/chapters/{gf}"
        if not os.path.exists(ch_path):
            missing_files.append(ch_path)
            continue
        
        with open(ch_path, "r", encoding="utf-8") as f:
            data = json.load(f)

        if isinstance(data, dict):
            wrapped_files.append(gf)
            blocks = data.get("blocks", [])
        else:
            blocks = data

        total_blocks += len(blocks)
        for b in blocks:
            # Check fields
            if "title" in b and "title_hi" not in b:
                missing_hi += 1
            if "title" in b and "title_gu" not in b:
                missing_gu += 1
            if "body" in b and "body_hi" not in b:
                missing_hi += 1
            if "body" in b and "body_gu" not in b:
                missing_gu += 1
            if "question" in b and "question_hi" not in b:
                missing_hi += 1
            if "question" in b and "question_gu" not in b:
                missing_gu += 1

        # Check assessment file
        q_path = f"app_core/assessment/{gf.replace('.json', '')}_questions.json"
        if os.path.exists(q_path):
            with open(q_path, "r", encoding="utf-8") as f:
                qs = json.load(f)
                total_mcqs += len(qs)

    print(f"\n--- GRAMMAR AUDIT RESULTS ---")
    print(f"Total Grammar Chapters Checked : {len(all_grammar)}")
    print(f"Missing Files                   : {len(missing_files)}")
    print(f"Wrapped Dictionary Files        : {len(wrapped_files)}")
    print(f"Total Learning Blocks           : {total_blocks}")
    print(f"Total Assessment MCQs           : {total_mcqs}")
    print(f"Missing Hindi (_hi) Fields      : {missing_hi}")
    print(f"Missing Gujarati (_gu) Fields   : {missing_gu}")

    # 2. Curriculum Mapping check
    print(f"\n--- CURRICULUM BOLD BOOK NAME AUDIT ---")
    curricula = ["ncert_class9.json", "cbse_class9.json", "gseb_class9.json", "ncert_class10.json", "cbse_class10.json", "gseb_class10.json"]
    for cname in curricula:
        cpath = f"app_core/curriculum/{cname}"
        if os.path.exists(cpath):
            with open(cpath, "r", encoding="utf-8") as f:
                cdata = json.load(f)
            subjs = cdata.get("subjects", [])
            print(f"\nCurriculum File: {cname}")
            for s in subjs:
                sname = s.get("name", "")
                ch_count = len(s.get("chapters", []))
                print(f"  - Subject: {sname} ({ch_count} chapters)")

if __name__ == "__main__":
    audit()
