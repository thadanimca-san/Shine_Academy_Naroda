import 'dart:io';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
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
    // For Phase 2 Beta Testing, we can set this to false to allow debugging/screenshots.
    // For Phase 3 Public Launch, set enableProtection to true.
    await SecurityService.instance.init(enableProtection: false);
  }
  
  registerDefaultBlocks();
  runApp(const ShineAcademyApp());
}