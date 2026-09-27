import os
import json
import time
from googletrans import Translator

CHAPTERS_DIR = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
translator = Translator()

def translate_safe(text, dest_lang):
    if not text:
        return ""
    for attempt in range(5):
        try:
            res = translator.translate(text, dest=dest_lang)
            time.sleep(0.1)
            return res.text
        except Exception as e:
            print(f"Translation failed for '{text[:20]}...' to {dest_lang}. Retrying {attempt+1}...")
            time.sleep(2)
    return text + f" ({dest_lang})"

def build_mcq(idx_str, question, options, correct_index, explanation):
    print(f"Translating MCQ {idx_str}...")
    q_hi = translate_safe(question, 'hi')
    q_gu = translate_safe(question, 'gu')
    opts_hi = options[:]
    opts_gu = options[:]
    expl_hi = translate_safe(explanation, 'hi')
    expl_gu = translate_safe(explanation, 'gu')
    
    return {
        "id": idx_str,
        "type": "mcq",
        "question": question,
        "question_hi": q_hi,
        "question_gu": q_gu,
        "options": options,
        "options_hi": opts_hi,
        "options_gu": opts_gu,
        "correct_index": correct_index,
        "explanation": explanation,
        "explanation_hi": expl_hi,
        "explanation_gu": expl_gu
    }

def build_theory(idx_str, title, body):
    print(f"Translating Theory {idx_str}...")
    title_hi = translate_safe(title, 'hi')
    title_gu = translate_safe(title, 'gu')
    body_hi = translate_safe(body, 'hi')
    body_gu = translate_safe(body, 'gu')
    return {
        "id": idx_str,
        "type": "theory",
        "title": title,
        "title_hi": title_hi,
        "title_gu": title_gu,
        "body": body,
        "body_hi": body_hi,
        "body_gu": body_gu
    }

def build_hook(idx_str, title, body):
    print(f"Translating Hook {idx_str}...")
    title_hi = translate_safe(title, 'hi')
    title_gu = translate_safe(title, 'gu')
    body_hi = translate_safe(body, 'hi')
    body_gu = translate_safe(body, 'gu')
    return {
        "id": idx_str,
        "type": "hook",
        "title": title,
        "title_hi": title_hi,
        "title_gu": title_gu,
        "body": body,
        "body_hi": body_hi,
        "body_gu": body_gu
    }

def process_chapter(ch_id, title, subject, hook_data, theory_data, mcq_data):
    file_path = os.path.join(CHAPTERS_DIR, f"{ch_id}.json")
    blocks = []
    
    blocks.append(build_hook(f"KOBJ_{ch_id}_HOOK", hook_data['title'], hook_data['body']))
    for i, t in enumerate(theory_data):
        blocks.append(build_theory(f"KOBJ_{ch_id}_THEORY_{i+1}", t['title'], t['body']))
    for i, m in enumerate(mcq_data):
        blocks.append(build_mcq(f"KOBJ_{ch_id}_MCQ_{i+1}", m['q'], m['opts'], m['ans'], m['expl']))
        
    full_json = {
        "metadata": {
            "id": ch_id,
            "title": title,
            "subject": subject,
            "grade": "10"
        },
        "blocks": blocks
    }
    
    with open(file_path, "w", encoding="utf-8") as f:
        json.dump(full_json, f, indent=2, ensure_ascii=False)
        f.write("\n")
    print(f"Successfully generated {file_path} with {len(blocks)} blocks.")

# CHAPTER 3: Subject-Verb Concord
ch3_hook = {
    "title": "The Dance Partners",
    "body": "A sentence is like a dance. The Subject and the Verb must always be in sync. If the subject is one person (singular), the verb must follow a singular step. If the subject is many people (plural), the verb changes its step to plural. If they don't match, they step on each other's toes, and the sentence sounds terrible! This rule of matching is called 'Subject-Verb Concord'."
}
ch3_theory = [
    {"title": "The Golden Rule", "body": "Singular subjects take singular verbs (The boy plays). Plural subjects take plural verbs (The boys play). Note that adding 's' to a noun makes it plural, but adding 's' to a verb makes it singular!"},
    {"title": "Tricky Subjects with 'And'", "body": "When two subjects are joined by 'and', they take a plural verb (Ram and Shyam are friends). However, if the two nouns suggest one idea, the verb is singular (Bread and butter is my favorite breakfast)."},
    {"title": "Words that are always Singular", "body": "Words like Everyone, Everybody, Someone, Nobody, Each, Every, Either, Neither always take a singular verb. Example: 'Everyone is happy.' 'Neither of the boys has come.'"}
]
ch3_mcqs = [
    {"q": "The list of items _______ on the desk.", "opts": ["is", "are", "am", "were"], "ans": 0, "expl": "The subject is 'list' (singular), not 'items'."},
    {"q": "A bouquet of yellow roses _______ color and fragrance to the room.", "opts": ["lends", "lend", "are lending", "have lent"], "ans": 0, "expl": "The subject is 'bouquet' (singular), so the verb is 'lends'."},
    {"q": "Either my shoes or your coat _______ always on the floor.", "opts": ["is", "are", "were", "have been"], "ans": 0, "expl": "With 'either...or', the verb matches the subject closest to it ('coat' is singular)."},
    {"q": "Rice and beans, my favorite dish, _______ me of my native Puerto Rico.", "opts": ["reminds", "remind", "are reminding", "have reminded"], "ans": 0, "expl": "'Rice and beans' is treated as a single dish, taking a singular verb."},
    {"q": "Every one of those books _______ fiction.", "opts": ["is", "are", "were", "am"], "ans": 0, "expl": "'Every one' is a singular subject."},
    {"q": "The committee _______ leading very different lives in private.", "opts": ["are", "is", "am", "was"], "ans": 0, "expl": "When a collective noun acts as individuals, it takes a plural verb."},
    {"q": "Neither the plates nor the serving bowl _______ on that shelf.", "opts": ["goes", "go", "are going", "were going"], "ans": 0, "expl": "Verb matches the closest subject ('bowl' is singular)."},
    {"q": "The Prime Minister, together with his wife, _______ the press cordially.", "opts": ["greets", "greet", "are greeting", "have greeted"], "ans": 0, "expl": "Phrases like 'together with' do not change the number of the subject (Prime Minister is singular)."},
    {"q": "Mathematics _______ John's favorite subject.", "opts": ["is", "are", "were", "am"], "ans": 0, "expl": "Subjects like Mathematics, Physics, News are singular."},
    {"q": "Fifty dollars _______ a lot of money to lose.", "opts": ["is", "are", "were", "am"], "ans": 0, "expl": "Amounts of money or periods of time are considered singular."}
]

# CHAPTER 4: Reported Speech
ch4_hook = {
    "title": "The Gossiping Grammar",
    "body": "Reported speech is basically how we gossip! If your friend Maya tells you, 'I am buying a car,' and you want to tell someone else what she said, you don't repeat her exact words like a robot. You say: 'Maya said that she was buying a car.' You changed the pronoun (I -> she) and shifted the tense backward (am -> was). That is the heart of Reported Speech!"
}
ch4_theory = [
    {"title": "The Rule of Backshifting", "body": "When the reporting verb is in the past tense (e.g., 'He said'), the tense inside the quote shifts one step back into the past. Simple Present becomes Simple Past. Present Continuous becomes Past Continuous. Simple Past becomes Past Perfect."},
    {"title": "Pronouns and Time Words", "body": "Pronouns change to match the speaker (I -> He/She). Time words also shift backward. 'Today' becomes 'that day'. 'Tomorrow' becomes 'the next day'. 'Yesterday' becomes 'the previous day'."},
    {"title": "Questions and Commands", "body": "For YES/NO questions, we use 'if' or 'whether' (He asked if I was ready). For WH-questions, we keep the WH-word (He asked where I lived). For commands, we use 'to + verb' (He ordered me to sit down)."}
]
ch4_mcqs = [
    {"q": "He said, 'I like coffee.' -> He said that he _______ coffee.", "opts": ["liked", "likes", "had liked", "is liking"], "ans": 0, "expl": "Simple present 'like' changes to simple past 'liked'."},
    {"q": "She said, 'I am reading.' -> She said that she _______ reading.", "opts": ["was", "is", "had been", "will be"], "ans": 0, "expl": "Present continuous 'am' changes to past continuous 'was'."},
    {"q": "Tom said, 'I bought a car.' -> Tom said that he _______ a car.", "opts": ["had bought", "bought", "buys", "has bought"], "ans": 0, "expl": "Simple past 'bought' changes to past perfect 'had bought'."},
    {"q": "The teacher said to me, 'Stand up!' -> The teacher ordered me _______.", "opts": ["to stand up", "standing up", "that I stand up", "stand up"], "ans": 0, "expl": "Commands use 'to + base verb'."},
    {"q": "He asked, 'Do you speak English?' -> He asked me _______ I spoke English.", "opts": ["if", "that", "where", "what"], "ans": 0, "expl": "Yes/No questions use 'if' or 'whether'."},
    {"q": "She asked, 'Where is the station?' -> She asked where the station _______.", "opts": ["was", "is", "had been", "will be"], "ans": 0, "expl": "WH-questions keep the WH-word and shift the verb to past tense at the end."},
    {"q": "Rahul said, 'I will call you tomorrow.' -> Rahul said he would call me _______.", "opts": ["the next day", "tomorrow", "today", "the previous day"], "ans": 0, "expl": "'Tomorrow' changes to 'the next day'."},
    {"q": "Riya says, 'I am happy.' -> Riya says that she _______ happy.", "opts": ["is", "was", "had been", "has been"], "ans": 0, "expl": "If the reporting verb ('says') is present, the tense does NOT change."},
    {"q": "He said, 'The sun rises in the east.' -> He said that the sun _______ in the east.", "opts": ["rises", "rose", "had risen", "will rise"], "ans": 0, "expl": "Universal truths do not change tense."},
    {"q": "She said, 'I have finished.' -> She said that she _______ finished.", "opts": ["had", "has", "was", "is"], "ans": 0, "expl": "Present perfect 'have' changes to past perfect 'had'."}
]

# CHAPTER 5: Determiners
ch5_hook = {
    "title": "The Pointers",
    "body": "If I say, 'Give me apple,' you might ask: 'Which apple? Any apple? That specific apple? Your apple?' Nouns need a tiny pointer word before them to clarify what exactly we are talking about. Those pointers are called Determiners. They determine the noun's identity. Words like 'a', 'the', 'my', 'this', 'some', 'any' act as the ultimate tour guides for nouns!"
}
ch5_theory = [
    {"title": "Articles (A/An/The)", "body": "'A' and 'An' are indefinite (any one item). We use 'A' before consonant sounds and 'An' before vowel sounds. 'The' is definite (a specific item we both know)."},
    {"title": "Demonstratives (This/That/These/Those)", "body": "These point to specific items. 'This' (singular) and 'These' (plural) are for things near you. 'That' (singular) and 'Those' (plural) are for things far away."},
    {"title": "Quantifiers (Some/Any/Much/Many)", "body": "They show amount. 'Some' is for positive sentences. 'Any' is for negative/questions. 'Many' is for countable nouns (many books). 'Much' is for uncountable nouns (much water)."}
]
ch5_mcqs = [
    {"q": "I want _______ apple from that basket.", "opts": ["an", "a", "the", "some"], "ans": 0, "expl": "'Apple' starts with a vowel sound, so we use 'an'."},
    {"q": "Could you pass me _______ salt, please?", "opts": ["the", "a", "an", "any"], "ans": 0, "expl": "We use 'the' for specific, understood items in context (the salt on the table)."},
    {"q": "I don't have _______ money left in my wallet.", "opts": ["any", "some", "many", "a"], "ans": 0, "expl": "'Any' is used in negative sentences."},
    {"q": "_______ students were absent yesterday.", "opts": ["Many", "Much", "Any", "A little"], "ans": 0, "expl": "'Students' is a countable noun, so we use 'many'."},
    {"q": "Can I have _______ water, please?", "opts": ["some", "any", "many", "few"], "ans": 0, "expl": "'Some' is used in polite requests even if it's a question."},
    {"q": "_______ book on the top shelf is mine.", "opts": ["That", "This", "These", "Those"], "ans": 0, "expl": "'Top shelf' implies distance, and 'book' is singular, so 'That'."},
    {"q": "There is very _______ time left before the exam.", "opts": ["little", "few", "many", "a"], "ans": 0, "expl": "'Time' is uncountable, so we use 'little'."},
    {"q": "She is _______ honest girl.", "opts": ["an", "a", "the", "some"], "ans": 0, "expl": "'Honest' starts with a vowel sound ('O'), so we use 'an'."},
    {"q": "I have read _______ book in this library.", "opts": ["every", "all", "much", "many"], "ans": 0, "expl": "'Every' is used with singular nouns to mean all individually."},
    {"q": "_______ of the two boys won a prize.", "opts": ["Each", "Every", "All", "Some"], "ans": 0, "expl": "'Each' is used when focusing on individuals within a group, especially two."}
]

# Run Generation
process_chapter("ncert_class10_grammar_ch3", "English Grammar Chapter 3: Subject-Verb Concord", "English Grammar", ch3_hook, ch3_theory, ch3_mcqs)
process_chapter("ncert_class10_grammar_ch4", "English Grammar Chapter 4: Reported Speech", "English Grammar", ch4_hook, ch4_theory, ch4_mcqs)
process_chapter("ncert_class10_grammar_ch5", "English Grammar Chapter 5: Determiners", "English Grammar", ch5_hook, ch5_theory, ch5_mcqs)

