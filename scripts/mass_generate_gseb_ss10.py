import subprocess
import time
import os

SYLLABUS = [
    "Heritage of India",
    "Cultural Heritage of India: Traditional Handicrafts and Fine Arts",
    "Cultural Heritage of India: Sculpture and Architecture",
    "Literary Heritage of India",
    "India's Heritage of Science and Technology",
    "Places of Indian Cultural Heritage",
    "Preservation of Our Heritage",
    "Natural Resources",
    "Forest and Wildlife Resources",
    "India: Agriculture",
    "India: Water Resources",
    "India: Minerals and Energy Resources",
    "Manufacturing Industries",
    "Transportation, Communication and Trade",
    "Economic Development",
    "Economic Liberalization and Globalization",
    "Economic Problems and Challenges: Poverty and Unemployment",
    "Price Rise and Consumer Awareness",
    "Human Development",
    "Social Problems of India and Challenges",
    "Social Change"
]

CONTEXT_DIR = "/home/ubuntu/Shine_Academy_Naroda/SAN/Year2026/GSEB/10ss"

def generate_all():
    print("Starting massive generation of GSEB Class 10 Social Science...")
    for idx, title in enumerate(SYLLABUS, start=1):
        chapter_num = idx
        print(f"\n=======================================================")
        print(f"Generating GSEB Social Science Chapter {chapter_num}: {title}")
        print(f"=======================================================")
        
        cmd = [
            "python3",
            "scripts/generate_gold_content.py",
            "--board", "GSEB",
            "--grade", "10",
            "--subject", "Social_Science",
            "--chapter_num", str(chapter_num),
            "--chapter_title", title,
            "--context_dir", CONTEXT_DIR
        ]
        
        try:
            subprocess.run(cmd, check=True)
            print(f"✅ Successfully completed Chapter {chapter_num}")
        except subprocess.CalledProcessError as e:
            print(f"❌ ERROR: Generation failed for Chapter {chapter_num}.")
            print(f"Exiting script so you can check API limits.")
            return
        
        time.sleep(5)

if __name__ == "__main__":
    generate_all()
