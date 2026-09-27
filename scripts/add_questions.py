import json
import os

file_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class12_economics_ch7.json"

with open(file_path, "r", encoding="utf-8") as f:
    data = json.load(f)

blocks = data.get("blocks", [])
start_id = 21

def get_id():
    global start_id
    id_str = f"KOBJ_GSEB_CLASS12_ECONOMICS_CH7_{start_id:02d}"
    start_id += 1
    return id_str

mcqs = [
    {
        "q": "Who was responsible for the introduction of population census for the first time in India ?",
        "q_hi": "भारत में पहली बार जनसंख्या जनगणना शुरू करने के लिए कौन जिम्मेदार था?",
        "q_gu": "ભારતમાં પ્રથમ વખત વસ્તી ગણતરી શરૂ કરવા માટે કોણ જવાબદાર હતું?",
        "options": ["Jamshedji Tata", "Swaminathan", "Deendayal Upadhyay", "Dadabhai Naoroji"],
        "options_hi": ["जमशेदजी टाटा", "स्वामीनाथन", "दीनदयाल उपाध्याय", "दादाभाई नौरोजी"],
        "options_gu": ["જમશેદજી ટાટા", "સ્વામીનાથન", "દીનદયાળ ઉપાધ્યાય", "દાદાભાઈ નૌરોજી"],
        "correct_index": 0
    },
    {
        "q": "What is the estimated population of India between 2011-2025 ?",
        "q_hi": "2011-2025 के बीच भारत की अनुमानित जनसंख्या क्या है?",
        "q_gu": "2011-2025 ની વચ્ચે ભારતની અંદાજિત વસ્તી કેટલી છે?",
        "options": ["155 crores", "130 crores", "139.98 crores", "180 crores"],
        "options_hi": ["155 करोड़", "130 करोड़", "139.98 करोड़", "180 करोड़"],
        "options_gu": ["155 કરોડ", "130 કરોડ", "139.98 કરોડ", "180 કરોડ"],
        "correct_index": 2
    },
    {
        "q": "In which year the first population census was under taken in India ?",
        "q_hi": "भारत में पहली जनसंख्या जनगणना किस वर्ष की गई थी?",
        "q_gu": "ભારતમાં પ્રથમ વસ્તી ગણતરી કયા વર્ષમાં હાથ ધરવામાં આવી હતી?",
        "options": ["1901", "1951", "1871", "1921"],
        "options_hi": ["1901", "1951", "1871", "1921"],
        "options_gu": ["1901", "1951", "1871", "1921"],
        "correct_index": 2
    },
    {
        "q": "How much was India's population in 1901 ?",
        "q_hi": "1901 में भारत की जनसंख्या कितनी थी?",
        "q_gu": "1901 માં ભારતની વસ્તી કેટલી હતી?",
        "options": ["22.2 crores", "25.2 crores", "102.7 crores", "23.8 crores"],
        "options_hi": ["22.2 करोड़", "25.2 करोड़", "102.7 करोड़", "23.8 करोड़"],
        "options_gu": ["22.2 કરોડ", "25.2 કરોડ", "102.7 કરોડ", "23.8 કરોડ"],
        "correct_index": 3
    },
    {
        "q": "How much was India's population in the year 2011?",
        "q_hi": "वर्ष 2011 में भारत की जनसंख्या कितनी थी?",
        "q_gu": "વર્ષ 2011 માં ભારતની વસ્તી કેટલી હતી?",
        "options": ["36.1 crores", "54.8 crores", "121.02 crores", "23.8 crores"],
        "options_hi": ["36.1 करोड़", "54.8 करोड़", "121.02 करोड़", "23.8 करोड़"],
        "options_gu": ["36.1 કરોડ", "54.8 કરોડ", "121.02 કરોડ", "23.8 કરોડ"],
        "correct_index": 2
    },
    {
        "q": "In which year was planning started in India?",
        "q_hi": "भारत में नियोजन किस वर्ष शुरू किया गया था?",
        "q_gu": "ભારતમાં આયોજનની શરૂઆત કયા વર્ષમાં થઈ હતી?",
        "options": ["1901", "1951", "1950", "2000"],
        "options_hi": ["1901", "1951", "1950", "2000"],
        "options_gu": ["1901", "1951", "1950", "2000"],
        "correct_index": 1
    },
    {
        "q": "Which country in the world, has the largest population?",
        "q_hi": "दुनिया के किस देश की जनसंख्या सबसे अधिक है?",
        "q_gu": "વિશ્વના કયા દેશની વસ્તી સૌથી વધુ છે?",
        "options": ["China", "India", "Australia", "America"],
        "options_hi": ["चीन", "भारत", "ऑस्ट्रेलिया", "अमेरिका"],
        "options_gu": ["ચીન", "ભારત", "ઓસ્ટ્રેલિયા", "અમેરિકા"],
        "correct_index": 0
    },
    {
        "q": "Which state in India has the highest female population per 1000 males?",
        "q_hi": "भारत के किस राज्य में प्रति 1000 पुरुषों पर महिलाओं की संख्या सबसे अधिक है?",
        "q_gu": "ભારતના કયા રાજ્યમાં દર 1000 પુરુષો દીઠ સ્ત્રીઓની સંખ્યા સૌથી વધુ છે?",
        "options": ["Gujarat", "Maharashtra", "Kerala", "Uttar Pradesh"],
        "options_hi": ["गुजरात", "महाराष्ट्र", "केरल", "उत्तर प्रदेश"],
        "options_gu": ["ગુજરાત", "મહારાષ્ટ્ર", "કેરળ", "ઉત્તર પ્રદેશ"],
        "correct_index": 2
    },
    {
        "q": "How much was the female population per 1000 male population in India in 2011?",
        "q_hi": "2011 में भारत में प्रति 1000 पुरुष जनसंख्या पर महिला जनसंख्या कितनी थी?",
        "q_gu": "2011 માં ભારતમાં દર 1000 પુરુષો દીઠ સ્ત્રીઓની વસ્તી કેટલી હતી?",
        "options": ["930", "950", "940", "970"],
        "options_hi": ["930", "950", "940", "970"],
        "options_gu": ["930", "950", "940", "970"],
        "correct_index": 2
    },
    {
        "q": "What was India's birth-rate in 2011?",
        "q_hi": "2011 में भारत की जन्म दर क्या थी?",
        "q_gu": "2011 માં ભારતનો જન્મદર શું હતો?",
        "options": ["21.8", "36.8", "72.0", "23.8"],
        "options_hi": ["21.8", "36.8", "72.0", "23.8"],
        "options_gu": ["21.8", "36.8", "72.0", "23.8"],
        "correct_index": 0
    }
]

for m in mcqs:
    block = {
        "id": get_id(),
        "type": "mcq",
        "question": m["q"],
        "question_hi": m["q_hi"],
        "question_gu": m["q_gu"],
        "options": m["options"],
        "options_hi": m["options_hi"],
        "options_gu": m["options_gu"],
        "correct_index": m["correct_index"],
        "explanation": "Refer to the textbook for detailed understanding.",
        "explanation_hi": "विस्तृत समझ के लिए पाठ्यपुस्तक देखें।",
        "explanation_gu": "વિગતવાર સમજ માટે પાઠ્યપુસ્તકનો સંદર્ભ લો."
    }
    blocks.append(block)

practice_qs = [
    # One Line
    ("What has been the basic cause for all the problems?", 
     "सभी समस्याओं का मूल कारण क्या रहा है?", 
     "તમામ સમસ્યાઓનું મૂળ કારણ શું રહ્યું છે?"),
    ("What is meant by working and non working population?", 
     "कार्यशील और गैर-कार्यशील जनसंख्या से क्या तात्पर्य है?", 
     "કાર્યશીલ અને બિન-કાર્યશીલ વસ્તી એટલે શું?"),
    ("What was the population growth rate in 2011?", 
     "2011 में जनसंख्या वृद्धि दर क्या थी?", 
     "2011 માં વસ્તી વૃદ્ધિ દર શું હતો?"),
    ("Where does India stand in the world population order?", 
     "विश्व जनसंख्या क्रम में भारत कहाँ खड़ा है?", 
     "વિશ્વ વસ્તી ક્રમમાં ભારત ક્યાં ઊભું છે?"),
    ("What was the female population per 1000 males in Gujarat in 2011?", 
     "2011 में गुजरात में प्रति 1000 पुरुषों पर महिलाओं की जनसंख्या कितनी थी?", 
     "2011 માં ગુજરાતમાં દર 1000 પુરુષો દીઠ સ્ત્રીઓની વસ્તી કેટલી હતી?"),
    ("What is meant by classification of population according to age group?", 
     "आयु समूह के अनुसार जनसंख्या के वर्गीकरण का क्या अर्थ है?", 
     "વય જૂથ મુજબ વસ્તીના વર્ગીકરણનો અર્થ શું છે?"),
    ("Which age group has the highest population in India?", 
     "भारत में किस आयु वर्ग की जनसंख्या सबसे अधिक है?", 
     "ભારતમાં કયા વય જૂથની વસ્તી સૌથી વધુ છે?"),
    ("State the percentage of rural urban population in India in the year 2011?", 
     "वर्ष 2011 में भारत में ग्रामीण शहरी जनसंख्या का प्रतिशत बताइए?", 
     "વર્ષ 2011 માં ભારતમાં ગ્રામીણ શહેરી વસ્તીની ટકાવારી જણાવો?"),
    ("What is meant by infant mortality rate?", 
     "शिशु मृत्यु दर से क्या तात्पर्य है?", 
     "બાળ મૃત્યુ દર એટલે શું?"),

    # Brief
    ("Why is the year 1921 identified as the year of 'great divide'?", 
     "वर्ष 1921 को 'महा विभाजन' के वर्ष के रूप में क्यों पहचाना जाता है?", 
     "વર્ષ 1921 ને 'મહા વિભાજન' ના વર્ષ તરીકે શા માટે ઓળખવામાં આવે છે?"),
    ("What is meant by productive and unproductive population?", 
     "उत्पादक और अनुत्पादक जनसंख्या से क्या तात्पर्य है?", 
     "ઉત્પાદક અને બિન-ઉત્પાદક વસ્તી એટલે શું?"),
    ("Give the meaning of birth-rate and state the formula to calculate birth-rate.", 
     "जन्म दर का अर्थ दें और जन्म दर की गणना करने का सूत्र बताएं।", 
     "જન્મદરનો અર્થ આપો અને જન્મદરની ગણતરી કરવાનું સૂત્ર જણાવો."),
    ("Give the meaning of death-rate and state the formula to calculate death-rate.", 
     "मृत्यु दर का अर्थ दें और मृत्यु दर की गणना करने का सूत्र बताएं।", 
     "મૃત્યુદરનો અર્થ આપો અને મૃત્યુદરની ગણતરી કરવાનું સૂત્ર જણાવો."),
    ("Give the meaning of population policy.", 
     "जनसंख्या नीति का अर्थ स्पष्ट करें।", 
     "વસ્તી નીતિનો અર્થ સ્પષ્ટ કરો."),

    # Pin Pointed
    ("Explain population explosion.", 
     "जनसंख्या विस्फोट की व्याख्या करें।", 
     "વસ્તી વિસ્ફોટ સમજાવો."),
    ("State the causes of low death-rate.", 
     "निम्न मृत्यु दर के कारण बताइए।", 
     "નીચા મૃત્યુદરના કારણો જણાવો."),

    # Detailed
    ("Discuss in detail the gender ratio (number of females per 1000 males)", 
     "लिंग अनुपात (प्रति 1000 पुरुषों पर महिलाओं की संख्या) पर विस्तार से चर्चा करें।", 
     "લિંગ પ્રમાણ (દર 1000 પુરુષો દીઠ સ્ત્રીઓની સંખ્યા) ની વિગતવાર ચર્ચા કરો."),
    ("Discuss in detail the causes for high birth-rate.", 
     "उच्च जन्म दर के कारणों पर विस्तार से चर्चा करें।", 
     "ઊંચા જન્મદરના કારણોની વિગતવાર ચર્ચા કરો."),
    ("Explain in detail the methods to control population.", 
     "जनसंख्या को नियंत्रित करने के तरीकों के बारे में विस्तार से बताएं।", 
     "વસ્તીને નિયંત્રित કરવાની પદ્ધતિઓ વિગતવાર સમજાવો.")
]

for q, q_hi, q_gu in practice_qs:
    block = {
        "id": get_id(),
        "type": "practice_question",
        "question": q,
        "question_hi": q_hi,
        "question_gu": q_gu,
        "explanation": "Refer to the textbook for the detailed answer.",
        "explanation_hi": "विस्तृत उत्तर के लिए पाठ्यपुस्तक देखें।",
        "explanation_gu": "વિગતવાર જવાબ માટે પાઠ્યપુસ્તકનો સંદર્ભ લો."
    }
    blocks.append(block)

data["blocks"] = blocks

with open(file_path, "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated {file_path} with {len(blocks)} blocks total.")
