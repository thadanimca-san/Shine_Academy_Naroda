import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:screenshot/screenshot.dart';

void main() {
  testWidgets('Test captureFromWidget', (WidgetTester tester) async {
    final controller = ScreenshotController();
    try {
      final bytes = await controller.captureFromWidget(
        MaterialApp(home: Scaffold(body: Text("Hello World"))),
        delay: Duration(milliseconds: 100),
      ).timeout(Duration(seconds: 2));
      print("Captured \${bytes.length} bytes");
    } catch (e) {
      print("Error: $e");
    }
  });
}
