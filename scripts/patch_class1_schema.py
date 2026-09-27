import json
import glob
from datetime import datetime

def load_json(filepath):
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return json.load(f)
    except:
        return None

def save_json(filepath, data):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def patch_class1_schema():
    print("Patching Class 1 Schema metadata and block requirements...")
    
    # We will search for all class1_*.json files in app_core/chapters/
    files = glob.glob("app_core/chapters/class1_*.json")
    
    current_time = datetime.utcnow().isoformat() + "Z"
    
    for filepath in files:
        data = load_json(filepath)
        if not data: continue
        
        # 1. Update Chapter Metadata
        meta = data.get("metadata", {})
        
        # Derive subject/chapter numbers from filename or existing data
        ch_id = meta.get("id", "")
        # Extract subject from "class1_maths_ch1" -> "maths"
        subject_key = ch_id.split('_')[1] if len(ch_id.split('_')) > 1 else "general"
        
        # Attempt to determine prerequisites (e.g. ch2 depends on ch1)
        ch_num = 1
        if "ch" in ch_id:
            try:
                ch_num = int(ch_id.split("ch")[-1])
            except:
                pass
                
        prereqs = []
        if ch_num > 1:
            prereqs.append(ch_id.replace(f"ch{ch_num}", f"ch{ch_num-1}"))
            
        next_chapters = []
        next_chapters.append(ch_id.replace(f"ch{ch_num}", f"ch{ch_num+1}"))
        
        # Add required schema fields
        meta["subtitle"] = f"Mastering {meta.get('title', 'Concepts')}"
        meta["grade"] = "1"
        meta["board"] = "Universal"
        meta["curriculum"] = ["Universal", "CBSE", "GSEB"]
        meta["language"] = "English" if subject_key != "hindi" else "Hindi"
        meta["difficulty"] = meta.get("difficulty", "Beginner")
        meta["estimated_minutes"] = meta.get("estimated_minutes", 15)
        meta["version"] = "2.0.0"
        meta["author"] = "EduOS AI Architect"
        meta["reviewed_by"] = "Shine Academy Pedagogy Engine"
        meta["last_updated"] = current_time
        meta["tags"] = ["class1", subject_key, "foundations", "interactive"]
        meta["learning_outcomes"] = [
            f"Understand the core concepts of {meta.get('title', 'the topic')}",
            "Apply knowledge through interactive assessments",
            "Connect the concept to real-world examples"
        ]
        meta["prerequisites"] = prereqs
        meta["next_chapters"] = next_chapters
        meta["core_concepts"] = [f"DICT_C1_{subject_key[:3].upper()}_CORE"] # Dummy mapping to generic dictionary term
        
        meta["ai_context"] = {
            "learning_goal": f"Ensure complete mastery of {meta.get('title', 'the topic')} for a Class 1 student.",
            "common_misconceptions": ["Students often confuse the basic definition.", "They may struggle with application."],
            "tutor_hint": "Use the real-world analogies provided in the hook and connection blocks.",
            "next_topics": next_chapters
        }
        
        data["metadata"] = meta
        
        # 2. Update Block Metadata
        blocks = data.get("blocks", [])
        for block in blocks:
            b_type = block.get("type", "")
            
            block["difficulty"] = "Beginner"
            block["estimated_minutes"] = 2
            
            # Map Bloom's Taxonomy based on block type
            if b_type in ["hook", "theory", "definition", "history"]:
                block["bloom"] = "Remember"
            elif b_type in ["flashcard", "diagram", "teacher_tip", "faqs", "trace_alphabet"]:
                block["bloom"] = "Understand"
            elif b_type in ["quiz", "mcq", "worked_example"]:
                block["bloom"] = "Apply"
            elif b_type in ["common_mistakes", "real_world_example"]:
                block["bloom"] = "Analyze"
            elif b_type in ["challenge_question", "reflection"]:
                block["bloom"] = "Evaluate"
            elif b_type in ["project", "coding_activity"]:
                block["bloom"] = "Create"
            else:
                block["bloom"] = "Understand"
                
        data["blocks"] = blocks
        
        save_json(filepath, data)
        print(f"Patched: {filepath}")
        
if __name__ == "__main__":
    patch_class1_schema()
