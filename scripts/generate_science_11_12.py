import json
import os

def load_json(filepath):
    if not os.path.exists(filepath):
        return {}
    with open(filepath, 'r', encoding='utf-8') as f:
        return json.load(f)

def save_json(data, filepath):
    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

def check_and_save(data, filepath):
    if os.path.exists(filepath):
        return False
    save_json(data, filepath)
    return True

# Define complete syllabus for Class 11 and 12 Science (NCERT/GSEB/CBSE standard)
class11_syllabus = {
    "physics": {
        "name": "Physics", "icon": "science", "color": "0xFF2196F3",
        "chapters": ["Physical World", "Units and Measurements", "Motion in a Straight Line", "Motion in a Plane", "Laws of Motion", "Work Energy and Power", "System of Particles and Rotational Motion", "Gravitation", "Mechanical Properties of Solids", "Mechanical Properties of Fluids", "Thermal Properties of Matter", "Thermodynamics", "Kinetic Theory", "Oscillations", "Waves"]
    },
    "chemistry": {
        "name": "Chemistry", "icon": "biotech", "color": "0xFF9C27B0",
        "chapters": ["Some Basic Concepts of Chemistry", "Structure of Atom", "Classification of Elements", "Chemical Bonding", "States of Matter", "Thermodynamics", "Equilibrium", "Redox Reactions", "Hydrogen", "s-Block Elements", "p-Block Elements", "Organic Chemistry", "Hydrocarbons", "Environmental Chemistry"]
    },
    "biology": {
        "name": "Biology", "icon": "biotech", "color": "0xFF4CAF50",
        "chapters": ["The Living World", "Biological Classification", "Plant Kingdom", "Animal Kingdom", "Morphology of Flowering Plants", "Anatomy of Flowering Plants", "Structural Organisation in Animals", "Cell", "Biomolecules", "Cell Cycle", "Transport in Plants", "Mineral Nutrition", "Photosynthesis", "Respiration", "Plant Growth", "Digestion", "Breathing", "Body Fluids", "Excretory Products", "Locomotion", "Neural Control", "Chemical Coordination"]
    },
    "maths": {
        "name": "Mathematics", "icon": "calculate", "color": "0xFFE91E63",
        "chapters": ["Sets", "Relations and Functions", "Trigonometric Functions", "Principle of Mathematical Induction", "Complex Numbers", "Linear Inequalities", "Permutations and Combinations", "Binomial Theorem", "Sequences and Series", "Straight Lines", "Conic Sections", "Introduction to 3D Geometry", "Limits and Derivatives", "Mathematical Reasoning", "Statistics", "Probability"]
    }
}

class12_syllabus = {
    "physics": {
        "name": "Physics", "icon": "science", "color": "0xFF2196F3",
        "chapters": ["Electric Charges and Fields", "Electrostatic Potential", "Current Electricity", "Moving Charges and Magnetism", "Magnetism and Matter", "Electromagnetic Induction", "Alternating Current", "Electromagnetic Waves", "Ray Optics", "Wave Optics", "Dual Nature of Radiation", "Atoms", "Nuclei", "Semiconductor Electronics"]
    },
    "chemistry": {
        "name": "Chemistry", "icon": "biotech", "color": "0xFF9C27B0",
        "chapters": ["Solid State", "Solutions", "Electrochemistry", "Chemical Kinetics", "Surface Chemistry", "General Principles of Isolation", "p-Block Elements", "d and f Block Elements", "Coordination Compounds", "Haloalkanes and Haloarenes", "Alcohols Phenols and Ethers", "Aldehydes Ketones and Carboxylic Acids", "Amines", "Biomolecules", "Polymers", "Chemistry in Everyday Life"]
    },
    "biology": {
        "name": "Biology", "icon": "biotech", "color": "0xFF4CAF50",
        "chapters": ["Reproduction in Organisms", "Sexual Reproduction in Flowering Plants", "Human Reproduction", "Reproductive Health", "Principles of Inheritance", "Molecular Basis of Inheritance", "Evolution", "Human Health and Disease", "Strategies for Enhancement in Food Production", "Microbes in Human Welfare", "Biotechnology: Principles", "Biotechnology and its Applications", "Organisms and Populations", "Ecosystem", "Biodiversity", "Environmental Issues"]
    },
    "maths": {
        "name": "Mathematics", "icon": "calculate", "color": "0xFFE91E63",
        "chapters": ["Relations and Functions", "Inverse Trigonometric Functions", "Matrices", "Determinants", "Continuity and Differentiability", "Application of Derivatives", "Integrals", "Application of Integrals", "Differential Equations", "Vector Algebra", "Three Dimensional Geometry", "Linear Programming", "Probability"]
    }
}

def generate_science_curriculum(grade, syllabus):
    curriculum_filepath = f"app_core/curriculum/class{grade}_science.json"
    print(f"Generating Class {grade} Science ({curriculum_filepath})...")
    data = load_json(curriculum_filepath)
    
    subjects_list = []
    os.makedirs("app_core/chapters", exist_ok=True)
    
    for subj_id, subj_info in syllabus.items():
        ch_list = []
        for i, title in enumerate(subj_info["chapters"]):
            module_id = f"class{grade}_science_{subj_id}_ch{i+1}"
            ch_list.append({
                "chapter_number": i+1,
                "title": f"Chapter {i+1}: {title}",
                "module_id": module_id,
                "is_available": True,
                "status": "Available"
            })
            
            # Generate Chapter JSON Blocks
            chapter_data = {
                "metadata": {
                    "id": module_id,
                    "title": title,
                    "subject": subj_info["name"],
                    "grade": str(grade),
                    "stream": "Science",
                    "difficulty": "Advanced",
                    "estimated_minutes": 60
                },
                "blocks": [
                    {
                        "id": f"KOBJ_{module_id}_01",
                        "type": "hook",
                        "title": "Welcome to Science",
                        "body": f"Topic: {title}. In Class {grade} Science, we dive deeper into the physical universe."
                    },
                    {
                        "id": f"KOBJ_{module_id}_02",
                        "type": "theory",
                        "title": "Core Theory",
                        "body": "Understanding the complex mechanisms is critical for competitive exams like JEE/NEET."
                    },
                    {
                        "id": f"KOBJ_{module_id}_03",
                        "type": "teacher_tip",
                        "title": "Competitive Exam Tip",
                        "body": "Always practice numericals based on this concept daily."
                    },
                    {
                        "id": f"KOBJ_{module_id}_04",
                        "type": "quiz",
                        "question": "Are you ready to crack JEE/NEET?",
                        "options": ["Yes, I am!", "I need more practice."],
                        "correct_index": 0,
                        "explanation": "Confidence is the first step to success!"
                    }
                ]
            }
            check_and_save(chapter_data, f"app_core/chapters/{module_id}.json")
            
        subjects_list.append({
            "id": subj_id,
            "name": subj_info["name"],
            "icon": subj_info["icon"],
            "color_hex": subj_info["color"],
            "chapters": ch_list
        })
        
    data["subjects"] = subjects_list
    save_json(data, curriculum_filepath)
    print(f"Class {grade} Science generation complete.")

if __name__ == "__main__":
    generate_science_curriculum(11, class11_syllabus)
    generate_science_curriculum(12, class12_syllabus)
