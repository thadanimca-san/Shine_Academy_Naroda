import os
import json
import glob

# ============================================================
# MASTER 3-WAY SYNC SCRIPT
# Syncs all Class 9 & 10 chapter files across:
#   1. app_core/chapters/
#   2. app_core/learning_modules/ (ncert_ + gseb_ dirs)
#   3. app_core/assessment/ (ncert_ + gseb_ question banks)
# ============================================================

CHAPTER_TITLES = {
    "ncert_class9_maths": {
        1: ("Number Systems", "संख्या पद्धति", "સંખ્યા પ્રણાળી"),
        2: ("Polynomials", "बहुपद", "બહુપદ"),
        3: ("Coordinate Geometry", "निर्देशांक ज्यामिति", "યામ ભૂમિતિ"),
        4: ("Linear Equations in Two Variables", "दो चरों में रैखिक समीकरण", "બે ચલોમાં રેખીય સમીકરણ"),
        5: ("Introduction to Euclid's Geometry", "यूक्लिड की ज्यामिति का परिचय", "યુક્લિડ ભૂમિતિ"),
        6: ("Lines and Angles", "रेखाएं और कोण", "રેખાઓ અને ખૂણા"),
        7: ("Triangles", "त्रिभुज", "ત્રિકોણ"),
        8: ("Quadrilaterals", "चतुर्भुज", "ચતુષ્કોણ"),
        9: ("Circles", "वृत्त", "વર્તુળ"),
        10: ("Heron's Formula", "हेरोन का सूत्र", "હેરોનનું સૂત્ર"),
        11: ("Surface Areas and Volumes", "पृष्ठीय क्षेत्रफल और आयतन", "પૃષ્ઠફળ અને ઘનફળ"),
        12: ("Statistics", "सांख्यिकी", "આંકડાશાસ્ત્ર"),
    },
    "ncert_class9_science": {
        1: ("Matter in Our Surroundings", "हमारे आस-पास के पदार्थ", "આપણી આસ-પાસ દ્રવ્ય"),
        2: ("Is Matter Around Us Pure?", "क्या हमारे आस-पास के पदार्थ शुद्ध हैं?", "આપણી આસ-પાસ ના દ્રવ્ય શુદ્ધ છે?"),
        3: ("Atoms and Molecules", "परमाणु एवं अणु", "પરમાણુ અને અણુ"),
        4: ("Structure of the Atom", "परमाणु की संरचना", "પરમાણુની રચના"),
        5: ("The Fundamental Unit of Life", "जीवन की मूल इकाई", "જીવનનો મૂળ એકમ"),
        6: ("Tissues", "ऊतक", "પેશી"),
        7: ("Motion", "गति", "ગતિ"),
        8: ("Force and Laws of Motion", "बल तथा गति के नियम", "બળ અને ગતિના નિયમ"),
        9: ("Gravitation", "गुरुत्वाकर्षण", "ગુરુત્વાકર્ષણ"),
        10: ("Work and Energy", "कार्य तथा ऊर्जा", "કાર્ય અને ઊર્જા"),
        11: ("Sound", "ध्वनि", "ધ્વનિ"),
        12: ("Improvement in Food Resources", "खाद्य संसाधनों में सुधार", "ખાદ્ય સ્ત્રોતોમાં સુધારણ"),
    },
    "ncert_class9_social_science": {
        **{i: (f"Chapter {i}", f"अध्याय {i}", f"પ્રકરણ {i}") for i in range(1, 21)}
    },
    "ncert_class9_english": {
        1: ("The Fun They Had", "उन्होंने जो आनंद लिया", "તેઓ ક્યારે શોધ કરી"),
        2: ("The Sound of Music", "संगीत की ध्वनि", "સંગીતનો અવાજ"),
        3: ("The Little Girl", "नन्ही लड़की", "નાની છોકરી"),
        4: ("A Truly Beautiful Mind", "सचमुच एक सुंदर मन", "સાચ્ચu સુંદર મન"),
        5: ("The Snake and the Mirror", "सांप और दर्पण", "સર્પ અને દર્પણ"),
        6: ("My Childhood", "मेरा बचपन", "મારું બાળપણ"),
        7: ("Reach for the Top", "शिखर की ओर बढ़ो", "ટોચ સુધી પહોંચો"),
        8: ("Kathmandu", "काठमांडू", "કાઠમાંડુ"),
        9: ("If I Were You", "अगर मैं आप होता", "જો હું તમે હોત"),
        10: ("Moments Supplementary", "क्षण पूरक पाठक", "ક્ષણ પૂરક"),
    },
    "ncert_class10_maths": {
        1: ("Real Numbers", "वास्तविक संख्याएं", "વાસ્તવિક સંખ્યાઓ"),
        2: ("Polynomials", "बहुपद", "બહુપદ"),
        3: ("Pair of Linear Equations in Two Variables", "दो चरों वाले रैखिक समीकरण युग्म", "દ્વાચલ સ. યુ."),
        4: ("Quadratic Equations", "द्विघात समीकरण", "દ્વિઘાત સ."),
        5: ("Arithmetic Progressions", "समांतर श्रेढ़ियां", "સ. શ્રેણી"),
        6: ("Triangles", "त्रिभुज", "ત્રિકોણ"),
        7: ("Coordinate Geometry", "निर्देशांक ज्यामिति", "યામ ભૂ."),
        8: ("Introduction to Trigonometry", "त्रिकोणमिति का परिचय", "ત્રિ. પ."),
        9: ("Some Applications of Trigonometry", "त्रिकोणमिति के अनुप्रयोग", "ત્રિ. ઉ."),
        10: ("Circles", "वृत्त", "વ."),
        11: ("Areas Related to Circles", "वृत्तों से संबंधित क्षेत्रफल", "વ. ક્ષ."),
        12: ("Surface Areas and Volumes", "पृष्ठीय क्षेत्रफल और आयतन", "પ.ઘ."),
        13: ("Statistics", "सांख्यिकी", "આ."),
        14: ("Probability", "प्रायिकता", "સ."),
    },
    "ncert_class10_science": {
        1: ("Chemical Reactions and Equations", "रासायनिक अभिक्रियाएं एवं समीकरण", "રાસા. ક્રિ."),
        2: ("Acids, Bases and Salts", "अम्ल, क्षारक एवं लवण", "એ.ક્ષા.લ."),
        3: ("Metals and Non-metals", "धातु एवं अधातु", "ધ. અ."),
        4: ("Carbon and its Compounds", "कार्बन एवं उसके यौगिक", "ક.સ."),
        5: ("Life Processes", "जीवन प्रक्रियाएं", "જ. ક્."),
        6: ("Control and Coordination", "नियंत्रण एवं समन्वय", "ન. સ."),
        7: ("How do Organisms Reproduce?", "जीव जनन कैसे करते हैं?", "જ. જ."),
        8: ("Heredity and Evolution", "आनुवंशिकता एवं जैव विकास", "આ. ઉ."),
        9: ("Light - Reflection and Refraction", "प्रकाश - परावर्तन तथा अपवर्तन", "પ. પ."),
        10: ("The Human Eye and the Colourful World", "मानव नेत्र तथा रंगबिरंगा संसार", "આ.ન."),
        11: ("Electricity", "विद्युत", "વ."),
        12: ("Magnetic Effects of Electric Current", "विद्युत धारा के चुंबकीय प्रभाव", "વ. ધ."),
        13: ("Our Environment", "हमारा पर्यावरण", "આ. પ."),
    },
    "ncert_class10_history": {
        1: ("The Rise of Nationalism in Europe", "यूरोप में राष्ट्रवाद का उदय", "યુ. રા."),
        2: ("Nationalism in India", "भारत में राष्ट्रवाद", "ભા. રા."),
        3: ("The Making of a Global World", "भूमंडलीकृत विश्व का बनना", "ભ. વ."),
        4: ("The Age of Industrialisation", "औद्योगीकरण का युग", "ઔ. ય."),
        5: ("Print Culture and the Modern World", "मुद्रण संस्कृति और आधुनिक दुनिया", "મ. સ."),
    },
    "ncert_class10_civics": {
        1: ("Power Sharing", "सत्ता की साझेदारी", "સ. ભ."),
        2: ("Federalism", "संघवाद", "સ."),
        3: ("Democracy and Diversity", "लोकतंत्र और विविधता", "લ. વ."),
        4: ("Gender, Religion and Caste", "जाति, धर्म और लैंगिक मसले", "ય. ધ."),
        5: ("Popular Struggles and Movements", "जन-संघर्ष और आंदोलन", "જ. સ."),
    },
    "ncert_class10_geography": {
        1: ("Resources and Development", "संसाधन और विकास", "સ. વ."),
        2: ("Forest and Wildlife Resources", "वन और वन्य जीव संसाधन", "વ. વ."),
        3: ("Water Resources", "जल संसाधन", "જ. સ."),
        4: ("Agriculture", "कृषि", "ક."),
        5: ("Minerals and Energy Resources", "खनिज और ऊर्जा संसाधन", "ખ. ઊ."),
        6: ("Manufacturing Industries", "विनिर्माण उद्योग", "ઉ."),
        7: ("Lifelines of National Economy", "राष्ट्रीय अर्थव्यवस्था की जीवन रेखाएं", "ર. જ."),
    },
    "ncert_class10_economics": {
        1: ("Development", "विकास", "વ."),
        2: ("Sectors of the Indian Economy", "भारतीय अर्थव्यवस्था के क्षेत्रक", "ભ. ઓ."),
        3: ("Money and Credit", "मुद्रा और साख", "મ. સ."),
        4: ("Globalisation and the Indian Economy", "वैश्वीकरण और भारतीय अर्थव्यवस्था", "વ. ભ."),
        5: ("Consumer Rights", "उपभोक्ता अधिकार", "ઉ. અ."),
    },
    "cbse_class10_english": {
        1: ("A Letter to God", "भगवान को पत्र", "ભ. ને પ."),
        2: ("Nelson Mandela: Long Walk to Freedom", "नेल्सन मंडेला", "ન. મ."),
        3: ("Two Stories about Flying", "उड़ान की दो कहानियाँ", "ઉ. ક."),
        4: ("From the Diary of Anne Frank", "ऐनी फ्रैंक की डायरी", "એ. ડ."),
        5: ("Glimpses of India", "भारत की झलकियां", "ભ. ઝ."),
        6: ("Mijbil the Otter", "मिजबिल", "મ."),
        7: ("Madam Rides the Bus", "बस की सवारी", "બ. સ."),
        8: ("The Sermon at Benares", "बनारस में उपदेश", "બ. ઉ."),
        9: ("The Proposal", "प्रस्ताव", "પ."),
    },
}

# Subject ID mapping for metadata
SUBJECT_IDS = {
    "ncert_class9_maths": ("ncert_class9_math", "ncert_class9"),
    "ncert_class9_science": ("ncert_class9_science", "ncert_class9"),
    "ncert_class9_social_science": ("ncert_class9_social", "ncert_class9"),
    "ncert_class9_english": ("ncert_class9_english", "ncert_class9"),
    "ncert_class10_maths": ("ncert_class10_math", "ncert_class10"),
    "ncert_class10_science": ("ncert_class10_science", "ncert_class10"),
    "ncert_class10_history": ("ncert_class10_social", "ncert_class10"),
    "ncert_class10_civics": ("ncert_class10_social", "ncert_class10"),
    "ncert_class10_geography": ("ncert_class10_social", "ncert_class10"),
    "ncert_class10_economics": ("ncert_class10_social", "ncert_class10"),
    "cbse_class10_english": ("cbse_class10_english", "cbse_class10"),
}

def sync_subject(prefix, max_chapters):
    """Sync all chapters of a subject across the 3-way structure."""
    titles_map = CHAPTER_TITLES.get(prefix, {})
    subj_id, class_id = SUBJECT_IDS.get(prefix, (prefix, prefix.rsplit("_", 2)[0]))
    
    synced = 0
    skipped = 0
    
    for ch_num in range(1, max_chapters + 1):
        chapter_file = f"app_core/chapters/{prefix}_ch{ch_num}.json"
        if not os.path.exists(chapter_file):
            skipped += 1
            continue
            
        with open(chapter_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        blocks = data if isinstance(data, list) else data.get("blocks", [])
        
        # Ensure all blocks have trilingual fields (fallback to English if missing)
        for idx, b in enumerate(blocks):
            if not isinstance(b, dict): continue
            if "id" not in b or not b["id"]:
                b["id"] = f"KOBJ_{prefix.upper()}_CH{ch_num}_BLOCK_{idx}"
            for k in ["title", "body", "question", "explanation"]:
                if k in b:
                    val = b[k]
                    if not b.get(f"{k}_hi"): b[f"{k}_hi"] = val
                    if not b.get(f"{k}_gu"): b[f"{k}_gu"] = val
            if "options" in b and isinstance(b["options"], list):
                if not b.get("options_hi"): b["options_hi"] = b["options"]
                if not b.get("options_gu"): b["options_gu"] = b["options"]
        
        # Write back as flat list
        with open(chapter_file, 'w', encoding='utf-8') as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)
        
        ch_title_info = titles_map.get(ch_num, (f"Chapter {ch_num}", f"अध्याय {ch_num}", f"પ્રકરણ {ch_num}"))
        ch_title_en, ch_title_hi, ch_title_gu = ch_title_info
        
        meta = {
            "id": f"{prefix}_ch{ch_num}",
            "title": f"Chapter {ch_num}: {ch_title_en}",
            "title_hi": f"अध्याय {ch_num}: {ch_title_hi}",
            "title_gu": f"પ્રકરણ {ch_num}: {ch_title_gu}",
            "subject_id": subj_id,
            "class_id": class_id
        }
        
        # Determine GSEB prefix
        gseb_prefix = prefix.replace("ncert_", "gseb_").replace("cbse_", "gseb_")
        
        # 2. Sync NCERT learning module
        ncert_lm_dir = f"app_core/learning_modules/{prefix}_ch{ch_num}"
        os.makedirs(ncert_lm_dir, exist_ok=True)
        with open(os.path.join(ncert_lm_dir, "blocks.json"), 'w', encoding='utf-8') as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)
        with open(os.path.join(ncert_lm_dir, "metadata.json"), 'w', encoding='utf-8') as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
        
        # 3. Sync GSEB learning module
        gseb_lm_dir = f"app_core/learning_modules/{gseb_prefix}_ch{ch_num}"
        os.makedirs(gseb_lm_dir, exist_ok=True)
        with open(os.path.join(gseb_lm_dir, "blocks.json"), 'w', encoding='utf-8') as f:
            json.dump(blocks, f, ensure_ascii=False, indent=2)
        gseb_meta = {**meta, "id": f"{gseb_prefix}_ch{ch_num}", "class_id": gseb_prefix.rsplit("_", 2)[0]}
        with open(os.path.join(gseb_lm_dir, "metadata.json"), 'w', encoding='utf-8') as f:
            json.dump(gseb_meta, f, ensure_ascii=False, indent=2)
        
        # 4. Extract assessment questions
        q_blocks = [b for b in blocks if b.get("type") in ["quiz", "mcq", "practice_question", "challenge_question", "true_false"] and "question" in b]
        questions = []
        for b in q_blocks:
            q = {
                "id": b.get("id", ""),
                "question": b.get("question", ""),
                "question_hi": b.get("question_hi", b.get("question", "")),
                "question_gu": b.get("question_gu", b.get("question", "")),
                "options": b.get("options", []),
                "options_hi": b.get("options_hi", b.get("options", [])),
                "options_gu": b.get("options_gu", b.get("options", [])),
                "correct_index": b.get("correct_index", 0),
                "explanation": b.get("explanation", ""),
                "explanation_hi": b.get("explanation_hi", b.get("explanation", "")),
                "explanation_gu": b.get("explanation_gu", b.get("explanation", ""))
            }
            questions.append(q)
        
        # Write assessment files for both ncert and gseb prefixes
        for assess_prefix in [prefix, gseb_prefix]:
            assess_file = f"app_core/assessment/{assess_prefix}_ch{ch_num}_questions.json"
            with open(assess_file, 'w', encoding='utf-8') as f:
                json.dump(questions, f, ensure_ascii=False, indent=2)
        
        synced += 1
    
    return synced, skipped

def main():
    print("=" * 70)
    print("  MASTER 3-WAY SYNC: CLASS 9 & 10 ALL SUBJECTS")
    print("=" * 70)
    
    subjects_config = [
        ("ncert_class9_science", 12),
        ("ncert_class9_maths", 12),
        ("ncert_class9_social_science", 20),
        ("ncert_class9_english", 10),
        ("ncert_class10_maths", 14),
        ("ncert_class10_science", 13),
        ("ncert_class10_history", 5),
        ("ncert_class10_civics", 5),
        ("ncert_class10_geography", 7),
        ("ncert_class10_economics", 5),
        ("cbse_class10_english", 9),
    ]
    
    total_synced = 0
    total_skipped = 0
    
    for prefix, max_ch in subjects_config:
        synced, skipped = sync_subject(prefix, max_ch)
        total_synced += synced
        total_skipped += skipped
        print(f"  ✅ {prefix}: {synced} chapters synced, {skipped} missing")
    
    print("-" * 70)
    print(f"  Total chapters synced: {total_synced}")
    print(f"  Total chapters missing: {total_skipped}")
    print("=" * 70)

if __name__ == "__main__":
    main()
