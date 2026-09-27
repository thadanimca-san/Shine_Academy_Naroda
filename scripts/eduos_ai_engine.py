import os
import json
import time
from datetime import datetime

try:
    import google.generativeai as genai
except ImportError:
    print("Please install google-generativeai: pip3 install google-generativeai")
    exit(1)

# ==========================================
# EduOS AI Content Engine (Quality First - 2 Chapters/Subject)
# ==========================================

API_KEY = "AIzaSyCXHEJ4KBrebP8ByUEZnVJzuE4u114MGGA"

def extract_json_from_response(text):
    text = text.strip()
    if text.startswith("```json"):
        text = text[7:]
    elif text.startswith("```"):
        text = text[3:]
    if text.endswith("```"):
        text = text[:-3]
    return text.strip()

def generate_toc(model, chapter_id, title, subject, grade):
    prompt = f"""
    You are an expert curriculum designer. 
    I am building a comprehensive textbook replacement chapter for: "{title}" (Subject: {subject}, Grade: {grade}).
    
    Please provide a list of 4 to 6 major sub-topics that MUST be covered to master this chapter completely.
    Return ONLY a valid JSON array of strings representing the sub-topics.
    """
    print(f"   [{chapter_id}] [Stage 1] Generating Table of Contents...")
    response = model.generate_content(prompt)
    json_text = extract_json_from_response(response.text)
    
    try:
        toc = json.loads(json_text)
        if isinstance(toc, list) and len(toc) > 0:
            return toc
        return ["Core Concept", "Key Examples", "Summary"]
    except Exception as e:
        print(f"   [{chapter_id}] ERROR parsing TOC: {e}")
        return ["Core Concept", "Key Examples", "Summary"]

def generate_subtopic_blocks(model, chapter_id, title, subject, grade, subtopic, topic_index):
    prompt = f"""
    You are the Chief Academic Architect of Shine Academy.
    We are writing a massive chapter: "{title}" (Subject: {subject}, Grade: {grade}).
    
    Right now, you are ONLY writing the section for this specific sub-topic: "{subtopic}"
    
    CRITICAL MANDATE: THE 8-STEP SOCRATIC GOLD STANDARD
    Do NOT write a 1-sentence summary. You must teach this specific sub-topic deeply and richly.
    
    PEDAGOGY RULES:
    1. Hook/Intro: Start with a story, analogy, or mystery related to THIS subtopic using a `hook` block.
    2. Socratic Discovery: Ask a predictive question using a `socratic` block.
    3. Discovery/Reveal: A `discovery` or `reveal` block introducing the core concept.
    4. Theory: A `theory` block with a massive paragraph explaining the HOW and WHY.
    5. Knowledge Check: A `knowledge_check` block to verify understanding immediately.
    6. Connection/Reflection: A `connection` or `reflection` block linking it to real life.
    
    The JSON MUST strictly follow this exact structure (NO nested 'content' objects!).
    Return ONLY a valid JSON array of block objects.
    
    [
      {{
        "id": "KOBJ_{topic_index}_1",
        "type": "hook",
        "title": "Hook Title",
        "body": "Interesting story or analogy..."
      }},
      {{
        "id": "KOBJ_{topic_index}_2",
        "type": "socratic",
        "question": "A thought provoking question",
        "options": ["A", "B", "C", "D"],
        "correct_index": 1,
        "explanation": "Explanation here"
      }},
      {{
        "id": "KOBJ_{topic_index}_3",
        "type": "theory",
        "title": "{subtopic}: Deep Dive",
        "body": "A massive, rich, textbook-level paragraph.",
        "bloom": "Understand",
        "difficulty": "Intermediate",
        "estimated_minutes": 5
      }},
      {{
        "id": "KOBJ_{topic_index}_4",
        "type": "knowledge_check",
        "question": "A challenging question based on the theory.",
        "options": ["A", "B", "C", "D"],
        "correct_index": 1,
        "explanation": "Why B is correct.",
        "bloom": "Apply",
        "difficulty": "Intermediate",
        "estimated_minutes": 2
      }}
    ]
    
    CRITICAL: The array MUST have all fields at the ROOT level of each block object. DO NOT put them inside a `content: {{}}` wrapper.
    Return ONLY a valid JSON array.
    """
    
    print(f"   [{chapter_id}] [Stage 2] Generating Subtopic: {subtopic}...")
    response = model.generate_content(prompt)
    json_text = extract_json_from_response(response.text)
    
    try:
        blocks = json.loads(json_text)
        if isinstance(blocks, list):
            return blocks
        return []
    except Exception as e:
        print(f"   [{chapter_id}] ERROR parsing Subtopic blocks: {e}")
        return []

def run_engine():
    genai.configure(api_key=API_KEY)
    
    # We will use gemini-3.5-flash-lite which has higher quotas
    model = genai.GenerativeModel('gemini-3.5-flash-lite')
    
    chapters_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
    os.makedirs(chapters_dir, exist_ok=True)
    
    print("Loading master_curriculum.json...")
    with open("/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json", "r") as f:
        master_data = json.load(f)
        
    # Group and filter targets (Max 2 per subject per grade)
    subject_grade_count = {}
    targets = []
    
    # We sort the keys to ensure consistent ordering
    for ch_id in sorted(master_data.keys()):
        ch_data = master_data[ch_id]
        if not isinstance(ch_data, dict):
            continue
            
        metadata = ch_data.get("metadata", {})
        if "title" in metadata:
            grade = metadata.get("grade", "Unknown")
            subject = metadata.get("subject", "Unknown")
            group_key = f"{grade}_{subject}"
            
            count = subject_grade_count.get(group_key, 0)
            if count < 2:
                targets.append({
                    "id": ch_id,
                    "title": metadata.get("title", "Untitled"),
                    "subject": subject,
                    "grade": grade,
                    "group": group_key
                })
                subject_grade_count[group_key] = count + 1
                
    print(f"Selected {len(targets)} priority chapters (max 2 per subject).")
    
    generated_count = 0
    for ch in targets:
        out_path = os.path.join(chapters_dir, f"{ch['id']}.json")
        
        # We need massive files now. If a file is under 6000 bytes, it's likely a "2 Biscuit" file!
        if os.path.exists(out_path) and os.path.getsize(out_path) > 6000:
            print(f"-> Skipping {ch['id']} (Already fully generated)")
            continue
            
        print(f"\n-> Generating {ch['id']}: {ch['title']} [{ch['group']}]...")
        
        # Robust Retry Loop to handle Google API Rate Limits automatically
        while True:
            try:
                # Stage 1: Get TOC
                toc = generate_toc(model, ch['id'], ch['title'], ch['subject'], ch['grade'])
                print(f"   [{ch['id']}] TOC Identified: {toc}")
                time.sleep(3) # Be polite to API
                
                all_blocks = []
                
                # Stage 2: Loop through TOC
                for index, subtopic in enumerate(toc):
                    blocks = generate_subtopic_blocks(model, ch['id'], ch['title'], ch['subject'], ch['grade'], subtopic, index)
                    if blocks:
                        all_blocks.extend(blocks)
                    time.sleep(5) # Delay between subtopics
                
                # Stage 3: Assembly
                if len(all_blocks) > 0:
                    final_data = {
                        "metadata": {
                            "id": ch['id'],
                            "title": ch['title'],
                            "subject": ch['subject'],
                            "grade": ch['grade'],
                            "difficulty": "Intermediate",
                            "estimated_minutes": 45,
                            "learning_outcomes": toc,
                            "ai_context": {
                                "learning_goal": "Master the complete Gold Standard Pedagogy of this chapter.",
                                "common_misconceptions": []
                            }
                        },
                        "blocks": all_blocks
                    }
                    
                    with open(out_path, 'w', encoding='utf-8') as f:
                        json.dump(final_data, f, indent=2, ensure_ascii=False)
                    print(f"   [SUCCESS] Saved {out_path} (Total Blocks: {len(all_blocks)})")
                    generated_count += 1
                    
                    print("   [Sleeping 12s before next chapter...]")
                    time.sleep(12)
                else:
                    print(f"   [FAILED] Could not generate blocks for {ch['id']}")
                    
                break # Break the retry loop if successful
                
            except Exception as e:
                error_msg = str(e)
                if "429" in error_msg or "Quota" in error_msg:
                    print(f"   [RATE LIMIT HIT] Sleeping for 60 seconds before retrying...")
                    time.sleep(60)
                else:
                    print(f"   [FAILED] Fatal error on {ch['id']}: {e}")
                    time.sleep(10)
                    break # Break if it's not a quota error
                    
    print(f"\n=============================================")
    print(f"BATCH COMPLETE. Generated {generated_count} Gold Standard chapters.")
    print(f"=============================================")

if __name__ == "__main__":
    run_engine()
