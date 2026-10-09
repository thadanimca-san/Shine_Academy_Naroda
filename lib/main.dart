import 'dart:io';
import 'package:flutter/foundation.dart' show kReleaseMode;
import 'package:flutter/material.dart';
import 'core/app.dart';
import 'core/services/activation_service.dart';
import 'core/engine/local_content_manager.dart';
import 'core/engine/dictionary_engine.dart';
import 'core/services/universal_dictionary_service.dart';
import 'core/services/trilingual_service.dart';
import 'core/engine/curriculum_database.dart';
import 'core/engine/default_blocks.dart';
import 'core/services/gamification_service.dart';
import 'core/services/analytics_service.dart';
import 'core/services/security_service.dart';
import 'core/engine/knowledge_graph_service.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await LocalContentManager.instance.init();
  await ActivationService.initialize();
  await GamificationService.instance.init();
  await AnalyticsService.instance.init();
  await DictionaryEngine.instance.init();
  await UniversalDictionaryService.instance.init();
  await TrilingualService.instance.init();
  await CurriculumDatabase.instance.load();
  await KnowledgeGraphService.instance.buildGraph();
  
  if (Platform.isAndroid || Platform.isIOS) {
    // Screenshots and screen recording are blocked in every build students
    // install (release). Debug builds stay open so developers can capture
    // screens while testing.
    await SecurityService.instance.init(enableProtection: kReleaseMode);
  }
  
  registerDefaultBlocks();
  runApp(const ShineAcademyApp());
}