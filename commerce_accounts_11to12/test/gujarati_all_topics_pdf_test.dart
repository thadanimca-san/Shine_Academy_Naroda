import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/medium_model.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/brs_generator.dart';
import 'package:commerce_accounts_11to12/services/cash_book_generator.dart';
import 'package:commerce_accounts_11to12/services/cash_flow_generator.dart';
import 'package:commerce_accounts_11to12/services/company_accounts_generator.dart';
import 'package:commerce_accounts_11to12/services/depreciation_generator.dart';
import 'package:commerce_accounts_11to12/services/dissolution_generator.dart';
import 'package:commerce_accounts_11to12/services/final_accounts_generator.dart';
import 'package:commerce_accounts_11to12/services/partnership_generator.dart';
import 'package:commerce_accounts_11to12/services/paper_pdf_service.dart';
import 'package:commerce_accounts_11to12/services/rectification_generator.dart';

/// Every PDF builder, run once in Gujarati medium, at high difficulty so
/// every branch (forfeiture/reissue, further bad debts, accrued/advance
/// income, etc.) is exercised. This is the regression guard for the
/// italic-font bug found during development: Noto Sans Gujarati has no
/// italic glyphs, so any pw.FontStyle.italic text anywhere in these
/// documents silently fell back to a Unicode-blind built-in font and
/// dropped both Gujarati and English characters. flutter_test surfaces
/// that as a "Unable to find a font to draw ..." console warning during
/// PdfPreview/print — this test doesn't capture stdout, but combined with
/// a manual check of test output it is the fastest way to catch a
/// reintroduced case across all eleven topics at once.
void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  const board = Board.gseb;
  const schoolClass = 12;
  const difficulty = 5;
  const medium = Medium.gujarati;

  Future<void> expectNonEmpty(Future<dynamic> Function() build) async {
    final doc = await build();
    final bytes = await doc.save();
    expect(bytes.isNotEmpty, isTrue);
  }

  test('Cash Book question paper + answer key render in Gujarati', () async {
    final problems = [CashBookGenerator.generate(board: board, schoolClass: schoolClass, difficulty: difficulty)];
    await expectNonEmpty(() => PaperPdfService.buildCashBookQuestionPaper(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
    await expectNonEmpty(() => PaperPdfService.buildCashBookAnswerKey(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
  });

  test('Depreciation question paper + answer key render in Gujarati', () async {
    final problems = [DepreciationGenerator.generate(board: board, schoolClass: schoolClass, difficulty: difficulty)];
    await expectNonEmpty(() => PaperPdfService.buildDepreciationQuestionPaper(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
    await expectNonEmpty(() => PaperPdfService.buildDepreciationAnswerKey(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
  });

  test('Rectification question paper + answer key render in Gujarati', () async {
    final problems = [RectificationGenerator.generate(board: board, schoolClass: schoolClass, difficulty: difficulty)];
    await expectNonEmpty(() => PaperPdfService.buildRectificationQuestionPaper(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
    await expectNonEmpty(() => PaperPdfService.buildRectificationAnswerKey(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
  });

  test('BRS question paper + answer key render in Gujarati', () async {
    final problems = [BrsGenerator.generate(board: board, schoolClass: schoolClass, difficulty: difficulty)];
    await expectNonEmpty(() => PaperPdfService.buildBrsQuestionPaper(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
    await expectNonEmpty(() => PaperPdfService.buildBrsAnswerKey(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
  });

  test('Final Accounts question paper + answer key render in Gujarati (Class 12, max difficulty adjustments)', () async {
    final problems = [FinalAccountsGenerator.generate(board: board, schoolClass: schoolClass, difficulty: difficulty)];
    await expectNonEmpty(() => PaperPdfService.buildFinalAccountsQuestionPaper(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
    await expectNonEmpty(() => PaperPdfService.buildFinalAccountsAnswerKey(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
  });

  test('Partnership Admission question paper + answer key render in Gujarati', () async {
    final problems = [PartnershipGenerator.generateAdmission(board: board, schoolClass: schoolClass, difficulty: difficulty)];
    await expectNonEmpty(() => PaperPdfService.buildPartnershipAdmissionQuestionPaper(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
    await expectNonEmpty(() => PaperPdfService.buildPartnershipAdmissionAnswerKey(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
  });

  test('Partnership Departure question paper + answer key render in Gujarati', () async {
    final problems = [PartnershipGenerator.generateDeparture(board: board, schoolClass: schoolClass, difficulty: difficulty)];
    await expectNonEmpty(() => PaperPdfService.buildPartnershipDepartureQuestionPaper(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
    await expectNonEmpty(() => PaperPdfService.buildPartnershipDepartureAnswerKey(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
  });

  test('Dissolution question paper + answer key render in Gujarati', () async {
    final problems = [DissolutionGenerator.generate(board: board, schoolClass: schoolClass, difficulty: difficulty)];
    await expectNonEmpty(() => PaperPdfService.buildDissolutionQuestionPaper(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
    await expectNonEmpty(() => PaperPdfService.buildDissolutionAnswerKey(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
  });

  test('Share Issue question paper + answer key render in Gujarati (forfeiture + reissue branch)', () async {
    final problems = [CompanyAccountsGenerator.generate(board: board, schoolClass: schoolClass, difficulty: difficulty)];
    await expectNonEmpty(() => PaperPdfService.buildShareIssueQuestionPaper(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
    await expectNonEmpty(() => PaperPdfService.buildShareIssueAnswerKey(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
  });

  test('Cash Flow question paper + answer key render in Gujarati', () async {
    final problems = [CashFlowGenerator.generate(board: board, schoolClass: schoolClass, difficulty: difficulty)];
    await expectNonEmpty(() => PaperPdfService.buildCashFlowQuestionPaper(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
    await expectNonEmpty(() => PaperPdfService.buildCashFlowAnswerKey(
        problems: problems, board: board, schoolClass: schoolClass, paperTitle: 'T', medium: medium));
  });
}
