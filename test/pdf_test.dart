import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:shine_academy_naroda/features/learning/learning_engine/services/pdf_export_service.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();
  
  test('PDF Generation Test', () async {
    final metadata = {
      'title': 'Test Chapter',
      'id': 'test_ch'
    };
    final blocks = [
      {'type': 'theory', 'body': 'Test theory block'}
    ];
    
    await PdfExportService.generateAndPrintChapter(metadata, blocks, studentName: 'Test Student');
  });
}
