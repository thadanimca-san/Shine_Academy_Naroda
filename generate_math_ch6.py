import json
import os

def main():
    metadata = {
        "title": "Triangles",
        "subject": "Maths",
        "grade": "10",
        "curriculum": ["GSEB", "NCERT", "CBSE"],
        "difficulty": "Intermediate",
        "version": "4.0.0",
        "id": "cbse_class10_maths_ch6"
    }

    blocks = []

    # 1. HOOK
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_HOOK",
        "type": "hook",
        "title": "Measuring the Unreachable",
        "title_hi": "पहुंच से बाहर को मापना",
        "title_gu": "પહોંચની બહાર માપવું",
        "body": "Have you ever wondered how we measure the height of Mount Everest or the distance to the moon? We definitely don't use a giant measuring tape! Instead, we use the magic of 'Similarity of Triangles'. Let's find out how!",
        "body_hi": "क्या आपने कभी सोचा है कि हम माउंट एवरेस्ट की ऊंचाई या चंद्रमा की दूरी को कैसे मापते हैं? हम निश्चित रूप से एक विशाल मापने वाले टेप का उपयोग नहीं करते हैं! इसके बजाय, हम 'त्रिभुजों की समरूपता' के जादू का उपयोग करते हैं। आइए जानें कैसे!",
        "body_gu": "શું તમે ક્યારેય વિચાર્યું છે કે આપણે માઉન્ટ એવરેસ્ટની ઊંચાઈ અથવા ચંદ્રનું અંતર કેવી રીતે માપીએ છીએ? આપણે ચોક્કસપણે વિશાળ માપન ટેપનો ઉપયોગ કરતા નથી! તેના બદલે, આપણે 'ત્રિકોણની સમાનતા' ના જાદુનો ઉપયોગ કરીએ છીએ. ચાલો જાણીએ કેવી રીતે!"
    })

    # 2. SOCRATIC THINKING
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_SOCRATIC",
        "type": "socratic_question",
        "title": "Think About It",
        "title_hi": "इस पर विचार करें",
        "title_gu": "આના વિશે વિચારો",
        "body": "Look at two photographs of the Taj Mahal—one passport-sized and one large poster. Do they have the same shape or the same size?",
        "body_hi": "ताजमहल की दो तस्वीरों को देखें - एक पासपोर्ट के आकार की और एक बड़ा पोस्टर। क्या उनका आकार (shape) समान है या परिमाण (size) समान है?",
        "body_gu": "તાજમહેલના બે ફોટોગ્રાફ્સ જુઓ - એક પાસપોર્ટ સાઇઝનો અને એક મોટો પોસ્ટર. શું તેમનો આકાર (shape) સમાન છે કે પરિમાણ (size) સમાન છે?",
        "options": ["Same shape, same size", "Different shape, same size", "Same shape, different size", "Different shape, different size"],
        "options_hi": ["समान आकार, समान परिमाण", "भिन्न आकार, समान परिमाण", "समान आकार, भिन्न परिमाण", "भिन्न आकार, भिन्न परिमाण"],
        "options_gu": ["સમાન આકાર, સમાન પરિમાણ", "ભિન્ન આકાર, સમાન પરિમાણ", "સમાન આકાર, ભિન્ન પરિમાણ", "ભિન્ન આકાર, ભિન્ન પરિમાણ"],
        "correct_index": 2,
        "explanation": "They have the same shape, but their sizes are different. In Mathematics, such figures are called 'Similar Figures'.",
        "explanation_hi": "उनका आकार समान है, लेकिन उनका परिमाण अलग है। गणित में, ऐसी आकृतियों को 'समरूप आकृतियाँ' कहा जाता है।",
        "explanation_gu": "તેમનો આકાર સમાન છે, પરંતુ તેમના પરિમાણો અલગ છે. ગણિતમાં, આવી આકૃતિઓને 'સમાન આકૃતિઓ' કહેવામાં આવે છે."
    })

    # 3. DISCOVERY
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_DISCOVERY",
        "type": "discovery",
        "title": "Similarity vs Congruence",
        "title_hi": "समरूपता बनाम सर्वांगसमता",
        "title_gu": "સમાનતા વિરુદ્ધ એકરૂપતા",
        "body": "In Class 9, you studied 'Congruent' figures—figures with the same shape AND same size. Now, we move to 'Similar' figures—they have the SAME SHAPE, but NOT necessarily the same size. All congruent figures are similar, but similar figures need not be congruent! All circles are similar. All squares are similar.",
        "body_hi": "कक्षा 9 में, आपने 'सर्वांगसम' आकृतियों का अध्ययन किया—समान आकार (shape) और समान परिमाण (size) वाली आकृतियाँ। अब, हम 'समरूप' आकृतियों की ओर बढ़ते हैं—उनका आकार समान होता है, लेकिन जरूरी नहीं कि परिमाण समान हो। सभी सर्वांगसम आकृतियाँ समरूप होती हैं, लेकिन समरूप आकृतियों का सर्वांगसम होना आवश्यक नहीं है! सभी वृत्त समरूप होते हैं। सभी वर्ग समरूप होते हैं।",
        "body_gu": "ધોરણ 9 માં, તમે 'એકરૂપ' આકૃતિઓનો અભ્યાસ કર્યો—સમાન આકાર (shape) અને સમાન પરિમાણ (size) ધરાવતી આકૃતિઓ. હવે, આપણે 'સમાન' આકૃતિઓ તરફ વળીએ છીએ—તેમનો આકાર સમાન છે, પરંતુ પરિમાણ સમાન હોવું જરૂરી નથી. બધી એકરૂપ આકૃતિઓ સમાન હોય છે, પરંતુ સમાન આકૃતિઓ એકરૂપ હોવી જરૂરી નથી! બધા વર્તુળો સમાન છે. બધા ચોરસ સમાન છે."
    })

    # 4. REVEAL
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_REVEAL",
        "type": "theory",
        "title": "Similarity of Polygons",
        "title_hi": "बहुभुजों की समरूपता",
        "title_gu": "બહુકોણની સમાનતા",
        "body": "Two polygons of the same number of sides are similar, if (i) their corresponding angles are equal and (ii) their corresponding sides are in the same ratio (or proportion). The ratio of corresponding sides is called the 'scale factor'.",
        "body_hi": "समान भुजाओं वाले दो बहुभुज समरूप होते हैं, यदि (i) उनके संगत कोण समान हों और (ii) उनकी संगत भुजाएँ एक ही अनुपात (या समानुपात) में हों। संगत भुजाओं के अनुपात को 'स्केल फैक्टर' कहा जाता है।",
        "body_gu": "સમાન સંખ્યામાં બાજુઓ ધરાવતા બે બહુકોણ સમાન હોય છે, જો (i) તેમના અનુરૂપ ખૂણાઓ સમાન હોય અને (ii) તેમની અનુરૂપ બાજુઓ સમાન ગુણોત્તર (અથવા પ્રમાણ) માં હોય. અનુરૂપ બાજુઓના ગુણોત્તરને 'સ્કેલ ફેક્ટર' કહેવામાં આવે છે."
    })

    # 5. KNOWLEDGE CHECK
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_CHECK_1",
        "type": "mcq",
        "question": "Which of the following statements is true?",
        "question_hi": "निम्नलिखित में से कौन सा कथन सत्य है?",
        "question_gu": "નીચેનામાંથી કયું વિધાન સાચું છે?",
        "options": ["All similar figures are congruent.", "All congruent figures are similar.", "All rectangles are similar.", "All triangles are similar."],
        "options_hi": ["सभी समरूप आकृतियाँ सर्वांगसम होती हैं।", "सभी सर्वांगसम आकृतियाँ समरूप होती हैं।", "सभी आयत समरूप होते हैं।", "सभी त्रिभुज समरूप होते हैं।"],
        "options_gu": ["બધી સમાન આકૃતિઓ એકરૂપ હોય છે.", "બધી એકરૂપ આકૃતિઓ સમાન હોય છે.", "બધા લંબચોરસ સમાન હોય છે.", "બધા ત્રિકોણ સમાન હોય છે."],
        "correct_index": 1,
        "explanation": "Congruent figures have the same shape and size, which satisfies the condition for similarity (same shape). However, similar figures may vary in size, so they aren't always congruent.",
        "explanation_hi": "सर्वांगसम आकृतियों का आकार और परिमाण समान होता है, जो समरूपता (समान आकार) की शर्त को पूरा करता है। हालांकि, समरूप आकृतियों का परिमाण भिन्न हो सकता है, इसलिए वे हमेशा सर्वांगसम नहीं होती हैं।",
        "explanation_gu": "એકરૂપ આકૃતિઓ સમાન આકાર અને કદ ધરાવે છે, જે સમાનતા (સમાન આકાર) ની શરતને સંતોષે છે. જોકે, સમાન આકૃતિઓનું કદ અલગ હોઈ શકે છે, તેથી તે હંમેશા એકરૂપ હોતી નથી."
    })

    # Thales Theorem Theory
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_THALES",
        "type": "theory",
        "title": "Basic Proportionality Theorem (Thales Theorem)",
        "title_hi": "आधारभूत समानुपातिकता प्रमेय (थेल्स प्रमेय)",
        "title_gu": "મૂળભૂત પ્રમાણસરતા પ્રમેય (થેલ્સનો પ્રમેય)",
        "body": "If a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio. In ∆ABC, if DE || BC, then AD/DB = AE/EC.",
        "body_hi": "यदि किसी त्रिभुज की एक भुजा के समांतर अन्य दो भुजाओं को भिन्न-भिन्न बिंदुओं पर प्रतिच्छेद करने के लिए एक रेखा खींची जाए, तो ये अन्य दो भुजाएँ एक ही अनुपात में विभाजित हो जाती हैं। ∆ABC में, यदि DE || BC है, तो AD/DB = AE/EC।",
        "body_gu": "જો કોઈ ત્રિકોણની એક બાજુને સમાંતર અન્ય બે બાજુઓને ભિન્ન બિંદુઓમાં છેદવા માટે એક રેખા દોરવામાં આવે, તો અન્ય બે બાજુઓ સમાન ગુણોત્તરમાં વિભાજિત થાય છે. ∆ABC માં, જો DE || BC, તો AD/DB = AE/EC."
    })

    # Exercises
    # EXERCISE 6.1
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_EX6_1_Q1_1",
        "type": "mcq",
        "question": "Exercise 6.1: Fill in the blank. All circles are _______.",
        "question_hi": "प्रश्नावली 6.1: रिक्त स्थान भरें। सभी वृत्त _______ होते हैं।",
        "question_gu": "સ્વાધ્યાય 6.1: ખાલી જગ્યા પૂરો. બધા વર્તુળો _______ હોય છે.",
        "options": ["congruent", "similar", "equal", "parallel"],
        "options_hi": ["सर्वांगसम", "समरूप", "समान", "समांतर"],
        "options_gu": ["એકરૂપ", "સમાન", "સમાન", "સમાંતર"],
        "correct_index": 1,
        "explanation": "All circles have the same shape, but can have different radii. Thus, they are similar.",
        "explanation_hi": "सभी वृत्तों का आकार समान होता है, लेकिन त्रिज्याएँ भिन्न हो सकती हैं। इस प्रकार, वे समरूप हैं।",
        "explanation_gu": "બધા વર્તુળો સમાન આકાર ધરાવે છે, પરંતુ ત્રિજ્યા અલગ હોઈ શકે છે. તેથી, તેઓ સમાન છે."
    })

    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_EX6_1_Q1_2",
        "type": "mcq",
        "question": "Exercise 6.1: Fill in the blank. All squares are _______.",
        "question_hi": "प्रश्नावली 6.1: रिक्त स्थान भरें। सभी वर्ग _______ होते हैं।",
        "question_gu": "સ્વાધ્યાય 6.1: ખાલી જગ્યા પૂરો. બધા ચોરસ _______ હોય છે.",
        "options": ["similar", "congruent", "equal", "parallel"],
        "options_hi": ["समरूप", "सर्वांगसम", "समान", "समांतर"],
        "options_gu": ["સમાન", "એકરૂપ", "સમાન", "સમાંતર"],
        "correct_index": 0,
        "explanation": "All squares have the same shape, but side lengths can differ. Thus, they are similar.",
        "explanation_hi": "सभी वर्गों का आकार समान होता है, लेकिन भुजा की लंबाई भिन्न हो सकती है। इस प्रकार, वे समरूप हैं।",
        "explanation_gu": "બધા ચોરસ સમાન આકાર ધરાવે છે, પરંતુ બાજુની લંબાઈ અલગ હોઈ શકે છે. તેથી, તેઓ સમાન છે."
    })

    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_EX6_1_Q1_3",
        "type": "mcq",
        "question": "Exercise 6.1: Fill in the blank. All _______ triangles are similar.",
        "question_hi": "प्रश्नावली 6.1: रिक्त स्थान भरें। सभी _______ त्रिभुज समरूप होते हैं।",
        "question_gu": "સ્વાધ્યાય 6.1: ખાલી જગ્યા પૂરો. બધા _______ ત્રિકોણ સમાન હોય છે.",
        "options": ["isosceles", "equilateral", "scalene", "right angled"],
        "options_hi": ["समद्विबाहु", "समबाहु", "विषमबाहु", "समकोण"],
        "options_gu": ["સમદ્વિબાજુ", "સમબાજુ", "વિષમબાજુ", "કાટકોણ"],
        "correct_index": 1,
        "explanation": "All equilateral triangles have angles of 60°, satisfying the similarity condition (AA).",
        "explanation_hi": "सभी समबाहु त्रिभुजों के कोण 60° होते हैं, जो समरूपता की शर्त (AA) को पूरा करते हैं।",
        "explanation_gu": "બધા સમબાજુ ત્રિકોણના ખૂણા 60° હોય છે, જે સમાનતાની શરત (AA) પૂરી કરે છે."
    })

    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_EX6_1_Q1_4",
        "type": "mcq",
        "question": "Exercise 6.1: Two polygons of the same number of sides are similar, if (a) their corresponding angles are _______ and (b) their corresponding sides are _______.",
        "question_hi": "प्रश्नावली 6.1: समान भुजाओं वाले दो बहुभुज समरूप होते हैं, यदि (a) उनके संगत कोण _______ हों और (b) उनकी संगत भुजाएँ _______ हों।",
        "question_gu": "સ્વાધ્યાય 6.1: સમાન સંખ્યામાં બાજુઓ ધરાવતા બે બહુકોણ સમાન હોય છે, જો (a) તેમના અનુરૂપ ખૂણાઓ _______ હોય અને (b) તેમની અનુરૂપ બાજુઓ _______ હોય.",
        "options": ["equal, proportional", "proportional, equal", "equal, equal", "proportional, proportional"],
        "options_hi": ["समान, समानुपाती", "समानुपाती, समान", "समान, समान", "समानुपाती, समानुपाती"],
        "options_gu": ["સમાન, પ્રમાણસર", "પ્રમાણસર, સમાન", "સમાન, સમાન", "પ્રમાણસર, પ્રમાણસર"],
        "correct_index": 0,
        "explanation": "By definition of similarity in polygons.",
        "explanation_hi": "बहुभुजों में समरूपता की परिभाषा के अनुसार।",
        "explanation_gu": "બહુકોણમાં સમાનતાની વ્યાખ્યા મુજબ."
    })

    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_EX6_1_Q2",
        "type": "mcq",
        "question": "Exercise 6.1: Give an example of a pair of non-similar figures.",
        "question_hi": "प्रश्नावली 6.1: गैर-समरूप आकृतियों के युग्म का एक उदाहरण दें।",
        "question_gu": "સ્વાધ્યાય 6.1: બિન-સમાન આકૃતિઓની જોડીનું ઉદાહરણ આપો.",
        "options": ["A rhombus and a rectangle", "Two circles", "Two equilateral triangles", "Two squares"],
        "options_hi": ["एक समचतुर्भुज और एक आयत", "दो वृत्त", "दो समबाहु त्रिभुज", "दो वर्ग"],
        "options_gu": ["સમબાજુ ચતુષ્કોણ અને લંબચોરસ", "બે વર્તુળો", "બે સમબાજુ ત્રિકોણ", "બે ચોરસ"],
        "correct_index": 0,
        "explanation": "A rhombus and a rectangle do not have equal corresponding angles, hence they are not similar.",
        "explanation_hi": "एक समचतुर्भुज और एक आयत के संगत कोण समान नहीं होते हैं, इसलिए वे समरूप नहीं हैं।",
        "explanation_gu": "સમબાજુ ચતુષ્કોણ અને લંબચોરસના અનુરૂપ ખૂણાઓ સમાન હોતા નથી, તેથી તેઓ સમાન નથી."
    })

    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_EX6_1_Q3",
        "type": "mcq",
        "question": "Exercise 6.1: Are a square and a rhombus with proportional sides similar?",
        "question_hi": "प्रश्नावली 6.1: क्या समानुपाती भुजाओं वाले एक वर्ग और एक समचतुर्भुज समरूप होते हैं?",
        "question_gu": "સ્વાધ્યાય 6.1: શું પ્રમાણસર બાજુઓવાળા ચોરસ અને સમબાજુ ચતુષ્કોણ સમાન છે?",
        "options": ["No, their corresponding angles are not equal", "Yes, they have 4 sides", "Yes, their sides are proportional", "No, their sides are not proportional"],
        "options_hi": ["नहीं, उनके संगत कोण समान नहीं हैं", "हाँ, उनकी 4 भुजाएँ हैं", "हाँ, उनकी भुजाएँ समानुपाती हैं", "नहीं, उनकी भुजाएँ समानुपाती नहीं हैं"],
        "options_gu": ["ના, તેમના અનુરૂપ ખૂણાઓ સમાન નથી", "હા, તેમની 4 બાજુઓ છે", "હા, તેમની બાજુઓ પ્રમાણસર છે", "ના, તેમની બાજુઓ પ્રમાણસર નથી"],
        "correct_index": 0,
        "explanation": "In a square, all angles are 90°, but in a rhombus, angles may not be 90°. Similarity requires equal angles.",
        "explanation_hi": "एक वर्ग में सभी कोण 90° होते हैं, लेकिन एक समचतुर्भुज में कोण 90° नहीं हो सकते हैं। समरूपता के लिए समान कोणों की आवश्यकता होती है।",
        "explanation_gu": "ચોરસમાં બધા ખૂણા 90° હોય છે, પરંતુ સમબાજુ ચતુષ્કોણમાં ખૂણા 90° ન હોઈ શકે. સમાનતા માટે સમાન ખૂણાઓ હોવા જરૂરી છે."
    })

    # EXERCISE 6.2 Example question based on text
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_EX6_2_Q1",
        "type": "mcq",
        "question": "Exercise 6.2: In ∆ABC, DE || BC. If AD=1.5 cm, DB=3 cm, and AE=1 cm, find EC.",
        "question_hi": "प्रश्नावली 6.2: ∆ABC में, DE || BC. यदि AD=1.5 सेमी, DB=3 सेमी, और AE=1 सेमी, तो EC ज्ञात कीजिए।",
        "question_gu": "સ્વાધ્યાય 6.2: ∆ABC માં, DE || BC. જો AD=1.5 સેમી, DB=3 સેમી, અને AE=1 સેમી, તો EC શોધો.",
        "options": ["2 cm", "3 cm", "1.5 cm", "4 cm"],
        "options_hi": ["2 सेमी", "3 सेमी", "1.5 सेमी", "4 सेमी"],
        "options_gu": ["2 સેમી", "3 સેમી", "1.5 સેમી", "4 સેમી"],
        "correct_index": 0,
        "explanation": "By Basic Proportionality Theorem, AD/DB = AE/EC. So, 1.5/3 = 1/EC => EC = 2 cm.",
        "explanation_hi": "आधारभूत समानुपातिकता प्रमेय द्वारा, AD/DB = AE/EC। इसलिए, 1.5/3 = 1/EC => EC = 2 सेमी।",
        "explanation_gu": "મૂળભૂત પ્રમાણસરતા પ્રમેય દ્વારા, AD/DB = AE/EC. તેથી, 1.5/3 = 1/EC => EC = 2 સેમી."
    })

    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_EX6_2_Q1_P2",
        "type": "mcq",
        "question": "Exercise 6.2: In ∆ABC, DE || BC. If AE=1.8 cm, EC=5.4 cm, and DB=7.2 cm, find AD.",
        "question_hi": "प्रश्नावली 6.2: ∆ABC में, DE || BC. यदि AE=1.8 सेमी, EC=5.4 सेमी, और DB=7.2 सेमी, तो AD ज्ञात कीजिए।",
        "question_gu": "સ્વાધ્યાય 6.2: ∆ABC માં, DE || BC. જો AE=1.8 સેમી, EC=5.4 સેમી, અને DB=7.2 સેમી, તો AD શોધો.",
        "options": ["2.4 cm", "1.2 cm", "3.6 cm", "4.8 cm"],
        "options_hi": ["2.4 सेमी", "1.2 सेमी", "3.6 सेमी", "4.8 सेमी"],
        "options_gu": ["2.4 સેમી", "1.2 સેમી", "3.6 સેમી", "4.8 સેમી"],
        "correct_index": 0,
        "explanation": "AD/DB = AE/EC => AD/7.2 = 1.8/5.4 => AD = (1/3) * 7.2 = 2.4 cm.",
        "explanation_hi": "AD/DB = AE/EC => AD/7.2 = 1.8/5.4 => AD = (1/3) * 7.2 = 2.4 सेमी।",
        "explanation_gu": "AD/DB = AE/EC => AD/7.2 = 1.8/5.4 => AD = (1/3) * 7.2 = 2.4 સેમી."
    })
    
    blocks.append({
        "id": "KOBJ_CLASS10_MATH_CH6_EX6_2_Q2_1",
        "type": "mcq",
        "question": "Exercise 6.2: E and F are points on the sides PQ and PR respectively of a ∆PQR. For PE=3.9 cm, EQ=3 cm, PF=3.6 cm and FR=2.4 cm, is EF || QR?",
        "question_hi": "प्रश्नावली 6.2: E और F क्रमशः ∆PQR की भुजाओं PQ और PR पर स्थित बिंदु हैं। यदि PE=3.9 सेमी, EQ=3 सेमी, PF=3.6 सेमी और FR=2.4 सेमी है, तो क्या EF || QR है?",
        "question_gu": "સ્વાધ્યાય 6.2: E અને F અનુક્રમે ∆PQR ની બાજુઓ PQ અને PR પર આવેલા બિંદુઓ છે. જો PE=3.9 સેમી, EQ=3 સેમી, PF=3.6 સેમી અને FR=2.4 સેમી હોય, તો શું EF || QR છે?",
        "options": ["No, EF is not parallel to QR", "Yes, EF || QR", "Cannot be determined", "EF is perpendicular to QR"],
        "options_hi": ["नहीं, EF, QR के समांतर नहीं है", "हाँ, EF || QR", "निर्धारित नहीं किया जा सकता", "EF, QR के लंबवत है"],
        "options_gu": ["ના, EF એ QR ને સમાંતર નથી", "હા, EF || QR", "નક્કી કરી શકાતું નથી", "EF એ QR ને લંબ છે"],
        "correct_index": 0,
        "explanation": "PE/EQ = 3.9/3 = 1.3. PF/FR = 3.6/2.4 = 1.5. Since PE/EQ ≠ PF/FR, EF is not parallel to QR.",
        "explanation_hi": "PE/EQ = 3.9/3 = 1.3। PF/FR = 3.6/2.4 = 1.5। चूँकि PE/EQ ≠ PF/FR, इसलिए EF, QR के समांतर नहीं है।",
        "explanation_gu": "PE/EQ = 3.9/3 = 1.3. PF/FR = 3.6/2.4 = 1.5. કારણ કે PE/EQ ≠ PF/FR, તેથી EF એ QR ને સમાંતર નથી."
    })

    # Wrap up in final structure
    output = {
        "metadata": metadata,
        "blocks": blocks
    }

    with open('app_core/chapters/ncert_class10_maths_ch6.json', 'w', encoding='utf-8') as f:
        json.dump(output, f, indent=2, ensure_ascii=False)
    print("Generated successfully!")

if __name__ == '__main__':
    main()
