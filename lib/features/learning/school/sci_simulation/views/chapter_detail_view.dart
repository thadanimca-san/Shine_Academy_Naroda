import 'package:flutter/material.dart';
import '../models/chapter_model.dart';
import '../services/pdf_generator_service.dart';
import '../simulations/motion_simulation_widget.dart';
import '../simulations/force_simulation_widget.dart';
import '../simulations/gravitation_simulation_widget.dart';
import '../simulations/work_energy_simulation_widget.dart';
import '../simulations/sound_simulation_widget.dart';
import '../simulations/states_of_matter_simulation_widget.dart';
import '../simulations/solution_simulation_widget.dart';
import '../simulations/chemistry_3d_simulation_widget.dart';
import '../simulations/atomic_structure_simulation_widget.dart';
import '../simulations/cell_simulation_widget.dart';
import '../simulations/osmosis_simulation_widget.dart';
import '../simulations/tissues_simulation_widget.dart';
import '../simulations/joints_simulation_widget.dart';
import '../simulations/pollination_simulation_widget.dart';
import '../simulations/human_reproductive_system_widget.dart';
import '../simulations/classification_tree_widget.dart';
import '../simulations/albedo_simulation_widget.dart';
import '../simulations/biogeochemical_cycle_widget.dart';
import '../simulations/food_resources_simulation_widget.dart';
import '../simulations/class8/microbe_explorer_simulation_widget.dart';
import '../simulations/class8/electromagnet_simulation_widget.dart';
import '../simulations/class8/mirror_lens_simulation_widget.dart';
import '../simulations/class8/food_web_simulation_widget.dart';
import '../simulations/class8/crop_production_simulation_widget.dart';
import '../simulations/class8/microorganisms_simulation_widget.dart';
import '../simulations/class8/synthetic_fibres_simulation_widget.dart';
import '../simulations/class8/materials_metals_simulation_widget.dart';
import '../simulations/class8/coal_petroleum_simulation_widget.dart';
import '../simulations/class8/combustion_flame_simulation_widget.dart';
import '../simulations/class8/conservation_simulation_widget.dart';
import '../simulations/class8/cell_structure_simulation_widget.dart';
import '../simulations/class8/reproduction_animals_simulation_widget.dart';
import '../simulations/class8/adolescence_simulation_widget.dart';
import '../simulations/class8/force_pressure_simulation_widget.dart';
import '../simulations/class8/friction_simulation_widget.dart';
import '../simulations/class8/sound_simulation_widget8.dart';
import '../simulations/class8/chemical_effects_simulation_widget.dart';
import '../simulations/class8/natural_phenomena_simulation_widget.dart';
import '../simulations/class8/light_simulation_widget.dart';
import '../simulations/class8/stars_solar_system_simulation_widget.dart';
import '../simulations/class8/pollution_simulation_widget.dart';
import '../simulations/class7/nutrition_plants_simulation_widget.dart';
import '../simulations/class7/nutrition_animals_simulation_widget.dart';
import '../simulations/class7/fibre_fabric_simulation_widget.dart';
import '../simulations/class7/heat_simulation_widget.dart';
import '../simulations/class7/acids_bases_salts_simulation_widget.dart';
import '../simulations/class7/physical_chemical_changes_simulation_widget.dart';
import '../simulations/class7/weather_climate_simulation_widget.dart';
import '../simulations/class7/winds_storms_cyclones_simulation_widget.dart';
import '../simulations/class7/soil_simulation_widget.dart';
import '../simulations/class7/respiration_simulation_widget.dart';
import '../simulations/class7/transportation_simulation_widget.dart';
import '../simulations/class7/reproduction_plants_simulation_widget.dart';
import '../simulations/class7/motion_time_simulation_widget.dart';
import '../simulations/class7/electric_current_effects_simulation_widget.dart';
import '../simulations/class7/light_simulation_widget7.dart';
import '../simulations/class7/water_resource_simulation_widget.dart';
import '../simulations/class7/forests_lifeline_simulation_widget.dart';
import '../simulations/class7/wastewater_simulation_widget.dart';
import '../simulations/class10/chemical_reactions_simulation_widget.dart';
import '../simulations/class10/acids_bases_salts_simulation_widget.dart';
import '../simulations/class10/metals_nonmetals_simulation_widget.dart';
import '../simulations/class10/carbon_compounds_simulation_widget.dart';
import '../simulations/class10/periodic_classification_simulation_widget.dart';
import '../simulations/class10/life_processes_simulation_widget.dart';
import '../simulations/class10/control_coordination_simulation_widget.dart';
import '../simulations/class10/reproduction_simulation_widget.dart';
import '../simulations/class10/heredity_evolution_simulation_widget.dart';
import '../simulations/class10/our_environment_simulation_widget.dart';
import '../simulations/class10/sustainable_management_simulation_widget.dart';
import '../simulations/class10/light_reflection_refraction_simulation_widget.dart';
import '../simulations/class10/human_eye_simulation_widget.dart';
import '../simulations/class10/electricity_simulation_widget.dart';
import '../simulations/class10/magnetic_effects_simulation_widget.dart';
import '../simulations/class10/sources_energy_simulation_widget.dart';
import '../widgets/fill_in_blank_quiz.dart';
import '../widgets/numerical_problem_set.dart';
import '../widgets/formula_section.dart';
import '../widgets/revision_notes_section.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

/// Maps each chapter to the interactive simulation widget(s) that best
/// teach its key topics. A chapter can carry more than one simulation
/// when it covers multiple distinct concepts (e.g. Gravitation covers
/// both free fall and buoyancy as separate widgets... though here that's
/// handled inside a single tabbed widget instead).
final Map<String, List<Widget Function()>> _chapterSimulations = {
  'cls9_phys_motion': [() => const MotionSimulationWidget()],
  'cls9_phys_force': [() => const ForceSimulationWidget()],
  'cls9_phys_gravitation': [() => const GravitationSimulationWidget()],
  'cls9_phys_workenergy': [() => const WorkEnergySimulationWidget()],
  'cls9_phys_sound': [() => const SoundSimulationWidget()],
  'cls9_chem_matter': [() => const StatesOfMatterSimulationWidget()],
  'cls9_chem_puresubstances': [() => const SolutionSimulationWidget()],
  'cls9_chem_atoms': [() => const Chemistry3DSimulationWidget()],
  'cls9_chem_atomicstructure': [() => const AtomicStructureSimulationWidget()],
  'cls9_bio_cell': [() => const CellSimulationWidget(), () => const OsmosisSimulationWidget()],
  'cls9_bio_tissues': [() => const TissuesSimulationWidget(), () => const JointsSimulationWidget()],
  'cls9_bio_reproduction': [() => const PollinationSimulationWidget(), () => const HumanReproductiveSystemWidget()],
  'cls9_bio_classification': [() => const ClassificationTreeWidget()],
  'cls9_earth_system': [() => const AlbedoSimulationWidget(), () => const BiogeochemicalCycleWidget()],
  'cls9_bio_foodresources': [() => const FoodResourcesSimulationWidget()],
  'cls8_bio_invisibleworld': [() => const MicrobeExplorerSimulationWidget()],
  'cls8_phys_electricitymagneticheating': [() => const ElectromagnetSimulationWidget()],
  'cls8_chem_particulatematter': [() => const StatesOfMatterSimulationWidget()],
  'cls8_chem_solutionsdensity': [() => const SolutionSimulationWidget()],
  'cls8_phys_lightmirrorslenses': [() => const MirrorLensSimulationWidget()],
  'cls8_bio_natureharmony': [() => const FoodWebSimulationWidget()],
  'cls8_bio_cropproduction': [() => const CropProductionSimulationWidget()],
  'cls8_bio_microorganisms': [() => const MicroorganismsSimulationWidget()],
  'cls8_chem_syntheticfibres': [() => const SyntheticFibresSimulationWidget()],
  'cls8_chem_materialsmetals': [() => const MaterialsMetalsSimulationWidget()],
  'cls8_chem_coalpetroleum': [() => const CoalPetroleumSimulationWidget()],
  'cls8_chem_combustionflame': [() => const CombustionFlameSimulationWidget()],
  'cls8_bio_conservation': [() => const ConservationSimulationWidget()],
  'cls8_bio_cellstructure': [() => const Class8CellStructureSimulationWidget()],
  'cls8_bio_reproductionanimals': [() => const ReproductionAnimalsSimulationWidget()],
  'cls8_bio_adolescence': [() => const AdolescenceSimulationWidget()],
  'cls8_phys_forcepressure': [() => const ForcePressureSimulationWidget()],
  'cls8_phys_friction': [() => const FrictionSimulationWidget()],
  'cls8_phys_sound': [() => const Class8SoundSimulationWidget()],
  'cls8_chem_electriccurrent': [() => const ChemicalEffectsSimulationWidget()],
  'cls8_phys_naturalphenomena': [() => const NaturalPhenomenaSimulationWidget()],
  'cls8_phys_light': [() => const LightSimulationWidget()],
  'cls8_phys_starssolarsystem': [() => const StarsSolarSystemSimulationWidget()],
  'cls8_chem_pollution': [() => const PollutionSimulationWidget()],
  'cls7_bio_nutritionplants': [() => const NutritionPlantsSimulationWidget()],
  'cls7_bio_nutritionanimals': [() => const NutritionAnimalsSimulationWidget()],
  'cls7_chem_fibrefabric': [() => const FibreFabricSimulationWidget()],
  'cls7_phys_heat': [() => const HeatSimulationWidget()],
  'cls7_chem_acidsbasessalts': [() => const AcidsBasesSaltsSimulationWidget()],
  'cls7_chem_physicalchemicalchanges': [() => const PhysicalChemicalChangesSimulationWidget()],
  'cls7_phys_weatherclimate': [() => const WeatherClimateSimulationWidget()],
  'cls7_phys_windsstormscyclones': [() => const WindsStormsCyclonesSimulationWidget()],
  'cls7_bio_soil': [() => const SoilSimulationWidget()],
  'cls7_bio_respiration': [() => const RespirationSimulationWidget()],
  'cls7_bio_transportation': [() => const TransportationSimulationWidget()],
  'cls7_bio_reproductionplants': [() => const ReproductionPlantsSimulationWidget()],
  'cls7_phys_motiontime': [() => const MotionTimeSimulationWidget()],
  'cls7_phys_electriccurrenteffects': [() => const ElectricCurrentEffectsSimulationWidget()],
  'cls7_phys_light': [() => const Class7LightSimulationWidget()],
  'cls7_chem_waterresource': [() => const WaterResourceSimulationWidget()],
  'cls7_bio_forestslifeline': [() => const ForestsLifelineSimulationWidget()],
  'cls7_chem_wastewater': [() => const WastewaterSimulationWidget()],
  'cls10_chem_chemicalreactions': [() => const ChemicalReactionsSimulationWidget()],
  'cls10_chem_acidsbasessalts': [() => const Class10AcidsBasesSaltsSimulationWidget()],
  'cls10_chem_metalsnonmetals': [() => const MetalsNonmetalsSimulationWidget()],
  'cls10_chem_carboncompounds': [() => const CarbonCompoundsSimulationWidget()],
  'cls10_chem_periodicclassification': [() => const PeriodicClassificationSimulationWidget()],
  'cls10_bio_lifeprocesses': [() => const LifeProcessesSimulationWidget()],
  'cls10_bio_controlcoordination': [() => const ControlCoordinationSimulationWidget()],
  'cls10_bio_reproduction': [() => const ReproductionSimulationWidget()],
  'cls10_bio_heredityevolution': [() => const HeredityEvolutionSimulationWidget()],
  'cls10_bio_ourenvironment': [() => const OurEnvironmentSimulationWidget()],
  'cls10_bio_sustainablemanagement': [() => const SustainableManagementSimulationWidget()],
  'cls10_phys_lightreflectionrefraction': [() => const LightReflectionRefractionSimulationWidget()],
  'cls10_phys_humaneye': [() => const HumanEyeSimulationWidget()],
  'cls10_phys_electricity': [() => const ElectricitySimulationWidget()],
  'cls10_phys_magneticeffects': [() => const MagneticEffectsSimulationWidget()],
  'cls10_phys_sourcesenergy': [() => const SourcesEnergySimulationWidget()],
};

class ChapterDetailView extends StatefulWidget {
  final ChapterModel chapter;

  const ChapterDetailView({super.key, required this.chapter});

  @override
  State<ChapterDetailView> createState() => _ChapterDetailViewState();
}

class _ChapterDetailViewState extends State<ChapterDetailView> {
  bool _generatingPdf = false;

  Future<void> _generate(Future<void> Function(ChapterModel) generator) async {
    setState(() => _generatingPdf = true);
    try {
      await generator(widget.chapter);
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Could not generate PDF: $e')),
        );
      }
    } finally {
      if (mounted) setState(() => _generatingPdf = false);
    }
  }

  @override
  Widget build(BuildContext context) {
    final chapter = widget.chapter;
    final simulations = _chapterSimulations[chapter.chapterId] ?? const [];

    return Scaffold(
      appBar: BrandAppBar(
        title: chapter.chapterName,
      ),
      body: SingleChildScrollView(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            if (chapter.imagePath != null) ...[
              ClipRRect(
                borderRadius: BorderRadius.circular(16),
                child: Image.asset(
                  chapter.imagePath!,
                  width: double.infinity,
                  fit: BoxFit.contain,
                  errorBuilder: (context, error, stackTrace) => const SizedBox.shrink(),
                ),
              ),
              const SizedBox(height: 16),
            ],
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
            if (chapter.revisionNotes.isNotEmpty) ...[
              Text(TrilingualService.instance.getUIText('Short Notes — Quick Revision'),
                style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
              ),
              Padding(
                padding: EdgeInsets.only(top: 2, bottom: 10),
                child: Text(TrilingualService.instance.getUIText('One card per sub-topic — read these the night before an exam.'),
                  style: TextStyle(fontSize: 12.5, color: Theme.of(context).colorScheme.onSurfaceVariant),
                ),
              ),
              RevisionNotesSection(notes: chapter.revisionNotes),
              const SizedBox(height: 20),
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
          if (chapter.fillInTheBlanks.isNotEmpty) ...[
            const SizedBox(height: 8),
            Row(
              children: [
                Expanded(
                  child: ElevatedButton.icon(
                    onPressed: _generatingPdf
                        ? null
                        : () => _generate(PdfGeneratorService.generateQuestionPaperPDF),
                    icon: Icon(Icons.picture_as_pdf),
                    label: Text(TrilingualService.instance.getUIText('Download Question Paper')),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.blue[800],
                      foregroundColor: Colors.white,
                    ),
                  ),
                ),
                const SizedBox(width: 12),
                Expanded(
                  child: ElevatedButton.icon(
                    onPressed: _generatingPdf
                        ? null
                        : () => _generate(PdfGeneratorService.generateAnswerKeyPDF),
                    icon: Icon(Icons.task_alt),
                    label: Text(TrilingualService.instance.getUIText('Download Answer Key')),
                    style: ElevatedButton.styleFrom(
                      backgroundColor: Colors.green[700],
                      foregroundColor: Colors.white,
                    ),
                  ),
                ),
              ],
            ),
            if (_generatingPdf) ...[
              const SizedBox(height: 8),
              const LinearProgressIndicator(),
            ],
          ],
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
      ),
    );
  }
}
