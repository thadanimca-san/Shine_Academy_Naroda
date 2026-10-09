import os
import json
import glob

def full_audit():
    print("=" * 70)
    print("   FULL AUDIT: CLASS 9 & 10 ALL SUBJECTS - CLASS/SUBJECT COVERAGE")
    print("=" * 70)
    
    subjects = {
        "class9": {
            "Science": {"prefix": "ncert_class9_science", "expected": 12},
            "Maths": {"prefix": "ncert_class9_maths", "expected": 12},
            "Social Science": {"prefix": "ncert_class9_social_science", "expected": 20},
            "English": {"prefix": "ncert_class9_english", "expected": 10},
        },
        "class10": {
            "Science": {"prefix": "ncert_class10_science", "expected": 13},
            "Maths": {"prefix": "ncert_class10_maths", "expected": 14},
            "Social Science - History": {"prefix": "ncert_class10_history", "expected": 5},
            "Social Science - Civics": {"prefix": "ncert_class10_civics", "expected": 5},
            "Social Science - Geography": {"prefix": "ncert_class10_geography", "expected": 7},
            "Social Science - Economics": {"prefix": "ncert_class10_economics", "expected": 5},
            "English (CBSE - First Flight)": {"prefix": "cbse_class10_english", "expected": 9},
        }
    }
    
    grand_total_blocks = 0
    grand_total_questions = 0
    grand_total_missing_hi = 0
    grand_total_missing_gu = 0
    issues = []
    
    for cls, subj_map in subjects.items():
        print(f"\n--- {cls.upper()} ---")
        for subj_name, info in subj_map.items():
            prefix = info["prefix"]
            expected = info["expected"]
            
            files = sorted(glob.glob(f"app_core/chapters/{prefix}_ch*.json"))
            files = [f for f in files if "BACKUP" not in f and "real_numbers" not in f]
            
            total_blocks = 0
            total_q = 0
            total_hi = 0
            total_gu = 0
            found = len(files)
            
            for fpath in files:
                with open(fpath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                blocks = data if isinstance(data, list) else data.get("blocks", [])
                total_blocks += len(blocks)
                
                for b in blocks:
                    for k in ["title", "body", "question", "explanation"]:
                        if k in b and f"{k}_hi" not in b: total_hi += 1
                        if k in b and f"{k}_gu" not in b: total_gu += 1
                    if "options" in b:
                        if "options_hi" not in b: total_hi += 1
                        if "options_gu" not in b: total_gu += 1
                    if b.get("type") in ["quiz", "mcq", "practice_question", "challenge_question"] and "question" in b:
                        total_q += 1
            
            grand_total_blocks += total_blocks
            grand_total_questions += total_q
            grand_total_missing_hi += total_hi
            grand_total_missing_gu += total_gu
            
            status = "✅" if found >= expected and total_hi == 0 and total_gu == 0 else "❌"
            print(f"  {status} {subj_name}: {found}/{expected} chapters | {total_blocks} blocks | {total_q} MCQs | hi_missing={total_hi} | gu_missing={total_gu}")
            
            if found < expected:
                issues.append(f"MISSING CHAPTERS: {subj_name} has {found}/{expected} chapters (prefix: {prefix})")
            if total_hi > 0:
                issues.append(f"MISSING HINDI: {subj_name} has {total_hi} blocks missing _hi")
            if total_gu > 0:
                issues.append(f"MISSING GUJARATI: {subj_name} has {total_gu} blocks missing _gu")
    
    print("\n" + "=" * 70)
    print(f"  Grand Total Blocks        : {grand_total_blocks}")
    print(f"  Grand Total MCQs/Questions: {grand_total_questions}")
    print(f"  Total Missing _hi         : {grand_total_missing_hi}")
    print(f"  Total Missing _gu         : {grand_total_missing_gu}")
    print("=" * 70)
    
    if issues:
        print("\n⚠️  ISSUES FOUND:")
        for issue in issues:
            print(f"  - {issue}")
    else:
        print("\n✅  ALL CLEAR — No issues found!")
    
    return issues

if __name__ == "__main__":
    full_audit()
