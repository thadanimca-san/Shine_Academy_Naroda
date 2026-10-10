"""Shared Hindi/Gujarati patterns for maths content: sentence templates,
marking-scheme phrases and assertion-reason wording."""
import re

# (English regex, Hindi format, Gujarati format); groups fill {0}, {1}, ...
TEMPLATES = [
 (r"^Prove that (\$[^$]+\$) is irrational\.$", "सिद्ध कीजिए कि {0} अपरिमेय है।", "સાબિત કરો કે {0} અસંમેય છે."),
 (r"^Express (\d+) as a product of its prime factors\.$", "{0} को अभाज्य गुणनखंडों के गुणनफल के रूप में व्यक्त कीजिए।", "{0} ને અવિભાજ્ય અવયવોના ગુણાકાર સ્વરૂપે દર્શાવો."),
 (r"^Divide repeatedly by primes: (\$[^$]+\$)$", "अभाज्य संख्याओं से बार-बार भाग दीजिए: {0}", "અવિભાજ્ય સંખ્યાઓ વડે વારંવાર ભાગાકાર કરો: {0}"),
 (r"^Find the LCM and HCF of (\d+) and (\d+) and verify that LCM \$\\times\$ HCF = product of the two numbers\.$",
  r"{0} और {1} का LCM और HCF ज्ञात कीजिए और सत्यापित कीजिए कि LCM $\times$ HCF = दोनों संख्याओं का गुणनफल।",
  r"{0} અને {1} ના લ.સા.અ. અને ગુ.સા.અ. શોધો અને ચકાસો કે લ.સા.અ. $\times$ ગુ.સા.અ. = બંને સંખ્યાઓનો ગુણાકાર."),
 (r"^HCF = (\d+), LCM = (\d+)$", "HCF = {0}, LCM = {1}", "ગુ.સા.અ. = {0}, લ.સા.અ. = {1}"),
 (r"^LCM \$\\times\$ HCF (\$[^$]+\$) and (\$[^$]+\$)\. Verified\.$",
  r"LCM $\times$ HCF {0} और {1}। सत्यापित।", r"લ.સા.અ. $\times$ ગુ.સા.અ. {0} અને {1}. ચકાસણી થઈ."),
 (r"^Find the LCM and HCF of (.+) and (\d+) by applying the prime factorisation method\.$",
  "अभाज्य गुणनखंडन विधि का प्रयोग करके {0} और {1} का LCM और HCF ज्ञात कीजिए।", "અવિભાજ્ય અવયવીકરણની રીતનો ઉપયોગ કરીને {0} અને {1} ના લ.સા.અ. અને ગુ.સા.અ. શોધો."),
 (r"^Find the zeroes of the quadratic polynomial (\$[^$]+\$), and verify the relationship between the zeroes and the coefficients\.$",
  "द्विघात बहुपद {0} के शून्यक ज्ञात कीजिए और शून्यकों तथा गुणांकों के बीच के संबंध की सत्यता की जाँच कीजिए।",
  "દ્વિઘાત બહુપદી {0} નાં શૂન્યો શોધો અને શૂન્યો તથા સહગુણકો વચ્ચેનો સંબંધ ચકાસો."),
 (r"^Factorising / solving (\$[^$]+\$) gives the zeroes (\$[^$]+\$) and (\$[^$]+\$)\.$",
  "अवयव बनाने / हल करने पर {0} से शून्यक {1} और {2} मिलते हैं।", "અવયવ પાડતાં / ઉકેલતાં {0} પરથી શૂન્યો {1} અને {2} મળે છે."),
 (r"^Factorising / solving (\$[^$]+\$) gives the zeroes (\$[^$]+\$) \(repeated\)\.$",
  "अवयव बनाने / हल करने पर {0} से शून्यक {1} (दो बार) मिलता है।", "અવયવ પાડતાં / ઉકેલતાં {0} પરથી શૂન્ય {1} (બે વાર) મળે છે."),
 (r"^Sum of zeroes (\$[^$]+\$) and (\$[^$]+\$) ✓$", "शून्यकों का योग {0} और {1} ✓", "શૂન્યોનો સરવાળો {0} અને {1} ✓"),
 (r"^Product of zeroes (\$[^$]+\$) and (\$[^$]+\$) ✓$", "शून्यकों का गुणनफल {0} और {1} ✓", "શૂન્યોનો ગુણાકાર {0} અને {1} ✓"),
 (r"^Find a quadratic polynomial whose sum and product of zeroes are (\$[^$]+\$) respectively\.$",
  "एक द्विघात बहुपद ज्ञात कीजिए जिसके शून्यकों का योग तथा गुणनफल क्रमशः {0} हैं।", "જેનાં શૂન્યોનો સરવાળો અને ગુણાકાર અનુક્રમે {0} હોય તેવી દ્વિઘાત બહુપદી શોધો."),
 (r"^Required polynomial (\$[^$]+\$)$", "अभीष्ट बहुपद {0}", "માગેલી બહુપદી {0}"),
 (r"^Taking a suitable (\$[^$]+\$): (\$[^$]+\$)$", "उपयुक्त {0} लेने पर: {1}", "યોગ્ય {0} લેતાં: {1}"),
 (r"^The graph of (\$[^$]+\$) is shown\. Find the number of zeroes of (\$[^$]+\$)\.$",
  "{0} का आलेख दिया गया है। {1} के शून्यकों की संख्या ज्ञात कीजिए।", "{0} નો આલેખ આપેલ છે. {1} નાં શૂન્યોની સંખ્યા શોધો."),
 (r"^On comparing the ratios (\$[^$]+\$), (\$[^$]+\$) and (\$[^$]+\$), find out whether the lines representing the pair (\$[^$]+\$) and (\$[^$]+\$) intersect at a point, are parallel or are coincident\.$",
  "अनुपातों {0}, {1} और {2} की तुलना करके ज्ञात कीजिए कि समीकरण युग्म {3} और {4} को निरूपित करने वाली रेखाएँ एक बिंदु पर प्रतिच्छेद करती हैं, समांतर हैं अथवा संपाती हैं।",
  "ગુણોત્તરો {0}, {1} અને {2} ની સરખામણી કરીને નક્કી કરો કે સમીકરણયુગ્મ {3} અને {4} ને દર્શાવતી રેખાઓ એક બિંદુમાં છેદે છે, સમાંતર છે કે સંપાતી છે."),
 (r"^On comparing the ratios (\$[^$]+\$), (\$[^$]+\$) and (\$[^$]+\$), find out whether the pair (\$[^$]+\$); (\$[^$]+\$) is consistent or inconsistent\.$",
  "अनुपातों {0}, {1} और {2} की तुलना करके ज्ञात कीजिए कि युग्म {3}; {4} संगत है या असंगत।",
  "ગુણોત્તરો {0}, {1} અને {2} ની સરખામણી કરીને નક્કી કરો કે યુગ્મ {3}; {4} સુસંગત છે કે અસંગત."),
 (r"^Hence the lines intersect at a point\.$", "अतः रेखाएँ एक बिंदु पर प्रतिच्छेद करती हैं।", "તેથી રેખાઓ એક બિંદુમાં છેદે છે."),
 (r"^Hence the lines are parallel\.$", "अतः रेखाएँ समांतर हैं।", "તેથી રેખાઓ સમાંતર છે."),
 (r"^Hence the lines are coincident\.$", "अतः रेखाएँ संपाती हैं।", "તેથી રેખાઓ સંપાતી છે."),
 (r"^Hence the pair is consistent \(unique solution\)\.$", "अतः युग्म संगत है (अद्वितीय हल)।", "તેથી યુગ્મ સુસંગત છે (અનન્ય ઉકેલ)."),
 (r"^Hence the pair is inconsistent \(no solution\)\.$", "अतः युग्म असंगत है (कोई हल नहीं)।", "તેથી યુગ્મ અસંગત છે (એક પણ ઉકેલ નથી)."),
 (r"^Hence the pair is consistent \(infinitely many solutions\)\.$", "अतः युग्म संगत है (अपरिमित रूप से अनेक हल)।", "તેથી યુગ્મ સુસંગત છે (અનંત ઉકેલો)."),
 (r"^Is the pair (\$[^$]+\$), (\$[^$]+\$) consistent or inconsistent\? If consistent, obtain the solution graphically\.$",
  "क्या युग्म {0}, {1} संगत है या असंगत? यदि संगत है, तो ग्राफ़ द्वारा हल ज्ञात कीजिए।", "શું યુગ્મ {0}, {1} સુસંગત છે કે અસંગત? જો સુસંગત હોય, તો આલેખની મદદથી ઉકેલ મેળવો."),
 (r"^Given the linear equation (\$[^$]+\$), write another linear equation in two variables such that the geometrical representation of the pair so formed is intersecting lines\.$",
  "रैखिक समीकरण {0} दिया है। दो चरों में एक अन्य ऐसा रैखिक समीकरण लिखिए कि इस प्रकार बने युग्म का ज्यामितीय निरूपण प्रतिच्छेद करती रेखाएँ हो।",
  "સુરેખ સમીકરણ {0} આપેલ છે. બે ચલમાં બીજું એવું સુરેખ સમીકરણ લખો કે જેથી બનતા યુગ્મનું ભૌમિતિક નિરૂપણ છેદતી રેખાઓ હોય."),
 (r"^Given the linear equation (\$[^$]+\$), write another linear equation in two variables such that the geometrical representation of the pair so formed is parallel lines\.$",
  "रैखिक समीकरण {0} दिया है। दो चरों में एक अन्य ऐसा रैखिक समीकरण लिखिए कि इस प्रकार बने युग्म का ज्यामितीय निरूपण समांतर रेखाएँ हो।",
  "સુરેખ સમીકરણ {0} આપેલ છે. બે ચલમાં બીજું એવું સુરેખ સમીકરણ લખો કે જેથી બનતા યુગ્મનું ભૌમિતિક નિરૂપણ સમાંતર રેખાઓ હોય."),
 (r"^Given the linear equation (\$[^$]+\$), write another linear equation in two variables such that the geometrical representation of the pair so formed is coincident lines\.$",
  "रैखिक समीकरण {0} दिया है। दो चरों में एक अन्य ऐसा रैखिक समीकरण लिखिए कि इस प्रकार बने युग्म का ज्यामितीय निरूपण संपाती रेखाएँ हो।",
  "સુરેખ સમીકરણ {0} આપેલ છે. બે ચલમાં બીજું એવું સુરેખ સમીકરણ લખો કે જેથી બનતા યુગ્મનું ભૌમિતિક નિરૂપણ સંપાતી રેખાઓ હોય."),
 (r"^One answer: (\$[^$]+\$) \(many answers are possible\)\.$", "एक उत्तर: {0} (अनेक उत्तर संभव हैं)।", "એક જવાબ: {0} (ઘણા જવાબ શક્ય છે)."),
 (r"^Check: (\$[^$]+\$)$", "जाँच: {0}", "ચકાસણી: {0}"),
 (r"^Solve the pair of linear equations (\$[^$]+\$) and (\$[^$]+\$) by the substitution method\.$",
  "प्रतिस्थापन विधि से रैखिक समीकरण युग्म {0} और {1} को हल कीजिए।", "અવેજની રીતથી સુરેખ સમીકરણયુગ્મ {0} અને {1} ઉકેલો."),
 (r"^Solve the pair of linear equations (\$[^$]+\$) and (\$[^$]+\$) by the elimination method and the substitution method\.$",
  "विलोपन विधि और प्रतिस्थापन विधि से रैखिक समीकरण युग्म {0} और {1} को हल कीजिए।", "લોપની રીત અને અવેજની રીતથી સુરેખ સમીકરણયુગ્મ {0} અને {1} ઉકેલો."),
 (r"^Express one variable in terms of the other from one equation and substitute it into the other equation\.$",
  "एक समीकरण से एक चर को दूसरे चर के पदों में व्यक्त कीजिए और उसे दूसरे समीकरण में प्रतिस्थापित कीजिए।", "એક સમીકરણમાંથી એક ચલને બીજા ચલના પદમાં દર્શાવો અને તેને બીજા સમીકરણમાં મૂકો."),
 (r"^Solving gives (\$[^$]+\$), (\$[^$]+\$)\.$", "हल करने पर {0}, {1}।", "ઉકેલતાં {0}, {1}."),
 (r"^Make the coefficients of one variable equal, subtract \(or add\) to eliminate it, and check by substitution\.$",
  "एक चर के गुणांक बराबर कीजिए, उसे विलुप्त करने के लिए घटाइए (या जोड़िए), और प्रतिस्थापन से जाँचिए।", "એક ચલના સહગુણક સરખા કરો, તેનો લોપ કરવા બાદબાકી (અથવા સરવાળો) કરો, અને અવેજથી ચકાસો."),
 (r"^Both methods give (\$[^$]+\$), (\$[^$]+\$)\.$", "दोनों विधियों से {0}, {1}।", "બંને રીતથી {0}, {1}."),
]

MARKING = {
 "(i) 1 mark": ("(i) 1 अंक", "(i) 1 ગુણ"),
 "(ii) 1 mark": ("(ii) 1 अंक", "(ii) 1 ગુણ"),
 "(iii) 1 mark factorisation, 1 mark answer": ("(iii) गुणनखंडन के लिए 1 अंक, उत्तर के लिए 1 अंक", "(iii) અવયવીકરણ માટે 1 ગુણ, જવાબ માટે 1 ગુણ"),
 "(iii) 1 mark method, 1 mark answer": ("(iii) विधि के लिए 1 अंक, उत्तर के लिए 1 अंक", "(iii) રીત માટે 1 ગુણ, જવાબ માટે 1 ગુણ"),
 "1 mark: $4^{n} = 2^{2n}$": ("1 अंक: $4^{n} = 2^{2n}$", "1 ગુણ: $4^{n} = 2^{2n}$"),
 "1 mark: $6^{n} = 2^{n} \\times 3^{n}$": ("1 अंक: $6^{n} = 2^{n} \\times 3^{n}$", "1 ગુણ: $6^{n} = 2^{n} \\times 3^{n}$"),
 "1 mark: 151": ("1 अंक: 151", "1 ગુણ: 151"),
 "1 mark: 21 rooms": ("1 अंक: 21 कमरे", "1 ગુણ: 21 ઓરડા"),
 "1 mark: 36 minutes": ("1 अंक: 36 मिनट", "1 ગુણ: 36 મિનિટ"),
 "1 mark: 7 divides $a$ and $b$": ("1 अंक: 7, $a$ और $b$ को विभाजित करता है", "1 ગુણ: 7 એ $a$ અને $b$ ને ભાગે છે"),
 "1 mark: HCF = 12": ("1 अंक: HCF = 12", "1 ગુણ: ગુ.સા.અ. = 12"),
 "1 mark: HCF = 16": ("1 अंक: HCF = 16", "1 ગુણ: ગુ.સા.અ. = 16"),
 "1 mark: HCF = 4": ("1 अंक: HCF = 4", "1 ગુણ: ગુ.સા.અ. = 4"),
 "1 mark: HCF and LCM": ("1 अंक: HCF और LCM", "1 ગુણ: ગુ.સા.અ. અને લ.સા.અ."),
 "1 mark: LCM": ("1 अंक: LCM", "1 ગુણ: લ.સા.અ."),
 "1 mark: LCM = 144": ("1 अंक: LCM = 144", "1 ગુણ: લ.સા.અ. = 144"),
 "1 mark: LCM = 22338": ("1 अंक: LCM = 22338", "1 ગુણ: લ.સા.અ. = 22338"),
 "1 mark: LCM = 9696": ("1 अंक: LCM = 9696", "1 ગુણ: લ.સા.અ. = 9696"),
 "1 mark: answer in hours": ("1 अंक: घंटों में उत्तर", "1 ગુણ: કલાકમાં જવાબ"),
 "1 mark: assuming the contrary and isolating $\\sqrt{7}$": ("1 अंक: विपरीत मानना और $\\sqrt{7}$ को अकेला करना", "1 ગુણ: વિરુદ્ધ ધારવું અને $\\sqrt{7}$ ને એકલું કરવું"),
 "1 mark: assuming the contrary and isolating the surd": ("1 अंक: विपरीत मानना और करणी को अकेला करना", "1 ગુણ: વિરુદ્ધ ધારવું અને કરણીને એકલી કરવી"),
 "1 mark: assuming the contrary with coprime $a, b$": ("1 अंक: सह-अभाज्य $a, b$ के साथ विपरीत मानना", "1 ગુણ: પરસ્પર અવિભાજ્ય $a, b$ સાથે વિરુદ્ધ ધારવું"),
 "1 mark: assumption": ("1 अंक: मान्यता", "1 ગુણ: ધારણા"),
 "1 mark: assumption with coprime": ("1 अंक: सह-अभाज्य के साथ मान्यता", "1 ગુણ: પરસ્પર અવિભાજ્ય સાથે ધારણા"),
 "1 mark: conclusion": ("1 अंक: निष्कर्ष", "1 ગુણ: નિષ્કર્ષ"),
 "1 mark: conclusion with reason": ("1 अंक: कारण सहित निष्कर्ष", "1 ગુણ: કારણ સાથે નિષ્કર્ષ"),
 "1 mark: conclusion with reason (no factor 5)": ("1 अंक: कारण सहित निष्कर्ष (गुणनखंड 5 नहीं)", "1 ગુણ: કારણ સાથે નિષ્કર્ષ (અવયવ 5 નથી)"),
 "1 mark: contradiction": ("1 अंक: विरोधाभास", "1 ગુણ: વિરોધાભાસ"),
 "1 mark: contradiction and conclusion": ("1 अंक: विरोधाभास और निष्कर्ष", "1 ગુણ: વિરોધાભાસ અને નિષ્કર્ષ"),
 "1 mark: factorisations": ("1 अंक: गुणनखंडन", "1 ગુણ: અવયવીકરણ"),
 "1 mark: identifying LCM with factorisations": ("1 अंक: गुणनखंडन सहित LCM पहचानना", "1 ગુણ: અવયવીકરણ સાથે લ.સા.અ. ઓળખવો"),
 "1 mark: isolating $\\sqrt{5}$": ("1 अंक: $\\sqrt{5}$ को अकेला करना", "1 ગુણ: $\\sqrt{5}$ ને એકલું કરવું"),
 "1 mark: prime factorisation": ("1 अंक: अभाज्य गुणनखंडन", "1 ગુણ: અવિભાજ્ય અવયવીકરણ"),
 "1 mark: recognising HCF": ("1 अंक: HCF पहचानना", "1 ગુણ: ગુ.સા.અ. ઓળખવો"),
 "1 mark: squaring and using Theorem 1.2 twice": ("1 अंक: वर्ग करना और प्रमेय 1.2 का दो बार प्रयोग", "1 ગુણ: વર્ગ કરવો અને પ્રમેય 1.2 નો બે વાર ઉપયોગ"),
 "1 mark: subtracting the remainders": ("1 अंक: शेषफल घटाना", "1 ગુણ: શેષ બાદ કરવી"),
 "1 mark: taking 13 common": ("1 अंक: 13 उभयनिष्ठ लेना", "1 ગુણ: 13 સામાન્ય લેવો"),
 "1 mark: taking 5 common": ("1 अंक: 5 उभयनिष्ठ लेना", "1 ગુણ: 5 સામાન્ય લેવો"),
 "1 mark: taking 7 common": ("1 अंक: 7 उभयनिष्ठ लेना", "1 ગુણ: 7 સામાન્ય લેવો"),
 "1 mark: using HCF × LCM = product": ("1 अंक: HCF × LCM = गुणनफल का प्रयोग", "1 ગુણ: ગુ.સા.અ. × લ.સા.અ. = ગુણાકારનો ઉપયોગ"),
 "1 mark: both prime factorisations": ("1 अंक: दोनों अभाज्य गुणनखंडन", "1 ગુણ: બંને અવિભાજ્ય અવયવીકરણ"),
 "1 mark: verification": ("1 अंक: सत्यापन", "1 ગુણ: ચકાસણી"),
 "1 mark: prime factorisations": ("1 अंक: अभाज्य गुणनखंडन", "1 ગુણ: અવિભાજ્ય અવયવીકરણ"),
 "1 mark: correct repeated division / factor tree": ("1 अंक: सही बार-बार भाग / गुणनखंड वृक्ष", "1 ગુણ: સાચો વારંવાર ભાગાકાર / અવયવ વૃક્ષ"),
 "1 mark: final answer in power form": ("1 अंक: घात के रूप में अंतिम उत्तर", "1 ગુણ: ઘાત સ્વરૂપે અંતિમ જવાબ"),
 "1 mark: HCF = 4": ("1 अंक: HCF = 4", "1 ગુણ: ગુ.સા.અ. = 4"),
 "1 mark: LCM = 9696": ("1 अंक: LCM = 9696", "1 ગુણ: લ.સા.અ. = 9696"),
 "1 mark: 7 divides $a$ and $b$": ("1 अंक: 7, $a$ और $b$ को विभाजित करता है", "1 ગુણ: 7 એ $a$ અને $b$ ને ભાગે છે"),
 "1 mark: $\\sqrt{7}$": ("1 अंक: $\\sqrt{7}$", "1 ગુણ: $\\sqrt{7}$"),
 "(iii) 1 mark each for sum and product (or width with working)": ("(iii) योग और गुणनफल के लिए 1-1 अंक (अथवा विधि सहित चौड़ाई)", "(iii) સરવાળો અને ગુણાકાર માટે 1-1 ગુણ (અથવા રીત સાથે પહોળાઈ)"),
 "(iii) 1 mark for $x = 3$, 1 mark for 4 m": ("(iii) $x = 3$ के लिए 1 अंक, 4 m के लिए 1 अंक", "(iii) $x = 3$ માટે 1 ગુણ, 4 m માટે 1 ગુણ"),
 "1 mark: $-\\dfrac{27}{4}$": ("1 अंक: $-\\dfrac{27}{4}$", "1 ગુણ: $-\\dfrac{27}{4}$"),
 "1 mark: $\\dfrac{5}{4}$": ("1 अंक: $\\dfrac{5}{4}$", "1 ગુણ: $\\dfrac{5}{4}$"),
 "1 mark: $k = \\dfrac{2}{3}$": ("1 अंक: $k = \\dfrac{2}{3}$", "1 ગુણ: $k = \\dfrac{2}{3}$"),
 "1 mark: 20": ("1 अंक: 20", "1 ગુણ: 20"),
 "1 mark: answer": ("1 अंक: उत्तर", "1 ગુણ: જવાબ"),
 "1 mark: correct polynomial": ("1 अंक: सही बहुपद", "1 ગુણ: સાચી બહુપદી"),
 "1 mark: factorisation": ("1 अंक: गुणनखंडन", "1 ગુણ: અવયવીકરણ"),
 "1 mark: method": ("1 अंक: विधि", "1 ગુણ: રીત"),
 "1 mark: polynomial": ("1 अंक: बहुपद", "1 ગુણ: બહુપદી"),
 "1 mark: product": ("1 अंक: गुणनफल", "1 ગુણ: ગુણાકાર"),
 "1 mark: product equation": ("1 अंक: गुणनफल का समीकरण", "1 ગુણ: ગુણાકારનું સમીકરણ"),
 "1 mark: product verified": ("1 अंक: गुणनफल सत्यापित", "1 ગુણ: ગુણાકાર ચકાસ્યો"),
 "1 mark: sum": ("1 अंक: योग", "1 ગુણ: સરવાળો"),
 "1 mark: sum and product": ("1 अंक: योग और गुणनफल", "1 ગુણ: સરવાળો અને ગુણાકાર"),
 "1 mark: sum and product of reciprocals": ("1 अंक: व्युत्क्रमों का योग और गुणनफल", "1 ગુણ: વ્યસ્તોનો સરવાળો અને ગુણાકાર"),
 "1 mark: sum verified": ("1 अंक: योग सत्यापित", "1 ગુણ: સરવાળો ચકાસ્યો"),
 "1 mark: using $x^{2} - Sx + P$": ("1 अंक: $x^{2} - Sx + P$ का प्रयोग", "1 ગુણ: $x^{2} - Sx + P$ નો ઉપયોગ"),
 "1 mark: zeroes": ("1 अंक: शून्यक", "1 ગુણ: શૂન્યો"),
 "1 mark: verification": ("1 अंक: सत्यापन", "1 ગુણ: ચકાસણી"),
 "1 mark: forming / rearranging the equations": ("1 अंक: समीकरण बनाना / व्यवस्थित करना", "1 ગુણ: સમીકરણ બનાવવાં / ગોઠવવાં"),
 "1 mark: eliminating or substituting correctly": ("1 अंक: सही विलोपन या प्रतिस्थापन", "1 ગુણ: સાચો લોપ કે અવેજ"),
 "1 mark: both values": ("1 अंक: दोनों मान", "1 ગુણ: બંને કિંમતો"),
 "1 mark: ratios $\\dfrac{a_1}{a_2}, \\dfrac{b_1}{b_2}, \\dfrac{c_1}{c_2}$": ("1 अंक: अनुपात $\\dfrac{a_1}{a_2}, \\dfrac{b_1}{b_2}, \\dfrac{c_1}{c_2}$", "1 ગુણ: ગુણોત્તરો $\\dfrac{a_1}{a_2}, \\dfrac{b_1}{b_2}, \\dfrac{c_1}{c_2}$"),
 "1 mark: table of points for both lines": ("1 अंक: दोनों रेखाओं के लिए बिंदुओं की सारणी", "1 ગુણ: બંને રેખાઓ માટે બિંદુઓનું કોષ્ટક"),
 "1 mark: correct graphs": ("1 अंक: सही आलेख", "1 ગુણ: સાચા આલેખ"),
 "1 mark: solution / conclusion": ("1 अंक: हल / निष्कर्ष", "1 ગુણ: ઉકેલ / નિષ્કર્ષ"),
 "1 mark: suitable equation": ("1 अंक: उपयुक्त समीकरण", "1 ગુણ: યોગ્ય સમીકરણ"),
 "1 mark: justification by ratios": ("1 अंक: अनुपातों द्वारा पुष्टि", "1 ગુણ: ગુણોત્તરો વડે સમર્થન"),
 "1 mark: $y = 5$": ("1 अंक: $y = 5$", "1 ગુણ: $y = 5$"),
 "1 mark: $x = -2$": ("1 अंक: $x = -2$", "1 ગુણ: $x = -2$"),
 "1 mark: $m = -1$": ("1 अंक: $m = -1$", "1 ગુણ: $m = -1$"),
 "1 mark: condition": ("1 अंक: शर्त", "1 ગુણ: શરત"),
 "1 mark: $k = \\pm 6$": ("1 अंक: $k = \\pm 6$", "1 ગુણ: $k = \\pm 6$"),
 "1 mark: rejecting $k = 6$": ("1 अंक: $k = 6$ को अस्वीकार करना", "1 ગુણ: $k = 6$ નો અસ્વીકાર"),
 "1 mark: forming both equations": ("1 अंक: दोनों समीकरण बनाना", "1 ગુણ: બંને સમીકરણ બનાવવાં"),
 "1 mark: simplifying": ("1 अंक: सरल करना", "1 ગુણ: સાદું રૂપ આપવું"),
 "2 marks: elimination and $x = 600$": ("2 अंक: विलोपन और $x = 600$", "2 ગુણ: લોપ અને $x = 600$"),
 "1 mark: $y = 400$": ("1 अंक: $y = 400$", "1 ગુણ: $y = 400$"),
 "1 mark: table for each line": ("1 अंक: प्रत्येक रेखा के लिए सारणी", "1 ગુણ: દરેક રેખા માટે કોષ્ટક"),
 "1 mark: graphs": ("1 अंक: आलेख", "1 ગુણ: આલેખ"),
 "1 mark: solution $(3, 2)$": ("1 अंक: हल $(3, 2)$", "1 ગુણ: ઉકેલ $(3, 2)$"),
 "1 mark: vertices": ("1 अंक: शीर्ष", "1 ગુણ: શિરોબિંદુઓ"),
 "1 mark: area": ("1 अंक: क्षेत्रफल", "1 ગુણ: ક્ષેત્રફળ"),
 "1 mark: graphs of both lines": ("1 अंक: दोनों रेखाओं के आलेख", "1 ગુણ: બંને રેખાઓના આલેખ"),
 "1 mark: solution $(2, 2)$": ("1 अंक: हल $(2, 2)$", "1 ગુણ: ઉકેલ $(2, 2)$"),
}

AR_OPTIONS = (
 ["अभिकथन (A) और कारण (R) दोनों सत्य हैं और कारण (R), अभिकथन (A) की सही व्याख्या करता है।",
  "अभिकथन (A) और कारण (R) दोनों सत्य हैं, परंतु कारण (R), अभिकथन (A) की सही व्याख्या नहीं करता है।",
  "अभिकथन (A) सत्य है, परंतु कारण (R) असत्य है।",
  "अभिकथन (A) असत्य है, परंतु कारण (R) सत्य है।"],
 ["વિધાન (A) અને કારણ (R) બંને સાચાં છે અને કારણ (R) એ વિધાન (A) ની સાચી સમજૂતી છે.",
  "વિધાન (A) અને કારણ (R) બંને સાચાં છે, પરંતુ કારણ (R) એ વિધાન (A) ની સાચી સમજૂતી નથી.",
  "વિધાન (A) સાચું છે, પરંતુ કારણ (R) ખોટું છે.",
  "વિધાન (A) ખોટું છે, પરંતુ કારણ (R) સાચું છે."])

AR_LABELS = (("**अभिकथन (A):**", "**कारण (R):**"), ("**વિધાન (A):**", "**કારણ (R):**"))
_TRUTH_BY_ANSWER = {0: (True, True, True), 1: (True, True, False), 2: (True, False, None), 3: (False, True, None)}
_CLAIMS = [(True, True, True), (True, True, False), (True, False, None), (False, True, None)]


def ar_feedback(correct_index, why_a, why_r, lang):
    a, r, explains = _TRUTH_BY_ANSWER[correct_index]
    hi = lang == "hi"
    word = (lambda t: "सत्य" if t else "असत्य") if hi else (lambda t: "સાચું" if t else "ખોટું")
    out = []
    for ca, cr, ce in _CLAIMS:
        if (ca, cr) == (a, r) and (ce is None or ce == explains):
            out.append(f"सही! A {word(a)} है: {why_a} R {word(r)} है: {why_r}" if hi else f"સાચું! A {word(a)} છે: {why_a} R {word(r)} છે: {why_r}")
        elif ca != a:
            out.append(f"अभिकथन को फिर से जाँचिए: यह {word(a)} है, क्योंकि {why_a}" if hi else f"વિધાનને ફરી ચકાસો: તે {word(a)} છે, કારણ કે {why_a}")
        elif cr != r:
            out.append(f"कारण को फिर से जाँचिए: यह {word(r)} है, क्योंकि {why_r}" if hi else f"કારણને ફરી ચકાસો: તે {word(r)} છે, કારણ કે {why_r}")
        elif explains:
            out.append(f"R, A की व्याख्या करता है: {why_r}" if hi else f"R એ A ની સમજૂતી આપે છે: {why_r}")
        else:
            out.append(f"दोनों सत्य हैं, परंतु R, A के सत्य होने का कारण नहीं है: {why_r}" if hi else f"બંને સાચાં છે, પરંતુ R એ A સાચું હોવાનું કારણ નથી: {why_r}")
    return out


def by_template(text, lang):
    for pattern, hi, gu in TEMPLATES:
        m = re.match(pattern, text)
        if m:
            return (hi if lang == "hi" else gu).format(*m.groups())
    return None


def is_math_only(text):
    """True when nothing outside $...$ needs translating (only digits, symbols, spaces)."""
    outside = re.sub(r"\$\$[\s\S]+?\$\$|\$[^$]+?\$", "", text)
    return not re.search(r"[A-Za-z]", outside)
