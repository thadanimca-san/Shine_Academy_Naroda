import subprocess
import time

tasks = [
    # Class 7 SS
    ("GSEB", 7, "Social_Science", 2, "The Delhi Sultanate"),
    ("GSEB", 7, "Social_Science", 3, "Mughal Empire"),
    ("GSEB", 7, "Social_Science", 5, "Adivasis"),
    ("GSEB", 7, "Social_Science", 6, "Nomadic and Denotified Tribes"),
    ("GSEB", 7, "Social_Science", 7, "Bhakti Age Mystics and Saints"),
    ("GSEB", 7, "Social_Science", 8, "Regional Culture"),
]

# Class 10 Science (13 chapters)
for i in range(1, 14):
    tasks.append(("NCERT", 10, "Science", i, f"Chapter {i}"))

# Class 10 Maths (14 chapters)
for i in range(1, 15):
    tasks.append(("NCERT", 10, "Maths", i, f"Chapter {i}"))

# Class 10 Social Science (21 chapters)
for i in range(1, 22):
    tasks.append(("GSEB", 10, "Social_Science", i, f"Chapter {i}"))

# Class 10 English (20 chapters)
for i in range(1, 21):
    tasks.append(("GSEB", 10, "English", i, f"Chapter {i}"))

# Class 10 Gujarati (24 chapters)
for i in range(1, 25):
    tasks.append(("GSEB", 10, "Gujarati", i, f"Chapter {i}"))

# Class 10 Hindi (24 chapters)
for i in range(1, 25):
    tasks.append(("GSEB", 10, "Hindi", i, f"Chapter {i}"))


import sys

# To allow running a subset, we can pass skip count
start_idx = int(sys.argv[1]) if len(sys.argv) > 1 else 0

for idx, (board, grade, subject, ch_num, ch_title) in enumerate(tasks[start_idx:]):
    print(f"--- [{start_idx + idx + 1}/{len(tasks)}] Running {board} Class {grade} {subject} Ch {ch_num} ---")
    cmd = [
        "python3", "scripts/generate_gold_content.py",
        "--board", str(board),
        "--grade", str(grade),
        "--subject", str(subject),
        "--chapter_num", str(ch_num),
        "--chapter_title", str(ch_title)
    ]
    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to generate {subject} chapter {ch_num}")
    time.sleep(2) # Small delay between chapters
