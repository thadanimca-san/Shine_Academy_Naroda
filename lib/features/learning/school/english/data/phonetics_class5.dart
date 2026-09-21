import '../models/phonetics.dart';

const class5Phonetics = PhoneticsLibrary(
  id: 'class5_phonetics',
  title: 'Phonetics',
  grade: 'Class 5',
  phonemes: [
    PhonemeEntry(
      id: 'ow_diphthong',
      ipaSymbol: '/aʊ/',
      label: 'OW sound',
      soundsLike: 'as in "cow", "house", "out" — like Hindi "अ" sliding quickly into "उ"',
      exampleWords: ['cow', 'house', 'out', 'mouse', 'town'],
      mouthTip: 'Start with your mouth wide open like "अ", then quickly round your lips into "उ" — one smooth glide, not two separate sounds.',
      category: PhonemeCategory.diphthong,
    ),
    PhonemeEntry(
      id: 'oy_diphthong',
      ipaSymbol: '/ɔɪ/',
      label: 'OY sound',
      soundsLike: 'as in "boy", "coin", "toy" — like Hindi "ऑ" sliding into "इ"',
      exampleWords: ['boy', 'coin', 'toy', 'join', 'voice'],
      mouthTip: 'Start with rounded lips for "ऑ", then quickly move your tongue up and forward toward "इ" — glide the two together fast.',
      category: PhonemeCategory.diphthong,
    ),
    PhonemeEntry(
      id: 'z_sound',
      ipaSymbol: '/z/',
      label: 'Z sound',
      soundsLike: 'as in "zoo", "buzz", "zebra" — close to Hindi "ज़" but with a buzzing vibration',
      exampleWords: ['zoo', 'buzz', 'zebra', 'zip', 'lazy'],
      mouthTip: 'Put your tongue where you would for "s", but turn your voice on so it buzzes — put a finger on your throat to feel the difference from "s".',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 's_sound',
      ipaSymbol: '/s/',
      label: 'S sound',
      soundsLike: 'as in "sun", "bus", "sit" — close to Hindi "स", no buzzing at all',
      exampleWords: ['sun', 'bus', 'sit', 'snake', 'glass'],
      mouthTip: 'Keep your tongue close to the roof of your mouth just behind your teeth and blow air out in a quiet hiss — no voice, just breath.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'r_sound',
      ipaSymbol: '/r/',
      label: 'English R sound',
      soundsLike: 'as in "red", "car", "run" — softer than the rolled Hindi "र", with the tongue not touching anywhere',
      exampleWords: ['red', 'car', 'run', 'road', 'right'],
      mouthTip: 'Curl the tip of your tongue back slightly without letting it touch the roof of your mouth, and let the sound glide out smoothly — do not tap or roll it like Hindi "र".',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'ng_sound',
      ipaSymbol: '/ŋ/',
      label: 'NG sound',
      soundsLike: 'as in "sing", "ring", "song" — close to Hindi "ङ" as in "रंग"',
      exampleWords: ['sing', 'ring', 'song', 'king', 'long'],
      mouthTip: 'Lift the back of your tongue to touch the back of the roof of your mouth and let the sound hum out through your nose — do not add a hard "g" or "k" after it.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'schwa',
      ipaSymbol: '/ə/',
      label: 'Schwa (uh) sound',
      soundsLike: 'the quick, lazy "uh" in unstressed parts of words like "banana", "sofa", "about" — like a very short, weak Hindi "अ"',
      exampleWords: ['banana', 'sofa', 'about', 'the', 'ago'],
      mouthTip: 'Relax your mouth completely — lips loose, tongue in the middle — and let out a short, soft "uh" with almost no effort or emphasis.',
      category: PhonemeCategory.shortVowel,
    ),
    PhonemeEntry(
      id: 'long_o',
      ipaSymbol: '/oʊ/',
      label: 'Long O sound',
      soundsLike: 'as in "boat", "go", "snow" — like Hindi "ओ" gliding into a soft "उ"',
      exampleWords: ['boat', 'go', 'snow', 'home', 'road'],
      mouthTip: 'Round your lips for "ओ" and let the sound gently glide toward "उ" at the end, like the word is closing your mouth slowly.',
      category: PhonemeCategory.diphthong,
    ),
    PhonemeEntry(
      id: 'j_sound',
      ipaSymbol: '/dʒ/',
      label: 'J sound',
      soundsLike: 'as in "jam", "bridge", "juice" — close to Hindi "ज" with a little more force at the start',
      exampleWords: ['jam', 'bridge', 'juice', 'jump', 'orange'],
      mouthTip: 'Touch the tip of your tongue to the ridge behind your top teeth, then release it with a buzzing voice all in one quick push.',
      category: PhonemeCategory.consonant,
    ),
  ],
  minimalPairs: [
    MinimalPair(
      id: 'sip_zip',
      wordA: 'sip',
      wordB: 'zip',
      contrastExplanation:
          '"Sip" starts with a quiet hiss (/s/, no voice), while "zip" starts with the same tongue position but '
          'with your voice buzzing (/z/). Put a finger on your throat — it should stay still for "sip" but '
          'vibrate for "zip".',
    ),
    MinimalPair(
      id: 'sing_sin',
      wordA: 'sing',
      wordB: 'sin',
      contrastExplanation:
          '"Sing" ends with the nasal "ng" sound (/ŋ/) made at the back of the mouth, while "sin" ends with a '
          'plain /n/ made with the tongue at the front, near the teeth. Say both slowly and notice where your '
          'tongue touches at the end.',
    ),
    MinimalPair(
      id: 'race_raise',
      wordA: 'race',
      wordB: 'raise',
      contrastExplanation:
          '"Race" ends with the quiet /s/ hiss, while "raise" ends with the buzzing /z/ sound. The spelling '
          'looks similar, but the final sound — and your throat vibration — is different.',
    ),
    MinimalPair(
      id: 'red_led',
      wordA: 'red',
      wordB: '(l)ed as in "led"',
      contrastExplanation:
          '"Red" starts with the English /r/, made without the tongue touching anywhere, while words starting '
          'with "l" touch the tongue tip firmly to the ridge behind the teeth. Neither is the tapped Hindi '
          '"र" — practice keeping your tongue floating for "red".',
    ),
    MinimalPair(
      id: 'cow_car',
      wordA: 'cow',
      wordB: 'car',
      contrastExplanation:
          '"Cow" uses the gliding /aʊ/ diphthong that ends with rounded lips, while "car" uses a single long '
          'vowel with the mouth staying open and the sound held steady. Notice how your lips move at the end '
          'of "cow" but stay still through "car".',
    ),
    MinimalPair(
      id: 'boy_toy',
      wordA: 'boy',
      wordB: 'toy',
      contrastExplanation:
          'Both share the same /ɔɪ/ gliding vowel, but they start with different consonants — "b" is voiced '
          '(voice buzzes right away) and "t" is voiceless (a quiet puff of air first). Feel your throat to '
          'spot the difference at the very start of each word.',
    ),
  ],
  letterSoundRules: [
    LetterSoundRule(
      id: 'tion_shun',
      letters: 'tion',
      soundDescription: 'usually makes a "shun" sound, close to Hindi "शन", at the end of a word',
      exampleWords: ['station', 'action', 'nation', 'education'],
    ),
    LetterSoundRule(
      id: 'ough_variants',
      letters: 'ough',
      soundDescription:
          'can be pronounced several different ways depending on the word — as "uff" in "enough", "oh" in '
          '"though", "oo" in "through", or "ow" in "plough" — so each word must be learned separately',
      exampleWords: ['enough', 'though', 'through', 'plough', 'thought'],
    ),
    LetterSoundRule(
      id: 'soft_c',
      letters: 'c (before e, i, y)',
      soundDescription: 'makes a soft /s/ sound, close to Hindi "स", when followed by "e", "i", or "y"',
      exampleWords: ['city', 'ice', 'cycle', 'fence'],
    ),
    LetterSoundRule(
      id: 'hard_c',
      letters: 'c (before a, o, u)',
      soundDescription: 'makes a hard /k/ sound when followed by "a", "o", or "u", or at the end of a word',
      exampleWords: ['cat', 'cot', 'cup', 'music'],
    ),
    LetterSoundRule(
      id: 'soft_g',
      letters: 'g (before e, i, y)',
      soundDescription: 'often makes a soft /dʒ/ sound, close to Hindi "ज", when followed by "e", "i", or "y"',
      exampleWords: ['gem', 'giant', 'gym', 'stage'],
    ),
    LetterSoundRule(
      id: 'hard_g',
      letters: 'g (before a, o, u)',
      soundDescription: 'makes a hard /g/ sound, close to Hindi "ग", when followed by "a", "o", or "u"',
      exampleWords: ['garden', 'go', 'gum', 'flag'],
    ),
    LetterSoundRule(
      id: 'ng_spelling',
      letters: 'ng',
      soundDescription: 'together make the single nasal /ŋ/ sound, not a separate "n" plus "g"',
      exampleWords: ['sing', 'ring', 'strong', 'morning'],
    ),
  ],
);
