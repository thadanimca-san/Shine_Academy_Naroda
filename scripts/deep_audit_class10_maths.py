import os
import json
import glob

def deep_audit():
    print("=== DEEP AUDIT CLASS 10 MATHS ===")
    
    # 1. Inspect app_core/chapters/ncert_class10_maths_ch*.json
    for ch_num in range(1, 16):
        filename = f"app_core/chapters/ncert_class10_maths_ch{ch_num}.json"
        if not os.path.exists(filename):
            print(f"Ch {ch_num}: FILE MISSING ({filename})")
            continue
            
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if isinstance(data, dict):
            blocks = data.get("blocks", [])
            is_wrapped = True
        else:
            blocks = data
            is_wrapped = False
            
        block_types = {}
        missing_hi = 0
        missing_gu = 0
        mcq_count = 0
        socratic_count = 0
        exercise_count = 0
        
        for b in blocks:
            btype = b.get("type", "unknown")
            block_types[btype] = block_types.get(btype, 0) + 1
            
            # Check translation keys
            for key in ["title", "body", "question", "explanation", "tip"]:
                if key in b and f"{key}_hi" not in b:
                    missing_hi += 1
                if key in b and f"{key}_gu" not in b:
                    missing_gu += 1
            if "options" in b:
                if "options_hi" not in b: missing_hi += 1
                if "options_gu" not in b: missing_gu += 1
                
            if btype == "quiz":
                mcq_count += 1
            elif btype == "socratic":
                socratic_count += 1
            elif "exercise" in b.get("id", "").lower() or "ex_" in b.get("id", "").lower() or "practice" in b.get("id", "").lower():
                exercise_count += 1
                
        print(f"Ch {ch_num}: blocks={len(blocks)}, wrapped={is_wrapped}, types={block_types}, missing_hi={missing_hi}, missing_gu={missing_gu}")

if __name__ == "__main__":
    deep_audit()
