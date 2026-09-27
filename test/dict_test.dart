import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/services.dart';
import 'package:shine_academy_naroda/core/engine/dictionary_engine.dart';
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  test('Load massive dict', () async {
    await DictionaryEngine.instance.init();
    print("Dictionary terms: ${DictionaryEngine.instance.index.length}");
  });
}
