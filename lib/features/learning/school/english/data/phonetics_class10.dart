import '../models/phonetics.dart';

const class10Phonetics = PhoneticsLibrary(
  id: 'class10_phonetics',
  title: 'Phonetics',
  grade: 'Class 10',
  phonemes: [
    PhonemeEntry(
      id: 'class10_intonation_rising',
      ipaSymbol: '↗',
      label: 'Rising Intonation',
      soundsLike: 'the pitch of voice rises toward the end of a sentence — typically used for Yes/No questions and to show politeness or uncertainty',
      exampleWords: ['Are you coming?↗', 'Really?↗', 'Excuse me?↗'],
      mouthTip: 'Let your voice climb higher on the final word or syllable, as if inviting a response.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'class10_intonation_falling',
      ipaSymbol: '↘',
      label: 'Falling Intonation',
      soundsLike: 'the pitch of voice falls toward the end of a sentence — typically used for statements, commands, and "wh-" questions to sound confident and complete',
      exampleWords: ['I am going home.↘', 'Close the door.↘', 'What is your name?↘'],
      mouthTip: 'Let your voice drop lower on the final stressed word, signalling that the sentence is finished.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'class10_tag_question_intonation',
      ipaSymbol: '↗ / ↘',
      label: 'Tag Question Intonation',
      soundsLike: 'a rising tone on a tag question ("isn\'t it?") shows genuine uncertainty, while a falling tone shows the speaker is fairly sure and just wants agreement',
      exampleWords: ['You are coming, aren\'t you?↗ (uncertain)', 'It\'s cold today, isn\'t it?↘ (confident)'],
      mouthTip: 'Practice the same tag question both ways to hear how the meaning subtly shifts with intonation.',
      category: PhonemeCategory.consonant,
    ),
    PhonemeEntry(
      id: 'class10_reduced_auxiliary',
      ipaSymbol: '/əv/',
      label: 'Reduced "have" (as in "should have")',
      soundsLike: 'in fast natural speech, "have" after modal verbs often reduces to a quick "uh" sound, sometimes misheard as "of"',
      exampleWords: ['should have (sounds like "shoulda")', 'could have (sounds like "coulda")', 'would have (sounds like "woulda")'],
      mouthTip: 'Notice that this is always spelled "have", never "of", even though it sounds reduced in speech.',
      category: PhonemeCategory.shortVowel,
    ),
    PhonemeEntry(
      id: 'class10_elision',
      ipaSymbol: '∅',
      label: 'Elision (dropped sounds in connected speech)',
      soundsLike: 'certain sounds are dropped entirely in fast, natural speech to make words easier to say together',
      exampleWords: ['next day (sounds like "nex day")', 'must be (sounds like "mus be")'],
      mouthTip: 'Notice how consonant clusters at word boundaries often simplify naturally — this is normal fluent speech, not incorrect pronunciation.',
      category: PhonemeCategory.consonant,
    ),
  ],
  minimalPairs: [
    MinimalPair(
      id: 'class10_pair_can_cant',
      wordA: 'I can go.',
      wordB: 'I can\'t go.',
      contrastExplanation: 'In fast speech, "can" (weak, schwa vowel) and "can\'t" (fuller vowel, often with a clearer final /t/ or nasalisation) are distinguished mainly by vowel length and stress, not just spelling — an important listening skill.',
    ),
    MinimalPair(
      id: 'class10_pair_statement_question',
      wordA: 'You\'re leaving.↘ (statement)',
      wordB: 'You\'re leaving?↗ (question)',
      contrastExplanation: 'The exact same words convey a statement or a surprised question depending entirely on whether the intonation falls or rises.',
    ),
  ],
  letterSoundRules: [
    LetterSoundRule(
      id: 'class10_rule_weak_forms_review',
      letters: 'weak forms (a, an, the, of, to, for)',
      soundDescription: 'these small function words are almost always reduced to a schwa /ə/ in natural connected speech, unlike their full pronunciation when said in isolation',
      exampleWords: ['a cup of tea (natural: "uh cup uv tea")', 'What are you doing? (natural: "whatcha doing")'],
    ),
    LetterSoundRule(
      id: 'class10_rule_assimilation',
      letters: 'assimilation at word boundaries',
      soundDescription: 'a final consonant sound sometimes shifts slightly to match the sound that follows it in the next word, for smoother connected speech',
      exampleWords: ['ten girls (n often sounds closer to "ng")', 'good boy (d often sounds softer, closer to "b")'],
    ),
    LetterSoundRule(
      id: 'class10_rule_stress_in_compounds',
      letters: 'compound noun stress',
      soundDescription: 'compound nouns (two words combined) usually stress the first word, while adjective+noun phrases usually stress the second',
      exampleWords: ['GREENhouse (compound noun)', 'green HOUSE (a house that is green)', 'BLACKboard vs. black BOARD'],
    ),
  ],
);
