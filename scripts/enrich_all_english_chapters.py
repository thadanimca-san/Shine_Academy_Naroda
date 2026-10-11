#!/usr/bin/env python3
import json
import os
import re

CURRICULUM_PATH = 'app_core/curriculum/govindsir_english.json'
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
    'bus': 'बस', 'train': 'ट्रेन', 'ticket': 'टिकટ', 'help': 'हेल्प', 'sir': 'सर',
    'madam': 'मैडम', 'call': 'कॉल', 'phone': 'फ़ोन', 'meeting': 'मीटिंग', 'interview': 'इंटरव्यू',
    'question': 'क्वेश्चन', 'answer': 'आंसर', 'right': 'राइट', 'wrong': 'रॉन्ग', 'confidence': 'कॉन्फिडेंस',
    'confident': 'कॉन्फिडेंट', 'fluent': 'फ्लूएंट', 'fluency': 'फ्लूएंसी', 'pronunciation': 'प्रनन्सिएशन',
    'grammar': 'ग्रामर', 'polite': 'पोलाइट', 'professional': 'प्रोफेशनल', 'time': 'टाइम',
    'about': 'अबाउट', 'with': 'विद', 'from': 'फ्रॉम', 'at': 'एट', 'in': 'इन', 'on': 'ऑन',
    'for': 'फॉर', 'by': 'बाय', 'to': 'टू', 'of': 'ऑफ', 'and': 'एंड', 'or': 'ऑर', 'but': 'बट'
}

def to_devanagari(text):
    if not text:
        return ""
    # remove links / tags
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
            # simple transliterate
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

print("Helper loaded.")
