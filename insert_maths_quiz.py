import json
import glob
import os

questions = [
  {
    "id": "KOBJ_CH1_Q1",
    "type": "quiz",
    "question": "Which of the following numbers belongs to the family of Real Numbers?",
    "question_hi": "निम्नलिखित में से कौन सी संख्या वास्तविक संख्याओं (Real Numbers) के परिवार से संबंधित है?",
    "options": [
      "Only Rational numbers",
      "Only Irrational numbers",
      "Both Rational and Irrational numbers",
      "Only Integers"
    ],
    "options_hi": [
      "केवल परिमेय संख्याएँ",
      "केवल अपरिमेय संख्याएँ",
      "परिमेय और अपरिमेय दोनों संख्याएँ",
      "केवल पूर्णांक"
    ],
    "correct_index": 2,
    "explanation": "As seen in the Number Tree, the family of Real Numbers includes all Rational and Irrational numbers.",
    "explanation_hi": "जैसा कि नंबर ट्री में देखा गया है, वास्तविक संख्याओं के परिवार में सभी परिमेय और अपरिमेय संख्याएँ शामिल हैं।"
  },
  {
    "id": "KOBJ_CH1_Q2",
    "type": "quiz",
    "question": "According to the Fundamental Theorem of Arithmetic, what is the prime factorisation of 12?",
    "question_hi": "अंकगणित की आधारभूत प्रमेय के अनुसार, 12 का अभाज्य गुणनखंड (prime factorisation) क्या है?",
    "options": [
      "3 × 4",
      "2² × 3",
      "2 × 6",
      "2³ × 3"
    ],
    "options_hi": [
      "3 × 4",
      "2² × 3",
      "2 × 6",
      "2³ × 3"
    ],
    "correct_index": 1,
    "explanation": "12 = 2 × 2 × 3, which is uniquely written as 2² × 3 using prime factors.",
    "explanation_hi": "12 = 2 × 2 × 3, जिसे अभाज्य गुणनखंडों का उपयोग करके 2² × 3 के रूप में विशिष्ट रूप से लिखा जाता है।"
  },
  {
    "id": "KOBJ_CH1_Q3",
    "type": "quiz",
    "question": "If you know that HCF(a, b) = 4 and LCM(a, b) = 24, and one number 'a' is 8, what is the value of 'b'?",
    "question_hi": "यदि आप जानते हैं कि HCF(a, b) = 4 और LCM(a, b) = 24 है, और एक संख्या 'a' 8 है, तो 'b' का मान क्या है?",
    "options": [
      "6",
      "12",
      "16",
      "24"
    ],
    "options_hi": [
      "6",
      "12",
      "16",
      "24"
    ],
    "correct_index": 1,
    "explanation": "Using the Board Exam trick: HCF × LCM = a × b. So, 4 × 24 = 8 × b. Therefore, 96 = 8b, which means b = 12.",
    "explanation_hi": "बोर्ड परीक्षा ट्रिक का उपयोग करते हुए: HCF × LCM = a × b। इसलिए, 4 × 24 = 8 × b। अतः 96 = 8b, जिसका अर्थ है b = 12।"
  },
  {
    "id": "KOBJ_CH1_Q4",
    "type": "quiz",
    "question": "Which of the following is an Irrational number?",
    "question_hi": "निम्नलिखित में से कौन सी एक अपरिमेय (Irrational) संख्या है?",
    "options": [
      "22/7",
      "√4",
      "√2",
      "1.5"
    ],
    "options_hi": [
      "22/7",
      "√4",
      "√2",
      "1.5"
    ],
    "correct_index": 2,
    "explanation": "√2 cannot be written in the form p/q. (Note: 22/7 is a rational approximation of π, but π itself is irrational).",
    "explanation_hi": "√2 को p/q के रूप में नहीं लिखा जा सकता है। (ध्यान दें: 22/7, π का एक परिमेय सन्निकटन है, लेकिन π स्वयं अपरिमेय है)।"
  },
  {
    "id": "KOBJ_CH1_Q5",
    "type": "quiz",
    "question": "Using the '2 and 5 Rule', will the fraction 7/20 have a terminating or non-terminating decimal expansion?",
    "question_hi": "'2 और 5 के नियम' का उपयोग करते हुए, क्या भिन्न 7/20 का दशमलव प्रसार शांत (terminating) होगा या अशांत (non-terminating)?",
    "options": [
      "Terminating",
      "Non-terminating repeating",
      "Non-terminating non-repeating",
      "Cannot be determined"
    ],
    "options_hi": [
      "शांत (Terminating)",
      "अशांत आवर्ती (Non-terminating repeating)",
      "अशांत अनावर्ती (Non-terminating non-repeating)",
      "निर्धारित नहीं किया जा सकता"
    ],
    "correct_index": 0,
    "explanation": "The denominator is 20. Its prime factors are 2² × 5. Since it only contains 2s and 5s, the decimal expansion is terminating.",
    "explanation_hi": "हर 20 है। इसके अभाज्य गुणनखंड 2² × 5 हैं। चूँकि इसमें केवल 2 और 5 हैं, दशमलव प्रसार शांत है।"
  }
]

def add_quizzes(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
            
        if 'blocks' not in data:
            return
            
        blocks = data['blocks']
        
        # Check if quizzes already exist
        if any(b.get('type') == 'quiz' for b in blocks):
            print(f"Quizzes already exist in {file_path}")
            return
            
        print(f"Adding 5 valid MCQs to {file_path}")
        blocks.extend(questions)
        
        with open(file_path, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            
    except Exception as e:
        print(f"Error processing {file_path}: {e}")

files = glob.glob('app_core/chapters/*class10_maths_ch1.json')
for file in files:
    add_quizzes(file)
