import json
import os

base_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules"

chapters = [
    {"id": "gseb_class8_science_ch1", "number": 1, "title": "Exploring the Investigative World of Science"},
    {"id": "gseb_class8_science_ch2", "number": 2, "title": "The Invisible Living World"},
    {"id": "gseb_class8_science_ch3", "number": 3, "title": "Health: The Ultimate Treasure"},
    {"id": "gseb_class8_science_ch4", "number": 4, "title": "Electricity: Magnetic and Heating Effects"},
    {"id": "gseb_class8_science_ch5", "number": 5, "title": "Exploring Forces"},
    {"id": "gseb_class8_science_ch6", "number": 6, "title": "Pressure, Winds, Storms, and Cyclones"},
    {"id": "gseb_class8_science_ch7", "number": 7, "title": "Particulate Nature of Matter"}
]

# Create manifest
manifest_path = os.path.join(base_dir, "gseb_class8_science_chapters.json")
manifest = {
  "subject": "Science",
  "grade": 8,
  "board": "GSEB",
  "language": "en",
  "chapters": []
}

for ch in chapters:
    manifest["chapters"].append({
        "id": ch["id"],
        "number": ch["number"],
        "title": ch["title"],
        "route": f"/learning_engine/{ch['id']}"
    })
    
    # Create directory if it doesn't exist
    ch_dir = os.path.join(base_dir, ch["id"])
    os.makedirs(ch_dir, exist_ok=True)
    
    # Create metadata.json for the chapter
    metadata = {
      "id": ch["id"],
      "title": ch["title"],
      "subtitle": f"Class 8 Science - Chapter {ch['number']}",
      "subject": "Science",
      "grade": 8,
      "board": "GSEB",
      "curriculum": ["GSEB", "CBSE"],
      "language": "English",
      "difficulty": "Intermediate",
      "estimated_minutes": 120,
      "version": "1.0.0",
      "author": "Shine Academy Pedagogy Team",
      "reviewed_by": "Chief Architect",
      "last_updated": "2026-08-08T00:00:00Z",
      "tags": ["Science", "Class 8"],
      "learning_outcomes": ["Understand the core concepts of " + ch["title"]],
      "ai_context": {
        "learning_goal": "Master " + ch["title"] + " using Socratic learning.",
        "common_misconceptions": [],
        "tutor_hint": "Guide the student gently.",
        "next_topics": [f"gseb_class8_science_ch{ch['number']+1}"]
      }
    }
    
    with open(os.path.join(ch_dir, "metadata.json"), "w") as f:
        json.dump(metadata, f, indent=2)

with open(manifest_path, "w") as f:
    json.dump(manifest, f, indent=2)

print("Class 8 Metadata and Manifest generated successfully.")
