import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/core/engine/dictionary_engine.dart';
import 'package:shine_academy_naroda/core/engine/local_content_manager.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await LocalContentManager.instance.init();
  await DictionaryEngine.instance.init();
  print("DONE TESTING INIT. dictionary length: ${DictionaryEngine.instance.index.length}");
}
