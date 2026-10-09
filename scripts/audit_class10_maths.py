import os
import json
import glob

def audit_class10_maths():
    print("=== AUDITING CLASS 10 MATHS ===")
    
    # 1. Check app_core/chapters/
    chapter_files = sorted(glob.glob("app_core/chapters/*class10_maths*.json"))
    print(f"Found {len(chapter_files)} chapter files in app_core/chapters:")
    for f in chapter_files:
        if "BACKUP" in f:
            continue
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
                if isinstance(data, dict) and "blocks" in data:
                    blocks = data["blocks"]
                    is_wrapped = True
                elif isinstance(data, list):
                    blocks = data
                    is_wrapped = False
                else:
                    blocks = []
                    is_wrapped = False
                
                missing_hi = 0
                missing_gu = 0
                for b in blocks:
                    if isinstance(b, dict):
                        # check title/body/question/options/explanation
                        if 'body' in b and 'body_hi' not in b: missing_hi += 1
                        if 'body' in b and 'body_gu' not in b: missing_gu += 1
                        if 'question' in b and 'question_hi' not in b: missing_hi += 1
                        if 'question' in b and 'question_gu' not in b: missing_gu += 1
                        if 'title' in b and 'title_hi' not in b: missing_hi += 1
                        if 'title' in b and 'title_gu' not in b: missing_gu += 1

                print(f"  {os.path.basename(f)}: blocks={len(blocks)}, wrapped={is_wrapped}, missing_hi={missing_hi}, missing_gu={missing_gu}")
        except Exception as e:
            print(f"  {os.path.basename(f)}: ERROR parsing - {e}")

    # 2. Check app_core/learning_modules/
    lm_dirs = sorted(glob.glob("app_core/learning_modules/*class10_maths*"))
    print(f"\nFound {len(lm_dirs)} directories in app_core/learning_modules:")
    for d in lm_dirs:
        blocks_file = os.path.join(d, "blocks.json")
        meta_file = os.path.join(d, "metadata.json")
        has_blocks = os.path.exists(blocks_file)
        has_meta = os.path.exists(meta_file)
        num_blocks = 0
        if has_blocks:
            try:
                with open(blocks_file, 'r', encoding='utf-8') as fp:
                    bdata = json.load(fp)
                    num_blocks = len(bdata) if isinstance(bdata, list) else len(bdata.get("blocks", []))
            except:
                pass
        print(f"  {os.path.basename(d)}: blocks.json={has_blocks} (count={num_blocks}), metadata.json={has_meta}")

    # 3. Check app_core/assessment/
    assess_files = sorted(glob.glob("app_core/assessment/*class10_maths*.json"))
    print(f"\nFound {len(assess_files)} files in app_core/assessment:")
    for f in assess_files:
        try:
            with open(f, 'r', encoding='utf-8') as fp:
                data = json.load(fp)
                questions = data if isinstance(data, list) else data.get("questions", [])
                missing_hi = 0
                missing_gu = 0
                for q in questions:
                    if isinstance(q, dict):
                        if 'question' in q and 'question_hi' not in q: missing_hi += 1
                        if 'question' in q and 'question_gu' not in q: missing_gu += 1
                print(f"  {os.path.basename(f)}: questions={len(questions)}, missing_hi={missing_hi}, missing_gu={missing_gu}")
        except Exception as e:
            print(f"  {os.path.basename(f)}: ERROR - {e}")

if __name__ == "__main__":
    audit_class10_maths()
