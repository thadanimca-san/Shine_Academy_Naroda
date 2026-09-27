#!/usr/bin/env python3
"""
Fix Abacus and Vedic Maths JSON schemas to match the standard format:
  { "metadata": {...}, "blocks": [...] }

Also adds proper IDs to all blocks.
"""
import json, os, re

CHAPTERS_DIR = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

ABACUS_TITLES = {
    1: ("Introduction to the Abacus", "एबेकस का परिचय", "એબેકસનો પરિચય"),
    2: ("Counting 1 to 9", "1 से 9 तक गिनना", "1 થી 9 ગણવું"),
    3: ("Simple Addition (No Carry)", "सरल जोड़ (कोई कैरी नहीं)", "સાદો સરવાળો (કોઈ ઉપાય નહીં)"),
    4: ("Simple Subtraction", "सरल घटाव", "સાદો બાદ"),
    5: ("Big Friends Concept (+9 to +6)", "बड़े मित्र संकल्पना (+9 से +6)", "મોટા મિત્ર ખ્યાલ (+9 થી +6)"),
}

VEDIC_TITLES = {
    1: ("Introduction to Vedic Mathematics and Core Techniques", "वैदिक गणित का परिचय और मूल तकनीकें", "વૈદિક ગણિતનો પરિચય અને મૂળ તકનીકો"),
    2: ("Nikhilam Sutra: Multiplication Near a Base", "निखिलम सूत्र: आधार के पास गुणा", "નિખિળમ સૂત્ર: આધાર પાસે ગુણાકાર"),
    3: ("Vertically and Crosswise (Urdhva Tiryagbhyam)", "ऊर्ध्व तिर्यग्भ्यां: ऊर्ध्व और तिरछे", "ઊર્ધ્વ તિર્યગ્ભ્યામ: ઊભા અને ત્રાંસા"),
    4: ("Squaring Numbers and Special Cases", "संख्याओं का वर्ग और विशेष प्रकरण", "સંખ્યાઓનો વર્ગ અને ખાસ કિસ્સા"),
    5: ("Division by Vedic Methods (Paravartya Sutra)", "वैदिक विधि से भाग (परावर्त्य सूत्र)", "વૈદિક પ્રણાલીથી ભાગ (પ્રવર્ત્ય સૂત્ર)"),
}


def fix_abacus(ch_num):
    filepath = os.path.join(CHAPTERS_DIR, f"abacus_level1_ch{ch_num}.json")
    if not os.path.exists(filepath):
        print(f"  [SKIP] {filepath} not found")
        return

    d = json.load(open(filepath, encoding="utf-8"))

    # If already in correct format, skip
    if isinstance(d, dict) and "metadata" in d and "blocks" in d:
        print(f"  [OK] abacus ch{ch_num} already in correct format")
        return

    en, hi, gu = ABACUS_TITLES[ch_num]
    blocks = d.get("blocks", [])

    # Fix block IDs if missing
    for i, block in enumerate(blocks):
        if not block.get("id"):
            btype = block.get("type", "block").upper()
            block["id"] = f"ABACUS_L1_CH{ch_num:02d}_{btype}_{i+1:02d}"

    new_doc = {
        "metadata": {
            "id": f"abacus_level1_ch{ch_num}",
            "title": en,
            "title_hi": hi,
            "title_gu": gu,
            "subject": "Abacus",
            "subject_hi": "एबेकस",
            "subject_gu": "એબેકસ",
            "grade": "Class 1-3 (Beginner)",
            "curriculum": "Shine Academy Abacus Program",
            "chapter_number": ch_num,
            "difficulty": "beginner",
            "version": "2.0"
        },
        "blocks": blocks
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(new_doc, f, ensure_ascii=False, indent=2)
    print(f"  [FIXED] abacus ch{ch_num}: {len(blocks)} blocks")


def build_vedic_blocks_from_raw(d, ch_num):
    """Convert raw list/dict vedic data into proper blocks array."""
    en, hi, gu = VEDIC_TITLES[ch_num]
    blocks = []

    if isinstance(d, list):
        # Each item in list might be a section
        for i, item in enumerate(d):
            if not isinstance(item, dict):
                continue

            # Try to extract title + body from various field names
            title = (item.get("title") or item.get("chapter_title") or
                     item.get("section_title") or item.get("step_name") or
                     item.get("step_id") or f"Section {i+1}")
            title_hi = item.get("title_hi") or item.get("chapter_title_hi") or ""
            title_gu = item.get("title_gu") or item.get("chapter_title_gu") or ""

            body = (item.get("body") or item.get("hook") or item.get("content") or
                    item.get("explanation") or item.get("description") or "")
            body_hi = (item.get("body_hi") or item.get("hook_hi") or
                       item.get("content_hi") or "")
            body_gu = (item.get("body_gu") or item.get("hook_gu") or
                       item.get("content_gu") or "")

            block_type = item.get("type", "theory")
            # Map known types
            if item.get("hook") or block_type == "hook":
                block_type = "hook"
            elif "question" in str(item.get("step_id","")).lower():
                block_type = "socratic_question"

            block = {
                "id": f"VEDIC_L1_CH{ch_num:02d}_{block_type.upper()}_{i+1:02d}",
                "type": block_type,
                "title": str(title),
                "title_hi": str(title_hi),
                "title_gu": str(title_gu),
                "body": str(body),
                "body_hi": str(body_hi),
                "body_gu": str(body_gu),
            }

            # Carry over any example/formula/quiz fields
            for key in ["example", "example_hi", "example_gu",
                        "formula", "options", "options_hi", "options_gu",
                        "correct_index", "explanation", "explanation_hi", "explanation_gu"]:
                if key in item:
                    block[key] = item[key]

            blocks.append(block)

    elif isinstance(d, dict):
        # Already has some structure — extract blocks if present
        raw_blocks = d.get("blocks", [])
        if raw_blocks:
            return raw_blocks

        # Otherwise, treat the whole dict as a single theory block
        title = d.get("chapter_title") or d.get("title") or en
        body = d.get("hook") or d.get("body") or d.get("content") or ""
        blocks.append({
            "id": f"VEDIC_L1_CH{ch_num:02d}_THEORY_01",
            "type": "theory",
            "title": str(title),
            "title_hi": d.get("chapter_title_hi", hi),
            "title_gu": d.get("chapter_title_gu", gu),
            "body": str(body),
            "body_hi": d.get("hook_hi", d.get("body_hi", "")),
            "body_gu": d.get("hook_gu", d.get("body_gu", "")),
        })

    return blocks


def fix_vedic(ch_num):
    filepath = os.path.join(CHAPTERS_DIR, f"vedic_maths_level1_ch{ch_num}.json")
    if not os.path.exists(filepath):
        print(f"  [SKIP] {filepath} not found")
        return

    d = json.load(open(filepath, encoding="utf-8"))

    # If already in correct format, skip
    if isinstance(d, dict) and "metadata" in d and "blocks" in d:
        print(f"  [OK] vedic ch{ch_num} already in correct format")
        return

    en, hi, gu = VEDIC_TITLES[ch_num]
    blocks = build_vedic_blocks_from_raw(d, ch_num)

    if not blocks:
        print(f"  [WARN] vedic ch{ch_num}: could not extract any blocks! Raw type={type(d).__name__}")
        return

    new_doc = {
        "metadata": {
            "id": f"vedic_maths_level1_ch{ch_num}",
            "title": en,
            "title_hi": hi,
            "title_gu": gu,
            "subject": "Vedic Maths",
            "subject_hi": "वैदिक गणित",
            "subject_gu": "વૈદિક ગણિત",
            "grade": "Class 5+ (All Ages)",
            "curriculum": "Shine Academy Vedic Maths Program",
            "chapter_number": ch_num,
            "difficulty": "intermediate",
            "version": "2.0"
        },
        "blocks": blocks
    }

    with open(filepath, "w", encoding="utf-8") as f:
        json.dump(new_doc, f, ensure_ascii=False, indent=2)
    print(f"  [FIXED] vedic ch{ch_num}: {len(blocks)} blocks extracted")


if __name__ == "__main__":
    print("=== Fixing Abacus Chapters ===")
    for i in range(1, 6):
        fix_abacus(i)

    print("\n=== Fixing Vedic Maths Chapters ===")
    for i in range(1, 6):
        fix_vedic(i)

    print("\nAll done!")
