import 'package:flutter_test/flutter_test.dart';
import 'package:shared_preferences/shared_preferences.dart';

import 'package:commerce_accounts_11to12/main.dart';

void main() {
  setUp(() {
    SharedPreferences.setMockInitialValues({});
  });

  testWidgets('App launches to activation or home screen', (WidgetTester tester) async {
    await tester.pumpWidget(const CommerceAccountsApp());
    await tester.pumpAndSettle();

    // Unactivated by default in a fresh test environment, so the
    // activation screen (asking for the device unlock code) should show.
    expect(find.text('Activate App'), findsOneWidget);
  });
}
