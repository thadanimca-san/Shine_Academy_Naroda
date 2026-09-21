/// One English speech sound (phoneme), taught with kid-friendly framing
/// rather than raw IPA jargon, though the IPA symbol is kept for reference.
/// Audio is played live via device text-to-speech on the example words,
/// so no pre-recorded files are needed.
class PhonemeEntry {
  final String id;
  final String ipaSymbol;
  final String label; // kid-friendly name, e.g. "Short A sound"
  final String soundsLike; // e.g. "as in 'cat', 'hat', 'map'"
  final List<String> exampleWords;
  final String mouthTip; // simple description of how to make the sound
  final PhonemeCategory category;

  const PhonemeEntry({
    required this.id,
    required this.ipaSymbol,
    required this.label,
    required this.soundsLike,
    required this.exampleWords,
    required this.mouthTip,
    required this.category,
  });
}

enum PhonemeCategory { shortVowel, longVowel, consonant, diphthong }

/// Two words that differ by exactly one sound — the core drill for
/// training a student's ear to hear sounds Hindi/Gujarati don't
/// distinguish (e.g. ship/sheep, bit/beat).
class MinimalPair {
  final String id;
  final String wordA;
  final String wordB;
  final String contrastExplanation; // what's different and why it matters

  const MinimalPair({
    required this.id,
    required this.wordA,
    required this.wordB,
    required this.contrastExplanation,
  });
}

/// A letter or letter-combination and the sound(s) it typically makes —
/// the phonics rules that connect spelling to pronunciation.
class LetterSoundRule {
  final String id;
  final String letters; // e.g. "ph", "igh", "ck"
  final String soundDescription; // e.g. "makes the /f/ sound"
  final List<String> exampleWords;

  const LetterSoundRule({
    required this.id,
    required this.letters,
    required this.soundDescription,
    required this.exampleWords,
  });
}

/// A themed collection of phonetics content for one grade.
class PhoneticsLibrary {
  final String id;
  final String title;
  final String grade;
  final List<PhonemeEntry> phonemes;
  final List<MinimalPair> minimalPairs;
  final List<LetterSoundRule> letterSoundRules;

  const PhoneticsLibrary({
    required this.id,
    required this.title,
    required this.grade,
    required this.phonemes,
    required this.minimalPairs,
    required this.letterSoundRules,
  });
}
