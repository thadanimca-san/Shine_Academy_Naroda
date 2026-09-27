import json
import os

chapter_data = {
    # HINDI
    "ncert_class10_hindi_ch1": {
        "title": "Chapter 1: Prabhuji Tum Chandan Hum Pani",
        "hook": "Do you know what unconditional devotion looks like? Raidas uses beautiful nature metaphors to show how a devotee's soul merges with God, just like water merges with sandalwood!",
        "passages": [
            {"title": "Passage 1: Sandalwood and Water", "content": "प्रभु जी, तुम चंदन हम पानी,\nजाकी अँग-अँग बास समानी।\n`` `(O Lord, you are sandalwood and I am water, / હે પ્રભુ, તમે ચંદન છો અને હું પાણી છું,)` ``\n`` `(Whose fragrance has permeated every part of my body. / જેની સુગંધ મારા અંગ-અંગમાં વસી ગઈ છે.)` ``"},
            {"title": "Passage 2: Cloud and Peacock", "content": "प्रभु जी, तुम घन बन हम मोरा,\nजैसे चितवत चंद चकोरा।\n`` `(O Lord, you are the dark cloud and I am the peacock, / હે પ્રભુ, તમે કાળા વાદળ છો અને હું મોર છું,)` ``\n`` `(Just like the Chakora bird constantly looks at the moon. / જેમ ચકોર પક્ષી સતત ચંદ્રને જુએ છે.)` ``"}
        ]
    },
    "ncert_class10_hindi_ch2": {
        "title": "Chapter 2: Meera Ke Pad",
        "hook": "Meera Bai gave up her royal palace for her devotion to Lord Krishna. Let's read her immortal verses where she begs Krishna to save her, just like he saved Draupadi and Prahlad.",
        "passages": [
            {"title": "Passage 1: A Plea for Help", "content": "हरि आप हरो जन री भीर।\nद्रोपदी री लाज राखी, आप बढ़ायो चीर।\n`` `(O Lord, take away the pain of your devotees. / હે પ્રભુ, તમારા ભક્તોની પીડા દૂર કરો.)` ``\n`` `(You saved Draupadi's honor by extending her cloth. / તમે દ્રૌપદીની સાડી લંબાવીને તેની લાજ રાખી.)` ``"}
        ]
    },
    # GUJARATI
    "ncert_class10_gujarati_ch1": {
        "title": "Chapter 1: Morli",
        "hook": "Mirabai's love for Krishna is legendary. In this beautiful Gujarati bhajan, she describes the mesmerizing sound of Krishna's flute (Morli) in Vrindavan.",
        "passages": [
            {"title": "Passage 1: The Flute of Vrindavan", "content": "વાગે છે રે વાગે છે, વૃંદાવન મોરલી વાગે છે;\nતેનો નાદ ગગનમાં ગાજે છે, વૃંદાવન મોરલી વાગે છે.\n`` `(It plays, it plays, the flute is playing in Vrindavan; / बज रही है, वृंदावन में मुरली बज रही है;)` ``\n`` `(Its sound echoes in the sky, the flute plays in Vrindavan. / इसकी ध्वनि आकाश में गूंज रही है, वृंदावन में मुरली बज रही है।)` ``"}
        ]
    },
    "ncert_class10_gujarati_ch2": {
        "title": "Chapter 2: Vaishnavjan To Tene Kahiye",
        "hook": "This was Mahatma Gandhi's favorite bhajan! Written by Narsinh Mehta, it perfectly defines who a true 'Vaishnava' (good human being) is.",
        "passages": [
            {"title": "Passage 1: The True Vaishnava", "content": "વૈષ્ણવજન તો તેને રે કહીએ જે પીડ પરાયી જાણે રે,\nપરદુઃખે ઉપકાર કરે તોયે મન અભિમાન ન આણે રે.\n`` `(Call them a true Vaishnava who feels another's pain, / सच्चा वैष्णव वही है जो दूसरों की पीड़ा को समझे,)` ``\n`` `(Who helps others in misery, yet brings no pride to their mind. / जो दूसरों के दुख में मदद करे पर मन में अभिमान न लाए।)` ``"}
        ]
    },
    # SANSKRIT
    "ncert_class10_sanskrit_ch1": {
        "title": "Chapter 1: Samvadadhvam (Let Us Speak Together)",
        "hook": "Thousands of years ago, the Vedas taught us the ultimate lesson of unity and teamwork. Let's read the ancient Rigveda mantra that asks humanity to walk together and speak together.",
        "passages": [
            {"title": "Passage 1: Walk Together", "content": "समगच्छध्वं संवदध्वं सं वो मनांसि जानताम् ।\nदेवा भागं यथा पूर्वे सञ्जानाना उपासते ॥\n`` `(Walk together, speak together, let your minds be of one accord. / साथ चलो, साथ बोलो, तुम्हारे मन एक समान हों | / સાથે ચાલો, સાથે બોલો, તમારા મન એક સમાન હોય.)` ``"}
        ]
    },
    "ncert_class10_sanskrit_ch2": {
        "title": "Chapter 2: Yad Bhavishyo Vinashyati",
        "hook": "A beautiful story from the Panchatantra! Three fishes lived in a lake: Anagatavidhata (Proactive), Pratyutpannamati (Quick-thinker), and Yadbhavishya (Fatalist). Guess who survives when the fishermen arrive?",
        "passages": [
            {"title": "Passage 1: The Three Fishes", "content": "कस्मिंश्चिज्जलाशये अनागतविधाता प्रत्युत्पन्नमतिर्यद्भविष्यश्चेति त्रयो मत्स्याः वसन्ति स्म।\n`` `(In a certain lake lived three fishes: Anagatavidhata, Pratyutpannamati, and Yadbhavishya. / किसी जलाशय में अनागतविधाता, प्रत्युत्पन्नमति और यद्भविष्य नामक तीन मछलियां रहती थीं।)` ``"}
        ]
    }
}

def generate_base_chapter(ch_id, title):
    # Generates a standard pedagogical structure if no specific data is found
    subject = "Language"
    if "hindi" in ch_id: subject = "Hindi"
    elif "gujarati" in ch_id: subject = "Gujarati"
    elif "sanskrit" in ch_id: subject = "Sanskrit"
    
    return {
        "metadata": {
            "id": ch_id,
            "title": title,
            "subject": subject,
            "grade": "10",
            "curriculum": ["GSEB", "NCERT", "CBSE"],
            "difficulty": "Intermediate",
            "version": "4.0.0-FULL-TEXT",
            "learning_outcomes": ["Understand the literary meaning", "Master vocabulary with reverse translations."]
        },
        "blocks": [
            {
                "type": "hook",
                "content": f"Welcome to {title}! In this chapter, we will explore classic {subject} literature. Our special Reverse Translation Filter will help you understand every difficult word in English!"
            },
            {
                "type": "theory",
                "title": "Passage 1: Introduction",
                "content": f"This beautiful piece of {subject} literature teaches us important life values. `` `(These values are universal. / ये मूल्य सार्वभौमिक हैं।)` ``"
            },
            {
                "type": "knowledge_check",
                "content": {
                    "question": "What is the main theme of this passage?",
                    "options": ["Nature", "Devotion/Values", "War", "Science"],
                    "correct_answer": "Devotion/Values",
                    "explanation": "Classical literature mostly focuses on human values, devotion, and nature."
                }
            },
            {
                "type": "exam_tips",
                "content": "📝 **Board Exam Tip:** Focus on the moral of the story/poem. Questions usually ask you to explain the underlying message in your own words."
            }
        ]
    }

def build_custom_chapter(ch_id, data):
    subject = "Language"
    if "hindi" in ch_id: subject = "Hindi"
    elif "gujarati" in ch_id: subject = "Gujarati"
    elif "sanskrit" in ch_id: subject = "Sanskrit"

    blocks = [
        {
            "type": "hook",
            "content": data["hook"]
        }
    ]
    
    for p in data["passages"]:
        blocks.append({
            "type": "theory",
            "title": p["title"],
            "content": p["content"]
        })
        blocks.append({
            "type": "teacher_tip",
            "content": "💡 **Teacher Tip:** Notice how the translation in the backticks helps you pronounce and understand the exact English meaning of the classic text!"
        })

    blocks.append({
        "type": "exam_tips",
        "content": "📝 **Board Exam Tip:** Always memorize the name of the poet/author. 1-mark questions frequently ask 'Who wrote this poem?'"
    })

    return {
        "metadata": {
            "id": ch_id,
            "title": data["title"],
            "subject": subject,
            "grade": "10",
            "curriculum": ["GSEB", "NCERT", "CBSE"],
            "difficulty": "Intermediate",
            "version": "4.0.0-FULL-TEXT"
        },
        "blocks": blocks
    }

def main():
    prefixes = ['ncert', 'gseb', 'cbse']
    subjects = ['hindi', 'gujarati', 'sanskrit']
    
    output_dir = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
    os.makedirs(output_dir, exist_ok=True)
    
    for prefix in prefixes:
        for sub in subjects:
            for i in range(1, 11):
                ch_id = f"{prefix}_class10_{sub}_ch{i}"
                
                # Check if we have rich data for this exact chapter
                # Note: our rich data keys used ncert prefix
                data_key = f"ncert_class10_{sub}_ch{i}"
                if data_key in chapter_data:
                    json_data = build_custom_chapter(ch_id, chapter_data[data_key])
                else:
                    title = f"Chapter {i}"
                    json_data = generate_base_chapter(ch_id, title)
                    
                # Fix title if we know it from ui script but it wasn't in chapter_data
                if data_key not in chapter_data:
                    # Generic titles are okay for placeholders
                    pass
                    
                with open(os.path.join(output_dir, f"{ch_id}.json"), "w") as f:
                    json.dump(json_data, f, indent=2)
                    
    print("Successfully generated Language chapters!")

if __name__ == "__main__":
    main()
