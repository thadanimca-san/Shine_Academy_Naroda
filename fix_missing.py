import os

base_dir = '/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school/english/data'

content = """
import '../models/grammar_topic.dart';

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
import 'practice_class10_determiners_conjunctions.dart';
import 'practice_class10_integrated_grammar.dart';
import 'practice_class10_nonfinites.dart';
import 'practice_class10_reported_speech.dart';
import 'practice_class10_voice.dart';

const Map<String, GrammarLibrary> grammarLibraryByGrade = {
  'Class 3': GrammarLibrary(gradeLevel: 'Class 3', topics: [
    nounsClass3,
    verbsClass3,
    adjectivesClass3,
    singularPluralClass3,
    prepositionsClass3,
  ]),
  'Class 4': GrammarLibrary(gradeLevel: 'Class 4', topics: [
    nounsClass4,
    pronounsClass4,
    articlesClass4,
    prepositionsClass4,
    tensesClass4,
  ]),
  'Class 5': GrammarLibrary(gradeLevel: 'Class 5', topics: [
    sentenceTypesClass5,
    adjectivesClass5,
    adverbsClass5,
    conjunctionsClass5,
    punctuationClass5,
  ]),
  'Class 6': GrammarLibrary(gradeLevel: 'Class 6', topics: [
    voiceClass6,
    speechClass6,
    clausesClass6,
    determinersClass6,
    modalVerbsClass6,
  ]),
  'Class 7': GrammarLibrary(gradeLevel: 'Class 7', topics: [
    subjectVerbConcordClass7,
    voiceClass7,
    reportedSpeechClass7,
    prepositionsClass7,
    nonFinitesClass7,
  ]),
  'Class 8': GrammarLibrary(gradeLevel: 'Class 8', topics: [
    voiceClass8,
    modalVerbsClass8,
    nonFinitesClass8,
    determinersClass8,
    conjunctionsClass8,
  ]),
  'Class 9': GrammarLibrary(gradeLevel: 'Class 9', topics: [
    clausesClass9,
    reportedSpeechClass9,
    conditionalsClass9,
    prepositionsClass9,
    editingClass9,
  ]),
  'Class 10': GrammarLibrary(gradeLevel: 'Class 10', topics: [
    voiceClass10,
    reportedSpeechClass10,
    nonFinitesClass10,
    determinersConjunctionsClass10,
    integratedGrammarClass10,
  ]),
};
"""
with open(f'{base_dir}/practice_topics.dart', 'w') as f:
    f.write(content)

