import json
import os

def update_ncert_class9_curriculum():
    curriculum_path = "app_core/curriculum/ncert_class9.json"
    
    curriculum_data = {
        "id": "ncert_class9",
        "name": "NCERT CLASS 9 (Core Concepts)",
        "subjects": [
            {
                "id": "ncert_class9_maths_new",
                "name": "Maths — Ganita Prakash (New 2024 Edition)",
                "color_hex": "0xFF2196F3",
                "icon": "calculate",
                "edition": "New Edition (Ganita Prakash)",
                "chapters": [
                    {"chapter_id": "ncert_class9_maths_ch1", "title": "Chapter 1: Number Systems", "module_id": "ncert_class9_maths_ch1"},
                    {"chapter_id": "ncert_class9_maths_ch2", "title": "Chapter 2: Polynomials", "module_id": "ncert_class9_maths_ch2"},
                    {"chapter_id": "ncert_class9_maths_ch3", "title": "Chapter 3: Coordinate Geometry", "module_id": "ncert_class9_maths_ch3"},
                    {"chapter_id": "ncert_class9_maths_ch4", "title": "Chapter 4: Linear Equations in Two Variables", "module_id": "ncert_class9_maths_ch4"},
                    {"chapter_id": "ncert_class9_maths_ch5", "title": "Chapter 5: Introduction to Euclid's Geometry", "module_id": "ncert_class9_maths_ch5"},
                    {"chapter_id": "ncert_class9_maths_ch6", "title": "Chapter 6: Lines and Angles", "module_id": "ncert_class9_maths_ch6"},
                    {"chapter_id": "ncert_class9_maths_ch7", "title": "Chapter 7: Triangles", "module_id": "ncert_class9_maths_ch7"},
                    {"chapter_id": "ncert_class9_maths_ch8", "title": "Chapter 8: Quadrilaterals", "module_id": "ncert_class9_maths_ch8"},
                    {"chapter_id": "ncert_class9_maths_ch9", "title": "Chapter 9: Circles", "module_id": "ncert_class9_maths_ch9"},
                    {"chapter_id": "ncert_class9_maths_ch10", "title": "Chapter 10: Heron's Formula", "module_id": "ncert_class9_maths_ch10"},
                    {"chapter_id": "ncert_class9_maths_ch11", "title": "Chapter 11: Surface Areas and Volumes", "module_id": "ncert_class9_maths_ch11"},
                    {"chapter_id": "ncert_class9_maths_ch12", "title": "Chapter 12: Statistics", "module_id": "ncert_class9_maths_ch12"}
                ]
            },
            {
                "id": "ncert_class9_maths_classic",
                "name": "Maths — Mathematics Classic (Old Full Edition)",
                "color_hex": "0xFF1976D2",
                "icon": "calculate",
                "edition": "Classic Full Edition",
                "chapters": [
                    {"chapter_id": "ncert_class9_maths_ch1", "title": "Chapter 1: Number Systems", "module_id": "ncert_class9_maths_ch1"},
                    {"chapter_id": "ncert_class9_maths_ch2", "title": "Chapter 2: Polynomials", "module_id": "ncert_class9_maths_ch2"},
                    {"chapter_id": "ncert_class9_maths_ch3", "title": "Chapter 3: Coordinate Geometry", "module_id": "ncert_class9_maths_ch3"},
                    {"chapter_id": "ncert_class9_maths_ch4", "title": "Chapter 4: Linear Equations in Two Variables", "module_id": "ncert_class9_maths_ch4"},
                    {"chapter_id": "ncert_class9_maths_ch5", "title": "Chapter 5: Introduction to Euclid's Geometry", "module_id": "ncert_class9_maths_ch5"},
                    {"chapter_id": "ncert_class9_maths_ch6", "title": "Chapter 6: Lines and Angles", "module_id": "ncert_class9_maths_ch6"},
                    {"chapter_id": "ncert_class9_maths_ch7", "title": "Chapter 7: Triangles", "module_id": "ncert_class9_maths_ch7"},
                    {"chapter_id": "ncert_class9_maths_ch8", "title": "Chapter 8: Quadrilaterals", "module_id": "ncert_class9_maths_ch8"},
                    {"chapter_id": "ncert_class9_maths_ch9", "title": "Chapter 9: Areas of Parallelograms & Triangles", "module_id": "ncert_class9_maths_ch9"},
                    {"chapter_id": "ncert_class9_maths_ch10", "title": "Chapter 10: Circles", "module_id": "ncert_class9_maths_ch10"},
                    {"chapter_id": "ncert_class9_maths_ch11", "title": "Chapter 11: Constructions", "module_id": "ncert_class9_maths_ch11"},
                    {"chapter_id": "ncert_class9_maths_ch12", "title": "Chapter 12: Heron's Formula", "module_id": "ncert_class9_maths_ch12"}
                ]
            },
            {
                "id": "ncert_class9_science",
                "name": "Science — Complete Textbook Edition",
                "color_hex": "0xFF4CAF50",
                "icon": "science",
                "edition": "Complete Textbook Edition",
                "chapters": [
                    {"chapter_id": "ncert_class9_science_ch1", "title": "Chapter 1: Matter in Our Surroundings", "module_id": "ncert_class9_science_ch1"},
                    {"chapter_id": "ncert_class9_science_ch2", "title": "Chapter 2: Is Matter Around Us Pure?", "module_id": "ncert_class9_science_ch2"},
                    {"chapter_id": "ncert_class9_science_ch3", "title": "Chapter 3: Atoms and Molecules", "module_id": "ncert_class9_science_ch3"},
                    {"chapter_id": "ncert_class9_science_ch4", "title": "Chapter 4: Structure of the Atom", "module_id": "ncert_class9_science_ch4"},
                    {"chapter_id": "ncert_class9_science_ch5", "title": "Chapter 5: The Fundamental Unit of Life", "module_id": "ncert_class9_science_ch5"},
                    {"chapter_id": "ncert_class9_science_ch6", "title": "Chapter 6: Tissues", "module_id": "ncert_class9_science_ch6"},
                    {"chapter_id": "ncert_class9_science_ch7", "title": "Chapter 7: Motion", "module_id": "ncert_class9_science_ch7"},
                    {"chapter_id": "ncert_class9_science_ch8", "title": "Chapter 8: Force and Laws of Motion", "module_id": "ncert_class9_science_ch8"},
                    {"chapter_id": "ncert_class9_science_ch9", "title": "Chapter 9: Gravitation", "module_id": "ncert_class9_science_ch9"},
                    {"chapter_id": "ncert_class9_science_ch10", "title": "Chapter 10: Work and Energy", "module_id": "ncert_class9_science_ch10"},
                    {"chapter_id": "ncert_class9_science_ch11", "title": "Chapter 11: Sound", "module_id": "ncert_class9_science_ch11"},
                    {"chapter_id": "ncert_class9_science_ch12", "title": "Chapter 12: Improvement in Food Resources", "module_id": "ncert_class9_science_ch12"}
                ]
            },
            {
                "id": "ncert_class9_english_beehive",
                "name": "English — Beehive (Main Textbook)",
                "color_hex": "0xFFE91E63",
                "icon": "book",
                "edition": "Main Reader",
                "chapters": [
                    {"chapter_id": "ncert_class9_english_ch1", "title": "Chapter 1: The Fun They Had & The Road Not Taken", "module_id": "ncert_class9_english_ch1"},
                    {"chapter_id": "ncert_class9_english_ch2", "title": "Chapter 2: The Sound of Music & Wind", "module_id": "ncert_class9_english_ch2"},
                    {"chapter_id": "ncert_class9_english_ch3", "title": "Chapter 3: The Little Girl & Rain on the Roof", "module_id": "ncert_class9_english_ch3"},
                    {"chapter_id": "ncert_class9_english_ch4", "title": "Chapter 4: A Truly Beautiful Mind & Innisfree", "module_id": "ncert_class9_english_ch4"},
                    {"chapter_id": "ncert_class9_english_ch5", "title": "Chapter 5: The Snake and the Mirror & Northland", "module_id": "ncert_class9_english_ch5"},
                    {"chapter_id": "ncert_class9_english_ch6", "title": "Chapter 6: My Childhood & No Men Are Foreign", "module_id": "ncert_class9_english_ch6"},
                    {"chapter_id": "ncert_class9_english_ch7", "title": "Chapter 7: Reach for the Top & Killing a Tree", "module_id": "ncert_class9_english_ch7"},
                    {"chapter_id": "ncert_class9_english_ch8", "title": "Chapter 8: Kathmandu & Slumber Spirit Seal", "module_id": "ncert_class9_english_ch8"},
                    {"chapter_id": "ncert_class9_english_ch9", "title": "Chapter 9: If I Were You", "module_id": "ncert_class9_english_ch9"}
                ]
            },
            {
                "id": "ncert_class9_english_moments",
                "name": "English — Moments (Supplementary Reader)",
                "color_hex": "0xFF9C27B0",
                "icon": "auto_stories",
                "edition": "Supplementary Reader",
                "chapters": [
                    {"chapter_id": "ncert_class9_english_ch10", "title": "Moments: The Lost Child & The Happy Prince", "module_id": "ncert_class9_english_ch10"}
                ]
            },
            {
                "id": "ncert_class9_social_science",
                "name": "Social Science — History, Geography, Civics & Eco",
                "color_hex": "0xFFFF9800",
                "icon": "public",
                "edition": "Full Curriculum (20 Chapters)",
                "chapters": [
                    {"chapter_id": "ncert_class9_social_science_ch1", "title": "Ch 1: Arrival of Europeans to India", "module_id": "ncert_class9_social_science_ch1"},
                    {"chapter_id": "ncert_class9_social_science_ch2", "title": "Ch 2: First World War & Russian Revolution", "module_id": "ncert_class9_social_science_ch2"},
                    {"chapter_id": "ncert_class9_social_science_ch3", "title": "Ch 3: Movement Towards a New World", "module_id": "ncert_class9_social_science_ch3"},
                    {"chapter_id": "ncert_class9_social_science_ch4", "title": "Ch 4: National Movements in India", "module_id": "ncert_class9_social_science_ch4"},
                    {"chapter_id": "ncert_class9_social_science_ch5", "title": "Ch 5: Movement Towards Independence", "module_id": "ncert_class9_social_science_ch5"},
                    {"chapter_id": "ncert_class9_social_science_ch6", "title": "Ch 6: World After 1945", "module_id": "ncert_class9_social_science_ch6"},
                    {"chapter_id": "ncert_class9_social_science_ch7", "title": "Ch 7: Post-Independence India", "module_id": "ncert_class9_social_science_ch7"},
                    {"chapter_id": "ncert_class9_social_science_ch8", "title": "Ch 8: Framing of Constitution & Features", "module_id": "ncert_class9_social_science_ch8"},
                    {"chapter_id": "ncert_class9_social_science_ch9", "title": "Ch 9: Fundamental Rights, Duties & Principles", "module_id": "ncert_class9_social_science_ch9"},
                    {"chapter_id": "ncert_class9_social_science_ch10", "title": "Ch 10: Organs of Government", "module_id": "ncert_class9_social_science_ch10"},
                    {"chapter_id": "ncert_class9_social_science_ch11", "title": "Ch 11: Judiciary", "module_id": "ncert_class9_social_science_ch11"},
                    {"chapter_id": "ncert_class9_social_science_ch12", "title": "Ch 12: Indian Democracy", "module_id": "ncert_class9_social_science_ch12"},
                    {"chapter_id": "ncert_class9_social_science_ch13", "title": "Ch 13: India: Location & Physiography - I", "module_id": "ncert_class9_social_science_ch13"},
                    {"chapter_id": "ncert_class9_social_science_ch14", "title": "Ch 14: India: Location & Physiography - II", "module_id": "ncert_class9_social_science_ch14"},
                    {"chapter_id": "ncert_class9_social_science_ch15", "title": "Ch 15: Drainage System", "module_id": "ncert_class9_social_science_ch15"},
                    {"chapter_id": "ncert_class9_social_science_ch16", "title": "Ch 16: Climate", "module_id": "ncert_class9_social_science_ch16"},
                    {"chapter_id": "ncert_class9_social_science_ch17", "title": "Ch 17: Natural Vegetation", "module_id": "ncert_class9_social_science_ch17"},
                    {"chapter_id": "ncert_class9_social_science_ch18", "title": "Ch 18: Wild Life", "module_id": "ncert_class9_social_science_ch18"},
                    {"chapter_id": "ncert_class9_social_science_ch19", "title": "Ch 19: India: Human Life", "module_id": "ncert_class9_social_science_ch19"},
                    {"chapter_id": "ncert_class9_social_science_ch20", "title": "Ch 20: Disaster Management", "module_id": "ncert_class9_social_science_ch20"}
                ]
            }
        ]
    }
    
    with open(curriculum_path, "w", encoding="utf-8") as f:
        json.dump(curriculum_data, f, ensure_ascii=False, indent=2)
    print(f"Successfully updated {curriculum_path} with explicit BOLD book names and dual editions.")

if __name__ == "__main__":
    update_ncert_class9_curriculum()
