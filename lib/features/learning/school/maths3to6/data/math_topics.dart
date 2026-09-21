import '../models/math_question.dart';

import 'math_class3_addition.dart';
import 'math_class3_subtraction.dart';
import 'math_class3_multiplication.dart';
import 'math_class3_shapes.dart';
import 'math_class3_measurement.dart';
import 'math_class3_numbers.dart';
import 'math_class3_time_money.dart';
import 'math_class3_data_handling.dart';

import 'math_class4_addition.dart';
import 'math_class4_subtraction.dart';
import 'math_class4_multiplication.dart';
import 'math_class4_division.dart';
import 'math_class4_fractions.dart';
import 'math_class4_measurement.dart';
import 'math_class4_time_money.dart';
import 'math_class4_geometry.dart';

import 'math_class5_large_numbers.dart';
import 'math_class5_division.dart';
import 'math_class5_fractions_decimals.dart';
import 'math_class5_perimeter_area.dart';
import 'math_class5_time_money.dart';
import 'math_class5_multiplication.dart';
import 'math_class5_patterns_geometry.dart';
import 'math_class5_data_handling.dart';

import 'math_class6_integers.dart';
import 'math_class6_fractions_decimals.dart';
import 'math_class6_ratio_proportion.dart';
import 'math_class6_geometry.dart';
import 'math_class6_percentages.dart';
import 'math_class6_algebra.dart';
import 'math_class6_mensuration.dart';
import 'math_class6_data_handling.dart';

/// Maths topics per grade, Class 3-6 — mirrors the sister English app's
/// grade-grouped registry pattern.
const List<MathTopic> class3MathTopics = [
  class3Addition,
  class3Subtraction,
  class3Multiplication,
  class3Shapes,
  class3Measurement,
  class3Numbers,
  class3TimeMoney,
  class3DataHandling,
];

const List<MathTopic> class4MathTopics = [
  class4Addition,
  class4Subtraction,
  class4Multiplication,
  class4Division,
  class4Fractions,
  class4Measurement,
  class4TimeMoney,
  class4Geometry,
];

const List<MathTopic> class5MathTopics = [
  class5LargeNumbers,
  class5Division,
  class5FractionsDecimals,
  class5PerimeterArea,
  class5TimeMoney,
  class5Multiplication,
  class5PatternsGeometry,
  class5DataHandling,
];

const List<MathTopic> class6MathTopics = [
  class6Integers,
  class6FractionsDecimals,
  class6RatioProportion,
  class6Geometry,
  class6Percentages,
  class6Algebra,
  class6Mensuration,
  class6DataHandling,
];

/// Grades in display order, each with its topic list.
const Map<String, List<MathTopic>> mathTopicsByGrade = {
  'Class 3': class3MathTopics,
  'Class 4': class4MathTopics,
  'Class 5': class5MathTopics,
  'Class 6': class6MathTopics,
};

/// Flat list of every maths topic across all grades.
const List<MathTopic> allMathTopics = [
  ...class3MathTopics,
  ...class4MathTopics,
  ...class5MathTopics,
  ...class6MathTopics,
];
