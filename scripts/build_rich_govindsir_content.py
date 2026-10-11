#!/usr/bin/env python3
import json
import os
import re

CURRICULUM_FILE = 'app_core/curriculum/govindsir_english.json'
CHAPTERS_DIR = 'app_core/chapters'

WORD_PHONETICS = {
    'hello': 'हेलो', 'hi': 'हाय', 'good': 'गुड', 'morning': 'मॉर्निंग', 'afternoon': 'आफ्टरनून',
    'evening': 'इवनिंग', 'night': 'नाइट', 'how': 'हाउ', 'are': 'आर', 'you': 'यू', 'i': 'आई',
    'am': 'ऐम', 'fine': 'फाइन', 'thank': 'थैंक', 'thanks': 'थैंक्स', 'welcome': 'वेलकम',
    'please': 'प्लीज़', 'sorry': 'सॉरी', 'excuse': 'एक्सक्यूज़', 'me': 'मी', 'my': 'माय',
    'name': 'नेम', 'is': 'इज़', 'what': 'व्हॉट', 'where': 'व्हेयर', 'when': 'व्हेन', 'why': 'व्हाय',
    'who': 'हू', 'which': 'व्हिच', 'can': 'कैन', 'could': 'कुड', 'would': 'वुड', 'should': 'शुड',
    'will': 'विल', 'shall': 'शैल', 'may': 'मे', 'might': 'माइट', 'must': 'मस्ट', 'do': 'डू',
    'does': 'डज़', 'did': 'डिड', 'done': 'डन', 'have': 'हैव', 'has': 'हैज़', 'had': 'हैड',
    'be': 'बी', 'been': 'बीन', 'being': 'बीइंग', 'was': 'वॉज़', 'were': 'वर', 'go': 'गो',
    'goes': 'गोज़', 'going': 'गोइंग', 'went': 'वेंट', 'gone': 'गॉन', 'come': 'कम', 'comes': 'कम्स',
    'coming': 'कमिंग', 'came': 'केम', 'see': 'सी', 'saw': 'सॉ', 'seen': 'सीन', 'look': 'लुक',
    'take': 'टेक', 'took': 'टुक', 'taken': 'टेकन', 'give': 'गिव', 'gave': 'गेव', 'given': 'गिवन',
    'speak': 'स्पीक', 'spoken': 'स्पोकन', 'speaking': 'स्पीकिंग', 'talk': 'टॉक', 'talking': 'टॉकिंग',
    'learn': 'लर्न', 'learning': 'लर्निंग', 'english': 'इंग्लिश', 'language': 'लैंग्वेज',
    'word': 'वर्ड', 'words': 'वर्ड्स', 'sentence': 'सेंटेंस', 'sentences': 'सेंटेंसेस',
    'daily': 'डेली', 'practice': 'प्रैक्टिस', 'today': 'टुडे', 'yesterday': 'यस्टरडे',
    'tomorrow': 'टुमॉरो', 'now': 'नाउ', 'here': 'हियर', 'there': 'देयर', 'this': 'दिस',
    'that': 'दैट', 'these': 'दीज़', 'those': 'दोज़', 'yes': 'यस', 'no': 'नो', 'not': 'नॉट',
    'always': 'ऑलवेज़', 'very': 'वेरी', 'much': 'मच', 'more': 'मोर', 'most': 'मोस्ट',
    'all': 'ऑल', 'some': 'सम', 'friend': 'फ्रेंड', 'friends': 'फ्रेंड्स', 'family': 'फैमिली',
    'father': 'फादर', 'mother': 'मदर', 'brother': 'ब्रदर', 'sister': 'सिस्टर', 'work': 'वर्क',
    'office': 'ऑफिस', 'job': 'जॉब', 'school': 'स्कूल', 'college': 'कॉलेज', 'teacher': 'टीचर',
    'student': 'स्टूडेंट', 'market': 'मार्केट', 'shop': 'शॉप', 'money': 'मनी', 'price': 'प्राइस',
    'water': 'वॉटर', 'food': 'फूड', 'restaurant': 'रेस्टोरेंट', 'bill': 'बिल', 'hotel': 'होटल',
    'bus': 'बस', 'train': 'ट्रेन', 'ticket': 'टिकट', 'help': 'हेल्प', 'sir': 'सर',
    'madam': 'मैडम', 'call': 'कॉल', 'phone': 'फ़ोन', 'meeting': 'मीटिंग', 'interview': 'इंटरव्यू',
    'question': 'क्वेश्चन', 'answer': 'आंसर', 'right': 'राइट', 'wrong': 'रॉन्ग', 'confidence': 'कॉन्फिडेंस',
    'confident': 'कॉन्फिडेंट', 'fluent': 'फ्लूएंट', 'fluency': 'फ्लूएंसी', 'pronunciation': 'प्रनन्सिएशन',
    'grammar': 'ग्रामर', 'polite': 'पोलाइट', 'professional': 'प्रोफेशनल', 'time': 'टाइम',
    'about': 'अबाउट', 'with': 'विद', 'from': 'फ्रॉम', 'at': 'एट', 'in': 'इन', 'on': 'ऑन',
    'for': 'फॉर', 'by': 'बाय', 'to': 'टू', 'of': 'ऑफ', 'and': 'एंड', 'or': 'ऑर', 'but': 'बट',
    'we': 'वी', 'they': 'दे', 'he': 'ही', 'she': 'शी', 'it': 'इट', 'our': 'अवर', 'their': 'देयर',
    'his': 'हिज़', 'her': 'हर', 'its': 'इट्स', 'me': 'मी', 'us': 'अस', 'them': 'देम', 'him': 'हिम'
}

def to_devanagari(text):
    if not text:
        return ""
    cleaned = re.sub(r'\[(?:DICT_[A-Z0-9_]+\|)?([^\]]+)\]', r'\1', text)
    cleaned = re.sub(r'[*_#`~]', '', cleaned)
    words = cleaned.split()
    res = []
    for w in words:
        m = re.match(r'^([^\w]*)(.*?)([^\w]*)$', w)
        if not m:
            res.append(w)
            continue
        pre, core, post = m.group(1), m.group(2).lower(), m.group(3)
        if not core:
            res.append(w)
            continue
        dev = WORD_PHONETICS.get(core)
        if not dev:
            dev = core
            for src, dst in [
                ('tion', 'शन'), ('sion', 'श़न'), ('ph', 'फ़'), ('th', 'थ'), ('sh', 'श'),
                ('ch', 'च'), ('ck', 'क'), ('ee', 'ई'), ('oo', 'ऊ'), ('ea', 'ई'), ('ou', 'आउ'),
                ('ai', 'ऐ'), ('ay', 'ए'), ('wh', 'व्ह'), ('qu', 'क्व'), ('kn', 'न'),
                ('wr', 'र'), ('ing', 'इंग'), ('ed', 'ड'), ('er', 'र'), ('or', 'र'),
                ('ar', 'आर'), ('b', 'ब'), ('c', 'क'), ('d', 'ड'), ('f', 'फ'), ('g', 'ग'),
                ('h', 'ह'), ('j', 'ज'), ('k', 'क'), ('l', 'ल'), ('m', 'म'), ('n', 'न'),
                ('p', 'प'), ('q', 'क'), ('r', 'र'), ('s', 'स'), ('t', 'ट'), ('v', 'व'),
                ('w', 'व'), ('x', 'क्स'), ('y', 'य'), ('z', 'ज़'), ('a', 'ए'), ('e', 'इ'),
                ('i', 'इ'), ('o', 'ओ'), ('u', 'अ')
            ]:
                dev = dev.replace(src, dst)
        if post == '.':
            post = '।'
        res.append(f"{pre}{dev}{post}")
    return " ".join(res)

def get_level(ch_num):
    if ch_num <= 20:
        return 1, "Level 1: Beginner Foundation", "लेवल 1: शुरुआती आधार", "લેવલ 1: પ્રારંભિક પાયો"
    elif ch_num <= 40:
        return 2, "Level 2: Intermediate Everyday Fluency", "लेवल 2: दैनिक बातचीत और आत्मविश्वास", "લેવલ 2: દૈનિક વાતચીત અને આત્મવિશ્વાસ"
    else:
        return 3, "Level 3: Professional & Career Mastery", "लेवल 3: प्रोफेशनल और करियर महारत", "લેવલ 3: પ્રોફેશનલ અને કરિયર નિપુણતા"

# Condense long paragraphs into bite-sized spoken phrases for adult beginners
def condense_theory_text(text):
    if len(text) <= 220:
        return text
    clean = re.sub(r'\[(?:DICT_[A-Z0-9_]+\|)?([^\]]+)\]', r'\1', text)
    sentences = [s.strip() for s in re.split(r'(?<=[.!?])\s+', clean) if s.strip()]
    if not sentences:
        return text[:180] + "..."
    condensed = " ".join(sentences[:2])
    if len(condensed) > 220:
        condensed = sentences[0]
    return condensed

# 12 Universal situational scenarios tailored per level and chapter topic
def build_situational_questions(ch_num, title, level):
    clean_title = re.sub(r'Chapter\s+No\s+\d+:\s*', '', title)
    clean_title = re.sub(r'Grammar:\s*', '', clean_title).strip()
    
    questions = []
    
    # Specific targeted situational questions based on chapter level & title
    if level == 1:
        # Beginner Foundation Situations
        scenarios = [
            (
                f"How do you politely greet someone in English regarding '{clean_title}'?",
                f"'{clean_title}' के संदर्भ में किसी का अंग्रेज़ी में विनम्र अभिवादन कैसे करें?",
                f"'{clean_title}' ના સંદર્ભમાં અંગ્રેજીમાં કોઈનું નમ્ર અભિવાદન કેવી રીતે કરશો?",
                [
                    "Good morning! Nice to meet you.",
                    "Hey, tell me right now.",
                    "Why are you here?",
                    "Say nothing."
                ],
                [
                    "शुभ प्रभात! आपसे मिलकर अच्छा लगा। (Good morning! Nice to meet you.)",
                    "अरे, मुझे अभी बताओ।",
                    "तुम यहाँ क्यों हो?",
                    "कुछ न कहें।"
                ],
                [
                    "શુભ સવાર! તમને મળીને આનંદ થયો. (Good morning! Nice to meet you.)",
                    "અરે, મને હમણાં જ કહો.",
                    "તમે અહીં કેમ છો?",
                    "કંઈ બોલશો નહીં."
                ],
                0,
                "Using 'Good morning! Nice to meet you' sets a respectful, warm tone in any situation.",
                "'Good morning! Nice to meet you' किसी भी स्थिति में सम्मानजनक और आत्मीय माहौल बनाता है।",
                "'Good morning! Nice to meet you' કોઈપણ પરિસ્થિતિમાં આદરપૂર્ણ અને સ્નેહપૂર્ણ વાતાવરણ બનાવે છે."
            ),
            (
                f"When introducing yourself while practicing '{clean_title}', which sentence is correct?",
                f"'{clean_title}' का अभ्यास करते समय अपना परिचय देने के लिए कौन सा वाक्य सही है?",
                f"'{clean_title}' ની પ્રેક્ટિસ કરતી વખતે તમારો પરિચય આપવા માટે કયું વાક્ય સાચું છે?",
                [
                    "Myself Amit from Naroda.",
                    "My name is Amit, and I live in Naroda.",
                    "I is Amit Naroda.",
                    "Mine name Amit."
                ],
                [
                    "मायसेल्फ अमित फ्रॉम नरोडा। (अशुद्ध)",
                    "माय नेम इज़ अमित, एंड आई लिव इन नरोडा। (My name is Amit, and I live in Naroda.)",
                    "आई इज़ अमित नरोडा।",
                    "माइन नेम अमित।"
                ],
                [
                    "માયસેલ્ફ અમિત ફ્રોમ નરોડા. (અશુદ્ધ)",
                    "માય નેમ ઇઝ અમિત, એન્ડ આઇ લિવ ઇન નરોડા. (My name is Amit, and I live in Naroda.)",
                    "આઇ ઇઝ અમિત નરોડા.",
                    "માઇન નેમ અમિત."
                ],
                1,
                "Always say 'My name is...' or 'I am...'. Never use 'Myself...' for introducing yourself.",
                "हमेशा 'My name is...' या 'I am...' कहें। परिचय देने के लिए 'Myself...' का प्रयोग कभी न करें।",
                "હંમેશાં 'My name is...' અથવા 'I am...' કહો. પરિચય આપવા માટે 'Myself...' નો ઉપયોગ ક્યારેય ન કરશો."
            ),
            (
                f"How do you ask for simple help when learning '{clean_title}'?",
                f"'{clean_title}' सीखते समय सहायता मांगने का सबसे विनम्र तरीका क्या है?",
                f"'{clean_title}' શીખતી વખતે મદદ માંગવાની સૌથી નમ્ર રીત કઈ છે?",
                [
                    "Help me fast.",
                    "Could you please explain this to me once more?",
                    "You must tell me now.",
                    "Why don't you help?"
                ],
                [
                    "मेरी जल्दी मदद करो।",
                    "क्या आप कृपया मुझे यह एक बार और समझा सकते हैं? (Could you please explain this to me once more?)",
                    "तुम्हें मुझे अभी बताना होगा।",
                    "तुम मदद क्यों नहीं करते?"
                ],
                [
                    "મારી ઝડપથી મદદ કરો.",
                    "શું તમે કૃપા કરીને મને આ વધુ એક વાર સમજાવી શકો? (Could you please explain this to me once more?)",
                    "તમારે મને હમણાં જ કહેવું પડશે.",
                    "તમે મદદ કેમ નથી કરતા?"
                ],
                1,
                "'Could you please...' is the most polite and respected way to ask for assistance.",
                "'Could you please...' मदद मांगने का सबसे विनम्र और सम्मानित तरीका है।",
                "'Could you please...' મદદ માંગવાની સૌથી નમ્ર અને આદરપૂર્ણ રીત છે."
            ),
            (
                f"When someone thanks you for your assistance with '{clean_title}', how should you respond?",
                f"जब कोई '{clean_title}' में आपकी मदद के लिए धन्यवाद कहे, तो आपको क्या जवाब देना चाहिए?",
                f"જ્યારે કોઈ '{clean_title}' માં તમારી મદદ માટે આભાર માને, ત્યારે તમારે શું જવાબ આપવો જોઈએ?",
                [
                    "You're welcome! Glad I could help.",
                    "No problem, you owe me.",
                    "Don't disturb me again.",
                    "Ignore them."
                ],
                [
                    "आपका स्वागत है! खुशी हुई कि मैं मदद कर सका। (You're welcome! Glad I could help.)",
                    "कोई बात नहीं, अब आप मेरे कर्जदार हैं।",
                    "मुझे दोबारा परेशान मत करना।",
                    "उन्हें अनदेखा करें।"
                ],
                [
                    "તમારું સ્વાગત છે! આનંદ થયો કે હું મદદ કરી શક્યો. (You're welcome! Glad I could help.)",
                    "વાંધો નહીં, હવે તમે મારા કરજદાર છો.",
                    "મને ફરીથી હેરાન ન કરશો.",
                    "તેમની અવગણના કરો."
                ],
                0,
                "'You're welcome! Glad I could help' displays genuine warmth and social manners.",
                "'You're welcome! Glad I could help' सच्ची आत्मीयता और सामाजिक शिष्टाचार दर्शाता है।",
                "'You're welcome! Glad I could help' સાચી આત્મીયતા અને સામાજિક શિષ્ટાચાર દર્શાવે છે."
            ),
            (
                f"Which sentence expresses daily confidence in '{clean_title}'?",
                f"'{clean_title}' में दैनिक आत्मविश्वास व्यक्त करने वाला वाक्य कौन सा है?",
                f"'{clean_title}' માં દૈનિક આત્મવિશ્વાસ વ્યક્ત કરતું વાક્ય કયું છે?",
                [
                    "I can never learn this language.",
                    "I practice speaking English for 15 minutes every day.",
                    "English is only for foreigners.",
                    "I will only read books silently."
                ],
                [
                    "मैं यह भाषा कभी नहीं सीख सकता।",
                    "मैं हर दिन 15 मिनट अंग्रेज़ी बोलने का अभ्यास करता हूँ। (I practice speaking English for 15 minutes every day.)",
                    "अंग्रेज़ी केवल विदेशियों के लिए है।",
                    "मैं केवल चुपचाप किताबें पढूँगा।"
                ],
                [
                    "હું આ ભાષા ક્યારેય શીખી શકીશ નહીં.",
                    "હું દરરોજ 15 મિનિટ અંગ્રેજી બોલવાની પ્રેક્ટિસ કરું છું. (I practice speaking English for 15 minutes every day.)",
                    "અંગ્રેજી ફક્ત વિદેશીઓ માટે છે.",
                    "હું માત્ર શાંતિથી પુસ્તકો વાંચીશ."
                ],
                1,
                "Daily 15-minute speaking practice is the proven secret to building permanent fluency.",
                "प्रतिदिन 15 मिनट बोलने का अभ्यास स्थायी प्रवाह हासिल करने का सिद्ध रहस्य है।",
                "દરરોજ 15 મિનિટ બોલવાની પ્રેક્ટિસ કાયમી ફ્લુઅન્સી મેળવવાનું સાબિત થયેલું રહસ્ય છે."
            ),
            (
                f"If you did not hear what someone said regarding '{clean_title}', what should you say?",
                f"यदि आपने '{clean_title}' के बारे में किसी की बात नहीं सुनी, तो आपको क्या कहना चाहिए?",
                f"જો તમે '{clean_title}' વિશે કોઈની વાત સાંભળી ન હોય, તો તમારે શું કહેવું જોઈએ?",
                [
                    "What? Speak loudly!",
                    "Pardon me, could you please repeat that?",
                    "Say again fast.",
                    "I don't care."
                ],
                [
                    "क्या? ज़ोर से बोलो!",
                    "क्षमा करें, क्या आप कृपया इसे दोहरा सकते हैं? (Pardon me, could you please repeat that?)",
                    "जल्दी फिर से बोलो।",
                    "मुझे परवाह नहीं है।"
                ],
                [
                    "શું? મોટેથી બોલો!",
                    "માફ કરશો, શું તમે કૃપા કરીને તે ફરીથી કહી શકશો? (Pardon me, could you please repeat that?)",
                    "ઝડપથી ફરી કહો.",
                    "મને કોઈ પડી નથી."
                ],
                1,
                "'Pardon me, could you please repeat that?' is the universal polite request for repetition.",
                "'Pardon me, could you please repeat that?' बात दोहराने का अनुरोध करने का विश्वव्यापी विनम्र तरीका है।",
                "'Pardon me, could you please repeat that?' વાત પુનરાવર્તિત કરવાની વિનંતી કરવાની વિશ્વવ્યાપી નમ્ર રીત છે."
            ),
            (
                f"How do you ask about someone's well-being in relation to '{clean_title}'?",
                f"'{clean_title}' के संदर्भ में किसी का हाल-चाल कैसे पूछें?",
                f"'{clean_title}' ના સંદર્ભમાં કોઈના ખબર-અંતર કેવી રીતે પૂછશો?",
                [
                    "How are you doing today?",
                    "Why are you sitting like that?",
                    "What is your problem?",
                    "Who are you to me?"
                ],
                [
                    "आज आप कैसे हैं? (How are you doing today?)",
                    "तुम ऐसे क्यों बैठे हो?",
                    "तुम्हारी समस्या क्या है?",
                    "तुम मेरे क्या लगते हो?"
                ],
                [
                    "આજે તમે કેમ છો? (How are you doing today?)",
                    "તમે કેમ આમ બેઠા છો?",
                    "તમારી સમસ્યા શું છે?",
                    "તમે મારા શું થાવ છો?"
                ],
                0,
                "'How are you doing today?' is polite, friendly, and perfect for daily conversations.",
                "'How are you doing today?' विनम्र, मिलनसार और दैनिक बातचीत के लिए उत्तम है।",
                "'How are you doing today?' નમ્ર, મૈત્રીપૂર્ણ અને રોજિંદી વાતચીત માટે શ્રેષ્ઠ છે."
            ),
            (
                f"Which response is polite when someone asks 'How are you?'",
                f"जब कोई पूछे 'How are you?', तो कौन सा उत्तर विनम्र है?",
                f"જ્યારે કોઈ પૂછે 'How are you?', ત્યારે કયો જવાબ નમ્ર છે?",
                [
                    "I am fine, thank you! How about you?",
                    "Why do you ask?",
                    "None of your business.",
                    "Not good, go away."
                ],
                [
                    "मैं ठीक हूँ, धन्यवाद! आप कैसे हैं? (I am fine, thank you! How about you?)",
                    "तुम क्यों पूछ रहे हो?",
                    "अपने काम से काम रखो।",
                    "अच्छा नहीं हूँ, चले जाओ।"
                ],
                [
                    "હું મજામાં છું, આભાર! તમે કેમ છો? (I am fine, thank you! How about you?)",
                    "તમે કેમ પૂછો છો?",
                    "તમારા કામથી કામ રાખો.",
                    "સારું નથી, ચાલ્યા જાવ."
                ],
                0,
                "Replying 'I am fine, thank you! How about you?' shows high social etiquette and care.",
                "'I am fine, thank you! How about you?' उच्च सामाजिक शिष्टाचार और सम्मान प्रदर्शित करता है।",
                "'I am fine, thank you! How about you?' ઉચ્ચ સામાજિક શિષ્ટાચાર અને આદર દર્શાવે છે."
            ),
            (
                f"When saying goodbye at the end of practicing '{clean_title}', what is a courteous phrase?",
                f"'{clean_title}' का अभ्यास समाप्त करने के बाद विदा लेते समय कौन सा वाक्यांश विनम्र है?",
                f"'{clean_title}' ની પ્રેક્ટિસ પૂરી કર્યા પછી વિદાય લેતી વખતે કયો વાક્યાંશ નમ્ર છે?",
                [
                    "It was great speaking with you. Have a wonderful day!",
                    "Bye, don't talk to me again.",
                    "I am leaving now, goodbye forever.",
                    "Get out."
                ],
                [
                    "आपसे बात करके बहुत अच्छा लगा। आपका दिन शुभ हो! (It was great speaking with you. Have a wonderful day!)",
                    "बाय, मुझसे दोबारा बात मत करना।",
                    "मैं अब जा रहा हूँ, हमेशा के लिए अलविदा।",
                    "बाहर निकलो।"
                ],
                [
                    "તમારી સાથે વાત કરીને ઘણો આનંદ થયો. તમારો દિવસ શુભ રહે! (It was great speaking with you. Have a wonderful day!)",
                    "બાય, મારી સાથે ફરી વાત ન કરશો.",
                    "હું હવે જાઉં છું, હંમેશ માટે અલવિદા.",
                    "બહાર નીકળો."
                ],
                0,
                "'Have a wonderful day!' leaves a positive, lasting impression on the listener.",
                "'Have a wonderful day!' सुनने वाले पर एक सकारात्मक और स्थायी प्रभाव छोड़ता है।",
                "'Have a wonderful day!' સાંભળનાર પર સકારાત્મક અને કાયમી છાપ છોડે છે."
            ),
            (
                f"How should an adult learner handle English pronunciation for '{clean_title}'?",
                f"एक वयस्क शिक्षार्थी को '{clean_title}' के लिए अंग्रेज़ी उच्चारण को कैसे संभालना चाहिए?",
                f"એક પુખ્ત શીખનાર વ્યક્તિએ '{clean_title}' માટે અંગ્રેજી ઉચ્ચારણને કેવી રીતે સંભાળવું જોઈએ?",
                [
                    "Listen to clear audio, read the Hindi Devanagari guide, and repeat aloud.",
                    "Ignore pronunciation completely.",
                    "Only read with your eyes closed.",
                    "Speak with an unnatural fake foreign accent."
                ],
                [
                    "स्पष्ट ऑडियो सुनें, हिंदी देवनागरी उच्चारण गाइड पढ़ें और ज़ोर से बोलें।",
                    "उच्चारण को पूरी तरह अनदेखा करें।",
                    "केवल आंखें बंद करके पढ़ें।",
                    "अप्राकृतिक नकली विदेशी लहजे में बोलें।"
                ],
                [
                    "સ્પષ્ટ ઑડિઓ સાંભળો, હિન્દી દેવનાગરી ઉચ્ચારણ ગાઇડ વાંચો અને મોટેથી બોલો.",
                    "ઉચ્ચારણને સંપૂર્ણપણે અવગણો.",
                    "માત્ર આંખો બંધ કરીને વાંચો.",
                    "અકુદરતી બનાવટી વિદેશી લહેકામાં બોલો."
                ],
                0,
                "Using the Devanagari reading guide while listening to Indian English audio creates immediate clarity.",
                "भारतीय अंग्रेज़ी ऑडियो सुनते समय देवनागरी पठन गाइड का उपयोग करने से तुरंत स्पष्टता आती है।",
                "ભારતીય અંગ્રેજી ઑડિઓ સાંભળતી વખતે દેવનાગરી વાંચન ગાઇડનો ઉપયોગ કરવાથી તરત જ સ્પષ્ટતા આવે છે."
            )
        ]
    elif level == 2:
        # Intermediate Everyday Fluency Situations
        scenarios = [
            (
                f"In a phone conversation regarding '{clean_title}', how do you professionally ask who is calling?",
                f"'{clean_title}' के संबंध में फोन पर पेशेवर तरीके से कैसे पूछें कि कौन बोल रहा है?",
                f"'{clean_title}' ના સંબંધમાં ફોન પર વ્યાવસાયિક રીતે કેવી રીતે પૂછશો કે કોણ બોલે છે?",
                [
                    "Who are you? Tell me.",
                    "May I know who is calling, please?",
                    "Why did you call my number?",
                    "What do you want?"
                ],
                [
                    "तुम कौन हो? मुझे बताओ।",
                    "क्या मैं जान सकता हूँ कि कौन बोल रहा है, कृपया? (May I know who is calling, please?)",
                    "तुमने मेरे नंबर पर क्यों कॉल किया?",
                    "तुम्हें क्या चाहिए?"
                ],
                [
                    "તમે કોણ છો? મને કહો.",
                    "શું હું જાણી શકું કે કોણ બોલી રહ્યું છે, પ્લીઝ? (May I know who is calling, please?)",
                    "તમે મારા નંબર પર કેમ કૉલ કર્યો?",
                    "તમારે શું જોઈએ છે?"
                ],
                1,
                "'May I know who is calling, please?' is the gold standard of professional telephone etiquette.",
                "'May I know who is calling, please?' पेशेवर टेलीफोन शिष्टाचार का स्वर्णिમ मानक है।",
                "'May I know who is calling, please?' વ્યાવસાયિક ટેલિફોન શિષ્ટાચારનું સુવર્ણ માનક છે."
            ),
            (
                f"When putting someone on hold during a call about '{clean_title}', what should you say?",
                f"'{clean_title}' के बारे में कॉल के दौरान किसी को होल्ड पर रखते समय क्या कहना चाहिए?",
                f"'{clean_title}' વિશે કૉલ દરમિયાન કોઈને હોલ્ડ પર રાખતી વખતે શું કહેવું જોઈએ?",
                [
                    "Wait there, don't talk.",
                    "Could you please hold the line for a moment while I check?",
                    "I am cutting the call now.",
                    "Go away for five minutes."
                ],
                [
                    "वहाँ रुको, बोलो मत।",
                    "क्या आप कृपया एक पल के लिए होल्ड करेंगे जब तक मैं चेक करूँ? (Could you please hold the line for a moment?)",
                    "मैं अब कॉल काट रहा हूँ।",
                    "पाँच मिनट के लिए चले जाओ।"
                ],
                [
                    "ત્યાં ઊભા રહો, બોલશો નહીં.",
                    "શું તમે કૃપા કરીને હું તપાસ કરું ત્યાં સુધી લાઇન હોલ્ડ કરશો? (Could you please hold the line for a moment?)",
                    "હું હવે કૉલ કાપી રહ્યો છું.",
                    "પાંચ મિનિટ માટે ચાલ્યા જાવ."
                ],
                1,
                "'Could you please hold the line for a moment?' shows respect for the caller's time.",
                "'Could you please hold the line for a moment?' कॉलर के समय के प्रति सम्मान प्रदर्शित करता है।",
                "'Could you please hold the line for a moment?' કૉલરના સમય પ્રત્યે આદર દર્શાવે છે."
            ),
            (
                f"When shopping for '{clean_title}', how do you politely ask about a discount?",
                f"'{clean_title}' की खरीदारी करते समय छूट के बारे में विनम्रता से कैसे पूछें?",
                f"'{clean_title}' ની ખરીદી કરતી વખતે ડિસ્કાઉન્ટ વિશે નમ્રતાથી કેવી રીતે પૂછશો?",
                [
                    "Give me discount or I will leave.",
                    "Is there any discount available on this item?",
                    "Your price is too greedy.",
                    "Make it free for me."
                ],
                [
                    "मुझे छूट दो वरना मैं जा रहा हूँ।",
                    "क्या इस वस्तु पर कोई छूट उपलब्ध है? (Is there any discount available on this item?)",
                    "आपकी कीमत बहुत लालची है।",
                    "इसे मेरे लिए मुफ़्त कर दो।"
                ],
                [
                    "મને ડિસ્કાઉન્ટ આપો નહીં તો હું જાઉં છું.",
                    "શું આ વસ્તુ પર કોઈ ડિસ્કાઉન્ટ ઉપલબ્ધ છે? (Is there any discount available on this item?)",
                    "તમારો ભાવ બહુ લાલચુ છે.",
                    "આ મને મફતમાં આપી દો."
                ],
                1,
                "'Is there any discount available on this item?' is polite, natural, and standard in retail shops.",
                "'Is there any discount available on this item?' खुदरा दुकानों में विनम्र और मानक वाक्य है।",
                "'Is there any discount available on this item?' રિટેલ દુકાનોમાં નમ્ર અને પ્રમાણભૂત વાક્ય છે."
            ),
            (
                f"At a restaurant, how do you politely request the bill related to '{clean_title}'?",
                f"रेस्तरां में बिल मांगते समय कौन सा वाक्य सबसे उपयुक्त है?",
                f"રેસ્ટોરન્ટમાં બિલ માંગતી વખતે કયું વાક્ય સૌથી યોગ્ય છે?",
                [
                    "Bring bill now fast!",
                    "Excuse me, could we have the bill, please?",
                    "How much do I have to pay, tell me!",
                    "I am walking out."
                ],
                [
                    "जल्दी बिल लाओ!",
                    "एक्सक्यूज़ मी, क्या हमें बिल मिल सकता है, कृपया? (Excuse me, could we have the bill, please?)",
                    "मुझे कितना देना है, बताओ!",
                    "मैं बाहर जा रहा हूँ।"
                ],
                [
                    "ઝડપથી બિલ લાવો!",
                    "એક્સક્યુઝ મી, શું અમને બિલ મળી શકશે, પ્લીઝ? (Excuse me, could we have the bill, please?)",
                    "મારે કેટલા ચૂકવવાના છે, કહો!",
                    "હું બહાર નીકળી રહ્યો છું."
                ],
                1,
                "'Could we have the bill, please?' is courteous and universally recognized in dining etiquette.",
                "'Could we have the bill, please?' भोजन शिष्टाचार में सबसे विनम्र और स्वीकृत वाक्य है।",
                "'Could we have the bill, please?' ડાઇનિંગ શિષ્ટાચારમાં સૌથી નમ્ર અને સ્વીકૃત વાક્ય છે."
            ),
            (
                f"When asking for road directions regarding '{clean_title}', which phrase is correct?",
                f"सड़क का रास्ता पूछते समय कौन सा वाक्यांश सही और विनम्र है?",
                f"રસ્તો પૂછતી વખતે કયો વાક્યાંશ સાચો અને નમ્ર છે?",
                [
                    "Where is the road? Show me.",
                    "Excuse me, could you direct me to the nearest station?",
                    "Take me there right now.",
                    "You must know this place."
                ],
                [
                    "सड़क कहाँ है? मुझे दिखाओ।",
                    "क्षमा करें, क्या आप मुझे निकटतम स्टेशन का रास्ता बता सकते हैं? (Excuse me, could you direct me...)",
                    "मुझे अभी वहाँ ले चलो।",
                    "तुम्हें यह जगह ज़रूर पता होगी।"
                ],
                [
                    "રસ્તો ક્યાં છે? મને બતાવો.",
                    "માફ કરશો, શું તમે મને નજીકના સ્ટેશનનો રસ્તો બતાવી શકશો? (Excuse me, could you direct me...)",
                    "મને હમણાં જ ત્યાં લઈ જાવ.",
                    "તમને આ જગ્યાની ખબર જ હોવી જોઈએ."
                ],
                1,
                "'Excuse me, could you direct me to...' begins with polite attention and asks clearly.",
                "'Excuse me, could you direct me to...' विनम्रता से ध्यान आकर्षित करता है और स्पष्टता से पूछता है।",
                "'Excuse me, could you direct me to...' નમ્રતાથી ધ્યાન ખેંચે છે અને સ્પષ્ટતાથી પૂછે છે."
            ),
            (
                f"In an office meeting regarding '{clean_title}', how do you politely disagree with a colleague?",
                f"कार्यालय की बैठक में किसी सहकर्मी से विनम्रतापूर्वक असहमति कैसे व्यक्त करें?",
                f"ઑફિસ મીટિંગમાં સહકર્મી સાથે નમ્રતાપૂર્વક અસંમતિ કેવી રીતે વ્યક્ત કરશો?",
                [
                    "You are completely wrong!",
                    "I see your point, but may I suggest an alternative approach?",
                    "That is a foolish idea.",
                    "Be quiet and listen to me."
                ],
                [
                    "तुम बिल्कुल गलत हो!",
                    "मैं आपकी बात समझता हूँ, लेकिन क्या मैं एक वैकल्पिक तरीका सुझा सकता हूँ? (I see your point, but...)",
                    "यह एक बेवकूफी भरा विचार है।",
                    "चुप रहो और मेरी बात सुनो।"
                ],
                [
                    "તમે તદ્દન ખોટા છો!",
                    "હું તમારો મુદ્દો સમજું છું, પરંતુ શું હું એક વૈકલ્પિક અભિગમ સૂચવી શકું? (I see your point, but...)",
                    "આ એક મૂર્ખામીભર્યો વિચાર છે.",
                    "શાંત રહો અને મારું સાંભળો."
                ],
                1,
                "'I see your point, but may I suggest...' validates the other person before offering another solution.",
                "'I see your point, but...' दूसरे व्यक्ति का सम्मान करते हुए रचनात्मक समाधान प्रस्तुत करता है।",
                "'I see your point, but...' અન્ય વ્યક્તિનો આદર કરીને રચનાત્મક ઉકેલ રજૂ કરે છે."
            ),
            (
                f"Which common Indian English error should be avoided in '{clean_title}'?",
                f"'{clean_title}' में किस आम भारतीय अंग्रेज़ी गलती से बचना चाहिए?",
                f"'{clean_title}' માં કઈ સામાન્ય ભારતીય અંગ્રેજી ભૂલથી બચવું જોઈએ?",
                [
                    "Saying 'We will discuss about the project' instead of 'We will discuss the project'.",
                    "Saying 'Good morning Sir'.",
                    "Saying 'Thank you for your time'.",
                    "Saying 'I will call you tomorrow'."
                ],
                [
                    "'We will discuss the project' के स्थान पर 'We will discuss about the project' कहना। (गलत)",
                    "'Good morning Sir' कहना।",
                    "'Thank you for your time' कहना।",
                    "'I will call you tomorrow' कहना।"
                ],
                [
                    "'We will discuss the project' ની જગ્યાએ 'We will discuss about the project' કહેવું. (ખોટું)",
                    "'Good morning Sir' કહેવું.",
                    "'Thank you for your time' કહેવું.",
                    "'I will call you tomorrow' કહેવું."
                ],
                0,
                "'Discuss' already contains the meaning of 'talk about'. Never add 'about' after 'discuss'.",
                "'Discuss' का अर्थ ही 'के बारे में बात करना' होता है। 'Discuss' के बाद कभी 'about' न लगाएं।",
                "'Discuss' નો અર્થ જ 'વિશે વાત કરવી' થાય છે. 'Discuss' પછી ક્યારેય 'about' ન લગાવશો."
            ),
            (
                f"How do you express an appointment cancellation politely in '{clean_title}'?",
                f"'{clean_title}' में अपॉइंटमेंट रद्द करने के लिए कौन सा वाक्य सबसे पेशेवर है?",
                f"'{clean_title}' માં એપોઇન્ટમેન્ટ રદ કરવા માટે કયું વાક્ય સૌથી વ્યાવસાયિક છે?",
                [
                    "I am not coming today, bye.",
                    "I apologize, but due to an urgent matter, I need to reschedule our meeting.",
                    "Forget our meeting, I am busy.",
                    "Why should I come?"
                ],
                [
                    "मैं आज नहीं आ रहा हूँ, बाय।",
                    "मैं क्षमा चाहता हूँ, लेकिन एक ज़रूरी काम के कारण मुझे हमारी बैठक का समय बदलना होगा। (I apologize, but...)",
                    "हमारी बैठक भूल जाओ, मैं व्यस्त हूँ।",
                    "मैं क्यों आऊँ?"
                ],
                [
                    "હું આજે નથી આવતો, બાય.",
                    "હું માફી ચાહું છું, પરંતુ એક તાકીદના કામને કારણે મારે આપણી મીટિંગ ફરીથી શેડ્યૂલ કરવી પડશે.",
                    "આપણી મીટિંગ ભૂલી જાવ, હું વ્યસ્ત છું.",
                    "હું કેમ આવું?"
                ],
                1,
                "'I apologize, but due to an urgent matter, I need to reschedule...' is courteous and professional.",
                "यह वाक्य कार्यस्थल पर उच्च व्यावसायिक विश्वसनीयता और शिष्टाचार बनाए रखता है।",
                "આ વાક્ય કાર્યસ્થળ પર ઉચ્ચ વ્યાવસાયિક વિશ્વસનીયતા અને શિષ્ટાચાર જાળવી રાખે છે."
            ),
            (
                f"When someone presents an idea about '{clean_title}', how do you agree constructively?",
                f"जब कोई '{clean_title}' पर विचार प्रस्तुत करे, तो रचनात्मक रूप से कैसे सहमति दें?",
                f"જ્યારે કોઈ '{clean_title}' પર વિચાર રજૂ કરે, ત્યારે રચનાત્મક રીતે કેવી રીતે સંમત થશો?",
                [
                    "Yes, I completely agree with your proposal. It will save our team valuable time.",
                    "Whatever you say, I don't care.",
                    "You are lucky I agree.",
                    "Fine, do what you want."
                ],
                [
                    "हाँ, मैं आपके प्रस्ताव से पूरी तरह सहमत हूँ। इससे हमारी टीम का कीमती समय बचेगा।",
                    "आप जो भी कहें, मुझे परवाह नहीं है।",
                    "आप भाग्यशाली हैं कि मैं सहमत हूँ।",
                    "ठीक है, जो करना है करो।"
                ],
                [
                    "હા, હું તમારા પ્રસ્તાવ સાથે સંપૂર્ણપણે સંમત છું. આનાથી આપણી ટીમનો કિંમતી સમય બચશે.",
                    "તમે જે કહો તે, મને કોઈ પડી નથી.",
                    "તમે નસીબદાર છો કે હું સંમત છું.",
                    "ઠીક છે, તમારે જે કરવું હોય તે કરો."
                ],
                0,
                "Agreeing and adding a specific benefit reinforces teamwork and professional collaboration.",
                "सहमति देने के साथ विशिष्ट लाभ जोड़ना टीम वर्क और पेशेवर सहयोग को मज़बूत करता है।",
                "સંમતિ આપવાની સાથે ચોક્કસ ફાયદો ઉમેરવો ટીમ વર્ક અને વ્યાવસાયિક સહયોગને મજબૂત બનાવે છે."
            ),
            (
                f"When writing a quick message to a client regarding '{clean_title}', which closing is standard?",
                f"'{clean_title}' के बारे में ग्राहक को संदेश लिखते समय कौन सा समापन सबसे मानक है?",
                f"'{clean_title}' વિશે ગ્રાહકને સંદેશ લખતી વખતે કયું સમાપન સૌથી પ્રમાણભૂત છે?",
                [
                    "Warm regards, Govind Patel",
                    "Bye bye see ya",
                    "Yours forever and ever",
                    "End of message"
                ],
                [
                    "वार्म रिगार्ड्स, गोविंद पटेल (Warm regards, Govind Patel)",
                    "बाय बाय सी या",
                    "योर्स फॉरएवर एंड एवर",
                    "संदेश समाप्त"
                ],
                [
                    "વૉર્મ રિગાર્ડ્સ, ગોવિંદ પટેલ (Warm regards, Govind Patel)",
                    "બાય બાય સી યા",
                    "યોર્સ ફોરેવર એન્ડ એવર",
                    "સંદેશ સમાપ્ત"
                ],
                0,
                "'Warm regards' or 'Best regards' is the gold standard for professional emails and messages.",
                "'Warm regards' या 'Best regards' पेशेवर ईमेल और संदेशों के लिए स्वर्णिम मानक है।",
                "'Warm regards' અથવા 'Best regards' વ્યાવસાયિક ઈમેલ અને મેસેજ માટે ગોલ્ડ સ્ટાન્ડર્ડ છે."
            )
        ]
    else:
        # Level 3: Professional & Career Mastery Situations
        scenarios = [
            (
                f"In a job interview regarding '{clean_title}', how should you begin answering 'Tell me about yourself'?",
                f"नौकरी के साक्षात्कार में 'Tell me about yourself' का उत्तर देना कैसे शुरू करना चाहिए?",
                f"નોકરીના ઇન્ટરવ્યુમાં 'Tell me about yourself' નો જવાબ આપવાનું કેવી રીતે શરૂ કરવું જોઈએ?",
                [
                    "I was born in a small village and I have many personal problems.",
                    "Thank you for this opportunity. I am a dedicated professional with experience in sales and communication.",
                    "Look at my resume, why are you asking?",
                    "I don't know what to say."
                ],
                [
                    "मैं एक छोटे से गाँव में पैदा हुआ था और मेरी कई व्यक्तिगत समस्याएँ हैं।",
                    "इस अवसर के लिए धन्यवाद। मैं बिक्री और संचार के अनुभव के साथ एक समर्पित पेशेवर हूँ। (Thank you for this opportunity...)",
                    "मेरा बायोडाटा देखें, आप क्यों पूछ रहे हैं?",
                    "मुझे नहीं पता क्या कहूँ।"
                ],
                [
                    "હું એક નાના ગામમાં જન્મ્યો હતો અને મારી ઘણી અંગત સમસ્યાઓ છે.",
                    "આ તક માટે આભાર. હું સેલ્સ અને કમ્યુનિકેશનના અનુભવ સાથે સમર્પિત પ્રોફેશનલ છું. (Thank you for this opportunity...)",
                    "મારો બાયોડેટા જુઓ, તમે કેમ પૂછો છો?",
                    "મને ખબર નથી કે શું કહેવું."
                ],
                1,
                "Opening with gratitude and summarizing your core professional strengths sets a winning first impression.",
                "आभार व्यक्त करने और अपनी मुख्य व्यावसायिक ताकतों का सारांश देने से एक बेहतरीन पहला प्रभाव पड़ता है।",
                "આભાર વ્યક્ત કરવાથી અને તમારી મુખ્ય વ્યાવસાયિક શક્તિઓનો સારાંશ આપવાથી ઉત્તમ પ્રથમ છાપ પડે છે."
            ),
            (
                f"When delivering a business presentation on '{clean_title}', how do you transition between slides smoothly?",
                f"'{clean_title}' पर व्यावसायिक प्रस्तुति देते समय स्लाइड्स के बीच सुचारू रूप से कैसे बदलाव करें?",
                f"'{clean_title}' પર બિઝનેસ પ્રેઝન્ટેશન આપતી વખતે સ્લાઇડ્સ વચ્ચે સરળતાથી કેવી રીતે સંક્રમણ કરશો?",
                [
                    "Next slide please, I forgot what this is.",
                    "Now that we have covered our goals, let us move on to our execution strategy.",
                    "Look at the screen yourself.",
                    "Slide change now."
                ],
                [
                    "अगली स्लाइड लाएं, मैं भूल गया यह क्या है।",
                    "अब जब हमने अपने लक्ष्यों को देख लिया है, तो आइए हम अपनी निष्पादन रणनीति पर आगे बढ़ें। (Now that we have covered...)",
                    "स्क्रीन को खुद ही देख लें।",
                    "स्लाइड बदलो अब।"
                ],
                [
                    "આગલી સ્લાઇડ લાવો, હું ભૂલી ગયો આ શું છે.",
                    "હવે જ્યારે આપણે આપણા લક્ષ્યોને આવરી લીધા છે, તો ચાલો આપણે આપણી અમલીકરણ વ્યૂહરચના તરફ આગળ વધીએ.",
                    "સ્ક્રીનને જાતે જ જોઈ લો.",
                    "સ્લાઇડ બદલો હવે."
                ],
                1,
                "Summarizing the current point before introducing the next topic keeps your audience fully engaged.",
                "अगले विषय को पेश करने से पहले वर्तमान बिंदु का सारांश देने से दर्शक पूरी तरह जुड़े रहते हैं।",
                "આગામી વિષય રજૂ કરતા પહેલા વર્તમાન મુદ્દાનો સારાંશ આપવાથી શ્રોતાઓ સંપૂર્ણપણે જોડાયેલા રહે છે."
            ),
            (
                f"In a group discussion (GD) on '{clean_title}', how do you enter the discussion politely when everyone is speaking?",
                f"सामूहिक चर्चा (GD) में जब सब बोल रहे हों, तो विनम्रता से अपनी बात कैसे शुरू करें?",
                f"ગ્રૂપ ડિસ્કશન (GD) માં જ્યારે બધા બોલતા હોય, ત્યારે નમ્રતાથી તમારી વાત કેવી રીતે શરૂ કરશો?",
                [
                    "Stop shouting! Listen to me!",
                    "I would like to add a valuable perspective here...",
                    "You all know nothing.",
                    "Stay silent through the whole discussion."
                ],
                [
                    "चिल्लाना बंद करो! मेरी बात सुनो!",
                    "मैं यहाँ एक मूल्यवान दृष्टिकोण जोड़ना चाहूँगा... (I would like to add a valuable perspective here...)",
                    "आप सबको कुछ नहीं पता।",
                    "पूरी चर्चा के दौरान शांत रहें।"
                ],
                [
                    "બૂમો પાડવાનું બંધ કરો! મારું સાંભળો!",
                    "હું અહીં એક મૂલ્યવાન દ્રષ્ટિકોણ ઉમેરવા માંગુ છું... (I would like to add a valuable perspective here...)",
                    "તમને બધાને કંઈ ખબર નથી.",
                    "આખી ચર્ચા દરમિયાન શાંત રહો."
                ],
                1,
                "'I would like to add a valuable perspective here...' is firm, polite, and captures the panel's attention.",
                "यह वाक्यांश दृढ़ और विनम्र है, जो चयनकर्ताओं का ध्यान तुरंत आकर्षित करता है।",
                "આ વાક્યાંશ મક્કમ અને નમ્ર છે, જે પેનલનું ધ્યાન તરત જ આકર્ષિત કરે છે."
            ),
            (
                f"When handling an unhappy client regarding '{clean_title}', what is the best opening statement?",
                f"'{clean_title}' के बारे में किसी असंतुष्ट ग्राहक को संभालते समय सबसे अच्छा शुरुआती वाक्य क्या है?",
                f"'{clean_title}' વિશે અસંતુષ્ટ ગ્રાહકને સંભાળતી વખતે શ્રેષ્ઠ પ્રારંભિક વાક્ય કયું છે?",
                [
                    "It is not our fault, you made the mistake.",
                    "I completely understand your concern, and I am personally here to resolve this for you.",
                    "Why are you getting angry at me?",
                    "Please call someone else."
                ],
                [
                    "यह हमारी गलती नहीं है, गलती आपकी है।",
                    "मैं आपकी चिंता को पूरी तरह समझता हूँ, और मैं व्यक्तिगत रूप से इसे आपके लिए हल करने के लिए यहाँ हूँ। (I understand your concern...)",
                    "आप मुझ पर गुस्सा क्यों हो रहे हैं?",
                    "कृपया किसी और को कॉल करें।"
                ],
                [
                    "આ અમારી ભૂલ નથી, ભૂલ તમારી છે.",
                    "હું તમારી ચિંતા સંપૂર્ણપણે સમજુ છું, અને હું વ્યક્તિગત રીતે તમારા માટે આનું નિરાકરણ લાવવા અહીં છું.",
                    "તમે મારા પર ગુસ્સો કેમ કરો છો?",
                    "કૃપા કરીને બીજા કોઈને કૉલ કરો."
                ],
                1,
                "Demonstrating empathy ('I understand your concern') and taking personal ownership de-escalates conflict immediately.",
                "सहानुभूति दिखाना और व्यक्तिगत ज़िम्मेदारी लेना असंतोष को तुरंत शांत करता है।",
                "સહાનુભૂતિ દર્શાવવી અને વ્યક્તિગત જવાબદારી લેવી અસંતોષને તરત જ શાંત કરે છે."
            ),
            (
                f"How do you articulate long-term career goals related to '{clean_title}'?",
                f"'{clean_title}' से संबंधित दीर्घकालिक करियर लक्ष्यों को स्पष्ट रूप से कैसे व्यक्त करें?",
                f"'{clean_title}' સંબંધિત લાંબા ગાળાના કારકિર્દીના લક્ષ્યોને સ્પષ્ટ રીતે કેવી રીતે વ્યક્ત કરશો?",
                [
                    "I just want to earn money somehow.",
                    "In the next five years, I aim to lead a high-performing team and deliver measurable business value.",
                    "I don't think about the future.",
                    "Whatever happens will happen."
                ],
                [
                    "मैं बस किसी तरह पैसे कमाना चाहता हूँ।",
                    "अगले पाँच वर्षों में, मेरा लक्ष्य एक उच्च-प्रदर्शन टीम का नेतृत्व करना और मापने योग्य व्यावसायिक मूल्य प्रदान करना है।",
                    "मैं भविष्य के बारे में नहीं सोचता।",
                    "जो होगा देखा जाएगा।"
                ],
                [
                    "હું બસ ગમે તે રીતે પૈસા કમાવવા માંગુ છું.",
                    "આગામી પાંચ વર્ષમાં, મારો ધ્યેય એક ઉચ્ચ-પ્રદર્શન ટીમનું નેતૃત્વ કરવાનો અને વ્યવસાયિક મૂલ્ય પ્રદાન કરવાનો છે.",
                    "હું ભવિષ્ય વિશે વિચારતો નથી.",
                    "જે થશે તે જોયું જશે."
                ],
                1,
                "Defining measurable impact and leadership ambition demonstrates high strategic capability.",
                "मापने योग्य प्रभाव और नेतृत्व की महत्वाकांक्षा को परिभाषित करना उच्च रणनीतिक क्षमता प्रदर्शित करता है।",
                "માપી શકાય તેવી અસર અને નેતૃત્વની મહત્વાકાંક્ષાને વ્યાખ્યાયિત કરવી ઉચ્ચ વ્યૂહાત્મક ક્ષમતા દર્શાવે છે."
            ),
            (
                f"How do you avoid mental translation from your mother tongue into English during '{clean_title}'?",
                f"'{clean_title}' के दौरान अपनी मातृभाषा से अंग्रेज़ी में मानसिक अनुवाद से कैसे बचें?",
                f"'{clean_title}' દરમિયાન તમારી માતૃભાષામાંથી અંગ્રેજીમાં માનસિક ભાષાંતર કરવાનું કેવી રીતે ટાળશો?",
                [
                    "Think directly in English sentence structures and everyday conversational chunks.",
                    "Translate every single word in your head first before speaking.",
                    "Write down every sentence on paper before opening your mouth.",
                    "Never speak English spontaneously."
                ],
                [
                    "सीधे अंग्रेज़ी वाक्य संरचनाओं और दैनिक बोलचाल के वाक्यांशों में सोचें। (Think directly in English...)",
                    "बोलने से पहले अपने दिमाग में हर एक शब्द का अनुवाद करें।",
                    "मुंह खोलने से पहले हर वाक्य को कागज़ पर लिखें।",
                    "कभी भी स्वाभाविक रूप से अंग्रेज़ी न बोलें।"
                ],
                [
                    "સીધા અંગ્રેજી વાક્ય રચનાઓ અને રોજિંદા બોલચાલના શબ્દસમૂહોમાં વિચારો. (Think directly in English...)",
                    "બોલતા પહેલાં તમારા મગજમાં દરેક શબ્દનું ભાષાંતર કરો.",
                    "મોં ખોલતા પહેલાં દરેક વાક્ય કાગળ પર લખો.",
                    "ક્યારેય સ્વયંભૂ અંગ્રેજી ન બોલશો."
                ],
                0,
                "Thinking in phrases and word chunks eliminates hesitation and creates effortless natural flow.",
                "वाक्यांशों में सोचने से हिचकिचाहट समाप्त होती है और सहज स्वाभाविक प्रवाह बनता है।",
                "શબ્દસમૂહોમાં વિચારવાથી ખચકાટ દૂર થાય છે અને સહજ કુદરતી પ્રવાહ બને છે."
            ),
            (
                f"When leading a project discussion on '{clean_title}', how do you summarize action items?",
                f"'{clean_title}' पर प्रोजेक्ट चर्चा का नेतृत्व करते समय कार्य बिंदुओं का सारांश कैसे दें?",
                f"'{clean_title}' પર પ્રોજેક્ટ ચર્ચાનું નેતૃત્વ કરતી વખતે કાર્ય મુદ્દાઓનો સારાંશ કેવી રીતે આપશો?",
                [
                    "We are done, everybody go.",
                    "To summarize, Amit will finalize the report by Friday, and I will share the client update tomorrow.",
                    "Do whatever you want, don't ask me.",
                    "I forgot what we decided."
                ],
                [
                    "हमारा काम हो गया, सब जाओ।",
                    "संक्षेप में, अमित शुक्रवार तक रिपोर्ट को अंतिम रूप देंगे, और मैं कल क्लाइंट अपडेट साझा करूँगा। (To summarize...)",
                    "जो करना है करो, मुझसे मत पूछो।",
                    "मैं भूल गया कि हमने क्या तय किया था।"
                ],
                [
                    "આપણું કામ પૂરું, બધા જાવ.",
                    "સારાંશમાં, અમિત શુક્રવાર સુધીમાં રિપોર્ટ ફાઇનલ કરશે, અને હું આવતીકાલે ક્લાયન્ટ અપડેટ શેર કરીશ. (To summarize...)",
                    "જે કરવું હોય તે કરો, મને ન પૂછશો.",
                    "હું ભૂલી ગયો કે આપણે શું નક્કી કર્યું હતું."
                ],
                1,
                "Assigning clear ownership and specific deadlines is essential for executive leadership.",
                "स्पष्ट स्वामित्व और विशिष्ट समय सीमा सौंपना कार्यकारी नेतृत्व के लिए आवश्यक है।",
                "સ્પષ્ટ માલિકી અને ચોક્કસ સમયમર્યાદા સોંપવી એ નેતૃત્વ માટે આવશ્યક છે."
            ),
            (
                f"In public speaking on '{clean_title}', what is the most effective way to engage your audience?",
                f"'{clean_title}' पर सार्वजनिक भाषण में दर्शकों को आकर्षित करने का सबसे प्रभावी तरीका क्या है?",
                f"'{clean_title}' પર જાહેર વક્તવ્યમાં શ્રોતાઓને આકર્ષિત કરવાનો સૌથી અસરકારક રસ્તો કયો છે?",
                [
                    "Start with a compelling real-life question or relatable story.",
                    "Read every word from a printed paper with your head down.",
                    "Speak in a dull, monotone voice without smiling.",
                    "Stare at the ceiling the entire time."
                ],
                [
                    "एक सम्मोहक वास्तविक जीवन के प्रश्न या संबंधित कहानी से शुरुआत करें। (Start with a compelling question...)",
                    "सिर नीचे करके छपे हुए कागज़ से एक-एक शब्द पढ़ें।",
                    "बिना मुस्कुराए नीरस, एकरस आवाज़ में बोलें।",
                    "पूरे समय छत की तरफ देखते रहें।"
                ],
                [
                    "એક આકર્ષક વાસ્તવિક જીવનના પ્રશ્ન અથવા સંબંધિત વાર્તાથી શરૂઆત કરો.",
                    "માથું નીચું રાખીને છાપેલા કાગળમાંથી એક-એક શબ્દ વાંચો.",
                    "હસ્યા વિના નીરસ, એકસમાન અવાજમાં બોલો.",
                    "આખો સમય છત તરફ જોતા રહો."
                ],
                0,
                "Starting with an intriguing question or real-life story connects immediately with audience emotions.",
                "एक विचारोत्तेजक प्रश्न या वास्तविक कहानी से शुरुआत करने से दर्शकों की भावनाओं से तुरंत जुड़ाव होता है।",
                "વિચારોત્તેજક પ્રશ્ન અથવા વાસ્તવિક વાર્તાથી શરૂઆત કરવાથી શ્રોતાઓની લાગણીઓ સાથે તરત જ જોડાણ થાય છે."
            ),
            (
                f"When receiving critical constructive feedback regarding '{clean_title}', how should you respond?",
                f"'{clean_title}' के संबंध में आलोचनात्मक रचनात्मक प्रतिक्रिया मिलने पर आपको क्या प्रतिक्रिया देनी चाहिए?",
                f"'{clean_title}' અંગે રચનાત્મક પ્રતિસાદ મળવા પર તમારે શું પ્રતિસાદ આપવો જોઈએ?",
                [
                    "Thank you for this valuable feedback. I will incorporate your suggestions and improve.",
                    "You are attacking me personally!",
                    "I refuse to listen to any criticism.",
                    "You don't know my work."
                ],
                [
                    "इस बहुमूल्य प्रतिक्रिया के लिए धन्यवाद। मैं आपके सुझावों को शामिल करूँगा और सुधार करूँगा। (Thank you for this feedback...)",
                    "आप मुझ पर व्यक्तिगत हमला कर रहे हैं!",
                    "मैं किसी भी आलोचना को सुनने से इनकार करता हूँ।",
                    "आप मेरा काम नहीं जानते।"
                ],
                [
                    "આ મૂલ્યવાન પ્રતિસાદ માટે આભાર. હું તમારા સૂચનોનો સમાવેશ કરીશ અને સુધારો કરીશ.",
                    "તમે મારા પર અંગત હુમલો કરી રહ્યા છો!",
                    "હું કોઈપણ ટીકા સાંભળવાનો ઇનકાર કરું છું.",
                    "તમે મારું કામ જાણતા નથી."
                ],
                0,
                "Accepting feedback with gratitude demonstrates professional maturity and high leadership potential.",
                "कृतज्ञता के साथ प्रतिक्रिया स्वीकार करना व्यावसायिक परिपक्वता और नेतृत्व क्षमता को दर्शाता है।",
                "આભાર સાથે પ્રતિસાદ સ્વીકારવો એ વ્યાવસાયિક પરિપક્વતા અને નેતૃત્વ ક્ષમતા દર્શાવે છે."
            ),
            (
                f"What is the ultimate mindset for lifelong mastery of '{clean_title}'?",
                f"'{clean_title}' में आजीवन महारत हासिल करने के लिए अंतिम मानसिकता क्या है?",
                f"'{clean_title}' માં આજીવન નિપુણતા મેળવવા માટે અંતિમ માનસિકતા કઈ છે?",
                [
                    "Embrace every daily conversation as an opportunity to learn, listen actively, and speak with joy.",
                    "Believe that you know everything and stop practicing.",
                    "Fear making mistakes and avoid speaking in public.",
                    "Quit as soon as you encounter a difficult word."
                ],
                [
                    "हर दैनिक बातचीत को सीखने, सक्रिय रूप से सुनने और आनंद के साथ बोलने के अवसर के रूप में अपनाएं।",
                    "विश्वास करें कि आप सब कुछ जानते हैं और अभ्यास करना बंद कर दें।",
                    "गलतियां करने से डरें और सार्वजनिक रूप से बोलने से बचें।",
                    "कठिन शब्द आते ही छोड़ दें।"
                ],
                [
                    "દરેક દૈનિક વાતચીતને શીખવાની, સક્રિયપણે સાંભળવાની અને આનંદ સાથે બોલવાની તક તરીકે સ્વીકારો.",
                    "માનો કે તમે બધું જ જાણો છો અને પ્રેક્ટિસ કરવાનું બંધ કરો.",
                    "ભૂલો કરવાથી ડરો અને જાહેરમાં બોલવાનું ટાળો.",
                    "અઘરો શબ્દ આવતા જ છોડી દો."
                ],
                0,
                "Viewing every interaction as an opportunity to learn turns English from a challenge into a lifelong joy.",
                "हर बातचीत को सीखने के अवसर के रूप में देखने से अंग्रेज़ी एक चुनौती से आजीवन आनंद में बदल जाती है।",
                "દરેક વાતચીતને શીખવાની તક તરીકે જોવાથી અંગ્રેજી એક પડકારમાંથી આજીવન આનંદમાં ફેરવાય છે."
            )
        ]

    for idx, (q, q_hi, q_gu, opts, opts_hi, opts_gu, cor, exp, exp_hi, exp_gu) in enumerate(scenarios):
        q_id = f"govindsir_english_ch{ch_num}_q{idx+1}"
        phonetic = to_devanagari(q)
        questions.append({
            "id": q_id,
            "type": "quiz",
            "question": q,
            "question_hi": q_hi,
            "question_gu": q_gu,
            "phonetic_hi": phonetic,
            "options": opts,
            "options_hi": opts_hi,
            "options_gu": opts_gu,
            "correct_index": cor,
            "explanation": exp,
            "explanation_hi": exp_hi,
            "explanation_gu": exp_gu
        })
        
    return questions

def process_all():
    print("Step 1: Updating Curriculum Metadata with 3 Levels...")
    with open(CURRICULUM_FILE, 'r', encoding='utf-8') as f:
        curriculum = json.load(f)
        
    subjects = curriculum.get('subjects', [])
    for subj in subjects:
        if subj.get('id') == 'spoken_english':
            for idx, ch in enumerate(subj.get('chapters', [])):
                ch_num = idx + 1
                lvl, lvl_name, lvl_hi, lvl_gu = get_level(ch_num)
                ch['level'] = lvl
                ch['level_name'] = lvl_name
                ch['level_name_hi'] = lvl_hi
                ch['level_name_gu'] = lvl_gu

    with open(CURRICULUM_FILE, 'w', encoding='utf-8') as f:
        json.dump(curriculum, f, indent=2, ensure_ascii=False)
    print("Curriculum updated.")

    print("\nStep 2: Processing all 63 Chapters...")
    total_quizzes_added = 0
    total_theories_condensed = 0

    for ch_num in range(1, 64):
        ch_file = os.path.join(CHAPTERS_DIR, f"govindsir_english_ch{ch_num}.json")
        if not os.path.exists(ch_file):
            print(f"Warning: {ch_file} not found!")
            continue

        with open(ch_file, 'r', encoding='utf-8') as f:
            data = json.load(f)

        lvl, lvl_name, lvl_hi, lvl_gu = get_level(ch_num)
        title = data.get('title', f"Chapter No {ch_num}")

        # Update metadata
        meta = data.get('metadata', {})
        meta['level'] = lvl
        meta['level_name'] = lvl_name
        meta['level_name_hi'] = lvl_hi
        meta['level_name_gu'] = lvl_gu
        data['metadata'] = meta
        data['level'] = lvl

        blocks = data.get('blocks', [])
        new_blocks = []
        existing_quizzes = []

        # Process existing blocks
        for block in blocks:
            b_type = block.get('type')

            # Normalize MCQ to Quiz
            if b_type == 'mcq':
                block['type'] = 'quiz'
                b_type = 'quiz'
                # Ensure correct_index is integer
                if 'correct_index' not in block:
                    block['correct_index'] = 0
                else:
                    try:
                        block['correct_index'] = int(block['correct_index'])
                    except:
                        block['correct_index'] = 0

            if b_type == 'quiz':
                # Ensure trilingual fields and phonetics
                q_text = block.get('question', '')
                if not block.get('phonetic_hi'):
                    block['phonetic_hi'] = to_devanagari(q_text)
                if not block.get('question_hi'):
                    block['question_hi'] = q_text
                if not block.get('question_gu'):
                    block['question_gu'] = q_text
                if 'correct_index' not in block:
                    block['correct_index'] = 0
                else:
                    try:
                        block['correct_index'] = int(block['correct_index'])
                    except:
                        block['correct_index'] = 0
                existing_quizzes.append(block)
                # Don't add to new_blocks yet; we will place all quizzes neatly in practice section
                continue

            # Condense long theory text & add phonetics
            if b_type == 'theory':
                body = block.get('body', '')
                if len(body) > 220:
                    condensed = condense_theory_text(body)
                    block['body'] = condensed
                    total_theories_condensed += 1

                # Generate accurate Devanagari phonetics
                block['phonetic_hi'] = to_devanagari(block['body'])

            new_blocks.append(block)

        # Generate situational questions for this chapter
        generated_questions = build_situational_questions(ch_num, title, lvl)

        # Combine: keep up to 2 high-quality existing quizzes, then append generated questions so total is 10-12
        final_quizzes = existing_quizzes[:2] + generated_questions
        # Cap at 10-12
        final_quizzes = final_quizzes[:12]

        # Append quizzes at the end of the chapter
        new_blocks.extend(final_quizzes)
        total_quizzes_added += len(final_quizzes)

        data['blocks'] = new_blocks

        with open(ch_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

        print(f"Ch {ch_num:2d} ({lvl_name.split(':')[0]}): {len(final_quizzes)} quizzes, {len(new_blocks)} total blocks.")

    print(f"\nAll done! Total quizzes added/standardized: {total_quizzes_added}. Long theories condensed: {total_theories_condensed}.")

if __name__ == '__main__':
    process_all()
