import 'package:flutter/material.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';
import '../models/chapter_model.dart';
import '../simulations/class7/integers_simulation_widget.dart';
import '../simulations/class7/fractions_decimals_simulation_widget.dart';
import '../simulations/class7/data_handling_simulation_widget.dart';
import '../simulations/class7/simple_equations_simulation_widget.dart';
import '../simulations/class7/lines_angles_simulation_widget.dart';
import '../simulations/class7/triangle_properties_simulation_widget.dart';
import '../simulations/class7/congruence_simulation_widget.dart';
import '../simulations/class7/comparing_quantities_simulation_widget.dart';
import '../simulations/class7/rational_numbers_simulation_widget.dart';
import '../simulations/class7/practical_geometry_simulation_widget.dart';
import '../simulations/class7/perimeter_area_simulation_widget.dart';
import '../simulations/class7/algebraic_expressions_simulation_widget.dart';
import '../simulations/class7/exponents_powers_simulation_widget.dart';
import '../simulations/class7/symmetry_simulation_widget.dart';
import '../simulations/class7/solid_shapes_simulation_widget.dart';
import '../simulations/class8/rational_numbers_simulation_widget.dart';
import '../simulations/class8/linear_equations_simulation_widget.dart';
import '../simulations/class8/quadrilaterals_simulation_widget.dart';
import '../simulations/class8/practical_geometry_simulation_widget.dart';
import '../simulations/class8/data_handling_simulation_widget.dart';
import '../simulations/class8/squares_square_roots_simulation_widget.dart';
import '../simulations/class8/cubes_cube_roots_simulation_widget.dart';
import '../simulations/class8/comparing_quantities_simulation_widget.dart';
import '../simulations/class8/algebraic_identities_simulation_widget.dart';
import '../simulations/class8/solid_shapes_simulation_widget.dart';
import '../simulations/class8/mensuration_simulation_widget.dart';
import '../simulations/class8/exponents_powers_simulation_widget.dart';
import '../simulations/class8/proportions_simulation_widget.dart';
import '../simulations/class8/factorisation_simulation_widget.dart';
import '../simulations/class8/introduction_graphs_simulation_widget.dart';
import '../simulations/class8/playing_numbers_simulation_widget.dart';
import '../simulations/class9/number_systems_simulation_widget.dart';
import '../simulations/class9/polynomials_simulation_widget.dart';
import '../simulations/class9/coordinate_geometry_simulation_widget.dart';
import '../simulations/class9/linear_equations_two_variables_simulation_widget.dart';
import '../simulations/class9/euclids_geometry_simulation_widget.dart';
import '../simulations/class9/lines_angles_simulation_widget.dart';
import '../simulations/class9/triangles_simulation_widget.dart';
import '../simulations/class9/quadrilaterals_simulation_widget.dart';
import '../simulations/class9/areas_parallelograms_triangles_simulation_widget.dart';
import '../simulations/class9/circles_simulation_widget.dart';
import '../simulations/class9/constructions_simulation_widget.dart';
import '../simulations/class9/herons_formula_simulation_widget.dart';
import '../simulations/class9/surface_areas_volumes_simulation_widget.dart';
import '../simulations/class9/statistics_simulation_widget.dart';
import '../simulations/class9/probability_simulation_widget.dart';
import '../simulations/class10/real_numbers_simulation_widget.dart';
import '../simulations/class10/polynomials_simulation_widget.dart';
import '../simulations/class10/pair_linear_equations_simulation_widget.dart';
import '../simulations/class10/quadratic_equations_simulation_widget.dart';
import '../simulations/class10/arithmetic_progressions_simulation_widget.dart';
import '../simulations/class10/triangles_simulation_widget.dart';
import '../simulations/class10/coordinate_geometry_simulation_widget.dart';
import '../simulations/class10/trigonometry_simulation_widget.dart';
import '../simulations/class10/applications_trigonometry_simulation_widget.dart';
import '../simulations/class10/circles_simulation_widget.dart';
import '../simulations/class10/constructions_simulation_widget.dart';
import '../simulations/class10/areas_related_circles_simulation_widget.dart';
import '../simulations/class10/surface_areas_volumes_simulation_widget.dart';
import '../simulations/class10/statistics_simulation_widget.dart';
import '../simulations/class10/probability_simulation_widget.dart';
import '../widgets/fill_in_blank_quiz.dart';
import '../widgets/numerical_problem_set.dart';
import '../widgets/formula_section.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Maps each chapter to the interactive simulation widget(s) that best
/// teach its key topics.
final Map<String, List<Widget Function()>> _chapterSimulations = {
  'cls7_math_integers': [() => const IntegersSimulationWidget()],
  'cls7_math_fractionsdecimals': [() => const FractionsDecimalsSimulationWidget()],
  'cls7_math_datahandling': [() => const DataHandlingSimulationWidget()],
  'cls7_math_simpleequations': [() => const SimpleEquationsSimulationWidget()],
  'cls7_math_linesangles': [() => const LinesAnglesSimulationWidget()],
  'cls7_math_triangleproperties': [() => const TrianglePropertiesSimulationWidget()],
  'cls7_math_congruence': [() => const CongruenceSimulationWidget()],
  'cls7_math_comparingquantities': [() => const ComparingQuantitiesSimulationWidget()],
  'cls7_math_rationalnumbers': [() => const RationalNumbersSimulationWidget()],
  'cls7_math_practicalgeometry': [() => const PracticalGeometrySimulationWidget()],
  'cls7_math_perimeterarea': [() => const PerimeterAreaSimulationWidget()],
  'cls7_math_algebraicexpressions': [() => const AlgebraicExpressionsSimulationWidget()],
  'cls7_math_exponentspowers': [() => const ExponentsPowersSimulationWidget()],
  'cls7_math_symmetry': [() => const SymmetrySimulationWidget()],
  'cls7_math_solidshapes': [() => const SolidShapesSimulationWidget()],
  'cls8_math_rationalnumbers': [() => const Class8RationalNumbersSimulationWidget()],
  'cls8_math_linearequations': [() => const LinearEquationsSimulationWidget()],
  'cls8_math_quadrilaterals': [() => const QuadrilateralsSimulationWidget()],
  'cls8_math_practicalgeometry': [() => const Class8PracticalGeometrySimulationWidget()],
  'cls8_math_datahandling': [() => const Class8DataHandlingSimulationWidget()],
  'cls8_math_squaressquareroots': [() => const SquaresSquareRootsSimulationWidget()],
  'cls8_math_cubescuberoots': [() => const CubesCubeRootsSimulationWidget()],
  'cls8_math_comparingquantities': [() => const Class8ComparingQuantitiesSimulationWidget()],
  'cls8_math_algebraicidentities': [() => const AlgebraicIdentitiesSimulationWidget()],
  'cls8_math_solidshapes': [() => const Class8SolidShapesSimulationWidget()],
  'cls8_math_mensuration': [() => const MensurationSimulationWidget()],
  'cls8_math_exponentspowers': [() => const Class8ExponentsPowersSimulationWidget()],
  'cls8_math_proportions': [() => const ProportionsSimulationWidget()],
  'cls8_math_factorisation': [() => const FactorisationSimulationWidget()],
  'cls8_math_introductiongraphs': [() => const IntroductionGraphsSimulationWidget()],
  'cls8_math_playingnumbers': [() => const PlayingNumbersSimulationWidget()],
  'cls9_math_numbersystems': [() => const NumberSystemsSimulationWidget()],
  'cls9_math_polynomials': [() => const PolynomialsSimulationWidget()],
  'cls9_math_coordinategeometry': [() => const CoordinateGeometrySimulationWidget()],
  'cls9_math_linearequationstwovariables': [() => const LinearEquationsTwoVariablesSimulationWidget()],
  'cls9_math_euclidsgeometry': [() => const EuclidsGeometrySimulationWidget()],
  'cls9_math_linesangles': [() => const Class9LinesAnglesSimulationWidget()],
  'cls9_math_triangles': [() => const TrianglesSimulationWidget()],
  'cls9_math_quadrilaterals': [() => const Class9QuadrilateralsSimulationWidget()],
  'cls9_math_areasparallelogramstriangles': [() => const AreasParallelogramsTrianglesSimulationWidget()],
  'cls9_math_circles': [() => const CirclesSimulationWidget()],
  'cls9_math_constructions': [() => const ConstructionsSimulationWidget()],
  'cls9_math_heronsformula': [() => const HeronsFormulaSimulationWidget()],
  'cls9_math_surfaceareasvolumes': [() => const SurfaceAreasVolumesSimulationWidget()],
  'cls9_math_statistics': [() => const StatisticsSimulationWidget()],
  'cls9_math_probability': [() => const ProbabilitySimulationWidget()],
  'cls10_math_realnumbers': [() => const RealNumbersSimulationWidget()],
  'cls10_math_polynomials': [() => const Class10PolynomialsSimulationWidget()],
  'cls10_math_pairlinearequations': [() => const PairLinearEquationsSimulationWidget()],
  'cls10_math_quadraticequations': [() => const QuadraticEquationsSimulationWidget()],
  'cls10_math_arithmeticprogressions': [() => const ArithmeticProgressionsSimulationWidget()],
  'cls10_math_triangles': [() => const Class10TrianglesSimulationWidget()],
  'cls10_math_coordinategeometry': [() => const Class10CoordinateGeometrySimulationWidget()],
  'cls10_math_trigonometry': [() => const TrigonometrySimulationWidget()],
  'cls10_math_applicationstrigonometry': [() => const ApplicationsTrigonometrySimulationWidget()],
  'cls10_math_circles': [() => const Class10CirclesSimulationWidget()],
  'cls10_math_constructions': [() => const Class10ConstructionsSimulationWidget()],
  'cls10_math_areasrelatedcircles': [() => const AreasRelatedCirclesSimulationWidget()],
  'cls10_math_surfaceareasvolumes': [() => const Class10SurfaceAreasVolumesSimulationWidget()],
  'cls10_math_statistics': [() => const Class10StatisticsSimulationWidget()],
  'cls10_math_probability': [() => const Class10ProbabilitySimulationWidget()],
};

class ChapterDetailView extends StatelessWidget {
  final ChapterModel chapter;

  const ChapterDetailView({super.key, required this.chapter});

  @override
  Widget build(BuildContext context) {
    final simulations = _chapterSimulations[chapter.chapterId] ?? const [];

    return Scaffold(
      appBar: BrandAppBar(
        title: chapter.chapterName,
      ),
      body: ListView(
        padding: const EdgeInsets.all(16.0),
        children: [
          if (simulations.isNotEmpty) ...[
            Text(TrilingualService.instance.getUIText('Interactive Simulation'),
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            for (final build in simulations) ...[
              build(),
              const SizedBox(height: 16),
            ],
            const SizedBox(height: 8),
          ],
          Text(TrilingualService.instance.getUIText('Core Concepts'),
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          ...chapter.concepts.map((concept) => Padding(
                padding: const EdgeInsets.only(bottom: 6.0),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(TrilingualService.instance.getUIText('• ')),
                    Expanded(child: Text(concept)),
                  ],
                ),
              )),
          if (chapter.formulas.isNotEmpty) ...[
            const SizedBox(height: 24),
            Text(
              'Formulas & Derivations (${chapter.formulas.length})',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            FormulaSection(formulas: chapter.formulas),
          ],
          const SizedBox(height: 24),
          Text(
            'Practice Questions (${chapter.fillInTheBlanks.length})',
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          FillInBlankQuiz(questions: chapter.fillInTheBlanks),
          if (chapter.numericalProblems.isNotEmpty) ...[
            const SizedBox(height: 24),
            Text(
              'Numerical Problems (${chapter.numericalProblems.length})',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            NumericalProblemSet(problems: chapter.numericalProblems),
          ],
        ],
      ),
    );
  }
}
