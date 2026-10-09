import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/features/learning/school/sci_simulation/services/pdf_generator_service.dart';
import 'package:shine_academy_naroda/features/learning/school/sci_simulation/data/sample_chapters.dart';
import 'package:flutter/material.dart';

void main() {
  testWidgets('Test PDF Generation', (WidgetTester tester) async {
    try {
      await PdfGeneratorService.generateAndOpenQuestionPaper(allClass9Chapters.take(1).toList());
      print("SUCCESS");
    } catch (e, stack) {
      print("ERROR: $e");
      print(stack);
    }
  });
}
