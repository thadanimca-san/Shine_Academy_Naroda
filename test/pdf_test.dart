import 'package:flutter_test/flutter_test.dart';
import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/services/pdf_export_service.dart';

void main() {
  testWidgets('PDF Export Test', (WidgetTester tester) async {
    final blocks = [
      {'type': 'theory', 'content': {'body_en': 'Test body', 'title_en': 'Test Title'}},
    ];
    
    try {
      await UniversalPdfEngine.generatePdfBytesFromWidgets(
        title: 'Test',
        widgets: [const Text('Hello')],
      );
      print("SUCCESS");
    } catch (e, stack) {
      print("ERROR: $e\\n$stack");
    }
  });
}
