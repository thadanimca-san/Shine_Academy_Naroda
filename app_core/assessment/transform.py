import json

file_path = '/home/ubuntu/Shine_Academy_Naroda/app_core/assessment/gseb_class10_maths_ch3_questions.json'

with open(file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Translation maps
q_gu = {
    "The pair of equations 5x - 15y = 8 and 3x - 9y = 24/5 has:": "સમીકરણો 5x - 15y = 8 અને 3x - 9y = 24/5 ની જોડના:",
    "If a pair of linear equations is consistent, then the lines will be:": "જો સુરેખ સમીકરણોની જોડ સુસંગત હોય, તો રેખાઓ:",
    "For what value of k do the equations 3x - y + 8 = 0 and 6x - ky = -16 represent coincident lines?": "k ની કઈ કિંમત માટે સમીકરણો 3x - y + 8 = 0 અને 6x - ky = -16 સંપાતી રેખાઓ દર્શાવે છે?",
    "The pair of equations x = a and y = b graphically represents lines which are:": "સમીકરણો x = a અને y = b ની જોડ આલેખની રીતે રેખાઓ દર્શાવે છે જે:",
    "Half the perimeter of a rectangular garden, whose length is 4m more than its width, is 36m. Find the dimensions.": "એક લંબચોરસ બગીચાની અર્ધપરિમિતિ 36m છે, જેની લંબાઈ તેની પહોળાઈ કરતાં 4m વધુ છે. તેના માપ શોધો.",
    "One equation of a pair of dependent linear equations is -5x + 7y = 2. The second equation can be:": "અવલંબી સુરેખ સમીકરણોની જોડનું એક સમીકરણ -5x + 7y = 2 છે. બીજું સમીકરણ આ હોઈ શકે:",
    "A fraction becomes 1/3 when 1 is subtracted from the numerator and it becomes 1/4 when 8 is added to its denominator. Find the fraction.": "જ્યારે અંશમાંથી 1 બાદ કરવામાં આવે ત્યારે એક અપૂર્ણાંક 1/3 બને છે અને જ્યારે તેના છેદમાં 8 ઉમેરવામાં આવે ત્યારે તે 1/4 બને છે. તે અપૂર્ણાંક શોધો.",
    "Five years ago, Nuri was thrice as old as Sonu. Ten years later, Nuri will be twice as old as Sonu. How old is Nuri now?": "પાંચ વર્ષ પહેલાં, નૂરીની ઉંમર સોનુની ઉંમર કરતા ત્રણ ગણી હતી. દસ વર્ષ પછી, નૂરીની ઉંમર સોનુની ઉંમર કરતા બમણી હશે. નૂરીની અત્યારની ઉંમર કેટલી છે?",
    "If x = a, y = b is the solution of the equations x - y = 2 and x + y = 4, then the values of a and b are:": "જો x = a, y = b એ સમીકરણો x - y = 2 અને x + y = 4 નો ઉકેલ હોય, તો a અને b ની કિંમત:",
    "The sum of the digits of a two-digit number is 9. Also, nine times this number is twice the number obtained by reversing the order of the digits. Find the number.": "બે અંકની એક સંખ્યાના અંકોનો સરવાળો 9 છે. વળી, આ સંખ્યાના નવ ગણા એ અંકોના ક્રમને ઉલટાવવાથી મળતી સંખ્યાના બમણા છે. તે સંખ્યા શોધો.",
    "For what value of p does the pair of equations 4x + py + 8 = 0 and 2x + 2y + 2 = 0 have unique solution?": "p ની કઈ કિંમત માટે સમીકરણો 4x + py + 8 = 0 અને 2x + 2y + 2 = 0 ને અનન્ય ઉકેલ છે?",
    "The pair of equations x = 0 and x = 5 has:": "સમીકરણો x = 0 અને x = 5 ની જોડના:",
    "Find the value of k for which the system kx - y = 2 and 6x - 2y = 3 has a unique solution.": "k ની કિંમત શોધો કે જેના માટે સમીકરણ સંહતિ kx - y = 2 અને 6x - 2y = 3 નો અનન્ય ઉકેલ હોય.",
    "A boat goes 16 km upstream and 24 km downstream in 6 hours. What type of equations will this form?": "એક હોડી 6 કલાકમાં પ્રવાહની સામેની દિશામાં 16 કિમી અને પ્રવાહની દિશામાં 24 કિમી જાય છે. આ કયા પ્રકારના સમીકરણો બનાવશે?",
    "If the lines given by 3x + 2ky = 2 and 2x + 5y + 1 = 0 are parallel, then the value of k is:": "જો 3x + 2ky = 2 અને 2x + 5y + 1 = 0 દ્વારા આપવામાં આવેલી રેખાઓ સમાંતર હોય, તો k ની કિંમત છે:",
    "Find the solution: x + y = 14 and x - y = 4.": "ઉકેલ શોધો: x + y = 14 અને x - y = 4.",
    "Ritu can row downstream 20 km in 2 hours, and upstream 4 km in 2 hours. Find her speed of rowing in still water.": "રિતુ પ્રવાહની દિશામાં 2 કલાકમાં 20 કિમી અને પ્રવાહની સામેની દિશામાં 2 કલાકમાં 4 કિમી હોડી હંકારી શકે છે. શાંત પાણીમાં હોડી હંકારવાની તેની ઝડપ શોધો.",
    "The father's age is six times his son's age. Four years hence, the age of the father will be four times his son's age. The present ages of the son and the father are, respectively:": "પિતાની ઉંમર તેના પુત્રની ઉંમર કરતા છ ગણી છે. ચાર વર્ષ પછી, પિતાની ઉંમર તેના પુત્રની ઉંમર કરતા ચાર ગણી હશે. પુત્ર અને પિતાની વર્તમાન ઉંમર અનુક્રમે છે:",
    "Which of the following pairs of equations is inconsistent?": "નીચેના પૈકી સમીકરણોની કઈ જોડ અસંગત છે?",
    "The cost of 5 pens and 8 pencils is Rs 120, while the cost of 8 pens and 5 pencils is Rs 153. Find the cost of 1 pen and 1 pencil.": "5 પેન અને 8 પેન્સિલની કિંમત 120 રૂપિયા છે, જ્યારે 8 પેન અને 5 પેન્સિલની કિંમત 153 રૂપિયા છે. 1 પેન અને 1 પેન્સિલની કિંમત શોધો."
}

opt_gu = {
    "One solution": "એક ઉકેલ",
    "Two solutions": "બે ઉકેલ",
    "Infinitely many solutions": "અનંત ઉકેલો",
    "No solution": "કોઈ ઉકેલ નહીં",
    "parallel": "સમાંતર હશે",
    "always coincident": "હંમેશા સંપાતી હશે",
    "intersecting or coincident": "છેદતી અથવા સંપાતી હશે",
    "always intersecting": "હંમેશા છેદતી હશે",
    "intersecting at (b, a)": "(b, a) પર છેદે છે",
    "coincident": "સંપાતી છે",
    "intersecting at (a, b)": "(a, b) પર છેદે છે",
    "Length=20m, Width=16m": "લંબાઈ=20m, પહોળાઈ=16m",
    "Length=16m, Width=20m": "લંબાઈ=16m, પહોળાઈ=20m",
    "Length=18m, Width=14m": "લંબાઈ=18m, પહોળાઈ=14m",
    "Length=24m, Width=12m": "લંબાઈ=24m, પહોળાઈ=12m",
    "40 years": "40 વર્ષ",
    "50 years": "50 વર્ષ",
    "60 years": "60 વર્ષ",
    "45 years": "45 વર્ષ",
    "3 and 5": "3 અને 5",
    "5 and 3": "5 અને 3",
    "3 and 1": "3 અને 1",
    "-1 and -3": "-1 અને -3",
    "Linear equations": "સુરેખ સમીકરણો",
    "Quadratic equations": "દ્વિઘાત સમીકરણો",
    "Equations reducible to linear form": "સુરેખ સ્વરૂપમાં પરિવર્તિત કરી શકાય તેવા સમીકરણો",
    "None of these": "આમાંથી કોઈ નહીં",
    "6 km/h": "6 કિમી/કલાક",
    "8 km/h": "8 કિમી/કલાક",
    "4 km/h": "4 કિમી/કલાક",
    "10 km/h": "10 કિમી/કલાક",
    "4 and 24": "4 અને 24",
    "5 and 30": "5 અને 30",
    "6 and 36": "6 અને 36",
    "3 and 24": "3 અને 24",
    "Pen: 15, Pencil: 6": "પેન: 15, પેન્સિલ: 6",
    "Pen: 16, Pencil: 5": "પેન: 16, પેન્સિલ: 5",
    "Pen: 17, Pencil: 4": "પેન: 17, પેન્સિલ: 4",
    "Pen: 18, Pencil: 3": "પેન: 18, પેન્સિલ: 3"
}

exp_gu = {
    "a1/a2 = 5/3. b1/b2 = -15/-9 = 5/3. c1/c2 = 8/(24/5) = 40/24 = 5/3. Since a1/a2 = b1/b2 = c1/c2, the lines are coincident, meaning infinitely many solutions.": "a1/a2 = 5/3. b1/b2 = -15/-9 = 5/3. c1/c2 = 8/(24/5) = 40/24 = 5/3. અહીં a1/a2 = b1/b2 = c1/c2 હોવાથી રેખાઓ સંપાતી છે, એટલે કે અનંત ઉકેલો મળે છે.",
    "Consistent means it has at least one solution. Intersecting lines have 1 solution, coincident lines have infinite solutions.": "સુસંગત નો અર્થ છે કે તેને ઓછામાં ઓછો એક ઉકેલ છે. છેદતી રેખાઓ માટે 1 ઉકેલ હોય છે, સંપાતી રેખાઓ માટે અનંત ઉકેલો હોય છે.",
    "Rewrite 6x - ky = -16 as 6x - ky + 16 = 0. For coincident lines, a1/a2 = b1/b2 = c1/c2. So 3/6 = -1/-k = 8/16. => 1/2 = 1/k = 1/2. Therefore, k = 2.": "6x - ky = -16 ને 6x - ky + 16 = 0 તરીકે લખો. સંપાતી રેખાઓ માટે, a1/a2 = b1/b2 = c1/c2. તેથી 3/6 = -1/-k = 8/16. => 1/2 = 1/k = 1/2. તેથી, k = 2.",
    "x = a is a vertical line. y = b is a horizontal line. They intersect exactly at the point (a, b).": "x = a શિરોલંબ રેખા છે. y = b સમક્ષિતિજ રેખા છે. તેઓ બરાબર (a, b) બિંદુ પર છેદે છે.",
    "Let length=l, width=w. l = w+4. Half perimeter = (2l+2w)/2 = l+w = 36. Substituting l: (w+4)+w = 36 => 2w = 32 => w=16. Then l = 20.": "ધારો કે લંબાઈ=l, પહોળાઈ=w. l = w+4. અર્ધપરિમિતિ = (2l+2w)/2 = l+w = 36. l ની કિંમત મુકતા: (w+4)+w = 36 => 2w = 32 => w=16. પછી l = 20.",
    "Dependent means coincident (all ratios equal). Multiply by -2: 10x - 14y = -4. This matches exactly.": "અવલંબી એટલે સંપાતી (બધા ગુણોત્તર સમાન). -2 વડે ગુણતા: 10x - 14y = -4. આ બરાબર મેળ ખાય છે.",
    "Let fraction be x/y. (x-1)/y = 1/3 => 3x-y=3. x/(y+8) = 1/4 => 4x-y=8. Subtracting first from second: x = 5. Then 3(5)-y=3 => 15-3=y => y=12. Fraction is 5/12.": "ધારો કે અપૂર્ણાંક x/y છે. (x-1)/y = 1/3 => 3x-y=3. x/(y+8) = 1/4 => 4x-y=8. બીજામાંથી પહેલું સમીકરણ બાદ કરતા: x = 5. પછી 3(5)-y=3 => 15-3=y => y=12. અપૂર્ણાંક 5/12 છે.",
    "N-5 = 3(S-5) => N-3S = -10. N+10 = 2(S+10) => N-2S = 10. Subtract equations: -S = -20 => S=20. N-2(20) = 10 => N=50.": "N-5 = 3(S-5) => N-3S = -10. N+10 = 2(S+10) => N-2S = 10. સમીકરણોની બાદબાકી કરતા: -S = -20 => S=20. N-2(20) = 10 => N=50.",
    "Adding equations: 2x = 6 => x=3. Substituting x: 3 + y = 4 => y=1. So a=3, b=1.": "સમીકરણોનો સરવાળો કરતા: 2x = 6 => x=3. x ની કિંમત મુકતા: 3 + y = 4 => y=1. તેથી a=3, b=1.",
    "Let tens be x, units be y. x+y=9. Number is 10x+y. Reversed is 10y+x. 9(10x+y) = 2(10y+x) => 90x+9y = 20y+2x => 88x = 11y => 8x=y. Substitute y=8x into x+y=9 => 9x=9 => x=1, y=8. Number is 18.": "ધારો કે દશક x છે, એકમ y છે. x+y=9. સંખ્યા 10x+y છે. ઉલટાવેલ સંખ્યા 10y+x છે. 9(10x+y) = 2(10y+x) => 90x+9y = 20y+2x => 88x = 11y => 8x=y. y=8x ને x+y=9 માં મુકતા => 9x=9 => x=1, y=8. સંખ્યા 18 છે.",
    "For unique solution, a1/a2 ≠ b1/b2. So 4/2 ≠ p/2 => 2 ≠ p/2 => p ≠ 4.": "અનન્ય ઉકેલ માટે, a1/a2 ≠ b1/b2. તેથી 4/2 ≠ p/2 => 2 ≠ p/2 => p ≠ 4.",
    "x=0 is the y-axis, and x=5 is a vertical line parallel to the y-axis. They never intersect.": "x=0 એ y-અક્ષ છે, અને x=5 એ y-અક્ષને સમાંતર શિરોલંબ રેખા છે. તેઓ ક્યારેય છેદતા નથી.",
    "For unique solution, a1/a2 ≠ b1/b2 => k/6 ≠ -1/-2 => k/6 ≠ 1/2 => k ≠ 3.": "અનન્ય ઉકેલ માટે, a1/a2 ≠ b1/b2 => k/6 ≠ -1/-2 => k/6 ≠ 1/2 => k ≠ 3.",
    "Let speed of boat be x, stream be y. 16/(x-y) + 24/(x+y) = 6. Variables are in denominator, so it's reducible to linear form.": "ધારો કે હોડીની ઝડપ x અને પ્રવાહની ઝડપ y છે. 16/(x-y) + 24/(x+y) = 6. ચલ છેદમાં હોવાથી, તે સુરેખ સ્વરૂપમાં પરિવર્તિત કરી શકાય તેવા સમીકરણો છે.",
    "Parallel means a1/a2 = b1/b2 ≠ c1/c2. So 3/2 = 2k/5 => 15 = 4k => k = 15/4.": "સમાંતર એટલે a1/a2 = b1/b2 ≠ c1/c2. તેથી 3/2 = 2k/5 => 15 = 4k => k = 15/4.",
    "Adding the equations gives 2x = 18 => x=9. Subtracting gives 2y = 10 => y=5.": "સમીકરણોનો સરવાળો કરતા 2x = 18 => x=9 મળે છે. બાદબાકી કરતા 2y = 10 => y=5 મળે છે.",
    "Downstream speed x+y = 20/2 = 10. Upstream speed x-y = 4/2 = 2. Adding them: 2x = 12 => x = 6.": "પ્રવાહની દિશામાં ઝડપ x+y = 20/2 = 10. પ્રવાહની સામે ઝડપ x-y = 4/2 = 2. તેમનો સરવાળો કરતા: 2x = 12 => x = 6.",
    "Let son=y, father=x. x = 6y. Also, x+4 = 4(y+4). Substitute x: 6y+4 = 4y+16 => 2y=12 => y=6. x = 6(6) = 36.": "ધારો કે પુત્ર=y, પિતા=x. x = 6y. વળી, x+4 = 4(y+4). x ની કિંમત મુકતા: 6y+4 = 4y+16 => 2y=12 => y=6. x = 6(6) = 36.",
    "Inconsistent means parallel lines (a1/a2 = b1/b2 ≠ c1/c2). For option 4: -2/-4 = 1/2, 1/2 = 1/2, 3/10 ≠ 1/2. So they are parallel.": "અસંગત એટલે સમાંતર રેખાઓ (a1/a2 = b1/b2 ≠ c1/c2). વિકલ્પ 4 માટે: -2/-4 = 1/2, 1/2 = 1/2, 3/10 ≠ 1/2. તેથી તેઓ સમાંતર છે.",
    "5x+8y=120 and 8x+5y=153. Add: 13x+13y=273 => x+y=21. Subtract: -3x+3y=-33 => x-y=11. Adding these new equations: 2x = 32 => x=16, y=5.": "5x+8y=120 અને 8x+5y=153. સરવાળો કરતા: 13x+13y=273 => x+y=21. બાદબાકી કરતા: -3x+3y=-33 => x-y=11. આ નવા સમીકરણોનો સરવાળો કરતા: 2x = 32 => x=16, y=5."
}

for obj in data:
    if "question_text" in obj:
        eng = obj["question_text"].get("english", "")
        hin = obj["question_text"].get("hindi", "")
        gu = q_gu.get(eng, eng)
        obj["question"] = eng
        obj["question_hi"] = hin
        obj["question_gu"] = gu
        del obj["question_text"]
        
    if "options" in obj and len(obj["options"]) > 0 and isinstance(obj["options"][0], dict):
        new_opts = []
        new_opts_hi = []
        new_opts_gu = []
        for opt in obj["options"]:
            eng_opt = opt.get("english", "")
            hin_opt = opt.get("hindi", "")
            gu_opt = opt_gu.get(eng_opt, eng_opt)
            new_opts.append(eng_opt)
            new_opts_hi.append(hin_opt)
            new_opts_gu.append(gu_opt)
        obj["options"] = new_opts
        obj["options_hi"] = new_opts_hi
        obj["options_gu"] = new_opts_gu
        
    if "explanation" in obj and isinstance(obj["explanation"], dict):
        eng_exp = obj["explanation"].get("english", "")
        hin_exp = obj["explanation"].get("hindi", "")
        gu_exp = exp_gu.get(eng_exp, eng_exp)
        obj["explanation"] = eng_exp
        obj["explanation_hi"] = hin_exp
        obj["explanation_gu"] = gu_exp
        
    if "distractor_rationale" in obj:
        del obj["distractor_rationale"]
        
    if "ai_context" in obj:
        del obj["ai_context"]

with open(file_path, 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
    f.write('\n')
