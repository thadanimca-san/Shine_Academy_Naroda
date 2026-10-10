# Hindi / Gujarati for Class 10 Maths Ch 8 questions.json
from tr_ch04_common import by_option, feedback, steps, _ITEMS

Q = {}
def add(key, question=None, step_overrides=None, **fields):
    iid = f"ch08.q.{key}"
    if question: Q[f"{iid}.question"] = question
    if step_overrides is not None: Q[f"{iid}.answer_steps"] = steps(iid, step_overrides)
    for f, v in fields.items(): Q[f"{iid}.{f}"] = v

TF = ("बताइए कि निम्नलिखित सत्य है या असत्य। अपने उत्तर का औचित्य दीजिए। ", "નીચેનું વિધાન સાચું છે કે ખોટું તે જણાવો. તમારા જવાબનું કારણ આપો. ")
def tf(key, stmt, expl):
    iid = f"ch08.q.{key}"
    item = _ITEMS[iid]
    Q[f"{iid}.question"] = (TF[0] + stmt[0], TF[1] + stmt[1])
    Q[f"{iid}.explanation"] = expl
    Q[f"{iid}.options"] = by_option(iid, {"True": ("सत्य", "સાચું"), "False": ("असत्य", "ખોટું")})
    right = item["options"][item["correct_index"]]
    Q[f"{iid}.option_feedback"] = ([("सही! " if o == right else "पूरी तरह नहीं। ") + expl[0] for o in item["options"]],
                                   [("સાચું! " if o == right else "બરાબર નથી. ") + expl[1] for o in item["options"]])

# Exercise 8.1
add("ex8_1.q1", ("$B$ पर समकोण वाले $\\triangle ABC$ में $AB = 24$ cm और $BC = 7$ cm है। ज्ञात कीजिए: (i) $\\sin A$, $\\cos A$ (ii) $\\sin C$, $\\cos C$", "$B$ આગળ કાટખૂણાવાળા $\\triangle ABC$ માં $AB = 24$ cm અને $BC = 7$ cm છે. શોધો: (i) $\\sin A$, $\\cos A$ (ii) $\\sin C$, $\\cos C$"))
Q["ch08.q.ex8_1.q1.figure.title"] = ("AB = 24 cm, BC = 7 cm", "AB = 24 cm, BC = 7 cm")
add("ex8_1.q2", ("$Q$ पर समकोण वाले $\\triangle PQR$ में $PQ = 12$ cm और $PR = 13$ cm है। $\\tan P - \\cot R$ का मान ज्ञात कीजिए।", "$Q$ આગળ કાટખૂણાવાળા $\\triangle PQR$ માં $PQ = 12$ cm અને $PR = 13$ cm છે. $\\tan P - \\cot R$ ની કિંમત શોધો."),
    {0: ("$QR = \\sqrt{13^{2} - 12^{2}} = 5$ cm, अतः $\\tan P = \\dfrac{QR}{PQ} = \\dfrac{5}{12}$ और $\\cot R = \\dfrac{QR}{PQ} = \\dfrac{5}{12}$।", "$QR = \\sqrt{13^{2} - 12^{2}} = 5$ cm, તેથી $\\tan P = \\dfrac{QR}{PQ} = \\dfrac{5}{12}$ અને $\\cot R = \\dfrac{QR}{PQ} = \\dfrac{5}{12}$.")})
Q["ch08.q.ex8_1.q2.figure.title"] = ("PQ = 12 cm, PR = 13 cm", "PQ = 12 cm, PR = 13 cm")
add("ex8_1.q3", ("यदि $\\sin A = \\dfrac{3}{4}$ है, तो $\\cos A$ और $\\tan A$ का मान परिकलित कीजिए।", "જો $\\sin A = \\dfrac{3}{4}$ હોય, તો $\\cos A$ અને $\\tan A$ ની કિંમત ગણો."),
    {0: ("सम्मुख $= 3k$, कर्ण $= 4k$, अतः संलग्न $= \\sqrt{16k^{2} - 9k^{2}} = \\sqrt{7}k$।", "સામેની બાજુ $= 3k$, કર્ણ $= 4k$, તેથી પાસેની બાજુ $= \\sqrt{16k^{2} - 9k^{2}} = \\sqrt{7}k$.")})
add("ex8_1.q4", ("यदि $15\\cot A = 8$ है, तो $\\sin A$ और $\\sec A$ ज्ञात कीजिए।", "જો $15\\cot A = 8$ હોય, તો $\\sin A$ અને $\\sec A$ શોધો."),
    {0: ("$\\cot A = \\dfrac{8}{15}$: संलग्न $= 8k$, सम्मुख $= 15k$, कर्ण $= 17k$।", "$\\cot A = \\dfrac{8}{15}$: પાસેની બાજુ $= 8k$, સામેની બાજુ $= 15k$, કર્ણ $= 17k$.")})
add("ex8_1.q5", ("यदि $\\sec \\theta = \\dfrac{13}{12}$ है, तो अन्य सभी त्रिकोणमितीय अनुपात परिकलित कीजिए।", "જો $\\sec \\theta = \\dfrac{13}{12}$ હોય, તો બાકીના બધા ત્રિકોણમિતીય ગુણોત્તર ગણો."),
    {0: ("कर्ण $= 13k$, संलग्न $= 12k$, अतः सम्मुख $= 5k$।", "કર્ણ $= 13k$, પાસેની બાજુ $= 12k$, તેથી સામેની બાજુ $= 5k$.")})
add("ex8_1.q6", ("यदि $\\angle A$ और $\\angle B$ ऐसे न्यून कोण हों कि $\\cos A = \\cos B$, तो दर्शाइए कि $\\angle A = \\angle B$।", "જો $\\angle A$ અને $\\angle B$ એવા લઘુકોણ હોય કે $\\cos A = \\cos B$, તો બતાવો કે $\\angle A = \\angle B$."),
    {0: ("समकोण त्रिभुज $PQR$ ($Q$ पर समकोण, $\\angle P = A$) और $XYZ$ ($Y$ पर समकोण, $\\angle X = B$) लीजिए।", "કાટકોણ ત્રિકોણ $PQR$ ($Q$ આગળ કાટખૂણો, $\\angle P = A$) અને $XYZ$ ($Y$ આગળ કાટખૂણો, $\\angle X = B$) લો."),
     1: ("$\\cos A = \\cos B$ से $\\dfrac{PQ}{PR} = \\dfrac{XY}{XZ}$, अर्थात् $\\dfrac{PQ}{XY} = \\dfrac{PR}{XZ} = k$।", "$\\cos A = \\cos B$ પરથી $\\dfrac{PQ}{PR} = \\dfrac{XY}{XZ}$, એટલે કે $\\dfrac{PQ}{XY} = \\dfrac{PR}{XZ} = k$."),
     2: ("तब $QR = \\sqrt{PR^{2} - PQ^{2}} = k\\sqrt{XZ^{2} - XY^{2}} = k \\cdot YZ$, अतः त्रिभुज समरूप हैं (SSS) और $\\angle A = \\angle B$।", "તો $QR = \\sqrt{PR^{2} - PQ^{2}} = k\\sqrt{XZ^{2} - XY^{2}} = k \\cdot YZ$, તેથી ત્રિકોણ સમરૂપ છે (બાબાબા) અને $\\angle A = \\angle B$.")})
add("ex8_1.q7", ("यदि $\\cot \\theta = \\dfrac{7}{8}$ है, तो मान निकालिए: (i) $\\dfrac{(1 + \\sin \\theta)(1 - \\sin \\theta)}{(1 + \\cos \\theta)(1 - \\cos \\theta)}$ (ii) $\\cot^{2} \\theta$",
                 "જો $\\cot \\theta = \\dfrac{7}{8}$ હોય, તો કિંમત શોધો: (i) $\\dfrac{(1 + \\sin \\theta)(1 - \\sin \\theta)}{(1 + \\cos \\theta)(1 - \\cos \\theta)}$ (ii) $\\cot^{2} \\theta$"))
add("ex8_1.q8", ("यदि $3\\cot A = 4$ है, तो जाँच कीजिए कि $\\dfrac{1 - \\tan^{2} A}{1 + \\tan^{2} A} = \\cos^{2} A - \\sin^{2} A$ है या नहीं।", "જો $3\\cot A = 4$ હોય, તો ચકાસો કે $\\dfrac{1 - \\tan^{2} A}{1 + \\tan^{2} A} = \\cos^{2} A - \\sin^{2} A$ છે કે નહિ."),
    {0: ("$\\cot A = \\dfrac{4}{3}$, अतः $\\tan A = \\dfrac{3}{4}$, $\\sin A = \\dfrac{3}{5}$, $\\cos A = \\dfrac{4}{5}$।", "$\\cot A = \\dfrac{4}{3}$, તેથી $\\tan A = \\dfrac{3}{4}$, $\\sin A = \\dfrac{3}{5}$, $\\cos A = \\dfrac{4}{5}$."),
     1: ("बायाँ पक्ष $= \\dfrac{1 - \\frac{9}{16}}{1 + \\frac{9}{16}} = \\dfrac{7}{25}$; दायाँ पक्ष $= \\dfrac{16}{25} - \\dfrac{9}{25} = \\dfrac{7}{25}$।", "ડા.બા. $= \\dfrac{1 - \\frac{9}{16}}{1 + \\frac{9}{16}} = \\dfrac{7}{25}$; જ.બા. $= \\dfrac{16}{25} - \\dfrac{9}{25} = \\dfrac{7}{25}$."),
     2: ("बायाँ पक्ष $=$ दायाँ पक्ष, अतः यह सत्य है।", "ડા.બા. $=$ જ.બા., તેથી તે સાચું છે.")})
add("ex8_1.q9", ("$B$ पर समकोण वाले $\\triangle ABC$ में यदि $\\tan A = \\dfrac{1}{\\sqrt{3}}$ है, तो निम्नलिखित के मान ज्ञात कीजिए: (i) $\\sin A \\cos C + \\cos A \\sin C$ (ii) $\\cos A \\cos C - \\sin A \\sin C$",
                 "$B$ આગળ કાટખૂણાવાળા $\\triangle ABC$ માં જો $\\tan A = \\dfrac{1}{\\sqrt{3}}$ હોય, તો નીચેનાની કિંમત શોધો: (i) $\\sin A \\cos C + \\cos A \\sin C$ (ii) $\\cos A \\cos C - \\sin A \\sin C$"),
    {0: ("$\\tan A = \\dfrac{1}{\\sqrt{3}}$: $BC = k$, $AB = \\sqrt{3}k$, $AC = 2k$। अतः $\\sin A = \\cos C = \\dfrac{1}{2}$ और $\\cos A = \\sin C = \\dfrac{\\sqrt{3}}{2}$।", "$\\tan A = \\dfrac{1}{\\sqrt{3}}$: $BC = k$, $AB = \\sqrt{3}k$, $AC = 2k$. તેથી $\\sin A = \\cos C = \\dfrac{1}{2}$ અને $\\cos A = \\sin C = \\dfrac{\\sqrt{3}}{2}$.")})
add("ex8_1.q10", ("$Q$ पर समकोण वाले $\\triangle PQR$ में $PR + QR = 25$ cm और $PQ = 5$ cm है। $\\sin P$, $\\cos P$ और $\\tan P$ के मान ज्ञात कीजिए।", "$Q$ આગળ કાટખૂણાવાળા $\\triangle PQR$ માં $PR + QR = 25$ cm અને $PQ = 5$ cm છે. $\\sin P$, $\\cos P$ અને $\\tan P$ ની કિંમત શોધો."),
    {0: ("$PR^{2} - QR^{2} = PQ^{2} = 25$, अतः $(PR - QR)(PR + QR) = 25$ और $PR - QR = 1$।", "$PR^{2} - QR^{2} = PQ^{2} = 25$, તેથી $(PR - QR)(PR + QR) = 25$ અને $PR - QR = 1$."),
     1: ("अतः $PR = 13$ cm और $QR = 12$ cm।", "તેથી $PR = 13$ cm અને $QR = 12$ cm.")})
tf("ex8_1.q11.i", ("$\\tan A$ का मान सदैव 1 से कम होता है।", "$\\tan A$ ની કિંમત હંમેશાં 1 કરતાં ઓછી હોય છે."), ("असत्य: $\\tan 60^\\circ = \\sqrt{3} > 1$।", "ખોટું: $\\tan 60^\\circ = \\sqrt{3} > 1$."))
tf("ex8_1.q11.ii", ("कोण $A$ के किसी मान के लिए $\\sec A = \\dfrac{12}{5}$।", "ખૂણા $A$ ની કોઈ કિંમત માટે $\\sec A = \\dfrac{12}{5}$."),
   ("सत्य: $\\sec A = \\dfrac{\\text{hypotenuse}}{\\text{adjacent}}$, $\\dfrac{12}{5}$ हो सकता है, क्योंकि कर्ण सबसे लंबी भुजा है (जैसे भुजाएँ 5, $\\sqrt{119}$, 12)।", "સાચું: $\\sec A = \\dfrac{\\text{hypotenuse}}{\\text{adjacent}}$, $\\dfrac{12}{5}$ હોઈ શકે, કારણ કે કર્ણ સૌથી લાંબી બાજુ છે (જેમ કે બાજુઓ 5, $\\sqrt{119}$, 12)."))
tf("ex8_1.q11.iii", ("$\\cos A$, कोण $A$ के कोसीकेंट के लिए प्रयुक्त एक संक्षिप्त रूप है।", "$\\cos A$ એ ખૂણા $A$ ના કોસીકન્ટ માટે વપરાતું ટૂંકું રૂપ છે."),
   ("असत्य: $\\cos A$, $A$ का कोसाइन है; कोसीकेंट $\\text{cosec } A$ लिखा जाता है।", "ખોટું: $\\cos A$ એ $A$ નો કોસાઇન છે; કોસીકન્ટ $\\text{cosec } A$ લખાય છે."))
tf("ex8_1.q11.iv", ("$\\cot A$, $\\cot$ और $A$ का गुणनफल है।", "$\\cot A$ એ $\\cot$ અને $A$ નો ગુણાકાર છે."), ("असत्य: $\\cot A$ एक संख्या है, कोण $A$ का कोटैंजेंट।", "ખોટું: $\\cot A$ એક સંખ્યા છે, ખૂણા $A$ નો કોટેન્જન્ટ."))
tf("ex8_1.q11.v", ("किसी भी कोण $\\theta$ के लिए $\\sin \\theta = \\dfrac{4}{3}$।", "કોઈ ખૂણા $\\theta$ માટે $\\sin \\theta = \\dfrac{4}{3}$."),
   ("असत्य: $\\sin \\theta = \\dfrac{\\text{opposite}}{\\text{hypotenuse}}$ कभी 1 से अधिक नहीं होता।", "ખોટું: $\\sin \\theta = \\dfrac{\\text{opposite}}{\\text{hypotenuse}}$ ક્યારેય 1 કરતાં વધુ હોતો નથી."))
# Exercise 8.2
for p in ("i", "ii", "iii", "iv", "v"):
    pass  # questions use the shared "Evaluate:" template
add("ex8_2.q2.i", None, None, option_feedback=feedback("ch08.q.ex8_2.q2.i", {
  "$\\sin 60^\\circ$": ("सही! मान $\\dfrac{\\sqrt{3}}{2}$ है।", "સાચું! કિંમત $\\dfrac{\\sqrt{3}}{2}$ છે."), "$\\cos 60^\\circ$": ("मान $\\dfrac{\\sqrt{3}}{2}$ है, पर $\\cos 60^\\circ = \\dfrac{1}{2}$।", "કિંમત $\\dfrac{\\sqrt{3}}{2}$ છે, પણ $\\cos 60^\\circ = \\dfrac{1}{2}$."),
  "$\\tan 60^\\circ$": ("यह $\\dfrac{2\\tan 30^\\circ}{1 - \\tan^{2} 30^\\circ}$ है, ऋण चिह्न के साथ।", "આ $\\dfrac{2\\tan 30^\\circ}{1 - \\tan^{2} 30^\\circ}$ છે, ઓછાની નિશાની સાથે."), "$\\sin 30^\\circ$": ("$\\sin 30^\\circ = \\dfrac{1}{2}$, पर मान $\\dfrac{\\sqrt{3}}{2}$ है।", "$\\sin 30^\\circ = \\dfrac{1}{2}$, પણ કિંમત $\\dfrac{\\sqrt{3}}{2}$ છે.")}))
add("ex8_2.q2.ii", None, None, option_feedback=feedback("ch08.q.ex8_2.q2.ii", {
  "$\\tan 90^\\circ$": ("$\\tan 90^\\circ$ परिभाषित नहीं है, पर यहाँ मान 0 है।", "$\\tan 90^\\circ$ વ્યાખ્યાયિત નથી, પણ અહીં કિંમત 0 છે."), "$1$": ("अंश $1 - 1 = 0$ है।", "અંશ $1 - 1 = 0$ છે."),
  "$\\sin 45^\\circ$": ("अंश 0 है, अतः मान 0 है।", "અંશ 0 છે, તેથી કિંમત 0 છે."), "$0$": ("सही! $\\dfrac{1 - 1}{1 + 1} = 0$।", "સાચું! $\\dfrac{1 - 1}{1 + 1} = 0$.")}))
add("ex8_2.q2.iii", ("$\\sin 2A = 2\\sin A$ तब सत्य होता है जबकि $A$ बराबर है", "$\\sin 2A = 2\\sin A$ ત્યારે સાચું છે જ્યારે $A$ બરાબર"),
    explanation=("$A = 0^\\circ$ पर दोनों पक्ष 0 हैं; अन्य कोणों के लिए वे अलग हैं।", "$A = 0^\\circ$ પર બંને બાજુ 0 છે; બાકીના ખૂણા માટે તે જુદી છે."),
    option_feedback=feedback("ch08.q.ex8_2.q2.iii", {
  "$0^\\circ$": ("सही! दोनों पक्ष 0 हैं।", "સાચું! બંને બાજુ 0 છે."), "$30^\\circ$": ("$\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$ पर $2\\sin 30^\\circ = 1$।", "$\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$ પણ $2\\sin 30^\\circ = 1$."),
  "$45^\\circ$": ("$\\sin 90^\\circ = 1$ पर $2\\sin 45^\\circ = \\sqrt{2}$।", "$\\sin 90^\\circ = 1$ પણ $2\\sin 45^\\circ = \\sqrt{2}$."), "$60^\\circ$": ("$\\sin 120^\\circ \\neq 2\\sin 60^\\circ = \\sqrt{3}$, जो 1 से अधिक है।", "$\\sin 120^\\circ \\neq 2\\sin 60^\\circ = \\sqrt{3}$, જે 1 કરતાં વધુ છે.")}))
add("ex8_2.q2.iv", None, None, option_feedback=feedback("ch08.q.ex8_2.q2.iv", {
  "$\\cos 60^\\circ$": ("मान $\\sqrt{3}$ है, पर $\\cos 60^\\circ = \\dfrac{1}{2}$।", "કિંમત $\\sqrt{3}$ છે, પણ $\\cos 60^\\circ = \\dfrac{1}{2}$."), "$\\sin 60^\\circ$": ("यह हर में धन चिह्न वाला उत्तर है।", "આ છેદમાં સરવાળાની નિશાનીવાળો જવાબ છે."),
  "$\\tan 60^\\circ$": ("सही! मान $\\sqrt{3}$ है।", "સાચું! કિંમત $\\sqrt{3}$ છે."), "$\\sin 30^\\circ$": ("मान $\\sqrt{3}$ है, पर $\\sin 30^\\circ = \\dfrac{1}{2}$।", "કિંમત $\\sqrt{3}$ છે, પણ $\\sin 30^\\circ = \\dfrac{1}{2}$.")}))
add("ex8_2.q3", ("यदि $\\tan(A + B) = \\sqrt{3}$ और $\\tan(A - B) = \\dfrac{1}{\\sqrt{3}}$; $0^\\circ < A + B \\leq 90^\\circ$; $A > B$ है, तो $A$ और $B$ ज्ञात कीजिए।",
                 "જો $\\tan(A + B) = \\sqrt{3}$ અને $\\tan(A - B) = \\dfrac{1}{\\sqrt{3}}$; $0^\\circ < A + B \\leq 90^\\circ$; $A > B$ હોય, તો $A$ અને $B$ શોધો."))
tf("ex8_2.q4.i", ("$\\sin(A + B) = \\sin A + \\sin B$ है।", "$\\sin(A + B) = \\sin A + \\sin B$ છે."), ("असत्य: $A = B = 30^\\circ$ लेने पर $\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$ पर $\\sin 30^\\circ + \\sin 30^\\circ = 1$।", "ખોટું: $A = B = 30^\\circ$ લેતાં $\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$ પણ $\\sin 30^\\circ + \\sin 30^\\circ = 1$."))
tf("ex8_2.q4.ii", ("$\\theta$ में वृद्धि होने पर $\\sin \\theta$ का मान भी बढ़ता है ($0^\\circ$ से $90^\\circ$ तक)।", "$\\theta$ વધે તેમ $\\sin \\theta$ ની કિંમત પણ વધે છે ($0^\\circ$ થી $90^\\circ$ સુધી)."),
   ("सत्य: $0, \\dfrac{1}{2}, \\dfrac{1}{\\sqrt{2}}, \\dfrac{\\sqrt{3}}{2}, 1$ बढ़ते हैं।", "સાચું: $0, \\dfrac{1}{2}, \\dfrac{1}{\\sqrt{2}}, \\dfrac{\\sqrt{3}}{2}, 1$ વધે છે."))
tf("ex8_2.q4.iii", ("$\\theta$ में वृद्धि होने पर $\\cos \\theta$ का मान भी बढ़ता है ($0^\\circ$ से $90^\\circ$ तक)।", "$\\theta$ વધે તેમ $\\cos \\theta$ ની કિંમત પણ વધે છે ($0^\\circ$ થી $90^\\circ$ સુધી)."),
   ("असत्य: $\\cos \\theta$ 1 से घटकर 0 हो जाता है।", "ખોટું: $\\cos \\theta$ 1 થી ઘટીને 0 થાય છે."))
tf("ex8_2.q4.iv", ("$\\theta$ के सभी मानों पर $\\sin \\theta = \\cos \\theta$।", "$\\theta$ ની બધી કિંમતો માટે $\\sin \\theta = \\cos \\theta$."), ("असत्य: यह केवल $\\theta = 45^\\circ$ के लिए सत्य है।", "ખોટું: તે ફક્ત $\\theta = 45^\\circ$ માટે સાચું છે."))
tf("ex8_2.q4.v", ("$A = 0^\\circ$ पर $\\cot A$ परिभाषित नहीं है।", "$A = 0^\\circ$ માટે $\\cot A$ વ્યાખ્યાયિત નથી."),
   ("सत्य: $\\cot 0^\\circ = \\dfrac{\\cos 0^\\circ}{\\sin 0^\\circ} = \\dfrac{1}{0}$, जो परिभाषित नहीं है।", "સાચું: $\\cot 0^\\circ = \\dfrac{\\cos 0^\\circ}{\\sin 0^\\circ} = \\dfrac{1}{0}$, જે વ્યાખ્યાયિત નથી."))
# Exercise 8.3
add("ex8_3.q1", ("त्रिकोणमितीय अनुपातों $\\sin A$, $\\sec A$ और $\\tan A$ को $\\cot A$ के पदों में व्यक्त कीजिए।", "ત્રિકોણમિતીય ગુણોત્તરો $\\sin A$, $\\sec A$ અને $\\tan A$ ને $\\cot A$ ના પદમાં દર્શાવો."),
    {0: ("$\\text{cosec}^{2} A = 1 + \\cot^{2} A$, अतः $\\sin A = \\dfrac{1}{\\sqrt{1 + \\cot^{2} A}}$।", "$\\text{cosec}^{2} A = 1 + \\cot^{2} A$, તેથી $\\sin A = \\dfrac{1}{\\sqrt{1 + \\cot^{2} A}}$."),
     2: ("$\\sec^{2} A = 1 + \\tan^{2} A = \\dfrac{\\cot^{2} A + 1}{\\cot^{2} A}$, अतः $\\sec A = \\dfrac{\\sqrt{1 + \\cot^{2} A}}{\\cot A}$।", "$\\sec^{2} A = 1 + \\tan^{2} A = \\dfrac{\\cot^{2} A + 1}{\\cot^{2} A}$, તેથી $\\sec A = \\dfrac{\\sqrt{1 + \\cot^{2} A}}{\\cot A}$.")})
add("ex8_3.q2", ("$\\angle A$ के अन्य सभी त्रिकोणमितीय अनुपातों को $\\sec A$ के पदों में लिखिए।", "$\\angle A$ ના બાકીના બધા ત્રિકોણમિતીય ગુણોત્તરોને $\\sec A$ ના પદમાં લખો."),
    {0: ("$\\cos A = \\dfrac{1}{\\sec A}$ और $\\tan A = \\sqrt{\\sec^{2} A - 1}$", "$\\cos A = \\dfrac{1}{\\sec A}$ અને $\\tan A = \\sqrt{\\sec^{2} A - 1}$"),
     2: ("$\\cot A = \\dfrac{1}{\\sqrt{\\sec^{2} A - 1}}$ और $\\text{cosec } A = \\dfrac{\\sec A}{\\sqrt{\\sec^{2} A - 1}}$", "$\\cot A = \\dfrac{1}{\\sqrt{\\sec^{2} A - 1}}$ અને $\\text{cosec } A = \\dfrac{\\sec A}{\\sqrt{\\sec^{2} A - 1}}$")})
FB83 = {
 "i": {"$1$": ("गुणनखंड 9 मत भूलिए।", "અવયવ 9 ભૂલશો નહિ."), "$9$": ("सही! $9 \\times 1 = 9$।", "સાચું! $9 \\times 1 = 9$."), "$8$": ("$\\sec^{2} A - \\tan^{2} A = 1$, अतः यह $9 \\times 1$ है।", "$\\sec^{2} A - \\tan^{2} A = 1$, તેથી તે $9 \\times 1$ છે."), "$0$": ("$\\sec^{2} A$ और $\\tan^{2} A$ में 1 का अंतर है।", "$\\sec^{2} A$ અને $\\tan^{2} A$ વચ્ચે 1 નો તફાવત છે.")},
 "ii": {"$0$": ("$\\theta = 45^\\circ$ लेकर जाँचिए: $(2 + \\sqrt{2})(2 - \\sqrt{2}) = 2$।", "$\\theta = 45^\\circ$ લઈ ચકાસો: $(2 + \\sqrt{2})(2 - \\sqrt{2}) = 2$."), "$1$": ("$\\theta = 45^\\circ$ लेकर जाँचिए: गुणनफल 2 है।", "$\\theta = 45^\\circ$ લઈ ચકાસો: ગુણાકાર 2 છે."),
        "$2$": ("सही! गुणनफल सरल होकर $\\dfrac{2\\sin \\theta \\cos \\theta}{\\sin \\theta \\cos \\theta} = 2$ बनता है।", "સાચું! ગુણાકાર સાદું રૂપ આપતાં $\\dfrac{2\\sin \\theta \\cos \\theta}{\\sin \\theta \\cos \\theta} = 2$ બને છે."), "$-1$": ("$\\theta = 45^\\circ$ लेकर जाँचिए: गुणनफल 2 है।", "$\\theta = 45^\\circ$ લઈ ચકાસો: ગુણાકાર 2 છે.")},
 "iii": {"$\\sec A$": ("गुणा कीजिए: $\\dfrac{(1 + \\sin A)(1 - \\sin A)}{\\cos A} = \\cos A$।", "ગુણાકાર કરો: $\\dfrac{(1 + \\sin A)(1 - \\sin A)}{\\cos A} = \\cos A$."), "$\\sin A$": ("$1 - \\sin^{2} A = \\cos^{2} A$, जिससे $\\cos A$ मिलता है।", "$1 - \\sin^{2} A = \\cos^{2} A$, જેનાથી $\\cos A$ મળે છે."),
         "$\\text{cosec } A$": ("सब कुछ $\\sin$ और $\\cos$ में लिखिए: उत्तर $\\cos A$ है।", "બધું $\\sin$ અને $\\cos$ માં લખો: જવાબ $\\cos A$ છે."), "$\\cos A$": ("सही! $\\dfrac{1 - \\sin^{2} A}{\\cos A} = \\cos A$।", "સાચું! $\\dfrac{1 - \\sin^{2} A}{\\cos A} = \\cos A$.")},
 "iv": {"$\\sec^{2} A$": ("यह केवल अंश $1 + \\tan^{2} A$ है।", "આ ફક્ત અંશ $1 + \\tan^{2} A$ છે."), "$-1$": ("अंश और हर दोनों धनात्मक हैं।", "અંશ અને છેદ બંને ધન છે."),
        "$\\cot^{2} A$": ("यह उलटा है: $\\dfrac{\\sec^{2} A}{\\text{cosec}^{2} A} = \\tan^{2} A$।", "આ ઊલટું છે: $\\dfrac{\\sec^{2} A}{\\text{cosec}^{2} A} = \\tan^{2} A$."), "$\\tan^{2} A$": ("सही! $\\dfrac{\\sec^{2} A}{\\text{cosec}^{2} A} = \\tan^{2} A$।", "સાચું! $\\dfrac{\\sec^{2} A}{\\text{cosec}^{2} A} = \\tan^{2} A$.")},
}
for p, fb in FB83.items():
    Q[f"ch08.q.ex8_3.q3.{p}.option_feedback"] = feedback(f"ch08.q.ex8_3.q3.{p}", fb)
Q["ch08.q.ex8_3.q3.ii.explanation"] = ("$\\sin$ और $\\cos$ के पदों में गुणनफल $\\dfrac{(\\sin \\theta + \\cos \\theta)^{2} - 1}{\\sin \\theta \\cos \\theta} = \\dfrac{2\\sin \\theta \\cos \\theta}{\\sin \\theta \\cos \\theta} = 2$ है।",
                                       "$\\sin$ અને $\\cos$ ના પદમાં ગુણાકાર $\\dfrac{(\\sin \\theta + \\cos \\theta)^{2} - 1}{\\sin \\theta \\cos \\theta} = \\dfrac{2\\sin \\theta \\cos \\theta}{\\sin \\theta \\cos \\theta} = 2$ છે.")
# identities: step overrides only where words appear
add("ex8_3.q4.iii", None, {0: ("$t = \\tan \\theta$ लेकर: बायाँ पक्ष $= \\dfrac{t^{2}}{t - 1} - \\dfrac{1}{t(t - 1)} = \\dfrac{t^{3} - 1}{t(t - 1)}$", "$t = \\tan \\theta$ લઈને: ડા.બા. $= \\dfrac{t^{2}}{t - 1} - \\dfrac{1}{t(t - 1)} = \\dfrac{t^{3} - 1}{t(t - 1)}$")})
add("ex8_3.q4.v", None, {0: ("अंश और हर को $\\sin A$ से भाग दीजिए: बायाँ पक्ष $= \\dfrac{\\cot A - 1 + \\text{cosec } A}{\\cot A + 1 - \\text{cosec } A}$", "અંશ અને છેદને $\\sin A$ વડે ભાગો: ડા.બા. $= \\dfrac{\\cot A - 1 + \\text{cosec } A}{\\cot A + 1 - \\text{cosec } A}$"),
                         1: ("अंश में $1$ के स्थान पर $\\text{cosec}^{2} A - \\cot^{2} A$ रखिए: अंश $= (\\cot A + \\text{cosec } A)(1 - \\text{cosec } A + \\cot A)$", "અંશમાં $1$ ને બદલે $\\text{cosec}^{2} A - \\cot^{2} A$ મૂકો: અંશ $= (\\cot A + \\text{cosec } A)(1 - \\text{cosec } A + \\cot A)$"),
                         2: ("उभयनिष्ठ गुणनखंड काटने पर, बायाँ पक्ष $= \\text{cosec } A + \\cot A =$ दायाँ पक्ष", "સામાન્ય અવયવ છેદતાં, ડા.બા. $= \\text{cosec } A + \\cot A =$ જ.બા.")})
add("ex8_3.q4.vi", None, {0: ("अंदर $\\dfrac{1 + \\sin A}{1 + \\sin A}$ से गुणा कीजिए: बायाँ पक्ष $= \\sqrt{\\dfrac{(1 + \\sin A)^{2}}{1 - \\sin^{2} A}} = \\sqrt{\\dfrac{(1 + \\sin A)^{2}}{\\cos^{2} A}}$", "અંદર $\\dfrac{1 + \\sin A}{1 + \\sin A}$ વડે ગુણો: ડા.બા. $= \\sqrt{\\dfrac{(1 + \\sin A)^{2}}{1 - \\sin^{2} A}} = \\sqrt{\\dfrac{(1 + \\sin A)^{2}}{\\cos^{2} A}}$")})
# examples
add("eg_tan43", ("यदि $\\tan A = \\dfrac{4}{3}$ है, तो कोण A के अन्य त्रिकोणमितीय अनुपात ज्ञात कीजिए।", "જો $\\tan A = \\dfrac{4}{3}$ હોય, તો ખૂણા A ના બાકીના ત્રિકોણમિતીય ગુણોત્તર શોધો."),
    {0: ("$BC = 4k$, $AB = 3k$, अतः $AC = 5k$।", "$BC = 4k$, $AB = 3k$, તેથી $AC = 5k$.")})
add("eg_angles", ("यदि $\\sin(A - B) = \\dfrac{1}{2}$, $\\cos(A + B) = \\dfrac{1}{2}$, $0^\\circ < A + B \\leq 90^\\circ$, $A > B$ है, तो $A$ और $B$ ज्ञात कीजिए।", "જો $\\sin(A - B) = \\dfrac{1}{2}$, $\\cos(A + B) = \\dfrac{1}{2}$, $0^\\circ < A + B \\leq 90^\\circ$, $A > B$ હોય, તો $A$ અને $B$ શોધો."))
add("eg_sec", ("सिद्ध कीजिए कि $\\sec A(1 - \\sin A)(\\sec A + \\tan A) = 1$।", "સાબિત કરો કે $\\sec A(1 - \\sin A)(\\sec A + \\tan A) = 1$."))
add("eg_sinminus", ("सर्वसमिका $\\sec^{2} \\theta = 1 + \\tan^{2} \\theta$ का प्रयोग करके सिद्ध कीजिए कि $\\dfrac{\\sin \\theta - \\cos \\theta + 1}{\\sin \\theta + \\cos \\theta - 1} = \\dfrac{1}{\\sec \\theta - \\tan \\theta}$।",
                    "નિત્યસમ $\\sec^{2} \\theta = 1 + \\tan^{2} \\theta$ નો ઉપયોગ કરી સાબિત કરો કે $\\dfrac{\\sin \\theta - \\cos \\theta + 1}{\\sin \\theta + \\cos \\theta - 1} = \\dfrac{1}{\\sec \\theta - \\tan \\theta}$."),
    {0: ("अंश और हर को $\\cos \\theta$ से भाग दीजिए: बायाँ पक्ष $= \\dfrac{\\tan \\theta - 1 + \\sec \\theta}{\\tan \\theta + 1 - \\sec \\theta}$", "અંશ અને છેદને $\\cos \\theta$ વડે ભાગો: ડા.બા. $= \\dfrac{\\tan \\theta - 1 + \\sec \\theta}{\\tan \\theta + 1 - \\sec \\theta}$"),
     1: ("अंश और हर को $(\\tan \\theta - \\sec \\theta)$ से गुणा कीजिए और $\\tan^{2} \\theta - \\sec^{2} \\theta = -1$ का प्रयोग कीजिए: अंश $= -1 - (\\tan \\theta - \\sec \\theta)$", "અંશ અને છેદને $(\\tan \\theta - \\sec \\theta)$ વડે ગુણો અને $\\tan^{2} \\theta - \\sec^{2} \\theta = -1$ નો ઉપયોગ કરો: અંશ $= -1 - (\\tan \\theta - \\sec \\theta)$")})
# MCQs
MCQ = {
 "mcq01": (("$\\sin 30^\\circ + \\cos 60^\\circ$ का मान है:", "$\\sin 30^\\circ + \\cos 60^\\circ$ ની કિંમત છે:"), None,
           {"$1$": ("सही!", "સાચું!"), "$\\dfrac{1}{2}$": ("दोनों पद जोड़िए: $\\dfrac{1}{2} + \\dfrac{1}{2}$।", "બંને પદ ઉમેરો: $\\dfrac{1}{2} + \\dfrac{1}{2}$."), "$\\sqrt{3}$": ("दोनों मान $\\dfrac{1}{2}$ हैं।", "બંને કિંમત $\\dfrac{1}{2}$ છે."), "$0$": ("जोड़िए, घटाइए नहीं।", "ઉમેરો, બાદ ન કરો.")}, None),
 "mcq02": (("यदि $\\sin A = \\dfrac{3}{5}$ है, तो $\\cos A$ है:", "જો $\\sin A = \\dfrac{3}{5}$ હોય, તો $\\cos A$ છે:"), ("भुजाएँ $3, 4, 5$: $\\cos A = \\dfrac{4}{5}$।", "બાજુઓ $3, 4, 5$: $\\cos A = \\dfrac{4}{5}$."),
           {"$\\dfrac{4}{5}$": ("सही!", "સાચું!"), "$\\dfrac{3}{4}$": ("यह $\\tan A$ है।", "આ $\\tan A$ છે."), "$\\dfrac{5}{3}$": ("यह $\\text{cosec } A$ है।", "આ $\\text{cosec } A$ છે."), "$\\dfrac{2}{5}$": ("$\\cos A \\neq 1 - \\sin A$; 3-4-5 त्रिभुज लीजिए।", "$\\cos A \\neq 1 - \\sin A$; 3-4-5 ત્રિકોણ લો.")}, None),
 "mcq03": (("$\\tan 45^\\circ$ का मान है:", "$\\tan 45^\\circ$ ની કિંમત છે:"), ("समद्विबाहु समकोण त्रिभुज में सम्मुख $=$ संलग्न, अतः $\\tan 45^\\circ = 1$।", "સમદ્વિબાજુ કાટકોણ ત્રિકોણમાં સામેની $=$ પાસેની, તેથી $\\tan 45^\\circ = 1$."),
           {"$1$": ("सही!", "સાચું!"), "$0$": ("$\\tan 0^\\circ = 0$, $\\tan 45^\\circ$ नहीं।", "$\\tan 0^\\circ = 0$, $\\tan 45^\\circ$ નહિ."), "$\\sqrt{3}$": ("यह $\\tan 60^\\circ$ है।", "આ $\\tan 60^\\circ$ છે."), "$\\dfrac{1}{\\sqrt{2}}$": ("यह $\\sin 45^\\circ$ या $\\cos 45^\\circ$ है।", "આ $\\sin 45^\\circ$ અથવા $\\cos 45^\\circ$ છે.")}, None),
 "mcq04": (("$\\sin^{2} 60^\\circ + \\cos^{2} 60^\\circ$ बराबर है:", "$\\sin^{2} 60^\\circ + \\cos^{2} 60^\\circ$ બરાબર છે:"), ("हर कोण के लिए $\\sin^{2} A + \\cos^{2} A = 1$।", "દરેક ખૂણા માટે $\\sin^{2} A + \\cos^{2} A = 1$."),
           {"$1$": ("सही! सर्वसमिका हर कोण के लिए सत्य है।", "સાચું! નિત્યસમ દરેક ખૂણા માટે સાચું છે."), "$\\dfrac{1}{2}$": ("$\\dfrac{3}{4} + \\dfrac{1}{4} = 1$।", "$\\dfrac{3}{4} + \\dfrac{1}{4} = 1$."), "$\\dfrac{\\sqrt{3}}{2}$": ("पहले मानों का वर्ग कीजिए: $\\dfrac{3}{4} + \\dfrac{1}{4}$।", "પહેલાં કિંમતોનો વર્ગ કરો: $\\dfrac{3}{4} + \\dfrac{1}{4}$."), "$2$": ("$\\sin^{2} A + \\cos^{2} A = 1$।", "$\\sin^{2} A + \\cos^{2} A = 1$.")}, None),
 "mcq05": (("यदि $\\tan A = \\dfrac{12}{5}$ है, तो $\\sin A$ है:", "જો $\\tan A = \\dfrac{12}{5}$ હોય, તો $\\sin A$ છે:"), ("भुजाएँ $5, 12, 13$: $\\sin A = \\dfrac{12}{13}$।", "બાજુઓ $5, 12, 13$: $\\sin A = \\dfrac{12}{13}$."),
           {"$\\dfrac{12}{13}$": ("सही! भुजाएँ 5, 12, 13।", "સાચું! બાજુઓ 5, 12, 13."), "$\\dfrac{5}{13}$": ("यह $\\cos A$ है।", "આ $\\cos A$ છે."), "$\\dfrac{12}{5}$": ("यह स्वयं $\\tan A$ है।", "આ પોતે $\\tan A$ છે."), "$\\dfrac{13}{12}$": ("यह $\\text{cosec } A$ है।", "આ $\\text{cosec } A$ છે.")}, None),
 "mcq06": (("$\\cos A$ का व्युत्क्रम है:", "$\\cos A$ નો વ્યસ્ત છે:"), None,
           {"$\\sec A$": ("सही!", "સાચું!"), "$\\text{cosec } A$": ("यह $\\sin A$ का व्युत्क्रम है।", "આ $\\sin A$ નો વ્યસ્ત છે."), "$\\cot A$": ("यह $\\tan A$ का व्युत्क्रम है।", "આ $\\tan A$ નો વ્યસ્ત છે."), "$\\tan A$": ("$\\tan A = \\dfrac{\\sin A}{\\cos A}$।", "$\\tan A = \\dfrac{\\sin A}{\\cos A}$.")}, None),
 "mcq07": (("$\\cos 90^\\circ$ का मान है:", "$\\cos 90^\\circ$ ની કિંમત છે:"), ("$\\cos$ का मान $0^\\circ$ पर 1 से घटकर $90^\\circ$ पर 0 हो जाता है।", "$\\cos$ ની કિંમત $0^\\circ$ પર 1 થી ઘટીને $90^\\circ$ પર 0 થાય છે."),
           {"$0$": ("सही!", "સાચું!"), "$1$": ("यह $\\cos 0^\\circ$ या $\\sin 90^\\circ$ है।", "આ $\\cos 0^\\circ$ અથવા $\\sin 90^\\circ$ છે."), "$\\dfrac{1}{2}$": ("यह $\\cos 60^\\circ$ है।", "આ $\\cos 60^\\circ$ છે."), "not defined": ("$\\tan 90^\\circ$ परिभाषित नहीं है, पर $\\cos 90^\\circ = 0$।", "$\\tan 90^\\circ$ વ્યાખ્યાયિત નથી, પણ $\\cos 90^\\circ = 0$.")},
           {"not defined": ("परिभाषित नहीं", "વ્યાખ્યાયિત નથી")}),
 "mcq08": (("$\\sin 60^\\circ - \\sin 30^\\circ$ बराबर है:", "$\\sin 60^\\circ - \\sin 30^\\circ$ બરાબર છે:"), ("$\\dfrac{\\sqrt{3}}{2} - \\dfrac{1}{2} = \\dfrac{\\sqrt{3} - 1}{2}$। ध्यान दें कि $\\sin(60^\\circ - 30^\\circ)$ अलग होगा।", "$\\dfrac{\\sqrt{3}}{2} - \\dfrac{1}{2} = \\dfrac{\\sqrt{3} - 1}{2}$. ધ્યાન રાખો કે $\\sin(60^\\circ - 30^\\circ)$ જુદું થશે."),
           {"$\\dfrac{\\sqrt{3} - 1}{2}$": ("सही!", "સાચું!"), "$\\sin 30^\\circ$": ("$\\sin 60^\\circ - \\sin 30^\\circ \\neq \\sin(60^\\circ - 30^\\circ)$।", "$\\sin 60^\\circ - \\sin 30^\\circ \\neq \\sin(60^\\circ - 30^\\circ)$."),
            "$\\dfrac{1}{2}$": ("यह इसे $\\sin 30^\\circ$ मान लेता है; इसके बजाय मान घटाइए।", "આ તેને $\\sin 30^\\circ$ માની લે છે; તેના બદલે કિંમતો બાદ કરો."), "$\\dfrac{\\sqrt{3} + 1}{2}$": ("यह योग है, अंतर नहीं।", "આ સરવાળો છે, તફાવત નહિ.")}, None),
 "mcq09": (("$(1 - \\cos^{2} A)\\,\\text{cosec}^{2} A$ बराबर है:", "$(1 - \\cos^{2} A)\\,\\text{cosec}^{2} A$ બરાબર છે:"), None,
           {"$1$": ("सही!", "સાચું!"), "$0$": ("$\\sin^{2} A \\times \\text{cosec}^{2} A = 1$।", "$\\sin^{2} A \\times \\text{cosec}^{2} A = 1$."), "$\\sin^{2} A$": ("$\\text{cosec}^{2} A$ से भी गुणा कीजिए।", "$\\text{cosec}^{2} A$ વડે પણ ગુણો."), "$\\cos^{2} A$": ("$1 - \\cos^{2} A = \\sin^{2} A$।", "$1 - \\cos^{2} A = \\sin^{2} A$.")}, None),
 "mcq10": (("यदि $2\\sin \\theta = 1$ है और $\\theta$ न्यून कोण है, तो $\\theta$ है:", "જો $2\\sin \\theta = 1$ હોય અને $\\theta$ લઘુકોણ હોય, તો $\\theta$ છે:"), None,
           {"$30^\\circ$": ("सही!", "સાચું!"), "$60^\\circ$": ("$\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$।", "$\\sin 60^\\circ = \\dfrac{\\sqrt{3}}{2}$."), "$45^\\circ$": ("$\\sin 45^\\circ = \\dfrac{1}{\\sqrt{2}}$।", "$\\sin 45^\\circ = \\dfrac{1}{\\sqrt{2}}$."), "$90^\\circ$": ("$\\sin 90^\\circ = 1$।", "$\\sin 90^\\circ = 1$.")}, None),
 "mcq11": (("न्यून कोण $A$ के लिए इनमें से क्या कभी सत्य नहीं हो सकता?", "લઘુકોણ $A$ માટે આમાંથી શું ક્યારેય સાચું ન હોઈ શકે?"), ("$\\sin A$ अधिक से अधिक 1 होता है, क्योंकि कर्ण सबसे लंबी भुजा है।", "$\\sin A$ વધુમાં વધુ 1 હોય છે, કારણ કે કર્ણ સૌથી લાંબી બાજુ છે."),
           {"$\\sin A = \\dfrac{5}{4}$": ("सही! $\\sin A$ कभी 1 से अधिक नहीं हो सकता।", "સાચું! $\\sin A$ ક્યારેય 1 કરતાં વધુ ન હોઈ શકે."), "$\\tan A = 5$": ("$\\tan A$ कोई भी धनात्मक संख्या हो सकता है।", "$\\tan A$ કોઈ પણ ધન સંખ્યા હોઈ શકે."),
            "$\\sec A = 2$": ("$\\sec 60^\\circ = 2$।", "$\\sec 60^\\circ = 2$."), "$\\cos A = 0.6$": ("संभव है: 3-4-5 त्रिभुज से $\\cos A = 0.6$ मिलता है।", "શક્ય છે: 3-4-5 ત્રિકોણથી $\\cos A = 0.6$ મળે છે.")}, None),
 "mcq12": (("यदि $\\sqrt{3}\\tan \\theta = 1$ है, तो $\\theta$ है:", "જો $\\sqrt{3}\\tan \\theta = 1$ હોય, તો $\\theta$ છે:"), None,
           {"$30^\\circ$": ("सही!", "સાચું!"), "$60^\\circ$": ("$\\tan 60^\\circ = \\sqrt{3}$।", "$\\tan 60^\\circ = \\sqrt{3}$."), "$45^\\circ$": ("$\\tan 45^\\circ = 1$।", "$\\tan 45^\\circ = 1$."), "$0^\\circ$": ("$\\tan 0^\\circ = 0$।", "$\\tan 0^\\circ = 0$.")}, None),
}
for key, (question, explanation, fb, options) in MCQ.items():
    iid = f"ch08.q.{key}"
    Q[f"{iid}.question"] = question
    if explanation: Q[f"{iid}.explanation"] = explanation
    Q[f"{iid}.option_feedback"] = feedback(iid, fb)
    if options: Q[f"{iid}.options"] = by_option(iid, options)
# Shine written questions
add("vsa1", ("सरल कीजिए: $(1 - \\cos^{2} A)\\,\\text{cosec}^{2} A$।", "સાદું રૂપ આપો: $(1 - \\cos^{2} A)\\,\\text{cosec}^{2} A$."))
add("vsa2", ("मान ज्ञात कीजिए: $(\\sin 30^\\circ + \\cos 30^\\circ)^{2}$।", "કિંમત શોધો: $(\\sin 30^\\circ + \\cos 30^\\circ)^{2}$."))
add("sa1", ("सिद्ध कीजिए कि $\\sin^{4} A - \\cos^{4} A = 2\\sin^{2} A - 1$।", "સાબિત કરો કે $\\sin^{4} A - \\cos^{4} A = 2\\sin^{2} A - 1$."))
add("sa2", ("सिद्ध कीजिए कि $\\tan A + \\cot A = \\sec A \\, \\text{cosec } A$।", "સાબિત કરો કે $\\tan A + \\cot A = \\sec A \\, \\text{cosec } A$."))
add("sa3", ("यदि $\\cos A = \\dfrac{12}{13}$ है, तो $\\sin A$ और $\\tan A$ ज्ञात कीजिए, और सत्यापित कीजिए कि $\\sin^{2} A + \\cos^{2} A = 1$।", "જો $\\cos A = \\dfrac{12}{13}$ હોય, તો $\\sin A$ અને $\\tan A$ શોધો, અને ચકાસો કે $\\sin^{2} A + \\cos^{2} A = 1$."),
    {0: ("संलग्न $= 12k$, कर्ण $= 13k$, सम्मुख $= 5k$: $\\sin A = \\dfrac{5}{13}$, $\\tan A = \\dfrac{5}{12}$।", "પાસેની બાજુ $= 12k$, કર્ણ $= 13k$, સામેની બાજુ $= 5k$: $\\sin A = \\dfrac{5}{13}$, $\\tan A = \\dfrac{5}{12}$.")})
add("la1", ("सिद्ध कीजिए कि $(1 + \\cot A - \\text{cosec } A)(1 + \\tan A + \\sec A) = 2$। अतः $(1 + \\cot 45^\\circ - \\text{cosec } 45^\\circ)(1 + \\tan 45^\\circ + \\sec 45^\\circ)$ का मान सीधे ज्ञात कीजिए और इसकी जाँच कीजिए।",
             "સાબિત કરો કે $(1 + \\cot A - \\text{cosec } A)(1 + \\tan A + \\sec A) = 2$. તે પરથી $(1 + \\cot 45^\\circ - \\text{cosec } 45^\\circ)(1 + \\tan 45^\\circ + \\sec 45^\\circ)$ ની કિંમત સીધી શોધો અને ચકાસો."),
    {3: ("$45^\\circ$ पर: $(1 + 1 - \\sqrt{2})(1 + 1 + \\sqrt{2}) = (2 - \\sqrt{2})(2 + \\sqrt{2})$", "$45^\\circ$ પર: $(1 + 1 - \\sqrt{2})(1 + 1 + \\sqrt{2}) = (2 - \\sqrt{2})(2 + \\sqrt{2})$")})
add("la2", ("सिद्ध कीजिए कि $\\sqrt{\\dfrac{\\sec A - 1}{\\sec A + 1}} + \\sqrt{\\dfrac{\\sec A + 1}{\\sec A - 1}} = 2\\,\\text{cosec } A$।", "સાબિત કરો કે $\\sqrt{\\dfrac{\\sec A - 1}{\\sec A + 1}} + \\sqrt{\\dfrac{\\sec A + 1}{\\sec A - 1}} = 2\\,\\text{cosec } A$."))
add("cb1", ("एक स्कूल ज़मीन से 2 m ऊँचे दरवाज़े तक व्हीलचेयर के लिए एक ढलान (रैम्प) बनाता है। रैम्प ज़मीन से $30^\\circ$ का कोण बनाता है।\n\n(i) दरवाज़े की ऊँचाई और रैम्प की लंबाई के पदों में $\\sin 30^\\circ$ लिखिए। (1)\n\n(ii) रैम्प की लंबाई ज्ञात कीजिए। (1)\n\n(iii) रैम्प द्वारा तय की गई क्षैतिज दूरी ज्ञात कीजिए। अथवा अपने उत्तरों से $\\tan 30^\\circ$ ज्ञात कीजिए और सारणी से उसकी जाँच कीजिए। (2)",
             "એક શાળા જમીનથી 2 m ઊંચા દરવાજા સુધી વ્હીલચેર માટે ઢાળ (રેમ્પ) બનાવે છે. રેમ્પ જમીન સાથે $30^\\circ$ નો ખૂણો બનાવે છે.\n\n(i) દરવાજાની ઊંચાઈ અને રેમ્પની લંબાઈના પદમાં $\\sin 30^\\circ$ લખો. (1)\n\n(ii) રેમ્પની લંબાઈ શોધો. (1)\n\n(iii) રેમ્પે કાપેલું સમક્ષિતિજ અંતર શોધો. અથવા તમારા જવાબો પરથી $\\tan 30^\\circ$ શોધો અને કોષ્ટકથી ચકાસો. (2)"),
    {0: ("(i) $\\sin 30^\\circ = \\dfrac{\\text{height}}{\\text{length of ramp}} = \\dfrac{2}{L}$ (ऊँचाई / रैम्प की लंबाई)", "(i) $\\sin 30^\\circ = \\dfrac{\\text{height}}{\\text{length of ramp}} = \\dfrac{2}{L}$ (ઊંચાઈ / રેમ્પની લંબાઈ)"),
     1: ("(ii) $\\dfrac{1}{2} = \\dfrac{2}{L}$, अतः $L = 4$ m।", "(ii) $\\dfrac{1}{2} = \\dfrac{2}{L}$, તેથી $L = 4$ m."),
     2: ("(iii) $\\sqrt{4^{2} - 2^{2}} = \\sqrt{12} = 2\\sqrt{3}$ m $\\approx 3.46$ m। अथवा $\\tan 30^\\circ = \\dfrac{2}{2\\sqrt{3}} = \\dfrac{1}{\\sqrt{3}}$, जैसा सारणी में है।", "(iii) $\\sqrt{4^{2} - 2^{2}} = \\sqrt{12} = 2\\sqrt{3}$ m $\\approx 3.46$ m. અથવા $\\tan 30^\\circ = \\dfrac{2}{2\\sqrt{3}} = \\dfrac{1}{\\sqrt{3}}$, જેમ કોષ્ટકમાં છે.")})
add("cb2", ("15 m लंबी एक सीढ़ी एक ऊर्ध्वाधर दीवार से टिकी है। इसका पाद दीवार से 9 m दूर है।\n\n(i) सीढ़ी दीवार पर कितनी ऊँचाई तक पहुँचती है? (1)\n\n(ii) यदि सीढ़ी भूमि से $\\theta$ कोण बनाती है, तो $\\cos \\theta$ ज्ञात कीजिए। (1)\n\n(iii) $\\sin \\theta$ और $\\tan \\theta$ ज्ञात कीजिए। अथवा सत्यापित कीजिए कि $\\sin^{2} \\theta + \\cos^{2} \\theta = 1$। (2)",
             "15 m લાંબી નિસરણી એક ઊભી દીવાલને અઢેલીને મૂકેલી છે. તેનો પાયો દીવાલથી 9 m દૂર છે.\n\n(i) નિસરણી દીવાલ પર કેટલી ઊંચાઈ સુધી પહોંચે છે? (1)\n\n(ii) જો નિસરણી જમીન સાથે $\\theta$ ખૂણો બનાવે, તો $\\cos \\theta$ શોધો. (1)\n\n(iii) $\\sin \\theta$ અને $\\tan \\theta$ શોધો. અથવા ચકાસો કે $\\sin^{2} \\theta + \\cos^{2} \\theta = 1$. (2)"),
    {2: ("(iii) $\\sin \\theta = \\dfrac{12}{15} = \\dfrac{4}{5}$, $\\tan \\theta = \\dfrac{12}{9} = \\dfrac{4}{3}$। अथवा $\\dfrac{16}{25} + \\dfrac{9}{25} = 1$ ✓", "(iii) $\\sin \\theta = \\dfrac{12}{15} = \\dfrac{4}{5}$, $\\tan \\theta = \\dfrac{12}{9} = \\dfrac{4}{3}$. અથવા $\\dfrac{16}{25} + \\dfrac{9}{25} = 1$ ✓")})

AR = {
 "ch08.q.ar1": ("न्यून कोण $A$ के लिए $\\sin A$, $\\dfrac{4}{3}$ नहीं हो सकता।", "समकोण त्रिभुज में कर्ण सबसे लंबी भुजा होती है।", "લઘુકોણ $A$ માટે $\\sin A$ એ $\\dfrac{4}{3}$ ન હોઈ શકે.", "કાટકોણ ત્રિકોણમાં કર્ણ સૌથી લાંબી બાજુ હોય છે.",
                "$\\sin A = \\dfrac{\\text{opposite}}{\\text{hypotenuse}} < 1$।", "कर्ण का सबसे लंबा होना ही $\\sin A < 1$ का कारण है।", "$\\sin A = \\dfrac{\\text{opposite}}{\\text{hypotenuse}} < 1$.", "કર્ણ સૌથી લાંબો હોવો એ જ $\\sin A < 1$ નું કારણ છે.",
                "$\\sin A = \\dfrac{\\text{opposite}}{\\text{hypotenuse}} < 1$, ठीक इसलिए कि कर्ण सबसे लंबी भुजा है।", "$\\sin A = \\dfrac{\\text{opposite}}{\\text{hypotenuse}} < 1$, બરાબર એટલા માટે કે કર્ણ સૌથી લાંબી બાજુ છે."),
 "ch08.q.ar2": ("$\\sin^{2} 35^\\circ + \\cos^{2} 35^\\circ = 1$।", "हर कोण $A$ के लिए $\\sin^{2} A + \\cos^{2} A = 1$।", "$\\sin^{2} 35^\\circ + \\cos^{2} 35^\\circ = 1$.", "દરેક ખૂણા $A$ માટે $\\sin^{2} A + \\cos^{2} A = 1$.",
                "यह $A = 35^\\circ$ वाली सर्वसमिका है।", "यह सर्वसमिका सीधे A देती है।", "આ $A = 35^\\circ$ વાળું નિત્યસમ છે.", "આ નિત્યસમ સીધું A આપે છે.",
                "R की सर्वसमिका से सीधे A मिलता है।", "R ના નિત્યસમથી સીધું A મળે છે."),
 "ch08.q.ar3": ("$\\sin(30^\\circ + 60^\\circ) = \\sin 30^\\circ + \\sin 60^\\circ$।", "$\\sin 90^\\circ = 1$।", "$\\sin(30^\\circ + 60^\\circ) = \\sin 30^\\circ + \\sin 60^\\circ$.", "$\\sin 90^\\circ = 1$.",
                "$\\sin 90^\\circ = 1$ पर $\\dfrac{1}{2} + \\dfrac{\\sqrt{3}}{2} \\neq 1$।", "$\\sin 90^\\circ = 1$ एक सही मान है।", "$\\sin 90^\\circ = 1$ પણ $\\dfrac{1}{2} + \\dfrac{\\sqrt{3}}{2} \\neq 1$.", "$\\sin 90^\\circ = 1$ એ સાચી કિંમત છે.",
                "A असत्य है: $\\sin 90^\\circ = 1$ पर $\\dfrac{1}{2} + \\dfrac{\\sqrt{3}}{2} \\neq 1$। R सत्य है।", "A ખોટું છે: $\\sin 90^\\circ = 1$ પણ $\\dfrac{1}{2} + \\dfrac{\\sqrt{3}}{2} \\neq 1$. R સાચું છે."),
 "ch08.q.ar4": ("$2\\sin 45^\\circ \\cos 45^\\circ = 1$।", "$\\tan 45^\\circ = 0$।", "$2\\sin 45^\\circ \\cos 45^\\circ = 1$.", "$\\tan 45^\\circ = 0$.",
                "$2 \\times \\dfrac{1}{\\sqrt{2}} \\times \\dfrac{1}{\\sqrt{2}} = 1$।", "$\\tan 45^\\circ = 1$, 0 नहीं।", "$2 \\times \\dfrac{1}{\\sqrt{2}} \\times \\dfrac{1}{\\sqrt{2}} = 1$.", "$\\tan 45^\\circ = 1$, 0 નહિ.",
                "A सत्य है: $2 \\times \\dfrac{1}{\\sqrt{2}} \\times \\dfrac{1}{\\sqrt{2}} = 1$। R असत्य है: $\\tan 45^\\circ = 1$।", "A સાચું છે: $2 \\times \\dfrac{1}{\\sqrt{2}} \\times \\dfrac{1}{\\sqrt{2}} = 1$. R ખોટું છે: $\\tan 45^\\circ = 1$."),
 "ch08.q.ar5": ("$\\cot 0^\\circ$ परिभाषित नहीं है।", "$\\sin 90^\\circ = 1$।", "$\\cot 0^\\circ$ વ્યાખ્યાયિત નથી.", "$\\sin 90^\\circ = 1$.",
                "$\\sin 0^\\circ = 0$ होने से $\\dfrac{\\cos 0^\\circ}{\\sin 0^\\circ}$ परिभाषित नहीं होता।", "यह सत्य है, पर इसका $\\cot 0^\\circ$ से कोई संबंध नहीं।", "$\\sin 0^\\circ = 0$ હોવાથી $\\dfrac{\\cos 0^\\circ}{\\sin 0^\\circ}$ વ્યાખ્યાયિત નથી.", "તે સાચું છે, પણ તેને $\\cot 0^\\circ$ સાથે કોઈ સંબંધ નથી.",
                "A सत्य है क्योंकि $\\sin 0^\\circ = 0$ से $\\dfrac{\\cos 0^\\circ}{\\sin 0^\\circ}$ परिभाषित नहीं होता। R सत्य है पर A से इसका कोई संबंध नहीं।", "A સાચું છે કારણ કે $\\sin 0^\\circ = 0$ થી $\\dfrac{\\cos 0^\\circ}{\\sin 0^\\circ}$ વ્યાખ્યાયિત નથી. R સાચું છે પણ A સાથે તેને કોઈ સંબંધ નથી."),
}
