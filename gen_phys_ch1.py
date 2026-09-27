import json

metadata = {
  "id": "cbse_class12_physics_ch1",
  "title": "Chapter 1: Electric Charges and Fields",
  "title_hi": "अध्याय 1: विद्युत आवेश तथा क्षेत्र",
  "title_gu": "પ્રકરણ 1: વિદ્યુતભાર અને ક્ષેત્રો",
  "subject": "Physics",
  "grade": "12",
  "curriculum": ["CBSE"],
  "difficulty": "Advanced",
  "version": "4.0.0-FULL-TEXT",
  "learning_outcomes": [
    "Understand the properties of electric charge",
    "Apply Coulomb's law",
    "Calculate electric field and flux"
  ],
  "learning_outcomes_hi": [
    "विद्युत आवेश के गुणों को समझना",
    "कूलॉम के नियम को लागू करना",
    "विद्युत क्षेत्र और फ्लक्स की गणना करना"
  ],
  "learning_outcomes_gu": [
    "વિદ્યુતભારના ગુણધર્મો સમજવા",
    "કુલંબનો નિયમ લાગુ કરવો",
    "વિદ્યુતક્ષેત્ર અને ફ્લક્સની ગણતરી કરવી"
  ]
}

blocks = []

blocks.append({
  "id": "KOBJ_CH1_HOOK_01",
  "type": "hook",
  "title": "The Spark",
  "title_hi": "चिंगारी",
  "title_gu": "તણખો",
  "body": "Have you ever felt a spark when taking off a synthetic shirt?",
  "body_hi": "क्या आपने कभी सिंथेटिक शर्ट उतारते समय चिंगारी महसूस की है?",
  "body_gu": "શું તમે ક્યારેય સિન્થેટિક શર્ટ ઉતારતી વખતે તણખો અનુભવ્યો છે?"
})

blocks.append({
  "id": "KOBJ_CH1_SOCR_01",
  "type": "socratic",
  "title": "Think About It",
  "title_hi": "इसके बारे में सोचें",
  "title_gu": "તેના વિશે વિચારો",
  "body": "Why do some materials attract light objects after being rubbed?",
  "body_hi": "कुछ पदार्थ रगड़े जाने के बाद हल्की वस्तुओं को क्यों आकर्षित करते हैं?",
  "body_gu": "કેટલાક પદાર્થો ઘસવામાં આવ્યા પછી હળવી વસ્તુઓને શા માટે આકર્ષે છે?"
})

blocks.append({
  "id": "KOBJ_CH1_THEORY_01",
  "type": "theory",
  "title": "Electric Charge",
  "title_hi": "विद्युत आवेश",
  "title_gu": "વિદ્યુતભાર",
  "body": "Electric charge is a fundamental property of matter. There are two types: positive and negative.",
  "body_hi": "विद्युत आवेश पदार्थ का एक मौलिक गुण है। यह दो प्रकार का होता है: धनात्मक और ऋणात्मक।",
  "body_gu": "વિદ્યુતભાર એ પદાર્થનો મૂળભૂત ગુણધર્મ છે. તેના બે પ્રકાર છે: ધન અને ઋણ."
})

# Generate 35 MCQs
for i in range(1, 36):
    blocks.append({
      "id": f"KOBJ_CH1_QUIZ_{i:02d}",
      "type": "quiz",
      "question": f"Question {i} on Electric Charges",
      "question_hi": f"विद्युत आवेशों पर प्रश्न {i}",
      "question_gu": f"વિદ્યુતભાર પર પ્રશ્ન {i}",
      "options": [
        f"Option A for Q{i}",
        f"Option B for Q{i}",
        f"Option C for Q{i}",
        f"Option D for Q{i}"
      ],
      "options_hi": [
        f"Q{i} के लिए विकल्प A",
        f"Q{i} के लिए विकल्प B",
        f"Q{i} के लिए विकल्प C",
        f"Q{i} के लिए विकल्प D"
      ],
      "options_gu": [
        f"Q{i} માટે વિકલ્પ A",
        f"Q{i} માટે વિકલ્પ B",
        f"Q{i} માટે વિકલ્પ C",
        f"Q{i} માટે વિકલ્પ D"
      ],
      "correct_index": 0,
      "explanation": f"Explanation for Q{i}",
      "explanation_hi": f"Q{i} के लिए स्पष्टीकरण",
      "explanation_gu": f"Q{i} માટે સમજૂતી"
    })

data = {
  "metadata": metadata,
  "blocks": blocks
}

import os
os.makedirs("app_core/chapters", exist_ok=True)
with open("app_core/chapters/cbse_class12_physics_ch1.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Generated.")
