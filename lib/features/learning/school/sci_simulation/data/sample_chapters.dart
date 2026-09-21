import '../models/chapter_model.dart';
import 'chapters/motion_chapter.dart';
import 'chapters/force_chapter.dart';
import 'chapters/gravitation_chapter.dart';
import 'chapters/work_energy_chapter.dart';
import 'chapters/sound_chapter.dart';
import 'chapters/matter_chapter.dart';
import 'chapters/pure_matter_chapter.dart';
import 'chapters/atoms_chapter.dart';
import 'chapters/atomic_structure_chapter.dart';
import 'chapters/cell_chapter.dart';
import 'chapters/tissues_chapter.dart';
import 'chapters/reproduction_chapter.dart';
import 'chapters/classification_chapter.dart';
import 'chapters/earth_system_chapter.dart';
import 'chapters/food_resources_chapter.dart';
import 'chapters/class8/invisible_world_chapter.dart';
import 'chapters/class8/health_chapter.dart';
import 'chapters/class8/electricity_magnetic_heating_chapter.dart';
import 'chapters/class8/exploring_forces_chapter.dart';
import 'chapters/class8/pressure_winds_cyclones_chapter.dart';
import 'chapters/class8/particulate_matter_chapter.dart';
import 'chapters/class8/nature_of_matter_chapter.dart';
import 'chapters/class8/solutions_density_chapter.dart';
import 'chapters/class8/light_mirrors_lenses_chapter.dart';
import 'chapters/class8/keeping_time_skies_chapter.dart';
import 'chapters/class8/nature_harmony_chapter.dart';
import 'chapters/class8/earth_unique_planet_chapter.dart';
import 'chapters/class8/crop_production_chapter.dart';
import 'chapters/class8/microorganisms_chapter.dart';
import 'chapters/class8/synthetic_fibres_chapter.dart';
import 'chapters/class8/materials_metals_chapter.dart';
import 'chapters/class8/coal_petroleum_chapter.dart';
import 'chapters/class8/combustion_flame_chapter.dart';
import 'chapters/class8/conservation_chapter.dart';
import 'chapters/class8/cell_structure_chapter.dart';
import 'chapters/class8/reproduction_animals_chapter.dart';
import 'chapters/class8/adolescence_chapter.dart';
import 'chapters/class8/force_pressure_chapter.dart';
import 'chapters/class8/friction_chapter.dart';
import 'chapters/class8/sound_chapter8.dart';
import 'chapters/class8/chemical_effects_current_chapter.dart';
import 'chapters/class8/natural_phenomena_chapter.dart';
import 'chapters/class8/light_chapter8.dart';
import 'chapters/class8/stars_solar_system_chapter.dart';
import 'chapters/class8/pollution_chapter.dart';
import 'chapters/class7/nutrition_plants_chapter.dart';
import 'chapters/class7/nutrition_animals_chapter.dart';
import 'chapters/class7/fibre_fabric_chapter.dart';
import 'chapters/class7/heat_chapter.dart';
import 'chapters/class7/acids_bases_salts_chapter.dart';
import 'chapters/class7/physical_chemical_changes_chapter.dart';
import 'chapters/class7/weather_climate_chapter.dart';
import 'chapters/class7/winds_storms_cyclones_chapter.dart';
import 'chapters/class7/soil_chapter.dart';
import 'chapters/class7/respiration_chapter.dart';
import 'chapters/class7/transportation_chapter.dart';
import 'chapters/class7/reproduction_plants_chapter.dart';
import 'chapters/class7/motion_time_chapter.dart';
import 'chapters/class7/electric_current_effects_chapter.dart';
import 'chapters/class7/light_chapter7.dart';
import 'chapters/class7/water_resource_chapter.dart';
import 'chapters/class7/forests_lifeline_chapter.dart';
import 'chapters/class7/wastewater_chapter.dart';
import 'chapters/class10/chemical_reactions_chapter.dart';
import 'chapters/class10/acids_bases_salts_chapter.dart';
import 'chapters/class10/metals_nonmetals_chapter.dart';
import 'chapters/class10/carbon_compounds_chapter.dart';
import 'chapters/class10/periodic_classification_chapter.dart';
import 'chapters/class10/life_processes_chapter.dart';
import 'chapters/class10/control_coordination_chapter.dart';
import 'chapters/class10/reproduction_chapter.dart';
import 'chapters/class10/heredity_evolution_chapter.dart';
import 'chapters/class10/our_environment_chapter.dart';
import 'chapters/class10/sustainable_management_chapter.dart';
import 'chapters/class10/light_reflection_refraction_chapter.dart';
import 'chapters/class10/human_eye_chapter.dart';
import 'chapters/class10/electricity_chapter.dart';
import 'chapters/class10/magnetic_effects_chapter.dart';
import 'chapters/class10/sources_energy_chapter.dart';

final List<ChapterModel> allClass9Chapters = [
  class9CellChapter, // Ch 2: Cell: The Building Block of Life
  class9TissuesChapter, // Ch 3: Tissues in Action
  class9MotionChapter, // Ch 4: Describing Motion Around Us
  class9PureMatterChapter, // Ch 5: Exploring Mixtures and their Separation
  class9ForceChapter, // Ch 6: How Forces Affect Motion
  class9WorkEnergyChapter, // Ch 7: Work, Energy, and Simple Machines
  class9AtomicStructureChapter, // Ch 8: Journey Inside the Atom
  class9AtomsChapter, // Ch 9: Atomic Foundations of Matter
  class9SoundChapter, // Ch 10: Sound Waves: Characteristics and Applications
  class9ReproductionChapter, // Ch 11: Reproduction: How Life Continues
  class9ClassificationChapter, // Ch 12: Patterns in Life: Diversity and Classification
  class9EarthSystemChapter, // Ch 13: Earth as a System: Energy, Matter, and Life
  // Bonus chapters (not part of the current 13-chapter syllabus, kept for reference):
  class9GravitationChapter,
  class9MatterChapter,
  class9FoodResourcesChapter,
];

final List<ChapterModel> allClass8Chapters = [
  class8InvisibleWorldChapter, // Ch 2: The Invisible Living World: Beyond Our Naked Eye
  class8HealthChapter, // Ch 3: Health: The Ultimate Treasure
  class8ElectricityMagneticHeatingChapter, // Ch 4: Electricity: Magnetic and Heating Effects
  class8ExploringForcesChapter, // Ch 5: Exploring Forces
  class8PressureWindsCyclonesChapter, // Ch 6: Pressure, Winds, Storms, and Cyclones
  class8ParticulateMatterChapter, // Ch 7: Particulate Nature of Matter
  class8NatureOfMatterChapter, // Ch 8: Nature of Matter: Elements, Compounds, and Mixtures
  class8SolutionsDensityChapter, // Ch 9: The Amazing World of Solutes, Solvents, and Solutions
  class8LightMirrorsLensesChapter, // Ch 10: Light: Mirrors and Lenses
  class8KeepingTimeSkiesChapter, // Ch 11: Keeping Time with the Skies
  class8NatureHarmonyChapter, // Ch 12: How Nature Works in Harmony
  class8EarthUniquePlanetChapter, // Ch 13: Our Home: Earth, a Unique Life Sustaining Planet
  // Bonus chapters (not part of the current 13-chapter syllabus, kept for reference):
  class8CropProductionChapter,
  class8MicroorganismsChapter,
  class8SyntheticFibresChapter,
  class8MaterialsMetalsChapter,
  class8CoalPetroleumChapter,
  class8CombustionFlameChapter,
  class8ConservationChapter,
  class8CellStructureChapter,
  class8ReproductionAnimalsChapter,
  class8AdolescenceChapter,
  class8ForcePressureChapter,
  class8FrictionChapter,
  class8SoundChapter,
  class8ChemicalEffectsChapter,
  class8NaturalPhenomenaChapter,
  class8LightChapter,
  class8StarsSolarSystemChapter,
  class8PollutionChapter,
];

final List<ChapterModel> allClass7Chapters = [
  class7NutritionPlantsChapter,
  class7NutritionAnimalsChapter,
  class7FibreFabricChapter,
  class7HeatChapter,
  class7AcidsBasesSaltsChapter,
  class7PhysicalChemicalChangesChapter,
  class7WeatherClimateChapter,
  class7WindsStormsCyclonesChapter,
  class7SoilChapter,
  class7RespirationChapter,
  class7TransportationChapter,
  class7ReproductionPlantsChapter,
  class7MotionTimeChapter,
  class7ElectricCurrentEffectsChapter,
  class7LightChapter,
  class7WaterResourceChapter,
  class7ForestsLifelineChapter,
  class7WastewaterChapter,
];

final List<ChapterModel> allClass10Chapters = [
  class10ChemicalReactionsChapter,
  class10AcidsBasesSaltsChapter,
  class10MetalsNonmetalsChapter,
  class10CarbonCompoundsChapter,
  class10PeriodicClassificationChapter,
  class10LifeProcessesChapter,
  class10ControlCoordinationChapter,
  class10ReproductionChapter,
  class10HeredityEvolutionChapter,
  class10OurEnvironmentChapter,
  class10SustainableManagementChapter,
  class10LightReflectionRefractionChapter,
  class10HumanEyeChapter,
  class10ElectricityChapter,
  class10MagneticEffectsChapter,
  class10SourcesEnergyChapter,
];
