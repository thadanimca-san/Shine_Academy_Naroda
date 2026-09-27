import re

path = '/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school/english/data/chapter_class3_bookfair.dart'
with open(path, 'r') as f:
    content = f.read()

# We need to extract all english texts and combine them into `chapterText`.
# Then extract all hindi texts and combine them into `hindiSummary`.
# Then extract all gujarati texts and combine them into `gujaratiSummary`.

english_texts = []
hindi_texts = []
gujarati_texts = []

eng_matches = re.findall(r"english:\s*'(.*?)',", content, re.DOTALL)
hin_matches = re.findall(r"hindi:\s*'(.*?)',", content, re.DOTALL)
guj_matches = re.findall(r"gujarati:\s*'(.*?)',", content, re.DOTALL)

def clean_string(s):
    # remove the inline string concatenations like ' ... ' \n ' ... '
    s = re.sub(r"'\s*\n\s*'", "", s)
    return s.strip()

for em in eng_matches:
    english_texts.append(clean_string(em))
for hm in hin_matches:
    hindi_texts.append(clean_string(hm))
for gm in guj_matches:
    gujarati_texts.append(clean_string(gm))

chapter_text = "\\n\\n".join(english_texts)
hindi_summary = " ".join(hindi_texts)
guj_summary = " ".join(gujarati_texts)

new_content = f"""import '../models/chapter.dart';

const chapterClass3Bookfair = Chapter(
  id: 'chapter_class3_bookfair',
  title: 'The School Book Fair',
  grade: 'Class 3',
  emoji: '📚',
  chapterText: '''{chapter_text}''',
  hindiSummary: '''{hindi_summary}''',
  gujaratiSummary: '''{guj_summary}''',
  glosses: [
    InlineGloss(
      word: 'stalls',
      meaningHi: 'दुकानें / स्टॉल',
      hiTransliteration: 'dukaanein / stall',
      meaningGu: 'દુકાનો / સ્ટોલ',
      guTransliteration: 'dukaano / stall',
    ),
    InlineGloss(
      word: 'stacked',
      meaningHi: 'चट्टा लगाना / ढेर लगा होना',
      hiTransliteration: 'chatta lagana / dher laga hona',
      meaningGu: 'ઢગલો કરવો / થપ્પી મારવી',
      guTransliteration: 'dhaglo karvo / thappi maarvi',
    ),
    InlineGloss(
      word: 'wandered',
      meaningHi: 'भटकना / घूमना',
      hiTransliteration: 'bhatakna / ghoomna',
      meaningGu: 'ભટકવું / રખડવું',
      guTransliteration: 'bhatakvu / rakhadvu',
    ),
    InlineGloss(
      word: 'swap',
      meaningHi: 'बदलना / अदला-बदली करना',
      hiTransliteration: 'badalna / adla-badli karna',
      meaningGu: 'બદલવું / અદલાબદલી કરવી',
      guTransliteration: 'badalvu / adlbadli karvi',
    ),
    InlineGloss(
      word: 'traded',
      meaningHi: 'व्यापार किया / बदला',
      hiTransliteration: 'vyaapaar kiya / badla',
      meaningGu: 'વેપાર કર્યો / બદલ્યું',
      guTransliteration: 'vepar karyo / badalyu',
    ),
    InlineGloss(
      word: 'fascinating',
      meaningHi: 'आकर्षक / मोहक',
      hiTransliteration: 'aakarshak / mohak',
      meaningGu: 'આકર્ષક / મનમોહક',
      guTransliteration: 'aakarshak / manmohak',
    ),
  ],
);
"""

with open(path, 'w') as f:
    f.write(new_content)

