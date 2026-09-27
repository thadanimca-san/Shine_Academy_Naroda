import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/paper_pdf_service.dart';
import 'package:commerce_accounts_11to12/services/problem_generator.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  test('question paper PDF renders with the DejaVu Sans (Rupee-capable) font without throwing', () async {
    final problems = [
      ProblemGenerator.generateJournalLedgerTrialBalance(board: Board.gseb, schoolClass: 11, difficulty: 2),
    ];
    final doc = await PaperPdfService.buildQuestionPaper(
      problems: problems,
      board: Board.gseb,
      schoolClass: 11,
      paperTitle: 'Font Test',
    );
    final bytes = await doc.save();
    expect(bytes.isNotEmpty, isTrue);
  });

  test('DejaVuSans.ttf asset loads and is a valid non-empty font file', () async {
    final data = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
    expect(data.lengthInBytes, greaterThan(100000));
  });
}
