import os
import json

def make_quiz(id_str, q_en, q_hi, q_gu, opts_en, opts_hi, opts_gu, correct_idx, expl_en, expl_hi, expl_gu, bloom="Apply", diff="Intermediate", mins=2):
    return {
        "id": id_str,
        "type": "quiz",
        "question": q_en,
        "options": opts_en,
        "correct_index": correct_idx,
        "explanation": expl_en,
        "question_hi": q_hi,
        "options_hi": opts_hi,
        "explanation_hi": expl_hi,
        "question_gu": q_gu,
        "options_gu": opts_gu,
        "explanation_gu": expl_gu,
        "bloom": bloom,
        "difficulty": diff,
        "estimated_minutes": mins
    }

def make_theory(id_str, title_en, title_hi, title_gu, body_en, body_hi, body_gu, btype="theory", bloom="Understand", diff="Beginner", mins=3):
    return {
        "id": id_str,
        "type": btype,
        "title": title_en,
        "body": body_en,
        "title_hi": title_hi,
        "body_hi": body_hi,
        "title_gu": title_gu,
        "body_gu": body_gu,
        "bloom": bloom,
        "difficulty": diff,
        "estimated_minutes": mins
    }

def get_metadata():
    return {
        "id": "ncert_class10_maths_ch6",
        "title": "Chapter 6: Triangles",
        "title_hi": "अध्याय 6: त्रिभुज",
        "title_gu": "પ્રકરણ 6: ત્રિકોણ",
        "subject": "Mathematics",
        "grade": "10",
        "board": "CBSE/GSEB",
        "curriculum": ["CBSE", "NCERT", "GSEB"],
        "language": "English, Hindi, Gujarati",
        "difficulty": "Intermediate",
        "estimated_minutes": 180,
        "version": "2.0.0",
        "author": "Shine Academy EduOS",
        "last_updated": "2026-10-01",
        "tags": [
            "triangles",
            "similar_figures",
            "basic_proportionality_theorem",
            "thales_theorem",
            "similarity_criteria",
            "aaa_similarity",
            "sss_similarity",
            "sas_similarity"
        ]
    }

# =========================================================================
# PART 1: SIMILAR FIGURES & EXERCISE 6.1
# =========================================================================
def get_part1_blocks():
    blocks = []

    # 1. Hook
    blocks.append(make_theory(
        "C10M_CH6_1",
        "The Art of Scaling: From Blueprints to Skyscrapers",
        "मापन और आकार की कला: ब्लूप्रिंट से गगनचुंबी इमारतों तक",
        "માપન અને કદની કળા: બ્લુપ્રિન્ટથી ગગનચુંબી ઇમારતો સુધી",
        "When an architect designs a skyscraper or a craftsman creates a miniature replica of the Taj Mahal, they do not change the proportions of the structure. Every door, pillar, and window is scaled down by the exact same ratio! Similarly, when you pinch to zoom into a photograph on your smartphone, the image expands without distorting faces or objects.\n\nIn mathematics, figures that share the exact **same shape**, but not necessarily the **same size**, are known as **Similar Figures (समरूप आकृतियाँ / સમરૂપ આકૃતિઓ)**. In this chapter, we will master the mathematics of similarity and unlock the geometric secrets of Triangles!",
        "जब कोई वास्तुकार किसी गगनचुंबी इमारत का डिज़ाइन बनाता है या कोई शिल्पकार ताजमहल की लघु प्रतिकृति बनाता है, तो वे संरचना के अनुपातों को नहीं बदलते हैं। प्रत्येक दरवाजे, खंभे और खिड़की को ठीक उसी अनुपात में छोटा किया जाता है! इसी प्रकार, जब आप अपने स्मार्टफोन पर किसी तस्वीर को ज़ूम इन करते हैं, तो चेहरों या वस्तुओं को विकृत किए बिना छवि बड़ी हो जाती है।\n\nगणित में, वे आकृतियाँ जिनका **आकार (shape) बिल्कुल समान** होता है, लेकिन **माप (size) समान होना आवश्यक नहीं** होता, **समरूप आकृतियाँ (Similar Figures)** कहलाती हैं। इस अध्याय में, हम समरूपता के गणित में महारत हासिल करेंगे और त्रिभुजों के ज्यामितीय रहस्यों को उजागर करेंगे!",
        "જ્યારે કોઈ આર્કિટેક્ટ ગગનચુંબી ઇમારતની ડિઝાઇન તૈયાર કરે છે અથવા કારીગર તાજમહેલનું લઘુ મોડેલ બનાવે છે, ત્યારે તેઓ બંધારણના પ્રમાણમાં કોઈ ફેરફાર કરતા નથી. દરેક દરવાજો, થાંભલો અને બારી બરાબર એક જ ગુણોત્તરમાં નાના કરવામાં આવે છે! એ જ રીતે, જ્યારે તમે તમારા સ્માર્ટફોન પર ફોટોગ્રાફને ઝૂમ કરો છો, ત્યારે ચહેરા કે વસ્તુઓ ખેંચાયા વિના ઈમેજ મોટી થાય છે.\n\nગણિતમાં, જે આકૃતિઓનો **આકાર એક સરખો** હોય, પરંતુ **કદ (માપ) સમાન હોવું જરૂરી ન હોય**, તેને **સમરૂપ આકૃતિઓ (Similar Figures)** કહેવામાં આવે છે. આ પ્રકરણમાં, આપણે સમરૂપતાના ગણિતમાં નિપુણતા મેળવીશું અને ત્રિકોણના ભૌમિતિક રહસ્યો ઉકેલીશું!",
        btype="hook",
        bloom="Understand",
        diff="Beginner",
        mins=3
    ))

    # 2. Socratic Question
    blocks.append(make_quiz(
        "C10M_CH6_2",
        "If you enlarge a photograph of a triangle to 3 times its width and 3 times its height, what happens to the interior angles of the triangle?",
        "यदि आप किसी त्रिभुज की तस्वीर को उसकी चौड़ाई से 3 गुना और ऊँचाई से 3 गुना बड़ा करते हैं, तो त्रिभुज के अंतःकोणों का क्या होता है?",
        "જો તમે ત્રિકોણના ફોટોગ્રાફને તેની પહોળાઈથી 3 ગણો અને ઊંચાઈથી 3 ગણો મોટો કરો, તો ત્રિકોણના અંદરના ખૂણાઓનું શું થાય છે?",
        [
            "The angles remain exactly the same",
            "The angles become 3 times larger",
            "The angles become one-third",
            "The sum of angles becomes 540°"
        ],
        [
            "कोण बिल्कुल समान रहते हैं",
            "कोण 3 गुना बड़े हो जाते हैं",
            "कोण एक-तिहाई हो जाते हैं",
            "कोणों का योग 540° हो जाता है"
        ],
        [
            "ખૂણાઓ બિલકુલ સમાન રહે છે",
            "ખૂણાઓ 3 ગણા મોટા થઈ જાય છે",
            "ખૂણાઓ ત્રીજા ભાગના થઈ જાય છે",
            "ખૂણાઓનો સરવાળો 540° થઈ જાય છે"
        ],
        0,
        "Scaling a geometric figure multiplies the lengths of its sides, but the interior angles remain completely unchanged! The sum of interior angles in any Euclidean triangle is always 180°.",
        "किसी ज्यामितीय आकृति को बड़ा करने पर उसकी भुजाओं की लंबाइयाँ बढ़ जाती हैं, लेकिन अंतःकोण बिल्कुल अपरिवर्तित रहते हैं! किसी भी यूक्लिडीय त्रिभुज के अंतःकोणों का योग हमेशा 180° ही रहता है।",
        "ભૌમિતિક આકૃતિને મોટી કરવાથી તેની બાજુઓની લંબાઈ વધે છે, પરંતુ અંદરના ખૂણાઓ બિલકુલ બદલાતા નથી! કોઈપણ યુક્લિડિયન ત્રિકોણના ખૂણાઓનો સરવાળો હંમેશા 180° જ રહે છે.",
        bloom="Understand",
        diff="Beginner",
        mins=2
    ))

    # 3. Discovery: Congruence vs Similarity
    blocks.append(make_theory(
        "C10M_CH6_3",
        "Discovery: Congruence vs Similarity (Same Size vs Same Shape)",
        "खोज: सर्वांगसमता बनाम समरूपता (समान माप बनाम समान रूप)",
        "શોધ: એકરૂપતા વિરુદ્ધ સમરૂપતા (સમાન કદ વિરુદ્ધ સમાન આકાર)",
        "In Class 9, we studied **Congruent Figures (सर्वांगसम आकृतियाँ / એકરૂપ આકૃતિઓ)**. Two figures are congruent ($\cong$) if they have both the **same shape** and the **same size**.\n\nIn Class 10, we study **Similar Figures (समरूप आकृतियाँ / સમરૂપ આકૃતિઓ)** ($\sim$). Two figures are similar if they have the **same shape**, but may differ in size!\n\n**The Golden Rule:**\n- All congruent figures are similar ($\cong \implies \sim$).\n- However, similar figures are NOT necessarily congruent ($\sim \not\implies \cong$).\n- A passport photo and a billboard poster of the same person are similar, not congruent!",
        "कक्षा 9 में, हमने **सर्वांगसम आकृतियों (Congruent Figures)** का अध्ययन किया था। दो आकृतियाँ सर्वांगसम ($\cong$) होती हैं यदि उनका **आकार और माप दोनों समान** हों।\n\nकक्षा 10 में, हम **समरूप आकृतियों (Similar Figures)** ($\sim$) का अध्ययन करते हैं। दो आकृतियाँ समरूप होती हैं यदि उनका **आकार समान** हो, भले ही उनका माप भिन्न हो!\n\n**स्वर्ण नियम:**\n- सभी सर्वांगसम आकृतियाँ समरूप होती हैं ($\cong \implies \sim$)।\n- परंतु, समरूप आकृतियों का सर्वांगसम होना आवश्यक नहीं है ($\sim \not\implies \cong$)।\n- एक ही व्यक्ति का पासपोर्ट फोटो और बड़ा होर्डिंग पोस्टर समरूप होते हैं, सर्वांगसम नहीं!",
        "ધોરણ 9 માં, આપણે **એકરૂપ આકૃતિઓ (Congruent Figures)** નો અભ્યાસ કર્યો હતો. બે આકૃતિઓ એકરૂપ ($\cong$) ત્યારે કહેવાય જ્યારે તેમનો **આકાર અને કદ બંને સમાન** હોય.\n\nધોરણ 10 માં, આપણે **સમરૂપ આકૃતિઓ (Similar Figures)** ($\sim$) નો અભ્યાસ કરીએ છીએ. બે આકૃતિઓ સમરૂપ ત્યારે કહેવાય જ્યારે તેમનો **આકાર એક સરખો** હોય, ભલે તેમનું કદ અલગ હોય!\n\n**સુવર્ણ નિયમ:**\n- બધી એકરૂપ આકૃતિઓ સમરૂપ હોય છે ($\cong \implies \sim$).\n- પરંતુ, સમરૂપ આકૃતિઓ એકરૂપ હોય જ એ જરૂરી નથી ($\sim \not\implies \cong$).\n- એક જ વ્યક્તિનો પાસપોર્ટ ફોટો અને વિશાળ હોર્ડિંગ પોસ્ટર સમરૂપ છે, એકરૂપ નથી!",
        btype="discovery",
        bloom="Understand",
        diff="Beginner",
        mins=3
    ))

    # 4. Theory: Conditions for Similarity of Polygons
    blocks.append(make_theory(
        "C10M_CH6_4",
        "Definition & Conditions for Similarity of Polygons",
        "बहुभुजों की समरूपता की परिभाषा एवं शर्तें",
        "બહુકોણોની સમરૂપતાની વ્યાખ્યા અને શરતો",
        "Two polygons having the same number of sides are **similar** if and only if:\n\n1. **Corresponding angles are equal:** \n   $$\\angle A = \\angle P, \\quad \\angle B = \\angle Q, \\quad \\dots$$\n2. **Corresponding sides are in the same ratio (proportional):** \n   $$\\frac{AB}{PQ} = \\frac{BC}{QR} = \\dots = k$$\n\nThe constant ratio $k$ is called the **scale factor** (or similarity ratio).\n- If $k = 1$, the figures are congruent.\n- If $k > 1$, the figure is enlarged.\n- If $k < 1$, the figure is reduced.",
        "समान भुजाओं की संख्या वाले दो बहुभुज **समरूप** होते हैं यदि और केवल यदि:\n\n1. **उनके संगत कोण बराबर हों:** \n   $$\\angle A = \\angle P, \\quad \\angle B = \\angle Q, \\quad \\dots$$\n2. **उनकी संगत भुजाएँ एक ही अनुपात में (समानुपाती) हों:** \n   $$\\frac{AB}{PQ} = \\frac{BC}{QR} = \\dots = k$$\n\nइस अचर अनुपात $k$ को **स्केल गुणक (Scale Factor)** या समरूपता अनुपात कहा जाता है।\n- यदि $k = 1$ है, तो आकृतियाँ सर्वांगसम होती हैं।\n- यदि $k > 1$ है, तो आकृति बड़ी (प्रवर्धित) होती है।\n- यदि $k < 1$ है, तो आकृति छोटी (लघुकृत) होती है।",
        "સમાન સંખ્યાની બાજુઓવાળા બે બહુકોણ **સમરૂપ** ત્યારે જ બને જો:\n\n1. **તેમના અનુરૂપ ખૂણાઓ સમાન હોય:** \n   $$\\angle A = \\angle P, \\quad \\angle B = \\angle Q, \\quad \\dots$$\n2. **તેમની અનુરૂપ બાજુઓ એક જ ગુણોત્તરમાં (સમપ્રમાણમાં) હોય:** \n   $$\\frac{AB}{PQ} = \\frac{BC}{QR} = \\dots = k$$\n\nઆ અચળ ગુણોત્તર $k$ ને **સ્કેલ ગુણક (Scale Factor)** કહેવામાં આવે છે.\n- જો $k = 1$ હોય, તો આકૃતિઓ એકરૂપ હોય છે.\n- જો $k > 1$ હોય, તો આકૃતિ મોટી બને છે.\n- જો $k < 1$ હોય, તો આકૃતિ નાની બને છે.",
        btype="theory",
        bloom="Remember",
        diff="Beginner",
        mins=3
    ))

    # 5. Teacher Tip: General Polygons vs Triangles
    blocks.append(make_theory(
        "C10M_CH6_5",
        "Teacher Tip: The Polygon Trap vs The Triangle Secret",
        "शिक्षक युक्ति: बहुभुज का भ्रम बनाम त्रिभुज का रहस्य",
        "શિક્ષકની સલાહ: બહુકોણની જાળ વિરુદ્ધ ત્રિકોણનું રહસ્ય",
        "**Beware of this common misconception!**\nFor general polygons with 4 or more sides, satisfying ONE condition does NOT automatically guarantee the other:\n- A square and a rectangle both have all angles equal to 90°, but their sides are NOT proportional (so they are not similar).\n- A square and a rhombus both have equal sides ($k = 1$), but their angles are NOT equal (so they are not similar).\n\n**The Triangle Miracle:** Triangles are uniquely rigid! In triangles, if corresponding angles are equal, the sides are automatically proportional, and vice versa! We will prove this in Theorem 6.3 and Theorem 6.4.",
        "**इस सामान्य भ्रम से सावधान रहें!**\n4 या अधिक भुजाओं वाले सामान्य बहुभुजों के लिए, केवल एक शर्त पूरी होने से दूसरी शर्त स्वतः पूरी नहीं होती:\n- एक वर्ग और एक आयत दोनों के सभी कोण 90° होते हैं, लेकिन उनकी भुजाएँ समानुपाती नहीं होतीं (इसलिए वे समरूप नहीं हैं)।\n- एक वर्ग और एक समचतुर्भुज दोनों की सभी भुजाएँ बराबर होती हैं, लेकिन उनके कोण बराबर नहीं होते (इसलिए वे समरूप नहीं हैं)।\n\n**त्रिभुज का चमत्कार:** त्रिभुज विशिष्ट होते हैं! त्रिभुजों में, यदि संगत कोण बराबर हों, तो भुजाएँ स्वतः समानुपाती हो जाती हैं, और इसका विलोम भी सत्य है! हम इसे प्रमेय 6.3 और 6.4 में सिद्ध करेंगे।",
        "**આ સામાન્ય ગેરસમજથી સાવધ રહો!**\n4 કે તેથી વધુ બાજુઓવાળા સામાન્ય બહુકોણ માટે, માત્ર એક શરત પૂરી થવાથી બીજી શરત આપમેળે પૂરી થતી નથી:\n- ચોરસ અને લંબચોરસ બંનેના બધા ખૂણા 90° હોય છે, પરંતુ તેમની બાજુઓ સમપ્રમાણમાં હોતી નથી (તેથી તેઓ સમરૂપ નથી).\n- ચોરસ અને સમબાજુ ચતુષ્કોણ બંનેની બાજુઓ સમાન હોય છે, પરંતુ તેમના ખૂણા સમાન હોતા નથી (તેથી તેઓ સમરૂપ નથી).\n\n**ત્રિકોણનો ચમત્કાર:** ત્રિકોણ અદ્વિતીય છે! ત્રિકોણમાં જો અનુરૂપ ખૂણાઓ સમાન હોય, તો બાજુઓ આપમેળે સમપ્રમાણમાં થઈ જાય છે, અને પ્રતીપ પણ સાચું છે! આપણે આ પ્રમેય 6.3 અને 6.4 માં સાબિત કરીશું.",
        btype="teacher_tip",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.1 Q1 (i to iv)
    blocks.append(make_quiz(
        "C10M_CH6_EX6.1_Q1_part1",
        "Exercise 6.1 (Q1.i): Fill in the blank: All circles are _________ (congruent, similar).",
        "प्रश्नावली 6.1 (Q1.i): रिक्त स्थान भरिए: सभी वृत्त _________ होते हैं (सर्वांगसम, समरूप)।",
        "સ્વાધ્યાય 6.1 (Q1.i): ખાલી જગ્યા પૂરો: બધા વર્તુળો _________ છે (એકરૂપ, સમરૂપ).",
        ["similar", "congruent", "equal in circumference", "elliptical"],
        ["समरूप", "सर्वांगसम", "परिधि में बराबर", "दीर्घवृत्ताकार"],
        ["સમરૂપ", "એકરૂપ", "પરિઘમાં સમાન", "ઉપવલયાકાર"],
        0,
        "All circles have the exact same circular shape with uniform curvature. Since radii can vary, circles have different sizes but identical shape, making them similar.",
        "सभी वृत्तों का आकार एक समान वृत्ताकार होता है। चूँकि त्रिज्याएँ भिन्न हो सकती हैं, इसलिए वृत्तों का माप अलग हो सकता है लेकिन रूप समान रहता है, अतः वे समरूप होते हैं।",
        "બધા વર્તુળોનો આકાર એક સરખો ગોળાકાર હોય છે. ત્રિજ્યા અલગ હોઈ શકે છે, તેથી તેમનું કદ જુદું હોઈ શકે પરંતુ આકાર સમાન રહે છે, તેથી તેઓ સમરૂપ છે.",
        bloom="Remember",
        diff="Beginner",
        mins=1
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.1_Q1_part2",
        "Exercise 6.1 (Q1.ii): Fill in the blank: All squares are _________ (similar, congruent).",
        "प्रश्नावली 6.1 (Q1.ii): रिक्त स्थान भरिए: सभी वर्ग _________ होते हैं (समरूप, सर्वांगसम)।",
        "સ્વાધ્યાય 6.1 (Q1.ii): ખાલી જગ્યા પૂરો: બધા ચોરસ _________ છે (સમરૂપ, એકરૂપ).",
        ["similar", "congruent", "rhombuses with non-right angles", "rectangles with unequal sides"],
        ["समरूप", "सर्वांगसम", "असमकोण वाले समचतुर्भुज", "असमान भुजाओं वाले आयत"],
        ["સમરૂપ", "એકરૂપ", "કાટકોણ વગરના સમબાજુ ચતુષ્કોણ", "અસમાન બાજુઓવાળા લંબચોરસ"],
        0,
        "Every square has four 90° angles (corresponding angles equal) and all four sides equal, so side ratios are always equal. Hence, all squares are similar.",
        "प्रत्येक वर्ग के चारों कोण 90° होते हैं (संगत कोण बराबर) और चारों भुजाएँ बराबर होती हैं, जिससे भुजाओं का अनुपात हमेशा बराबर रहता है। अतः सभी वर्ग समरूप होते हैं।",
        "દરેક ચોરસના ચારેય ખૂણા 90° હોય છે (અનુરૂપ ખૂણા સમાન) અને ચારેય બાજુઓ સમાન હોય છે, જેથી બાજુઓનો ગુણોત્તર હંમેશા સમાન રહે છે. તેથી બધા ચોરસ સમરૂપ છે.",
        bloom="Remember",
        diff="Beginner",
        mins=1
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.1_Q1_part3",
        "Exercise 6.1 (Q1.iii): Fill in the blank: All _________ triangles are similar (isosceles, equilateral).",
        "प्रश्नावली 6.1 (Q1.iii): रिक्त स्थान भरिए: सभी _________ त्रिभुज समरूप होते हैं (समद्विबाहु, समबाहु)।",
        "સ્વાધ્યાય 6.1 (Q1.iii): ખાલી જગ્યા પૂરો: બધા _________ ત્રિકોણ સમરૂપ છે (સમદ્વિબાજુ, સમબાજુ).",
        ["equilateral", "isosceles", "scalene right", "obtuse scalene"],
        ["समबाहु", "समद्विबाहु", "विषमबाहु समकोण", "अधिककोण विषमबाहु"],
        ["સમબાજુ", "સમદ્વિબાજુ", "વિષમબાજુ કાટકોણ", "ગુરુકોણ વિષમબાજુ"],
        0,
        "In any equilateral triangle, all three angles are 60° and all three sides are equal. Therefore, corresponding angles are always equal and corresponding sides are proportional.",
        "किसी भी समबाहु त्रिभुज में तीनों कोण 60° होते हैं और तीनों भुजाएँ बराबर होती हैं। अतः संगत कोण हमेशा बराबर और संगत भुजाएँ समानुपाती होती हैं।",
        "કોઈપણ સમબાજુ ત્રિકોણમાં ત્રણેય ખૂણા 60° હોય છે અને ત્રણેય બાજુઓ સમાન હોય છે. તેથી અનુરૂપ ખૂણા હંમેશા સમાન અને બાજુઓ સમપ્રમાણમાં હોય છે.",
        bloom="Remember",
        diff="Beginner",
        mins=1
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.1_Q1_part4",
        "Exercise 6.1 (Q1.iv): Two polygons of the same number of sides are similar, if (a) their corresponding angles are _________ and (b) their corresponding sides are _________ (equal, proportional).",
        "प्रश्नावली 6.1 (Q1.iv): भुजाओं की समान संख्या वाले दो बहुभुज समरूप होते हैं, यदि (a) उनके संगत कोण _________ हों तथा (b) उनकी संगत भुजाएँ _________ हों (बराबर, समानुपाती)।",
        "સ્વાધ્યાય 6.1 (Q1.iv): સમાન સંખ્યાની બાજુઓવાળા બે બહુકોણ સમરૂપ થાય, જો (a) તેમના અનુરૂપ ખૂણાઓ _________ હોય અને (b) તેમની અનુરૂપ બાજુઓ _________ હોય (સમાન, સમપ્રમાણમાં).",
        [
            "(a) equal, (b) proportional",
            "(a) proportional, (b) equal",
            "(a) supplementary, (b) equal",
            "(a) complementary, (b) proportional"
        ],
        [
            "(a) बराबर, (b) समानुपाती",
            "(a) समानुपाती, (b) बराबर",
            "(a) संपूरक, (b) बराबर",
            "(a) पूरक, (b) समानुपाती"
        ],
        [
            "(a) સમાન, (b) સમપ્રમાણમાં",
            "(a) સમપ્રમાણમાં, (b) સમાન",
            "(a) પૂરક, (b) સમાન",
            "(a) કોટિકોણ, (b) સમપ્રમાણમાં"
        ],
        0,
        "By definition of polygon similarity, corresponding angles must be equal, and corresponding sides must be proportional.",
        "बहुभुज समरूपता की परिभाषा के अनुसार, संगत कोण बराबर होने चाहिए और संगत भुजाएँ समानुपाती होनी चाहिए।",
        "બહુકોણ સમરૂપતાની વ્યાખ્યા મુજબ, અનુરૂપ ખૂણાઓ સમાન હોવા જોઈએ અને અનુરૂપ બાજુઓ સમપ્રમાણમાં હોવી જોઈએ.",
        bloom="Remember",
        diff="Beginner",
        mins=1
    ))

    # Exercise 6.1 Q2 (i and ii)
    blocks.append(make_quiz(
        "C10M_CH6_EX6.1_Q2_part1",
        "Exercise 6.1 (Q2.i): Which of the following is a pair of similar figures?",
        "प्रश्नावली 6.1 (Q2.i): निम्नलिखित में से कौन समरूप आकृतियों का एक युग्म है?",
        "સ્વાધ્યાય 6.1 (Q2.i): નીચેનામાંથી કઈ જોડી સમરૂપ આકૃતિઓની જોડી છે?",
        [
            "Two equilateral triangles with sides 3 cm and 6 cm",
            "A square and a rectangle",
            "An equilateral triangle and a scalene right triangle",
            "A rhombus and a trapezium"
        ],
        [
            "3 सेमी और 6 सेमी भुजाओं वाले दो समबाहु त्रिभुज",
            "एक वर्ग और एक आयत",
            "एक समबाहु त्रिभुज और एक विषमबाहु समकोण त्रिभुज",
            "एक समचतुर्भुज और एक समलंब"
        ],
        [
            "3 સેમી અને 6 સેમી બાજુવાળા બે સમબાજુ ત્રિકોણ",
            "એક ચોરસ અને એક લંબચોરસ",
            "એક સમબાજુ ત્રિકોણ અને એક વિષમબાજુ કાટકોણ ત્રિકોણ",
            "એક સમબાજુ ચતુષ્કોણ અને એક સમલંબ"
        ],
        0,
        "Any two equilateral triangles have corresponding angles equal to 60° and sides in a constant ratio (3/6 = 1/2). Hence, they are always similar.",
        "किन्हीं भी दो समबाहु त्रिभुजों के संगत कोण 60° होते हैं और भुजाओं का अनुपात स्थिर (3/6 = 1/2) होता है। अतः वे हमेशा समरूप होते हैं।",
        "કોઈપણ બે સમબાજુ ત્રિકોણના અનુરૂપ ખૂણા 60° હોય છે અને બાજુઓ અચળ ગુણોત્તર (3/6 = 1/2) માં હોય છે. તેથી તેઓ હંમેશા સમરૂપ હોય છે.",
        bloom="Understand",
        diff="Beginner",
        mins=1
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.1_Q2_part2",
        "Exercise 6.1 (Q2.ii): Which of the following is a pair of non-similar figures?",
        "प्रश्नावली 6.1 (Q2.ii): निम्नलिखित में से कौन ऐसी आकृतियों का युग्म है जो समरूप नहीं हैं?",
        "સ્વાધ્યાય 6.1 (Q2.ii): નીચેનામાંથી કઈ જોડી એવી આકૃતિઓની જોડી છે જે સમરૂપ નથી?",
        [
            "A square of side 4 cm and a rectangle of sides 4 cm and 6 cm",
            "Two circles of radii 2 cm and 5 cm",
            "Two squares of sides 3 cm and 8 cm",
            "Two equilateral triangles of sides 2 cm and 7 cm"
        ],
        [
            "4 सेमी भुजा वाला एक वर्ग और 4 सेमी व 6 सेमी भुजाओं वाला एक आयत",
            "2 सेमी और 5 सेमी त्रिज्या वाले दो वृत्त",
            "3 सेमी और 8 सेमी भुजाओं वाले दो वर्ग",
            "2 सेमी और 7 सेमी भुजाओं वाले दो समबाहु त्रिभुज"
        ],
        [
            "4 સેમી બાજુવાળો એક ચોરસ અને 4 સેમી તથા 6 સેમી બાજુવાળો એક લંબચોરસ",
            "2 સેમી અને 5 સેમી ત્રિજ્યાવાળા બે વર્તુળો",
            "3 સેમી અને 8 સેમી બાજુવાળા બે ચોરસ",
            "2 સેમી અને 7 સેમી બાજુવાળા બે સમબાજુ ત્રિકોણ"
        ],
        0,
        "A square and a rectangle have equal angles (90°), but their sides are not in the same ratio (4/4 ≠ 4/6). Hence, they are non-similar figures.",
        "एक वर्ग और एक आयत के सभी कोण बराबर (90°) होते हैं, परंतु उनकी भुजाएँ समान अनुपात में नहीं होतीं (4/4 ≠ 4/6)। अतः वे समरूप आकृतियाँ नहीं हैं।",
        "ચોરસ અને લંબચોરસના ખૂણા સમાન (90°) હોય છે, પરંતુ તેમની બાજુઓ સમાન ગુણોત્તરમાં હોતી નથી (4/4 ≠ 4/6). તેથી તેઓ સમરૂપ આકૃતિઓ નથી.",
        bloom="Understand",
        diff="Beginner",
        mins=1
    ))

    # Exercise 6.1 Q3
    blocks.append(make_quiz(
        "C10M_CH6_EX6.1_Q3",
        "Exercise 6.1 (Q3): State whether quadrilateral PQRS (rhombus with sides 1.5 cm and non-right angles) and quadrilateral ABCD (square with sides 3 cm and 90° angles) are similar.",
        "प्रश्नावली 6.1 (Q3): बताइए कि क्या चतुर्भुज PQRS (1.5 सेमी भुजा वाला समचतुर्भुज, कोण 90° नहीं) और चतुर्भुज ABCD (3 सेमी भुजा वाला वर्ग, सभी कोण 90°) समरूप हैं।",
        "સ્વાધ્યાય 6.1 (Q3): જણાવો કે શું ચતુષ્કોણ PQRS (1.5 સેમી બાજુવાળો સમબાજુ ચતુષ્કોણ, ખૂણા 90° નથી) અને ચતુષ્કોણ ABCD (3 સેમી બાજુવાળો ચોરસ, બધા ખૂણા 90°) સમરૂપ છે કે નહીં.",
        [
            "No, because corresponding angles are not equal",
            "Yes, because their sides are proportional (1.5/3 = 1/2)",
            "Yes, because both are quadrilaterals",
            "No, because their perimeters are different"
        ],
        [
            "नहीं, क्योंकि उनके संगत कोण बराबर नहीं हैं",
            "हाँ, क्योंकि उनकी भुजाएँ समानुपाती हैं (1.5/3 = 1/2)",
            "हाँ, क्योंकि दोनों चतुर्भुज हैं",
            "नहीं, क्योंकि उनके परिमाप भिन्न हैं"
        ],
        [
            "ના, કારણ કે તેમના અનુરૂપ ખૂણાઓ સમાન નથી",
            "હા, કારણ કે તેમની બાજુઓ સમપ્રમાણમાં છે (1.5/3 = 1/2)",
            "હા, કારણ કે બંને ચતુષ્કોણ છે",
            "ના, કારણ કે તેમની પરિમિતિ અલગ છે"
        ],
        0,
        "Although corresponding sides are in the same ratio (1.5/3 = 1/2), the angles of rhombus PQRS are not 90°, whereas all angles of square ABCD are 90°. Since corresponding angles are not equal, the quadrilaterals are not similar.",
        "यद्यपि संगत भुजाएँ समान अनुपात में हैं (1.5/3 = 1/2), परंतु समचतुर्भुज PQRS के कोण 90° नहीं हैं, जबकि वर्ग ABCD के सभी कोण 90° हैं। चूँकि संगत कोण बराबर नहीं हैं, इसलिए ये चतुर्भुज समरूप नहीं हैं।",
        "જોકે અનુરૂપ બાજુઓ સમાન ગુણોત્તરમાં છે (1.5/3 = 1/2), પરંતુ સમબાજુ ચતુષ્કોણ PQRS ના ખૂણા 90° નથી, જ્યારે ચોરસ ABCD ના બધા ખૂણા 90° છે. અનુરૂપ ખૂણા સમાન ન હોવાથી, આ ચતુષ્કોણો સમરૂપ નથી.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    return blocks

# =========================================================================
# PART 2: BASIC PROPORTIONALITY THEOREM & EXERCISE 6.2
# =========================================================================
def get_part2_blocks():
    blocks = []

    # 13. Hook: Thales of Miletus
    blocks.append(make_theory(
        "C10M_CH6_6",
        "Thales of Miletus and the Pyramid's Shadow",
        "माइलेटस के थेल्स और पिरामिड की परछाई",
        "મિલેટસના થેલ્સ અને પિરામિડનો પડછાયો",
        "Over 2,600 years ago, Greek mathematician **Thales of Miletus** visited Egypt. The Egyptian Pharaoh challenged him to determine the height of the Great Pyramid of Giza. Without climbing a single stone, Thales planted his walking staff upright in the desert sand. He observed the sun cast shadows of both his stick and the mighty pyramid.\n\nHe waited until the shadow of the staff was equal to its height, and declared: 'At this very moment, the height of the pyramid is equal to the length of its shadow!' Thales realized that the sun's parallel rays create **similar triangles**. This groundbreaking insight gave birth to the **Basic Proportionality Theorem (आधारभूत आनुपातिकता प्रमेय / સમપ્રમાણતાનું મૂળભૂત પ્રમેય)**, widely celebrated as **Thales' Theorem**!",
        "2,600 वर्ष से भी पहले, यूनानी गणितज्ञ **माइलेटस के थेल्स (Thales of Miletus)** मिस्र गए। मिस्र के फराओ ने उन्हें गीज़ा के महान पिरामिड की ऊँचाई मापने की चुनौती दी। बिना किसी पत्थर पर चढ़े, थेल्स ने अपनी लाठी को रेगिस्तान की रेत में सीधा खड़ा कर दिया। उन्होंने देखा कि सूर्य उनकी लाठी और विशाल पिरामिड दोनों की परछाई बना रहा था।\n\nउन्होंने तब तक प्रतीक्षा की जब तक लाठी की परछाई उसकी ऊँचाई के बराबर नहीं हो गई, और घोषणा की: 'इस क्षण, पिरामिड की ऊँचाई उसकी परछाई की लंबाई के बराबर है!' थेल्स ने समझा कि सूर्य की समानांतर किरणें **समरूप त्रिभुज** बनाती हैं। इस खोज ने **आधारभूत आनुपातिकता प्रमेय (थेल्स प्रमेय)** को जन्म दिया!",
        "2,600 વર્ષથી પણ વધુ સમય પહેલાં, ગ્રીક ગણિતશાસ્ત્રી **મિલેટસના થેલ્સ (Thales of Miletus)** ઇજિપ્ત ગયા. ઇજિપ્તના રાજાએ તેમને ગીઝાના વિશાળ પિરામિડની ઊંચાઈ માપવાનો પડકાર આપ્યો. કોઈપણ પથ્થર પર ચઢ્યા વિના, થેલ્સે પોતાની લાકડી રણની રેતીમાં ઊભી રોપી દીધી. તેમણે જોયું કે સૂર્ય તેમની લાકડી અને પિરામિડ બંનેનો પડછાયો પાડી રહ્યો હતો.\n\nલાકડીનો પડછાયો તેની લંબાઈ જેટલો થયો ત્યાં સુધી તેમણે રાહ જોઈ અને જાહેર કર્યું: 'આ જ ક્ષણે, પિરામિડની ઊંચાઈ તેના પડછાયાની લંબાઈ જેટલી છે!' થેલ્સે સમજ્યું કે સૂર્યના સમાંતર કિરણો **સમરૂપ ત્રિકોણ** બનાવે છે. આ ક્રાંતિકારી શોધે **સમપ્રમાણતાના મૂળભૂત પ્રમેય (થેલ્સનું પ્રમેય)** ને જન્મ આપ્યો!",
        btype="hook",
        bloom="Understand",
        diff="Beginner",
        mins=3
    ))

    # 14. Socratic Question
    blocks.append(make_quiz(
        "C10M_CH6_7",
        "A vertical 2-metre pole casts a shadow of 3 metres on level ground. At the exact same moment, a nearby tree casts a shadow of 12 metres. What is the height of the tree?",
        "एक ऊर्ध्वाधर 2-मीटर लंबा खंभा समतल जमीन पर 3 मीटर लंबी परछाई बनाता है। ठीक उसी क्षण, पास का एक पेड़ 12 मीटर लंबी परछाई बनाता है। पेड़ की ऊँचाई क्या है?",
        "એક ઊભો 2-મીટર લાંબો થાંભલો જમીન પર 3 મીટર લાંબો પડછાયો પાડે છે. બરાબર તે જ સમયે, નજીકનું એક ઝાડ 12 મીટર લાંબો પડછાયો પાડે છે. ઝાડની ઊંચાઈ કેટલી છે?",
        ["8 metres", "6 metres", "18 metres", "10 metres"],
        ["8 मीटर", "6 मीटर", "18 मीटर", "10 मीटर"],
        ["8 મીટર", "6 મીટર", "18 મીટર", "10 મીટર"],
        0,
        "Because the sun's rays strike at the same angle, the ratio of height to shadow is constant: Height / Shadow = 2 / 3 = H / 12 => H = (2/3) × 12 = 8 metres.",
        "चूँकि सूर्य की किरणें समान कोण पर पड़ती हैं, ऊँचाई और परछाई का अनुपात स्थिर रहता है: ऊँचाई / परछाई = 2 / 3 = H / 12 => H = (2/3) × 12 = 8 मीटर।",
        "સૂર્યના કિરણો એક જ ખૂણે આપાત થતા હોવાથી, ઊંચાઈ અને પડછાયાનો ગુણોત્તર અચળ રહે છે: ઊંચાઈ / પડછાયો = 2 / 3 = H / 12 => H = (2/3) × 12 = 8 મીટર.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 15. Discovery: Area ratio proof intuition
    blocks.append(make_theory(
        "C10M_CH6_8",
        "Discovery: The Area Method that Proves BPT",
        "खोज: क्षेत्रफल विधि जो BPT को सिद्ध करती है",
        "શોધ: ક્ષેત્રફળ પદ્ધતિ જે BPT ને સાબિત કરે છે",
        "Consider $\\triangle ABC$. Draw line $DE \\parallel BC$ cutting $AB$ at $D$ and $AC$ at $E$. Join $BE$ and $CD$, and draw heights $EN \\perp AB$ and $DM \\perp AC$.\n\n1. Area of $\\triangle ADE = \\frac{1}{2} \\times AD \\times EN$\n2. Area of $\\triangle BDE = \\frac{1}{2} \\times DB \\times EN$\n   $$\\frac{\\text{ar}(\\triangle ADE)}{\\text{ar}(\\triangle BDE)} = \\frac{AD}{DB}$$\n\n3. Similarly, taking base $AE$ and $EC$ with height $DM$:\n   $$\\frac{\\text{ar}(\\triangle ADE)}{\\text{ar}(\\triangle CDE)} = \\frac{AE}{EC}$$\n\n**The Crucial Link:** $\\triangle BDE$ and $\\triangle CDE$ share the same base $DE$ and lie between the same parallel lines ($DE \\parallel BC$). From Class 9, their areas are equal: $\\text{ar}(\\triangle BDE) = \\text{ar}(\\triangle CDE)$!\n\nTherefore, LHS equals RHS: $\\mathbf{\\frac{AD}{DB} = \\frac{AE}{EC}}$!",
        "$\\triangle ABC$ पर विचार करें। भुजा $AB$ पर $D$ और $AC$ पर $E$ को प्रतिच्छेद करते हुए एक रेखा $DE \\parallel BC$ खींचें। $BE$ और $CD$ को मिलाएँ, तथा शीर्षलम्ब $EN \\perp AB$ और $DM \\perp AC$ खींचें।\n\n1. $\\triangle ADE$ का क्षेत्रफल $= \\frac{1}{2} \\times AD \\times EN$\n2. $\\triangle BDE$ का क्षेत्रफल $= \\frac{1}{2} \\times DB \\times EN$\n   $$\\frac{\\text{ar}(\\triangle ADE)}{\\text{ar}(\\triangle BDE)} = \\frac{AD}{DB}$$\n\n3. इसी प्रकार, शीर्षलम्ब $DM$ के साथ आधार $AE$ और $EC$ लेने पर:\n   $$\\frac{\\text{ar}(\\triangle ADE)}{\\text{ar}(\\triangle CDE)} = \\frac{AE}{EC}$$\n\n**महत्वपूर्ण कड़ी:** $\\triangle BDE$ और $\\triangle CDE$ का एक ही आधार $DE$ है और वे एक ही समांतर रेखाओं ($DE \\parallel BC$) के बीच स्थित हैं। कक्षा 9 के प्रमेय से, इनके क्षेत्रफल बराबर हैं: $\\text{ar}(\\triangle BDE) = \\text{ar}(\\triangle CDE)$!\n\nअतः, $\\mathbf{\\frac{AD}{DB} = \\frac{AE}{EC}}$ सिद्ध होता है!",
        "$\\triangle ABC$ નો વિચાર કરો. બાજુ $AB$ ને $D$ માં અને $AC$ ને $E$ માં છેદતી રેખા $DE \\parallel BC$ દોરો. $BE$ અને $CD$ જોડો, તથા વેધ $EN \\perp AB$ અને $DM \\perp AC$ દોરો.\n\n1. $\\triangle ADE$ નું ક્ષેત્રફળ $= \\frac{1}{2} \\times AD \\times EN$\n2. $\\triangle BDE$ નું ક્ષેત્રફળ $= \\frac{1}{2} \\times DB \\times EN$\n   $$\\frac{\\text{ar}(\\triangle ADE)}{\\text{ar}(\\triangle BDE)} = \\frac{AD}{DB}$$\n\n3. એ જ રીતે, વેધ $DM$ સાથે પાયો $AE$ અને $EC$ લેતા:\n   $$\\frac{\\text{ar}(\\triangle ADE)}{\\text{ar}(\\triangle CDE)} = \\frac{AE}{EC}$$\n\n**મુખ્ય કડી:** $\\triangle BDE$ અને $\\triangle CDE$ એક જ પાયા $DE$ પર અને સમાંતર રેખાઓ ($DE \\parallel BC$) વચ્ચે આવેલા છે. ધોરણ 9 ના પ્રમેય મુજબ, તેમના ક્ષેત્રફળ સમાન છે: $\\text{ar}(\\triangle BDE) = \\text{ar}(\\triangle CDE)$!\n\nતેથી, $\\mathbf{\\frac{AD}{DB} = \\frac{AE}{EC}}$ સાબિત થાય છે!",
        btype="discovery",
        bloom="Analyze",
        diff="Intermediate",
        mins=4
    ))

    # 16. Theory: Theorem 6.1 (BPT)
    blocks.append(make_theory(
        "C10M_CH6_9",
        "Theorem 6.1: Basic Proportionality Theorem (BPT)",
        "प्रमेय 6.1: आधारभूत आनुपातिकता प्रमेय (थेल्स प्रमेय)",
        "પ્રમેય 6.1: સમપ્રમાણતાનું મૂળભૂત પ્રમેય (થેલ્સનું પ્રમેય)",
        "**Statement (Theorem 6.1):**\nIf a line is drawn parallel to one side of a triangle to intersect the other two sides in distinct points, the other two sides are divided in the same ratio.\n\nIn $\\triangle ABC$, if $DE \\parallel BC$, then:\n$$\\mathbf{\\frac{AD}{DB} = \\frac{AE}{EC}}$$\n\n**Useful Alternate Forms (Adding 1 to both sides):**\n1. $\\frac{AD}{DB} + 1 = \\frac{AE}{EC} + 1 \\implies \\mathbf{\\frac{AB}{DB} = \\frac{AC}{EC}}$\n2. Reciprocating first: $\\frac{DB}{AD} + 1 = \\frac{EC}{AE} + 1 \\implies \\mathbf{\\frac{AB}{AD} = \\frac{AC}{AE}}$\n\nThese alternative ratios allow you to relate a part of the side to the whole side directly!",
        "**कथन (प्रमेय 6.1):**\nयदि किसी त्रिभुज की एक भुजा के समांतर अन्य दो भुजाओं को भिन्न-भिन्न बिंदुओं पर प्रतिच्छेद करने के लिए एक रेखा खींची जाए, तो ये अन्य दो भुजाएँ एक ही अनुपात में विभाजित हो जाती हैं।\n\n$\\triangle ABC$ में, यदि $DE \\parallel BC$ हो, तो:\n$$\\mathbf{\\frac{AD}{DB} = \\frac{AE}{EC}}$$\n\n**उपयोगी वैकल्पिक रूप (दोनों पक्षों में 1 जोड़ने पर):**\n1. $\\frac{AD}{DB} + 1 = \\frac{AE}{EC} + 1 \\implies \\mathbf{\\frac{AB}{DB} = \\frac{AC}{EC}}$\n2. व्युत्क्रम करके जोड़ने पर: $\\frac{DB}{AD} + 1 = \\frac{EC}{AE} + 1 \\implies \\mathbf{\\frac{AB}{AD} = \\frac{AC}{AE}}$\n\nये वैकल्पिक अनुपात आपको पूरी भुजा और उसके खंड के बीच सीधा संबंध स्थापित करने में मदद करते हैं!",
        "**વિધાન (પ્રમેય 6.1):**\nજો ત્રિકોણની કોઈ એક બાજુને સમાંતર દોરેલી રેખા બાકીની બે બાજુઓને ભિન્ન બિંદુઓમાં છેદે, તો તે બાજુઓ પર કપાતા રેખાખંડો તે બાજુઓનું સમાન ગુણોત્તરમાં વિભાજન કરે છે.\n\n$\\triangle ABC$ માં, જો $DE \\parallel BC$ હોય, તો:\n$$\\mathbf{\\frac{AD}{DB} = \\frac{AE}{EC}}$$\n\n**ઉપયોગી વૈકલ્પિક સ્વરૂપો (બંને બાજુ 1 ઉમેરતા):**\n1. $\\frac{AD}{DB} + 1 = \\frac{AE}{EC} + 1 \\implies \\mathbf{\\frac{AB}{DB} = \\frac{AC}{EC}}$\n2. વ્યસ્ત કરીને 1 ઉમેરતા: $\\frac{DB}{AD} + 1 = \\frac{EC}{AE} + 1 \\implies \\mathbf{\\frac{AB}{AD} = \\frac{AC}{AE}}$\n\nઆ વૈકલ્પિક ગુણોત્તરો તમને બાજુના ટુકડા અને આખી બાજુ વચ્ચે સીધો સંબંધ નક્કી કરવામાં મદદ કરે છે!",
        btype="theory",
        bloom="Remember",
        diff="Beginner",
        mins=3
    ))

    # 17. Theory: Theorem 6.2 (Converse of BPT)
    blocks.append(make_theory(
        "C10M_CH6_10",
        "Theorem 6.2: Converse of Basic Proportionality Theorem",
        "प्रमेय 6.2: आधारभूत आनुपातिकता प्रमेय का विलोम",
        "પ્રમેય 6.2: સમપ્રમાણતાના મૂળભૂત પ્રમેયનું પ્રતીપ",
        "**Statement (Theorem 6.2):**\nIf a line divides any two sides of a triangle in the same ratio, then the line must be parallel to the third side.\n\nIn $\\triangle ABC$, if points $D$ on $AB$ and $E$ on $AC$ satisfy:\n$$\\mathbf{\\frac{AD}{DB} = \\frac{AE}{EC}}$$\nthen line $DE$ is parallel to side $BC$ ($DE \\parallel BC$).\n\n**Proof Logic (Contradiction):** If $DE$ is not parallel to $BC$, imagine another line $DE' \\parallel BC$. By BPT, $\\frac{AD}{DB} = \\frac{AE'}{E'C}$. Equating with the given ratio shows $E$ and $E'$ must coincide!",
        "**कथन (प्रमेय 6.2):**\nयदि एक रेखा किसी त्रिभुज की दो भुजाओं को एक ही अनुपात में विभाजित करे, तो वह तीसरी भुजा के समांतर होती है।\n\n$\\triangle ABC$ में, यदि भुजा $AB$ पर बिंदु $D$ और $AC$ पर बिंदु $E$ इस प्रकार हों कि:\n$$\\mathbf{\\frac{AD}{DB} = \\frac{AE}{EC}}$$\nतो रेखा $DE$, तीसरी भुजा $BC$ के समांतर होगी ($DE \\parallel BC$)।\n\n**उपपत्ति का तर्क (विरोधाभास):** यदि $DE \\parallel BC$ न हो, तो मान लें कि $DE' \\parallel BC$ है। BPT से $\\frac{AD}{DB} = \\frac{AE'}{E'C}$ होगा। दिए गए अनुपात से तुलना करने पर सिद्ध होता है कि $E$ और $E'$ संपाતી (coincide) हैं!",
        "**વિધાન (પ્રમેય 6.2):**\nજો કોઈ રેખા ત્રિકોણની બે બાજુઓનું સમાન ગુણોત્તરમાં વિભાજન કરે, તો તે રેખા ત્રીજી બાજુને સમાંતર હોય છે.\n\n$\\triangle ABC$ માં, જો બાજુ $AB$ પર બિંદુ $D$ અને $AC$ પર બિંદુ $E$ માટે:\n$$\\mathbf{\\frac{AD}{DB} = \\frac{AE}{EC}}$$\nહોય, તો રેખા $DE$ ત્રીજી બાજુ $BC$ ને સમાંતર હોય ($DE \\parallel BC$).\n\n**સાબિતીનો તર્ક (અનિષ્ટાપત્તિ):** જો $DE$ સમાંતર ન હોય, તો ધારો કે $DE' \\parallel BC$ છે. BPT મુજબ $\\frac{AD}{DB} = \\frac{AE'}{E'C}$ થાય. આપેલ ગુણોત્તર સાથે સરખાવતા સાબિત થાય છે કે બિંદુઓ $E$ અને $E'$ એક જ (સંપાતી) છે!",
        btype="theory",
        bloom="Understand",
        diff="Intermediate",
        mins=3
    ))

    # 18. Teacher Tip: Using BPT in Trapeziums
    blocks.append(make_theory(
        "C10M_CH6_11",
        "Teacher Tip: The Diagonal Trick for Trapeziums",
        "शिक्षक युक्ति: समलंब चतुर्भुज में विकर्ण की चाल",
        "શિક્ષકની સલાહ: સમલંબ ચતુષ્કોણમાં વિકર્ણની યુક્તિ",
        "When solving trapezium problems involving non-parallel sides and diagonals (such as Ex 6.2 Q9 and Q10):\n- Draw a construction line through the intersection of diagonals $O$ parallel to the parallel bases ($OE \\parallel AB \\parallel DC$).\n- Apply BPT in $\\triangle ABD$ to get $\\frac{AE}{ED} = \\frac{BO}{OD}$.\n- Apply BPT in $\\triangle ADC$ to get $\\frac{AE}{ED} = \\frac{AO}{OC}$.\n- Equating the common ratio immediately yields: $\\mathbf{\\frac{AO}{CO} = \\frac{BO}{DO}}$ or $\\mathbf{\\frac{AO}{BO} = \\frac{CO}{DO}}$!",
        "समलंब चतुर्भुज (Trapezium) के प्रश्नों को हल करते समय जहाँ विकर्ण दिए गए हों (जैसे प्रश्नावली 6.2 के Q9 और Q10):\n- विकर्णों के प्रतिच्छेद बिंदु $O$ से होकर समांतर भुजाओं के समांतर एक रचना रेखा $OE \\parallel AB \\parallel DC$ खींचें।\n- $\\triangle ABD$ में BPT लगाने पर: $\\frac{AE}{ED} = \\frac{BO}{OD}$ मिलता है।\n- $\\triangle ADC$ में BPT लगाने पर: $\\frac{AE}{ED} = \\frac{AO}{OC}$ मिलता है।\n- दोनों को बराबर करने पर तुरंत प्राप्त होता है: $\\mathbf{\\frac{AO}{CO} = \\frac{BO}{DO}}$ या $\\mathbf{\\frac{AO}{BO} = \\frac{CO}{DO}}$!",
        "સમલંબ ચતુષ્કોણના પ્રશ્નો ઉકેલતી વખતે જ્યાં વિકર્ણો આપેલા હોય (જેમ કે સ્વાધ્યાય 6.2 ના Q9 અને Q10):\n- વિકર્ણોના છેદબિંદુ $O$ માંથી સમાંતર બાજુઓને સમાંતર એક રચના રેખા $OE \\parallel AB \\parallel DC$ દોરો.\n- $\\triangle ABD$ માં BPT વાપરતા: $\\frac{AE}{ED} = \\frac{BO}{OD}$ મળે છે.\n- $\\triangle ADC$ માં BPT વાપરતા: $\\frac{AE}{ED} = \\frac{AO}{OC}$ મળે છે.\n- બંને સરખાવતા સીધું જ પરિણામ મળે છે: $\\mathbf{\\frac{AO}{CO} = \\frac{BO}{DO}}$ અથવા $\\mathbf{\\frac{AO}{BO} = \\frac{CO}{DO}}$!",
        btype="teacher_tip",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.2 Q1 (i and ii)
    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q1_part1",
        "Exercise 6.2 (Q1.i): In $\\triangle ABC$, $DE \\parallel BC$. Given $AD = 1.5\\text{ cm}, DB = 3\\text{ cm}$, and $AE = 1\\text{ cm}$. Find the length of $EC$.",
        "प्रश्नावली 6.2 (Q1.i): $\\triangle ABC$ में, $DE \\parallel BC$ है। दिया है $AD = 1.5\\text{ सेमी}, DB = 3\\text{ सेमी}$ और $AE = 1\\text{ सेमी}$। $EC$ की लंबाई ज्ञात कीजिए।",
        "સ્વાધ્યાય 6.2 (Q1.i): $\\triangle ABC$ માં, $DE \\parallel BC$ છે. આપેલ છે $AD = 1.5\\text{ સેમી}, DB = 3\\text{ સેમી}$ અને $AE = 1\\text{ સેમી}$। $EC$ ની લંબાઈ શોધો.",
        ["2 cm", "1.5 cm", "3 cm", "2.5 cm"],
        ["2 सेमी", "1.5 सेमी", "3 सेमी", "2.5 सेमी"],
        ["2 સેમી", "1.5 સેમી", "3 સેમી", "2.5 સેમી"],
        0,
        "By Basic Proportionality Theorem (Theorem 6.1): AD / DB = AE / EC => 1.5 / 3 = 1 / EC => 1 / 2 = 1 / EC => EC = 2 cm.",
        "आधारभूत आनुपातिकता प्रमेय (BPT) द्वारा: AD / DB = AE / EC => 1.5 / 3 = 1 / EC => 1 / 2 = 1 / EC => EC = 2 सेमी।",
        "સમપ્રમાણતાના મૂળભૂત પ્રમેય (BPT) મુજબ: AD / DB = AE / EC => 1.5 / 3 = 1 / EC => 1 / 2 = 1 / EC => EC = 2 સેમી.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q1_part2",
        "Exercise 6.2 (Q1.ii): In $\\triangle ABC$, $DE \\parallel BC$. Given $DB = 7.2\\text{ cm}, AE = 1.8\\text{ cm}$, and $EC = 5.4\\text{ cm}$. Find the length of $AD$.",
        "प्रश्नावली 6.2 (Q1.ii): $\\triangle ABC$ में, $DE \\parallel BC$ है। दिया है $DB = 7.2\\text{ सेमी}, AE = 1.8\\text{ सेमी}$ और $EC = 5.4\\text{ सेमी}$। $AD$ की लंबाई ज्ञात कीजिए।",
        "સ્વાધ્યાય 6.2 (Q1.ii): $\\triangle ABC$ માં, $DE \\parallel BC$ છે. આપેલ છે $DB = 7.2\\text{ સેમી}, AE = 1.8\\text{ સેમી}$ અને $EC = 5.4\\text{ સેમી}$। $AD$ ની લંબાઈ શોધો.",
        ["2.4 cm", "2.8 cm", "3.6 cm", "1.8 cm"],
        ["2.4 सेमी", "2.8 सेमी", "3.6 सेमी", "1.8 सेमी"],
        ["2.4 સેમી", "2.8 સેમી", "3.6 સેમી", "1.8 સેમી"],
        0,
        "By BPT: AD / DB = AE / EC => AD / 7.2 = 1.8 / 5.4 => AD / 7.2 = 1 / 3 => AD = 7.2 / 3 = 2.4 cm.",
        "BPT द्वारा: AD / DB = AE / EC => AD / 7.2 = 1.8 / 5.4 => AD / 7.2 = 1 / 3 => AD = 7.2 / 3 = 2.4 सेमी।",
        "BPT મુજબ: AD / DB = AE / EC => AD / 7.2 = 1.8 / 5.4 => AD / 7.2 = 1 / 3 => AD = 7.2 / 3 = 2.4 સેમી.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # Exercise 6.2 Q2 (i, ii, iii)
    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q2_part1",
        "Exercise 6.2 (Q2.i): $E$ and $F$ are points on sides $PQ$ and $PR$ of $\\triangle PQR$. Given $PE = 3.9\\text{ cm}, EQ = 3\\text{ cm}, PF = 3.6\\text{ cm}$, and $FR = 2.4\\text{ cm}$. Is $EF \\parallel QR$?",
        "प्रश्नावली 6.2 (Q2.i): $\\triangle PQR$ की भुजाओं $PQ$ और $PR$ पर बिंदु $E$ और $F$ स्थित हैं। दिया है $PE = 3.9\\text{ सेमी}, EQ = 3\\text{ सेमी}, PF = 3.6\\text{ सेमी}$ और $FR = 2.4\\text{ सेमी}$। क्या $EF \\parallel QR$ है?",
        "સ્વાધ્યાય 6.2 (Q2.i): $\\triangle PQR$ ની બાજુઓ $PQ$ અને $PR$ પર બિંદુઓ $E$ અને $F$ આવેલા છે. આપેલ છે $PE = 3.9\\text{ સેમી}, EQ = 3\\text{ સેમી}, PF = 3.6\\text{ સેમી}$ અને $FR = 2.4\\text{ સેમી}$। શું $EF \\parallel QR$ છે?",
        [
            "No, because PE/EQ ≠ PF/FR (1.3 ≠ 1.5)",
            "Yes, because PE/EQ = PF/FR",
            "Yes, by Converse of BPT",
            "Cannot be determined without angle measures"
        ],
        [
            "नहीं, क्योंकि PE/EQ ≠ PF/FR (1.3 ≠ 1.5)",
            "हाँ, क्योंकि PE/EQ = PF/FR",
            "हाँ, BPT के विलोम द्वारा",
            "कोणों के माप के बिना निर्धारित नहीं किया जा सकता"
        ],
        [
            "ના, કારણ કે PE/EQ ≠ PF/FR (1.3 ≠ 1.5)",
            "હા, કારણ કે PE/EQ = PF/FR",
            "હા, BPT ના પ્રતીપ મુજબ",
            "ખૂણાના માપ વિના નક્કી કરી શકાય નહીં"
        ],
        0,
        "Calculate ratios: PE / EQ = 3.9 / 3 = 1.3. PF / FR = 3.6 / 2.4 = 1.5. Since PE / EQ ≠ PF / FR, by Theorem 6.2 EF is NOT parallel to QR.",
        "अनुपातों की गणना करें: PE / EQ = 3.9 / 3 = 1.3। PF / FR = 3.6 / 2.4 = 1.5। चूँकि PE / EQ ≠ PF / FR है, अतः प्रमेय 6.2 के अनुसार EF, QR के समांतर नहीं है।",
        "ગુણોત્તરની ગણતરી કરો: PE / EQ = 3.9 / 3 = 1.3. PF / FR = 3.6 / 2.4 = 1.5. PE / EQ ≠ PF / FR હોવાથી, પ્રમેય 6.2 મુજબ EF એ QR ને સમાંતર નથી.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q2_part2",
        "Exercise 6.2 (Q2.ii): In $\\triangle PQR$, $PE = 4\\text{ cm}, QE = 4.5\\text{ cm}, PF = 8\\text{ cm}$, and $RF = 9\\text{ cm}$. Is $EF \\parallel QR$?",
        "प्रश्नावली 6.2 (Q2.ii): $\\triangle PQR$ में, $PE = 4\\text{ सेमी}, QE = 4.5\\text{ सेमी}, PF = 8\\text{ सेमी}$ और $RF = 9\\text{ सेमी}$ है। क्या $EF \\parallel QR$ है?",
        "સ્વાધ્યાય 6.2 (Q2.ii): $\\triangle PQR$ માં, $PE = 4\\text{ સેમી}, QE = 4.5\\text{ સેમી}, PF = 8\\text{ સેમી}$ અને $RF = 9\\text{ સેમી}$ છે. શું $EF \\parallel QR$ છે?",
        [
            "Yes, because PE/QE = PF/RF = 8/9",
            "No, because PE/QE ≠ PF/RF",
            "No, because the sides have decimal values",
            "Cannot be determined"
        ],
        [
            "हाँ, क्योंकि PE/QE = PF/RF = 8/9",
            "नहीं, क्योंकि PE/QE ≠ PF/RF",
            "नहीं, क्योंकि भुजाएँ दशमलव में हैं",
            "निर्धारित नहीं किया जा सकता"
        ],
        [
            "હા, કારણ કે PE/QE = PF/RF = 8/9",
            "ના, કારણ કે PE/QE ≠ PF/RF",
            "ના, કારણ કે બાજુઓ દશાંશમાં છે",
            "નક્કી કરી શકાય નહીં"
        ],
        0,
        "Calculate ratios: PE / QE = 4 / 4.5 = 40 / 45 = 8 / 9. PF / RF = 8 / 9. Since PE / QE = PF / RF, by Theorem 6.2 (Converse of BPT), EF is parallel to QR.",
        "अनुपातों की गणना करें: PE / QE = 4 / 4.5 = 40 / 45 = 8 / 9। PF / RF = 8 / 9। चूँकि PE / QE = PF / RF है, अतः प्रमेय 6.2 (BPT के विलोम) द्वारा EF, QR के समांतर है।",
        "ગુણોત્તરની ગણતરી કરો: PE / QE = 4 / 4.5 = 40 / 45 = 8 / 9. PF / RF = 8 / 9. PE / QE = PF / RF હોવાથી, પ્રમેય 6.2 (BPT ના પ્રતીપ) મુજબ EF એ QR ને સમાંતર છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q2_part3",
        "Exercise 6.2 (Q2.iii): In $\\triangle PQR$, $PQ = 1.28\\text{ cm}, PR = 2.56\\text{ cm}, PE = 0.18\\text{ cm}$, and $PF = 0.36\\text{ cm}$. Is $EF \\parallel QR$?",
        "प्रश्नावली 6.2 (Q2.iii): $\\triangle PQR$ में, $PQ = 1.28\\text{ सेमी}, PR = 2.56\\text{ सेमी}, PE = 0.18\\text{ सेमी}$ और $PF = 0.36\\text{ सेमी}$ है। क्या $EF \\parallel QR$ है?",
        "સ્વાધ્યાય 6.2 (Q2.iii): $\\triangle PQR$ માં, $PQ = 1.28\\text{ સેમી}, PR = 2.56\\text{ સેમી}, PE = 0.18\\text{ સેમી}$ અને $PF = 0.36\\text{ સેમી}$ છે. શું $EF \\parallel QR$ છે?",
        [
            "Yes, because PE/PQ = PF/PR = 9/64",
            "No, because PE/PQ ≠ PF/PR",
            "No, because PQ > PR",
            "Cannot be determined"
        ],
        [
            "हाँ, क्योंकि PE/PQ = PF/PR = 9/64",
            "नहीं, क्योंकि PE/PQ ≠ PF/PR",
            "नहीं, क्योंकि PQ > PR",
            "निर्धारित नहीं किया जा सकता"
        ],
        [
            "હા, કારણ કે PE/PQ = PF/PR = 9/64",
            "ના, કારણ કે PE/PQ ≠ PF/PR",
            "ના, કારણ કે PQ > PR",
            "નક્કી કરી શકાય નહીં"
        ],
        0,
        "Calculate part/whole ratios: PE / PQ = 0.18 / 1.28 = 18 / 128 = 9 / 64. PF / PR = 0.36 / 2.56 = 36 / 256 = 9 / 64. Since PE / PQ = PF / PR, by Converse of BPT, EF is parallel to QR.",
        "अनुपातों की गणना करें: PE / PQ = 0.18 / 1.28 = 18 / 128 = 9 / 64। PF / PR = 0.36 / 2.56 = 36 / 256 = 9 / 64। चूँकि PE / PQ = PF / PR है, अतः BPT के विलोम द्वारा EF, QR के समांतर है।",
        "ગુણોત્તરની ગણતરી કરો: PE / PQ = 0.18 / 1.28 = 18 / 128 = 9 / 64. PF / PR = 0.36 / 2.56 = 36 / 256 = 9 / 64. PE / PQ = PF / PR હોવાથી, BPT ના પ્રતીપ મુજબ EF એ QR ને સમાંતર છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.2 Q3
    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q3",
        "Exercise 6.2 (Q3): In quadrilateral ABCD, $LM \\parallel CB$ (with $M$ on $AB, L$ on $AC$) and $LN \\parallel CD$ (with $N$ on $AD$). What common ratio proves that $\\frac{AM}{AB} = \\frac{AN}{AD}$?",
        "प्रश्नावली 6.2 (Q3): चतुर्भुज ABCD में, $LM \\parallel CB$ ($M, AB$ पर है और $L, AC$ पर है) तथा $LN \\parallel CD$ ($N, AD$ पर है)। कौन सा उभयनिष्ठ अनुपात यह सिद्ध करता है कि $\\frac{AM}{AB} = \\frac{AN}{AD}$?",
        "સ્વાધ્યાય 6.2 (Q3): ચતુષ્કોણ ABCD માં, $LM \\parallel CB$ ($M$ એ $AB$ પર અને $L$ એ $AC$ પર છે) તથા $LN \\parallel CD$ ($N$ એ $AD$ પર છે). કયો સામાન્ય ગુણોત્તર સાબિત કરે છે કે $\\frac{AM}{AB} = \\frac{AN}{AD}$?",
        [
            "Both equal AL / AC by BPT in △ABC and △ADC",
            "Both equal BC / CD",
            "Both equal AC / BD",
            "Both equal 1"
        ],
        [
            "दोनों △ABC और △ADC में BPT द्वारा AL / AC के बराबर हैं",
            "दोनों BC / CD के बराबर हैं",
            "दोनों AC / BD के बराबर हैं",
            "दोनों 1 के बराबर हैं"
        ],
        [
            "બંને △ABC અને △ADC માં BPT મુજબ AL / AC ને સમાન છે",
            "બંને BC / CD ને સમાન છે",
            "બંને AC / BD ને સમાન છે",
            "બંને 1 ને સમાન છે"
        ],
        0,
        "In △ABC, LM ∥ CB => AM / AB = AL / AC (by BPT corollary). In △ADC, LN ∥ CD => AN / AD = AL / AC. Comparing both gives AM / AB = AN / AD.",
        "△ABC में, LM ∥ CB => AM / AB = AL / AC (BPT के उपप्रमेय द्वारा)। △ADC में, LN ∥ CD => AN / AD = AL / AC। दोनों की तुलना करने पर AM / AB = AN / AD सिद्ध होता है।",
        "△ABC માં, LM ∥ CB => AM / AB = AL / AC (BPT ના પરિણામ મુજબ). △ADC માં, LN ∥ CD => AN / AD = AL / AC. બંનેની સરખામણી કરતા AM / AB = AN / AD સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.2 Q4
    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q4",
        "Exercise 6.2 (Q4): In $\\triangle ABC$, $DE \\parallel AC$ and $DF \\parallel AE$. To prove $\\frac{BF}{FE} = \\frac{BE}{EC}$, which common ratio links both triangles $\\triangle ABE$ and $\\triangle ABC$?",
        "प्रश्नावली 6.2 (Q4): $\\triangle ABC$ में, $DE \\parallel AC$ और $DF \\parallel AE$ है। $\\frac{BF}{FE} = \\frac{BE}{EC}$ सिद्ध करने के लिए कौन सा उभयनिष्ठ अनुपात $\\triangle ABE$ और $\\triangle ABC$ दोनों को जोड़ता है?",
        "સ્વાધ્યાય 6.2 (Q4): $\\triangle ABC$ માં, $DE \\parallel AC$ અને $DF \\parallel AE$ છે. $\\frac{BF}{FE} = \\frac{BE}{EC}$ સાબિત કરવા માટે કયો સામાન્ય ગુણોત્તર $\\triangle ABE$ અને $\\triangle ABC$ બંનેને જોડે છે?",
        [
            "The ratio BD / DA on side AB",
            "The ratio BC / AC",
            "The ratio DE / DF",
            "The ratio BE / BF"
        ],
        [
            "भुजा AB पर अनुपात BD / DA",
            "अनुपात BC / AC",
            "अनुपात DE / DF",
            "अनुपात BE / BF"
        ],
        [
            "બાજુ AB પર ગુણોત્તર BD / DA",
            "ગુણોત્તર BC / AC",
            "ગુણોત્તર DE / DF",
            "ગુણોત્તર BE / BF"
        ],
        0,
        "In △BCA, DE ∥ AC => BD / DA = BE / EC ... (1). In △BEA, DF ∥ AE => BD / DA = BF / FE ... (2). From (1) and (2), BF / FE = BE / EC.",
        "△BCA में, DE ∥ AC => BD / DA = BE / EC ... (1)। △BEA में, DF ∥ AE => BD / DA = BF / FE ... (2)। (1) और (2) से, BF / FE = BE / EC सिद्ध होता है।",
        "△BCA માં, DE ∥ AC => BD / DA = BE / EC ... (1). △BEA માં, DF ∥ AE => BD / DA = BF / FE ... (2). (1) અને (2) પરથી, BF / FE = BE / EC સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.2 Q5
    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q5",
        "Exercise 6.2 (Q5): In figure, $DE \\parallel OQ$ and $DF \\parallel OR$. Show that $EF \\parallel QR$. From BPT in $\\triangle POQ$ and $\\triangle POR$, what common ratio equates $PE / EQ$ to $PF / FR$?",
        "प्रश्नावली 6.2 (Q5): आकृति में, $DE \\parallel OQ$ और $DF \\parallel OR$ है। दर्शाइए कि $EF \\parallel QR$ है। $\\triangle POQ$ और $\\triangle POR$ में BPT से कौन सा उभयनिष्ठ अनुपात $PE / EQ$ को $PF / FR$ के बराबर करता है?",
        "સ્વાધ્યાય 6.2 (Q5): આકૃતિમાં, $DE \\parallel OQ$ અને $DF \\parallel OR$ છે. દર્શાવો કે $EF \\parallel QR$ છે. $\\triangle POQ$ અને $\\triangle POR$ માં BPT પરથી કયો સામાન્ય ગુણોત્તર $PE / EQ$ અને $PF / FR$ ને સમાન બનાવે છે?",
        [
            "The ratio PD / DO on line segment PO",
            "The ratio PE / PF",
            "The ratio OQ / OR",
            "The ratio DE / DF"
        ],
        [
            "रेखाखंड PO पर अनुपात PD / DO",
            "अनुपात PE / PF",
            "अनुपात OQ / OR",
            "अनुपात DE / DF"
        ],
        [
            "રેખાખંડ PO પર ગુણોત્તર PD / DO",
            "ગુણોત્તર PE / PF",
            "ગુણોત્તર OQ / OR",
            "ગુણોત્તર DE / DF"
        ],
        0,
        "In △POQ, DE ∥ OQ => PE / EQ = PD / DO. In △POR, DF ∥ OR => PF / FR = PD / DO. Therefore PE / EQ = PF / FR. In △PQR, by Converse of BPT, EF ∥ QR.",
        "△POQ में, DE ∥ OQ => PE / EQ = PD / DO। △POR में, DF ∥ OR => PF / FR = PD / DO। अतः PE / EQ = PF / FR। △PQR में BPT के विलोम द्वारा EF ∥ QR सिद्ध होता है।",
        "△POQ માં, DE ∥ OQ => PE / EQ = PD / DO. △POR માં, DF ∥ OR => PF / FR = PD / DO. તેથી PE / EQ = PF / FR. △PQR માં BPT ના પ્રતીપ મુજબ EF ∥ QR સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.2 Q6
    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q6",
        "Exercise 6.2 (Q6): Points $A, B, C$ are on $OP, OQ, OR$ such that $AB \\parallel PQ$ and $AC \\parallel PR$. Show that $BC \\parallel QR$. What theorem directly concludes that $BC \\parallel QR$ from $\\frac{OB}{BQ} = \\frac{OC}{CR}$ in $\\triangle OQR$?",
        "प्रश्नावली 6.2 (Q6): $OP, OQ, OR$ पर क्रमशः बिंदु $A, B, C$ इस प्रकार स्थित हैं कि $AB \\parallel PQ$ और $AC \\parallel PR$ है। दर्शाइए कि $BC \\parallel QR$ है। $\\triangle OQR$ में $\\frac{OB}{BQ} = \\frac{OC}{CR}$ से $BC \\parallel QR$ किस प्रमेय द्वारा निष्कर्ष निकलता है?",
        "સ્વાધ્યાય 6.2 (Q6): $OP, OQ, OR$ પર અનુક્રમે બિંદુઓ $A, B, C$ એવી રીતે આવેલા છે કે જેથી $AB \\parallel PQ$ અને $AC \\parallel PR$ થાય. દર્શાવો કે $BC \\parallel QR$ છે. $\\triangle OQR$ માં $\\frac{OB}{BQ} = \\frac{OC}{CR}$ પરથી $BC \\parallel QR$ કયા પ્રમેય મુજબ સાબિત થાય છે?",
        [
            "Converse of Basic Proportionality Theorem (Theorem 6.2)",
            "Pythagoras Theorem",
            "Midpoint Theorem",
            "AAA Similarity Criterion"
        ],
        [
            "आधारभूत आनुपातिकता प्रमेय का विलोम (प्रमेय 6.2)",
            "पाइथागोरस प्रमेय",
            "मध्य-बिंदु प्रमेय",
            "AAA समरूपता कसौटी"
        ],
        [
            "સમપ્રમાણતાના મૂળભૂત પ્રમેયનું પ્રતીપ (પ્રમેય 6.2)",
            "પાયથાગોરસ પ્રમેય",
            "મધ્યબિંદુ પ્રમેય",
            "ખૂ-ખૂ-ખૂ સમરૂપતા શરત"
        ],
        0,
        "In △OPQ, AB ∥ PQ => OA / AP = OB / BQ. In △OPR, AC ∥ PR => OA / AP = OC / CR. Thus OB / BQ = OC / CR. In △OQR, by Theorem 6.2 (Converse of BPT), BC ∥ QR.",
        "△OPQ में, AB ∥ PQ => OA / AP = OB / BQ। △OPR में, AC ∥ PR => OA / AP = OC / CR। अतः OB / BQ = OC / CR। △OQR में BPT के विलोम (प्रमेय 6.2) द्वारा BC ∥ QR सिद्ध होता है।",
        "△OPQ માં, AB ∥ PQ => OA / AP = OB / BQ. △OPR માં, AC ∥ PR => OA / AP = OC / CR. તેથી OB / BQ = OC / CR. △OQR માં BPT ના પ્રતીપ (પ્રમેય 6.2) મુજબ BC ∥ QR સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.2 Q7
    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q7",
        "Exercise 6.2 (Q7): Using Theorem 6.1 (BPT), prove that a line drawn through the midpoint $D$ of side $AB$ of $\\triangle ABC$ parallel to $BC$ bisects side $AC$ at $E$. What is the ratio $AD / DB$?",
        "प्रश्नावली 6.2 (Q7): प्रमेय 6.1 (BPT) का प्रयोग करते हुए सिद्ध कीजिए कि $\\triangle ABC$ की एक भुजा $AB$ के मध्य-बिंदु $D$ से होकर $BC$ के समांतर खींची गई रेखा $AC$ को $E$ पर समद्विभाजित करती है। अनुपात $AD / DB$ का मान क्या है?",
        "સ્વાધ્યાય 6.2 (Q7): પ્રમેય 6.1 (BPT) નો ઉપયોગ કરીને સાબિત કરો કે $\\triangle ABC$ ની બાજુ $AB$ ના મધ્યબિંદુ $D$ માંથી $BC$ ને સમાંતર દોરેલી રેખા $AC$ ને $E$ માં દુભાગે છે. ગુણોત્તર $AD / DB$ નું મૂલ્ય શું છે?",
        [
            "1, because AD = DB (D is midpoint), so AE / EC = 1 => AE = EC",
            "2",
            "1/2",
            "0"
        ],
        [
            "1, क्योंकि AD = DB (D मध्य-बिंदु है), अतः AE / EC = 1 => AE = EC",
            "2",
            "1/2",
            "0"
        ],
        [
            "1, કારણ કે AD = DB ($D$ મધ્યબિંદુ છે), તેથી AE / EC = 1 => AE = EC",
            "2",
            "1/2",
            "0"
        ],
        0,
        "Since D is midpoint of AB, AD = DB => AD / DB = 1. Since DE ∥ BC, by BPT: AD / DB = AE / EC => 1 = AE / EC => AE = EC. Hence E bisects AC.",
        "चूँकि D, AB का मध्य-बिंदु है, AD = DB => AD / DB = 1। चूँकि DE ∥ BC है, BPT द्वारा: AD / DB = AE / EC => 1 = AE / EC => AE = EC। अतः E, AC का मध्य-बिंदु है।",
        "$D$ એ $AB$ નું મધ્યબિંદુ હોવાથી, AD = DB => AD / DB = 1. DE ∥ BC હોવાથી BPT મુજબ: AD / DB = AE / EC => 1 = AE / EC => AE = EC. આમ $E$ એ $AC$ નું મધ્યબિંદુ છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # Exercise 6.2 Q8
    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q8",
        "Exercise 6.2 (Q8): Using Theorem 6.2 (Converse of BPT), prove that the line joining the midpoints $D$ of side $AB$ and $E$ of side $AC$ in $\\triangle ABC$ is parallel to $BC$. Why are the ratios $AD/DB$ and $AE/EC$ equal?",
        "प्रश्नावली 6.2 (Q8): प्रमेय 6.2 (BPT के विलोम) का प्रयोग करते हुए सिद्ध कीजिए कि $\\triangle ABC$ में भुजा $AB$ के मध्य-बिंदु $D$ और $AC$ के मध्य-बिंदु $E$ को मिलाने वाली रेखा $BC$ के समांतर होती है। अनुपात $AD/DB$ और $AE/EC$ बराबर क्यों हैं?",
        "સ્વાધ્યાય 6.2 (Q8): પ્રમેય 6.2 (BPT ના પ્રતીપ) નો ઉપયોગ કરીને સાબિત કરો કે $\\triangle ABC$ માં બાજુ $AB$ ના મધ્યબિંદુ $D$ અને $AC$ ના મધ્યબિંદુ $E$ ને જોડતી રેખા $BC$ ને સમાંતર છે. ગુણોત્તર $AD/DB$ અને $AE/EC$ શા માટે સમાન છે?",
        [
            "Both equal 1 (since AD = DB and AE = EC)",
            "Both equal 2",
            "Both equal 1/2",
            "Because AB = AC"
        ],
        [
            "दोनों 1 के बराबर हैं (चूँकि AD = DB और AE = EC)",
            "दोनों 2 के बराबर हैं",
            "दोनों 1/2 के बराबर हैं",
            "क्योंकि AB = AC है"
        ],
        [
            "બંને 1 ને સમાન છે (કારણ કે AD = DB અને AE = EC)",
            "બંને 2 ને સમાન છે",
            "બંને 1/2 ને સમાન છે",
            "કારણ કે AB = AC છે"
        ],
        0,
        "D is midpoint of AB => AD = DB => AD / DB = 1. E is midpoint of AC => AE = EC => AE / EC = 1. Thus AD / DB = AE / EC = 1. By Theorem 6.2 (Converse of BPT), DE ∥ BC.",
        "D, AB का मध्य-बिंदु है => AD = DB => AD / DB = 1। E, AC का मध्य-बिंदु है => AE = EC => AE / EC = 1। अतः AD / DB = AE / EC = 1। BPT के विलोम (प्रमेय 6.2) द्वारा DE ∥ BC सिद्ध होता है।",
        "$D$ એ $AB$ નું મધ્યબિંદુ છે => AD = DB => AD / DB = 1. $E$ એ $AC$ નું મધ્યબિંદુ છે => AE = EC => AE / EC = 1. આથી AD / DB = AE / EC = 1. BPT ના પ્રતીપ (પ્રમેય 6.2) મુજબ DE ∥ BC સાબિત થાય છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # Exercise 6.2 Q9
    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q9",
        "Exercise 6.2 (Q9): $ABCD$ is a trapezium in which $AB \\parallel DC$ and its diagonals intersect each other at the point $O$. Which of the following equations correctly represents the relationship between the diagonal segments?",
        "प्रश्नावली 6.2 (Q9): $ABCD$ एक समलंब है जिसमें $AB \\parallel DC$ है तथा इसके विकर्ण परस्पर बिंदु $O$ पर प्रतिच्छेद करते हैं। निम्नलिखित में से कौन सा समीकरण विकर्ण खंडों के संबंध को सही रूप से दर्शाता है?",
        "સ્વાધ્યાય 6.2 (Q9): $ABCD$ એક સમલંબ ચતુષ્કોણ છે જેમાં $AB \\parallel DC$ છે અને તેના વિકર્ણો પરસ્પર બિંદુ $O$ માં છેદે છે. નીચેનામાંથી કયું સમીકરણ વિકર્ણના રેખાખંડો વચ્ચેનો સાચો સંબંધ દર્શાવે છે?",
        [
            "AO / BO = CO / DO (or AO / CO = BO / DO)",
            "AO = BO and CO = DO",
            "AO · BO = CO · DO",
            "AO + BO = CO + DO"
        ],
        [
            "AO / BO = CO / DO (या AO / CO = BO / DO)",
            "AO = BO और CO = DO",
            "AO · BO = CO · DO",
            "AO + BO = CO + DO"
        ],
        [
            "AO / BO = CO / DO (અથવા AO / CO = BO / DO)",
            "AO = BO અને CO = DO",
            "AO · BO = CO · DO",
            "AO + BO = CO + DO"
        ],
        0,
        "Draw OE ∥ AB ∥ DC through O meeting AD at E. In △ADC, OE ∥ DC => AE / ED = AO / OC. In △ABD, OE ∥ AB => AE / ED = BO / OD. Equating both: AO / OC = BO / OD, which rearranges to AO / BO = CO / DO.",
        "O से होकर AD को E पर मिलती हुई एक रेखा OE ∥ AB ∥ DC खींचें। △ADC में, OE ∥ DC => AE / ED = AO / OC। △ABD में, OE ∥ AB => AE / ED = BO / OD। दोनों को बराबर करने पर: AO / OC = BO / OD, जिसे पुनर्व्यवस्थित करने पर AO / BO = CO / DO प्राप्त होता है।",
        "$O$ માંથી પસાર થતી અને $AD$ ને $E$ માં મળતી રેખા OE ∥ AB ∥ DC દોરો. △ADC માં, OE ∥ DC => AE / ED = AO / OC. △ABD માં, OE ∥ AB => AE / ED = BO / OD. બંને સરખાવતા: AO / OC = BO / OD, જેથી AO / BO = CO / DO સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=3
    ))

    # Exercise 6.2 Q10
    blocks.append(make_quiz(
        "C10M_CH6_EX6.2_Q10",
        "Exercise 6.2 (Q10): The diagonals of a quadrilateral $ABCD$ intersect each other at the point $O$ such that $\\frac{AO}{BO} = \\frac{CO}{DO}$. By drawing $OE \\parallel AB$ meeting $AD$ at $E$, what does Converse of BPT prove about lines $AB$ and $DC$?",
        "प्रश्नावली 6.2 (Q10): एक चतुर्भुज $ABCD$ के विकर्ण परस्पर बिंदु $O$ पर इस प्रकार प्रतिच्छेद करते हैं कि $\\frac{AO}{BO} = \\frac{CO}{DO}$ है। $O$ से $AD$ को $E$ पर मिलती हुई रेखा $OE \\parallel AB$ खींचने पर, BPT का विलोम $AB$ और $DC$ के विषय में क्या सिद्ध करता है?",
        "સ્વાધ્યાય 6.2 (Q10): એક ચતુષ્કોણ $ABCD$ ના વિકર્ણો પરસ્પર બિંદુ $O$ માં એવી રીતે છેદે છે કે જેથી $\\frac{AO}{BO} = \\frac{CO}{DO}$ થાય. $O$ માંથી $AD$ ને $E$ માં મળતી રેખા $OE \\parallel AB$ દોરતા, BPT નું પ્રતીપ $AB$ અને $DC$ વિશે શું સાબિત કરે છે?",
        [
            "OE ∥ DC, which implies AB ∥ DC, so ABCD is a trapezium",
            "ABCD is a rectangle",
            "ABCD is a square",
            "ABCD is a rhombus"
        ],
        [
            "OE ∥ DC, जिसका अर्थ है AB ∥ DC, अतः ABCD एक समलंब है",
            "ABCD एक आयत है",
            "ABCD एक वर्ग है",
            "ABCD एक समचतुर्भुज है"
        ],
        [
            "OE ∥ DC, જે દર્શાવે છે કે AB ∥ DC, તેથી ABCD સમલંબ ચતુષ્કોણ છે",
            "ABCD લંબચોરસ છે",
            "ABCD ચોરસ છે",
            "ABCD સમબાજુ ચતુષ્કોણ છે"
        ],
        0,
        "Given AO / BO = CO / DO => AO / CO = BO / OD. Drawing OE ∥ AB in △DAB gives AE / ED = BO / OD. Thus AE / ED = AO / CO. In △ADC, by Converse of BPT, OE ∥ DC. Since OE ∥ AB and OE ∥ DC, we get AB ∥ DC. Therefore ABCD is a trapezium.",
        "दिया है AO / BO = CO / DO => AO / CO = BO / OD। △DAB में OE ∥ AB खींचने पर AE / ED = BO / OD मिलता है। अतः AE / ED = AO / CO। △ADC में BPT के विलोम द्वारा OE ∥ DC। चूँकि OE ∥ AB और OE ∥ DC है, अतः AB ∥ DC। इसलिए ABCD एक समलंब है।",
        "આપેલ છે AO / BO = CO / DO => AO / CO = BO / OD. △DAB માં OE ∥ AB દોરતા AE / ED = BO / OD મળે છે. તેથી AE / ED = AO / CO. △ADC માં BPT ના પ્રતીપ મુજબ OE ∥ DC. OE ∥ AB અને OE ∥ DC હોવાથી, AB ∥ DC મળે છે. આથી ABCD સમલંબ ચતુષ્કોણ છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=3
    ))

    return blocks

# =========================================================================
# PART 3: SIMILARITY CRITERIA & EXERCISE 6.3
# =========================================================================
def get_part3_blocks():
    blocks = []

    # 32. Hook: Minimal Information
    blocks.append(make_theory(
        "C10M_CH6_12",
        "The Minimal Information Secret in Triangles",
        "त्रिभुजों में न्यूनतम जानकारी का रहस्य",
        "ત્રિકોણમાં ન્યૂનતમ માહિતીનું રહસ્ય",
        "In Class 9, you learned that you do not need to measure all 6 parts (3 sides and 3 angles) to prove two triangles are congruent. Three well-chosen elements (SAS, ASA, SSS) are sufficient.\n\nFor **Similarity**, can we do even better?\nYES! Because the sum of angles in any triangle is fixed at 180°, if just **TWO angles** of one triangle match two angles of another triangle, the third angle MUST automatically match! This remarkable fact gives us the most powerful and frequently used tool in geometry: the **AA (Angle-Angle) Similarity Criterion**!",
        "कक्षा 9 में आपने सीखा था कि दो त्रिभुजों को सर्वांगसम सिद्ध करने के लिए सभी 6 भागों (3 भुजाओं और 3 कोणों) को मापने की आवश्यकता नहीं होती है। केवल 3 उपयुक्त भाग (SAS, ASA, SSS) ही पर्याप्त होते हैं।\n\nक्या **समरूपता (Similarity)** के लिए हम इससे भी कम जानकारी में काम कर सकते हैं?\nहाँ! चूँकि किसी भी त्रिभुज के कोणों का योग 180° निश्चित होता है, यदि एक त्रिभुज के केवल **दो कोण** दूसरे त्रिभुज के दो कोणों के बराबर हों, तो तीसरा कोण स्वतः ही बराबर होगा! यह तथ्य हमें ज्यामिति का सबसे शक्तिशाली और उपयोगी उपकरण प्रदान करता है: **AA (कोण-कोण) समरूपता कसौटी**!",
        "ધોરણ 9 માં તમે શીખ્યા હતા કે બે ત્રિકોણોને એકરૂપ સાબિત કરવા માટે બધા 6 અંગો (3 બાજુઓ અને 3 ખૂણાઓ) માપવાની જરૂર નથી. યોગ્ય રીતે પસંદ કરેલા માત્ર 3 અંગો (SAS, ASA, SSS) પૂરતા છે.\n\nશું **સમરૂપતા (Similarity)** માટે આપણે આનાથી પણ ઓછી માહિતીથી કામ ચલાવી શકીએ?\nહા! કારણ કે કોઈપણ ત્રિકોણના ખૂણાઓનો સરવાળો 180° નિશ્ચિત હોય છે, જો એક ત્રિકોણના માત્ર **બે ખૂણા** બીજા ત્રિકોણના બે ખૂણા સાથે મેળ ખાતા હોય, તો ત્રીજો ખૂણો આપમેળે જ સમાન બનશે! આ અદ્ભુત હકીકત આપણને ભૂમિતિનું સૌથી શક્તિશાળી સાધન આપે છે: **AA (ખૂ-ખૂ) સમરૂપતાની શરત**!",
        btype="hook",
        bloom="Understand",
        diff="Beginner",
        mins=2
    ))

    # 33. Socratic Question
    blocks.append(make_quiz(
        "C10M_CH6_13",
        "In $\\triangle ABC$, $\\angle A = 55^\\circ$ and $\\angle B = 65^\\circ$. In $\\triangle DEF$, $\\angle D = 55^\\circ$ and $\\angle F = 60^\\circ$. Are the two triangles similar?",
        "$\\triangle ABC$ में, $\\angle A = 55^\\circ$ और $\\angle B = 65^\\circ$ है। $\\triangle DEF$ में, $\\angle D = 55^\\circ$ और $\\angle F = 60^\\circ$ है। क्या दोनों त्रिभुज समरूप हैं?",
        "$\\triangle ABC$ માં, $\\angle A = 55^\\circ$ અને $\\angle B = 65^\\circ$ છે. $\\triangle DEF$ માં, $\\angle D = 55^\\circ$ અને $\\angle F = 60^\\circ$ છે. શું બંને ત્રિકોણ સમરૂપ છે?",
        [
            "Yes, because ∠C = 180° - (55°+65°) = 60°, so all three angles match",
            "No, because angle B does not equal angle F",
            "No, because we do not know the side lengths",
            "Cannot be determined without a diagram"
        ],
        [
            "हाँ, क्योंकि ∠C = 180° - (55°+65°) = 60°, अतः तीनों कोण समान हैं",
            "नहीं, क्योंकि कोण B, कोण F के बराबर नहीं है",
            "नहीं, क्योंकि हमें भुजाओं की लंबाई ज्ञात नहीं है",
            "आकृति के बिना निर्धारित नहीं किया जा सकता"
        ],
        [
            "હા, કારણ કે ∠C = 180° - (55°+65°) = 60°, તેથી ત્રણેય ખૂણા સમાન છે",
            "ના, કારણ કે ખૂણો B એ ખૂણા F ને સમાન નથી",
            "ના, કારણ કે આપણને બાજુઓની લંબાઈ ખબર નથી",
            "આકૃતિ વગર નક્કી કરી શકાય નહીં"
        ],
        0,
        "In △ABC: ∠C = 180° - (55° + 65°) = 60°. In △DEF: ∠E = 180° - (55° + 60°) = 65°. Thus ∠A = ∠D = 55°, ∠B = ∠E = 65°, and ∠C = ∠F = 60°. By AAA / AA similarity, △ABC ~ △DEF.",
        "△ABC में: ∠C = 180° - (55° + 65°) = 60°। △DEF में: ∠E = 180° - (55° + 60°) = 65°। अतः ∠A = ∠D = 55°, ∠B = ∠E = 65° और ∠C = ∠F = 60°। AAA / AA समरूपता द्वारा △ABC ~ △DEF समरूप हैं।",
        "△ABC માં: ∠C = 180° - (55° + 65°) = 60°. △DEF માં: ∠E = 180° - (55° + 60°) = 65°. આમ ∠A = ∠D = 55°, ∠B = ∠E = 65° અને ∠C = ∠F = 60°. AAA / AA સમરૂપતા મુજબ △ABC ~ △DEF સમરૂપ છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # 34. Discovery: Vertex Correspondence
    blocks.append(make_theory(
        "C10M_CH6_14",
        "Discovery: Vertex Correspondence & Symbolic Notation",
        "खोज: शीर्षों की संगति और प्रतीकात्मक संकेतन",
        "શોધ: શિરોબિંદુઓની સંગતતા અને પ્રતીકાત્મક સંકેત",
        "When writing that two triangles are similar, the order of letters indicates the exact correspondence between vertices:\n$$\\triangle ABC \\sim \\triangle PQR$$\n\nThis single line conveys 6 facts:\n1. **Angles:** $\\angle A = \\angle P, \\quad \\angle B = \\angle Q, \\quad \\angle C = \\angle R$\n2. **Sides:** $\\frac{AB}{PQ} = \\frac{BC}{QR} = \\frac{AC}{PR}$\n\n**Warning:** If $\\angle A = \\angle Q$ and $\\angle B = \\angle P$, writing $\\triangle ABC \\sim \\triangle PQR$ is mathematically INCORRECT! You must write $\\mathbf{\\triangle ABC \\sim \\triangle QPR}$. Always match corresponding vertices!",
        "जब हम लिखते हैं कि दो त्रिभुज समरूप हैं, तो अक्षरों का क्रम शीर्षों के बीच सटीक संगति को दर्शाता है:\n$$\\triangle ABC \\sim \\triangle PQR$$\n\nयह एक पंक्ति 6 तथ्यों को व्यक्त करती है:\n1. **कोण:** $\\angle A = \\angle P, \\quad \\angle B = \\angle Q, \\quad \\angle C = \\angle R$\n2. **भुजाएँ:** $\\frac{AB}{PQ} = \\frac{BC}{QR} = \\frac{AC}{PR}$\n\n**चेतावनी:** यदि $\\angle A = \\angle Q$ और $\\angle B = \\angle P$ हो, तो $\\triangle ABC \\sim \\triangle PQR$ लिखना गणितीय रूप से गलत है! आपको $\\mathbf{\\triangle ABC \\sim \\triangle QPR}$ लिखना होगा। हमेशा संगत शीर्षों का मिलान करें!",
        "જ્યારે આપણે લખીએ છીએ કે બે ત્રિકોણો સમરૂપ છે, ત્યારે અક્ષરોનો ક્રમ શિરોબિંદુઓ વચ્ચેની ચોક્કસ સંગતતા દર્શાવે છે:\n$$\\triangle ABC \\sim \\triangle PQR$$\n\nઆ એક જ વાક્ય 6 હકીકતો દર્શાવે છે:\n1. **ખૂણાઓ:** $\\angle A = \\angle P, \\quad \\angle B = \\angle Q, \\quad \\angle C = \\angle R$\n2. **બાજુઓ:** $\\frac{AB}{PQ} = \\frac{BC}{QR} = \\frac{AC}{PR}$\n\n**ચેતવણી:** જો $\\angle A = \\angle Q$ અને $\\angle B = \\angle P$ હોય, તો $\\triangle ABC \\sim \\triangle PQR$ લખવું ગાણિતિક રીતે ખોટું છે! તમારે $\\mathbf{\\triangle ABC \\sim \\triangle QPR}$ લખવું પડે. હંમેશા અનુરૂપ શિરોબિંદુઓ મેળવો!",
        btype="discovery",
        bloom="Understand",
        diff="Beginner",
        mins=2
    ))

    # 35. Theory: 3 Criteria (AAA, SSS, SAS)
    blocks.append(make_theory(
        "C10M_CH6_15",
        "The Three Master Criteria for Similarity of Triangles",
        "त्रिभुजों की समरूपता की तीन मुख्य कसौटियाँ",
        "ત્રિકોણની સમરૂપતાની ત્રણ મુખ્ય શરતો",
        "### 1. AAA Similarity Criterion (Theorem 6.3) & AA Corollary:\nIf in two triangles, corresponding angles are equal, then their corresponding sides are in the same ratio and hence the two triangles are similar.\n- **AA Corollary:** If two angles of one triangle are respectively equal to two angles of another triangle, the triangles are similar.\n\n### 2. SSS Similarity Criterion (Theorem 6.4):\nIf in two triangles, sides of one triangle are proportional to the sides of the other triangle, then their corresponding angles are equal and hence the triangles are similar.\n\n### 3. SAS Similarity Criterion (Theorem 6.5):\nIf one angle of a triangle is equal to one angle of another triangle and the sides including these angles are proportional, then the two triangles are similar.",
        "### 1. AAA (कोण-कोण-कोण) समरूपता कसौटी (प्रमेय 6.3) एवं AA उपप्रमेय:\nयदि दो त्रिभुजों में संगत कोण बराबर हों, तो उनकी संगत भुजाएँ एक ही अनुपात में होती हैं और इसलिए दोनों त्रिभुज समरूप होते हैं।\n- **AA उपप्रमेय:** यदि एक त्रिभुज के दो कोण किसी अन्य त्रिभुज के दो कोणों के क्रमशः बराबर हों, तो दोनों त्रिभुज समरूप होते हैं।\n\n### 2. SSS (भुजा-भुजा-भुजा) समरूपता कसौटी (प्रमेय 6.4):\nयदि दो त्रिभुजों में एक त्रिभुज की भुजाएँ दूसरे त्रिभुज की भुजाओं के समानुपाती हों, तो उनके संगत कोण बराबर होते हैं और इसलिए दोनों त्रिभुज समरूप होते हैं।\n\n### 3. SAS (भुजा-कोण-भुजा) समरूपता कसौटी (प्रमेय 6.5):\nयदि एक त्रिभुज का एक कोण दूसरे त्रिभुज के एक कोण के बराबर हो तथा इन कोणों को अंतर्गत करने वाली भुजाएँ समानुपाती हों, तो दोनों त्रिभुज समरूप होते हैं।",
        "### 1. AAA (ખૂ-ખૂ-ખૂ) સમરૂપતાની શરત (પ્રમેય 6.3) અને AA પરિણામ:\nજો બે ત્રિકોણોમાં અનુરૂપ ખૂણાઓ સમાન હોય, તો તેમની અનુરૂપ બાજુઓ એક જ ગુણોત્તરમાં હોય અને તેથી તે બે ત્રિકોણો સમરૂપ થાય.\n- **AA શરત:** જો એક ત્રિકોણના બે ખૂણાઓ બીજા ત્રિકોણના બે ખૂણાઓને અનુરૂપ સમાન હોય, તો તે બે ત્રિકોણો સમરૂપ થાય.\n\n### 2. SSS (બા-બા-બા) સમરૂપતાની શરત (પ્રમેય 6.4):\nજો બે ત્રિકોણોમાં એક ત્રિકોણની બાજુઓ બીજા ત્રિકોણની બાજુઓના સમપ્રમાણમાં હોય, તો તેમના અનુરૂપ ખૂણાઓ સમાન હોય અને તેથી બંને ત્રિકોણો સમરૂપ થાય.\n\n### 3. SAS (બા-ખૂ-બા) સમરૂપતાની શરત (પ્રમેય 6.5):\nજો કોઈ ત્રિકોણનો એક ખૂણો બીજા ત્રિકોણના એક ખૂણાને સમાન હોય અને આ ખૂણાઓને સમાવતી બાજુઓ સમપ્રમાણમાં હોય, તો તે બે ત્રિકોણો સમરૂપ થાય.",
        btype="theory",
        bloom="Remember",
        diff="Beginner",
        mins=3
    ))

    # 36. Teacher Tip: The Included Angle Trap
    blocks.append(make_theory(
        "C10M_CH6_16",
        "Teacher Tip: The 'Included Angle' Trap in SAS",
        "शिक्षक युक्ति: SAS में 'अंतर्गत कोण' की सावधानी",
        "શિક્ષકની સલાહ: બા-ખૂ-બા માં 'અંતર્ગત ખૂણા' ની સાવચેતી",
        "In **SAS Similarity**, the equal angle MUST be the **included angle** (the angle directly formed between the two proportional sides)!\n\nFor example:\nIf $\\frac{AB}{DE} = \\frac{BC}{EF}$, the required angle must be $\\angle B = \\angle E$.\nIf instead you are given $\\angle A = \\angle D$, the triangles are **NOT necessarily similar**! Never assume SAS unless the angle sits precisely between the two proportional sides.",
        "**SAS (भुजा-कोण-भुजा) समरूपता** में, बराबर कोण अनिवार्य रूप से **अंतर्गत कोण (Included Angle)** ही होना चाहिए (जो दोनों समानुपाती भुजाओं के बीच बनता है)!\n\nउदाहरण के लिए:\nयदि $\\frac{AB}{DE} = \\frac{BC}{EF}$ हो, तो आवश्यक कोण $\\angle B = \\angle E$ होना चाहिए।\nयदि इसके स्थान पर आपको $\\angle A = \\angle D$ दिया जाए, तो त्रिभुज **समरूप होना आवश्यक नहीं है**! जब तक कोण दोनों समानुपाती भुजाओं के ठीक बीच में न हो, तब तक SAS कसौटी लागू न करें।",
        "**SAS (બા-ખૂ-બા) સમરૂપતા** માં, સમાન ખૂણો ફરજિયાતપણે **અંતર્ગત ખૂણો (Included Angle)** જ હોવો જોઈએ (જે બે સમપ્રમાણ બાજુઓની વચ્ચે બને છે)!\n\nઉદાહરણ તરીકે:\nજો $\\frac{AB}{DE} = \\frac{BC}{EF}$ હોય, તો જરૂરી ખૂણો $\\angle B = \\angle E$ જ હોવો જોઈએ.\nજો તેના બદલે તમને $\\angle A = \\angle D$ આપવામાં આવે, તો ત્રિકોણો **સમરૂપ હોવા જરૂરી નથી**! જ્યાં સુધી ખૂણો બે સમપ્રમાણ બાજુઓની બરાબર વચ્ચે ન હોય, ત્યાં સુધી બા-ખૂ-બા શરત લાગુ કરશો નહીં.",
        btype="teacher_tip",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.3 Q1 (i to vi)
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q1_part1",
        "Exercise 6.3 (Q1.i): In $\\triangle ABC$, $\\angle A = 60^\\circ, \\angle B = 80^\\circ, \\angle C = 40^\\circ$. In $\\triangle PQR$, $\\angle P = 60^\\circ, \\angle Q = 80^\\circ, \\angle R = 40^\\circ$. Are the triangles similar?",
        "प्रश्नावली 6.3 (Q1.i): $\\triangle ABC$ में, $\\angle A = 60^\\circ, \\angle B = 80^\\circ, \\angle C = 40^\\circ$ है। $\\triangle PQR$ में, $\\angle P = 60^\\circ, \\angle Q = 80^\\circ, \\angle R = 40^\\circ$ है। क्या ये त्रिभुज समरूप हैं?",
        "સ્વાધ્યાય 6.3 (Q1.i): $\\triangle ABC$ માં, $\\angle A = 60^\\circ, \\angle B = 80^\\circ, \\angle C = 40^\\circ$ છે. $\\triangle PQR$ માં, $\\angle P = 60^\\circ, \\angle Q = 80^\\circ, \\angle R = 40^\\circ$ છે. શું ત્રિકોણો સમરૂપ છે?",
        [
            "Yes, △ABC ~ △PQR by AAA similarity criterion",
            "No, because sides are not given",
            "Yes, △ABC ~ △QPR by SAS",
            "No, the triangles are congruent, not similar"
        ],
        [
            "हाँ, AAA समरूपता कसौटी द्वारा △ABC ~ △PQR",
            "नहीं, क्योंकि भुजाएँ नहीं दी गई हैं",
            "हाँ, SAS द्वारा △ABC ~ △QPR",
            "नहीं, त्रिभुज सर्वांगसम हैं, समरूप नहीं"
        ],
        [
            "હા, ખૂ-ખૂ-ખૂ સમરૂપતા શરત મુજબ △ABC ~ △PQR",
            "ના, કારણ કે બાજુઓ આપેલી નથી",
            "હા, બા-ખૂ-બા મુજબ △ABC ~ △QPR",
            "ના, ત્રિકોણો એકરૂપ છે, સમરૂપ નથી"
        ],
        0,
        "Corresponding angles are equal: ∠A = ∠P = 60°, ∠B = ∠Q = 80°, ∠C = ∠R = 40°. By AAA criterion, △ABC ~ △PQR.",
        "संगत कोण बराबर हैं: ∠A = ∠P = 60°, ∠B = ∠Q = 80°, ∠C = ∠R = 40°। AAA कसौटी द्वारा △ABC ~ △PQR समरूप हैं।",
        "અનુરૂપ ખૂણાઓ સમાન છે: ∠A = ∠P = 60°, ∠B = ∠Q = 80°, ∠C = ∠R = 40°. ખૂ-ખૂ-ખૂ શરત મુજબ △ABC ~ △PQR સમરૂપ છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q1_part2",
        "Exercise 6.3 (Q1.ii): In $\\triangle ABC$, $AB = 2, BC = 2.5, CA = 3$. In $\\triangle PQR$, $PQ = 6, QR = 4, PR = 5$. Are the triangles similar?",
        "प्रश्नावली 6.3 (Q1.ii): $\\triangle ABC$ में, $AB = 2, BC = 2.5, CA = 3$ है। $\\triangle PQR$ में, $PQ = 6, QR = 4, PR = 5$ है। क्या ये त्रिभुज समरूप हैं?",
        "સ્વાધ્યાય 6.3 (Q1.ii): $\\triangle ABC$ માં, $AB = 2, BC = 2.5, CA = 3$ છે. $\\triangle PQR$ માં, $PQ = 6, QR = 4, PR = 5$ છે. શું ત્રિકોણો સમરૂપ છે?",
        [
            "Yes, △ABC ~ △QRP by SSS similarity criterion (ratio = 1/2)",
            "No, because AB/PQ ≠ BC/QR",
            "Yes, △ABC ~ △PQR by SSS",
            "Cannot be determined without angle measures"
        ],
        [
            "हाँ, SSS समरूपता कसौटी द्वारा △ABC ~ △QRP (अनुपात = 1/2)",
            "नहीं, क्योंकि AB/PQ ≠ BC/QR",
            "हाँ, SSS द्वारा △ABC ~ △PQR",
            "कोणों के माप के बिना निर्धारित नहीं किया जा सकता"
        ],
        [
            "હા, બા-બા-બા સમરૂપતા શરત મુજબ △ABC ~ △QRP (ગુણોત્તર = 1/2)",
            "ના, કારણ કે AB/PQ ≠ BC/QR",
            "હા, બા-બા-બા મુજબ △ABC ~ △PQR",
            "ખૂણાઓના માપ વિના નક્કી કરી શકાય નહીં"
        ],
        0,
        "Check side ratios: AB / QR = 2 / 4 = 1/2. BC / PR = 2.5 / 5 = 1/2. CA / PQ = 3 / 6 = 1/2. Since all three pairs of corresponding sides are in the ratio 1/2, by SSS criterion, △ABC ~ △QRP.",
        "भुजाओं के अनुपात की जाँच करें: AB / QR = 2 / 4 = 1/2। BC / PR = 2.5 / 5 = 1/2। CA / PQ = 3 / 6 = 1/2। चूँकि संगत भुजाओं के तीनों युग्म 1/2 के अनुपात में हैं, अतः SSS कसौटी द्वारा △ABC ~ △QRP समरूप हैं।",
        "બાજુઓના ગુણોત્તર તપાસો: AB / QR = 2 / 4 = 1/2. BC / PR = 2.5 / 5 = 1/2. CA / PQ = 3 / 6 = 1/2. અનુરૂપ બાજુઓની ત્રણેય જોડીઓ 1/2 ના ગુણોત્તરમાં હોવાથી, બા-બા-બા શરત મુજબ △ABC ~ △QRP સમરૂપ છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q1_part3",
        "Exercise 6.3 (Q1.iii): In $\\triangle LMP$, $LM = 2.7, MP = 2, LP = 3$. In $\\triangle DEF$, $DE = 4, EF = 5, DF = 6$. Are the triangles similar?",
        "प्रश्नावली 6.3 (Q1.iii): $\\triangle LMP$ में, $LM = 2.7, MP = 2, LP = 3$ है। $\\triangle DEF$ में, $DE = 4, EF = 5, DF = 6$ है। क्या ये त्रिभुज समरूप हैं?",
        "સ્વાધ્યાય 6.3 (Q1.iii): $\\triangle LMP$ માં, $LM = 2.7, MP = 2, LP = 3$ છે. $\\triangle DEF$ માં, $DE = 4, EF = 5, DF = 6$ છે. શું ત્રિકોણો સમરૂપ છે?",
        [
            "No, the triangles are not similar because LM/EF = 2.7/5 ≠ 1/2",
            "Yes, by SSS criterion",
            "Yes, by SAS criterion",
            "Cannot be determined"
        ],
        [
            "नहीं, त्रिभुज समरूप नहीं हैं क्योंकि LM/EF = 2.7/5 ≠ 1/2",
            "हाँ, SSS कसौटी द्वारा",
            "हाँ, SAS कसौटी द्वारा",
            "निर्धारित नहीं किया जा सकता"
        ],
        [
            "ના, ત્રિકોણો સમરૂપ નથી કારણ કે LM/EF = 2.7/5 ≠ 1/2",
            "હા, બા-બા-બા શરત મુજબ",
            "હા, બા-ખૂ-બા શરત મુજબ",
            "નક્કી કરી શકાય નહીં"
        ],
        0,
        "Calculate ratios: MP / DE = 2 / 4 = 1/2. LP / DF = 3 / 6 = 1/2. But LM / EF = 2.7 / 5 ≠ 1/2. Since the three pairs of sides are not proportional, the triangles are not similar.",
        "अनुपातों की गणना करें: MP / DE = 2 / 4 = 1/2। LP / DF = 3 / 6 = 1/2। परंतु LM / EF = 2.7 / 5 ≠ 1/2। चूँकि भुजाओं के तीनों युग्म समानुपाती नहीं हैं, अतः त्रिभुज समरूप नहीं हैं।",
        "ગુણોત્તર ગણો: MP / DE = 2 / 4 = 1/2. LP / DF = 3 / 6 = 1/2. પરંતુ LM / EF = 2.7 / 5 ≠ 1/2. ત્રણેય બાજુઓ સમપ્રમાણમાં ન હોવાથી, ત્રિકોણો સમરૂપ નથી.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q1_part4",
        "Exercise 6.3 (Q1.iv): In $\\triangle MNL$, $MN = 2.5, ML = 5, \\angle M = 70^\\circ$. In $\\triangle QPR$, $QP = 5, QR = 10, \\angle Q = 70^\\circ$. Are the triangles similar?",
        "प्रश्नावली 6.3 (Q1.iv): $\\triangle MNL$ में, $MN = 2.5, ML = 5, \\angle M = 70^\\circ$ है। $\\triangle QPR$ में, $QP = 5, QR = 10, \\angle Q = 70^\\circ$ है। क्या ये त्रिभुज समरूप हैं?",
        "સ્વાધ્યાય 6.3 (Q1.iv): $\\triangle MNL$ માં, $MN = 2.5, ML = 5, \\angle M = 70^\\circ$ છે. $\\triangle QPR$ માં, $QP = 5, QR = 10, \\angle Q = 70^\\circ$ છે. શું ત્રિકોણો સમરૂપ છે?",
        [
            "Yes, △MNL ~ △QPR by SAS similarity criterion",
            "No, because angle M is not equal to angle P",
            "No, because MN/QR ≠ ML/QP",
            "Yes, by SSS criterion"
        ],
        [
            "हाँ, SAS समरूपता कसौटी द्वारा △MNL ~ △QPR",
            "नहीं, क्योंकि कोण M, कोण P के बराबर नहीं है",
            "नहीं, क्योंकि MN/QR ≠ ML/QP",
            "हाँ, SSS कसौटी द्वारा"
        ],
        [
            "હા, બા-ખૂ-બા સમરૂપતા શરત મુજબ △MNL ~ △QPR",
            "ના, કારણ કે ખૂણો M એ ખૂણા P ને સમાન નથી",
            "ના, કારણ કે MN/QR ≠ ML/QP",
            "હા, બા-બા-બા શરત મુજબ"
        ],
        0,
        "In △MNL and △QPR: MN / QP = 2.5 / 5 = 1/2. ML / QR = 5 / 10 = 1/2. Included angles are equal: ∠M = ∠Q = 70°. By SAS similarity criterion, △MNL ~ △QPR.",
        "△MNL और △QPR में: MN / QP = 2.5 / 5 = 1/2। ML / QR = 5 / 10 = 1/2। अंतर्गत कोण बराबर हैं: ∠M = ∠Q = 70°। अतः SAS समरूपता कसौटी द्वारा △MNL ~ △QPR समरूप हैं।",
        "△MNL અને △QPR માં: MN / QP = 2.5 / 5 = 1/2. ML / QR = 5 / 10 = 1/2. અંતર્ગત ખૂણા સમાન છે: ∠M = ∠Q = 70°. આથી બા-ખૂ-બા સમરૂપતા શરત મુજબ △MNL ~ △QPR સમરૂપ છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q1_part5",
        "Exercise 6.3 (Q1.v): In $\\triangle ABC$, $AB = 2.5, BC = 3, \\angle A = 80^\\circ$. In $\\triangle DEF$, $DF = 5, EF = 6, \\angle F = 80^\\circ$. Are the triangles similar?",
        "प्रश्नावली 6.3 (Q1.v): $\\triangle ABC$ में, $AB = 2.5, BC = 3, \\angle A = 80^\\circ$ है। $\\triangle DEF$ में, $DF = 5, EF = 6, \\angle F = 80^\\circ$ है। क्या ये त्रिभुज समरूप हैं?",
        "સ્વાધ્યાય 6.3 (Q1.v): $\\triangle ABC$ માં, $AB = 2.5, BC = 3, \\angle A = 80^\\circ$ છે. $\\triangle DEF$ માં, $DF = 5, EF = 6, \\angle F = 80^\\circ$ છે. શું ત્રિકોણો સમરૂપ છે?",
        [
            "No, because ∠A is not the included angle between sides AB and BC",
            "Yes, by SAS criterion",
            "Yes, by SSS criterion",
            "Yes, because 2.5/5 = 3/6 and angles are 80°"
        ],
        [
            "नहीं, क्योंकि ∠A भुजाओं AB और BC के बीच का अंतर्गत कोण नहीं है",
            "हाँ, SAS कसौटी द्वारा",
            "हाँ, SSS कसौटी द्वारा",
            "हाँ, क्योंकि 2.5/5 = 3/6 और कोण 80° हैं"
        ],
        [
            "ના, કારણ કે ∠A એ બાજુઓ AB અને BC વચ્ચેનો અંતર્ગત ખૂણો નથી",
            "હા, બા-ખૂ-બા શરત મુજબ",
            "હા, બા-બા-બા શરત મુજબ",
            "હા, કારણ કે 2.5/5 = 3/6 અને ખૂણા 80° છે"
        ],
        0,
        "In △ABC, the given sides are AB and BC, so the included angle is ∠B, not ∠A. Since ∠A is not the included angle, the SAS criterion cannot be satisfied. Hence, the triangles are not similar.",
        "△ABC में दी गई भुजाएँ AB और BC हैं, अतः अंतर्गत कोण ∠B होना चाहिए, ∠A नहीं। चूँकि ∠A अंतर्गत कोण नहीं है, अतः SAS कसौटी संतुष्ट नहीं होती। इसलिए त्रिभुज समरूप नहीं हैं।",
        "△ABC માં આપેલી બાજુઓ AB અને BC છે, જેથી અંતર્ગત ખૂણો ∠B થાય, ∠A નહીં. ∠A અંતર્ગત ખૂણો ન હોવાથી બા-ખૂ-બા શરત સંતોષાતી નથી. તેથી ત્રિકોણો સમરૂપ નથી.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q1_part6",
        "Exercise 6.3 (Q1.vi): In $\\triangle DEF$, $\\angle D = 70^\\circ, \\angle E = 80^\\circ$. In $\\triangle PQR$, $\\angle Q = 80^\\circ, \\angle R = 30^\\circ$. Are the triangles similar?",
        "प्रश्नावली 6.3 (Q1.vi): $\\triangle DEF$ में, $\\angle D = 70^\\circ, \\angle E = 80^\\circ$ है। $\\triangle PQR$ में, $\\angle Q = 80^\\circ, \\angle R = 30^\\circ$ है। क्या ये त्रिभुज समरूप हैं?",
        "સ્વાધ્યાય 6.3 (Q1.vi): $\\triangle DEF$ માં, $\\angle D = 70^\\circ, \\angle E = 80^\\circ$ છે. $\\triangle PQR$ માં, $\\angle Q = 80^\\circ, \\angle R = 30^\\circ$ છે. શું ત્રિકોણો સમરૂપ છે?",
        [
            "Yes, △DEF ~ △PQR by AAA / AA similarity criterion",
            "No, because the angles are completely different",
            "Yes, by SAS criterion",
            "Cannot be determined without sides"
        ],
        [
            "हाँ, AAA / AA समरूपता कसौटी द्वारा △DEF ~ △PQR",
            "नहीं, क्योंकि कोण पूरी तरह से भिन्न हैं",
            "हाँ, SAS कसौटी द्वारा",
            "भुजाओं के बिना निर्धारित नहीं किया जा सकता"
        ],
        [
            "હા, ખૂ-ખૂ-ખૂ / ખૂ-ખૂ સમરૂપતા શરત મુજબ △DEF ~ △PQR",
            "ના, કારણ કે ખૂણાઓ સંપૂર્ણપણે અલગ છે",
            "હા, બા-ખૂ-બા શરત મુજબ",
            "બાજુઓ વિના નક્કી કરી શકાય નહીં"
        ],
        0,
        "In △DEF: ∠F = 180° - (70° + 80°) = 30°. In △PQR: ∠P = 180° - (80° + 30°) = 70°. Thus ∠D = ∠P = 70°, ∠E = ∠Q = 80°, and ∠F = ∠R = 30°. By AA similarity, △DEF ~ △PQR.",
        "△DEF में: ∠F = 180° - (70° + 80°) = 30°। △PQR में: ∠P = 180° - (80° + 30°) = 70°। अतः ∠D = ∠P = 70°, ∠E = ∠Q = 80° और ∠F = ∠R = 30°। AA समरूपता द्वारा △DEF ~ △PQR समरूप हैं।",
        "△DEF માં: ∠F = 180° - (70° + 80°) = 30°. △PQR માં: ∠P = 180° - (80° + 30°) = 70°. આમ ∠D = ∠P = 70°, ∠E = ∠Q = 80° અને ∠F = ∠R = 30°. AA શરત મુજબ △DEF ~ △PQR સમરૂપ છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # Exercise 6.3 Q2
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q2",
        "Exercise 6.3 (Q2): In figure, $\\triangle ODC \\sim \\triangle OBA, \\angle BOC = 125^\\circ$, and $\\angle CDO = 70^\\circ$. Find the measures of $\\angle DOC, \\angle DCO$, and $\\angle OAB$.",
        "प्रश्नावली 6.3 (Q2): आकृति में, $\\triangle ODC \\sim \\triangle OBA, \\angle BOC = 125^\\circ$ और $\\angle CDO = 70^\\circ$ है। $\\angle DOC, \\angle DCO$ और $\\angle OAB$ के माप ज्ञात कीजिए।",
        "સ્વાધ્યાય 6.3 (Q2): આકૃતિમાં, $\\triangle ODC \\sim \\triangle OBA, \\angle BOC = 125^\\circ$ અને $\\angle CDO = 70^\\circ$ છે. $\\angle DOC, \\angle DCO$ અને $\\angle OAB$ ના માપ શોધો.",
        [
            "∠DOC = 55°, ∠DCO = 55°, ∠OAB = 55°",
            "∠DOC = 65°, ∠DCO = 45°, ∠OAB = 70°",
            "∠DOC = 55°, ∠DCO = 70°, ∠OAB = 55°",
            "∠DOC = 70°, ∠DCO = 55°, ∠OAB = 70°"
        ],
        [
            "∠DOC = 55°, ∠DCO = 55°, ∠OAB = 55°",
            "∠DOC = 65°, ∠DCO = 45°, ∠OAB = 70°",
            "∠DOC = 55°, ∠DCO = 70°, ∠OAB = 55°",
            "∠DOC = 70°, ∠DCO = 55°, ∠OAB = 70°"
        ],
        [
            "∠DOC = 55°, ∠DCO = 55°, ∠OAB = 55°",
            "∠DOC = 65°, ∠DCO = 45°, ∠OAB = 70°",
            "∠DOC = 55°, ∠DCO = 70°, ∠OAB = 55°",
            "∠DOC = 70°, ∠DCO = 55°, ∠OAB = 70°"
        ],
        0,
        "1. DOB is a straight line: ∠DOC = 180° - 125° = 55°. 2. In △ODC: ∠DCO = 180° - (70° + 55°) = 55°. 3. Since △ODC ~ △OBA: ∠OAB = ∠OCD = 55°.",
        "1. DOB एक सरल रेखा है: ∠DOC = 180° - 125° = 55°। 2. △ODC में: ∠DCO = 180° - (70° + 55°) = 55°। 3. चूँकि △ODC ~ △OBA है: ∠OAB = ∠OCD = 55°।",
        "1. DOB સીધી રેખા છે: ∠DOC = 180° - 125° = 55°. 2. △ODC માં: ∠DCO = 180° - (70° + 55°) = 55°. 3. △ODC ~ △OBA હોવાથી: ∠OAB = ∠OCD = 55°.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.3 Q3
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q3",
        "Exercise 6.3 (Q3): Diagonals $AC$ and $BD$ of a trapezium $ABCD$ with $AB \\parallel DC$ intersect at $O$. Using a triangle similarity criterion, which pair of similar triangles proves that $\\frac{OA}{OC} = \\frac{OB}{OD}$?",
        "प्रश्नावली 6.3 (Q3): समलंब $ABCD$ जिसमें $AB \\parallel DC$ है, के विकर्ण $AC$ और $BD$ परस्पर $O$ पर प्रतिच्छेद करते हैं। त्रिभुजों की समरूपता कसौटी का प्रयोग करते हुए, समरूप त्रिभुजों का कौन सा युग्म यह सिद्ध करता है कि $\\frac{OA}{OC} = \\frac{OB}{OD}$?",
        "સ્વાધ્યાય 6.3 (Q3): સમલંબ ચતુષ્કોણ $ABCD$ જેમાં $AB \\parallel DC$ છે, તેના વિકર્ણો $AC$ અને $BD$ પરસ્પર $O$ માં છેદે છે. ત્રિકોણ સમરૂપતાની શરતનો ઉપયોગ કરીને, સમરૂપ ત્રિકોણોની કઈ જોડી સાબિત કરે છે કે $\\frac{OA}{OC} = \\frac{OB}{OD}$?",
        [
            "△OAB ~ △OCD by AA similarity (alternate interior angles)",
            "△OAD ~ △OBC by SAS",
            "△ABC ~ △ADC by SSS",
            "△ABD ~ △CDB by RHS"
        ],
        [
            "AA समरूपता द्वारा △OAB ~ △OCD (एकांतर अंतःकोण)",
            "SAS द्वारा △OAD ~ △OBC",
            "SSS द्वारा △ABC ~ △ADC",
            "RHS द्वारा △ABD ~ △CDB"
        ],
        [
            "AA સમરૂપતા મુજબ △OAB ~ △OCD (યુગ્મકોણ)",
            "બા-ખૂ-બા મુજબ △OAD ~ △OBC",
            "બા-બા-બા મુજબ △ABC ~ △ADC",
            "કા-ક-બા મુજબ △ABD ~ △CDB"
        ],
        0,
        "In △OAB and △OCD: ∠OAB = ∠OCD (alternate interior angles, AB ∥ DC), ∠OBA = ∠ODC (alternate interior angles), and ∠AOB = ∠COD (vertically opposite). By AA similarity, △OAB ~ △OCD => OA / OC = OB / OD.",
        "△OAB और △OCD में: ∠OAB = ∠OCD (एकांतर अंतःकोण, AB ∥ DC), ∠OBA = ∠ODC (एकांतर अंतःकोण), और ∠AOB = ∠COD (शीर्षाभिमुख कोण)। AA समरूपता द्वारा △OAB ~ △OCD => OA / OC = OB / OD सिद्ध होता है।",
        "△OAB અને △OCD માં: ∠OAB = ∠OCD (યુગ્મકોણ, AB ∥ DC), ∠OBA = ∠ODC (યુગ્મકોણ), અને ∠AOB = ∠COD (અભિકોણ). AA સમરૂપતા મુજબ △OAB ~ △OCD => OA / OC = OB / OD સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.3 Q4
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q4",
        "Exercise 6.3 (Q4): In figure, $\\frac{QR}{QS} = \\frac{QT}{PR}$ and $\\angle 1 = \\angle 2$. Show that $\\triangle PQS \\sim \\triangle TQR$. What key deduction from $\\angle 1 = \\angle 2$ allows replacing $PR$ with $PQ$?",
        "प्रश्नावली 6.3 (Q4): आकृति में, $\\frac{QR}{QS} = \\frac{QT}{PR}$ तथा $\\angle 1 = \\angle 2$ है। दर्शाइए कि $\\triangle PQS \\sim \\triangle TQR$ है। $\\angle 1 = \\angle 2$ से कौन सा महत्वपूर्ण निष्कर्ष $PR$ को $PQ$ से प्रतिस्थापित करने की अनुमति देता है?",
        "સ્વાધ્યાય 6.3 (Q4): આકૃતિમાં, $\\frac{QR}{QS} = \\frac{QT}{PR}$ અને $\\angle 1 = \\angle 2$ છે. દર્શાવો કે $\\triangle PQS \\sim \\triangle TQR$ છે. $\\angle 1 = \\angle 2$ પરથી કયું તારણ $PR$ ની જગ્યાએ $PQ$ મૂકવાની છૂટ આપે છે?",
        [
            "In △PQR, ∠1 = ∠2 implies PQ = PR (sides opposite equal angles are equal)",
            "PQ + PR = QR",
            "PR is the median of △TQR",
            "PQ ∥ TR"
        ],
        [
            "△PQR में, ∠1 = ∠2 का अर्थ है PQ = PR (समान कोणों के सम्मुख भुजाएँ बराबर होती हैं)",
            "PQ + PR = QR",
            "PR, △TQR की माध्यिका है",
            "PQ ∥ TR"
        ],
        [
            "△PQR માં, ∠1 = ∠2 નો અર્થ થાય છે PQ = PR (સમાન ખૂણાઓની સામેની બાજુઓ સમાન હોય)",
            "PQ + PR = QR",
            "PR એ △TQR ની મધ્યગા છે",
            "PQ ∥ TR"
        ],
        0,
        "In △PQR, since ∠1 = ∠2, sides opposite to equal angles are equal: PQ = PR. Substituting PR = PQ in the given ratio gives QR / QS = QT / PQ => QT / PQ = QR / QS. In △PQS and △TQR, with common angle ∠Q, by SAS similarity, △PQS ~ △TQR.",
        "△PQR में, चूँकि ∠1 = ∠2 है, समान कोणों की सम्मुख भुजाएँ बराबर होती हैं: PQ = PR। दिए गए अनुपात में PR = PQ रखने पर QR / QS = QT / PQ प्राप्त होता है। △PQS और △TQR में उभयनिष्ठ कोण ∠Q के साथ SAS कसौटी द्वारा △PQS ~ △TQR सिद्ध होता है।",
        "△PQR માં, ∠1 = ∠2 હોવાથી સામેની બાજુઓ સમાન થાય: PQ = PR. આપેલ ગુણોત્તરમાં PR = PQ મૂકતા QR / QS = QT / PQ મળે છે. △PQS અને △TQR માં સામાન્ય ખૂણો ∠Q હોવાથી બા-ખૂ-બા શરત મુજબ △PQS ~ △TQR સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.3 Q5
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q5",
        "Exercise 6.3 (Q5): $S$ and $T$ are points on sides $PR$ and $QR$ of $\\triangle PQR$ such that $\\angle P = \\angle RTS$. Show that $\\triangle RPQ \\sim \\triangle RTS$. Which similarity criterion applies?",
        "प्रश्नावली 6.3 (Q5): $\\triangle PQR$ की भुजाओं $PR$ और $QR$ पर क्रमशः बिंदु $S$ और $T$ इस प्रकार स्थित हैं कि $\\angle P = \\angle RTS$ है। दर्शाइए कि $\\triangle RPQ \\sim \\triangle RTS$ है। यहाँ कौन सी समरूपता कसौटी लागू होती है?",
        "સ્વાધ્યાય 6.3 (Q5): $\\triangle PQR$ ની બાજુઓ $PR$ અને $QR$ પર અનુક્રમે બિંદુઓ $S$ અને $T$ એવી રીતે આવેલા છે કે જેથી $\\angle P = \\angle RTS$ થાય. દર્શાવો કે $\\triangle RPQ \\sim \\triangle RTS$ છે. અહીં કઈ સમરૂપતા શરત લાગુ પડે છે?",
        [
            "AA similarity criterion (∠P = ∠RTS and common angle ∠R)",
            "SAS similarity criterion",
            "SSS similarity criterion",
            "RHS similarity criterion"
        ],
        [
            "AA समरूपता कसौटी (∠P = ∠RTS और उभयनिष्ठ कोण ∠R)",
            "SAS समरूपता कसौटी",
            "SSS समरूपता कसौटी",
            "RHS समरूपता कसौटी"
        ],
        [
            "AA સમરૂપતા શરત (∠P = ∠RTS અને સામાન્ય ખૂણો ∠R)",
            "બા-ખૂ-બા સમરૂપતા શરત",
            "બા-બા-બા સમરૂપતા શરત",
            "કા-ક-બા સમરૂપતા શરત"
        ],
        0,
        "In △RPQ and △RTS: 1. ∠RPQ = ∠RTS (given). 2. ∠PRQ = ∠TRS (common angle ∠R). By AA similarity criterion, △RPQ ~ △RTS.",
        "△RPQ और △RTS में: 1. ∠RPQ = ∠RTS (दिया है)। 2. ∠PRQ = ∠TRS (उभयनिष्ठ कोण ∠R)। अतः AA समरूपता कसौटी द्वारा △RPQ ~ △RTS सिद्ध होता है।",
        "△RPQ અને △RTS માં: 1. ∠RPQ = ∠RTS (આપેલ છે). 2. ∠PRQ = ∠TRS (સામાન્ય ખૂણો ∠R). આથી AA સમરૂપતા શરત મુજબ △RPQ ~ △RTS સાબિત થાય છે.",
        bloom="Understand",
        diff="Beginner",
        mins=2
    ))

    # Exercise 6.3 Q6
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q6",
        "Exercise 6.3 (Q6): In figure, if $\\triangle ABE \\cong \\triangle ACD$, show that $\\triangle ADE \\sim \\triangle ABC$. What side proportions follow from the congruence?",
        "प्रश्नावली 6.3 (Q6): आकृति में, यदि $\\triangle ABE \\cong \\triangle ACD$ है, तो दर्शाइए कि $\\triangle ADE \\sim \\triangle ABC$ है। सर्वांगसमता से कौन सा भुजा अनुपात प्राप्त होता है?",
        "સ્વાધ્યાય 6.3 (Q6): આકૃતિમાં, જો $\\triangle ABE \\cong \\triangle ACD$ હોય, તો દર્શાવો કે $\\triangle ADE \\sim \\triangle ABC$ છે. એકરૂપતા પરથી કયો બાજુ ગુણોત્તર મળે છે?",
        [
            "AB = AC and AD = AE => AD/AB = AE/AC, with common ∠A giving SAS similarity",
            "AB / BC = AD / DE",
            "BE / CD = 1/2",
            "AD / DB = AE / EC by BPT"
        ],
        [
            "AB = AC और AD = AE => AD/AB = AE/AC, उभयनिष्ठ ∠A के साथ SAS समरूपता देता है",
            "AB / BC = AD / DE",
            "BE / CD = 1/2",
            "BPT द्वारा AD / DB = AE / EC"
        ],
        [
            "AB = AC અને AD = AE => AD/AB = AE/AC, સામાન્ય ∠A સાથે બા-ખૂ-બા સમરૂપતા આપે છે",
            "AB / BC = AD / DE",
            "BE / CD = 1/2",
            "BPT મુજબ AD / DB = AE / EC"
        ],
        0,
        "Since △ABE ≅ △ACD: AB = AC (CPCTC) and AE = AD => AD = AE (CPCTC). Dividing: AD / AB = AE / AC. In △ADE and △ABC, AD / AB = AE / AC and ∠DAE = ∠BAC (common angle ∠A). By SAS similarity, △ADE ~ △ABC.",
        "चूँकि △ABE ≅ △ACD है: AB = AC और AE = AD (CPCTC)। भाग देने पर: AD / AB = AE / AC। △ADE और △ABC में, AD / AB = AE / AC और उभयनिष्ठ कोण ∠A के साथ SAS कसौटी द्वारा △ADE ~ △ABC सिद्ध होता है।",
        "△ABE ≅ △ACD હોવાથી: AB = AC અને AE = AD (CPCTC). ભાગાકાર કરતા: AD / AB = AE / AC. △ADE અને △ABC માં, AD / AB = AE / AC અને સામાન્ય ખૂણા ∠A સાથે બા-ખૂ-બા શરત મુજબ △ADE ~ △ABC સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.3 Q7 (i to iv)
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q7_part1",
        "Exercise 6.3 (Q7.i): Altitudes $AD$ and $CE$ of $\\triangle ABC$ intersect at $P$. Show that $\\triangle AEP \\sim \\triangle CDP$. Which angles match?",
        "प्रश्नावली 6.3 (Q7.i): $\\triangle ABC$ के शीर्षलम्ब $AD$ और $CE$ परस्पर बिंदु $P$ पर प्रतिच्छेद करते हैं। दर्शाइए कि $\\triangle AEP \\sim \\triangle CDP$ है। कौन से कोण समान हैं?",
        "સ્વાધ્યાય 6.3 (Q7.i): $\\triangle ABC$ ના વેધ $AD$ અને $CE$ પરસ્પર બિંદુ $P$ માં છેદે છે. દર્શાવો કે $\\triangle AEP \\sim \\triangle CDP$ છે. કયા ખૂણાઓ સમાન છે?",
        [
            "∠AEP = ∠CDP = 90° and ∠APE = ∠CPD (vertically opposite angles), by AA",
            "∠AEP = ∠CDP = 45°",
            "∠A = ∠C and AP = CP",
            "AE = CD and EP = DP"
        ],
        [
            "∠AEP = ∠CDP = 90° और ∠APE = ∠CPD (शीर्षाभिमुख कोण), AA द्वारा",
            "∠AEP = ∠CDP = 45°",
            "∠A = ∠C और AP = CP",
            "AE = CD और EP = DP"
        ],
        [
            "∠AEP = ∠CDP = 90° અને ∠APE = ∠CPD (અભિકોણ), AA મુજબ",
            "∠AEP = ∠CDP = 45°",
            "∠A = ∠C અને AP = CP",
            "AE = CD અને EP = DP"
        ],
        0,
        "In △AEP and △CDP: ∠AEP = ∠CDP = 90° (altitudes) and ∠APE = ∠CPD (vertically opposite angles). By AA similarity criterion, △AEP ~ △CDP.",
        "△AEP और △CDP में: ∠AEP = ∠CDP = 90° (शीर्षलम्ब) और ∠APE = ∠CPD (शीर्षाभिमुख कोण)। अतः AA समरूपता कसौटी द्वारा △AEP ~ △CDP सिद्ध होता है।",
        "△AEP અને △CDP માં: ∠AEP = ∠CDP = 90° (વેધ) અને ∠APE = ∠CPD (અભિકોણ). આમ AA સમરૂપતા શરત મુજબ △AEP ~ △CDP સાબિત થાય છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q7_part2",
        "Exercise 6.3 (Q7.ii): Altitudes $AD$ and $CE$ intersect at $P$. Show that $\\triangle ABD \\sim \\triangle CBE$. Which two angles establish similarity?",
        "प्रश्नावली 6.3 (Q7.ii): शीर्षलम्ब $AD$ और $CE$ परस्पर $P$ पर प्रतिच्छेद करते हैं। दर्शाइए कि $\\triangle ABD \\sim \\triangle CBE$ है। कौन से दो कोण समरूपता स्थापित करते हैं?",
        "સ્વાધ્યાય 6.3 (Q7.ii): વેધ $AD$ અને $CE$ પરસ્પર $P$ માં છેદે છે. દર્શાવો કે $\\triangle ABD \\sim \\triangle CBE$ છે. કયા બે ખૂણા સમરૂપતા સ્થાપિત કરે છે?",
        [
            "∠ADB = ∠CEB = 90° and common angle ∠B, by AA criterion",
            "∠A = ∠C and ∠D = ∠E",
            "AB = CB and BD = BE",
            "∠ADB = ∠CEB = 60°"
        ],
        [
            "∠ADB = ∠CEB = 90° और उभयनिष्ठ कोण ∠B, AA कसौटी द्वारा",
            "∠A = ∠C और ∠D = ∠E",
            "AB = CB और BD = BE",
            "∠ADB = ∠CEB = 60°"
        ],
        [
            "∠ADB = ∠CEB = 90° અને સામાન્ય ખૂણો ∠B, AA શરત મુજબ",
            "∠A = ∠C અને ∠D = ∠E",
            "AB = CB અને BD = BE",
            "∠ADB = ∠CEB = 60°"
        ],
        0,
        "In △ABD and △CBE: 1. ∠ADB = ∠CEB = 90° (altitudes). 2. ∠ABD = ∠CBE (common angle ∠B). By AA similarity criterion, △ABD ~ △CBE.",
        "△ABD और △CBE में: 1. ∠ADB = ∠CEB = 90° (शीर्षलम्ब)। 2. ∠ABD = ∠CBE (उभयनिष्ठ कोण ∠B)। अतः AA समरूपता कसौटी द्वारा △ABD ~ △CBE सिद्ध होता है।",
        "△ABD અને △CBE માં: 1. ∠ADB = ∠CEB = 90° (વેધ). 2. ∠ABD = ∠CBE (સામાન્ય ખૂણો ∠B). આમ AA સમરૂપતા શરત મુજબ △ABD ~ △CBE સાબિત થાય છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q7_part3",
        "Exercise 6.3 (Q7.iii): Altitudes $AD$ and $CE$ intersect at $P$. Show that $\\triangle AEP \\sim \\triangle ADB$. Which angles are equal?",
        "प्रश्नावली 6.3 (Q7.iii): शीर्षलम्ब $AD$ और $CE$ परस्पर $P$ पर प्रतिच्छेद करते हैं। दर्शाइए कि $\\triangle AEP \\sim \\triangle ADB$ है। कौन से कोण बराबर हैं?",
        "સ્વાધ્યાય 6.3 (Q7.iii): વેધ $AD$ અને $CE$ પરસ્પર $P$ માં છેદે છે. દર્શાવો કે $\\triangle AEP \\sim \\triangle ADB$ છે. કયા ખૂણાઓ સમાન છે?",
        [
            "∠AEP = ∠ADB = 90° and common angle ∠A, by AA criterion",
            "∠P = ∠B and AE = AD",
            "∠APE = ∠ABD",
            "AP = AB and EP = DB"
        ],
        [
            "∠AEP = ∠ADB = 90° और उभयनिष्ठ कोण ∠A, AA कसौटी द्वारा",
            "∠P = ∠B और AE = AD",
            "∠APE = ∠ABD",
            "AP = AB और EP = DB"
        ],
        [
            "∠AEP = ∠ADB = 90° અને સામાન્ય ખૂણો ∠A, AA શરત મુજબ",
            "∠P = ∠B અને AE = AD",
            "∠APE = ∠ABD",
            "AP = AB અને EP = DB"
        ],
        0,
        "In △AEP and △ADB: 1. ∠AEP = ∠ADB = 90°. 2. ∠PAE = ∠DAB (common angle ∠A). By AA similarity criterion, △AEP ~ △ADB.",
        "△AEP और △ADB में: 1. ∠AEP = ∠ADB = 90°। 2. ∠PAE = ∠DAB (उभयनिष्ठ कोण ∠A)। अतः AA समरूपता कसौटी द्वारा △AEP ~ △ADB सिद्ध होता है।",
        "△AEP અને △ADB માં: 1. ∠AEP = ∠ADB = 90°. 2. ∠PAE = ∠DAB (સામાન્ય ખૂણો ∠A). આમ AA સમરૂપતા શરત મુજબ △AEP ~ △ADB સાબિત થાય છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q7_part4",
        "Exercise 6.3 (Q7.iv): Altitudes $AD$ and $CE$ intersect at $P$. Show that $\\triangle PDC \\sim \\triangle BEC$. Which two angles match?",
        "प्रश्नावली 6.3 (Q7.iv): शीर्षलम्ब $AD$ और $CE$ परस्पर $P$ पर प्रतिच्छेद करते हैं। दर्शाइए कि $\\triangle PDC \\sim \\triangle BEC$ है। कौन से दो कोण समान हैं?",
        "સ્વાધ્યાય 6.3 (Q7.iv): વેધ $AD$ અને $CE$ પરસ્પર $P$ માં છેદે છે. દર્શાવો કે $\\triangle PDC \\sim \\triangle BEC$ છે. કયા બે ખૂણા સમાન છે?",
        [
            "∠PDC = ∠BEC = 90° and common angle ∠C, by AA criterion",
            "∠DPC = ∠EBC and PD = BE",
            "CD = CE and ∠P = ∠B",
            "∠PDC = 45° and ∠BEC = 45°"
        ],
        [
            "∠PDC = ∠BEC = 90° और उभयनिष्ठ कोण ∠C, AA कसौटी द्वारा",
            "∠DPC = ∠EBC और PD = BE",
            "CD = CE और ∠P = ∠B",
            "∠PDC = 45° और ∠BEC = 45°"
        ],
        [
            "∠PDC = ∠BEC = 90° અને સામાન્ય ખૂણો ∠C, AA શરત મુજબ",
            "∠DPC = ∠EBC અને PD = BE",
            "CD = CE અને ∠P = ∠B",
            "∠PDC = 45° અને ∠BEC = 45°"
        ],
        0,
        "In △PDC and △BEC: 1. ∠PDC = ∠BEC = 90°. 2. ∠PCD = ∠BCE (common angle ∠C). By AA similarity criterion, △PDC ~ △BEC.",
        "△PDC और △BEC में: 1. ∠PDC = ∠BEC = 90°। 2. ∠PCD = ∠BCE (उभयनिष्ठ कोण ∠C)। अतः AA समरूपता कसौटी द्वारा △PDC ~ △BEC सिद्ध होता है।",
        "△PDC અને △BEC માં: 1. ∠PDC = ∠BEC = 90°. 2. ∠PCD = ∠BCE (સામાન્ય ખૂણો ∠C). આમ AA સમરૂપતા શરત મુજબ △PDC ~ △BEC સાબિત થાય છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # Exercise 6.3 Q8
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q8",
        "Exercise 6.3 (Q8): $E$ is a point on side $AD$ produced of a parallelogram $ABCD$ and $BE$ intersects $CD$ at $F$. Show that $\\triangle ABE \\sim \\triangle CFB$. Why are the corresponding angles equal?",
        "प्रश्नावली 6.3 (Q8): समांतर चतुर्भुज $ABCD$ की बढ़ाई गई भुजा $AD$ पर स्थित $E$ एक बिंदु है तथा $BE$ भुजा $CD$ को $F$ पर प्रतिच्छेद करती है। दर्शाइए कि $\\triangle ABE \\sim \\triangle CFB$ है। संगत कोण बराबर क्यों हैं?",
        "સ્વાધ્યાય 6.3 (Q8): સમાંતરબાજુ ચતુષ્કોણ $ABCD$ ની લંબાવેલી બાજુ $AD$ પરનું બિંદુ $E$ છે અને $BE$ એ $CD$ ને $F$ માં છેદે છે. દર્શાવો કે $\\triangle ABE \\sim \\triangle CFB$ છે. અનુરૂપ ખૂણાઓ શા માટે સમાન છે?",
        [
            "∠A = ∠C (opposite angles of parallelogram) and ∠AEB = ∠CBF (alternate interior angles as AE ∥ BC)",
            "∠A = ∠F and ∠B = ∠C",
            "AB = CF and BE = BF",
            "Because ABCD is a rectangle"
        ],
        [
            "∠A = ∠C (समांतर चतुर्भुज के सम्मुख कोण) और ∠AEB = ∠CBF (एकांतर अंतःकोण क्योंकि AE ∥ BC)",
            "∠A = ∠F और ∠B = ∠C",
            "AB = CF और BE = BF",
            "क्योंकि ABCD एक आयत है"
        ],
        [
            "∠A = ∠C (સમાંતરબાજુ ચતુષ્કોણના સામસામેના ખૂણા) અને ∠AEB = ∠CBF (યુગ્મકોણ કારણ કે AE ∥ BC)",
            "∠A = ∠F અને ∠B = ∠C",
            "AB = CF અને BE = BF",
            "કારણ કે ABCD લંબચોરસ છે"
        ],
        0,
        "In △ABE and △CFB: 1. ∠A = ∠C (opposite angles of parallelogram ABCD are equal). 2. AE ∥ BC (AD produced ∥ BC), so transversal BE gives alternate interior angles ∠AEB = ∠CBF. By AA criterion, △ABE ~ △CFB.",
        "△ABE और △CFB में: 1. ∠A = ∠C (समांतर चतुर्भुज ABCD के सम्मुख कोण बराबर होते हैं)। 2. AE ∥ BC, अतः तिर्यक रेखा BE के लिए एकांतर अंतःकोण ∠AEB = ∠CBF। AA कसौटी द्वारा △ABE ~ △CFB सिद्ध होता है।",
        "△ABE અને △CFB માં: 1. ∠A = ∠C (સમાંતરબાજુ ચતુષ્કોણ ABCD ના સામસામેના ખૂણા સમાન). 2. AE ∥ BC હોવાથી છેદિકા BE માટે યુગ્મકોણ ∠AEB = ∠CBF. AA શરત મુજબ △ABE ~ △CFB સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.3 Q9 (i and ii)
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q9_part1",
        "Exercise 6.3 (Q9.i): $ABC$ and $AMP$ are two right triangles, right-angled at $B$ and $M$ respectively. Prove that $\\triangle ABC \\sim \\triangle AMP$. Which angles are equal?",
        "प्रश्नावली 6.3 (Q9.i): $ABC$ और $AMP$ दो समकोण त्रिभुज हैं, जिनके कोण $B$ और $M$ समकोण हैं। सिद्ध कीजिए कि $\\triangle ABC \\sim \\triangle AMP$ है। कौन से कोण समान हैं?",
        "સ્વાધ્યાય 6.3 (Q9.i): $ABC$ અને $AMP$ બે કાટકોણ ત્રિકોણ છે, જેમાં ખૂણા $B$ અને $M$ કાટખૂણા છે. સાબિત કરો કે $\\triangle ABC \\sim \\triangle AMP$ છે. કયા ખૂણા સમાન છે?",
        [
            "∠ABC = ∠AMP = 90° and common angle ∠A, by AA criterion",
            "∠B = ∠M and ∠C = ∠P = 45°",
            "AB = AM and BC = MP",
            "AC = AP and BC = MP"
        ],
        [
            "∠ABC = ∠AMP = 90° और उभयनिष्ठ कोण ∠A, AA कसौटी द्वारा",
            "∠B = ∠M और ∠C = ∠P = 45°",
            "AB = AM और BC = MP",
            "AC = AP और BC = MP"
        ],
        [
            "∠ABC = ∠AMP = 90° અને સામાન્ય ખૂણો ∠A, AA શરત મુજબ",
            "∠B = ∠M અને ∠C = ∠P = 45°",
            "AB = AM અને BC = MP",
            "AC = AP અને BC = MP"
        ],
        0,
        "In △ABC and △AMP: 1. ∠ABC = ∠AMP = 90° (given). 2. ∠BAC = ∠MAP (common angle ∠A). By AA similarity criterion, △ABC ~ △AMP.",
        "△ABC और △AMP में: 1. ∠ABC = ∠AMP = 90° (दिया है)। 2. ∠BAC = ∠MAP (उभयनिष्ठ कोण ∠A)। अतः AA समरूपता कसौटी द्वारा △ABC ~ △AMP सिद्ध होता है।",
        "△ABC અને △AMP માં: 1. ∠ABC = ∠AMP = 90° (આપેલ છે). 2. ∠BAC = ∠MAP (સામાન્ય ખૂણો ∠A). આથી AA સમરૂપતા શરત મુજબ △ABC ~ △AMP સાબિત થાય છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q9_part2",
        "Exercise 6.3 (Q9.ii): Since $\\triangle ABC \\sim \\triangle AMP$, which corresponding sides ratio proves that $\\frac{CA}{PA} = \\frac{BC}{MP}$?",
        "प्रश्नावली 6.3 (Q9.ii): चूँकि $\\triangle ABC \\sim \\triangle AMP$ है, संगत भुजाओं का कौन सा अनुपात $\\frac{CA}{PA} = \\frac{BC}{MP}$ सिद्ध करता है?",
        "સ્વાધ્યાય 6.3 (Q9.ii): $\\triangle ABC \\sim \\triangle AMP$ હોવાથી, અનુરૂપ બાજુઓનો કયો ગુણોત્તર સાબિત કરે છે કે $\\frac{CA}{PA} = \\frac{BC}{MP}$?",
        [
            "Corresponding sides of similar triangles are in the same ratio: CA/PA = BC/MP = AB/AM",
            "Pythagoras Theorem in both triangles",
            "Area ratio theorem",
            "Hypotenuse equality"
        ],
        [
            "समरूप त्रिभुजों की संगत भुजाएँ समान अनुपात में होती हैं: CA/PA = BC/MP = AB/AM",
            "दोनों त्रिभुजों में पाइथागोरस प्रमेय",
            "क्षेत्रफल अनुपात प्रमेय",
            "कर्ण की समानता"
        ],
        [
            "સમરૂપ ત્રિકોણોની અનુરૂપ બાજુઓ સમાન ગુણોત્તરમાં હોય છે: CA/PA = BC/MP = AB/AM",
            "બંને ત્રિકોણમાં પાયથાગોરસ પ્રમેય",
            "ક્ષેત્રફળ ગુણોત્તર પ્રમેય",
            "કર્ણની સમાનતા"
        ],
        0,
        "From △ABC ~ △AMP, the corresponding sides are proportional: AB / AM = BC / MP = CA / PA. Taking the last two ratios directly gives CA / PA = BC / MP.",
        "△ABC ~ △AMP से, संगत भुजाएँ समानुपाती होती हैं: AB / AM = BC / MP = CA / PA। अंतिम दो अनुपातों को लेने पर सीधे CA / PA = BC / MP प्राप्त होता है।",
        "△ABC ~ △AMP પરથી, અનુરૂપ બાજુઓ સમપ્રમાણમાં હોય: AB / AM = BC / MP = CA / PA. છેલ્લા બે ગુણોત્તર લેતા સીધું જ CA / PA = BC / MP સાબિત થાય છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # Exercise 6.3 Q10 (i, ii, iii)
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q10_part1",
        "Exercise 6.3 (Q10.i): $CD$ and $GH$ are bisectors of $\\angle ACB$ and $\\angle EGF$ such that $D$ and $H$ lie on sides $AB$ and $FE$ of $\\triangle ABC$ and $\\triangle FEG$. If $\\triangle ABC \\sim \\triangle FEG$, show that $\\frac{CD}{GH} = \\frac{AC}{FG}$. Which pair of similar triangles gives this ratio?",
        "प्रश्नावली 6.3 (Q10.i): $CD$ और $GH$ क्रमशः $\\angle ACB$ और $\\angle EGF$ के ऐसे समद्विभाजक हैं कि बिंदु $D$ और $H$ क्रमशः $\\triangle ABC$ और $\\triangle FEG$ की भुजाओं $AB$ और $FE$ पर स्थित हैं। यदि $\\triangle ABC \\sim \\triangle FEG$ है, तो दर्शाइए कि $\\frac{CD}{GH} = \\frac{AC}{FG}$ है। समरूप त्रिभुजों का कौन सा युग्म यह अनुपात देता है?",
        "સ્વાધ્યાય 6.3 (Q10.i): $CD$ અને $GH$ અનુક્રમે $\\angle ACB$ અને $\\angle EGF$ ના દ્વિભાજકો છે જ્યાં $D$ અને $H$ એ $\\triangle ABC$ અને $\\triangle FEG$ ની બાજુઓ $AB$ અને $FE$ પર આવેલા છે. જો $\\triangle ABC \\sim \\triangle FEG$ હોય, તો દર્શાવો કે $\\frac{CD}{GH} = \\frac{AC}{FG}$ છે. સમરૂપ ત્રિકોણોની કઈ જોડી આ ગુણોત્તર આપે છે?",
        [
            "△DCA ~ △HGF by AA similarity criterion",
            "△DCB ~ △HGF by SSS",
            "△ABC ~ △DCA by SAS",
            "△CDG ~ △AHF by RHS"
        ],
        [
            "AA समरूपता कसौटी द्वारा △DCA ~ △HGF",
            "SSS द्वारा △DCB ~ △HGF",
            "SAS द्वारा △ABC ~ △DCA",
            "RHS द्वारा △CDG ~ △AHF"
        ],
        [
            "AA સમરૂપતા શરત મુજબ △DCA ~ △HGF",
            "બા-બા-બા મુજબ △DCB ~ △HGF",
            "બા-ખૂ-બા મુજબ △ABC ~ △DCA",
            "કા-ક-બા મુજબ △CDG ~ △AHF"
        ],
        0,
        "Since △ABC ~ △FEG: ∠A = ∠F and ∠C = ∠G => (1/2)∠C = (1/2)∠G => ∠ACD = ∠FGH. In △DCA and △HGF: ∠A = ∠F and ∠ACD = ∠FGH. By AA criterion, △DCA ~ △HGF => CD / GH = AC / FG.",
        "चूँकि △ABC ~ △FEG है: ∠A = ∠F और ∠C = ∠G => (1/2)∠C = (1/2)∠G => ∠ACD = ∠FGH। △DCA और △HGF में: ∠A = ∠F और ∠ACD = ∠FGH। AA कसौटी द्वारा △DCA ~ △HGF => CD / GH = AC / FG सिद्ध होता है।",
        "△ABC ~ △FEG હોવાથી: ∠A = ∠F અને ∠C = ∠G => (1/2)∠C = (1/2)∠G => ∠ACD = ∠FGH. △DCA અને △HGF માં: ∠A = ∠F અને ∠ACD = ∠FGH. AA શરત મુજબ △DCA ~ △HGF => CD / GH = AC / FG સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q10_part2",
        "Exercise 6.3 (Q10.ii): In the same configuration, show that $\\triangle DCB \\sim \\triangle HGE$. Which angles prove their similarity?",
        "प्रश्नावली 6.3 (Q10.ii): उसी स्थिति में, दर्शाइए कि $\\triangle DCB \\sim \\triangle HGE$ है। कौन से कोण उनकी समरूपता सिद्ध करते हैं?",
        "સ્વાધ્યાય 6.3 (Q10.ii): તે જ ગોઠવણીમાં, દર્શાવો કે $\\triangle DCB \\sim \\triangle HGE$ છે. કયા ખૂણાઓ તેમની સમરૂપતા સાબિત કરે છે?",
        [
            "∠B = ∠E and ∠DCB = ∠HGE (half of equal angles ∠C and ∠G), by AA",
            "∠D = ∠H and CD = GH",
            "BC = GE and BD = HE",
            "∠B = ∠E = 90°"
        ],
        [
            "∠B = ∠E और ∠DCB = ∠HGE (समान कोणों ∠C और ∠G के आधे), AA द्वारा",
            "∠D = ∠H और CD = GH",
            "BC = GE और BD = HE",
            "∠B = ∠E = 90°"
        ],
        [
            "∠B = ∠E અને ∠DCB = ∠HGE (સમાન ખૂણા ∠C અને ∠G ના અડધા), AA મુજબ",
            "∠D = ∠H અને CD = GH",
            "BC = GE અને BD = HE",
            "∠B = ∠E = 90°"
        ],
        0,
        "From △ABC ~ △FEG: ∠B = ∠E and ∠C = ∠G => (1/2)∠C = (1/2)∠G => ∠DCB = ∠HGE. By AA similarity criterion, △DCB ~ △HGE.",
        "△ABC ~ △FEG से: ∠B = ∠E और ∠C = ∠G => (1/2)∠C = (1/2)∠G => ∠DCB = ∠HGE। अतः AA समरूपता कसौटी द्वारा △DCB ~ △HGE सिद्ध होता है।",
        "△ABC ~ △FEG પરથી: ∠B = ∠E અને ∠C = ∠G => (1/2)∠C = (1/2)∠G => ∠DCB = ∠HGE. આમ AA સમરૂપતા શરત મુજબ △DCB ~ △HGE સાબિત થાય છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q10_part3",
        "Exercise 6.3 (Q10.iii): Show that $\\triangle DCA \\sim \\triangle HGF$.",
        "प्रश्नावली 6.3 (Q10.iii): दर्शाइए कि $\\triangle DCA \\sim \\triangle HGF$ है।",
        "સ્વાધ્યાય 6.3 (Q10.iii): દર્શાવો કે $\\triangle DCA \\sim \\triangle HGF$ છે.",
        [
            "Proved by AA similarity since ∠A = ∠F and ∠DCA = ∠HGF",
            "Proved by SSS similarity",
            "Proved by RHS similarity",
            "Cannot be proved without knowing angle D"
        ],
        [
            "AA समरूपता द्वारा सिद्ध क्योंकि ∠A = ∠F और ∠DCA = ∠HGF",
            "SSS समरूपता द्वारा सिद्ध",
            "RHS समरूपता द्वारा सिद्ध",
            "कोण D जाने बिना सिद्ध नहीं किया जा सकता"
        ],
        [
            "AA સમરૂપતા દ્વારા સાબિત કારણ કે ∠A = ∠F અને ∠DCA = ∠HGF",
            "બા-બા-બા સમરૂપતા દ્વારા સાબિત",
            "કા-ક-બા સમરૂપતા દ્વારા સાબિત",
            "ખૂણો D જાણ્યા વગર સાબિત કરી શકાય નહીં"
        ],
        0,
        "Since △ABC ~ △FEG, ∠A = ∠F and ∠C = ∠G. Bisector gives ∠DCA = (1/2)∠C = (1/2)∠G = ∠HGF. By AA similarity criterion, △DCA ~ △HGF.",
        "चूँकि △ABC ~ △FEG है, ∠A = ∠F और ∠C = ∠G। समद्विभाजक से ∠DCA = (1/2)∠C = (1/2)∠G = ∠HGF प्राप्त होता है। AA समरूपता कसौटी द्वारा △DCA ~ △HGF सिद्ध होता है।",
        "△ABC ~ △FEG હોવાથી, ∠A = ∠F અને ∠C = ∠G. દ્વિભાજક પરથી ∠DCA = (1/2)∠C = (1/2)∠G = ∠HGF મળે છે. AA સમરૂપતા શરત મુજબ △DCA ~ △HGF સાબિત થાય છે.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # Exercise 6.3 Q11
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q11",
        "Exercise 6.3 (Q11): In figure, $E$ is a point on side $CB$ produced of an isosceles triangle $ABC$ with $AB = AC$. If $AD \\perp BC$ and $EF \\perp AC$, prove that $\\triangle ABD \\sim \\triangle ECF$. Why is $\\angle ABD = \\angle ECF$?",
        "प्रश्नावली 6.3 (Q11): आकृति में, $AB = AC$ वाले एक समद्विबाहु त्रिभुज $ABC$ की बढ़ाई गई भुजा $CB$ पर स्थित $E$ एक बिंदु है। यदि $AD \\perp BC$ और $EF \\perp AC$ है, तो सिद्ध कीजिए कि $\\triangle ABD \\sim \\triangle ECF$ है। $\\angle ABD = \\angle ECF$ क्यों है?",
        "સ્વાધ્યાય 6.3 (Q11): આકૃતિમાં, $AB = AC$ વાળા સમદ્વિબાજુ ત્રિકોણ $ABC$ ની લંબાવેલી બાજુ $CB$ પરનું બિંદુ $E$ છે. જો $AD \\perp BC$ અને $EF \\perp AC$ હોય, તો સાબિત કરો કે $\\triangle ABD \\sim \\triangle ECF$ છે. $\\angle ABD = \\angle ECF$ શા માટે છે?",
        [
            "In △ABC, AB = AC implies base angles ∠B = ∠C, so ∠ABD = ∠ECF",
            "Because AD bisects ∠A",
            "Because EF is parallel to AB",
            "Because both are 90° angles"
        ],
        [
            "△ABC में, AB = AC का अर्थ है आधार कोण ∠B = ∠C, अतः ∠ABD = ∠ECF",
            "क्योंकि AD, ∠A को समद्विभाजित करता है",
            "क्योंकि EF, AB के समांतर है",
            "क्योंकि दोनों 90° के कोण हैं"
        ],
        [
            "△ABC માં, AB = AC હોવાથી પાયાના ખૂણા ∠B = ∠C થાય, તેથી ∠ABD = ∠ECF",
            "કારણ કે AD એ ∠A નો દ્વિભાજક છે",
            "કારણ કે EF એ AB ને સમાંતર છે",
            "કારણ કે બંને 90° ના ખૂણા છે"
        ],
        0,
        "In △ABC, AB = AC => ∠B = ∠C => ∠ABD = ∠ECF. In △ABD and △ECF: 1. ∠ADB = ∠EFC = 90° (altitudes). 2. ∠ABD = ∠ECF. By AA similarity criterion, △ABD ~ △ECF.",
        "△ABC में, AB = AC => ∠B = ∠C => ∠ABD = ∠ECF। △ABD और △ECF में: 1. ∠ADB = ∠EFC = 90° (लम्ब)। 2. ∠ABD = ∠ECF। अतः AA समरूपता कसौटी द्वारा △ABD ~ △ECF सिद्ध होता है।",
        "△ABC માં, AB = AC => ∠B = ∠C => ∠ABD = ∠ECF. △ABD અને △ECF માં: 1. ∠ADB = ∠EFC = 90° (વેધ). 2. ∠ABD = ∠ECF. આમ AA સમરૂપતા શરત મુજબ △ABD ~ △ECF સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.3 Q12
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q12",
        "Exercise 6.3 (Q12): Sides $AB$ and $BC$ and median $AD$ of a triangle $ABC$ are respectively proportional to sides $PQ$ and $QR$ and median $PM$ of $\\triangle PQR$. Show that $\\triangle ABC \\sim \\triangle PQR$. What step links $BC / QR$ to $BD / QM$?",
        "प्रश्नावली 6.3 (Q12): एक त्रिभुज $ABC$ की भुजाएँ $AB$ और $BC$ तथा माध्यिका $AD$ एक अन्य त्रिभुज $PQR$ की क्रमशः भुजाओं $PQ$ और $QR$ तथा माध्यिका $PM$ के समानुपाती हैं। दर्शाइए कि $\\triangle ABC \\sim \\triangle PQR$ है। कौन सा चरण $BC / QR$ को $BD / QM$ से जोड़ता है?",
        "સ્વાધ્યાય 6.3 (Q12): ત્રિકોણ $ABC$ ની બાજુઓ $AB$ અને $BC$ તથા મધ્યગા $AD$, ત્રિકોણ $PQR$ ની અનુરૂપ બાજુઓ $PQ$ અને $QR$ તથા મધ્યગા $PM$ ના સમપ્રમાણમાં છે. દર્શાવો કે $\\triangle ABC \\sim \\triangle PQR$ છે. કયું પગથિયું $BC / QR$ ને $BD / QM$ સાથે જોડે છે?",
        [
            "Medians bisect sides: BC = 2BD and QR = 2QM, so BC/QR = 2BD/(2QM) = BD/QM",
            "BC = BD and QR = QM",
            "AD ⊥ BC and PM ⊥ QR",
            "Area of △ABD = Area of △PQM"
        ],
        [
            "माध्यिकाएँ भुजाओं को समद्विभाजित करती हैं: BC = 2BD और QR = 2QM, अतः BC/QR = 2BD/(2QM) = BD/QM",
            "BC = BD और QR = QM",
            "AD ⊥ BC और PM ⊥ QR",
            "△ABD का क्षेत्रफल = △PQM का क्षेत्रफल"
        ],
        [
            "મધ્યગા બાજુઓને દુભાગે છે: BC = 2BD અને QR = 2QM, તેથી BC/QR = 2BD/(2QM) = BD/QM",
            "BC = BD અને QR = QM",
            "AD ⊥ BC અને PM ⊥ QR",
            "△ABD નું ક્ષેત્રફળ = △PQM નું ક્ષેત્રફળ"
        ],
        0,
        "Given AB/PQ = BC/QR = AD/PM => AB/PQ = (2BD)/(2QM) = AD/PM => AB/PQ = BD/QM = AD/PM. By SSS similarity, △ABD ~ △PQM => ∠B = ∠Q. Then in △ABC and △PQR: AB/PQ = BC/QR and ∠B = ∠Q. By SAS similarity, △ABC ~ △PQR.",
        "दिया है AB/PQ = BC/QR = AD/PM => AB/PQ = (2BD)/(2QM) = AD/PM => AB/PQ = BD/QM = AD/PM। SSS समरूपता से △ABD ~ △PQM => ∠B = ∠Q। अब △ABC और △PQR में: AB/PQ = BC/QR और ∠B = ∠Q होने से SAS कसौटी द्वारा △ABC ~ △PQR सिद्ध होता है।",
        "આપેલ છે AB/PQ = BC/QR = AD/PM => AB/PQ = (2BD)/(2QM) = AD/PM => AB/PQ = BD/QM = AD/PM. બા-બા-બા સમરૂપતા પરથી △ABD ~ △PQM => ∠B = ∠Q. હવે △ABC અને △PQR માં: AB/PQ = BC/QR અને ∠B = ∠Q હોવાથી બા-ખૂ-બા શરત મુજબ △ABC ~ △PQR સાબિત થાય છે.",
        bloom="Analyze",
        diff="Advanced",
        mins=3
    ))

    # Exercise 6.3 Q13
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q13",
        "Exercise 6.3 (Q13): $D$ is a point on side $BC$ of a triangle $ABC$ such that $\\angle ADC = \\angle BAC$. Show that $CA^2 = CB \\cdot CD$. Which similar triangles establish this result?",
        "प्रश्नावली 6.3 (Q13): एक त्रिभुज $ABC$ की भुजा $BC$ पर एक बिंदु $D$ इस प्रकार स्थित है कि $\\angle ADC = \\angle BAC$ है। दर्शाइए कि $CA^2 = CB \\cdot CD$ है। कौन से समरूप त्रिभुज यह परिणाम सिद्ध करते हैं?",
        "સ્વાધ્યાય 6.3 (Q13): ત્રિકોણ $ABC$ ની બાજુ $BC$ પર બિંદુ $D$ એવું આવેલું છે કે જેથી $\\angle ADC = \\angle BAC$ થાય. દર્શાવો કે $CA^2 = CB \\cdot CD$ છે. કયા સમરૂપ ત્રિકોણો આ પરિણામ સ્થાપિત કરે છે?",
        [
            "△BAC ~ △ADC by AA similarity (∠BAC = ∠ADC and common angle ∠C)",
            "△ABD ~ △CAD by SSS",
            "△ABC ~ △DBA by SAS",
            "△ADC ~ △ADB by RHS"
        ],
        [
            "AA समरूपता द्वारा △BAC ~ △ADC (∠BAC = ∠ADC और उभयनिष्ठ कोण ∠C)",
            "SSS द्वारा △ABD ~ △CAD",
            "SAS द्वारा △ABC ~ △DBA",
            "RHS द्वारा △ADC ~ △ADB"
        ],
        [
            "AA સમરૂપતા મુજબ △BAC ~ △ADC (∠BAC = ∠ADC અને સામાન્ય ખૂણો ∠C)",
            "બા-બા-બા મુજબ △ABD ~ △CAD",
            "બા-ખૂ-બા મુજબ △ABC ~ △DBA",
            "કા-ક-બા મુજબ △ADC ~ △ADB"
        ],
        0,
        "In △BAC and △ADC: 1. ∠BAC = ∠ADC (given). 2. ∠BCA = ∠ACD (common angle ∠C). By AA criterion, △BAC ~ △ADC. Proportional sides: CA / CD = CB / CA => CA × CA = CB × CD => CA² = CB · CD.",
        "△BAC और △ADC में: 1. ∠BAC = ∠ADC (दिया है)। 2. ∠BCA = ∠ACD (उभयनिष्ठ कोण ∠C)। AA कसौटी द्वारा △BAC ~ △ADC। संगत भुजाओं का अनुपात: CA / CD = CB / CA => CA × CA = CB × CD => CA² = CB · CD सिद्ध होता है।",
        "△BAC અને △ADC માં: 1. ∠BAC = ∠ADC (આપેલ છે). 2. ∠BCA = ∠ACD (સામાન્ય ખૂણો ∠C). AA શરત મુજબ △BAC ~ △ADC. અનુરૂપ બાજુઓનો ગુણોત્તર: CA / CD = CB / CA => CA × CA = CB × CD => CA² = CB · CD સાબિત થાય છે.",
        bloom="Apply",
        diff="Intermediate",
        mins=2
    ))

    # Exercise 6.3 Q14
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q14",
        "Exercise 6.3 (Q14): Sides $AB$ and $AC$ and median $AD$ of $\\triangle ABC$ are respectively proportional to sides $PQ$ and $PR$ and median $PM$ of another triangle $PQR$. To prove $\\triangle ABC \\sim \\triangle PQR$, which construction is performed?",
        "प्रश्नावली 6.3 (Q14): एक त्रिभुज $ABC$ की भुजाएँ $AB$ और $AC$ तथा माध्यिका $AD$ एक अन्य त्रिभुज $PQR$ की भुजाओं $PQ$ और $PR$ तथा माध्यिका $PM$ के क्रमशः समानुपाती हैं। $\\triangle ABC \\sim \\triangle PQR$ सिद्ध करने के लिए कौन सी रचना की जाती है?",
        "સ્વાધ્યાય 6.3 (Q14): ત્રિકોણ $ABC$ ની બાજુઓ $AB$ અને $AC$ તથા મધ્યગા $AD$, ત્રિકોણ $PQR$ ની અનુરૂપ બાજુઓ $PQ$ અને $PR$ તથા મધ્યગા $PM$ ના સમપ્રમાણમાં છે. $\\triangle ABC \\sim \\triangle PQR$ સાબિત કરવા માટે કઈ રચના કરવામાં આવે છે?",
        [
            "Extend AD to E such that AD = DE, and PM to N such that PM = MN (forming parallelograms)",
            "Draw altitudes from A and P to opposite sides",
            "Construct angle bisectors of ∠A and ∠P",
            "Draw circumcircles around both triangles"
        ],
        [
            "AD को E तक इस प्रकार बढ़ाएं कि AD = DE तथा PM को N तक इस प्रकार बढ़ाएं कि PM = MN (समांतर चतुर्भुज बनाना)",
            "A और P से सम्मुख भुजाओं पर शीर्षलम्ब खींचना",
            "∠A और ∠P के कोण समद्विभाजक खींचना",
            "दोनों त्रिभुजों के चारों ओर परिवृत्त बनाना"
        ],
        [
            "AD ને E સુધી એ રીતે લંબાવો કે જેથી AD = DE થાય અને PM ને N સુધી જેથી PM = MN થાય (સમાંતરબાજુ ચતુષ્કોણ રચવા)",
            "A અને P માંથી સામેની બાજુઓ પર વેધ દોરવા",
            "∠A અને ∠P ના કોણ દ્વિભાજક દોરવા",
            "બંને ત્રિકોણની આસપાસ પરિવૃત્ત દોરવા"
        ],
        0,
        "By extending AD to E (AD = DE) and PM to N (PM = MN), ABEC and PQNR become parallelograms where diagonals bisect each other. Proving △ABE ~ △PQN yields ∠BAD = ∠QPM, and △ACE ~ △PRN yields ∠CAD = ∠RPM. Adding gives ∠A = ∠P, proving △ABC ~ △PQR by SAS.",
        "AD को E तक (AD = DE) तथा PM को N तक (PM = MN) बढ़ाने पर ABEC और PQNR समांतर चतुर्भुज बन जाते हैं जिनके विकर्ण एक-दूसरे को समद्विभाजित करते हैं। △ABE ~ △PQN से ∠BAD = ∠QPM तथा △ACE ~ △PRN से ∠CAD = ∠RPM मिलता है। जोड़ने पर ∠A = ∠P प्राप्त होता है, जिससे SAS द्वारा △ABC ~ △PQR सिद्ध होता है।",
        "AD ને E સુધી (AD = DE) અને PM ને N સુધી (PM = MN) લંબાવવાથી ABEC અને PQNR સમાંતરબાજુ ચતુષ્કોણ બને છે જેના વિકર્ણો પરસ્પર દુભાગે છે. △ABE ~ △PQN પરથી ∠BAD = ∠QPM અને △ACE ~ △PRN પરથી ∠CAD = ∠RPM મળે છે. સરવાળો કરતા ∠A = ∠P મળે છે, જેથી બા-ખૂ-બા મુજબ △ABC ~ △PQR સાબિત થાય છે.",
        bloom="Analyze",
        diff="Advanced",
        mins=3
    ))

    # Exercise 6.3 Q15
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q15",
        "Exercise 6.3 (Q15): A vertical pole of length 6 m casts a shadow 4 m long on the ground and at the same time a tower casts a shadow 28 m long. Find the height of the tower.",
        "प्रश्नावली 6.3 (Q15): लंबाई 6 मीटर वाला एक ऊर्ध्वाधर स्तंभ भूमि पर 4 मीटर लंबी छाया बनाता है, जबकि उसी समय एक मीनार की छाया की लंबाई 28 मीटर है। मीनार की ऊँचाई ज्ञात कीजिए।",
        "સ્વાધ્યાય 6.3 (Q15): 6 મીટર લંબાઈવાળો એક શિરોલંબ થાંભલો જમીન પર 4 મીટર લાંબો પડછાયો પાડે છે, જ્યારે તે જ સમયે એક મિનારાનો પડછાયો 28 મીટર લાંબો છે. મિનારાની ઊંચાઈ શોધો.",
        ["42 m", "36 m", "48 m", "56 m"],
        ["42 मीटर", "36 मीटर", "48 मीटर", "56 मीटर"],
        ["42 મીટર", "36 મીટર", "48 મીટર", "56 મીટર"],
        0,
        "Sun rays strike at identical angle, so the pole triangle and tower triangle are similar by AA: Height of Tower / Height of Pole = Shadow of Tower / Shadow of Pole => H / 6 = 28 / 4 = 7 => H = 6 × 7 = 42 m.",
        "सूर्य की किरणें समान कोण पर पड़ती हैं, अतः खंभे का त्रिभुज और मीनार का त्रिभुज AA समरूपता द्वारा समरूप हैं: मीनार की ऊँचाई / खंभे की ऊँचाई = मीनार की छाया / खंभे की छाया => H / 6 = 28 / 4 = 7 => H = 6 × 7 = 42 मीटर।",
        "સૂર્યના કિરણો સમાન ખૂણે પડતા હોવાથી, થાંભલાનો ત્રિકોણ અને મિનારાનો ત્રિકોણ AA મુજબ સમરૂપ છે: મિનારાની ઊંચાઈ / થાંભલાની ઊંચાઈ = મિનારાનો પડછાયો / થાંભલાનો પડછાયો => H / 6 = 28 / 4 = 7 => H = 6 × 7 = 42 મીટર.",
        bloom="Apply",
        diff="Beginner",
        mins=2
    ))

    # Exercise 6.3 Q16
    blocks.append(make_quiz(
        "C10M_CH6_EX6.3_Q16",
        "Exercise 6.3 (Q16): If $AD$ and $PM$ are medians of triangles $ABC$ and $PQR$, respectively, where $\\triangle ABC \\sim \\triangle PQR$, prove that $\\frac{AB}{PQ} = \\frac{AD}{PM}$.",
        "प्रश्नावली 6.3 (Q16): यदि $AD$ और $PM$ क्रमशः त्रिभुजों $ABC$ और $PQR$ की माध्यिकाएँ हैं, जहाँ $\\triangle ABC \\sim \\triangle PQR$ है, तो सिद्ध कीजिए कि $\\frac{AB}{PQ} = \\frac{AD}{PM}$ है।",
        "સ્વાધ્યાય 6.3 (Q16): જો $AD$ અને $PM$ અનુક્રમે ત્રિકોણ $ABC$ અને $PQR$ ની મધ્યગાઓ હોય, જ્યાં $\\triangle ABC \\sim \\triangle PQR$ છે, તો સાબિત કરો કે $\\frac{AB}{PQ} = \\frac{AD}{PM}$ થાય.",
        [
            "△ABD ~ △PQM by SAS since AB/PQ = BD/QM and ∠B = ∠Q, giving AB/PQ = AD/PM",
            "Because AD = PM and AB = PQ",
            "By Pythagoras Theorem in both triangles",
            "Because medians are always equal to sides"
        ],
        [
            "SAS द्वारा △ABD ~ △PQM क्योंकि AB/PQ = BD/QM और ∠B = ∠Q, जिससे AB/PQ = AD/PM",
            "क्योंकि AD = PM और AB = PQ",
            "दोनों त्रिभुजों में पाइथागोरस प्रमेय द्वारा",
            "क्योंकि माध्यिकाएँ हमेशा भुजाओं के बराबर होती हैं"
        ],
        [
            "બા-ખૂ-બા મુજબ △ABD ~ △PQM કારણ કે AB/PQ = BD/QM અને ∠B = ∠Q, જેથી AB/PQ = AD/PM",
            "કારણ કે AD = PM અને AB = PQ",
            "બંને ત્રિકોણમાં પાયથાગોરસ પ્રમેય દ્વારા",
            "કારણ કે મધ્યગાઓ હંમેશા બાજુઓ જેટલી જ હોય છે"
        ],
        0,
        "Since △ABC ~ △PQR: AB / PQ = BC / QR = (2BD) / (2QM) = BD / QM and ∠B = ∠Q. In △ABD and △PQM: AB / PQ = BD / QM and ∠B = ∠Q. By SAS criterion, △ABD ~ △PQM => AB / PQ = AD / PM.",
        "चूँकि △ABC ~ △PQR है: AB / PQ = BC / QR = (2BD) / (2QM) = BD / QM तथा ∠B = ∠Q। △ABD और △PQM में: AB / PQ = BD / QM और ∠B = ∠Q। SAS कसौटी द्वारा △ABD ~ △PQM => AB / PQ = AD / PM सिद्ध होता है।",
        "△ABC ~ △PQR હોવાથી: AB / PQ = BC / QR = (2BD) / (2QM) = BD / QM અને ∠B = ∠Q. △ABD અને △PQM માં: AB / PQ = BD / QM અને ∠B = ∠Q. બા-ખૂ-બા શરત મુજબ △ABD ~ △PQM => AB / PQ = AD / PM સાબિત થાય છે.",
        bloom="Analyze",
        diff="Intermediate",
        mins=2
    ))

    return blocks

# =========================================================================
# PART 4: REFLECTION, CONNECTION, MASTERY & SUMMARY
# =========================================================================
def get_part4_blocks():
    blocks = []

    # Enrichment: Area Theorem & Pythagoras Theorem via Similarity
    blocks.append(make_theory(
        "C10M_CH6_17",
        "Enrichment Connection: Area Ratio & Pythagoras Proof via Similarity",
        "ज्ञान संवर्धन: समरूपता द्वारा क्षेत्रफल अनुपात और पाइथागोरस प्रमेय",
        "જ્ઞાન સંવર્ધન: સમરૂપતા દ્વારા ક્ષેત્રફળ ગુણોત્તર અને પાયથાગોરસ પ્રમેય",
        "### 1. Ratio of Areas of Similar Triangles:\nThe ratio of the areas of two similar triangles is equal to the **square** of the ratio of their corresponding sides:\n$$\\mathbf{\\frac{\\text{ar}(\\triangle ABC)}{\\text{ar}(\\triangle PQR)} = \\left(\\frac{AB}{PQ}\\right)^2 = \\left(\\frac{BC}{QR}\\right)^2 = \\left(\\frac{AC}{PR}\\right)^2}$$\n*Note:* If the side ratio is $1:3$, the area ratio is $1:9$!\n\n### 2. Pythagoras Theorem via Similarity:\nIn right $\\triangle ABC$ with $\\angle B = 90^\\circ$, draw altitude $BD \\perp AC$.\n- $\\triangle ADB \\sim \\triangle ABC \\implies \\frac{AD}{AB} = \\frac{AB}{AC} \\implies AB^2 = AD \\cdot AC$\n- $\\triangle BDC \\sim \\triangle ABC \\implies \\frac{CD}{BC} = \\frac{BC}{AC} \\implies BC^2 = CD \\cdot AC$\nAdding both equations:\n$$AB^2 + BC^2 = AC(AD + CD) = AC \\cdot AC = \\mathbf{AC^2}$$",
        "### 1. समरूप त्रिभुजों के क्षेत्रफलों का अनुपात:\nदो समरूप त्रिभुजों के क्षेत्रफलों का अनुपात उनकी संगत भुजाओं के अनुपात के **वर्ग** के बराबर होता है:\n$$\\mathbf{\\frac{\\text{ar}(\\triangle ABC)}{\\text{ar}(\\triangle PQR)} = \\left(\\frac{AB}{PQ}\\right)^2 = \\left(\\frac{BC}{QR}\\right)^2 = \\left(\\frac{AC}{PR}\\right)^2}$$\n*ध्यान दें:* यदि भुजाओं का अनुपात $1:3$ है, तो क्षेत्रफलों का अनुपात $1:9$ होगा!\n\n### 2. समरूपता द्वारा पाइथागोरस प्रमेय:\nसमकोण $\\triangle ABC$ (जहाँ $\\angle B = 90^\\circ$) में, शीर्षलम्ब $BD \\perp AC$ खींचें।\n- $\\triangle ADB \\sim \\triangle ABC \\implies \\frac{AD}{AB} = \\frac{AB}{AC} \\implies AB^2 = AD \\cdot AC$\n- $\\triangle BDC \\sim \\triangle ABC \\implies \\frac{CD}{BC} = \\frac{BC}{AC} \\implies BC^2 = CD \\cdot AC$\nदोनों समीकरणों को जोड़ने पर:\n$$AB^2 + BC^2 = AC(AD + CD) = AC \\cdot AC = \\mathbf{AC^2}$$",
        "### 1. સમરૂપ ત્રિકોણોના ક્ષેત્રફળોનો ગુણોત્તર:\nબે સમરૂપ ત્રિકોણોના ક્ષેત્રફળોનો ગુણોત્તર તેમની અનુરૂપ બાજુઓના ગુણોત્તરના **વર્ગ** જેટલો હોય છે:\n$$\\mathbf{\\frac{\\text{ar}(\\triangle ABC)}{\\text{ar}(\\triangle PQR)} = \\left(\\frac{AB}{PQ}\\right)^2 = \\left(\\frac{BC}{QR}\\right)^2 = \\left(\\frac{AC}{PR}\\right)^2}$$\n*નોંધ:* જો બાજુઓનો ગુણોત્તર $1:3$ હોય, તો ક્ષેત્રફળનો ગુણોત્તર $1:9$ થાય!\n\n### 2. સમરૂપતા દ્વારા પાયથાગોરસ પ્રમેય:\nકાટકોણ $\\triangle ABC$ (જ્યાં $\\angle B = 90^\\circ$) માં, વેધ $BD \\perp AC$ દોરો.\n- $\\triangle ADB \\sim \\triangle ABC \\implies \\frac{AD}{AB} = \\frac{AB}{AC} \\implies AB^2 = AD \\cdot AC$\n- $\\triangle BDC \\sim \\triangle ABC \\implies \\frac{CD}{BC} = \\frac{BC}{AC} \\implies BC^2 = CD \\cdot AC$\nબંને સમીકરણો ઉમેરતા:\n$$AB^2 + BC^2 = AC(AD + CD) = AC \\cdot AC = \\mathbf{AC^2}$$",
        btype="theory",
        bloom="Understand",
        diff="Intermediate",
        mins=4
    ))

    # Step 6: Reflection
    blocks.append(make_theory(
        "C10M_CH6_18",
        "Step 6: Socratic Reflection on Similarity & Real-World Scaling",
        "चरण 6: समरूपता और वास्तविक दुनिया के मापन पर सुकराती चिंतन",
        "પગલું 6: સમરૂપતા અને વાસ્તવિક દુનિયાના માપન પર સોક્રેટીક ચિંતન",
        "Consider a map of India printed at a scale of 1 : 10,000,000. \n- Is Gujarat on the map **similar** to Gujarat on the Earth's surface? Yes! Every coastal bend, highway intersection, and border angle matches the real world precisely.\n- What would happen if a cartographer scaled longitude by factor 2, but scaled latitude by factor 3? The map would stretch unnaturally, bending angles and distorting shapes—destroying similarity!\n\n**Key Takeaway:** True similarity requires a single, uniform scale factor $k$ across all directions. In nature and physics, similarity principles govern everything from acoustic horn designs and optical telescopes to how animals scale their bone strength!",
        "1 : 10,000,000 के पैमाने पर छपे भारत के मानचित्र पर विचार करें।\n- क्या मानचित्र पर गुजरात पृथ्वी की सतह पर स्थित गुजरात के **समरूप** है? हाँ! प्रत्येक तटीય मोड़, राजमार्ग प्रतिच्छेद और सीमा कोण वास्तविक दुनिया से बिल्कुल मेल खाते हैं।\n- क्या होगा यदि कोई मानचित्रकार देशांतर को 2 के गुणक से बड़ा करे, लेकिन अक्षांश को 3 के गुणक से बड़ा करे? मानचित्र अस्वाभाविक रूप से खिंच जाएगा, कोण बदल जाएंगे और आकार विकृत हो जाएगा—जिससे समरूपता समाप्त हो जाएगी!\n\n**प्रमुख सीख:** वास्तविक समरूपता के लिए सभी दिशाओं में एक समान स्केल गुणक $k$ होना अनिवार्य है। प्रकृति और भौतिकी में, समरूपता के सिद्धांत ध्वनि हॉर्न, ऑप्टिकल दूरबीनों से लेकर जानवरों की हड्डियों की ताकत तक सब कुछ नियंत्रित करते हैं!",
        "1 : 10,000,000 ના સ્કેલ પર છપાયેલા ભારતના નકશાનો વિચાર કરો.\n- શું નકશા પરનું ગુજરાત પૃથ્વીની સપાટી પરના વાસ્તવિક ગુજરાતને **સમરૂપ** છે? હા! દરેક દરિયાઈ વળાંક, હાઇવે ક્રોસિંગ અને સરહદનો ખૂણો વાસ્તવિક દુનિયા સાથે ચોક્કસ મેળ ખાય છે.\n- જો કોઈ નકશાકાર રેખાંશને 2 ના ગુણકથી મોટો કરે અને અક્ષાંશને 3 ના ગુણકથી મોટો કરે તો શું થાય? નકશો વિકૃત થઈ જશે, ખૂણા બદલાઈ જશે અને આકાર ખેંચાઈ જશે—સમરૂપતા નાશ પામશે!\n\n**મુખ્ય શીખ:** સાચી સમરૂપતા માટે બધી દિશાઓમાં એક જ સમાન સ્કેલ ગુણક $k$ હોવો જરૂરી છે. કુદરત અને ભૌતિકશાસ્ત્રમાં, અવાજના હોર્ન, ટેલિસ્કોપથી લઈને પ્રાણીઓના હાડકાંની મજબૂતી સુધી બધું જ સમરૂપતાના સિદ્ધાંતો પર નિર્ભર છે!",
        btype="reflection",
        bloom="Evaluate",
        diff="Intermediate",
        mins=3
    ))

    # Step 7: Connection to Trigonometry
    blocks.append(make_theory(
        "C10M_CH6_19",
        "Step 7: Knowledge Graph Connection to Trigonometry",
        "चरण 7: त्रिकोणमिति के साथ ज्ञान ग्राफ (Knowledge Graph) जुड़ाव",
        "પગલું 7: ત્રિકોણમિતિ સાથે નોલેજ ગ્રાફ જોડાણ",
        "Why does $\\sin 30^\\circ$ always equal $\\frac{1}{2}$, whether the triangle is microscopic inside a silicon chip or as vast as the orbit of the Moon?\n\nThe answer is **Triangle Similarity (AA Criterion)**!\nAny two right-angled triangles with an acute angle of $30^\\circ$ share angles $90^\\circ, 30^\\circ, 60^\\circ$. By AA similarity, they are strictly similar! Consequently, the ratio of the side opposite $30^\\circ$ to the hypotenuse is mathematically locked at $1 : 2$, independent of side lengths!\n\nWithout Chapter 6 (Triangles), Chapter 8 (Introduction to Trigonometry) could not exist! Trigonometry is simply the study of ratios in similar right triangles.",
        "चाहे त्रिभुज सिलिकॉन चिप के अंदर सूक्ष्म हो या चंद्रमा की कक्षा जितना विशाल, $\\sin 30^\\circ$ का मान हमेशा $\\frac{1}{2}$ ही क्यों होता है?\n\nइसका उत्तर है **त्रिभुज समरूपता (AA कसौटी)**!\n$30^\\circ$ न्यूनकोण वाले किन्हीं भी दो समकोण त्रिभुजों के कोण $90^\\circ, 30^\\circ, 60^\\circ$ होते हैं। AA समरूपता द्वारा वे अनिवार्य रूप से समरूप होते हैं! परिणामस्वरूप, $30^\\circ$ के सम्मुख भुजा और कर्ण का अनुपात हमेशा $1 : 2$ ही रहता है, चाहे भुजाएँ कितनी भी लंबी क्यों न हों!\n\nअध्याय 6 (त्रिभुज) के बिना अध्याय 8 (त्रिकोणमिति का परिचय) का अस्तित्व ही संभव नहीं था! त्रिकोणमिति वास्तव में समरूप समकोण त्रिभुजों के अनुपातों का ही अध्ययन है।",
        "ભલે ત્રિકોણ સિલિકોન ચિપમાં અતિસૂક્ષ્મ હોય કે ચંદ્રની ભ્રમણકક્ષા જેટલો વિશાળ હોય, $\\sin 30^\\circ$ નું મૂલ્ય હંમેશા $\\frac{1}{2}$ કેમ રહે છે?\n\nતેનો જવાબ છે **ત્રિકોણ સમરૂપતા (AA શરત)**!\n$30^\\circ$ લઘુકોણવાળા કોઈપણ બે કાટકોણ ત્રિકોણના ખૂણા $90^\\circ, 30^\\circ, 60^\\circ$ હોય છે. AA સમરૂપતા મુજબ તેઓ સંપૂર્ણપણે સમરૂપ છે! પરિણામે, $30^\\circ$ ની સામેની બાજુ અને કર્ણનો ગુણોત્તર બાજુઓની લંબાઈ ગમે તે હોય તો પણ હંમેશા $1 : 2$ જ રહે છે!\n\nપ્રકરણ 6 (ત્રિકોણ) વગર પ્રકરણ 8 (ત્રિકોણમિતિનો પરિચય) શક્ય જ નથી! ત્રિકોણમિતિ એ વાસ્તવમાં સમરૂપ કાટકોણ ત્રિકોણના ગુણોત્તરોનો જ અભ્યાસ છે.",
        btype="connection",
        bloom="Analyze",
        diff="Intermediate",
        mins=3
    ))

    # Step 8: Mastery Challenge
    blocks.append(make_quiz(
        "C10M_CH6_20",
        "Step 8 (Mastery Challenge): In $\\triangle ABC$, line $DE \\parallel BC$ cuts $AB$ at $D$ and $AC$ at $E$. If $AD = x, DB = x - 2, AE = x + 2$, and $EC = x - 1$, find the value of $x$.",
        "चरण 8 (महारत चुनौती): $\\triangle ABC$ में, रेखा $DE \\parallel BC$ भुजा $AB$ को $D$ पर तथा $AC$ को $E$ पर काटती है। यदि $AD = x, DB = x - 2, AE = x + 2$ और $EC = x - 1$ हो, तो $x$ का मान ज्ञात कीजिए।",
        "પગલું 8 (માસ્ટરી ચેલેન્જ): $\\triangle ABC$ માં, રેખા $DE \\parallel BC$ એ બાજુ $AB$ ને $D$ માં અને $AC$ ને $E$ માં છેદે છે. જો $AD = x, DB = x - 2, AE = x + 2$ અને $EC = x - 1$ હોય, તો $x$ નું મૂલ્ય શોધો.",
        ["x = 4", "x = 3", "x = 5", "x = 2"],
        ["x = 4", "x = 3", "x = 5", "x = 2"],
        ["x = 4", "x = 3", "x = 5", "x = 2"],
        0,
        "By Basic Proportionality Theorem: AD / DB = AE / EC => x / (x - 2) = (x + 2) / (x - 1). Cross multiplying: x(x - 1) = (x - 2)(x + 2) => x² - x = x² - 4 => -x = -4 => x = 4.",
        "आधारभूत आनुपातिकता प्रमेय (BPT) द्वारा: AD / DB = AE / EC => x / (x - 2) = (x + 2) / (x - 1)। वज्र गुणन करने पर: x(x - 1) = (x - 2)(x + 2) => x² - x = x² - 4 => -x = -4 => x = 4।",
        "સમપ્રમાણતાના મૂળભૂત પ્રમેય મુજબ: AD / DB = AE / EC => x / (x - 2) = (x + 2) / (x - 1). ચોકડી ગુણાકાર કરતા: x(x - 1) = (x - 2)(x + 2) => x² - x = x² - 4 => -x = -4 => x = 4.",
        bloom="Evaluate",
        diff="Advanced",
        mins=3
    ))

    # Summary: Triangles Cheat Sheet
    blocks.append(make_theory(
        "C10M_CH6_21",
        "Chapter 6 Summary: The Triangles Quick Revision Guide",
        "अध्याय 6 सारांश: त्रिभुज त्वरित पुनरावृत्ति मार्गदर्शिका",
        "પ્રકરણ 6 સારાંશ: ત્રિકોણ ઝડપી પુનરાવર્તન માર્ગદર્શિકા",
        "### Key Principles of Chapter 6 (Triangles):\n\n1. **Similar Figures:** Same shape, not necessarily same size. All congruent figures are similar, but converse is not true.\n2. **Polygon Similarity:** Requires BOTH: (i) corresponding angles equal, and (ii) corresponding sides proportional.\n3. **Basic Proportionality Theorem (BPT / Thales Theorem):** In $\\triangle ABC$, if $DE \\parallel BC$, then $\\frac{AD}{DB} = \\frac{AE}{EC}$ and $\\frac{AD}{AB} = \\frac{AE}{AC}$.\n4. **Converse of BPT:** If $\\frac{AD}{DB} = \\frac{AE}{EC}$, then $DE \\parallel BC$.\n5. **AAA / AA Criterion:** If two angles of one triangle equal two angles of another, the triangles are similar.\n6. **SSS Criterion:** If three sides of one triangle are proportional to three sides of another, they are similar.\n7. **SAS Criterion:** If two pairs of sides are proportional and their **included angles** are equal, they are similar.",
        "### अध्याय 6 (त्रिभुज) के मुख्य सिद्धांत:\n\n1. **समरूप आकृतियाँ:** आकार समान, माप समान होना आवश्यक नहीं। सभी सर्वांगसम आकृतियाँ समरूप होती हैं, परंतु विलोम सत्य नहीं है।\n2. **बहुभुज समरूपता:** दोनों शर्तें आवश्यक हैं: (i) संगत कोण बराबर हों, और (ii) संगत भुजाएँ समानुपाती हों।\n3. **आधारभूत आनुपातिकता प्रमेय (BPT / थेल्स प्रमेय):** $\\triangle ABC$ में, यदि $DE \\parallel BC$ हो, तो $\\frac{AD}{DB} = \\frac{AE}{EC}$ तथा $\\frac{AD}{AB} = \\frac{AE}{AC}$।\n4. **BPT का विलोम:** यदि $\\frac{AD}{DB} = \\frac{AE}{EC}$ हो, तो $DE \\parallel BC$।\n5. **AAA / AA कसौटी:** यदि एक त्रिभुज के दो कोण दूसरे त्रिभुज के दो कोणों के बराबर हों, तो दोनों त्रिभुज समरूप होते हैं।\n6. **SSS कसौटी:** यदि एक त्रिभुज की तीनों भुजाएँ दूसरे त्रिभुज की तीनों भुजाओं के समानुपाती हों, तो वे समरूप होते हैं।\n7. **SAS कसौटी:** यदि दो भुजाएँ समानुपाती हों और उनके **अंतर्गत कोण** बराबर हों, तो वे समरूप होते हैं।",
        "### પ્રકરણ 6 (ત્રિકોણ) ના મુખ્ય સિદ્ધાંતો:\n\n1. **સમરૂપ આકૃતિઓ:** સમાન આકાર, કદ સમાન હોવું જરૂરી નથી. બધી એકરૂપ આકૃતિઓ સમરૂપ છે, પરંતુ પ્રતીપ સાચું નથી.\n2. **બહુકોણ સમરૂપતા:** બંને શરતો જરૂરી: (i) અનુરૂપ ખૂણાઓ સમાન હોય, અને (ii) અનુરૂપ બાજુઓ સમપ્રમાણમાં હોય.\n3. **સમપ્રમાણતાનું મૂળભૂત પ્રમેય (BPT / થેલ્સનું પ્રમેય):** $\\triangle ABC$ માં, જો $DE \\parallel BC$ હોય, તો $\\frac{AD}{DB} = \\frac{AE}{EC}$ અને $\\frac{AD}{AB} = \\frac{AE}{AC}$.\n4. **BPT નું પ્રતીપ:** જો $\\frac{AD}{DB} = \\frac{AE}{EC}$ હોય, તો $DE \\parallel BC$.\n5. **AAA / AA શરત:** જો એક ત્રિકોણના બે ખૂણા બીજા ત્રિકોણના બે ખૂણાઓને સમાન હોય, તો બંને ત્રિકોણો સમરૂપ થાય.\n6. **SSS શરત:** જો ત્રણેય બાજુઓ સમપ્રમાણમાં હોય, તો ત્રિકોણો સમરૂપ થાય.\n7. **SAS શરત:** જો બે બાજુઓ સમપ્રમાણમાં હોય અને તેમના **અંતર્ગત ખૂણા** સમાન હોય, તો ત્રિકોણો સમરૂપ થાય.",
        btype="summary",
        bloom="Remember",
        diff="Beginner",
        mins=3
    ))

    return blocks

def generate_chapter():
    all_blocks = []
    all_blocks.extend(get_part1_blocks())
    all_blocks.extend(get_part2_blocks())
    all_blocks.extend(get_part3_blocks())
    all_blocks.extend(get_part4_blocks())

    chapter_data = {
        "metadata": get_metadata(),
        "blocks": all_blocks
    }

    out_dir = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters"
    os.makedirs(out_dir, exist_ok=True)
    out_file = os.path.join(out_dir, "ncert_class10_maths_ch6.json")

    with open(out_file, "w", encoding="utf-8") as f:
        json.dump(chapter_data, f, indent=2, ensure_ascii=False)

    print(f"Generated {out_file} successfully with {len(chapter_data['blocks'])} blocks!")

    # Synchronize GSEB equivalent since Class 10 Maths is identical
    gseb_file = os.path.join(out_dir, "gseb_class10_maths_ch6.json")
    chapter_data_gseb = json.loads(json.dumps(chapter_data))
    chapter_data_gseb["metadata"]["id"] = "gseb_class10_maths_ch6"
    with open(gseb_file, "w", encoding="utf-8") as f:
        json.dump(chapter_data_gseb, f, indent=2, ensure_ascii=False)
    print(f"Synchronized {gseb_file} successfully!")

if __name__ == "__main__":
    generate_chapter()
