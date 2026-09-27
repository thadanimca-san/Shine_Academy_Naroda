import 'dart:io';
import 'dart:convert';
import 'lib/features/learning/school/english/models/reading_passage.dart';
import 'lib/core/engine/local_content_manager.dart';
import 'package:flutter/widgets.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  
  // Emulate _tryLoadLocalOverride
  await LocalContentManager.instance.init();
  
  final jsonPath = 'app_core/english/reading/class5_reading_riverbank.json';
  final data = await LocalContentManager.instance.readLocalJson(jsonPath);
  
  print("DATA IS NULL? ${data == null}");
  if (data != null) {
    print("CONTAINS BODY? ${data.containsKey('body')}");
    final passage = ReadingPassage.fromJson(data);
    print("BODY HAS PRIYANSHI? ${passage.body.contains('Priyanshi')}");
    print("BODY HAS FARIDA? ${passage.body.contains('Farida')}");
  }
}
