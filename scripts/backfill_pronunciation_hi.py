#!/usr/bin/env python3
"""
Backfill script: Add 'pronunciation_hi' (phonetic Devanagari) to all existing
dictionary entries that are missing it.

pronunciation_hi = How the English word SOUNDS written in Hindi/Devanagari script.
Example: "sun" → "सन", "apple" → "एपल", "beautiful" → "ब्यूटीफुल"

Uses Gemini AI in large batches for speed and quality.
"""

import json
import time
import os
import google.generativeai as genai

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"
genai.configure(api_key=API_KEY)
MODEL_NAME = 'gemini-2.0-flash-lite'
model = genai.GenerativeModel(MODEL_NAME)

DICT_FILE = "/home/ubuntu/Shine_Academy_Naroda/app_core/universal_dictionary/generated_massive_dict.json"
BATCH_SIZE = 50  # 50 words per API call — fast and cheap

def get_pronunciation_batch(words: list[str]) -> dict[str, str]:
    """
    Ask Gemini to give phonetic Devanagari pronunciation for a list of English words.
    Returns dict: {english_word: devanagari_pronunciation}
    """
    word_list = "\n".join([f'- "{w}"' for w in words])
    prompt = f"""You are a Hindi phonetics expert helping Indian students pronounce English words.

For each English word below, write how it SOUNDS in Devanagari (Hindi) script.
This is PHONETIC TRANSLITERATION — NOT translation. Write how the word is SPOKEN, not its meaning.

Rules:
- Use proper Hindi vowel sounds: अ, आ, इ, ई, उ, ऊ, ए, ऐ, ओ, औ, अं
- Use ॉ for the "o" sound in words like "school" (स्कूल), "doctor" (डॉक्टर)
- Use ् (halant) for consonant clusters
- Keep it simple so a Class 3 student can read it

Words:
{word_list}

Return ONLY a valid JSON object like this (no markdown, no explanation):
{{
  "sun": "सन",
  "apple": "एपल",
  "beautiful": "ब्यूटीफुल",
  "school": "स्कूल"
}}
"""
    for attempt in range(3):
        try:
            response = model.generate_content(prompt)
            text = response.text.strip()
            if text.startswith("```json"):
                text = text[7:]
            if text.startswith("```"):
                text = text[3:]
            if text.endswith("```"):
                text = text[:-3]
            result = json.loads(text.strip())
            return result
        except Exception as e:
            if "429" in str(e) or "quota" in str(e).lower():
                print(f"  ⏳ Rate limit. Waiting 60s...")
                time.sleep(60)
            else:
                print(f"  ⚠ Attempt {attempt+1} failed: {str(e)[:80]}")
                time.sleep(5)
    return {}

def main():
    print("=" * 65)
    print(" BACKFILL: Adding pronunciation_hi to all dictionary entries")
    print("=" * 65)

    # Load dictionary
    with open(DICT_FILE, "r", encoding="utf-8") as f:
        data = json.load(f)

    terms = data.get("terms", [])
    print(f"  Total entries: {len(terms)}")

    # Find entries missing pronunciation_hi
    missing = [(i, t) for i, t in enumerate(terms) if not t.get("pronunciation_hi")]
    print(f"  Missing pronunciation_hi: {len(missing)}")

    if not missing:
        print("  ✅ All entries already have pronunciation_hi!")
        return

    fixed = 0
    errors = 0
    save_every = 10  # Save every 10 batches

    for batch_start in range(0, len(missing), BATCH_SIZE):
        batch = missing[batch_start:batch_start + BATCH_SIZE]
        batch_num = batch_start // BATCH_SIZE + 1
        total_batches = (len(missing) + BATCH_SIZE - 1) // BATCH_SIZE

        words = [t.get("term", {}).get("english", "") for _, t in batch]
        words = [w for w in words if w]  # filter empty

        print(f"\n  📦 Batch {batch_num}/{total_batches}: {words[:5]}{'...' if len(words) > 5 else ''}")

        pronunciations = get_pronunciation_batch(words)

        for idx, term in batch:
            english = term.get("term", {}).get("english", "").lower()
            pron = pronunciations.get(english) or pronunciations.get(english.capitalize())
            if pron:
                terms[idx]["pronunciation_hi"] = pron
                fixed += 1
            else:
                errors += 1

        # Save periodically
        if batch_num % save_every == 0:
            data["terms"] = terms
            with open(DICT_FILE, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            print(f"  💾 Saved progress. Fixed so far: {fixed}")

        time.sleep(2)  # Polite delay

    # Final save
    data["terms"] = terms
    with open(DICT_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"\n{'=' * 65}")
    print(f"  ✅ DONE!")
    print(f"  pronunciation_hi added: {fixed}")
    print(f"  Words not matched:      {errors}")
    print(f"{'=' * 65}")

if __name__ == "__main__":
    main()
