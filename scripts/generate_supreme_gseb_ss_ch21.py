import json
import os

def generate_supreme_gseb_ss_ch21():
    chapter_id = "gseb_class10_social_science_ch21"
    title = "Chapter 21: Social Change"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "Constitutional Rights, Child Protection, Senior Citizens, Anti-Corruption, RTI, RTE & NFSA",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB/NCERT",
        "curriculum": ["GSEB", "CBSE", "Universal"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-SS",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "tags": [
            "social_science",
            "social_change",
            "human_rights",
            "child_rights",
            "child_labour",
            "senior_citizens",
            "corruption",
            "anti_corruption",
            "rti_2005",
            "rte_2009",
            "nfsa_2013",
            "maa_annapurna_yojana",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand the concept, dynamics, and driving factors of Social Change `(સામાજિક પરિવર્તન / सामाजिक परिवर्तन)`.",
            "Explain Universal Declaration of Human Rights and Fundamental Rights in the Indian Constitution.",
            "Analyze Child Rights `(બાળ અધિકારો / बाल अधिकार)` and legal provisions against Child Labour `(બાળ મજૂરી / बाल श्रम)`.",
            "Describe the welfare measures, legal acts, and schemes for Senior Citizens `(વરિષ્ઠ નાગરિકો / वरिष्ठ नागरिक)`.",
            "Examine the root causes, adverse impacts of Corruption `(ભ્રષ્ટાચાર / भ्रष्टाचार)`, and institutional anti-corruption mechanisms (ACB, CVC, Lokpal).",
            "Master the step-by-step process, timeframes, and exemptions of the Right to Information Act, 2005 (RTI).",
            "Evaluate the transformative provisions of the Right to Education Act, 2009 (RTE) and National Food Security Act, 2013 (NFSA)."
        ],
        "ai_context": {
            "learning_goal": "Transform the student into a socially conscious citizen and board exam topper by mastering constitutional rights, welfare legislation, citizen empowerment tools (RTI/RTE/NFSA), and anti-corruption frameworks with extreme depth, real-world case studies, and bilingual clarity.",
            "common_misconceptions": [
                "Students confuse the time limit for RTI in ordinary matters (30 days) with matters concerning life and personal liberty (48 hours).",
                "Students believe all government files are accessible under RTI (Fact: Section 8 exempts national security, defense, and strategic secrets).",
                "Students mix up the provisions of the Child Labour Act (1986) with its 2016 amendment regarding adolescent labor in hazardous occupations.",
                "Students confuse AAY (Antyodaya Anna Yojana) allocation (35 kg/family) with Priority Households allocation (5 kg/person) under NFSA."
            ],
            "tutor_hint": "Use real-life relatable citizen scenarios (e.g. asking for municipal road repair status via RTI, admitting an underprivileged child under RTE 25% quota, or reporting bribe demands to ACB helpline 1064) to make abstract legal acts tangible."
        }
    }
    
    blocks = []
    
    # =========================================================================
    # MODULE 1: THE DYNAMICS OF SOCIAL CHANGE & HUMAN RIGHTS
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine a world without equal voting rights, where children are forced to work in coal mines instead of going to school, and where citizens cannot question government spending. Society was not always as progressive as it is today. How did our traditions, laws, and daily lives evolve from ancient social hierarchies to modern democracy? Welcome to the powerful phenomenon of **Social Change `(સામાજિક પરિવર્તન / सामाजिक परिवर्तन)`**!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Social Change is propelled by continuous interactions between technological advancement, economic growth, cultural interactions, and progressive legal reforms `(કાનૂની સુધારાઓ / कानूनी सुधार)`.",
        "image_url": "assets/images/gseb_ss_ch21_social_change_factors.jpg",
        "alt_text": "Mind map of Social Change Drivers: Modernization, Industrialization, Globalization, Legal Framework, and Human Rights"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 1. Meaning & Nature of Social Change `(સામાજિક પરિવર્તનનો અર્થ અને સ્વરૂપ / सामाजिक परिवर्तन का अर्थ और स्वरूप)`\n\n**Social Change** refers to fundamental alterations in:\n1. **Social Structure `(સામાજિક માળખું / सामाजिक संरचना)`:** Changes in family systems (e.g. transition from joint families `(સંયુક્ત કુટુંબ / संयुक्त परिवार)` to nuclear families `(વિભક્ત કુટુંબ / एकल परिवार)`), caste dynamics, and social status.\n2. **Social Relationships `(સામાજિક સંબંધો / सामाजिक संबंध)`:** Evolving interpersonal connections, gender equality, and reduction in social discrimination `(સામાજિક ભેદભાવ / सामाजिक भेदभाव)`.\n3. **Cultural Values and Norms `(સાંસ્કૃતિક મૂલ્યો અને ધોરણો / सांस्कृतिक मूल्य और मानक)`:** Shifts in beliefs, dress codes, rituals, dietary habits, and modern scientific outlook `(વૈજ્ઞાનિક દ્રષ્ટિકોણ / वैज्ञानिक दृष्टिकोण)`.\n\n### Key Driving Factors of Social Change:\n- **Modernization `(આધુનિકીકરણ / आधुनिकीकरण)`:** Adoption of rational, evidence-based, and scientific attitudes in daily life.\n- **Industrialization `(ઔદ્યોગિકીકરણ / औद्योगिकीकरण)` & Urbanization `(શહેરીકરણ / शहरीकरण)`:** Migration from rural agricultural societies to bustling industrial urban centers.\n- **Globalization `(વૈશ્વિકીકરણ / वैश्वीकरण)` & Westernization `(પશ્ચિમીકરણ / पश्चिमीकरण)`:** Cross-border cultural exchange, global trade, internet communication, and media exposure.\n- **Legal & Constitutional Enactments `(બંધારણીય અને કાનૂની જોગવાઈઓ / संवैधानिक और कानूनी प्रावधान)`:** Legislation enacted by the Parliament to ban regressive customs like untouchability, dowry, and child marriage.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 2. Universal Declaration of Human Rights `(માનવ અધિકારોનું સાર્વત્રિક જાહેરનામું / मानव अधिकारों की सार्वभौमिक घोषणा)`\n\nOn **10th December 1948**, the United Nations General Assembly (UNGA) proclaimed the **Universal Declaration of Human Rights (UDHR)**. Because of this historic milestone, **10th December** is globally celebrated every year as **Human Rights Day `(માનવ અધિકાર દિન / मानव अधिकार दिवस)`**.\n\n**What are Human Rights?**\nHuman Rights are inherent, inalienable moral and legal claims possessed by every human being from birth, irrespective of race, caste, gender, religion, language, or nationality. They ensure that every individual lives with human dignity `(માનવ ગૌરવ / मानव गरिमा)`.\n\n### Fundamental Rights in the Indian Constitution `(ભારતીય બંધારણમાં મૂળભૂત હકો / भारतीय संविधान में मौलिक अधिकार)`\nThe Constitution of India enshrines six Fundamental Rights in Part III:\n1. **Right to Equality `(સમાનતાનો હક / समानता का अधिकार)`** (Articles 14–18)\n2. **Right to Freedom `(સ્વાતંત્ર્યનો હક / स्वतंत्रता का अधिकार)`** (Articles 19–22)\n3. **Right against Exploitation `(શોષણ સામેનો હક / शोषण के विरुद्ध अधिकार)`** (Articles 23–24)\n4. **Right to Freedom of Religion `(ધાર્મિક સ્વાતંત્ર્યનો હક / धार्मिक स्वतंत्रता का अधिकार)`** (Articles 25–28)\n5. **Cultural and Educational Rights `(સાંસ્કૃતિક અને શૈક્ષણિક હક / सांस्कृतिक और शैक्षिक अधिकार)`** (Articles 29–30)\n6. **Right to Constitutional Remedies `(બંધારણીય ઇલાજોનો હક / संवैधानिक उपचारों का अधिकार)`** (Article 32)",
        "difficulty": "Advanced",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Chief Academic Architect Tip:**\nDr. B. R. Ambedkar referred to **Article 32 (Right to Constitutional Remedies `(બંધારણીય ઇલાજોનો હક / संवैधानिक उपचारों का अधिकार)`)** as the *'Heart and Soul of the Constitution' `(બંધારણનો આત્મા અને હૃદય / संविधान की आत्मा और हृदय)`*. Without Article 32, all other fundamental rights would merely remain theoretical promises on paper because Article 32 empowers citizens to directly approach the Supreme Court via writs (Habeas Corpus, Mandamus, Prohibition, Quo-Warranto, Certiorari) if any fundamental right is violated!",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "mcq",
        "question": "On which date is 'World Human Rights Day' celebrated across the globe?",
        "options": [
            "15th August",
            "10th December",
            "26th January",
            "1st May"
        ],
        "correct_answer": "10th December",
        "explanation": "On 10th December 1948, the United Nations adopted the Universal Declaration of Human Rights (UDHR). Hence, 10th December is commemorated worldwide as Human Rights Day `(માનવ અધિકાર દિન / मानव अधिकार दिवस)`."
    })

    # =========================================================================
    # MODULE 2: CHILD RIGHTS & ERADICATION OF CHILD LABOUR
    # =========================================================================
    blocks.append({
        "type": "diagram",
        "content": "Every child is born with four fundamental categories of rights recognized by the UN and the Indian Constitution: Survival, Protection, Development, and Participation.",
        "image_url": "assets/images/gseb_ss_ch21_child_rights_pillars.jpg",
        "alt_text": "Four Pillars of Child Rights: Survival, Development, Protection, and Active Participation"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 3. Child Rights: The Foundation of a Healthy Nation `(બાળ અધિકારો / बाल अधिकार)`\n\nChildren are the most vulnerable and tender segment of society. The United Nations declared the **Charter of Child Rights in 1992**, which India ratified. \n\n### The 4 Major Pillars of Child Rights:\n1. **Right to Survival & Life `(જીવન જીવવાનો અધિકાર / जीवन का अधिकार)`:** Right to proper nutrition, clean drinking water, immunization, and quality healthcare from birth.\n2. **Right to Protection `(સુરક્ષાનો અધિકાર / सुरक्षा का अधिकार)`:** Protection against all forms of physical violence, mental harassment, child abuse, hazardous labor, trafficking `(માનવ તસ્કરી / मानव तस्करी)`, and abandonment.\n3. **Right to Development `(વિકાસનો અધિકાર / विकास का अधिकार)`:** Right to free, compulsory elementary education, sports, recreation, mental and moral development.\n4. **Right to Participation `(સહભાગિતાનો અધિકાર / सहभागिता का अधिकार)`:** Right to express thoughts freely and participate in decisions affecting their well-being.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 4. Child Labour: Causes, Evils & Legal Prohibition `(બાળ મજૂરી: કારણો, પરિણામો અને કાયદાકીય પ્રતિબંધ / बाल श्रम: कारण, प्रभाव और कानूनी निषेध)`\n\n**Child Labour `(બાળ મજૂરી / बाल श्रम)`** is a grave social crime where a child under the age of 14 is engaged in economic work, depriving them of schooling and a normal childhood.\n\n### Causes of Child Labour:\n- **Poverty `(ગરીબી / गरीबी)`:** Extreme financial hardship forcing parents to send children to work for supplementary income.\n- **Illiteracy and Ignorance `(નિરક્ષરતા અને અજ્ઞાનતા / निरक्षरता और अज्ञानता)`:** Lack of awareness among parents regarding the long-term benefits of education.\n- **Large Family Size:** Inability to feed and educate multiple children.\n- **Cheap Labor Demand:** Employers exploit children by paying meager wages `(ઓછા વેતન / कम मजदूरी)` for long working hours without unionization.\n\n### Legal Enactments Against Child Labour:\n- **Child and Adolescent Labour (Prohibition and Regulation) Act, 1986 (Amended in 2016):**\n  - **Complete ban** on the employment of any child below **14 years** of age in **all occupations and processes**.\n  - Employment of adolescents aged **14 to 18 years** is strictly prohibited in **hazardous occupations and processes `(જોખમી વ્યવસાયો અને પ્રક્રિયાઓ / जोखिम भरे व्यवसाय)`** (e.g. mines, fireworks, inflammable substances, chemical factories).\n  - Stringent penalties: Imprisonment from 6 months up to 2 years and/or fine from ₹20,000 to ₹50,000 for violators.\n- **National Childline Emergency Service:** Toll-free helpline **1098** operating 24/7 across India for rescuing children in distress.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "common_mistakes",
        "content": "⚠️ **Common Board Exam Mistake to Avoid:**\nDo not confuse the terms **'Child'** and **'Adolescent'** under the amended Child Labour Act, 2016:\n- **Child `(બાળક / बालक)`:** A person who has not completed **14 years** of age. (Banned from ALL types of commercial employment).\n- **Adolescent `(કિશોર / किशोर)`:** A person between **14 and 18 years** of age. (Banned strictly from *hazardous* occupations and processes).",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "mcq",
        "question": "What is the dedicated 24x7 toll-free emergency helpline number in India for rescuing children in distress and preventing child abuse?",
        "options": [
            "100",
            "108",
            "1098",
            "1064"
        ],
        "correct_answer": "1098",
        "explanation": "'CHILDLINE 1098' is India's first 24-hour, free, emergency phone outreach service for children in need of care and protection."
    })

    # =========================================================================
    # MODULE 3: WELFARE AND PROTECTION OF SENIOR CITIZENS
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Our parents and grandparents dedicated their entire youth, energy, and resources to nurture our families and build our country. But in the modern fast-paced era, why are so many elderly citizens facing abandonment, loneliness `(એકલતા / अकेलापन)`, and emotional neglect? Let us explore how Indian law stands as a protective shield for our senior citizens!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 5. Problems of Senior Citizens & Constitutional Duty `(વૃદ્ધો / વરિષ્ઠ નાગરિકોની સમસ્યાઓ / वरिष्ठ नागरिकों की समस्याएँ)`\n\nDue to rapid urbanization, modern materialistic lifestyle, and the breakdown of traditional joint family systems `(સંયુક્ત કુટુંબ વ્યવસ્થાનું વિભાજન / संयुक्त परिवार प्रणाली का विघटन)`, senior citizens face severe vulnerabilities:\n1. **Physical & Health Vulnerabilities:** Chronic illnesses, joint pain, loss of eyesight/hearing, and skyrocketing medical expenditures `(તબીબી ખર્ચ / चिकित्सा खर्च)`.\n2. **Psychological & Emotional Issues:** Loneliness, feeling unwanted, grief over the loss of a spouse, depression, and social isolation.\n3. **Financial Insecurity `(આર્થિક અસલામતી / आर्थिक असुरक्षा)`:** Lack of regular pension or income after retirement, leading to financial dependence on unwilling children.\n\n### Government Policies & Legal Protective Measures:\n1. **National Policy for Older Persons (1999) `(વરિષ્ઠ નાગરિકો માટેની રાષ્ટ્રીય નીતિ / वरिष्ठ नागरिकों के लिए राष्ट्रीय नीति)`:** Formulated to ensure financial security, healthcare, shelter, welfare, and protection against abuse.\n2. **Maintenance and Welfare of Parents and Senior Citizens Act, 2007 `(માતા-પિતા અને વરિષ્ઠ નાગરિકોની જાળવણી અને કલ્યાણ અધિનિયમ / माता-पिता एवं वरिष्ठ नागरिक भरण-पोषण एवं कल्याण अधिनियम)`:**\n   - Children and legal heirs are legally obligated to maintain their elderly parents (providing food, shelter, clothing, and medical care).\n   - Abandoning elderly parents is punishable by up to 3 months of imprisonment and/or monetary fines.\n   - Establishment of special **Maintenance Tribunals `(ભરણ-પોષણ ટ્રિબ્યુનલ / भरण-पोषण अधिकरण)`** where parents can seek swift monthly maintenance allowance without costly court litigation.\n3. **Institutional Welfare Facilities:**\n   - Setting up of **Old Age Homes `(વૃદ્ધાશ્રમો / वृद्धाश्रम)`** equipped with healthcare, dining, and recreational facilities.\n   - Senior Citizen National Helpline **14567** (Elder Line).\n   - Travel concessions in state transport buses, Indian Railways, and air travel.\n   - Special high-interest rates on Fixed Deposits (FDs) in banks and post offices, along with income tax exemptions.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "memory_trick",
        "content": "**Mnemonic to Remember Senior Citizen Protection Measures (H-E-L-P):**\n- **H** - **Health & Concessions:** Subsidized medical care, bus/train seat reservations, higher interest rates.\n- **E** - **Elder Line & Old Age Homes:** Toll-free 14567 helpline and state-run Old Age Homes `(વૃદ્ધાશ્રમ / वृद्धाश्रम)`.\n- **L** - **Legal Maintenance Act (2007):** Compulsory maintenance allowance from children via speedy tribunals.\n- **P** - **Policy (1999) & Pensions:** National Policy for Older Persons and monthly social security pensions.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })
    
    blocks.append({
        "type": "mcq",
        "question": "Under the Maintenance and Welfare of Parents and Senior Citizens Act (2007), what legal protection is provided to elderly parents?",
        "options": [
            "They are forced to move to an old age home immediately.",
            "Children and legal heirs are legally bound to provide food, shelter, clothing, and healthcare under penalty of law.",
            "Parents lose all rights over their ancestral property.",
            "Children are exempted from all family responsibilities after turning 18."
        ],
        "correct_answer": "Children and legal heirs are legally bound to provide food, shelter, clothing, and healthcare under penalty of law.",
        "explanation": "The 2007 Act makes it a legal duty for children and heirs to maintain their parents and senior citizens, empowering parents to claim monthly maintenance allowance through dedicated tribunals."
    })

    # =========================================================================
    # MODULE 4: CORRUPTION - THREAT TO DEMOCRACY & ANTI-CORRUPTION LAWS
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Imagine taxes paid by honest citizens for constructing world-class roads and public hospitals being siphoned off into secret foreign bank accounts. What happens when public power is misused for private greed? It destroys the economy, hurts the poor the most, and erodes trust in democracy. Let's decode the menace of **Corruption `(ભ્રષ્ટાચાર / भ्रष्टाचार)`** and how the law fights back!",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 6. Meaning, Forms & Evil Effects of Corruption `(ભ્રષ્ટાચારનો અર્થ, સ્વરૂપો અને દુષ્પરિણામો / भ्रष्टाचार का अर्थ, रूप और दुष्परिणाम)`\n\n**Corruption `(ભ્રષ્ટાચાર / भ्रष्टाचार)`** is defined as the improper or unlawful behavior of individuals holding public or private authority to extract undue personal financial gains or illicit advantages.\n\n### Diverse Manifestations of Corruption:\n- **Bribery `(લાંચ-રુશ્વત / रिश्वत)`:** Offering or accepting money or gifts to do an official favor or bypass legal rules.\n- **Nepotism & Favoritism `(સગાંવાદ અને પક્ષપાત / भाई-भतीजावाद और पक्षपात)`:** Giving undeserved government contracts, jobs, or promotions to relatives and friends.\n- **Embezzlement & Extortion `(ઉચાપત અને જબરદસ્તી વસૂલી / गबन और अवैध वसूली)`:** Stealing public funds and forcing citizens to pay extra illegal charges for standard government services.\n\n### Evil Impacts of Corruption on Society & Economy:\n1. **Violation of Human Rights & Social Injustice:** Poor and honest citizens are deprived of their lawful entitlements and welfare benefits.\n2. **Rise of Black Money `(કાળા નાણાંનો ઉદ્ભવ / काले धन का उद्भव)`:** Tax evasion creates an underground parallel economy that fuels inflation and illegal activities.\n3. **Decline in Quality of Public Infrastructure:** Substandard materials used in public construction cause bridges, schools, and roads to collapse prematurely.\n4. **Erosion of Public Faith in Democracy:** Citizens lose trust in administrative institutions and the rule of law `(કાયદાનું શાસન / कानून का शासन)`.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 7. Institutional Framework to Eradicate Corruption `(ભ્રષ્ટાચાર નાથવા માટેના કાનૂની અને સંસ્થાકીય પગલાં / भ्रष्टाचार निवारण के उपाय)`\n\nTo combat corruption decisively, India has instituted robust legal enactments and oversight bodies:\n\n1. **Prevention of Corruption Act, 1988 `(ભ્રષ્ટાચાર નિવારણ અધિનિયમ / भ्रष्टाचार निवारण अधिनियम)`:**\n   - Defines public servants comprehensively.\n   - Treats demanding or accepting illegal gratification as a severe cognizable criminal offence carrying rigorous imprisonment from 3 to 7 years.\n2. **Anti-Corruption Bureau (ACB) `(લાંચ-રુશ્વત વિરોધી બ્યુરો / भ्रष्टाचार निरोधक ब्यूरो)`:**\n   - Active specialized police agency in Gujarat and other states that conducts sudden trap raids to catch corrupt officials red-handed.\n   - **Gujarat ACB Toll-Free Helpline: 1064** (available 24/7 for reporting bribe demands).\n3. **Central Vigilance Commission (CVC) `(કેન્દ્રીય તકેદારી પંચ / केंद्रीय सतर्कता आयोग)`:** Established in 1964 to investigate corruption complaints against central government officers.\n4. **Lokpal & Lokayukta Act, 2013 `(લોકપાલ અને લોકાયુક્ત / लोकपाल और लोकायुक्त)`:**\n   - **Lokpal `(લોકપાલ / लोकपाल)`:** Supreme independent anti-corruption ombudsman at the National/Central level with jurisdiction to investigate allegations against the Prime Minister, Union Ministers, Members of Parliament, and top bureaucrats.\n   - **Lokayukta `(લોકાયુક્ત / लोकायुक्त)`:** Anti-corruption ombudsman established at the State level to investigate state ministers, MLAs, and administrative officials.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM TOP SCORING QUESTION (4 Marks):**\n**Que:** Explain the measures and institutional mechanisms established in India to control corruption.\n\n**Ideal Model Answer Blueprint:**\n1. **Prevention of Corruption Act (1988):** Strict penal provisions for public servants taking bribes.\n2. **Anti-Corruption Bureau (ACB - Toll-free 1064):** Conducting trap operations to catch corrupt employees.\n3. **Central Vigilance Commission (CVC):** Monitoring integrity across central administrative departments.\n4. **Lokpal at Centre & Lokayukta at State:** Autonomous statutory ombudsman bodies investigating high-level political and administrative corruption.\n5. **Right to Information (RTI 2005) & Digital Governance:** E-governance, Direct Benefit Transfer (DBT), and public tracking of tenders.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    # =========================================================================
    # MODULE 5: RIGHT TO INFORMATION (RTI) ACT, 2005
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Before 2005, government offices were surrounded by an iron curtain of secrecy. If a newly built village road broke within two weeks, citizens had no way of knowing how much budget was sanctioned or which contractor built it. But on **12th October 2005**, Indian democracy received its most lethal weapon of transparency: The **Right to Information (RTI) Act `(માહિતી મેળવવાનો અધિકાર / सूचना का अधिकार)`**! Let's explore how a ₹20 application can shake corrupt offices.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "The step-by-step procedure of submitting an RTI application, timeline for response, and the two-tier appellate hierarchy.",
        "image_url": "assets/images/gseb_ss_ch21_rti_flowchart.jpg",
        "alt_text": "RTI Process Flowchart: Application to PIO (30 Days) -> 1st Appeal to Appellate Authority (30 Days) -> 2nd Appeal to SIC/CIC (90 Days)"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 8. Objectives & Core Principles of RTI Act, 2005 `(આર.ટી.આઈ. કાયદાના ઉદ્દેશો અને જોગવાઈઓ / सूचना के अधिकार के उद्देश्य)`\n\nThe **Right to Information Act, 2005** came into force nationwide on **12th October 2005**. \n\n### Primary Objectives of RTI:\n- **Transparency `(પારદર્શિતા / पारदर्शिता)`:** Opening government files, records, vouchers, and contracts for public scrutiny.\n- **Accountability `(જવાબદેહી / जवाबदेही)`:** Making every public servant answerable to the tax-paying public.\n- **Containment of Corruption `(ભ્રષ્ટાચાર પર અંકુશ / भ्रष्टाचार पर नियंत्रण)`:** Eliminating under-the-table bribery by creating verifiable digital records.\n- **Citizen Empowerment `(નાગરિક સશક્તિકરણ / नागरिक सशक्तिकरण)`:** Enabling common citizens to participate actively in democratic governance.\n\n### What Can a Citizen Inspect Under RTI?\n- Certified copies of official documents, records, memos, circulars, and contracts.\n- Inspection of government works (e.g. measuring road thickness, testing concrete samples of a public school building).\n- Obtaining certified samples of construction material and electronic records (CDs, pen drives, printouts).",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 9. Step-by-Step Procedure for Filing RTI `(આર.ટી.આઈ. અરજી કરવાની પદ્ધતિ / आरटीआई आवेदन की प्रक्रिया)`\n\n1. **Submission of Application:**\n   - The applicant submits an application in writing or online in English, Hindi, or Gujarati to the **Public Information Officer (PIO) / Public Relation Officer `(જન માહિતી અધિકારી / लोक सूचना अधिकारी)`**.\n   - Application fee: A nominal fee of **₹20** (via Court fee stamp, Demand Draft, or cash receipt). \n   - **Fee Exemption:** Citizens living **Below Poverty Line (BPL) `(ગરીબી રેખા હેઠળના નાગરિકો / गरीबी रेखा से नीचे)`** do NOT have to pay any application fee.\n2. **Strict Time Limits for Information Provision:**\n   - **Normal Cases:** The PIO must provide the requested information within **30 days `(30 દિવસ / 30 दिन)`** from the date of application receipt.\n   - **Matters Involving Life or Personal Liberty `(જીવન કે વ્યક્તિગત સ્વાતંત્ર્ય સાથે સંકળાયેલી બાબત / जीवन या व्यक्तिगत स्वतंत्रता)`:** Information MUST be provided within **48 hours `(48 કલાક / 48 घंटे)`**.\n3. **Appellate Mechanism `(અપીલ પદ્ધતિ / अपील की व्यवस्था)`:**\n   - **First Appeal `(પ્રથમ અપીલ / प्रथम अपील)`:** If information is denied or not provided within 30 days, the applicant can file an appeal before the senior **Appellate Authority `(અપીલ સત્તાધિકારી / अपीलीय प्राधिकारी)`** within **30 days**.\n   - **Second Appeal `(બીજી અપીલ / द्वितीय अपील)`:** If still dissatisfied with the First Appellate decision, a second appeal can be filed before the independent **State Information Commission (SIC) `(રાજ્ય માહિતી પંચ / राज्य सूचना आयोग)`** or **Central Information Commission (CIC)** within **90 days**.\n\n### Exemptions Under Section 8 `(માહિતી ન આપવાની જોગવાઈઓ / सूचना न देने के प्रावधान)`:\nInformation can be legally withheld if disclosure harms:\n- National sovereignty, integrity, and strategic military/defense secrets `(રાષ્ટ્રનું સાર્વભૌમત્વ અને સુરક્ષા / राष्ट्र की संप्रभुता और सुरक्षा)`.\n- Secret intelligence information or pending criminal investigations.\n- Matters under judicial contempt or trade secrets `(વ્યાપારિક ગોપનીયતા / व्यापारिक गोपनीयता)`.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "mcq",
        "question": "Under the RTI Act 2005, within how many hours must a Public Information Officer (PIO) provide information if the matter concerns an individual's life or personal liberty?",
        "options": [
            "24 hours",
            "48 hours",
            "7 days",
            "30 days"
        ],
        "correct_answer": "48 hours",
        "explanation": "Section 7(1) of the RTI Act mandates that if the information sought concerns the life or liberty of a person, it must be provided within 48 hours of receiving the request."
    })

    # =========================================================================
    # MODULE 6: RIGHT TO EDUCATION (RTE) ACT, 2009
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 10. Right of Children to Free and Compulsory Education (RTE) Act, 2009 `(શિક્ષણનો અધિકાર કાયદો - આર.ટી.ઈ. / शिक्षा का अधिकार अधिनियम)`\n\nTo fulfill the vision of universal literacy, the Indian Parliament added **Article 21-A** to the Constitution via the 86th Constitutional Amendment, establishing education as a Fundamental Right. Following this, the **RTE Act, 2009** was enacted and came into force on **1st April 2010**.\n\n### Salient Provisions of the RTE Act:\n1. **Free & Compulsory Elementary Education:** Every child between **6 and 14 years** of age has the fundamental right to free admission, attendance, and completion of elementary education (Class 1 to 8) in a neighborhood school.\n2. **25% Quota in Private Unaided Schools `(ખાનગી શાળાઓમાં 25% અનામત / निजी स्कूलों में 25% आरक्षण)`:** Mandatory reservation of at least **25% of seats in Class 1** in private schools for children from Economically Weaker Sections (EWS) and Disadvantaged Groups. The government reimburses their fees.\n3. **Prohibition of Screening & Capitation Fees:**\n   - Schools cannot charge any **Capitation Fee `(કેપિટેશન ફી / कैपिटेशन फीस)`** (fine up to 10 times the fee charged).\n   - No screening tests or parent interviews for admissions.\n4. **No Detention & Child-Friendly Learning Environment:**\n   - Strict ban on **Physical Punishment and Mental Harassment `(શારીરિક શિક્ષા અને માનસિક ત્રાસ પર પ્રતિબંધ / शारीरिक दंड और मानसिक प्रताड़ना पर प्रतिबंध)`**.\n   - Prescribed Pupil-Teacher Ratio (PTR): **1:30** for Primary (Classes 1–5) and **1:35** for Upper Primary (Classes 6–8).\n   - Mandatory all-weather school building, separate toilets for boys and girls, clean drinking water, playground, and barrier-free ramps.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM HOT SPOT (3 Marks):**\n**Que:** State any three major student-friendly provisions of the Right to Education (RTE) Act, 2009.\n\n**Scoring Points:**\n1. Free and compulsory elementary education for children aged 6–14 years (Article 21-A).\n2. 25% reservation in private un-aided primary schools for underprivileged/poor children.\n3. Complete legal prohibition on physical punishment, mental harassment, capitation fee, and admission screening tests.",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    # =========================================================================
    # MODULE 7: NATIONAL FOOD SECURITY ACT (NFSA), 2013 & MAA ANNAPURNA
    # =========================================================================
    blocks.append({
        "type": "hook",
        "content": "Can a nation truly progress if millions of its citizens sleep on an empty stomach? Food is the first biological necessity of life. To ensure nutritional security and banish chronic hunger forever, India enacted one of the world's largest welfare laws in 2013: The **National Food Security Act (NFSA)**! Let's understand how subsidized grain reaches every poor household.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "Targeted Public Distribution System (TPDS) framework under NFSA 2013 providing food security to Antyodaya and Priority Households.",
        "image_url": "assets/images/gseb_ss_ch21_nfsa_pds.jpg",
        "alt_text": "Pillars of NFSA 2013: AAY 35kg/family, PHH 5kg/person, Mid-Day Meal, and Women Empowerment via Ration Cards"
    })
    
    blocks.append({
        "type": "theory",
        "content": "### 11. National Food Security Act (NFSA), 2013 `(રાષ્ટ્રીય અન્ન સલામતી કાયદો / राष्ट्रीय खाद्य सुरक्षा अधिनियम)`\n\nEnacted on **5th July 2013**, the **NFSA** legally transforms the welfare approach of food security into a legal right for up to **75% of rural population** and **50% of urban population** across India.\n\n### Categorization of Beneficiaries & Entitlements:\n1. **Antyodaya Anna Yojana (AAY) Families `(અંત્યોદય અન્ન યોજના / अंत्योदय अन्न योजना)`:**\n   - Poorest of the poor families receive **35 kg foodgrains per family per month**.\n2. **Priority Households (PHH) `(અગ્રતા ધરાવતા કુટુંબો / प्राथमिकता वाले परिवार)`:**\n   - Each individual member receives **5 kg foodgrains per person per month**.\n   - **Highly Subsidized Prices:** Rice at **₹3/kg**, Wheat at **₹2/kg**, and Coarse Grains `(જાડા અનાજ / मोटे अनाज)` at **₹1/kg** (Provided free under ongoing central/state welfare extensions).\n\n### Gujarat Government's 'Maa Annapurna Yojana' `(મા અન્નપૂર્ણા યોજના / माँ अन्नपूर्णा योजना)`:\n- Launched in Gujarat in **April 2016** to implement NFSA with maximum efficiency.\n- Ensures that eligible poor and middle-class families in urban and rural Gujarat receive quality foodgrains at nominal rates through Fair Price Shops (FPS) `(વાજબી ભાવની દુકાનો / उचित मूल्य की दुकानें)`.\n\n### Special Provisions for Women & Child Nutrition:\n- **Maternity Nutritional Support:** Pregnant women and lactating mothers are entitled to free meals during pregnancy and 6 months post-childbirth, along with a maternity cash benefit of at least **₹6,000**.\n- **Child Nutrition:** Nutritious hot cooked meals for children aged 6 months to 14 years through Anganwadis and the **Mid-Day Meal Scheme (PM POSHAN) `(મધ્યાહન ભોજન યોજના / मध्याह्न भोजन योजना)`**.\n- **Women Empowerment:** The **eldest woman** of 18 years or above in every eligible household is recognized as the **Head of the Household `(કુટુંબના વડા / परिवार की मुखिया)`** for the purpose of issuing ration cards.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })
    
    blocks.append({
        "type": "mcq",
        "question": "Under the National Food Security Act (NFSA 2013), how much foodgrain is entitled to each Antyodaya Anna Yojana (AAY) family per month?",
        "options": [
            "10 kg per family",
            "20 kg per family",
            "35 kg per family",
            "50 kg per family"
        ],
        "correct_answer": "35 kg per family",
        "explanation": "Under NFSA 2013, the poorest Antyodaya Anna Yojana (AAY) families receive 35 kg of foodgrains per family per month, while Priority Households (PHH) receive 5 kg per person per month."
    })

    # =========================================================================
    # MODULE 8: INTEGRATED BOARD EXAM HOTS & CHAPTER SUMMARY
    # =========================================================================
    blocks.append({
        "type": "theory",
        "content": "### 12. Chapter Revision Matrix (Quick Board Summary)\n\n| Topic / Legislation | Year Enacted | Key Statutory Highlight | Toll-free / Key Benchmark |\n| :--- | :--- | :--- | :--- |\n| **Human Rights Declaration** | 10 Dec 1948 | Universal human dignity and freedom | Celebrated as Human Rights Day |\n| **Child Labour (Prohibition) Act** | 1986 (Amended 2016) | Total ban under 14 yrs; Hazardous ban 14-18 yrs | **Childline 1098** |\n| **Senior Citizens Maintenance Act** | 2007 | Children legally bound to maintain elderly | **Elder Line 14567** |\n| **Prevention of Corruption Act** | 1988 | Imprisonment 3 to 7 years for bribery | **Gujarat ACB 1064** |\n| **Right to Information (RTI)** | 12 Oct 2005 | 30-day response (48 hrs for life/liberty) | ₹20 fee (Free for BPL) |\n| **Right to Education (RTE)** | 2009 (Enforced 2010) | Free education 6–14 yrs; 25% private quota | Article 21-A |\n| **National Food Security Act** | 2013 | AAY (35 kg/fam), PHH (5 kg/person) | Maa Annapurna Scheme |",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "reflection",
        "content": "### 🌟 Socratic Reflection for the Future Citizen\nLaws, constitutional rights, and welfare acts are only as powerful as the awareness of the citizens who use them. If you notice a 10-year-old child working in a roadside tea-stall during school hours, or an elderly neighbor being neglected, what concrete legal and societal steps will you take today to make a difference?",
        "difficulty": "Advanced",
        "bloom": "Create"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Target Output Paths
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch21.json"
    ncert_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch21.json"
    
    # Ensure directory exists
    os.makedirs(os.path.dirname(gseb_path), exist_ok=True)
    os.makedirs(os.path.dirname(ncert_path), exist_ok=True)
    
    # Write GSEB Chapter JSON
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
        
    # Write NCERT / Unified Chapter JSON with NCERT ID
    ncert_json = dict(final_json)
    ncert_json["metadata"] = dict(final_json["metadata"])
    ncert_json["metadata"]["id"] = "ncert_class10_social_science_ch21"
    
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(ncert_json, f, indent=2, ensure_ascii=False)
        
    print(f"Supreme GSEB SS Chapter 21 generated successfully at:")
    print(f"1. {gseb_path}")
    print(f"2. {ncert_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch21()
