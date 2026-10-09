import os
import json
import glob

def final_audit():
    print("==========================================================")
    print("      FINAL AUDIT REPORT: CLASS 10 MATHEMATICS (CH 1-14)   ")
    print("==========================================================")
    
    total_blocks = 0
    total_questions = 0
    wrapped_files = 0
    missing_hi_count = 0
    missing_gu_count = 0
    
    for ch_num in range(1, 15):
        filename = f"app_core/chapters/ncert_class10_maths_ch{ch_num}.json"
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if isinstance(data, dict):
            wrapped_files += 1
            blocks = data.get("blocks", [])
        else:
            blocks = data
            
        total_blocks += len(blocks)
        
        m_hi = 0
        m_gu = 0
        q_count = 0
        
        for b in blocks:
            for k in ["title", "body", "question", "explanation"]:
                if k in b and f"{k}_hi" not in b: m_hi += 1
                if k in b and f"{k}_gu" not in b: m_gu += 1
            if "options" in b:
                if "options_hi" not in b: m_hi += 1
                if "options_gu" not in b: m_gu += 1
                
            if b.get("type") in ["quiz", "mcq", "practice_question", "challenge_question"] and "question" in b:
                q_count += 1
                
        total_questions += q_count
        missing_hi_count += m_hi
        missing_gu_count += m_gu
        
        print(f"  Ch {ch_num:2d}: {len(blocks):3d} blocks | {q_count:2d} MCQs/Practice | missing_hi={m_hi} | missing_gu={m_gu}")

    print("----------------------------------------------------------")
    print(f"Total Class 10 Maths Chapters: 14 Chapters")
    print(f"Grand Total Learning Blocks  : {total_blocks} Blocks")
    print(f"Grand Total Assessment Qs    : {total_questions} Questions")
    print(f"Wrapped Array Files (Error)  : {wrapped_files}")
    print(f"Total Missing Hindi (_hi)    : {missing_hi_count}")
    print(f"Total Missing Gujarati (_gu) : {missing_gu_count}")
    print("==========================================================")

if __name__ == "__main__":
    final_audit()
