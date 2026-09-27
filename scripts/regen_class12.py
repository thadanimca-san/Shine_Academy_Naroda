import json

def create_curriculum():
    curriculum = {
        "curriculum_id": "gseb_class12_commerce",
        "board": "GSEB",
        "class_name": "Class 12",
        "stream": "Commerce",
        "title": "Class 12 GSEB Commerce (Complete Course)",
        "subjects": []
    }

    # 1. Accountancy
    acc_chapters = []
    # GSEB Standard Chapters
    for i in range(1, 14):
        acc_chapters.append({
            "chapter_number": i,
            "title": f"Chapter {i}",
            "module_id": f"gseb_class12_accounts_ch{i}",
            "is_available": True,
            "status": "Available"
        })
    # Gujarati Versions
    for i in range(2, 8):
        acc_chapters.append({
            "chapter_number": i,
            "title": f"Chapter {i} (Gujarati)",
            "module_id": f"gseb_class12_accounts_ch{i}_gu",
            "is_available": True,
            "status": "Available"
        })
    # Other accounts modules
    acc_chapters.append({
        "chapter_number": 14,
        "title": "Final Accounts",
        "module_id": "gseb_class12_accounts_ch2_final_accounts",
        "is_available": True,
        "status": "Available"
    })
    acc_chapters.append({
        "chapter_number": 15,
        "title": "Partnership Concepts",
        "module_id": "gseb_class12_ch1_partnership",
        "is_available": True,
        "status": "Available"
    })
    # NCERT Accounts
    ncert_ids = ["leac101", "leac102", "leac103", "leac104", "leac201", "leac202", "leac203", "leac204", "leac205", "leac206"]
    for i, leac in enumerate(ncert_ids):
        acc_chapters.append({
            "chapter_number": 16 + i,
            "title": f"NCERT Chapter {leac.replace('leac', '')}",
            "module_id": f"ncert_class12_accounts_{leac}",
            "is_available": True,
            "status": "Available"
        })

    curriculum["subjects"].append({
        "id": "acc",
        "name": "Accountancy",
        "icon": "account_balance",
        "color_hex": "0xFF3F51B5",
        "chapters": acc_chapters
    })

    # 2. Statistics
    stat_chapters = []
    for i in range(1, 10):
        stat_chapters.append({
            "chapter_number": i,
            "title": f"Chapter {i}",
            "module_id": f"gseb_class12_stats_ch{i}",
            "is_available": True,
            "status": "Available"
        })
    for i in range(1, 6):
        stat_chapters.append({
            "chapter_number": i,
            "title": f"Chapter {i} (Gujarati)",
            "module_id": f"gseb_class12_stats_ch{i}_gu",
            "is_available": True,
            "status": "Available"
        })

    curriculum["subjects"].append({
        "id": "stat",
        "name": "Statistics",
        "icon": "bar_chart",
        "color_hex": "0xFF009688",
        "chapters": stat_chapters
    })

    # 3. English
    eng_chapters = []
    for i in range(1, 11):
        eng_chapters.append({
            "chapter_number": i,
            "title": f"Chapter {i}",
            "module_id": f"gseb_class12_english_ch{i}",
            "is_available": True,
            "status": "Available"
        })

    curriculum["subjects"].append({
        "id": "eng",
        "name": "English",
        "icon": "language",
        "color_hex": "0xFFE91E63",
        "chapters": eng_chapters
    })

    # 4. OC
    oc_chapters = []
    for i in range(1, 13):
        oc_chapters.append({
            "chapter_number": i,
            "title": f"Chapter {i}",
            "module_id": f"gseb_class12_oc_ch{i}",
            "is_available": True,
            "status": "Available"
        })

    curriculum["subjects"].append({
        "id": "oc",
        "name": "OC (Organization of Commerce & Management)",
        "icon": "business_center",
        "color_hex": "0xFFFF9800",
        "chapters": oc_chapters
    })

    # 5. Economics
    eco_chapters = []
    for i in range(1, 12):
        eco_chapters.append({
            "chapter_number": i,
            "title": f"Chapter {i}",
            "module_id": f"gseb_class12_eco_ch{i}",
            "is_available": True,
            "status": "Available"
        })

    curriculum["subjects"].append({
        "id": "eco",
        "name": "Economics",
        "icon": "trending_up",
        "color_hex": "0xFF4CAF50",
        "chapters": eco_chapters
    })

    # 6. Gujarati
    guj_chapters = [{
        "chapter_number": 1,
        "title": "અખિલ બ્રહ્માંડમાં",
        "module_id": "gseb_class12_commerce_guj_ch1",
        "is_available": True,
        "status": "Available"
    }]

    curriculum["subjects"].append({
        "id": "guj",
        "name": "Gujarati (Second Language)",
        "icon": "translate",
        "color_hex": "0xFF9C27B0",
        "chapters": guj_chapters
    })

    # 7. Hindi
    hin_chapters = [{
        "chapter_number": 1,
        "title": "कृष्ण भक्ति",
        "module_id": "gseb_class12_commerce_hin_ch1",
        "is_available": True,
        "status": "Available"
    }]

    curriculum["subjects"].append({
        "id": "hin",
        "name": "Hindi (Second Language)",
        "icon": "g_translate",
        "color_hex": "0xFFF44336",
        "chapters": hin_chapters
    })

    # Read original to merge original titles if they exist
    try:
        with open("/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class12_commerce.json", "r") as f:
            original = json.load(f)
            # Create mapping of module_id to title
            title_map = {}
            for subj in original.get("subjects", []):
                for chap in subj.get("chapters", []):
                    if "module_id" in chap and "title" in chap:
                        title_map[chap["module_id"]] = chap["title"]
                        
            # Apply original titles
            for subj in curriculum["subjects"]:
                for chap in subj["chapters"]:
                    mid = chap["module_id"]
                    if mid in title_map:
                        chap["title"] = title_map[mid]
    except Exception as e:
        print("Could not merge original titles:", e)

    with open("/home/ubuntu/Shine_Academy_Naroda/app_core/curriculum/gseb_class12_commerce.json", "w") as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
        
    print("Successfully regenerated gseb_class12_commerce.json!")

if __name__ == "__main__":
    create_curriculum()
