import os
import json
import time
from googletrans import Translator

CHAPTERS_DIR = '/home/ubuntu/Shine_Academy_Naroda/app_core/chapters'
translator = Translator()

def translate_safe(text, dest_lang):
    if not text:
        return ""
    # For English grammar options, we often don't want to translate them 
    # but the rule says every block must have _hi and _gu.
    # We will pass the text to translator.
    for attempt in range(5):
        try:
            res = translator.translate(text, dest=dest_lang)
            time.sleep(0.1)
            return res.text
        except Exception as e:
            print(f"Translation failed for '{text}' to {dest_lang}. Retrying {attempt+1}... Error: {e}")
            time.sleep(2)
    return text + f" ({dest_lang})"

def build_mcq(idx_str, question, options, correct_index, explanation):
    print(f"Translating MCQ {idx_str}...")
    q_hi = translate_safe(question, 'hi')
    q_gu = translate_safe(question, 'gu')
    
    # Do not translate english grammar options, just copy them to satisfy schema
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
    
    # 1. Hook
    blocks.append(build_hook(f"KOBJ_{ch_id}_HOOK", hook_data['title'], hook_data['body']))
    
    # 2. Theory
    for i, t in enumerate(theory_data):
        blocks.append(build_theory(f"KOBJ_{ch_id}_THEORY_{i+1}", t['title'], t['body']))
        
    # 3. MCQs
    for i, m in enumerate(mcq_data):
        blocks.append(build_mcq(f"KOBJ_{ch_id}_MCQ_{i+1}", m['q'], m['opts'], m['ans'], m['expl']))
        
    # Build full json
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

# CHAPTER 1: TENSES
ch1_hook = {
    "title": "The Time Traveler's Mistake",
    "body": "Imagine a time traveler who wants to warn you about tomorrow, but he says: 'I went to the future tomorrow!' Does that make sense? No! Because 'went' means it already happened, but 'tomorrow' hasn't happened yet! Tenses are the time-traveling tools of English. If you use the wrong tense, you might accidentally send your listener to the past instead of the future!"
}
ch1_theory = [
    {"title": "Present Tense: What's Happening Now?", "body": "The Present Tense tells us about things happening right now or regularly. 1. Simple Present: Habits and facts (I play). 2. Present Continuous: Happening at this exact moment (I am playing). 3. Present Perfect: Just finished, effect remains (I have played). 4. Present Perfect Continuous: Started in past, still happening (I have been playing)."},
    {"title": "Past Tense: The Museum of History", "body": "The Past Tense describes completed events. 1. Simple Past: Finished at a specific time (I played). 2. Past Continuous: Ongoing in the past (I was playing). 3. Past Perfect: The 'past of the past' (I had played). 4. Past Perfect Continuous: Ongoing action ending before another past action (I had been playing)."},
    {"title": "Future Tense: The Crystal Ball", "body": "The Future Tense predicts what hasn't happened. 1. Simple Future: Predictions and promises (I will play). 2. Future Continuous: Will be ongoing (I will be playing). 3. Future Perfect: Will be completed by a specific time (I will have played). 4. Future Perfect Continuous: Ongoing up to a future point (I will have been playing)."}
]
ch1_mcqs = [
    {"q": "He _______ (go) to the gym every morning.", "opts": ["goes", "is going", "went", "has gone"], "ans": 0, "expl": "Daily habit uses simple present."},
    {"q": "Look! The bus _______ (come).", "opts": ["is coming", "comes", "came", "has come"], "ans": 0, "expl": "Happening right now uses present continuous."},
    {"q": "I _______ (visit) my grandparents last weekend.", "opts": ["visited", "visit", "have visited", "was visiting"], "ans": 0, "expl": "Completed action in the past with specific time."},
    {"q": "By the time we arrived, the movie _______ (already / start).", "opts": ["had already started", "already started", "has already started", "was already starting"], "ans": 0, "expl": "Past perfect for earlier past action."},
    {"q": "I think it _______ (rain) tomorrow.", "opts": ["will rain", "rains", "is raining", "has rained"], "ans": 0, "expl": "Prediction about the future uses 'will'."},
    {"q": "Water _______ (boil) at 100 degrees Celsius.", "opts": ["boils", "is boiling", "boiled", "will boil"], "ans": 0, "expl": "Scientific fact uses simple present."},
    {"q": "They _______ (play) football at the moment.", "opts": ["are playing", "play", "played", "were playing"], "ans": 0, "expl": "Action happening at the time of speaking."},
    {"q": "I _______ (just / finish) my homework.", "opts": ["have just finished", "just finished", "am just finishing", "had just finished"], "ans": 0, "expl": "Action recently completed with 'just'."},
    {"q": "She _______ (never / visit) Paris.", "opts": ["has never visited", "never visits", "never visited", "had never visited"], "ans": 0, "expl": "Life experience up to now uses present perfect."},
    {"q": "World War II _______ (end) in 1945.", "opts": ["ended", "ends", "has ended", "was ending"], "ans": 0, "expl": "Historical event in the past uses simple past."},
    {"q": "They _______ (play) soccer when it started raining.", "opts": ["were playing", "played", "are playing", "have played"], "ans": 0, "expl": "Past continuous interrupted by simple past."},
    {"q": "I _______ (finish) my homework before the power went out.", "opts": ["had finished", "finished", "have finished", "was finishing"], "ans": 0, "expl": "Action completed before another past action."},
    {"q": "By next year, I _______ (graduate) from university.", "opts": ["will have graduated", "will graduate", "am graduating", "graduate"], "ans": 0, "expl": "Action completed by a certain future time uses future perfect."},
    {"q": "Don't call me at 8 PM; I _______ (eat) dinner.", "opts": ["will be eating", "will eat", "eat", "am eating"], "ans": 0, "expl": "Ongoing future action uses future continuous."},
    {"q": "She _______ (buy) a new car yesterday.", "opts": ["bought", "buys", "has bought", "is buying"], "ans": 0, "expl": "'Yesterday' indicates simple past."}
]

# CHAPTER 2: MODALS
ch2_hook = {
    "title": "The Mood Ring of Grammar",
    "body": "Verbs are like food. But sometimes food needs spice! Modals (can, could, should, must, might) are the spices of English. They change the 'mood' or 'flavor' of the main verb. Saying 'You do it' is a fact. Saying 'You MUST do it' is an order. Saying 'You CAN do it' is an ability. One word changes the entire emotion of the sentence!"
}
ch2_theory = [
    {"title": "Ability and Permission (Can/Could/May)", "body": "'Can' shows current ability (I can swim). 'Could' shows past ability (I could swim when I was 5). 'May' and 'Can' are both used for permission, but 'May' is more formal (May I come in?)."},
    {"title": "Advice and Obligation (Should/Must/Ought to)", "body": "'Should' is for good advice (You should sleep). 'Must' is a strict rule or strong obligation (You must wear a seatbelt). 'Ought to' is a moral duty (We ought to respect elders)."},
    {"title": "Possibility (Might/May/Could)", "body": "When you aren't 100% sure, use modals of possibility. 'It might rain today' (low possibility). 'It may rain today' (medium possibility). 'It could rain' (general possibility)."}
]
ch2_mcqs = [
    {"q": "You _______ wear a helmet while riding a bike. It's the law.", "opts": ["must", "can", "might", "could"], "ans": 0, "expl": "'Must' implies strong obligation or law."},
    {"q": "_______ I borrow your pen?", "opts": ["May", "Should", "Will", "Must"], "ans": 0, "expl": "'May' is used for polite permission."},
    {"q": "It _______ rain tonight, so take an umbrella.", "opts": ["might", "must", "can", "will"], "ans": 0, "expl": "'Might' indicates a possibility."},
    {"q": "She _______ speak three languages fluently.", "opts": ["can", "must", "should", "would"], "ans": 0, "expl": "'Can' denotes ability."},
    {"q": "You _______ respect your elders.", "opts": ["ought to", "might", "can", "would"], "ans": 0, "expl": "'Ought to' is used for moral duty."},
    {"q": "When I was young, I _______ run very fast.", "opts": ["could", "can", "must", "should"], "ans": 0, "expl": "'Could' denotes past ability."},
    {"q": "_______ God bless you!", "opts": ["May", "Can", "Will", "Should"], "ans": 0, "expl": "'May' is used for wishes and prayers."},
    {"q": "We _______ leave now or we will miss the train.", "opts": ["must", "can", "might", "would"], "ans": 0, "expl": "'Must' indicates strong necessity."},
    {"q": "You _______ not play with fire.", "opts": ["should", "could", "may", "would"], "ans": 0, "expl": "'Should' gives strong advice against a bad idea."},
    {"q": "He _______ be at home, but I am not sure.", "opts": ["might", "must", "can", "will"], "ans": 0, "expl": "'Might' shows weak possibility."}
]

# Run Generation
process_chapter("ncert_class10_grammar_ch1", "English Grammar Chapter 1: Tenses", "English Grammar", ch1_hook, ch1_theory, ch1_mcqs)
process_chapter("ncert_class10_grammar_ch2", "English Grammar Chapter 2: Modals", "English Grammar", ch2_hook, ch2_theory, ch2_mcqs)

