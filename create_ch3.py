import json

data = {
  "metadata": {
    "title": "Pair of Linear Equations in Two Variables",
    "subject": "Maths",
    "grade": "10",
    "curriculum": [
      "GSEB",
      "NCERT",
      "CBSE"
    ],
    "difficulty": "Intermediate",
    "version": "4.0.0",
    "id": "cbse_class10_maths_ch3"
  },
  "blocks": [
    {
      "id": "CH3_HOOK",
      "type": "hook",
      "title": "The Mystery of Ages",
      "title_hi": "उम्र का रहस्य",
      "title_gu": "ઉંમરનું રહસ્ય",
      "body": "A father tells his daughter, 'Seven years ago, I was seven times as old as you were then. Also, three years from now, I shall be three times as old as you will be.' Isn't this interesting? How can we find their present ages?",
      "body_hi": "एक पिता अपनी बेटी से कहता है, 'सात साल पहले, मैं तुम्हारी उस समय की उम्र का सात गुना था। साथ ही, अब से तीन साल बाद, मैं तुम्हारी उम्र का तीन गुना हो जाऊंगा।' क्या यह दिलचस्प नहीं है? हम उनकी वर्तमान उम्र कैसे जान सकते हैं?",
      "body_gu": "એક પિતા તેની પુત્રીને કહે છે, 'સાત વર્ષ પહેલાં, હું તારા કરતાં સાત ગણો મોટો હતો. વળી, હવેથી ત્રણ વર્ષ પછી, હું તારી ઉંમર કરતાં ત્રણ ગણો થઈશ.' શું આ રસપ્રદ નથી? આપણે તેમની વર્તમાન ઉંમર કેવી રીતે શોધી શકીએ?"
    },
    {
      "id": "CH3_SOCRATIC",
      "type": "socratic_question",
      "title": "Think About It",
      "title_hi": "इस पर विचार करें",
      "title_gu": "આના વિશે વિચારો",
      "body": "If you have two unknown values to find (like the father's age and the daughter's age), how many different clues or equations do you think you need to find both values exactly?",
      "body_hi": "यदि आपको खोजने के लिए दो अज्ञात मान हैं (जैसे पिता की उम्र और बेटी की उम्र), तो आपको लगता है कि दोनों मानों को सटीक रूप से खोजने के लिए आपको कितने अलग-अलग सुराग या समीकरणों की आवश्यकता है?",
      "body_gu": "જો તમારે શોધવા માટે બે અજ્ઞાત મૂલ્યો છે (જેમ કે પિતાની ઉંમર અને પુત્રીની ઉંમર), તો તમને બંને મૂલ્યો બરાબર શોધવા માટે કેટલા જુદા જુદા સંકેતો અથવા સમીકરણોની જરૂર છે?",
      "options": [
        "1",
        "2",
        "3",
        "None"
      ],
      "options_hi": [
        "1",
        "2",
        "3",
        "कोई नहीं"
      ],
      "options_gu": [
        "1",
        "2",
        "3",
        "કોઈ નહીં"
      ],
      "correct_index": 1,
      "explanation": "To solve for two variables, we generally need two distinct equations.",
      "explanation_hi": "दो चरों को हल करने के लिए, हमें आम तौर पर दो अलग-अलग समीकरणों की आवश्यकता होती है।",
      "explanation_gu": "બે ચલો ઉકેલવા માટે, આપણને સામાન્ય રીતે બે અલગ-અલગ સમીકરણોની જરૂર હોય છે."
    },
    {
      "id": "CH3_DISCOVERY",
      "type": "discovery",
      "title": "Connecting the Dots",
      "title_hi": "कड़ियों को जोड़ना",
      "title_gu": "બિંદુઓને જોડવું",
      "body": "When we represent two straight lines on a graph, they can either intersect at one point, be parallel and never touch, or overlap completely. This visual geometry is exactly what happens with pairs of linear equations!",
      "body_hi": "जब हम एक ग्राफ पर दो सीधी रेखाओं का प्रतिनिधित्व करते हैं, तो वे या तो एक बिंदु पर प्रतिच्छेद कर सकती हैं, समानांतर हो सकती हैं और कभी नहीं छू सकती हैं, या पूरी तरह से ओवरलैप कर सकती हैं। यह दृश्य ज्यामिति बिल्कुल वही है जो रैखिक समीकरणों के जोड़े के साथ होती है!",
      "body_gu": "જ્યારે આપણે આલેખ પર બે સીધી રેખાઓ રજૂ કરીએ છીએ, ત્યારે તે કાં તો એક બિંદુ પર છેદે છે, સમાંતર હોઈ શકે છે અને ક્યારેય સ્પર્શ કરી શકતી નથી, અથવા સંપૂર્ણપણે ઓવરલેપ થઈ શકે છે. આ દ્રશ્ય ભૂમિતિ બરાબર છે જે રેખીય સમીકરણોની જોડી સાથે થાય છે!"
    },
    {
      "type": "theory",
      "id": "CH3_T1_01",
      "title": "General Form of a Linear Equation",
      "title_hi": "रैखिक समीकरण का सामान्य रूप",
      "title_gu": "રેખીય સમીકરણનું સામાન્ય સ્વરૂપ",
      "body": "An equation of the form ax + by + c = 0, where a, b, and c are real numbers, and a and b are not both zero, is called a linear equation in two variables x and y.",
      "body_hi": "ax + by + c = 0 के रूप का एक समीकरण, जहाँ a, b, और c वास्तविक संख्याएँ हैं, और a और b दोनों शून्य नहीं हैं, दो चरों x और y में एक रैखिक समीकरण कहलाता है।",
      "body_gu": "ax + by + c = 0 ના સ્વરૂપનું સમીકરણ, જ્યાં a, b અને c વાસ્તવિક સંખ્યાઓ છે, અને a અને b બંને શૂન્ય નથી, તેને x અને y બે ચલોમાં રેખીય સમીકરણ કહેવાય છે."
    },
    {
      "type": "theory",
      "id": "CH3_T1_02",
      "title": "Graphical Representation",
      "title_hi": "चित्रमय निरूपण",
      "title_gu": "ગ્રાફિકલ રજૂઆત",
      "body": "A pair of linear equations in two variables will graphically represent two straight lines. These lines can intersect (one unique solution), be parallel (no solution), or be coincident (infinitely many solutions).",
      "body_hi": "दो चरों में रैखिक समीकरणों का एक जोड़ा ग्राफिक रूप से दो सीधी रेखाओं का प्रतिनिधित्व करेगा। ये रेखाएँ प्रतिच्छेद कर सकती हैं (एक अद्वितीय समाधान), समानांतर हो सकती हैं (कोई समाधान नहीं), या संपाती हो सकती हैं (अपरिमित रूप से अनेक समाधान)।",
      "body_gu": "બે ચલોમાં રેખીય સમીકરણોની જોડી ગ્રાફિકલી બે સીધી રેખાઓ રજૂ કરશે. આ રેખાઓ છેદે છે (એક અનન્ય ઉકેલ), સમાંતર હોઈ શકે છે (કોઈ ઉકેલ નથી), અથવા એકરૂપ હોઈ શકે છે (અનંત ઘણા ઉકેલો)."
    },
    {
      "type": "mcq",
      "id": "CH3_Q1",
      "question": "What is the condition for two lines a1x + b1y + c1 = 0 and a2x + b2y + c2 = 0 to be parallel?",
      "question_hi": "दो रेखाओं a1x + b1y + c1 = 0 और a2x + b2y + c2 = 0 के समानांतर होने की शर्त क्या है?",
      "question_gu": "બે રેખાઓ a1x + b1y + c1 = 0 અને a2x + b2y + c2 = 0 સમાંતર હોવાની શરત શું છે?",
      "options": [
        "a1/a2 = b1/b2 = c1/c2",
        "a1/a2 != b1/b2",
        "a1/a2 = b1/b2 != c1/c2",
        "a1/a2 != c1/c2"
      ],
      "options_hi": [
        "a1/a2 = b1/b2 = c1/c2",
        "a1/a2 != b1/b2",
        "a1/a2 = b1/b2 != c1/c2",
        "a1/a2 != c1/c2"
      ],
      "options_gu": [
        "a1/a2 = b1/b2 = c1/c2",
        "a1/a2 != b1/b2",
        "a1/a2 = b1/b2 != c1/c2",
        "a1/a2 != c1/c2"
      ],
      "correct_index": 2,
      "explanation": "For lines to be parallel (no solution), a1/a2 must equal b1/b2, but not equal c1/c2.",
      "explanation_hi": "रेखाओं के समानांतर होने (कोई समाधान नहीं) के लिए, a1/a2 को b1/b2 के बराबर होना चाहिए, लेकिन c1/c2 के बराबर नहीं होना चाहिए।",
      "explanation_gu": "રેખાઓ સમાંતર (કોઈ ઉકેલ નહીં) માટે, a1/a2 એ b1/b2 ની બરાબર હોવી જોઈએ, પરંતુ c1/c2 બરાબર નથી."
    },
    {
      "id": "CH3_REFLECTION",
      "type": "reflection",
      "title": "Your Turn",
      "title_hi": "आपकी बारी",
      "title_gu": "તમારો વારો",
      "body": "Explain in your own words the difference between 'consistent' and 'inconsistent' pair of linear equations.",
      "body_hi": "अपने शब्दों में रैखिक समीकरणों के 'संगत' (consistent) और 'असंगत' (inconsistent) युग्म के बीच का अंतर स्पष्ट करें।",
      "body_gu": "તમારા પોતાના શબ્દોમાં રેખીય સમીકરણોની 'સુસંગત' (consistent) અને 'અસંગત' (inconsistent) જોડી વચ્ચેનો તફાવત સમજાવો."
    },
    {
      "id": "CH3_MASTERY",
      "type": "mastery",
      "title": "The Final Challenge",
      "title_hi": "अंतिम चुनौती",
      "title_gu": "અંતિમ પડકાર",
      "body": "Use the substitution method to solve the equations: x + y = 14 and x - y = 4. What are the values of x and y?",
      "body_hi": "समीकरणों को हल करने के लिए प्रतिस्थापन विधि का उपयोग करें: x + y = 14 और x - y = 4. x और y के मान क्या हैं?",
      "body_gu": "સમીકરણો ઉકેલવા માટે અવેજી પદ્ધતિનો ઉપયોગ કરો: x + y = 14 અને x - y = 4. x અને y ના મૂલ્યો શું છે?"
    }
  ]
}

with open("app_core/chapters/ncert_class10_maths_ch3.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
