import '../models/dictionary_word.dart';
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

const Map<String, List<DictionaryTopic>> dictionaryTopicsByGrade = {
  'Class 3': [
    class3Animals,
    class3Body,
    class3Clothes,
    class3ColoursShapes,
    class3Family,
    class3Feelings,
    class3Food,
    class3Nature,
    class3Numbers,
    class3Occupations,
    class3School,
    class3Science,
    class3SocialStudies,
    class3Sports,
    class3Time,
    class3Transport,
    class3Weather,
  ],
  'Class 4': [
    class4Animals,
    class4Body,
    class4Clothes,
    class4ColoursShapes,
    class4Family,
    class4Feelings,
    class4Food,
    class4Nature,
    class4Numbers,
    class4Occupations,
    class4School,
    class4Science,
    class4SocialStudies,
    class4Sports,
    class4Time,
    class4Transport,
    class4Weather,
  ],
  'Class 5': [
    class5Animals,
    class5Body,
    class5Clothes,
    class5ColoursShapes,
    class5Family,
    class5Feelings,
    class5Food,
    class5Nature,
    class5Numbers,
    class5Occupations,
    class5School,
    class5Science,
    class5SocialStudies,
    class5Sports,
    class5Time,
    class5Transport,
    class5Weather,
  ],
  'Class 6': [
    class6Animals,
    class6Body,
    class6Clothes,
    class6ColoursShapes,
    class6Family,
    class6Feelings,
    class6Food,
    class6Nature,
    class6Numbers,
    class6Occupations,
    class6School,
    class6Science,
    class6SocialStudies,
    class6Sports,
    class6Time,
    class6Transport,
    class6Weather,
  ],
  'Class 7': [
    class7AcademicWords,
    class7ExamVocabulary,
    class7IdiomsPhrasalVerbs,
    class7SynonymsAntonyms,
  ],
  'Class 8': [
    class8AcademicWords,
    class8IdiomsPhrasalVerbs,
    class8SynonymsAntonyms,
  ],
  'Class 9': [
    class9AcademicWords,
    class9IdiomsPhrasalVerbs,
    class9SynonymsAntonyms,
  ],
  'Class 10': [
    class10AcademicWords,
    class10IdiomsPhrasalVerbs,
    class10SynonymsAntonyms,
  ],
};

final allDictionaryTopics = dictionaryTopicsByGrade.values.expand((topics) => topics).toList();
