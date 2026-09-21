import 'dart:io';

import 'package:flutter/services.dart' show rootBundle;
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:shine_academy_naroda/core/utils/pdf_branding_util.dart';

import '../data/branding.dart';
import '../models/account_model.dart';
import '../models/brs_model.dart';
import '../models/depreciation_model.dart';
import '../models/cash_flow_model.dart';
import '../models/company_accounts_model.dart';
import '../models/dissolution_model.dart';
import '../models/final_accounts_model.dart';
import '../models/medium_model.dart';
import '../models/partnership_model.dart';
import '../models/problem_model.dart';
import 'accounting_solver.dart';
import 'localization_service.dart';
import 'brs_generator.dart';
import 'cash_book_generator.dart';
import 'cash_book_solver.dart';
import 'cash_flow_generator.dart';
import 'company_accounts_generator.dart';
import 'depreciation_generator.dart';
import 'depreciation_solver.dart';
import 'dissolution_generator.dart';
import 'final_accounts_generator.dart';
import 'final_accounts_solver.dart';
import 'partnership_generator.dart';
import 'rectification_generator.dart';

/// Builds a question paper PDF and a matching fully-worked answer key PDF
/// from the same list of [GeneratedProblem]s. Both documents carry the
/// Shine Academy Naroda branding in the header/footer, since every
/// printed paper a teacher hands out is also promotion for the academy.
class PaperPdfService {
  PaperPdfService._();

  static pw.ThemeData? _cachedTheme;
  static pw.ThemeData? _cachedGujaratiTheme;

  /// DejaVu Sans supports the ₹ (Rupee) glyph, which the pdf package's
  /// built-in default font does not — without this, every ₹ prints as a
  /// missing-glyph box. Loaded once and reused across all documents.
  ///
  /// DejaVu Sans has no Gujarati glyph coverage at all, so Gujarati-medium
  /// papers use Noto Sans Gujarati instead (loaded/cached separately, since
  /// most documents are still English and shouldn't pay for a font they
  /// don't use). Noto Sans Gujarati in turn has no Latin glyph coverage —
  /// every paper mixes in English (account codes, "A/c Dr.", branding,
  /// page numbers, and any term not yet in the translation dictionary) —
  /// so DejaVu Sans is registered as its [pw.ThemeData.fontFallback] to
  /// cover those characters instead of them rendering as missing-glyph
  /// boxes.
  static Future<pw.ThemeData> _loadTheme([Medium medium = Medium.english]) async {
    if (medium == Medium.gujarati) {
      if (_cachedGujaratiTheme != null) return _cachedGujaratiTheme!;
      final regularData = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
      final boldData = await rootBundle.load('assets/fonts/NotoSansGujarati-Bold.ttf');
      final latinFallbackData = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
      // Noto Sans Gujarati ships no italic variant, and leaving `italic`
      // unset makes the pdf package silently fall back to its built-in
      // Helvetica-Oblique — which has zero Unicode coverage and drops
      // every Gujarati AND fallback glyph in any pw.FontStyle.italic text
      // (several answer-key labels, e.g. "Balance c/d", are italicised).
      // Reusing the regular Gujarati font for italic avoids that silent
      // fallback; it just renders upright instead of slanted.
      final regularFont = pw.Font.ttf(regularData);
      final boldFont = pw.Font.ttf(boldData);
      final theme = pw.ThemeData.withFont(
        base: regularFont,
        bold: boldFont,
        italic: regularFont,
        boldItalic: boldFont,
        fontFallback: [pw.Font.ttf(latinFallbackData)],
      );
      _cachedGujaratiTheme = theme;
      return theme;
    }
    if (_cachedTheme != null) return _cachedTheme!;
    final regularData = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
    final boldData = await rootBundle.load('assets/fonts/DejaVuSans-Bold.ttf');
    final theme = pw.ThemeData.withFont(
      base: pw.Font.ttf(regularData),
      bold: pw.Font.ttf(boldData),
    );
    _cachedTheme = theme;
    return theme;
  }

  static Future<pw.Document> buildQuestionPaper({
    required List<GeneratedProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    final totalMarks = problems.fold(0.0, (s, p) => s + p.marks);

    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, totalMarks, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text('Q${i + 1}. (${_fmtMarks(problems[i].marks)} marks)',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
            pw.Text(LocalizationService.translatePhrase(problems[i].questionText, medium)),
            pw.SizedBox(height: 4),
            for (final t in problems[i].transactions)
              pw.Bullet(text: LocalizationService.translatePhrase(t.transactionText, medium)),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildAnswerKey({
    required List<GeneratedProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);

    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final problem = problems[i];
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. ${LocalizationService.t('Journal', medium)} Entries',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));

            for (final entry in problem.transactions) {
              final solution = AccountingSolver.explainEntry(entry, board: board);
              widgets.add(pw.SizedBox(height: 6));
              widgets.add(pw.Text(LocalizationService.translatePhrase(entry.transactionText, medium),
                  style: const pw.TextStyle(fontStyle: pw.FontStyle.italic)));
              widgets.add(_journalEntryTable(entry, medium));
              for (final step in solution.steps) {
                widgets.add(pw.Bullet(
                    text: LocalizationService.translatePhrase('${step.title}: ${step.reasoning}', medium),
                    style: const pw.TextStyle(fontSize: 9)));
              }
            }

            final ledgers = AccountingSolver.postToLedger(problem.transactions);
            widgets.add(pw.SizedBox(height: 8));
            widgets.add(pw.Text('${LocalizationService.t('Ledger', medium)} Accounts',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 12)));
            for (final l in ledgers) {
              widgets.add(_ledgerTable(l, medium));
            }

            final tb = AccountingSolver.buildTrialBalance(ledgers);
            widgets.add(pw.SizedBox(height: 8));
            widgets.add(pw.Text(LocalizationService.t('Trial Balance', medium),
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 12)));
            widgets.add(_trialBalanceTable(tb, medium));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildCashBookQuestionPaper({
    required List<GeneratedCashBookProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text(
                'Q${i + 1}. ${LocalizationService.t('Prepare a Double Column Cash Book from the following transactions', medium)}:',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
            pw.Text('${LocalizationService.t('Opening Cash Balance', medium)}: ${_fmtMarks(problems[i].openingCash)}, '
                '${LocalizationService.t('Opening Bank Balance', medium)}: ${_fmtMarks(problems[i].openingBank)}'),
            pw.SizedBox(height: 4),
            for (final t in problems[i].transactions)
              pw.Bullet(text: LocalizationService.translatePhrase(t.transactionText, medium)),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildCashBookAnswerKey({
    required List<GeneratedCashBookProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final problem = problems[i];
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. ${LocalizationService.t('Double Column Cash Book', medium)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(_cashBookTable(problem, medium));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static pw.Widget _cashBookTable(GeneratedCashBookProblem problem, [Medium medium = Medium.english]) {
    final totals = CashBookSolver.solve(problem.transactions,
        openingCash: problem.openingCash, openingBank: problem.openingBank);

    pw.TableRow row(String receiptP, String rDisc, String rCash, String rBank, String paymentP, String pDisc, String pCash, String pBank) {
      return pw.TableRow(children: [
        _cell(receiptP), _cell(rDisc), _cell(rCash), _cell(rBank),
        _cell(paymentP), _cell(pDisc), _cell(pCash), _cell(pBank),
      ]);
    }

    final particulars = LocalizationService.t('Particulars', medium);
    final disc = LocalizationService.t('Disc.', medium);
    final cash = LocalizationService.t('Cash', medium);
    final bank = LocalizationService.t('Bank', medium);
    final toBalanceBd = LocalizationService.t('To Balance b/d', medium);
    final byBalanceCd = LocalizationService.t('By Balance c/d', medium);

    final rows = <pw.TableRow>[
      row(particulars, disc, cash, bank, particulars, disc, cash, bank),
      row(toBalanceBd, '', _fmtMarks(problem.openingCash), _fmtMarks(problem.openingBank), '', '', '', ''),
    ];

    for (final tx in problem.transactions) {
      final r = tx.receiptRow;
      final p = tx.paymentRow;
      rows.add(row(
        r != null ? 'To ${LocalizationService.translatePhrase(r.particulars, medium)}' : '',
        r?.discountAmount != null ? _fmtMarks(r!.discountAmount!) : '',
        r?.cashAmount != null ? _fmtMarks(r!.cashAmount!) : '',
        r?.bankAmount != null ? _fmtMarks(r!.bankAmount!) : '',
        p != null ? 'By ${LocalizationService.translatePhrase(p.particulars, medium)}' : '',
        p?.discountAmount != null ? _fmtMarks(p!.discountAmount!) : '',
        p?.cashAmount != null ? _fmtMarks(p!.cashAmount!) : '',
        p?.bankAmount != null ? _fmtMarks(p!.bankAmount!) : '',
      ));
    }

    rows.add(row(
      '', _fmtMarks(totals.totalDiscountAllowed), '', '',
      byBalanceCd, _fmtMarks(totals.totalDiscountReceived),
      _fmtMarks(totals.closingCashBalance), _fmtMarks(totals.closingBankBalance),
    ));

    return pw.Table(border: pw.TableBorder.all(width: 0.5), children: rows);
  }

  static pw.Widget _cell(String text) => pw.Padding(padding: const pw.EdgeInsets.all(3), child: pw.Text(text, style: const pw.TextStyle(fontSize: 8)));

  static Future<pw.Document> buildDepreciationQuestionPaper({
    required List<GeneratedDepreciationProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Builder(builder: (ctx) {
              final s = problems[i].schedule;
              final methodLabel = LocalizationService.t(
                  s.method == DepreciationMethod.straightLine ? 'Straight Line Method (SLM)' : 'Written Down Value Method (WDV)',
                  medium);
              return pw.Text(
                'Q${i + 1}. A ${s.assetName} was purchased for ${_fmtMarks(s.originalCost)}. '
                '${LocalizationService.t('Calculate depreciation for', medium)} ${s.years} '
                '${LocalizationService.t('years under the', medium)} $methodLabel @ ${s.ratePercent}% p.a.',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold),
              );
            }),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildDepreciationAnswerKey({
    required List<GeneratedDepreciationProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final s = problems[i].schedule;
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. ${s.assetName} — ${LocalizationService.t('Depreciation', medium)} Schedule',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(_depreciationTable(s, medium));
            for (var y = 0; y < s.rows.length; y++) {
              for (final step in DepreciationSolver.explainYear(s, y)) {
                widgets.add(pw.Bullet(
                    text: LocalizationService.translatePhrase('${step.title}: ${step.reasoning}', medium),
                    style: const pw.TextStyle(fontSize: 9)));
              }
            }
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static pw.Widget _depreciationTable(DepreciationSchedule s, [Medium medium = Medium.english]) {
    return pw.Table(
      border: pw.TableBorder.all(width: 0.5),
      children: [
        pw.TableRow(children: [
          _cell(LocalizationService.t('Year', medium)),
          _cell(LocalizationService.t('Opening', medium)),
          _cell(LocalizationService.t('Depreciation', medium)),
          _cell(LocalizationService.t('Closing', medium)),
        ]),
        for (final row in s.rows)
          pw.TableRow(children: [
            _cell('${row.year}'),
            _cell(_fmtMarks(row.openingBalance)),
            _cell(_fmtMarks(row.depreciationAmount)),
            _cell(_fmtMarks(row.closingBalance)),
          ]),
      ],
    );
  }

  static Future<pw.Document> buildRectificationQuestionPaper({
    required List<GeneratedRectificationProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text('Q${i + 1}. ${LocalizationService.t('Pass rectifying journal entries for the following errors', medium)}:',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
            pw.SizedBox(height: 4),
            for (var j = 0; j < problems[i].cases.length; j++)
              pw.Bullet(
                  text:
                      '${String.fromCharCode(97 + j)}) ${LocalizationService.translatePhrase(problems[i].cases[j].errorDescription, medium)}'),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildRectificationAnswerKey({
    required List<GeneratedRectificationProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. ${LocalizationService.t('Rectification of Errors', medium)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            for (var j = 0; j < problems[i].cases.length; j++) {
              final c = problems[i].cases[j];
              widgets.add(pw.SizedBox(height: 6));
              widgets.add(pw.Text('${String.fromCharCode(97 + j)}) ${LocalizationService.translatePhrase(c.errorDescription, medium)}',
                  style: const pw.TextStyle(fontStyle: pw.FontStyle.italic)));
              widgets.add(_journalEntryTable(c.rectifyingEntry, medium));
              widgets.add(pw.Text(
                LocalizationService.t(
                    c.effect.toString().contains('oneSided')
                        ? 'One-sided error — routed through Suspense A/c.'
                        : 'Two-sided error — entry balances directly, no Suspense A/c needed.',
                    medium),
                style: const pw.TextStyle(fontSize: 9, fontStyle: pw.FontStyle.italic),
              ));
            }
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildBrsQuestionPaper({
    required List<GeneratedBrsProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text(
              'Q${i + 1}. ${LocalizationService.t('From the following particulars, prepare a Bank Reconciliation Statement and find the', medium)} '
              '${LocalizationService.t('Balance as per Pass Book', medium)}. ${LocalizationService.t('Balance as per Cash Book', medium)}: ${_fmtMarks(problems[i].cashBookBalance)}',
              style: pw.TextStyle(fontWeight: pw.FontWeight.bold),
            ),
            pw.SizedBox(height: 4),
            for (final item in problems[i].items)
              pw.Bullet(text: LocalizationService.translatePhrase(item.description, medium)),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildBrsAnswerKey({
    required List<GeneratedBrsProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final p = problems[i];
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. ${LocalizationService.t('Bank Reconciliation Statement', medium)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(_brsTable(p, medium));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static pw.Widget _brsTable(GeneratedBrsProblem p, [Medium medium = Medium.english]) {
    final addLabel = '${LocalizationService.t('Add', medium)} (₹)';
    final lessLabel = '${LocalizationService.t('Less', medium)} (₹)';
    final rows = <pw.TableRow>[
      pw.TableRow(children: [_cell(LocalizationService.t('Particulars', medium)), _cell(addLabel), _cell(lessLabel)]),
      pw.TableRow(children: [
        _cell(LocalizationService.t('Balance as per Cash Book', medium)),
        _cell(_fmtMarks(p.cashBookBalance)),
        _cell(''),
      ]),
    ];
    for (final item in p.items) {
      final isAdd = item.effectOnPassBookBalance == BrsAdjustment.add;
      rows.add(pw.TableRow(children: [
        _cell(LocalizationService.translatePhrase(item.description, medium)),
        _cell(isAdd ? _fmtMarks(item.amount) : ''),
        _cell(!isAdd ? _fmtMarks(item.amount) : ''),
      ]));
    }
    rows.add(pw.TableRow(children: [
      _cell(LocalizationService.t('Balance as per Pass Book', medium)),
      _cell(_fmtMarks(p.passBookBalance)),
      _cell(''),
    ]));
    return pw.Table(border: pw.TableBorder.all(width: 0.5), children: rows);
  }

  static Future<pw.Document> buildFinalAccountsQuestionPaper({
    required List<GeneratedFinalAccountsProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text(
              'Q${i + 1}. ${LocalizationService.t('From the following Trial Balance and adjustments, prepare the Trading Account, '
                  'Profit & Loss Account, and Balance Sheet:', medium)}',
              style: pw.TextStyle(fontWeight: pw.FontWeight.bold),
            ),
            pw.SizedBox(height: 4),
            _finalAccountsTrialBalanceTable(problems[i].input, medium),
            pw.SizedBox(height: 4),
            pw.Text('${LocalizationService.t('Adjustments', medium)}:', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 10)),
            for (final adj in problems[i].adjustments)
              pw.Bullet(text: LocalizationService.translatePhrase(adj.description, medium)),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildFinalAccountsAnswerKey({
    required List<GeneratedFinalAccountsProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final r = problems[i].result;
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. ${LocalizationService.t('Final Accounts', medium)}', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(pw.SizedBox(height: 4));
            widgets.add(pw.Text(LocalizationService.t('Trading Account', medium), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 11)));
            widgets.add(_twoSidedStatementTable(
              r.tradingAccountDebit, r.tradingAccountCredit,
              r.grossProfit > 0 ? LocalizationService.t('Gross Profit c/d', medium) : null, r.grossProfit > 0 ? r.grossProfit : null,
              r.grossProfit < 0 ? LocalizationService.t('Gross Loss c/d', medium) : null, r.grossProfit < 0 ? -r.grossProfit : null,
              medium,
            ));
            widgets.add(pw.SizedBox(height: 4));
            widgets.add(pw.Text(LocalizationService.t('Profit & Loss Account', medium), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 11)));
            widgets.add(_twoSidedStatementTable(
              r.profitLossDebit, r.profitLossCredit,
              r.netProfit > 0 ? LocalizationService.t('Net Profit (to Capital)', medium) : null, r.netProfit > 0 ? r.netProfit : null,
              r.netProfit < 0 ? LocalizationService.t('Net Loss (to Capital)', medium) : null, r.netProfit < 0 ? -r.netProfit : null,
              medium,
            ));
            widgets.add(pw.SizedBox(height: 4));
            widgets.add(pw.Text(LocalizationService.t('Balance Sheet', medium), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 11)));
            widgets.add(_twoSidedStatementTable(r.balanceSheetLiabilities, r.balanceSheetAssets, null, null, null, null, medium));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static pw.Widget _finalAccountsTrialBalanceTable(FinalAccountsInput i, [Medium medium = Medium.english]) {
    final rows = <TrialBalanceItem>[
      TrialBalanceItem(name: 'Opening Stock', debitAmount: i.openingStock),
      TrialBalanceItem(name: 'Purchases', debitAmount: i.purchases),
      TrialBalanceItem(name: 'Purchases Return', creditAmount: i.purchasesReturn),
      TrialBalanceItem(name: 'Sales', creditAmount: i.sales),
      TrialBalanceItem(name: 'Sales Return', debitAmount: i.salesReturn),
      TrialBalanceItem(name: 'Wages', debitAmount: i.wages),
      TrialBalanceItem(name: 'Carriage Inwards', debitAmount: i.carriageInwards),
      TrialBalanceItem(name: 'Carriage Outwards', debitAmount: i.carriageOutwards),
      TrialBalanceItem(name: 'Rent', debitAmount: i.rent),
      TrialBalanceItem(name: 'Salaries', debitAmount: i.salaries),
      TrialBalanceItem(name: 'Discount Allowed', debitAmount: i.discountAllowed),
      TrialBalanceItem(name: 'Discount Received', creditAmount: i.discountReceived),
      TrialBalanceItem(name: 'Commission Received', creditAmount: i.commissionReceived),
      TrialBalanceItem(name: 'Debtors', debitAmount: i.debtors),
      TrialBalanceItem(name: 'Creditors', creditAmount: i.creditors),
      TrialBalanceItem(name: 'Capital', creditAmount: i.capital),
      TrialBalanceItem(name: 'Drawings', debitAmount: i.drawings),
      TrialBalanceItem(name: 'Cash', debitAmount: i.cash),
      TrialBalanceItem(name: 'Bank', debitAmount: i.bank),
      TrialBalanceItem(name: 'Furniture', debitAmount: i.furniture),
      TrialBalanceItem(name: 'Machinery', debitAmount: i.machinery),
    ];

    final tableRows = <pw.TableRow>[
      pw.TableRow(children: [
        _cell(LocalizationService.t('Particulars', medium)),
        _cell(LocalizationService.t('Debit', medium)),
        _cell(LocalizationService.t('Credit', medium)),
      ]),
    ];
    for (final row in rows) {
      if (row.debitAmount <= 0 && row.creditAmount <= 0) continue;
      tableRows.add(pw.TableRow(children: [
        _cell(LocalizationService.t(row.name, medium)),
        _cell(row.debitAmount > 0 ? _fmtMarks(row.debitAmount) : ''),
        _cell(row.creditAmount > 0 ? _fmtMarks(row.creditAmount) : ''),
      ]));
    }
    return pw.Table(border: pw.TableBorder.all(width: 0.5), children: tableRows);
  }

  static pw.Widget _twoSidedStatementTable(
    List<StatementLine> left,
    List<StatementLine> right,
    String? leftBalLabel,
    double? leftBalAmt,
    String? rightBalLabel,
    double? rightBalAmt, [
    Medium medium = Medium.english,
  ]) {
    final maxRows = [left.length + (leftBalLabel != null ? 1 : 0), right.length + (rightBalLabel != null ? 1 : 0)]
        .reduce((a, b) => a > b ? a : b);
    final leftWithBal = [
      for (final l in left) StatementLine(particulars: LocalizationService.t(l.particulars, medium), amount: l.amount),
      if (leftBalLabel != null) StatementLine(particulars: leftBalLabel, amount: leftBalAmt!),
    ];
    final rightWithBal = [
      for (final r in right) StatementLine(particulars: LocalizationService.t(r.particulars, medium), amount: r.amount),
      if (rightBalLabel != null) StatementLine(particulars: rightBalLabel, amount: rightBalAmt!),
    ];

    final rows = <pw.TableRow>[];
    for (var i = 0; i < maxRows; i++) {
      final l = i < leftWithBal.length ? leftWithBal[i] : null;
      final r = i < rightWithBal.length ? rightWithBal[i] : null;
      rows.add(pw.TableRow(children: [
        _cell(l?.particulars ?? ''),
        _cell(l != null ? _fmtMarks(l.amount) : ''),
        _cell(r?.particulars ?? ''),
        _cell(r != null ? _fmtMarks(r.amount) : ''),
      ]));
    }
    return pw.Table(border: pw.TableBorder.all(width: 0.5), children: rows);
  }

  static Future<pw.Document> buildPartnershipAdmissionQuestionPaper({
    required List<GeneratedAdmissionProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Builder(builder: (ctx) {
              final p = problems[i];
              final sharePercent = (p.newPartnerShare * 100).round();
              return pw.Text(
                'Q${i + 1}. ${p.existingPartners.map((e) => '${e.name} (${_pctLabel(e.profitShareRatio)})').join(' and ')} '
                'are partners. They admit ${p.newPartnerName} for a $sharePercent% share in the firm, bringing in '
                'capital of ${_fmtMarks(p.newPartnerCapital)}. Goodwill of the firm is valued at '
                '${_fmtMarks(p.goodwill.totalFirmGoodwill)}. Existing capitals: '
                '${p.existingPartners.map((e) => '${e.name} ${_fmtMarks(e.capital)}').join(', ')}. '
                'Pass the necessary entries and prepare Partners\' Capital Accounts.',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold),
              );
            }),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildPartnershipAdmissionAnswerKey({
    required List<GeneratedAdmissionProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final p = problems[i];
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. ${LocalizationService.t('Admission', medium)} of ${p.newPartnerName}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(pw.Text(
                '${LocalizationService.t('New Profit Sharing Ratio', medium)}: ${p.result.newProfitSharingRatios.entries.map((e) => '${e.key} ${_pctLabel(e.value)}').join(', ')}',
                style: const pw.TextStyle(fontSize: 10)));
            widgets.add(pw.Text(
                '${LocalizationService.t('Sacrificing Ratio', medium)}: ${p.result.sacrificingRatios.entries.map((e) => '${e.key} ${_pctLabel(e.value)}').join(', ')}',
                style: const pw.TextStyle(fontSize: 10)));
            widgets.add(pw.SizedBox(height: 4));
            widgets.add(_capitalAccountsTable(p.result.capitalAccounts, medium));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildPartnershipDepartureQuestionPaper({
    required List<GeneratedDepartureProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Builder(builder: (ctx) {
              final p = problems[i];
              final reasonLabel = p.reason == DepartureReason.retirement ? 'retires' : 'dies';
              return pw.Text(
                'Q${i + 1}. ${p.allPartners.map((e) => '${e.name} (${_pctLabel(e.profitShareRatio)})').join(', ')} '
                'are partners. ${p.departingPartnerName} $reasonLabel from the firm. Goodwill of the firm is valued '
                'at ${_fmtMarks(p.goodwill.totalFirmGoodwill)}. Remaining partners continue in their existing ratio. '
                'Capitals: ${p.allPartners.map((e) => '${e.name} ${_fmtMarks(e.capital)}').join(', ')}. '
                'Pass the necessary entries and prepare Partners\' Capital Accounts.',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold),
              );
            }),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildPartnershipDepartureAnswerKey({
    required List<GeneratedDepartureProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final p = problems[i];
            final reasonLabel = LocalizationService.t(p.reason == DepartureReason.retirement ? 'Retirement' : 'Death', medium);
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. $reasonLabel of ${p.departingPartnerName}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(pw.Text(
                '${LocalizationService.t('New Profit Sharing Ratio', medium)}: ${p.result.newProfitSharingRatios.entries.map((e) => '${e.key} ${_pctLabel(e.value)}').join(', ')}',
                style: const pw.TextStyle(fontSize: 10)));
            widgets.add(pw.Text(
                '${LocalizationService.t('Gaining Ratio', medium)}: ${p.result.gainingRatios.entries.map((e) => '${e.key} ${_pctLabel(e.value)}').join(', ')}',
                style: const pw.TextStyle(fontSize: 10)));
            widgets.add(pw.SizedBox(height: 4));
            widgets.add(_capitalAccountsTable(p.result.capitalAccounts, medium));
            widgets.add(pw.Text(
                'Amount payable to ${p.departingPartnerName}: ${_fmtMarks(p.result.amountPayableToDepartingPartner)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 10)));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static pw.Widget _capitalAccountsTable(List<CapitalAccountRow> rows, [Medium medium = Medium.english]) {
    return pw.Table(
      border: pw.TableBorder.all(width: 0.5),
      children: [
        pw.TableRow(children: [
          _cell(LocalizationService.t('Particulars', medium)),
          _cell(LocalizationService.t('Balance b/d', medium)),
          _cell(LocalizationService.t('Goodwill Dr', medium)),
          _cell(LocalizationService.t('Goodwill Cr', medium)),
          _cell(LocalizationService.t('Balance c/d', medium)),
        ]),
        for (final row in rows)
          pw.TableRow(children: [
            _cell(row.partnerName),
            _cell(_fmtMarks(row.openingBalance)),
            _cell(row.goodwillDebit > 0 ? _fmtMarks(row.goodwillDebit) : '-'),
            _cell(row.goodwillCredit > 0 ? _fmtMarks(row.goodwillCredit) : '-'),
            _cell(_fmtMarks(row.closingBalance)),
          ]),
      ],
    );
  }

  static String _pctLabel(double share) => '${(share * 100).round()}%';

  static Future<pw.Document> buildShareIssueQuestionPaper({
    required List<GeneratedShareIssueProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text('Q${i + 1}. ${_shareIssueQuestionText(problems[i])}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildShareIssueAnswerKey({
    required List<GeneratedShareIssueProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final p = problems[i];
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. ${LocalizationService.t('Issue of Shares', medium)}', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            for (final step in p.result.steps) {
              widgets.add(pw.SizedBox(height: 4));
              widgets.add(pw.Text(LocalizationService.translatePhrase(step.title, medium), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 10)));
              widgets.add(_shareIssueStepTable(step, medium));
              widgets.add(pw.Text(LocalizationService.translatePhrase(step.narration, medium), style: const pw.TextStyle(fontSize: 8, fontStyle: pw.FontStyle.italic)));
            }
            widgets.add(pw.SizedBox(height: 6));
            widgets.add(pw.Text('${LocalizationService.t('Total Capital Raised', medium)}: ${_fmtMarks(p.result.totalCapitalRaised)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 10)));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static String _shareIssueQuestionText(GeneratedShareIssueProblem p) {
    final c = p.calls;
    final premiumText = c.premiumPerShare > 0 ? ' (including a premium of ${_fmtMarks(c.premiumPerShare)} per share)' : '';
    final forfeitureText = p.sharesForfeited > 0
        ? ', except the final call on ${p.sharesForfeited} shares, which were subsequently forfeited and reissued '
            'at ${_fmtMarks(p.reissuePricePerShare)} per share, fully paid up'
        : '';
    return 'A company issued ${p.sharesIssued} shares of ${_fmtMarks(c.faceValue)} each$premiumText, payable as: '
        'Application ${_fmtMarks(c.applicationAmount)}, Allotment ${_fmtMarks(c.allotmentAmount)}'
        '${c.firstCallAmount > 0 ? ', First Call ${_fmtMarks(c.firstCallAmount)}' : ''}'
        '${c.finalCallAmount > 0 ? ', Final Call ${_fmtMarks(c.finalCallAmount)}' : ''}. '
        'All shares were subscribed and all money was received$forfeitureText. Pass the necessary journal entries.';
  }

  static pw.Widget _shareIssueStepTable(ShareIssueStep step, [Medium medium = Medium.english]) {
    final rows = <pw.TableRow>[
      pw.TableRow(children: [_cell('${LocalizationService.t('Bank', medium)} A/c Dr.'), _cell(_fmtMarks(step.debitCash))]),
      if (step.secondDebitAccountName != null)
        pw.TableRow(children: [
          _cell('${LocalizationService.t(step.secondDebitAccountName!, medium)} Dr.'),
          _cell(_fmtMarks(step.secondDebitAmount ?? 0)),
        ]),
      pw.TableRow(children: [
        _cell('   ${LocalizationService.t('To', medium)} ${LocalizationService.t(step.creditAccountName, medium)}'),
        _cell(_fmtMarks(step.creditAmount)),
      ]),
      if (step.secondCreditAccountName != null)
        pw.TableRow(children: [
          _cell('   ${LocalizationService.t('To', medium)} ${LocalizationService.t(step.secondCreditAccountName!, medium)}'),
          _cell(_fmtMarks(step.secondCreditAmount ?? 0)),
        ]),
    ];
    return pw.Table(border: pw.TableBorder.all(width: 0.5), children: rows);
  }

  static Future<pw.Document> buildCashFlowQuestionPaper({
    required List<GeneratedCashFlowProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text('Q${i + 1}. ${LocalizationService.t('From the following information, prepare a Cash Flow Statement (Indirect Method) for the year:', medium)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
            pw.SizedBox(height: 4),
            _cashFlowFactsList(problems[i].data, medium),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildCashFlowAnswerKey({
    required List<GeneratedCashFlowProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final r = problems[i].result;
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. ${LocalizationService.t('Cash Flow Statement', medium)}', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(_cashFlowSectionTable(LocalizationService.t('A. Cash Flow from Operating Activities', medium), r.operatingLines, medium));
            widgets.add(_cashFlowSectionTable(LocalizationService.t('B. Cash Flow from Investing Activities', medium), r.investingLines, medium));
            widgets.add(_cashFlowSectionTable(LocalizationService.t('C. Cash Flow from Financing Activities', medium), r.financingLines, medium));
            widgets.add(pw.SizedBox(height: 4));
            widgets.add(pw.Text('${LocalizationService.t('Net Increase in Cash', medium)}: ${_fmtMarks(r.netIncreaseInCash)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 10)));
            widgets.add(pw.Text('${LocalizationService.t('Closing Cash and Bank Balance', medium)}: ${_fmtMarks(r.closingCash)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 10)));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static pw.Widget _cashFlowFactsList(CashFlowBalanceSheetData d, [Medium medium = Medium.english]) {
    final facts = <String>[
      'Net Profit before Tax: ${_fmtMarks(d.netProfitBeforeTax)}',
      'Depreciation for the year: ${_fmtMarks(d.depreciationForYear)}',
      if (d.debtorsOpening > 0 || d.debtorsClosing > 0)
        'Debtors: Opening ${_fmtMarks(d.debtorsOpening)}, Closing ${_fmtMarks(d.debtorsClosing)}',
      if (d.stockOpening > 0 || d.stockClosing > 0)
        'Stock: Opening ${_fmtMarks(d.stockOpening)}, Closing ${_fmtMarks(d.stockClosing)}',
      if (d.creditorsOpening > 0 || d.creditorsClosing > 0)
        'Creditors: Opening ${_fmtMarks(d.creditorsOpening)}, Closing ${_fmtMarks(d.creditorsClosing)}',
      if (d.outstandingExpensesOpening > 0 || d.outstandingExpensesClosing > 0)
        'Outstanding Expenses: Opening ${_fmtMarks(d.outstandingExpensesOpening)}, Closing ${_fmtMarks(d.outstandingExpensesClosing)}',
      if (d.machineryPurchased > 0) 'Machinery Purchased: ${_fmtMarks(d.machineryPurchased)}',
      if (d.machinerySold > 0) 'Machinery Sold: ${_fmtMarks(d.machinerySold)}',
      if (d.loanRaised > 0) 'Loan Raised: ${_fmtMarks(d.loanRaised)}',
      if (d.loanRepaid > 0) 'Loan Repaid: ${_fmtMarks(d.loanRepaid)}',
      if (d.sharesIssuedForCash > 0) 'Shares Issued for Cash: ${_fmtMarks(d.sharesIssuedForCash)}',
      'Opening Cash and Bank Balance: ${_fmtMarks(d.openingCashAndBank)}',
    ];
    return pw.Column(children: [for (final f in facts) pw.Bullet(text: LocalizationService.translatePhrase(f, medium))]);
  }

  static pw.Widget _cashFlowSectionTable(String title, List<CashFlowLine> lines, [Medium medium = Medium.english]) {
    return pw.Padding(
      padding: const pw.EdgeInsets.symmetric(vertical: 4),
      child: pw.Column(
        crossAxisAlignment: pw.CrossAxisAlignment.start,
        children: [
          pw.Text(title, style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 10)),
          pw.Table(
            border: pw.TableBorder.all(width: 0.5),
            children: [
              for (final line in lines)
                pw.TableRow(children: [
                  _cell(LocalizationService.translatePhrase(line.particulars, medium)),
                  _cell(_fmtMarks(line.amount)),
                ]),
            ],
          ),
        ],
      ),
    );
  }

  static Future<pw.Document> buildDissolutionQuestionPaper({
    required List<GeneratedDissolutionProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Builder(builder: (ctx) {
              final p = problems[i];
              return pw.Text(
                'Q${i + 1}. ${p.partners.map((e) => '${e.name} (${_pctLabel(e.profitShareRatio)})').join(', ')} '
                'decide to dissolve the firm. Capitals: ${p.partners.map((e) => '${e.name} ${_fmtMarks(e.capital)}').join(', ')}. '
                'Assets realised: ${p.assets.map((a) => '${a.assetName} (Book ${_fmtMarks(a.bookValue)}, Realised ${_fmtMarks(a.realisedAmount)})').join(', ')}. '
                'Liabilities paid: ${p.liabilities.map((l) => '${l.liabilityName} (Book ${_fmtMarks(l.bookValue)}, Paid ${_fmtMarks(l.amountPaid)})').join(', ')}.'
                '${p.dissolutionExpenses > 0 ? ' Realisation expenses ${_fmtMarks(p.dissolutionExpenses)}.' : ''} '
                '${LocalizationService.t('Prepare the Realisation Account and show the final settlement with partners.', medium)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold),
              );
            }),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildDissolutionAnswerKey({
    required List<GeneratedDissolutionProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
    Medium medium = Medium.english,
  }) async {
    final theme = await _loadTheme(medium);
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel, null, medium),
        footer: (ctx) => _buildFooter(ctx, medium),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final p = problems[i];
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. ${LocalizationService.t('Dissolution', medium)} — ${LocalizationService.t('Realisation Account', medium)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(_realisationAccountTable(p.result, medium));
            widgets.add(pw.SizedBox(height: 4));
            widgets.add(pw.Text(
                p.result.realisationProfitOrLoss >= 0
                    ? 'Realisation Profit: ${_fmtMarks(p.result.realisationProfitOrLoss)}'
                    : 'Realisation Loss: ${_fmtMarks(-p.result.realisationProfitOrLoss)}',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 10)));
            for (final s in p.result.partnerSettlements) {
              widgets.add(pw.Text(
                  '${s.partnerName}: Capital ${_fmtMarks(s.capitalBalance)} '
                  '${s.shareOfRealisationProfit >= 0 ? '+' : '-'} ${_fmtMarks(s.shareOfRealisationProfit.abs())} '
                  '= ${_fmtMarks(s.finalAmountReceived)}',
                  style: const pw.TextStyle(fontSize: 9)));
            }
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static pw.Widget _realisationAccountTable(DissolutionResult result, [Medium medium = Medium.english]) {
    final maxRows = [result.realisationDebit.length, result.realisationCredit.length].reduce((a, b) => a > b ? a : b);
    final rows = <pw.TableRow>[
      pw.TableRow(children: [
        _cell(LocalizationService.t('Debit', medium)),
        _cell(LocalizationService.t('Amount', medium)),
        _cell(LocalizationService.t('Credit', medium)),
        _cell(LocalizationService.t('Amount', medium)),
      ]),
    ];
    for (var i = 0; i < maxRows; i++) {
      final d = i < result.realisationDebit.length ? result.realisationDebit[i] : null;
      final c = i < result.realisationCredit.length ? result.realisationCredit[i] : null;
      rows.add(pw.TableRow(children: [
        _cell(d != null ? LocalizationService.translatePhrase(d.particulars, medium) : ''),
        _cell(d != null ? _fmtMarks(d.amount) : ''),
        _cell(c != null ? LocalizationService.translatePhrase(c.particulars, medium) : ''),
        _cell(c != null ? _fmtMarks(c.amount) : ''),
      ]));
    }
    return pw.Table(border: pw.TableBorder.all(width: 0.5), children: rows);
  }

  static pw.Widget _journalEntryTable(JournalEntry entry, [Medium medium = Medium.english]) {
    final accountName = (String n) => LocalizationService.t(n, medium);
    return pw.Table(
      border: pw.TableBorder.all(width: 0.5),
      columnWidths: const {0: pw.FlexColumnWidth(3), 1: pw.FlexColumnWidth(1), 2: pw.FlexColumnWidth(1)},
      children: [
        for (final line in entry.lines)
          pw.TableRow(children: [
            pw.Padding(
              padding: const pw.EdgeInsets.all(3),
              child: pw.Text(line.side == EntrySide.debit
                  ? '${accountName(line.account.name)} A/c Dr.'
                  : '   To ${accountName(line.account.name)} A/c'),
            ),
            pw.Padding(padding: const pw.EdgeInsets.all(3), child: pw.Text(line.side == EntrySide.debit ? _fmtMarks(line.amount) : '')),
            pw.Padding(padding: const pw.EdgeInsets.all(3), child: pw.Text(line.side == EntrySide.credit ? _fmtMarks(line.amount) : '')),
          ]),
        pw.TableRow(children: [
          pw.Padding(
              padding: const pw.EdgeInsets.all(3),
              child: pw.Text(LocalizationService.translatePhrase(entry.narration, medium),
                  style: const pw.TextStyle(fontStyle: pw.FontStyle.italic, fontSize: 9))),
          pw.Container(),
          pw.Container(),
        ]),
      ],
    );
  }

  static pw.Widget _ledgerTable(dynamic ledger, [Medium medium = Medium.english]) {
    return pw.Padding(
      padding: const pw.EdgeInsets.symmetric(vertical: 4),
      child: pw.Column(
        crossAxisAlignment: pw.CrossAxisAlignment.start,
        children: [
          pw.Text('${LocalizationService.t(ledger.account.name as String, medium)} A/c',
              style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 11)),
          pw.Row(
            children: [
              pw.Expanded(child: _ledgerSide(LocalizationService.t('Debit', medium), ledger.debitPostings, ledger.totalDebit,
                  ledger.balanceSide == EntrySide.credit ? ledger.balanceAmount : null, medium)),
              pw.Expanded(child: _ledgerSide(LocalizationService.t('Credit', medium), ledger.creditPostings, ledger.totalCredit,
                  ledger.balanceSide == EntrySide.debit ? ledger.balanceAmount : null, medium)),
            ],
          ),
        ],
      ),
    );
  }

  static pw.Widget _ledgerSide(String label, List postings, double total, double? balFigure, [Medium medium = Medium.english]) {
    return pw.Column(
      crossAxisAlignment: pw.CrossAxisAlignment.start,
      children: [
        pw.Text(label, style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 9)),
        for (final p in postings)
          pw.Text('${LocalizationService.translatePhrase(p.particulars as String, medium)}  ${_fmtMarks(p.amount as double)}',
              style: const pw.TextStyle(fontSize: 9)),
        if (balFigure != null && balFigure > 0.005)
          pw.Text('${LocalizationService.translatePhrase('Balance c/d', medium)}  ${_fmtMarks(balFigure)}',
              style: const pw.TextStyle(fontSize: 9, fontStyle: pw.FontStyle.italic)),
      ],
    );
  }

  static pw.Widget _trialBalanceTable(dynamic tb, [Medium medium = Medium.english]) {
    return pw.Table(
      border: pw.TableBorder.all(width: 0.5),
      columnWidths: const {0: pw.FlexColumnWidth(3), 1: pw.FlexColumnWidth(1), 2: pw.FlexColumnWidth(1)},
      children: [
        pw.TableRow(children: [
          pw.Padding(padding: const pw.EdgeInsets.all(3), child: pw.Text(LocalizationService.t('Account', medium), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 9))),
          pw.Padding(padding: const pw.EdgeInsets.all(3), child: pw.Text(LocalizationService.t('Debit', medium), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 9))),
          pw.Padding(padding: const pw.EdgeInsets.all(3), child: pw.Text(LocalizationService.t('Credit', medium), style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 9))),
        ]),
        for (final row in tb.rows)
          pw.TableRow(children: [
            pw.Padding(padding: const pw.EdgeInsets.all(3), child: pw.Text(LocalizationService.t(row.account.name as String, medium), style: const pw.TextStyle(fontSize: 9))),
            pw.Padding(padding: const pw.EdgeInsets.all(3), child: pw.Text(row.debitAmount > 0 ? _fmtMarks(row.debitAmount) : '', style: const pw.TextStyle(fontSize: 9))),
            pw.Padding(padding: const pw.EdgeInsets.all(3), child: pw.Text(row.creditAmount > 0 ? _fmtMarks(row.creditAmount) : '', style: const pw.TextStyle(fontSize: 9))),
          ]),
      ],
    );
  }

  static pw.Widget _buildHeader(Board board, int schoolClass, String title, String setLabel, double? totalMarks,
      [Medium medium = Medium.english]) {
    final boardLabel = board == Board.gseb ? 'GSEB' : 'CBSE';
    final logoFile = File(Branding.logoAssetPath);
    final hasLogo = logoFile.existsSync();

    return pw.Column(
      children: [
        pw.Row(
          mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
          children: [
            if (hasLogo)
              pw.Image(pw.MemoryImage(logoFile.readAsBytesSync()), height: 36)
            else
              pw.Text(Branding.academyName, style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 12)),
            pw.Text(setLabel, style: const pw.TextStyle(fontSize: 10)),
          ],
        ),
        pw.SizedBox(height: 6),
        pw.Text(LocalizationService.translatePhrase(title, medium),
            style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 16), textAlign: pw.TextAlign.center),
        pw.Text('$boardLabel — Class $schoolClass — Accountancy', style: const pw.TextStyle(fontSize: 11), textAlign: pw.TextAlign.center),
        if (totalMarks != null)
          pw.Text('Total Marks: ${_fmtMarks(totalMarks)}', style: const pw.TextStyle(fontSize: 10)),
        pw.Divider(),
      ],
    );
  }

  static pw.Widget _buildFooter(pw.Context ctx, [Medium medium = Medium.english]) {
    return pw.Column(
      children: [
        pw.Divider(height: 4),
        pw.Row(
          mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
          children: [
            pw.Text('${Branding.academyName} — ${Branding.tagline}', style: const pw.TextStyle(fontSize: 8, color: PdfColors.grey700)),
            pw.Text(Branding.websiteUrl, style: const pw.TextStyle(fontSize: 8, color: PdfColors.grey700)),
            pw.Text('Page ${ctx.pageNumber}/${ctx.pagesCount}', style: const pw.TextStyle(fontSize: 8)),
          ],
        ),
      ],
    );
  }

  static String _fmtMarks(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
