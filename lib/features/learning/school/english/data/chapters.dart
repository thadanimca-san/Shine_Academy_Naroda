import '../models/chapter.dart';

import 'chapter_class3.dart';
import 'chapter_class3_kite.dart';
import 'chapter_class3_rainyday.dart';
import 'chapter_class3_lunchbox.dart';
import 'chapter_class3_strayanddog.dart';
import 'chapter_class3_grandpasgarden.dart';
import 'chapter_class3_bookfair.dart';
import 'chapter_class3_lostkitten.dart';
import 'chapter_class3_waterdrop.dart';
import 'chapter_class3_marketday.dart';

import 'chapter_class4.dart';
import 'chapter_class4_kite.dart';
import 'chapter_class4_elephant.dart';
import 'chapter_class4_recycle.dart';
import 'chapter_class4_kalpana.dart';
import 'chapter_class4_lunchbox.dart';
import 'chapter_class4_potter.dart';
import 'chapter_class4_drain.dart';
import 'chapter_class4_sciencefair.dart';
import 'chapter_class4_mela.dart';

import 'chapter_class5.dart';
import 'chapter_class5_astronomer.dart';
import 'chapter_class5_river.dart';
import 'chapter_class5_kite.dart';
import 'chapter_class5_bridge.dart';
import 'chapter_class5_mystery.dart';
import 'chapter_class5_race.dart';
import 'chapter_class5_invention.dart';
import 'chapter_class5_wellrepair.dart';
import 'chapter_class5_garba.dart';

import 'chapter_class6.dart';
import 'chapter_class6_scientist.dart';
import 'chapter_class6_drought.dart';
import 'chapter_class6_lighthouse.dart';
import 'chapter_class6_railway.dart';
import 'chapter_class6_reef.dart';
import 'chapter_class6_technology.dart';
import 'chapter_class6_sports.dart';
import 'chapter_class6_biography.dart';
import 'chapter_class6_conservation.dart';

import 'chapter_class7_waterfilter.dart';
import 'chapter_class7_cricket.dart';
import 'chapter_class7_chandrayaan.dart';
import 'chapter_class7_lostletter.dart';
import 'chapter_class7_treeplantation.dart';
import 'chapter_class7_freedomfighter.dart';
import 'chapter_class7_mystery.dart';
import 'chapter_class7_paralympian.dart';
import 'chapter_class7_internetsafety.dart';
import 'chapter_class7_folkmusic.dart';
import 'chapter_class7_scienceexpo.dart';

import 'chapter_class8_robotics.dart';
import 'chapter_class8_debate.dart';
import 'chapter_class8_farmerdaughter.dart';
import 'chapter_class8_himalayanrescue.dart';
import 'chapter_class8_streetplay.dart';
import 'chapter_class8_oldmap.dart';

import 'chapter_class9_watershed.dart';
import 'chapter_class9_courtroom.dart';
import 'chapter_class9_startup.dart';
import 'chapter_class9_archive.dart';
import 'chapter_class9_mountaineer.dart';
import 'chapter_class9_dialect.dart';

import 'chapter_class10_ai_ethics.dart';
import 'chapter_class10_wrongfulconviction.dart';
import 'chapter_class10_climaterefugees.dart';
import 'chapter_class10_entrepreneur.dart';
import 'chapter_class10_organdonation.dart';
import 'chapter_class10_ancientscript.dart';

const List<Chapter> class3Chapters = [
  chapterClass3,
  chapterClass3Kite,
  chapterClass3Rainyday,
  chapterClass3Lunchbox,
  chapterClass3Strayanddog,
  chapterClass3Grandpasgarden,
  chapterClass3Bookfair,
  chapterClass3Lostkitten,
  chapterClass3Waterdrop,
  chapterClass3Marketday,
];

const List<Chapter> class4Chapters = [
  chapterClass4,
  chapterClass4Kite,
  chapterClass4Elephant,
  chapterClass4Recycle,
  chapterClass4Kalpana,
  chapterClass4Lunchbox,
  chapterClass4Potter,
  chapterClass4Drain,
  chapterClass4Sciencefair,
  chapterClass4Mela,
];

const List<Chapter> class5Chapters = [
  chapterClass5,
  chapterClass5Astronomer,
  chapterClass5River,
  chapterClass5Kite,
  chapterClass5Bridge,
  chapterClass5Mystery,
  chapterClass5Race,
  chapterClass5Invention,
  chapterClass5WellRepair,
  chapterClass5Garba,
];

const List<Chapter> class6Chapters = [
  chapterClass6,
  chapterClass6Scientist,
  chapterClass6Drought,
  chapterClass6Lighthouse,
  chapterClass6Railway,
  chapterClass6Reef,
  chapterClass6Technology,
  chapterClass6Sports,
  chapterClass6Biography,
  chapterClass6Conservation,
];

const List<Chapter> class7Chapters = [
  chapterClass7WaterFilter,
  chapterClass7Cricket,
  chapterClass7Chandrayaan,
  chapterClass7LostLetter,
  chapterClass7TreePlantation,
  chapterClass7FreedomFighter,
  chapterClass7Mystery,
  chapterClass7Paralympian,
  chapterClass7InternetSafety,
  chapterClass7FolkMusic,
  chapterClass7ScienceExpo,
];

const List<Chapter> class8Chapters = [
  chapterClass8Robotics,
  chapterClass8Debate,
  chapterClass8FarmerDaughter,
  chapterClass8HimalayanRescue,
  chapterClass8StreetPlay,
  chapterClass8OldMap,
];

const List<Chapter> class9Chapters = [
  chapterClass9Watershed,
  chapterClass9Courtroom,
  chapterClass9Startup,
  chapterClass9Archive,
  chapterClass9Mountaineer,
  chapterClass9Dialect,
];

const List<Chapter> class10Chapters = [
  chapterClass10AiEthics,
  chapterClass10WrongfulConviction,
  chapterClass10ClimateRefugees,
  chapterClass10Entrepreneur,
  chapterClass10OrganDonation,
  chapterClass10AncientScript,
];

const Map<String, List<Chapter>> chaptersByGrade = {
  'Class 3': class3Chapters,
  'Class 4': class4Chapters,
  'Class 5': class5Chapters,
  'Class 6': class6Chapters,
  'Class 7': class7Chapters,
  'Class 8': class8Chapters,
  'Class 9': class9Chapters,
  'Class 10': class10Chapters,
};

const List<Chapter> allChapters = [
  ...class3Chapters,
  ...class4Chapters,
  ...class5Chapters,
  ...class6Chapters,
  ...class7Chapters,
  ...class8Chapters,
  ...class9Chapters,
  ...class10Chapters,
];
