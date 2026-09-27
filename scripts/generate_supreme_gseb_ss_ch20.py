import json
import os

def generate_supreme_gseb_ss_ch20():
    chapter_id = "gseb_class10_social_science_ch20"
    title = "Chapter 20: Social Problems of India and Challenges"
    
    metadata = {
        "id": chapter_id,
        "title": title,
        "subtitle": "The Ultimate Board Exam Mastery Guide",
        "subject": "Social Science",
        "grade": "10",
        "board": "GSEB / NCERT",
        "curriculum": ["GSEB", "NCERT", "CBSE"],
        "language": "English/Hindi/Gujarati (Bilingual)",
        "difficulty": "Advanced",
        "estimated_minutes": 180,
        "version": "3.0.0-SUPREME-SOCIAL-SCIENCE",
        "author": "Antigravity Supreme Intelligence",
        "reviewed_by": "Chief Academic Architect",
        "last_updated": "2026-08-16",
        "tags": [
            "social_science",
            "gseb_class10",
            "social_problems",
            "communalism",
            "casteism",
            "minorities",
            "scheduled_castes",
            "scheduled_tribes",
            "terrorism",
            "naxalism",
            "insurgency",
            "constitutional_provisions",
            "board_special",
            "bilingual"
        ],
        "learning_outcomes": [
            "Understand the multi-cultural fabric of India and the societal hurdles obstructing national unity.",
            "Differentiate between personal religious faith and dangerous communalism `(सांप्रदायिकता / સાંપ્રદાયિકતા)`, and master constitutional remedies to eliminate communal divides.",
            "Analyze the historical evolution of the caste system `(जाति व्यवस्था / જ્ઞાતિ વ્યવસ્થા)` into rigid discrimination and evaluate protective constitutional articles (Articles 15, 16, 17, 25, 46, 330, 332, 341, 342).",
            "Examine the special safeguards and affirmative action mechanisms established for Minorities, Scheduled Castes (SC), and Scheduled Tribes (ST).",
            "Distinguish clearly between localized rebellion/insurgency `(विद्रोह / બળવાખોરી)` and global/cross-border terrorism `(आतंकवाद / આતંકવાદ)` across Kashmir, the North-East, and the Naxalite Red Corridor.",
            "Assess the severe socio-economic impacts of terrorism and detail India's strategic, administrative, intelligence, and socio-economic counter-measures."
        ],
        "ai_context": {
            "learning_goal": "Transform the student into a critically minded board-exam topper on India's sociological dynamics, constitutional safeguards, internal security, and nation-building challenges. Highlighting key articles and points ensures full marks in 4-mark board descriptive questions.",
            "common_misconceptions": [
                "Students confuse personal religion with communalism (Communalism is the political weaponization and intolerance of religion against national solidarity).",
                "Students confuse Insurgency with Terrorism (Insurgency is a regional struggle against state authority with local roots; Terrorism is intentional violence targeting innocent civilians with cross-border linkages and global motives).",
                "Students mix up Article 17 (Abolition of Untouchability) with Article 15 (Prohibition of discrimination on grounds of religion, race, caste, sex, or place of birth).",
                "Students assume Naxalism originated in Kashmir or the North-East (It originated in Naxalbari village, West Bengal in 1967 under Charu Majumdar and Kanu Sanyal)."
            ],
            "tutor_hint": "When explaining constitutional safeguards, use the 'Constitutional Shield' mnemonic. For distinctions between Insurgency and Terrorism, emphasize geographical scope, civilian targeting, and external backing."
        }
    }
    
    blocks = []
    
    # ==========================================
    # MODULE 1: THE SOCRATIC HOOK & DIVERSITY OF INDIA
    # ==========================================
    blocks.append({
        "type": "hook",
        "content": "Imagine a vibrant tapestry woven with thousands of distinct threads—different languages `(भाषाएं / ભાષાઓ)`, faiths `(धर्म / ધર્મો)`, castes `(जातियां / જ્ઞાતિઓ)`, and traditions `(परंपराएं / પરંપરાઓ)`. That magnificent mosaic is **India (भारत / ભારત)**! For thousands of years, India has stood as a beacon of **Unity in Diversity (विविधता में एकता / વિવિધતામાં એકતા)** and peaceful coexistence `(शांतिपूर्ण सह-अस्तित्व / શાંતિપૂર્ણ સહઅસ્તિત્વ)`. \n\nYet, today our nation faces grave challenges that threaten to tear this fabric apart: **Communalism `(सांप्रदायिकता / સાંપ્રદાયિકતા)`**, **Casteism `(जातिवाद / જ્ઞાતિવાદ)`**, and **Terrorism `(आतंकवाद / આતંકવાદ)`**. How did a land of universal tolerance `(सर्वधर्म समभाव / સર્વધર્મ સમભાવ)` become vulnerable to these social fractures, and how does the Indian Constitution protect our democracy? Let us embark on this crucial journey.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })
    
    blocks.append({
        "type": "diagram",
        "content": "A visual concept map showing the foundational pillar of Indian Democracy—Unity in Diversity—contrasted against the three destructive social forces: Communalism, Caste Discrimination, and Terrorism.",
        "image_url": "assets/images/gseb_ss_ch20_social_challenges_overview.jpg",
        "alt_text": "Diagram depicting India's social fabric under challenge by Communalism, Casteism, and Terrorism."
    })
    
    blocks.append({
        "type": "ai_tutor_prompt",
        "content": "Let's test your conceptual intuition: If a person deeply loves their own religion, does that make them 'communal'?",
        "options": [
            "Yes, because showing devotion to one religion automatically hurts other religions.",
            "No, personal faith is a fundamental right; communalism only begins when one considers their religion superior and opposes or harms other communities.",
            "Yes, true secularism means abandoning all religious practices."
        ],
        "correct_answer": "No, personal faith is a fundamental right; communalism only begins when one considers their religion superior and opposes or harms other communities.",
        "explanation": "Having personal religious faith `(धार्मिक आस्था / ધાર્મિક આસ્થા)` is protected by the Constitution (Article 25). Communalism `(सांप्रदायिकता / સાંપ્રદાયિકતા)` is a narrow, intolerant mindset that prioritizes one's religious group above the nation and creates hostility towards other communities."
    })

    blocks.append({
        "type": "theory",
        "content": "### Social Structure of India `(भारत की सामाजिक संरचना / ભારતનું સામાજિક માળખું)`\nIndia's social framework is uniquely characterized by immense diversity `(विविधता / વિવિધતા)` in language, culture, race, and religion. As a developing nation transitioning from a traditional feudal setup to an egalitarian modern democracy `(समतामूलक आधुनिक लोकतंत्र / સમાનતાવાદી આધુનિક લોકશાહી)`, several historical imbalances and prejudices have surfaced as major social problems.\n\nKey socio-demographic features of India:\n1. **Multi-Religious Coexistence:** Home to Hinduism, Islam, Christianity, Sikhism, Buddhism, Jainism, Zoroastrianism, and Judaism.\n2. **Linguistic Pluralism:** 22 officially recognized languages in the Eighth Schedule of the Constitution, alongside hundreds of dialects.\n3. **Caste & Community Stratification:** Historical social hierarchies that created socio-economic disparities.\n4. **Constitutional Vision:** Preamble `(प्रस्तावना / આમુખ)` guarantees Justice, Liberty, Equality, and Fraternity `(बंधुता / બંધુતા)` to ensure human dignity and national unity.",
        "difficulty": "Beginner",
        "bloom": "Understand"
    })

    # ==========================================
    # MODULE 2: COMMUNALISM — CAUSES, PERILS & REMEDIES
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "### 1. Communalism `(सांप्रदायिकता / સાંપ્રદાયિકતા)`\n**Religion `(धर्म / ધર્મ)`** is a matter of personal faith, reverence, and spiritual pursuit. However, when an individual or group places their sectarian religious identity above the nation's interest and views other religious groups with hatred, suspicion, or hostility, it becomes **Communalism `(सांप्रदायिकता / સાંપ્રદાયિકતા)`**.\n\n#### Manifestations of Communalism:\n* **Narrow Groupism `(संकीर्ण गुटबाजी / સંકુચિત જૂથવાદ)`:** Believing that one's religious interests are completely distinct and opposed to those of other citizens.\n* **Prejudice & Stereotyping `(पूर्वाग्रह और दुर्भावना / પૂર્વગ્રહ અને દ્વેષ)`:** Spreading misinformation and hatred against other communities.\n* **Communal Clashes `(सांप्रदायिक दंगे / કોમી રમખાણો)`:** Violent conflicts resulting in loss of innocent human lives, destruction of public properties, and trauma.\n* **Obstacle to Democracy:** Diverts national attention and resources away from poverty eradication, industrial growth, and educational progress toward mutual conflict.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "Flowchart contrasting the vicious cycle of Communal Friction (Prejudice -> Hate Speech -> Violence -> National Loss) against the virtuous cycle of Secular Harmony (Mutual Respect -> Inclusive Education -> Social Cohesion -> National Prosperity).",
        "image_url": "assets/images/gseb_ss_ch20_communalism_vs_secularism.jpg",
        "alt_text": "Flowchart comparing Communal Friction and Secular Harmony."
    })

    blocks.append({
        "type": "theory",
        "content": "### Measures to Eradicate Communalism `(सांप्रदायिकता दूर करने के उपाय / સાંપ્રદાયિકતા નાબૂદીના ઉપાયો)`\nEliminating communalism is a paramount national imperative requiring concerted action across all sectors of society:\n\n1. **Secular Governance `(धर्मनिरपेक्ष शासन / બિનસાંપ્રદાયિક શાસન)`:**\n   * The State maintains strict religious neutrality. The Constitution prohibits the state from patronizing or discriminating against any faith.\n   * Political parties based strictly on communal agendas must be discouraged, and electoral laws must strictly forbid seeking votes on religious grounds.\n\n2. **Education & Value-Oriented Curriculum `(शिक्षा और नैतिक मूल्य / શિક્ષણ અને નૈતિક મૂલ્યો)`:**\n   * School curricula must incorporate moral values, tolerance, and the common spiritual essence of all religions `(सर्वधर्म समभाव)`.\n   * Morning prayers in schools should highlight universal human brotherhood, patriotism, and scientific temperament `(वैज्ञानिक दृष्टिकोण / વૈજ્ઞાનિક અભિગમ)`.\n\n3. **Positive Role of Mass Media `(संचार माध्यमों की भूमिका / પ્રસાર માધ્યમોની ભૂમિકા)`:**\n   * Television, cinema, print newspapers, and digital media must actively promote communal harmony and avoid sensationalizing sensitive incidents.\n   * Strict deterrence against hateful propaganda on social media `(भड़काऊ प्रचार / ઉશ્કેરણીજનક પ્રચાર)`.\n\n4. **Strict Administrative & Police Action `(प्रशासनिक एवं पुलिस कार्रवाई / વહીવટી અને પોલીસ પગલાં)`:**\n   * Impartial, swift, and stern law enforcement during tensions. Special fast-track courts for prosecuting perpetrators of communal violence.\n\n5. **Youth Empowerment & Civil Society `(युवा शक्ति और सामाजिक संगठन / યુવા શક્તિ અને સામાજિક સંગઠનો)`:**\n   * Channeling the dynamism of youth through NCC, NSS, and sports toward nation-building, cross-cultural understanding, and disaster relief.",
        "difficulty": "Advanced",
        "bloom": "Apply"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Master Examiner Tip for 4-Mark Board Answers:**\nWhen asked to explain *'Measures to overcome communalism'*, structure your answer under clear sub-headings:\n1. Role of Education & Schools\n2. Role of Mass Media & Technology\n3. State & Administrative Actions\n4. Role of Political Parties & Election Laws\n5. Role of Citizens & Youth Organizations\n\nWriting point-wise with clear constitutional terms fetches full 4/4 marks in GSEB & CBSE examinations!",
        "difficulty": "Intermediate",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "memory_trick",
        "content": "**Mnemonic to Remember 5 Anti-Communalism Steps:** **S-M-A-R-T**\n* **S** - **S**ecular State & Politics (No religious vote-bank politics)\n* **M** - **M**edia Responsibility (Promoting harmony, combating fake news)\n* **A** - **A**dministrative Sternness (Neutral police & speedy justice)\n* **R** - **R**eformative Education (Value-based learning in schools)\n* **T** - **T**olerance & Youth Leadership (NCC, NSS, inter-faith youth initiatives)",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "question_text": "Which of the following is NOT an effective and constitutionally sound measure to eradicate communalism from Indian society?",
        "options": [
            "Encouraging value-oriented education and inter-faith understanding in school curricula.",
            "Forming political parties and vote banks exclusively based on specific religious identities.",
            "Utilizing radio, television, and print media to foster communal brotherhood.",
            "Strict and neutral administrative action against hate mongers."
        ],
        "correct_answer": "Forming political parties and vote banks exclusively based on specific religious identities.",
        "explanation": "Forming political parties on religious lines deepens societal divides and promotes communalism `(सांप्रदायिकता)`. The Representation of the People Act forbids seeking votes on religious grounds.",
        "distractor_rationale": "Value education, positive media engagement, and impartial administration are proven remedies to strengthen secular unity.",
        "bloom": "Analyze",
        "difficulty": "Intermediate"
    })

    # ==========================================
    # MODULE 3: CASTEISM & CONSTITUTIONAL SAFEGUARDS
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "### 2. Casteism `(जातिवाद / જ્ઞાતિવાદ)` and Social Inequalities\n\n#### Historical Origin of Caste System:\n* **Ancient Varna System `(प्राचीन वर्ण व्यवस्था / પ્રાચીન વર્ણ વ્યવસ્થા)`:** Originally formulated in the Vedic era based on the division of labour `(श्रम विभाजन / શ્રમ વિભાજન)` and occupational specialization. It consisted of four broad functional categories:\n  1. **Brahmins `(ब्राह्मण)`:** Knowledge, philosophy, religious rituals, and teaching.\n  2. **Kshatriyas `(क्षत्रिय)`:** Defense, administration, governance, and warfare.\n  3. **Vaishyas `(वैश्य)`:** Agriculture, trade, commerce, and animal husbandry.\n  4. **Shudras `(शूद्र)`:** Service and artisanal vocations.\n\n* **Degeneration into Hereditary Casteism:** Over centuries, occupational mobility was replaced by rigid birth-based stratification `(जन्म-आधारित व्यवस्था / જન્મ-આધારિત વ્યવસ્થા)`. Society became fragmented into thousands of sub-castes `(उप-जातियां / પેટા-જ્ઞાતિઓ)`, creating severe socio-economic disparities, practices of untouchability `(अस्पृश्यता / અસ્પૃશ્યતા)`, and institutional exploitation.",
        "difficulty": "Intermediate",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "diagram",
        "content": "A schematic diagram displaying the evolution from Ancient Functional Varna Division (flexible, occupation-based) to Degenerated Rigid Caste Stratification (rigid, birth-based, discriminatory) and modern Constitutional Equalization.",
        "image_url": "assets/images/gseb_ss_ch20_caste_system_evolution.jpg",
        "alt_text": "Schematic comparing Ancient Varna classification with modern Constitutional equality."
    })

    blocks.append({
        "type": "theory",
        "content": "### Key Constitutional Provisions for Equality `(समानता के संवैधानिक प्रावधान / સમાનતાની બંધારણીય જોગવાઈઓ)`\nThe architects of the Indian Constitution, led by **Dr. B.R. Ambedkar**, enacted comprehensive safeguards to dismantle caste inequalities:\n\n1. **Article 14 `(अनुच्छेद 14 / કલમ 14)` — Equality Before Law:**\n   * Guarantees equality before the law and equal protection of the laws to all citizens within India.\n\n2. **Article 15 `(अनुच्छेद 15 / કલમ 15)` — Prohibition of Discrimination:**\n   * Prohibits discrimination against any citizen on grounds of religion, race, caste, sex, or place of birth regarding access to shops, public restaurants, hotels, wells, tanks, and public places.\n   * Enables special provisions for the advancement of socially and educationally backward classes `(सामाजिक और शैक्षणिक रूप से पिछड़े वर्ग)`.\n\n3. **Article 16 `(अनुच्छेद 16 / કલમ 16)` — Equality of Opportunity in Public Employment:**\n   * Guarantees equal opportunity for all citizens in matters of public employment.\n   * Empowers the State to create reservations in appointments for underrepresented backward classes.\n\n4. **Article 17 `(अनुच्छेद 17 / કલમ 17)` — Abolition of Untouchability `(अस्पृश्यता का उन्मूलन / અસ્પૃશ્યતા નાબૂદી)`:**\n   * 'Untouchability' is abolished and its practice in any form is forbidden. The enforcement of any disability arising out of untouchability is a punishable offense under the **Protection of Civil Rights Act**.\n\n5. **Article 25 `(अनुच्छेद 25 / કલમ 25)` — Freedom of Religion & Public Temple Entry:**\n   * Guarantees freedom of conscience and religion, and ensures Hindu religious institutions of a public character are thrown open to all classes and sections of Hindus.\n\n6. **Article 46 `(अनुच्छेद 46 / કલમ 46)` — Directive Principles for Weaker Sections:**\n   * Directs the State to promote with special care the educational and economic interests of the weaker sections of the people, especially Scheduled Castes (SC) and Scheduled Tribes (ST), and protect them from social injustice and all forms of exploitation.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **Board Exam Golden Rule — Never Confuse Article 15 and Article 17!**\n* **Article 15:** Prohibits general discrimination based on religion, race, caste, sex, or birth place.\n* **Article 17:** Specifically outlaws **Untouchability `(अस्पृश्यता / અસ્પૃશ્યતા)`** and makes its practice a cognizable crime.\n* **Article 46:** Directs government welfare policies for educational and economic upliftment of SC, ST, and weaker sections.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    blocks.append({
        "type": "mcq",
        "question_text": "Which Article of the Indian Constitution completely abolishes 'Untouchability' and renders its practice in any form a punishable offense?",
        "options": [
            "Article 14",
            "Article 15",
            "Article 17",
            "Article 46"
        ],
        "correct_answer": "Article 17",
        "explanation": "Article 17 explicitly abolishes untouchability `(अस्पृश्यता / અસ્પૃશ્યતા)` and forbids its practice in any form. Anyone enforcing untouchability is liable for punishment by law.",
        "distractor_rationale": "Article 14 grants equality before law; Article 15 prohibits discrimination in public spaces; Article 46 is a Directive Principle promoting education and economic interests of SC/ST.",
        "bloom": "Remember",
        "difficulty": "Beginner"
    })

    # ==========================================
    # MODULE 4: MINORITIES, SCHEDULED CASTES (SC) & SCHEDULED TRIBES (ST)
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "### 3. Minorities `(अल्पसंख्यक / લઘુમતીઓ)`\nIn any given country or state, a group of people who are numerically less than 50% of the total population and possess distinct linguistic, religious, or ethnic identities are referred to as a **Minority `(अल्पसंख्यक / લઘુમતી)`**.\n\n#### Constitutional Safeguards for Minorities:\n* **National Commission for Minorities `(राष्ट्रीय अल्पसंख्यक आयोग / રાષ્ટ્રીય લઘુમતી પંચ)`:** Established to safeguard minority rights, monitor welfare schemes, and address grievances.\n* **Article 29 `(अनुच्छेद 29 / કલમ 29)` — Protection of Language, Script & Culture:**\n  * Any section of citizens having a distinct language, script, or culture has the right to conserve the same.\n  * No citizen shall be denied admission into any state-aided educational institution on grounds only of religion, race, caste, or language.\n* **Article 30 `(अनुच्छेद 30 / કલમ 30)` — Right to Establish Educational Institutions:**\n  * All minorities, whether based on religion or language, have the right to establish and administer educational institutions of their choice.\n  * The State shall not discriminate against minority institutions while granting financial aid.",
        "difficulty": "Advanced",
        "bloom": "Understand"
    })

    blocks.append({
        "type": "theory",
        "content": "### 4. Scheduled Castes (SC) & Scheduled Tribes (ST) `(અનુસૂચિત જાતિઓ અને અનુસૂચિત જનજાતિઓ)`\n\n#### Legal Identification in the Constitution:\n* **Scheduled Castes (SC) `(अनुच्छेद 341 / કલમ 341)`:** Castes that faced historical untouchability and social isolation, specified by the President of India under **Article 341** in consultation with state Governors.\n* **Scheduled Tribes (ST) `(अनुच्छेद 342 / કલમ 342)`:** Indigenous tribal communities `(Adivasis / આદિવાસીઓ)` living largely in remote, hilly, and forest regions with distinct customs, culture, and dialects, notified by the President under **Article 342**.\n\n#### Comprehensive Safeguards:\n1. **Protective Measures `(सुरक्षात्मक उपाय / રક્ષણાત્મક પગલાં)`:**\n   * **SC/ST (Prevention of Atrocities) Act, 1989:** Strictest penal provisions against atrocities, physical humiliation, or dispossession of land.\n   * **Protection of Tribal Land:** Laws preventing transfer of tribal land to non-tribals to prevent exploitation by money-lenders `(साहूकार / શાહુકારો)`.\n\n2. **Developmental & Educational Measures `(विकास और शैक्षणिक उपाय / વિકાસ અને શૈક્ષણિક પગલાં)`:**\n   * Reservation in government educational institutions and universities.\n   * Post-matric scholarships, free residential schools (Eklavya Model Residential Schools), book banks, and coaching grants.\n   * Sub-plans for tribal areas to build roads, healthcare centers, and clean water supplies.\n\n3. **Political Reservation `(राजनीतिक आरक्षण / રાજકીય અનામત)`:**\n   * **Article 330:** Reservation of seats for Scheduled Castes and Scheduled Tribes in the **Lok Sabha (House of the People)**.\n   * **Article 332:** Reservation of seats for SC and ST in the **State Legislative Assemblies `(विधानसभाएं / વિધાનસભાઓ)`**.\n   * **Local Governance:** Reservation of seats and chairperson posts in Gram Panchayats, Taluka Panchayats, District Panchayats, and Municipalities (under 73rd and 74th Constitutional Amendments).",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "diagram",
        "content": "Diagram illustrating the Three Pillars of Affirmative Action for SC/ST: 1. Protective (Anti-Atrocity Laws), 2. Developmental (Scholarships & Education), 3. Political Representation (Articles 330 & 332).",
        "image_url": "assets/images/gseb_ss_ch20_sc_st_affirmative_action.jpg",
        "alt_text": "Three pillars of constitutional empowerment for SC and ST communities."
    })

    blocks.append({
        "type": "mcq",
        "question_text": "Under which Articles of the Indian Constitution are the lists of Scheduled Castes (SC) and Scheduled Tribes (ST) formally specified by the President?",
        "options": [
            "Article 341 for SC and Article 342 for ST",
            "Article 370 for SC and Article 356 for ST",
            "Article 15 for SC and Article 16 for ST",
            "Article 330 for SC and Article 332 for ST"
        ],
        "correct_answer": "Article 341 for SC and Article 342 for ST",
        "explanation": "The President of India notifies the list of Scheduled Castes under Article 341 and Scheduled Tribes under Article 342 in consultation with state authorities.",
        "distractor_rationale": "Articles 330 and 332 govern political seat reservations in Lok Sabha and Vidhan Sabhas; Articles 15 & 16 guarantee equality.",
        "bloom": "Remember",
        "difficulty": "Intermediate"
    })

    # ==========================================
    # MODULE 5: TERRORISM VS INSURGENCY (REBELLION)
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "### 5. Terrorism: A Grave Challenge to Humanity `(આતંકવાદ: માનવતા સામે ગંભીર પડકાર / आतंकवाद: मानवता के लिए गंभीर चुनौती)`\n**Terrorism `(आतंकवाद / આતંકવાદ)`** is a deliberate, systematic, and unlawful use of violence, fear, and intimidation against innocent civilians and state institutions to achieve ideological, religious, or political goals. It is an organized crime against humanity that operates outside the boundaries of human conscience and civilized international law.\n\n### Crucial Board Distinction: Rebellion / Insurgency vs. Terrorism\n\n| Parameter | Rebellion / Insurgency `(विद्रोह / બળવાખોરી)` | Terrorism `(आतंकवाद / આતંકવાદ)` |\n| :--- | :--- | :--- |\n| **Geographic Scope** | **Regional / Local Problem** (confined to a particular state or region). | **National & Global Problem** (transcends borders, impacting multiple nations). |\n| **Local Support & Roots** | Driven by localized grievances of a section of regional population. | Operates without local popular goodwill; relies on fear and weaponized coercion. |\n| **Target of Violence** | Directed primarily against state government authority, military, or administrative symbols. | Ruthlessly targets **innocent, unarmed civilians**, crowded public places, schools, and markets. |\n| **Cross-Border Ties** | May or may not have external connections; often focused on internal governance issues. | Heavily backed by foreign enemy states, illegal arms smuggling, drug trafficking, and international terror modules. |\n| **Democratic Scope** | Can often be resolved through state-level negotiations, autonomy pacts, and political dialogue. | Rejects democratic processes completely; seeks mass terror, societal destabilization, and extortion. |",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "diagram",
        "content": "A high-clarity comparison matrix showing the fundamental differences between Insurgency (Regional Scope, Grievance-Driven, Local Base) and Terrorism (Global Scope, Civilian Targeting, Proxy War & Terror Financing).",
        "image_url": "assets/images/gseb_ss_ch20_terrorism_vs_insurgency_matrix.jpg",
        "alt_text": "Comparison chart distinguishing Insurgency and Terrorism."
    })

    blocks.append({
        "type": "teacher_tip",
        "content": "💡 **High-Scoring Teacher Insight:**\nQuestions asking *'Differentiate between Insurgency (Rebellion) and Terrorism'* are repeated frequently in 3-mark and 4-mark questions. Always present your answer in a neat 2-column tabular format covering:\n1. Geographical scope (Local vs Global)\n2. Nature of targets (State infrastructure vs Innocent civilians)\n3. External links (Local dissent vs Foreign proxy sponsors)\n4. Resolution methods (Dialogue & accords vs Security action & zero tolerance)",
        "difficulty": "Intermediate",
        "bloom": "Apply"
    })

    # ==========================================
    # MODULE 6: TERRORISM & EXTREMISM IN INDIA
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "### 6. Terrorism and Extremism Landscape in India\nIndia has battled three distinct forms of violent internal security threats:\n\n#### A. Cross-Border Terrorism in Jammu & Kashmir `(जम्मू-कश्मीर में सीमा पार आतंकवाद / જમ્મુ-કાશ્મીરમાં સરહદપારનો આતંકવાદ)`:\n* Following the accession of Jammu & Kashmir to India, Pakistan launched unprovoked wars and subsequently initiated a **Proxy War `(छद्म युद्ध / પ્રોક્સી યુદ્ધ)`** through state-sponsored terrorist outfits (e.g., Lashkar-e-Taiba, Jaish-e-Mohammed).\n* **Tragic Impact:** Infiltration across the Line of Control (LoC), targeting of civilian leaders, security personnel, and the forced exodus of hundreds of thousands of **Kashmiri Pandits `(कश्मीरी पंडितों का विस्थापन)`** who became refugees in their own nation.\n* **National Action:** Iron-fisted counter-insurgency operations, modernization of border fencing, abrogation of special temporary provisions, zero-tolerance policy, and massive developmental integration.\n\n#### B. Insurgency in North-East India `(पूर्वोत्तर भारत में उग्रवाद / પૂર્વોત્તર ભારતમાં બળવાખોરી)`:\n* The North-Eastern region shares long, porous international borders with China, Myanmar, Bangladesh, and Bhutan. Geographic isolation, multi-tribal rivalries, illegal migration, and economic underdevelopment fueled insurgent groups.\n* **Key Insurgent Organizations by State:**\n  * **Assam `(असम)`:** ULFA (United Liberation Front of Asom), NDFB (National Democratic Front of Bodoland).\n  * **Nagaland `(नागालैंड)`:** NSCN (National Socialist Council of Nagaland - Isak-Muivah & Khaplang factions).\n  * **Manipur `(मणिपुर)`:** UNLF (United National Liberation Front), PLA (People's Liberation Army), PREPAK.\n  * **Tripura `(त्रिपुरा)`:** ATTF (All Tripura Tiger Force), NLFT (National Liberation Front of Tripura).\n* **Peace Accords & Integration:** Successful peace agreements (e.g., Bodo Accord, Mizo Peace Accord), infrastructure buildout, and the *Act East Policy* have restored widespread peace.\n\n#### C. Naxalism / Left-Wing Extremism (LWE) `(नक्सलवाद / નક્સલવાદ)`:\n* **Origin:** Began in **1967** in **Naxalbari village** (Darjeeling district, West Bengal) under the leadership of **Charu Majumdar** and **Kanu Sanyal** as a violent agrarian uprising against feudal landlords.\n* **Expansion ('Red Corridor' `(रेड कॉरिडोर / રેડ કોરિડોર)`):** Spread across forested tribal regions of West Bengal, Jharkhand, Bihar, Chhattisgarh, Odisha, Andhra Pradesh, Telangana, and Maharashtra.\n* **Ideology & Nature:** Uses Maoist armed violence to overthrow democratic governance.\n* **Dual Government Strategy:** Security crackdowns (CoBRA commandos, central paramilitary forces) combined with intensive road construction, solar electrification, mobile connectivity, schools, and implementation of the Forest Rights Act.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "diagram",
        "content": "Geographical overview map concept highlighting India's internal security landscape: 1. Jammu & Kashmir (Cross-border proxy terror), 2. North-Eastern States (Tribal insurgent movements), 3. Central & Eastern Red Corridor (Naxalite-Maoist belt).",
        "image_url": "assets/images/gseb_ss_ch20_security_map_india.jpg",
        "alt_text": "Map infographic of internal security regions in India: J&K, North-East, and Naxal Red Corridor."
    })

    blocks.append({
        "type": "mcq",
        "question_text": "In which year and state did the Naxalite movement (Left-Wing Extremism) originate in India?",
        "options": [
            "1947 in Jammu & Kashmir",
            "1967 in Naxalbari village, West Bengal",
            "1984 in Punjab",
            "1991 in Nagaland"
        ],
        "correct_answer": "1967 in Naxalbari village, West Bengal",
        "explanation": "Naxalism originated in 1967 in Naxalbari village of Darjeeling district, West Bengal, spearheaded by Charu Majumdar and Kanu Sanyal.",
        "distractor_rationale": "1947 was Indian Independence; 1984 was Punjab militancy; 1991 was economic reforms.",
        "bloom": "Remember",
        "difficulty": "Beginner"
    })

    # ==========================================
    # MODULE 7: SOCIO-ECONOMIC IMPACTS & COUNTERMEASURES
    # ==========================================
    blocks.append({
        "type": "theory",
        "content": "### 7. Social and Economic Impacts of Terrorism `(આતંકવાદની સામાજિક અને આર્થિક અસરો / आतंकवाद के सामाजिक और आर्थिक प्रभाव)`\n\n#### A. Social Impacts of Terrorism `(सामाजिक प्रभाव / સામાજિક અસરો)`:\n1. **Destruction of Human Lives & Families:** Tragic demise of innocent civilians, breadwinners, and security personnel, leaving families devastated.\n2. **Atmosphere of Constant Fear & Suspicion:** Destroys mutual trust between communities, breeds suspicion, and shatters centuries of peaceful social coexistence.\n3. **Refugee Crises & Forced Migration:** Millions are forced to abandon their ancestral homes, businesses, and cultural roots (e.g., Kashmiri Pandits).\n4. **Disruption of Education and Social Life:** Closure of schools, colleges, cultural festivals, and community celebrations in violence-hit areas.\n\n#### B. Economic Impacts of Terrorism `(आर्थिक प्रभाव / આર્થિક અસરો)`:\n1. **Diversion of National Resources:** Hundreds of thousands of crores of rupees that could have funded healthcare, schools, poverty eradication, and irrigation are diverted into defense, border surveillance, and security forces.\n2. **Destruction of Infrastructure:** Terrorists target railway tracks, bridges, power grids, telecommunication towers, and government buildings, incurring massive reconstruction costs.\n3. **Collapse of Tourism and Hospitality:** Regions renowned for world-class tourism (like Kashmir and scenic North-East valleys) suffer immediate economic collapse when tourists stay away.\n4. **Flight of Capital and Industries:** Businessmen and investors migrate away from terror-affected zones, leading to factory closures, loss of employment, and local economic stagnation.\n5. **Extortion & Disruption of Trade:** Illegal extortion `(फिरौती / ખંડણી)` and strikes called by terror outfits paralyze daily transport, trade, and market supply chains.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "theory",
        "content": "### India's Comprehensive Counter-Terror Strategy `(આતંકવાદ સામે લડવાની ભારતીય વ્યૂહરચના / आतंकवाद विरोधी भारतीय रणनीति)`\n* **Zero Tolerance Policy `(शून्य सहनशीलता नीति / ઝીરો ટોલરન્સ નીતિ)`:** No dialogue or concessions with perpetrators of terror; stern military, kinetic, and diplomatic response.\n* **Robust Intelligence & Investigation:** Institutionalization of specialized agencies like the **National Investigation Agency (NIA)**, Multi-Agency Centre (MAC), Intelligence Bureau (IB), and RAW.\n* **Modernization of Armed Forces & Police:** State-of-the-art weaponry, night-vision surveillance, cyber-warfare capabilities, and drone technology.\n* **Choking Terror Financing:** Rigorous enforcement of anti-money laundering laws, cooperation with the Financial Action Task Force (FATF), and confiscation of benami properties.\n* **International Diplomacy:** Championing the **Comprehensive Convention on International Terrorism (CCIT)** at the United Nations to isolate state sponsors of terror globally.",
        "difficulty": "Advanced",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "memory_trick",
        "content": "**Mnemonic to Remember Economic Impacts of Terrorism:** **D-I-S-R-U-P-T**\n* **D** - **D**iversion of public budget to defense\n* **I** - **I**nvestment flight & factory closures\n* **S** - **S**tagnation of trade & market supply\n* **R** - **R**econstruction costs for bombed bridges/rails\n* **U** - **U**nemployment and poverty escalation\n* **P** - **P**roperty destruction (public & private)\n* **T** - **T**ourism industry collapse",
        "difficulty": "Beginner",
        "bloom": "Remember"
    })

    # ==========================================
    # MODULE 8: BOARD EXAM MASTERY (PYQs, HOTS & MODEL ANSWERS)
    # ==========================================
    blocks.append({
        "type": "exam_tips",
        "content": "🔥 **BOARD EXAM TOPPER'S BLUEPRINT — FREQUENTLY ASKED BOARD QUESTIONS (PYQs):**\n\n#### Q1. Explain the measures to eradicate communalism from Indian society. (4 Marks)\n**Model Structure:**\n* **Introduction (1 mark):** Define communalism as a narrow mindset that places religious interest above the nation and creates inter-community discord.\n* **Key Measures (2.5 marks):** Point-wise explanation of:\n  1. Secular Governance & ban on communal vote-bank politics.\n  2. Value-based education and multi-faith tolerance in school syllabi.\n  3. Positive, constructive role of mass media and digital platforms.\n  4. Stern administrative and police action.\n  5. Youth channelization via NCC, NSS, and sports.\n* **Conclusion (0.5 mark):** A strong closing sentence on how national integration is essential for India's economic super-power vision.\n\n#### Q2. Explain the socio-economic effects of terrorism. (4 Marks)\n**Model Structure:**\n* Divide answer into two distinct clear sections: **(A) Social Impacts** (Human casualties, atmosphere of fear, refugee displacement, educational disruption) and **(B) Economic Impacts** (Budget diversion, destruction of infrastructure, tourism destruction, industrial flight, unemployment).\n\n#### Q3. What constitutional provisions have been enacted for Scheduled Castes and Scheduled Tribes? (3 Marks)\n**Model Structure:**\n* Mention Articles **15**, **17** (Abolition of Untouchability), **46** (Directive Principle for education & economic promotion), **330 & 332** (Seat reservations in Lok Sabha and Vidhan Sabhas), and **341 & 342** (Presidential listing).",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "common_mistakes",
        "content": "⚠️ **COMMON EXAM MISTAKES TO AVOID:**\n1. **Vague General Answers:** Do NOT just write 'terrorism is bad' or 'people should love each other'. Mention specific constitutional terms like *Secularism*, *Articles 15/17/46/330/341/342*, *Zero Tolerance Policy*, *NIA*, and *Red Corridor*.\n2. **Confusing Insurgent Outfits:** Remember: **ULFA & NDFB** belong to Assam; **NSCN** belongs to Nagaland; **ATTF & NLFT** belong to Tripura.\n3. **Mixing Up Minority Articles:** Remember: **Article 29** protects minority language, script, and culture; **Article 30** gives minorities the right to establish and run educational institutions.",
        "difficulty": "Intermediate",
        "bloom": "Analyze"
    })

    blocks.append({
        "type": "board_questions",
        "content": "### Higher Order Thinking Skills (HOTS) & Assertion-Reasoning Practice:\n\n**Assertion (A):** The Constitution of India provides reservations for Scheduled Castes and Scheduled Tribes in legislative bodies under Articles 330 and 332.\n**Reason (R):** Historical injustices, social isolation, and economic backwardness necessitate guaranteed political representation to ensure inclusive democratic participation.\n\n* **Correct Evaluation:** Both (A) and (R) are true, and (R) is the correct explanation of (A).\n* **Key Takeaway:** Affirmative action in India is a constitutional mechanism designed to remedy structural historical marginalization.",
        "difficulty": "Advanced",
        "bloom": "Evaluate"
    })

    blocks.append({
        "type": "summary",
        "content": "### 5-Minute Rapid Revision Capsule `(द्रुत पुनरावलोकन / ઝડપી પુનરાવર્તન)`:\n* **Communalism `(सांप्रदायिकता / સાંપ્રદાયિકતા)`:** Placing narrow religious identity above the nation. Solved by secularism, value education, responsible media, and firm administration.\n* **Casteism `(जातिवाद / જ્ઞાતિવાદ)`:** Originated from Vedic Varna functional division of labour, degenerated into rigid birth-based discrimination.\n* **Constitutional Bulwarks:** Article 14 (Equality), Article 15 (Anti-discrimination), Article 16 (Equal opportunity), Article 17 (Untouchability abolished), Article 25 (Religious freedom), Article 46 (Weaker sections welfare).\n* **Minorities `(લઘુમતીઓ)`:** Groups <50% population. Protected by Article 29 (Culture conservation) and Article 30 (Educational institutions).\n* **SC/ST Safeguards:** Listed under Articles 341/342; political seats reserved under Articles 330/332; protected by Atrocities Act 1989.\n* **Terrorism vs Insurgency:** Insurgency is regional and grievance-driven; Terrorism is global/national, targets innocent civilians, and is weaponized by foreign proxy states.\n* **Extremism Wings:** J&K Cross-border terror, North-East tribal insurgencies (ULFA, NSCN, ATTF), and Naxalism (started 1967 in Naxalbari, WB).\n* **Combating Terror:** Zero-tolerance policy, intelligence agencies (NIA/IB), international diplomacy (FATF/CCIT), and socio-economic development.",
        "difficulty": "Intermediate",
        "bloom": "Remember"
    })

    final_json = {
        "metadata": metadata,
        "blocks": blocks
    }
    
    # Target output paths requested:
    # 1. app_core/chapters/gseb_class10_social_science_ch20.json
    # 2. app_core/chapters/ncert_class10_social_science_ch20.json
    
    gseb_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/gseb_class10_social_science_ch20.json"
    ncert_path = "/home/ubuntu/Shine_Academy_Naroda/app_core/chapters/ncert_class10_social_science_ch20.json"
    
    os.makedirs(os.path.dirname(gseb_path), exist_ok=True)
    
    # Save GSEB chapter
    with open(gseb_path, "w", encoding="utf-8") as f:
        json.dump(final_json, f, indent=2, ensure_ascii=False)
    print(f"Generated supreme chapter at: {gseb_path}")
    
    # Save NCERT / Universal chapter with matching ID
    ncert_json = dict(final_json)
    ncert_json["metadata"] = dict(final_json["metadata"])
    ncert_json["metadata"]["id"] = "ncert_class10_social_science_ch20"
    with open(ncert_path, "w", encoding="utf-8") as f:
        json.dump(ncert_json, f, indent=2, ensure_ascii=False)
    print(f"Generated supreme chapter at: {ncert_path}")

if __name__ == "__main__":
    generate_supreme_gseb_ss_ch20()
