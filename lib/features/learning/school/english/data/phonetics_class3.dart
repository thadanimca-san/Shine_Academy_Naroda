import '../models/phonetics.dart';

const class3Phonetics = PhoneticsLibrary(
  id: 'class3_phonetics',
  title: 'Phonetics',
  grade: 'Class 3',
  phonemes: [
    PhonemeEntry(
      id: 'short_e',
      ipaSymbol: '/e/',
      label: 'Short E sound',
      soundsLike: 'as in "bed", "pen", "red" — close to Hindi "ऍ" (like the "e" in "एक" said quickly)',
      exampleWords: ['bed', 'pen', 'red', 'ten', 'hen'],
      mouthTip: 'Open your mouth a little and keep the sound short and flat — say "ए" but stop it quickly.',
      category: PhonemeCategory.shortVowel,
    ),
    PhonemeEntry(
      id: 'short_o',
      ipaSymbol: '/ɒ/',
      label: 'Short O sound',
      soundsLike: 'as in "dog", "hot", "box" — close to Hindi "ऑ" (the open "o" sound)',
      exampleWords: ['dog', 'hot', 'box', 'top', 'pot'],
      mouthTip: 'Open your mouth round like a small "O" shape and let the sound out quickly.',
      category: PhonemeCategory.shortVowel,
    ),
    PhonemeEntry(
      id: 'short_u',
      ipaSymbol: '/ʌ/',
      label: 'Short U sound',
      soundsLike: 'as in "cup", "sun", "bus" — close to Hindi "अ" (a soft, quick "uh")',
      exampleWords: ['cup', 'sun', 'bus', 'run', 'fun'],
      mouthTip: 'Keep your mouth relaxed and barely open — say a quick, soft "अ" sound.',
      category: PhonemeCategory.shortVowel,
    ),
    PhonemeEntry(
      id: 'p_sound',
      ipaSymbol: '/p/',
      label: 'P sound',
      soundsLike: 'as in "pen", "map", "top" — close to Hindi "प" but with a small puff of air',
      exampleWords: ['pen', 'map', 'top', 'pig', 'cap'],
      mouthTip: 'Press your lips together tightly, then let them pop open with a little puff of air — no voice buzzing.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'b_sound',
      ipaSymbol: '/b/',
      label: 'B sound',
      soundsLike: 'as in "bat", "bag", "cab" — close to Hindi "ब"',
      exampleWords: ['bat', 'bag', 'cab', 'big', 'bed'],
      mouthTip: 'Press your lips together like for "p", but let your voice buzz as your lips pop open. Touch your throat to feel it buzz.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 's_sound',
      ipaSymbol: '/s/',
      label: 'S sound',
      soundsLike: 'as in "sun", "bus", "sit" — close to Hindi "स", a soft hiss with no buzzing',
      exampleWords: ['sun', 'bus', 'sit', 'sad', 'six'],
      mouthTip: 'Put your teeth close together and push air out in a quiet hiss, like a snake — no voice buzzing.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'z_sound',
      ipaSymbol: '/z/',
      label: 'Z sound',
      soundsLike: 'as in "zoo", "buzz", "zip" — close to Hindi "ज़", a buzzing hiss',
      exampleWords: ['zoo', 'buzz', 'zip', 'zebra', 'lazy'],
      mouthTip: 'Make the same hiss shape as "s", but this time turn your voice on so it buzzes like a bee.',
      category: PhonemeCategory.consonant,
    ),
  ],
  minimalPairs: [
    MinimalPair(
      id: 'pat_bat',
      wordA: 'pat',
      wordB: 'bat',
      contrastExplanation:
          '"Pat" starts with a quiet puff of air (/p/), and "bat" starts with a buzzing sound (/b/). Put your '
          'hand near your mouth — you should feel more air on "pat". Put a finger on your throat — you should '
          'feel a buzz only on "bat".',
    ),
    MinimalPair(
      id: 'sip_zip',
      wordA: 'sip',
      wordB: 'zip',
      contrastExplanation:
          '"Sip" starts with a quiet hiss (/s/) and no buzzing, while "zip" starts with the same hiss shape but '
          'with your voice buzzing (/z/). Touch your throat while saying both words to feel the difference.',
    ),
    MinimalPair(
      id: 'bed_bad',
      wordA: 'bed',
      wordB: 'bad',
      contrastExplanation:
          '"Bed" uses the short E sound, with the mouth only a little open, while "bad" uses the short A sound, '
          'with the mouth opened wider. Many students mix these up — practice opening your mouth extra wide '
          'for "bad".',
    ),
    MinimalPair(
      id: 'cup_cap',
      wordA: 'cup',
      wordB: 'cap',
      contrastExplanation:
          '"Cup" uses the short U sound (a soft, relaxed "अ"), while "cap" uses the short A sound (mouth wide '
          'open). Say "cup" with a relaxed mouth, then "cap" with a wide-open mouth to feel the change.',
    ),
  ],
  letterSoundRules: [
    LetterSoundRule(
      id: 'sh_digraph',
      letters: 'sh',
      soundDescription: 'makes one soft hissing sound, close to Hindi "श", as in "shop"',
      exampleWords: ['shop', 'fish', 'ship', 'wish'],
    ),
    LetterSoundRule(
      id: 'ch_digraph',
      letters: 'ch',
      soundDescription: 'makes the "ch" sound, close to Hindi "च", as in "chip"',
      exampleWords: ['chip', 'chin', 'much', 'lunch'],
    ),
    LetterSoundRule(
      id: 'bl_blend',
      letters: 'bl',
      soundDescription: 'the "b" and "l" sounds blend smoothly together at the start of a word',
      exampleWords: ['black', 'blue', 'block', 'blob'],
    ),
    LetterSoundRule(
      id: 'st_blend',
      letters: 'st',
      soundDescription: 'the "s" and "t" sounds blend together, both heard clearly, one after the other',
      exampleWords: ['stop', 'star', 'best', 'fast'],
    ),
    LetterSoundRule(
      id: 'double_letter_short_vowel',
      letters: 'ss / zz',
      soundDescription: 'doubling "s" or "z" keeps the vowel before it short and just makes one long hiss or buzz',
      exampleWords: ['miss', 'pass', 'buzz', 'fuzz'],
    ),
  ],
);
