#!/usr/bin/env python3
"""
Smart dictionary cleaner + pronunciation_hi backfiller.

Step 1: Fix corrupted words where 'n' was accidentally prepended.
Step 2: Add pronunciation_hi (phonetic Devanagari) to every entry missing it.

Uses google.genai (new SDK) for Gemini API calls.
"""

import json
import time
import re
import os
import google.genai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
client = genai.Client(api_key=API_KEY)
MODEL = "gemini-3.5-flash-lite"

DICT_FILE = "/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary/generated_massive_dict.json"
BATCH_SIZE = 50

# ─── STEP 1: DETECT & FIX CORRUPTED WORDS ────────────────────────────────────

def is_corrupted_n_word(term_obj: dict) -> tuple:
    """
    Returns (is_corrupted, fixed_word).
    A word is corrupted if it starts with 'n' AND the ID shows the 'n' was
    prepended accidentally.
    e.g., 'nbulbs' with id DICT_ENG_NBULBS → should be 'bulbs'
    """
    eng = term_obj.get("term", {}).get("english", "")
    tid = term_obj.get("id", "")

    if not eng.startswith("n") or len(eng) < 3:
        return False, eng

    without_n = eng[1:]

    # Extract the word part from ID (after last underscore)
    id_word_part = tid.upper().split("_")[-1] if "_" in tid else tid.upper()

    # Corrupted if: ID word part starts with N, but without_n doesn't start with N
    # and without_n is a clean alphabetic word
    without_n_upper = without_n.upper()
    if (id_word_part.startswith("N") and
            not without_n_upper.startswith("N") and
            len(without_n) >= 3 and
            re.match(r'^[a-zA-Z]+$', without_n)):
        return True, without_n

    return False, eng


def fix_corrupted_words(terms: list) -> tuple:
    """Fix all n-prefixed corrupted words. Returns (fixed_terms, count_fixed)."""
    fixed_count = 0

    for i, term in enumerate(terms):
        is_bad, fixed_word = is_corrupted_n_word(term)
        if is_bad:
            original = term["term"]["english"]
            term["term"]["english"] = fixed_word
            old_id = term.get("id", "")
            term["id"] = f"DICT_ENG_{fixed_word.upper()}"
            fixed_count += 1
            if fixed_count <= 20:
                print(f"  ✔ Fixed: '{original}' → '{fixed_word}'  (was: {old_id})")

    print(f"\n  Total corrupted words fixed: {fixed_count}")

    # Remove duplicates (same English word appearing twice after fixing)
    seen = set()
    clean_terms = []
    dupes = 0
    for term in terms:
        eng = term.get("term", {}).get("english", "").lower().strip()
        if not eng:
            continue
        if eng in seen:
            dupes += 1
            continue
        seen.add(eng)
        clean_terms.append(term)

    print(f"  Duplicate entries removed : {dupes}")
    print(f"  Clean entries remaining   : {len(clean_terms)}")
    return clean_terms, fixed_count


# ─── STEP 2: ADD pronunciation_hi ────────────────────────────────────────────

def get_pronunciation_batch(words: list) -> dict:
    """Get phonetic Devanagari for a batch of English words via Gemini."""
    word_list = "\n".join([f'- "{w}"' for w in words])
    prompt = f"""You are a Hindi phonetics expert helping Indian students pronounce English words.

For each English word below, write how it SOUNDS in Devanagari (Hindi) script.
This is PHONETIC TRANSLITERATION — NOT translation. Write how the word is SPOKEN, not its meaning.

Rules:
- Use ॉ for short "o" as in doctor=डॉक्टर, school=स्कूल
- Use ् (halant) for consonant clusters: street=स्ट्रीट
- Use correct vowels: अ आ इ ई उ ऊ ए ऐ ओ औ
- Keep it readable for a Class 3 student

Words:
{word_list}

Return ONLY a compact valid JSON object — no markdown, no explanation:
{{"word1": "देवनागरी1", "word2": "देवनागरी2"}}"""

    for attempt in range(3):
        try:
            response = client.models.generate_content(
                model=MODEL,
                contents=prompt
            )
            text = response.text.strip()
            text = re.sub(r'^```json\s*', '', text)
            text = re.sub(r'^```\s*', '', text)
            text = re.sub(r'\s*```$', '', text)
            return json.loads(text.strip())
        except Exception as e:
            if "429" in str(e) or "quota" in str(e).lower():
                print(f"    ⏳ Rate limit. Waiting 60s...")
                time.sleep(60)
            else:
                print(f"    ⚠ Attempt {attempt+1}: {str(e)[:80]}")
                time.sleep(5)
    return {}


def backfill_pronunciation(terms: list) -> int:
    """Add pronunciation_hi to all entries missing it. Returns count added."""
    missing = [(i, t) for i, t in enumerate(terms) if not t.get("pronunciation_hi")]
    total_missing = len(missing)
    print(f"\n  Entries needing pronunciation_hi: {total_missing}")

    if total_missing == 0:
        print("  ✅ All entries already have pronunciation_hi!")
        return 0

    added = 0
    total_batches = (total_missing + BATCH_SIZE - 1) // BATCH_SIZE

    for batch_num, batch_start in enumerate(range(0, total_missing, BATCH_SIZE), 1):
        batch = missing[batch_start:batch_start + BATCH_SIZE]
        words = [t.get("term", {}).get("english", "") for _, t in batch]
        words = [w for w in words if w]

        pct = (batch_start / total_missing) * 100
        print(f"  📦 Batch {batch_num}/{total_batches} ({pct:.0f}%) — {words[:3]}...")

        pronunciations = get_pronunciation_batch(words)

        for idx, term in batch:
            eng = term.get("term", {}).get("english", "")
            pron = (pronunciations.get(eng) or
                    pronunciations.get(eng.lower()) or
                    pronunciations.get(eng.capitalize()))
            if pron:
                terms[idx]["pronunciation_hi"] = pron
                added += 1

        # Save every 20 batches (~1000 words)
        if batch_num % 20 == 0:
            _save(terms)
            print(f"    💾 Progress saved. Added so far: {added}")

        time.sleep(1.5)

    return added


def _save(terms):
    with open(DICT_FILE, "w", encoding="utf-8") as f:
        json.dump({"terms": terms}, f, ensure_ascii=False, indent=2)


def main():
    print("=" * 65)
    print(" Shine Academy — Dictionary Fixer + Pronunciation Adder")
    print("=" * 65)

    print("\n📖 Loading dictionary...")
    with open(DICT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)
    terms = data.get("terms", [])
    print(f"  Loaded {len(terms)} entries")

    # STEP 1: Fix corrupted words
    print("\n" + "─" * 65)
    print("  STEP 1: Fixing n-prefixed corrupted words...")
    print("─" * 65)
    terms, fixed_count = fix_corrupted_words(terms)
    _save(terms)
    print(f"  💾 Saved after word fixes.")

    # STEP 2: Add pronunciation_hi
    print("\n" + "─" * 65)
    print("  STEP 2: Adding pronunciation_hi to all entries...")
    print("─" * 65)
    added = backfill_pronunciation(terms)

    # Final save
    _save(terms)

    print("\n" + "=" * 65)
    print("  ✅ ALL DONE!")
    print(f"  Corrupted words fixed  : {fixed_count}")
    print(f"  pronunciation_hi added : {added}")
    print(f"  Total clean entries    : {len(terms)}")
    print("=" * 65)


if __name__ == "__main__":
    main()
