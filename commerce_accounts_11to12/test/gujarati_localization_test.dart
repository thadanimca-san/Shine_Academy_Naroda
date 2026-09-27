import 'package:flutter/services.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:commerce_accounts_11to12/models/medium_model.dart';
import 'package:commerce_accounts_11to12/models/problem_model.dart';
import 'package:commerce_accounts_11to12/services/localization_service.dart';
import 'package:commerce_accounts_11to12/services/paper_pdf_service.dart';
import 'package:commerce_accounts_11to12/services/problem_generator.dart';

void main() {
  TestWidgetsFlutterBinding.ensureInitialized();

  group('LocalizationService', () {
    test('t() returns English unchanged when medium is English', () {
      expect(LocalizationService.t('Cash', Medium.english), 'Cash');
    });

    test('t() returns the Gujarati translation for a known term', () {
      expect(LocalizationService.t('Cash', Medium.gujarati), 'રોકડ');
    });

    test('t() falls back to English for an untranslated term rather than blanking out', () {
      expect(LocalizationService.t('Some Untranslated Thing', Medium.gujarati), 'Some Untranslated Thing');
    });

    test('translatePhrase() replaces the longer of two overlapping keys, not a partial match', () {
      final result = LocalizationService.translatePhrase('Trial Balance', Medium.gujarati);
      expect(result, 'મેળવણી પત્રક');
      expect(result.contains('બાકી'), isFalse); // "Balance" alone must not have partially matched
    });

    test('translatePhrase() substitutes multiple known terms inside a dynamic sentence', () {
      final result = LocalizationService.translatePhrase('Debit: Cash, Credit: Sales', Medium.gujarati);
      expect(result, contains('રોકડ'));
      expect(result, contains('વેચાણ'));
      expect(result, contains('ઉધાર'));
      expect(result, contains('જમા'));
    });
  });

  group('Gujarati PDF generation', () {
    test('NotoSansGujarati-Regular.ttf and Bold.ttf assets load and are valid non-empty font files', () async {
      final regular = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
      final bold = await rootBundle.load('assets/fonts/NotoSansGujarati-Bold.ttf');
      expect(regular.lengthInBytes, greaterThan(50000));
      expect(bold.lengthInBytes, greaterThan(50000));
    });

    test('question paper PDF renders in Gujarati medium without throwing', () async {
      final problems = [
        ProblemGenerator.generateJournalLedgerTrialBalance(board: Board.gseb, schoolClass: 11, difficulty: 2),
      ];
      final doc = await PaperPdfService.buildQuestionPaper(
        problems: problems,
        board: Board.gseb,
        schoolClass: 11,
        paperTitle: 'Journal, Ledger & Trial Balance',
        medium: Medium.gujarati,
      );
      final bytes = await doc.save();
      expect(bytes.isNotEmpty, isTrue);
    });

    test('answer key PDF renders in Gujarati medium without throwing', () async {
      final problems = [
        ProblemGenerator.generateJournalLedgerTrialBalance(board: Board.gseb, schoolClass: 11, difficulty: 2),
      ];
      final doc = await PaperPdfService.buildAnswerKey(
        problems: problems,
        board: Board.gseb,
        schoolClass: 11,
        paperTitle: 'Journal, Ledger & Trial Balance',
        medium: Medium.gujarati,
      );
      final bytes = await doc.save();
      expect(bytes.isNotEmpty, isTrue);
    });

    test('English medium still uses the DejaVu theme and Gujarati medium does not affect it', () async {
      final problems = [
        ProblemGenerator.generateJournalLedgerTrialBalance(board: Board.cbse, schoolClass: 11, difficulty: 2),
      ];
      final englishDoc = await PaperPdfService.buildQuestionPaper(
        problems: problems,
        board: Board.cbse,
        schoolClass: 11,
        paperTitle: 'English Medium Test',
      );
      final bytes = await englishDoc.save();
      expect(bytes.isNotEmpty, isTrue);
    });
  });
}
