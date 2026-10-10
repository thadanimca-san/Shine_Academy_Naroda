/// Hindi and Gujarati for the labels of the learning, quiz-game and paper
/// screens. Looked up by [TrilingualService.getUIText] after its main table.
const Map<String, Map<String, String>> learningUiTranslations = {
  // Lessons
  'Full lesson': {'hi': 'पूरा पाठ', 'gu': 'સંપૂર્ણ પાઠ'},
  'Quick revision': {'hi': 'त्वरित पुनरावृत्ति', 'gu': 'ઝડપી પુનરાવર્તન'},
  'A story to inspire you': {'hi': 'प्रेरणा देने वाली कहानी', 'gu': 'પ્રેરણા આપતી વાર્તા'},
  'Where this can take you': {'hi': 'यह आपको कहाँ तक ले जा सकता है', 'gu': 'આ તમને ક્યાં સુધી લઈ જઈ શકે'},
  'Factor tree': {'hi': 'गुणनखंड वृक्ष', 'gu': 'અવયવ વૃક્ષ'},
  'Factor tree needs a composite number.': {'hi': 'गुणनखंड वृक्ष के लिए भाज्य संख्या चाहिए।', 'gu': 'અવયવ વૃક્ષ માટે વિભાજ્ય સંખ્યા જોઈએ.'},
  'Graph': {'hi': 'आलेख', 'gu': 'આલેખ'},
  'Graph data is missing.': {'hi': 'आलेख का डेटा उपलब्ध नहीं है।', 'gu': 'આલેખની માહિતી ઉપલબ્ધ નથી.'},
  'Figure': {'hi': 'आकृति', 'gu': 'આકૃતિ'},
  'Figure data is missing.': {'hi': 'आकृति का डेटा उपलब्ध नहीं है।', 'gu': 'આકૃતિની માહિતી ઉપલબ્ધ નથી.'},
  'Play again': {'hi': 'फिर से चलाएँ', 'gu': 'ફરી ચલાવો'},
  'You reached the end of the lesson!': {'hi': 'आपने पाठ पूरा पढ़ लिया!', 'gu': 'તમે પાઠ પૂરો વાંચી લીધો!'},
  'Chapter completed! Proud of you.': {'hi': 'अध्याय पूरा हुआ! हमें आप पर गर्व है।', 'gu': 'પ્રકરણ પૂર્ણ થયું! અમને તમારા પર ગર્વ છે.'},
  'Hard work today is success tomorrow. Mark this chapter complete and collect your reward.': {
    'hi': 'आज की मेहनत कल की सफलता है। अध्याय को पूरा चिह्नित करें और अपना इनाम लें।',
    'gu': 'આજની મહેનત એ આવતીકાલની સફળતા છે. પ્રકરણ પૂર્ણ તરીકે નોંધો અને તમારું ઇનામ મેળવો.',
  },
  'Keep the knowledge fresh: play the quiz or do a quick revision tomorrow.': {
    'hi': 'ज्ञान को ताज़ा रखें: क्विज़ खेलें या कल त्वरित पुनरावृत्ति करें।',
    'gu': 'જ્ઞાન તાજું રાખો: ક્વિઝ રમો અથવા આવતીકાલે ઝડપી પુનરાવર્તન કરો.',
  },
  'Mark complete (+500 XP)': {'hi': 'पूरा चिह्नित करें (+500 XP)', 'gu': 'પૂર્ણ તરીકે નોંધો (+500 XP)'},
  'day learning streak': {'hi': 'दिन की सीखने की लय', 'gu': 'દિવસની શીખવાની સળંગ ગતિ'},
  'Could not save your progress. Please try again.': {
    'hi': 'आपकी प्रगति सहेजी नहीं जा सकी। कृपया फिर से प्रयास करें।',
    'gu': 'તમારી પ્રગતિ સાચવી શકાઈ નહીં. કૃપા કરીને ફરી પ્રયાસ કરો.',
  },
  'Good try, but think again!': {'hi': 'अच्छा प्रयास, पर फिर से सोचिए!', 'gu': 'સરસ પ્રયાસ, પણ ફરી વિચારો!'},

  // Quiz game
  'Quiz time!': {'hi': 'क्विज़ का समय!', 'gu': 'ક્વિઝનો સમય!'},
  'Quiz Game': {'hi': 'क्विज़ गेम', 'gu': 'ક્વિઝ ગેમ'},
  'Play Quiz Game': {'hi': 'क्विज़ गेम खेलें', 'gu': 'ક્વિઝ ગેમ રમો'},
  'Exam Mode': {'hi': 'परीक्षा मोड', 'gu': 'પરીક્ષા મોડ'},
  'Learn from every answer, earn XP': {'hi': 'हर उत्तर से सीखें, XP कमाएँ', 'gu': 'દરેક જવાબમાંથી શીખો, XP કમાઓ'},
  'Timed, like the board exam': {'hi': 'समयबद्ध, बोर्ड परीक्षा की तरह', 'gu': 'સમયમર્યાદા સાથે, બોર્ડ પરીક્ષાની જેમ'},
  'Try Exam Mode (timed)': {'hi': 'परीक्षा मोड आज़माएँ (समयबद्ध)', 'gu': 'પરીક્ષા મોડ અજમાવો (સમયમર્યાદા સાથે)'},
  'Excellent! You got it.': {'hi': 'शानदार! आपने सही उत्तर दिया।', 'gu': 'શાબાશ! તમારો જવાબ સાચો છે.'},
  'Well done! You found it on the second try.': {'hi': 'बहुत अच्छे! दूसरे प्रयास में आपने सही उत्तर खोज लिया।', 'gu': 'ખૂબ સરસ! બીજા પ્રયાસમાં તમે સાચો જવાબ શોધી કાઢ્યો.'},
  'Good try! Read why, then pick again.': {'hi': 'अच्छा प्रयास! कारण पढ़ें, फिर दोबारा चुनें।', 'gu': 'સરસ પ્રયાસ! કારણ વાંચો, પછી ફરી પસંદ કરો.'},
  'No worries: now you know it. Here is why.': {'hi': 'कोई बात नहीं: अब आप जान गए। कारण यह है।', 'gu': 'કોઈ વાંધો નહીં: હવે તમે જાણી ગયા. કારણ આ છે.'},
  'Answer': {'hi': 'उत्तर', 'gu': 'જવાબ'},
  'Question': {'hi': 'प्रश्न', 'gu': 'પ્રશ્ન'},
  'Next question': {'hi': 'अगला प्रश्न', 'gu': 'આગળનો પ્રશ્ન'},
  'See my score': {'hi': 'मेरा स्कोर देखें', 'gu': 'મારો સ્કોર જુઓ'},
  'correct': {'hi': 'सही', 'gu': 'સાચા'},
  'Best streak': {'hi': 'सबसे लंबी सही लय', 'gu': 'સૌથી લાંબી સાચી હારમાળા'},
  'Play another round': {'hi': 'एक और राउंड खेलें', 'gu': 'બીજો રાઉન્ડ રમો'},
  'No quiz questions are ready for this chapter yet.': {
    'hi': 'इस अध्याय के लिए अभी क्विज़ प्रश्न तैयार नहीं हैं।',
    'gu': 'આ પ્રકરણ માટે હજુ ક્વિઝ પ્રશ્નો તૈયાર નથી.',
  },
  'Outstanding! You are ready for the board exam on this topic.': {
    'hi': 'उत्कृष्ट! इस विषय में आप बोर्ड परीक्षा के लिए तैयार हैं।',
    'gu': 'ઉત્કૃષ્ટ! આ વિષયમાં તમે બોર્ડ પરીક્ષા માટે તૈયાર છો.',
  },
  'Great work! A little more practice and you will master it.': {
    'hi': 'बहुत बढ़िया! थोड़ा और अभ्यास करें और आप इसमें निपुण हो जाएँगे।',
    'gu': 'ખૂબ સરસ! થોડો વધુ અભ્યાસ કરો અને તમે આમાં નિપુણ બની જશો.',
  },
  'Good effort! Read the lesson once more and play again: you will improve.': {
    'hi': 'अच्छा प्रयास! पाठ एक बार और पढ़ें और फिर खेलें: आप ज़रूर बेहतर करेंगे।',
    'gu': 'સરસ પ્રયાસ! પાઠ ફરી એક વાર વાંચો અને ફરી રમો: તમે જરૂર સુધારો કરશો.',
  },
  'Every expert was once a beginner. Revise the lesson and try again!': {
    'hi': 'हर विशेषज्ञ कभी शुरुआत करने वाला था। पाठ दोहराएँ और फिर प्रयास करें!',
    'gu': 'દરેક નિષ્ણાત ક્યારેક શરૂઆત કરનાર હતો. પાઠનું પુનરાવર્તન કરો અને ફરી પ્રયાસ કરો!',
  },

  // Chapter list
  'Learn': {'hi': 'सीखें', 'gu': 'શીખો'},
  'Practice': {'hi': 'अभ्यास', 'gu': 'અભ્યાસ'},
  'Coming soon': {'hi': 'जल्द आ रहा है', 'gu': 'ટૂંક સમયમાં'},
  'Interactive content ready': {'hi': 'इंटरैक्टिव सामग्री तैयार', 'gu': 'ઇન્ટરએક્ટિવ સામગ્રી તૈયાર'},
  'Premium Content - Requires Activation': {'hi': 'प्रीमियम सामग्री - सक्रियण आवश्यक', 'gu': 'પ્રીમિયમ સામગ્રી - સક્રિયકરણ જરૂરી'},
  'Activate to Unlock': {'hi': 'खोलने के लिए सक्रिय करें', 'gu': 'ખોલવા માટે સક્રિય કરો'},
  'Ask AI Tutor': {'hi': 'AI शिक्षक से पूछें', 'gu': 'AI શિક્ષકને પૂછો'},

  // Papers and PDFs
  'Model answer:': {'hi': 'आदर्श उत्तर:', 'gu': 'આદર્શ જવાબ:'},
  'Explanation:': {'hi': 'व्याख्या:', 'gu': 'સમજૂતી:'},
  'Marking scheme:': {'hi': 'अंक योजना:', 'gu': 'ગુણ યોજના:'},
  'Time': {'hi': 'समय', 'gu': 'સમય'},
  'Maximum Marks': {'hi': 'अधिकतम अंक', 'gu': 'મહત્તમ ગુણ'},
  'General Instructions:': {'hi': 'सामान्य निर्देश:', 'gu': 'સામાન્ય સૂચનાઓ:'},
  'All questions are compulsory.': {'hi': 'सभी प्रश्न अनिवार्य हैं।', 'gu': 'બધા પ્રશ્નો ફરજિયાત છે.'},
  'Figures to the right indicate the marks for each question.': {
    'hi': 'दाईं ओर के अंक प्रत्येक प्रश्न के अंक दर्शाते हैं।',
    'gu': 'જમણી બાજુના આંકડા દરેક પ્રશ્નના ગુણ દર્શાવે છે.',
  },
  'Write your answers neatly in the answer sheet.': {'hi': 'उत्तर-पुस्तिका में अपने उत्तर साफ़-साफ़ लिखें।', 'gu': 'ઉત્તરવહીમાં તમારા જવાબ સુઘડ રીતે લખો.'},
  'Preparing pages...': {'hi': 'पृष्ठ तैयार हो रहे हैं...', 'gu': 'પાનાં તૈયાર થઈ રહ્યાં છે...'},
  'Drawing page items': {'hi': 'पृष्ठ बन रहे हैं', 'gu': 'પાનાં બની રહ્યાં છે'},
  'Generating PDF...': {'hi': 'PDF बन रही है...', 'gu': 'PDF બની રહી છે...'},
  'PDF Details': {'hi': 'PDF विवरण', 'gu': 'PDF વિગતો'},
  'Generate': {'hi': 'बनाएँ', 'gu': 'બનાવો'},
  'Cancel': {'hi': 'रद्द करें', 'gu': 'રદ કરો'},
  'Not enough questions yet for a full board paper': {
    'hi': 'पूरे बोर्ड प्रश्न-पत्र के लिए अभी पर्याप्त प्रश्न नहीं हैं',
    'gu': 'સંપૂર્ણ બોર્ડ પ્રશ્નપત્ર માટે હજુ પૂરતા પ્રશ્નો નથી',
  },
};
