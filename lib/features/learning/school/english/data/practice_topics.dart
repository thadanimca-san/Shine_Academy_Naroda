import '../models/practice_question.dart';
import 'practice_class10_determiners_conjunctions.dart';
import 'practice_class10_integrated_grammar.dart';
import 'practice_class10_nonfinites.dart';
import 'practice_class10_reported_speech.dart';
import 'practice_class10_voice.dart';
import 'practice_class3_adjectives.dart';
import 'practice_class3_nouns.dart';
import 'practice_class3_prepositions.dart';
import 'practice_class3_singular_plural.dart';
import 'practice_class3_verbs.dart';
import 'practice_class4_articles.dart';
import 'practice_class4_nouns.dart';
import 'practice_class4_prepositions.dart';
import 'practice_class4_pronouns.dart';
import 'practice_class4_tenses.dart';
import 'practice_class5_adjectives.dart';
import 'practice_class5_adverbs.dart';
import 'practice_class5_conjunctions.dart';
import 'practice_class5_punctuation.dart';
import 'practice_class5_sentence_types.dart';
import 'practice_class6_clauses.dart';
import 'practice_class6_determiners.dart';
import 'practice_class6_modal_verbs.dart';
import 'practice_class6_speech.dart';
import 'practice_class6_voice.dart';
import 'practice_class7_nonfinites.dart';
import 'practice_class7_prepositions.dart';
import 'practice_class7_reported_speech.dart';
import 'practice_class7_subject_verb_concord.dart';
import 'practice_class7_voice.dart';
import 'practice_class8_conjunctions.dart';
import 'practice_class8_determiners.dart';
import 'practice_class8_modal_verbs.dart';
import 'practice_class8_nonfinites.dart';
import 'practice_class8_voice.dart';
import 'practice_class9_clauses.dart';
import 'practice_class9_conditionals.dart';
import 'practice_class9_editing.dart';
import 'practice_class9_prepositions.dart';
import 'practice_class9_reported_speech.dart';

const Map<String, List<PracticeTopic>> practiceTopicsByGrade = {
  'Class 3': [
    class3Adjectives,
    class3Nouns,
    class3Prepositions,
    class3SingularPlural,
    class3Verbs,
  ],
  'Class 4': [
    class4Articles,
    class4Nouns,
    class4Prepositions,
    class4Pronouns,
    class4Tenses,
  ],
  'Class 5': [
    class5Adjectives,
    class5Adverbs,
    class5Conjunctions,
    class5Punctuation,
    class5SentenceTypes,
  ],
  'Class 6': [
    class6Clauses,
    class6Determiners,
    class6ModalVerbs,
    class6Speech,
    class6Voice,
  ],
  'Class 7': [
    class7NonFinites,
    class7Prepositions,
    class7ReportedSpeech,
    class7SubjectVerbConcord,
    class7Voice,
  ],
  'Class 8': [
    class8Conjunctions,
    class8Determiners,
    class8ModalVerbs,
    class8NonFinites,
    class8Voice,
  ],
  'Class 9': [
    class9Clauses,
    class9Conditionals,
    class9Editing,
    class9Prepositions,
    class9ReportedSpeech,
  ],
  'Class 10': [
    class10DeterminersConjunctions,
    class10IntegratedGrammar,
    class10NonFinites,
    class10ReportedSpeech,
    class10Voice,
  ],
};

final allPracticeTopics = practiceTopicsByGrade.values.expand((topics) => topics).toList();
