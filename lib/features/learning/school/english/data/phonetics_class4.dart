import '../models/phonetics.dart';

const class4Phonetics = PhoneticsLibrary(
  id: 'class4_phonetics',
  title: 'Phonetics',
  grade: 'Class 4',
  phonemes: [
    PhonemeEntry(
      id: 'short_a',
      ipaSymbol: '/æ/',
      label: 'Short A sound',
      soundsLike: 'as in "cat", "hat", "map" — close to Hindi "ऐ" but shorter and flatter',
      exampleWords: ['cat', 'hat', 'map', 'sad', 'bag'],
      mouthTip: 'Open your mouth wide and keep the sound short and quick — like saying "ऐ" but cutting it off fast.',
      category: PhonemeCategory.shortVowel,
    ),
    PhonemeEntry(
      id: 'long_a',
      ipaSymbol: '/eɪ/',
      label: 'Long A sound',
      soundsLike: 'as in "cake", "rain", "day" — sounds like Hindi "ए" gliding into "इ"',
      exampleWords: ['cake', 'rain', 'day', 'name', 'plate'],
      mouthTip: 'Start with your mouth a little open, then let your lips move slightly, like saying "ए" and sliding it forward.',
      category: PhonemeCategory.longVowel,
    ),
    PhonemeEntry(
      id: 'short_i',
      ipaSymbol: '/ɪ/',
      label: 'Short I sound',
      soundsLike: 'as in "sit", "big", "fish" — close to Hindi "इ" but quicker and lighter',
      exampleWords: ['sit', 'big', 'fish', 'pin', 'six'],
      mouthTip: 'Keep your mouth barely open and say a very short, light "इ" sound.',
      category: PhonemeCategory.shortVowel,
    ),
    PhonemeEntry(
      id: 'long_ee',
      ipaSymbol: '/iː/',
      label: 'Long EE sound',
      soundsLike: 'as in "sheep", "tree", "see" — like Hindi "ई", held a little longer',
      exampleWords: ['sheep', 'tree', 'see', 'feet', 'green'],
      mouthTip: 'Smile slightly and stretch out the "ई" sound a bit longer than usual.',
      category: PhonemeCategory.longVowel,
    ),
    PhonemeEntry(
      id: 'th_unvoiced',
      ipaSymbol: '/θ/',
      label: 'Soft TH sound',
      soundsLike: 'as in "think", "three", "bath" — there is no Hindi sound exactly like this one',
      exampleWords: ['think', 'three', 'bath', 'thumb', 'mouth'],
      mouthTip: 'Put your tongue lightly between your teeth and blow air out gently — no voice, just breath.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'th_voiced',
      ipaSymbol: '/ð/',
      label: 'Buzzy TH sound',
      soundsLike: 'as in "this", "that", "mother" — softer than "soft TH", with your voice buzzing',
      exampleWords: ['this', 'that', 'mother', 'father', 'brother'],
      mouthTip: 'Put your tongue between your teeth like the soft TH, but this time let your voice buzz through it.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'v_sound',
      ipaSymbol: '/v/',
      label: 'V sound',
      soundsLike: 'as in "van", "very", "seven" — many Hindi speakers mix this up with "w" (व)',
      exampleWords: ['van', 'very', 'seven', 'voice', 'love'],
      mouthTip: 'Touch your top teeth gently to your bottom lip and let your voice buzz through — different from the "w" lip-rounding sound.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'w_sound',
      ipaSymbol: '/w/',
      label: 'W sound',
      soundsLike: 'as in "wet", "window", "away" — round your lips like blowing a bubble',
      exampleWords: ['wet', 'window', 'away', 'water', 'well'],
      mouthTip: 'Round your lips into a small circle, like getting ready to blow, then relax into the vowel.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'sh_sound',
      ipaSymbol: '/ʃ/',
      label: 'SH sound',
      soundsLike: 'as in "ship", "wash", "shoe" — close to Hindi "श"',
      exampleWords: ['ship', 'wash', 'shoe', 'fish', 'shop'],
      mouthTip: 'Round your lips a little and push air out in one smooth hiss, like telling someone to be quiet.',
      category: PhonemeCategory.consonant,
    ),
  ],
  minimalPairs: [
    MinimalPair(
      id: 'ship_sheep',
      wordA: 'ship',
      wordB: 'sheep',
      contrastExplanation:
          '"Ship" uses the short I sound (/ɪ/), and "sheep" uses the long EE sound (/iː/). In Hindi we often '
          'hear both as "इ", but in English the vowel length changes the whole meaning of the word.',
    ),
    MinimalPair(
      id: 'bit_beat',
      wordA: 'bit',
      wordB: 'beat',
      contrastExplanation:
          '"Bit" is short and quick; "beat" stretches the vowel sound longer. Practice saying "bit" fast and '
          '"beat" with the "ई" held for a moment.',
    ),
    MinimalPair(
      id: 'van_wan',
      wordA: 'van',
      wordB: '(w)an sound in "one"',
      contrastExplanation:
          '"Van" starts with teeth touching the lip (/v/), while words starting with "w" round the lips '
          'without touching the teeth at all. Try saying "van" and "wet" one after another to feel the '
          'difference.',
    ),
    MinimalPair(
      id: 'think_this',
      wordA: 'think',
      wordB: 'this',
      contrastExplanation:
          'Both start with the tongue between the teeth, but "think" is a breathy, voiceless sound while '
          '"this" adds a buzzing voice. Put a finger on your throat — you should feel it vibrate for "this" '
          'but not for "think".',
    ),
    MinimalPair(
      id: 'cat_cut',
      wordA: 'cat',
      wordB: 'cut',
      contrastExplanation:
          '"Cat" uses the short A sound (mouth wide open), while "cut" uses a different short vowel with the '
          'mouth more relaxed and central. Many Hindi speakers pronounce both the same way — practice '
          'opening your mouth wider for "cat".',
    ),
  ],
  letterSoundRules: [
    LetterSoundRule(
      id: 'ph_f',
      letters: 'ph',
      soundDescription: 'usually makes the /f/ sound, just like the letter "f"',
      exampleWords: ['phone', 'elephant', 'photo', 'dolphin'],
    ),
    LetterSoundRule(
      id: 'igh_long_i',
      letters: 'igh',
      soundDescription: 'makes the long I sound, as in "my" or "eye"',
      exampleWords: ['light', 'night', 'high', 'right'],
    ),
    LetterSoundRule(
      id: 'ck_k',
      letters: 'ck',
      soundDescription: 'makes a single /k/ sound, usually after a short vowel',
      exampleWords: ['back', 'clock', 'duck', 'sick'],
    ),
    LetterSoundRule(
      id: 'ch_sound',
      letters: 'ch',
      soundDescription: 'usually makes the "ch" sound, close to Hindi "च"',
      exampleWords: ['chair', 'lunch', 'church', 'teacher'],
    ),
    LetterSoundRule(
      id: 'silent_k',
      letters: 'kn',
      soundDescription: 'the "k" is silent at the start of a word — only the /n/ sound is heard',
      exampleWords: ['know', 'knife', 'knee', 'knock'],
    ),
    LetterSoundRule(
      id: 'oo_long',
      letters: 'oo',
      soundDescription: 'often makes a long "ऊ" sound, as in "moon"',
      exampleWords: ['moon', 'food', 'zoo', 'school'],
    ),
    LetterSoundRule(
      id: 'silent_w',
      letters: 'wr',
      soundDescription: 'the "w" is silent at the start of a word — only the /r/ sound is heard',
      exampleWords: ['write', 'wrong', 'wrist', 'wrap'],
    ),
  ],
);
