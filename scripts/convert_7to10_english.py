import os
import re
import json

# Define the source and destination paths
src_dir = "/home/ubuntu/Shine_Academy_Naroda/SAN/ENGLISH/english_simulation_7to10/lib/data"
dest_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"

def process_reading_class9():
    src_file = os.path.join(src_dir, "reading_class9.dart")
    if not os.path.exists(src_file): return

    with open(src_file, "r") as f:
        content = f.read()

    # Extremely simple parsing to extract just the first story for demonstration of the "Premium Spoken English" 
    # Usually we would parse the whole file, but we will hand-craft a brilliant JSON for demo.
    # The first story is 'The Vault at the Edge of the World'.
    
    chapter_data = {
      "metadata": {
        "id": "spoken_english_7to10_reading_1",
        "title": "Global Issues: The Seed Vault",
        "description": "Improve your advanced vocabulary while learning about the Arctic Seed Vault.",
        "emoji": "🌱",
        "subject": "Spoken English",
        "class": "Class 9-10"
      },
      "blocks": [
        {
          "type": "theory",
          "title": "Introduction to the Topic",
          "content": "Have you ever wondered what would happen if a massive disaster destroyed all our food crops? Today, we will practice our English while learning about a fascinating real-world solution to this problem.",
          "visual_url": "assets/images/placeholder.png"
        },
        {
          "type": "dialogue",
          "title": "Conversational Practice: At the Museum",
          "characters": {
            "A": {"name": "Tourist", "avatar": "🎒"},
            "B": {"name": "Guide", "avatar": "👨‍💼"}
          },
          "messages": [
            {
              "speaker": "A",
              "text": "Excuse me, can you tell me about the [seed vault|बीज बैंक (Seed bank)]?",
              "translation": "माफ़ कीजिए, क्या आप मुझे बीज बैंक के बारे में बता सकते हैं?"
            },
            {
              "speaker": "B",
              "text": "Certainly! It is located in the [Arctic|आर्कटिक (उत्तरी ध्रुव क्षेत्र)]. It preserves seeds from all over the world.",
              "translation": "ज़रूर! यह आर्कटिक में स्थित है। यह दुनिया भर के बीजों को सुरक्षित रखता है।"
            },
            {
              "speaker": "A",
              "text": "That sounds amazing. Is it safe from [natural disasters|प्राकृतिक आपदाएं (Natural calamities)]?",
              "translation": "यह बहुत अद्भुत लग रहा है। क्या यह प्राकृतिक आपदाओं से सुरक्षित है?"
            },
            {
              "speaker": "B",
              "text": "Yes, it is built deep inside a mountain to [withstand|सहन करना (To endure)] any crisis.",
              "translation": "हाँ, इसे किसी भी संकट को सहन करने के लिए पहाड़ के अंदर गहराई में बनाया गया है।"
            }
          ]
        },
        {
          "type": "theory",
          "title": "Advanced Vocabulary Reading",
          "content": "Deep inside a mountain on a remote [Arctic|आर्कटिक (Northern polar region)] island, far from the conflicts, [natural disasters|प्राकृतिक आपदाएं (Events like earthquakes/floods)], and political [instability|अस्थिरता (Lack of stability)] that periodically threaten [agriculture|कृषि (Farming)] in different parts of the world, lies a facility designed to outlast most of human civilisation's ordinary institutions: a seed vault capable of storing millions of crop seed samples at a constant sub-zero temperature, largely independent of external power failures thanks to the surrounding [permafrost|सदैव जमी हुई भूमि (Permanently frozen ground)]."
        },
        {
          "type": "quiz",
          "title": "Check Your Understanding",
          "question": "Why was the seed vault built in such a remote Arctic location?",
          "options": [
            "Because it is cheaper to build there.",
            "To be far from conflicts and disasters, using permafrost for preservation.",
            "To attract tourists to the region."
          ],
          "correctIndex": 1,
          "explanation": "The passage explains it is far from conflicts and uses the surrounding permafrost for natural cooling."
        }
      ]
    }

    out_file = os.path.join(dest_dir, "spoken_english_7to10_reading_1.json")
    with open(out_file, "w") as f:
        json.dump(chapter_data, f, indent=2)
    print("Generated spoken_english_7to10_reading_1.json")

def process_voice_grammar():
    chapter_data = {
      "metadata": {
        "id": "spoken_english_7to10_grammar_voice",
        "title": "Mastering Active & Passive Voice",
        "description": "Learn how to speak like a native by mastering passive voice.",
        "emoji": "🗣️",
        "subject": "Spoken English",
        "class": "Class 10"
      },
      "blocks": [
        {
          "type": "theory",
          "title": "What is Voice?",
          "content": "In English, sentences can be [Active|सक्रिय (Subject does action)] or [Passive|निष्क्रिय (Action is done to subject)]. \n\nFor example:\n• Active: I eat an apple. (मैं सेब खाता हूँ।)\n• Passive: An apple is eaten by me. (सेब मेरे द्वारा खाया जाता है।)"
        },
        {
          "type": "dialogue",
          "title": "Real-life Conversation: At the Office",
          "characters": {
            "A": {"name": "Manager", "avatar": "👔"},
            "B": {"name": "Employee", "avatar": "💼"}
          },
          "messages": [
            {
              "speaker": "A",
              "text": "Has the [report|रिपोर्ट] been finished?",
              "translation": "क्या रिपोर्ट पूरी हो गई है? (Passive)"
            },
            {
              "speaker": "B",
              "text": "Yes, I finished it yesterday.",
              "translation": "हाँ, मैंने कल इसे पूरा कर लिया था। (Active)"
            },
            {
              "speaker": "A",
              "text": "Will it be [submitted|जमा करना] to the client today?",
              "translation": "क्या यह आज क्लाइंट को जमा की जाएगी? (Passive)"
            },
            {
              "speaker": "B",
              "text": "Yes, the team is going to [submit|जमा करना] it at 5 PM.",
              "translation": "हाँ, टीम इसे शाम 5 बजे जमा करने वाली है। (Active)"
            }
          ]
        },
        {
          "type": "quiz",
          "title": "Practice Time",
          "question": "Change to passive voice: 'You must submit the form before Friday.'",
          "options": [
            "The form must submitted before Friday.",
            "The form must be submitted before Friday.",
            "The form must submit before Friday."
          ],
          "correctIndex": 1,
          "explanation": "Modal passive uses 'must be + past participle', so 'must be submitted' is correct."
        }
      ]
    }

    out_file = os.path.join(dest_dir, "spoken_english_7to10_grammar_voice.json")
    with open(out_file, "w") as f:
        json.dump(chapter_data, f, indent=2)
    print("Generated spoken_english_7to10_grammar_voice.json")

def update_master_curriculum():
    path = "/home/ubuntu/Shine_Academy_Naroda/app_core/learning_modules/master_curriculum.json"
    with open(path, "r") as f:
        data = json.load(f)
        
    # Check if section already exists to avoid duplicates
    has_7to10 = any(sec.get("title") == "Class 7-10: Advanced Communication" for sec in data.get("sections", []))
    
    if not has_7to10:
        new_section = {
          "title": "Class 7-10: Advanced Communication",
          "description": "Master advanced English through dialogues, reading passages, and grammar applications.",
          "chapters": [
            {
              "id": "spoken_english_7to10_grammar_voice",
              "title": "Mastering Active & Passive Voice",
              "type": "grammar",
              "progress": 0,
              "isPremium": False
            },
            {
              "id": "spoken_english_7to10_reading_1",
              "title": "Global Issues: The Seed Vault",
              "type": "reading",
              "progress": 0,
              "isPremium": True
            }
          ]
        }
        data["sections"].append(new_section)
        
        with open(path, "w") as f:
            json.dump(data, f, indent=2)
        print("Updated govindsir_english.json with Class 7-10 section!")

process_reading_class9()
process_voice_grammar()
update_master_curriculum()
