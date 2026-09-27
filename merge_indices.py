import os

base_dir = '/home/ubuntu/Shine_Academy_Naroda/lib/features/learning/school'

def merge_topics(file_name, import_base, map_name):
    # Read english3to6
    with open(f'{base_dir}/english3to6/data/{file_name}', 'r') as f:
        content3 = f.read()
    # Read english_simulation
    with open(f'{base_dir}/english_simulation/data/{file_name}', 'r') as f:
        content7 = f.read()
        
    # We will just write a new file for english/data
    out_lines = []
    
    if file_name == 'reading_topics.dart':
        out = f"""import '../models/reading_passage.dart';
import 'reading_class3.dart';
import 'reading_class4.dart';
import 'reading_class5.dart';
import 'reading_class6.dart';
import 'reading_class7.dart';
import 'reading_class8.dart';
import 'reading_class9.dart';
import 'reading_class10.dart';

const Map<String, ReadingLibrary> readingLibraryByGrade = {{
  'Class 3': class3Reading,
  'Class 4': class4Reading,
  'Class 5': class5Reading,
  'Class 6': class6Reading,
  'Class 7': class7Reading,
  'Class 8': class8Reading,
  'Class 9': class9Reading,
  'Class 10': class10Reading,
}};
"""
        with open(f'{base_dir}/english/data/{file_name}', 'w') as f:
            f.write(out)

    elif file_name == 'writing_topics.dart':
        out = f"""import '../models/writing_prompt.dart';
import 'writing_class3.dart';
import 'writing_class4.dart';
import 'writing_class5.dart';
import 'writing_class6.dart';
import 'writing_class7.dart';
import 'writing_class8.dart';
import 'writing_class9.dart';
import 'writing_class10.dart';

const Map<String, WritingLibrary> writingLibraryByGrade = {{
  'Class 3': class3Writing,
  'Class 4': class4Writing,
  'Class 5': class5Writing,
  'Class 6': class6Writing,
  'Class 7': class7Writing,
  'Class 8': class8Writing,
  'Class 9': class9Writing,
  'Class 10': class10Writing,
}};
"""
        with open(f'{base_dir}/english/data/{file_name}', 'w') as f:
            f.write(out)

    elif file_name == 'practice_topics.dart':
        out = f"""import '../models/grammar_topic.dart';
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

const Map<String, GrammarLibrary> grammarLibraryByGrade = {{
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
}};
"""
        with open(f'{base_dir}/english/data/{file_name}', 'w') as f:
            f.write(out)

    elif file_name == 'phonetics_topics.dart':
        out = f"""import '../models/phonetics_topic.dart';
import 'phonetics_class3.dart';
import 'phonetics_class4.dart';
import 'phonetics_class5.dart';
import 'phonetics_class6.dart';
import 'phonetics_class7.dart';
import 'phonetics_class8.dart';
import 'phonetics_class9.dart';
import 'phonetics_class10.dart';

const Map<String, PhoneticsLibrary> phoneticsLibraryByGrade = {{
  'Class 3': class3Phonetics,
  'Class 4': class4Phonetics,
  'Class 5': class5Phonetics,
  'Class 6': class6Phonetics,
  'Class 7': class7Phonetics,
  'Class 8': class8Phonetics,
  'Class 9': class9Phonetics,
  'Class 10': class10Phonetics,
}};
"""
        with open(f'{base_dir}/english/data/{file_name}', 'w') as f:
            f.write(out)

    elif file_name == 'dictionary_topics.dart':
        out = f"""import '../models/dictionary_topic.dart';
import 'class10_academic_words.dart';
import 'class10_idioms_phrasal_verbs.dart';
import 'class10_synonyms_antonyms.dart';
import 'class3_animals.dart';
import 'class3_body.dart';
import 'class3_clothes.dart';
import 'class3_colours_shapes.dart';
import 'class3_family.dart';
import 'class3_feelings.dart';
import 'class3_food.dart';
import 'class3_nature.dart';
import 'class3_numbers.dart';
import 'class3_occupations.dart';
import 'class3_school.dart';
import 'class3_science.dart';
import 'class3_social_studies.dart';
import 'class3_sports.dart';
import 'class3_time.dart';
import 'class3_transport.dart';
import 'class3_weather.dart';
import 'class4_animals.dart';
import 'class4_body.dart';
import 'class4_clothes.dart';
import 'class4_colours_shapes.dart';
import 'class4_family.dart';
import 'class4_feelings.dart';
import 'class4_food.dart';
import 'class4_nature.dart';
import 'class4_numbers.dart';
import 'class4_occupations.dart';
import 'class4_school.dart';
import 'class4_science.dart';
import 'class4_social_studies.dart';
import 'class4_sports.dart';
import 'class4_time.dart';
import 'class4_transport.dart';
import 'class4_weather.dart';
import 'class5_animals.dart';
import 'class5_body.dart';
import 'class5_clothes.dart';
import 'class5_colours_shapes.dart';
import 'class5_family.dart';
import 'class5_feelings.dart';
import 'class5_food.dart';
import 'class5_nature.dart';
import 'class5_numbers.dart';
import 'class5_occupations.dart';
import 'class5_school.dart';
import 'class5_science.dart';
import 'class5_social_studies.dart';
import 'class5_sports.dart';
import 'class5_time.dart';
import 'class5_transport.dart';
import 'class5_weather.dart';
import 'class6_animals.dart';
import 'class6_body.dart';
import 'class6_clothes.dart';
import 'class6_colours_shapes.dart';
import 'class6_family.dart';
import 'class6_feelings.dart';
import 'class6_food.dart';
import 'class6_nature.dart';
import 'class6_numbers.dart';
import 'class6_occupations.dart';
import 'class6_school.dart';
import 'class6_science.dart';
import 'class6_social_studies.dart';
import 'class6_sports.dart';
import 'class6_time.dart';
import 'class6_transport.dart';
import 'class6_weather.dart';
import 'class7_academic_words.dart';
import 'class7_exam_vocabulary.dart';
import 'class7_idioms_phrasal_verbs.dart';
import 'class7_synonyms_antonyms.dart';
import 'class8_academic_words.dart';
import 'class8_idioms_phrasal_verbs.dart';
import 'class8_synonyms_antonyms.dart';
import 'class9_academic_words.dart';
import 'class9_idioms_phrasal_verbs.dart';
import 'class9_synonyms_antonyms.dart';

const Map<String, DictionaryLibrary> dictionaryLibraryByGrade = {{
  'Class 3': DictionaryLibrary(gradeLevel: 'Class 3', topics: [
    class3Animals, class3Body, class3Clothes, class3ColoursShapes,
    class3Family, class3Feelings, class3Food, class3Nature, class3Numbers,
    class3Occupations, class3School, class3Science, class3SocialStudies,
    class3Sports, class3Time, class3Transport, class3Weather,
  ]),
  'Class 4': DictionaryLibrary(gradeLevel: 'Class 4', topics: [
    class4Animals, class4Body, class4Clothes, class4ColoursShapes,
    class4Family, class4Feelings, class4Food, class4Nature, class4Numbers,
    class4Occupations, class4School, class4Science, class4SocialStudies,
    class4Sports, class4Time, class4Transport, class4Weather,
  ]),
  'Class 5': DictionaryLibrary(gradeLevel: 'Class 5', topics: [
    class5Animals, class5Body, class5Clothes, class5ColoursShapes,
    class5Family, class5Feelings, class5Food, class5Nature, class5Numbers,
    class5Occupations, class5School, class5Science, class5SocialStudies,
    class5Sports, class5Time, class5Transport, class5Weather,
  ]),
  'Class 6': DictionaryLibrary(gradeLevel: 'Class 6', topics: [
    class6Animals, class6Body, class6Clothes, class6ColoursShapes,
    class6Family, class6Feelings, class6Food, class6Nature, class6Numbers,
    class6Occupations, class6School, class6Science, class6SocialStudies,
    class6Sports, class6Time, class6Transport, class6Weather,
  ]),
  'Class 7': DictionaryLibrary(gradeLevel: 'Class 7', topics: [
    class7AcademicWords,
    class7SynonymsAntonyms,
    class7IdiomsPhrasalVerbs,
    class7ExamVocabulary,
  ]),
  'Class 8': DictionaryLibrary(gradeLevel: 'Class 8', topics: [
    class8AcademicWords,
    class8SynonymsAntonyms,
    class8IdiomsPhrasalVerbs,
  ]),
  'Class 9': DictionaryLibrary(gradeLevel: 'Class 9', topics: [
    class9AcademicWords,
    class9SynonymsAntonyms,
    class9IdiomsPhrasalVerbs,
  ]),
  'Class 10': DictionaryLibrary(gradeLevel: 'Class 10', topics: [
    class10AcademicWords,
    class10SynonymsAntonyms,
    class10IdiomsPhrasalVerbs,
  ]),
}};
"""
        with open(f'{base_dir}/english/data/{file_name}', 'w') as f:
            f.write(out)


merge_topics('reading_topics.dart', '', '')
merge_topics('writing_topics.dart', '', '')
merge_topics('practice_topics.dart', '', '')
merge_topics('phonetics_topics.dart', '', '')
merge_topics('dictionary_topics.dart', '', '')

