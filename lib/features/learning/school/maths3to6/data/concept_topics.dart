import '../models/concept.dart';
import 'concepts_class3.dart';
import 'concepts_class4.dart';
import 'concepts_class5.dart';
import 'concepts_class6.dart';

/// Grades in display order, each with its glossary.
const Map<String, ConceptTopic> conceptTopicByGrade = {
  'Class 3': class3Concepts,
  'Class 4': class4Concepts,
  'Class 5': class5Concepts,
  'Class 6': class6Concepts,
};
