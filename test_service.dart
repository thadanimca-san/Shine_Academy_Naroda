import 'package:flutter/widgets.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/core/services/universal_dictionary_service.dart';

void main() {
  testWidgets('Test dict init', (WidgetTester tester) async {
    WidgetsFlutterBinding.ensureInitialized();
    await UniversalDictionaryService.instance.init();
    print('Total terms: ${UniversalDictionaryService.instance.getAllTerms().length}');
    var foodTerm = UniversalDictionaryService.instance.getAllTerms().where((t) {
      final en = (t['term']?['english'] ?? '').toString().toLowerCase().trim();
      return en == 'food';
    }).toList();
    print('Food term: $foodTerm');
  });
}
