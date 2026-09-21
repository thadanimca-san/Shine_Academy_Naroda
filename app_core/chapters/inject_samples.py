import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_maths_ch1.json'
with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

sample_blocks = [
  {
    "id": "SAMPLE_HOOK",
    "type": "hook",
    "title": "The Mystery of Prime Numbers",
    "title_hi": "अभाज्य संख्याओं का रहस्य",
    "title_gu": "અવિભાજ્ય સંખ્યાઓનું રહસ્ય",
    "body": "Have you ever wondered how your online messages are kept secure? It all comes down to prime numbers! Let's explore the magic of Real Numbers.",
    "body_hi": "क्या आपने कभी सोचा है कि आपके ऑनलाइन संदेश सुरक्षित कैसे रहते हैं? यह सब अभाज्य संख्याओं के कारण है! आइए वास्तविक संख्याओं के जादू का पता लगाएं।",
    "body_gu": "શું તમે ક્યારેય વિચાર્યું છે કે તમારા ઓનલાઇન સંદેશાઓ કેવી રીતે સુરક્ષિત રહે છે? આ બધું અવિભાજ્ય સંખ્યાઓને કારણે છે! ચાલો વાસ્તવિક સંખ્યાઓના જાદુનું અન્વેષણ કરીએ."
  },
  {
    "id": "SAMPLE_SOCRATIC",
    "type": "socratic_question",
    "title": "Think About It",
    "title_hi": "इस पर विचार करें",
    "title_gu": "આના વિશે વિચારો",
    "body": "If you multiply two prime numbers together, how many factors will the resulting number have?",
    "body_hi": "यदि आप दो अभाज्य संख्याओं को एक साथ गुणा करते हैं, तो परिणामी संख्या के कितने गुणनखंड होंगे?",
    "body_gu": "જો તમે બે અવિભાજ્ય સંખ્યાઓનો ગુણાકાર કરો છો, તો પરિણામી સંખ્યામાં કેટલા અવયવ હશે?",
    "options": ["2", "3", "4", "Infinite"],
    "options_hi": ["2", "3", "4", "अनंत"],
    "options_gu": ["2", "3", "4", "અનંત"],
    "correct_index": 2,
    "explanation": "It will have 4 factors: 1, the first prime, the second prime, and the product itself.",
    "explanation_hi": "इसके 4 गुणनखंड होंगे: 1, पहला अभाज्य, दूसरा अभाज्य, और स्वयं गुणनफल।",
    "explanation_gu": "તેમાં 4 અવયવો હશે: 1, પ્રથમ અવિભાજ્ય, બીજી અવિભાજ્ય, અને ઉત્પાદન પોતે."
  },
  {
    "id": "SAMPLE_DISCOVERY",
    "type": "discovery",
    "title": "Building Blocks",
    "title_hi": "निर्माण खंड",
    "title_gu": "બિલ્ડીંગ બ્લોક્સ",
    "body": "Just like every wall is made of individual bricks, every number is made of prime numbers multiplied together. This is the fundamental rule of arithmetic.",
    "body_hi": "जैसे हर दीवार ईंटों से बनी होती है, वैसे ही हर संख्या अभाज्य संख्याओं को गुणा करके बनी होती है। यह अंकगणित का मूल नियम है।",
    "body_gu": "જેમ દરેક દિવાલ ઇંટોથી બનેલી છે, તેમ દરેક સંખ્યા અવિભાજ્ય સંખ્યાઓનો ગુણાકાર કરીને બનેલી છે. આ અંકગણિતનો મૂળભૂત નિયમ છે."
  },
  {
    "id": "SAMPLE_REFLECTION",
    "type": "reflection",
    "title": "Your Turn",
    "title_hi": "आपकी बारी",
    "title_gu": "તમારો વારો",
    "body": "Close your eyes and try to explain what a 'composite number' is to an imaginary friend. If you can explain it simply, you've mastered it!",
    "body_hi": "अपनी आँखें बंद करें और एक काल्पनिक दोस्त को 'भाज्य संख्या' क्या है, यह समझाने का प्रयास करें। यदि आप इसे सरलता से समझा सकते हैं, तो आपने इसमें महारत हासिल कर ली है!",
    "body_gu": "તમારી આંખો બંધ કરો અને કાલ્પનિક મિત્રને 'સંયુક્ત સંખ્યા' શું છે તે સમજાવવાનો પ્રયાસ કરો. જો તમે તેને સરળતાથી સમજાવી શકો, તો તમે તેમાં નિપુણતા પ્રાપ્ત કરી છે!"
  },
  {
    "id": "SAMPLE_MASTERY",
    "type": "mastery",
    "title": "The Final Challenge",
    "title_hi": "अंतिम चुनौती",
    "title_gu": "અંતિમ પડકાર",
    "body": "You now have all the tools. Apply Euclid's Division Lemma to find the HCF of 455 and 42 on a piece of paper.",
    "body_hi": "अब आपके पास सभी उपकरण हैं। एक कागज के टुकड़े पर 455 और 42 का HCF खोजने के लिए यूक्लिड के विभाजन लेम्मा को लागू करें।",
    "body_gu": "હવે તમારી પાસે બધા સાધનો છે. કાગળના ટુકડા પર 455 અને 42 ના HCF શોધવા માટે યુક્લિડના ભાગાકાર લેમ્માને લાગુ કરો."
  }
]

# Insert after title and description, so say at index 0 or 1
data['blocks'] = sample_blocks + data['blocks']

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)

print("Injected successfully!")
