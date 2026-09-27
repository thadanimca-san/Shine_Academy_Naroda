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

# --- CLASS 11 COMMERCE ---

def generate_class11_commerce():
    print("Generating Class 11 Commerce...")
    curriculum_filepath = "app_core/curriculum/class11_commerce.json"
    data = load_json(curriculum_filepath)
    
    # Define syllabus
    syllabus = {
        "accounts": {
            "name": "Accountancy",
            "icon": "account_balance",
            "color": "0xFF4CAF50",
            "chapters": ["Accounting and its Terminology", "Dual Effect of Transactions", "Journal", "Ledger", "Cash Book", "Subsidiary Books", "Bank Reconciliation Statement", "Rectification of Errors", "Depreciation Accounts", "Final Accounts"]
        },
        "statistics": {
            "name": "Statistics",
            "icon": "bar_chart",
            "color": "0xFF009688",
            "chapters": ["Collection of Data", "Presentation of Data", "Measures of Central Tendency", "Measures of Dispersion", "Skewness of Frequency Distribution", "Permutations, Combinations and Binomial Expansion", "Sampling Methods", "Function", "Geometric Progression"]
        },
        "business": {
            "name": "Business Studies (OC)",
            "icon": "business_center",
            "color": "0xFF2196F3",
            "chapters": ["Nature, Purpose and Scope of Business", "Business Services 1", "Business Services 2", "Forms of Business Organization 1", "Forms of Business Organization 2", "Public Sector, Private Sector and Global Enterprises", "Source of Business Finance", "Small Scale Industries", "Internal Trade", "International Trade"]
        },
        "economics": {
            "name": "Economics",
            "icon": "trending_up",
            "color": "0xFF9C27B0",
            "chapters": ["Economics: An Introduction", "Fundamental Concepts and Terminologies", "Demand", "Supply", "Cost of Production and Concepts of Revenue", "Market", "Indian Economy", "Economic Reforms", "National Income", "Budget"]
        },
        "english": {
            "name": "English",
            "icon": "language",
            "color": "0xFFFF9800",
            "chapters": ["The Portrait of a Lady", "We're Not Afraid to Die", "Discovering Tut", "Landscape of the Soul", "The Ailing Planet", "The Browning Version", "The Adventure", "Silk Road"]
        }
    }
    
    subjects_list = []
    
    os.makedirs("app_core/chapters", exist_ok=True)
    
    for subj_id, subj_info in syllabus.items():
        ch_list = []
        for i, title in enumerate(subj_info["chapters"]):
            module_id = f"class11_commerce_{subj_id}_ch{i+1}"
            ch_list.append({
                "chapter_number": i+1,
                "title": f"Chapter {i+1}: {title}",
                "module_id": module_id
            })
            
            # Generate Chapter JSON
            chapter_data = {
                "metadata": {
                    "id": module_id,
                    "title": title,
                    "subject": subj_info["name"],
                    "grade": "11",
                    "stream": "Commerce",
                    "difficulty": "Advanced",
                    "estimated_minutes": 60
                },
                "blocks": [
                    {
                        "id": f"KOBJ_{module_id}_01",
                        "type": "hook",
                        "title": "Welcome to Commerce",
                        "body": f"Topic: {title}. Class 11 is the foundation for your commerce career."
                    },
                    {
                        "id": f"KOBJ_{module_id}_02",
                        "type": "theory",
                        "title": "Core Theory",
                        "body": "Understand the principles deeply."
                    },
                    {
                        "id": f"KOBJ_{module_id}_03",
                        "type": "teacher_tip",
                        "title": "Professional Tip",
                        "body": "Chartered Accountants and professionals use these concepts daily."
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
    print("Class 11 Commerce generation complete.")

# --- CLASS 12 COMMERCE ---

def generate_class12_commerce():
    print("Generating Class 12 Commerce...")
    curriculum_filepath = "app_core/curriculum/gseb_class12_commerce.json"
    data = load_json(curriculum_filepath)
    
    os.makedirs("app_core/chapters", exist_ok=True)
    
    for subject in data.get("subjects", []):
        subj_id = subject.get("id")
        subj_name = subject.get("name")
        
        for chapter in subject.get("chapters", []):
            # Fix data_file to module_id
            if "data_file" in chapter:
                # e.g., "app_core/chapters/gseb_class12_stats_ch1.json" -> "gseb_class12_stats_ch1"
                filepath = chapter["data_file"]
                if filepath:
                    module_id = filepath.split('/')[-1].replace('.json', '')
                    chapter["module_id"] = module_id
                del chapter["data_file"]
                
            module_id = chapter.get("module_id")
            title = chapter.get("title", "Chapter")
            
            if not module_id:
                # If neither existed, create one
                module_id = f"gseb_class12_commerce_{subj_id}_ch{chapter.get('chapter_number', 1)}"
                chapter["module_id"] = module_id
                
            chapter["is_available"] = True
            chapter["status"] = "Available"
                
            chapter_filepath = f"app_core/chapters/{module_id}.json"
            chapter_data = {
                "metadata": {
                    "id": module_id,
                    "title": title,
                    "subject": subj_name,
                    "grade": "12",
                    "stream": "Commerce",
                    "difficulty": "Board Level",
                    "estimated_minutes": 60
                },
                "blocks": [
                    {
                        "id": f"KOBJ_{module_id}_01",
                        "type": "hook",
                        "title": "Board Exam Prep",
                        "body": f"Topic: {title}. This is crucial for your Class 12 Boards."
                    },
                    {
                        "id": f"KOBJ_{module_id}_02",
                        "type": "theory",
                        "title": "Board Level Theory",
                        "body": "Mastering this chapter will guarantee excellent marks."
                    },
                    {
                        "id": f"KOBJ_{module_id}_03",
                        "type": "teacher_tip",
                        "title": "Board Examiner's View",
                        "body": "Always present your answers neatly in accounting formats."
                    }
                ]
            }
            check_and_save(chapter_data, chapter_filepath)

    save_json(data, curriculum_filepath)
    print("Class 12 Commerce generation complete.")

if __name__ == "__main__":
    generate_class11_commerce()
    generate_class12_commerce()
