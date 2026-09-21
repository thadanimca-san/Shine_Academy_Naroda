import '../models/phonetics.dart';

const class6Phonetics = PhoneticsLibrary(
  id: 'class6_phonetics',
  title: 'Phonetics',
  grade: 'Class 6',
  phonemes: [
    PhonemeEntry(
      id: 'f_sound_advanced',
      ipaSymbol: '/f/',
      label: 'F sound (breath only)',
      soundsLike: 'as in "fan", "laugh", "photo" — close to Hindi "फ" but with no puff of extra breath and no voice buzz at all',
      exampleWords: ['fan', 'laugh', 'photo', 'safe', 'roof'],
      mouthTip: 'Rest your top teeth gently on your bottom lip and push air out in a steady hiss — keep your throat silent, no buzzing.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'v_sound_advanced',
      ipaSymbol: '/v/',
      label: 'V sound (voiced pair of F)',
      soundsLike: 'as in "van", "save", "very" — same mouth shape as /f/ but your voice buzzes through it, unlike Hindi "व" which is made with both lips',
      exampleWords: ['van', 'save', 'very', 'move', 'live'],
      mouthTip: 'Use the exact same teeth-on-lip position as /f/, but switch your voice on so you feel a buzz — put a finger on your throat to check.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'zh_sound',
      ipaSymbol: '/ʒ/',
      label: 'ZH sound (buzzy SH)',
      soundsLike: 'as in "measure", "vision", "treasure" — like Hindi "श" but with your voice buzzing, similar to the middle sound in some Gujarati words with soft "ज"',
      exampleWords: ['measure', 'vision', 'treasure', 'usual', 'garage'],
      mouthTip: 'Shape your mouth exactly as you would for the SH sound, but turn your voice on so it buzzes — it should feel like a voiced version of "shh".',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'j_sound',
      ipaSymbol: '/dʒ/',
      label: 'J sound (as in judge)',
      soundsLike: 'as in "judge", "jump", "cage" — close to Hindi "ज" but starts with a hard little stop before the buzz',
      exampleWords: ['judge', 'jump', 'cage', 'bridge', 'giant'],
      mouthTip: 'Touch the tip of your tongue behind your top teeth to fully stop the air for a split second, then release it into a buzzy "zh" — the stop-and-release combination is what makes this different from /ʒ/.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'er_r_controlled',
      ipaSymbol: '/ɜːr/',
      label: 'ER sound (r-controlled vowel)',
      soundsLike: 'as in "bird", "her", "learn" — there is no equivalent in Hindi; it is not "अ" plus a rolled "र", but one single blended sound',
      exampleWords: ['bird', 'her', 'learn', 'first', 'nurse'],
      mouthTip: 'Curl the middle of your tongue up and back without letting the tip touch the roof of your mouth, and hold that shape for the whole vowel instead of adding a separate "r" sound afterward.',
      category: PhonemeCategory.longVowel,
    ),
    PhonemeEntry(
      id: 'ar_r_controlled',
      ipaSymbol: '/ɑːr/',
      label: 'AR sound (r-controlled vowel)',
      soundsLike: 'as in "car", "star", "farm" — starts like the open Hindi "आ" but the tongue pulls back for the "r" quality instead of a separate rolled sound',
      exampleWords: ['car', 'star', 'farm', 'dark', 'sharp'],
      mouthTip: 'Open your mouth wide for "आ", then pull the back of your tongue slightly back and down — do not tap or roll your tongue tip.',
      category: PhonemeCategory.longVowel,
    ),
    PhonemeEntry(
      id: 'schwa_unstressed',
      ipaSymbol: '/ə/',
      label: 'Schwa in unstressed syllables',
      soundsLike: 'a quick, lazy "अ" sound — the weakest, shortest vowel in English, heard in the parts of a word you do NOT stress',
      exampleWords: ['banana', 'camera', 'family', 'problem', 'about'],
      mouthTip: 'Let your mouth relax completely and barely open it — do not try to say a clear vowel here; just let the syllable slide by quickly and quietly.',
      category: PhonemeCategory.shortVowel,
    ),
    PhonemeEntry(
      id: 'word_stress_pattern',
      ipaSymbol: 'ˈstress',
      label: 'Word stress (which syllable is loudest)',
      soundsLike: 'one syllable in every word is said a little louder, longer, and clearer than the others — like beating a small drum harder on one beat',
      exampleWords: ['TAble', 'baNAna', 'comPUTer', 'ELephant', 'imPORtant'],
      mouthTip: 'Push a little extra breath and pitch into the stressed syllable and let the other syllables shrink toward a quick schwa — clap once on the stressed beat while saying the word to feel the pattern.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'ir_r_controlled',
      ipaSymbol: '/ɪər/',
      label: 'EAR sound (r-controlled vowel)',
      soundsLike: 'as in "ear", "near", "fear" — glides from a short Hindi "इ" into the same blended r-quality as in "bird", never a hard rolled "र"',
      exampleWords: ['ear', 'near', 'fear', 'clear', 'here'],
      mouthTip: 'Start with your tongue high and forward for a light "इ", then let it relax back and down smoothly into the r-coloured finish without tapping the tongue tip.',
      category: PhonemeCategory.diphthong,
    ),
  ],
  minimalPairs: [
    MinimalPair(
      id: 'fine_vine',
      wordA: 'fine',
      wordB: 'vine',
      contrastExplanation:
          '"Fine" starts with the breathy, voiceless /f/, while "vine" starts with the buzzing, voiced /v/ — '
          'the teeth-and-lip position is identical, so the only difference is whether your voice is switched '
          'on. Put a finger on your throat: silent for "fine", buzzing for "vine".',
    ),
    MinimalPair(
      id: 'measure_mesher',
      wordA: 'measure',
      wordB: '(mesh + er, like "fresher")',
      contrastExplanation:
          '"Measure" uses the buzzy /ʒ/ sound in the middle, while a word built on "mesh" uses the plain, '
          'breathy /ʃ/. Say "shh" for a plain hiss, then buzz your voice through the same shape to get the '
          'sound inside "measure".',
    ),
    MinimalPair(
      id: 'judge_zhudge',
      wordA: 'judge',
      wordB: '(genre-style "zh" sound alone)',
      contrastExplanation:
          '"Judge" begins with a hard little stop of the tongue before the buzz (/dʒ/), while words like '
          '"genre" use only the buzzy glide with no stop (/ʒ/). Try starting "judge" by fully blocking the '
          'air for an instant before releasing the buzz — that stop is missing in a plain "zh" sound.',
    ),
    MinimalPair(
      id: 'bird_bed',
      wordA: 'bird',
      wordB: 'bed',
      contrastExplanation:
          '"Bird" uses the r-controlled /ɜːr/ vowel, made by curling the tongue back with no separate "r" '
          'tap, while "bed" uses a plain short vowel with the tongue flat and forward. Many Hindi speakers '
          'add a rolled "र" after the vowel in "bird" — instead, hold the curled tongue shape as one smooth '
          'sound.',
    ),
    MinimalPair(
      id: 'present_noun_verb',
      wordA: 'PREsent (a gift)',
      wordB: 'preSENT (to give/show)',
      contrastExplanation:
          'Same spelling, same letters, but the stress moves: as a noun the first syllable is stressed '
          '("PRE-sent"), and as a verb the second syllable is stressed ("pre-SENT"). Many English words '
          'shift stress like this to change from noun to verb — try clapping on the stressed syllable for '
          'each meaning.',
    ),
    MinimalPair(
      id: 'car_cut',
      wordA: 'car',
      wordB: 'cut',
      contrastExplanation:
          '"Car" uses the r-controlled /ɑːr/ vowel with the tongue pulled back, while "cut" uses a short, '
          'central vowel with no r-colouring at all. Practice holding the "car" vowel steady without adding '
          'any extra rolled sound at the end.',
    ),
    MinimalPair(
      id: 'photograph_photography',
      wordA: 'PHOtograph',
      wordB: 'phoTOgraphy',
      contrastExplanation:
          'Adding the suffix "-y" shifts the stress from the first syllable to the second, and the vowel '
          'sounds change with it — unstressed syllables flatten toward a schwa. Say both words aloud and '
          'notice how the "o" in "photo-" changes quality when it is no longer stressed.',
    ),
  ],
  letterSoundRules: [
    LetterSoundRule(
      id: 'tion_shun',
      letters: '-tion',
      soundDescription: 'makes a "shun" sound (/ʃən/), close to Hindi "शन", with the stress always falling on the syllable right before it',
      exampleWords: ['nation', 'station', 'action', 'education'],
    ),
    LetterSoundRule(
      id: 'sion_zhun',
      letters: '-sion',
      soundDescription: 'after a vowel usually makes a buzzy "zhun" sound (/ʒən/), but after a consonant it makes "shun" (/ʃən/) instead',
      exampleWords: ['vision', 'television', 'tension', 'mission'],
    ),
    LetterSoundRule(
      id: 'silent_letters_advanced',
      letters: 's / b / p (in island, debt, receipt)',
      soundDescription: 'some consonants are written but never pronounced at all, usually left over from old spellings — you must simply memorise these',
      exampleWords: ['island', 'debt', 'receipt', 'doubt'],
    ),
    LetterSoundRule(
      id: 'ear_er_rule',
      letters: 'ear / ere / eer',
      soundDescription: 'before a consonant these often make the r-controlled "ear" sound (/ɪər/), as in "near" — but watch out, "ear" can also make /ɜːr/ as in "learn" or /ɛər/ as in "bear"',
      exampleWords: ['near', 'clear', 'here', 'deer'],
    ),
    LetterSoundRule(
      id: 'or_ar_stress_shift',
      letters: '-or / -ate',
      soundDescription: 'these endings often carry a weak schwa sound in nouns, but "-ate" is pronounced as a fuller vowel in verbs, shifting the whole word\'s rhythm',
      exampleWords: ['actor', 'estimate', 'graduate', 'sailor'],
    ),
    LetterSoundRule(
      id: 'prefix_stress_shift',
      letters: 're- / un- / dis-',
      soundDescription: 'these prefixes are usually unstressed and said quickly with a schwa, letting the main stress fall later in the word',
      exampleWords: ['rewrite', 'unhappy', 'disagree', 'return'],
    ),
    LetterSoundRule(
      id: 'ough_variety',
      letters: 'ough',
      soundDescription: 'one of English\'s trickiest patterns — it can sound like "uff" (enough), "oh" (though), "oo" (through), or "ow" (bough), so each word must be learned individually',
      exampleWords: ['enough', 'though', 'through', 'bought'],
    ),
  ],
);
