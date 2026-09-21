import 'dart:io';

import 'package:flutter/services.dart' show rootBundle;
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:shine_academy_naroda/core/utils/pdf_branding_util.dart';

import '../data/branding.dart';
import '../models/board_model.dart';
import '../models/central_tendency_model.dart';
import '../models/correlation_model.dart';
import '../models/data_series_model.dart';
import '../models/index_number_model.dart';
import 'central_tendency_generator.dart';
import 'correlation_generator.dart';
import 'dispersion_generator.dart';
import 'index_number_generator.dart';
import 'regression_generator.dart';

/// Builds a worksheet PDF and a matching fully-worked answer key PDF
/// from the same list of generated problems. Both documents carry the
/// Shine Academy Naroda branding, since every printed paper a teacher
/// hands out is also promotion for the academy.
class PaperPdfService {
  PaperPdfService._();

  static pw.ThemeData? _cachedTheme;

  /// DejaVu Sans supports the ₹ (Rupee) and other symbols the pdf
  /// package's built-in default font may not — loaded once and reused.
  static Future<pw.ThemeData> _loadTheme() async {
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

  static Future<pw.Document> buildCentralTendencyQuestionPaper({
    required List<GeneratedCentralTendencyProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
  }) async {
    final theme = await _loadTheme();
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel),
        footer: (ctx) => _buildFooter(ctx),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text('Q${i + 1}. Find the Mean, Median and Mode of the following data:',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
            pw.SizedBox(height: 4),
            _seriesTable(problems[i].series),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildCentralTendencyAnswerKey({
    required List<GeneratedCentralTendencyProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
  }) async {
    final theme = await _loadTheme();
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel),
        footer: (ctx) => _buildFooter(ctx),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final p = problems[i];
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. Measures of Central Tendency',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(_measureSection('Mean', p.result.mean.steps, _fmt(p.result.mean.mean)));
            widgets.add(_measureSection('Median', p.result.median.steps, _fmt(p.result.median.median)));
            widgets.add(_measureSection(
                'Mode', p.result.mode.steps, p.result.mode.mode != null ? _fmt(p.result.mode.mode!) : 'No mode'));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static pw.Widget _measureSection(String title, List<SolutionStep> steps, String answer) {
    return pw.Padding(
      padding: const pw.EdgeInsets.symmetric(vertical: 4),
      child: pw.Column(
        crossAxisAlignment: pw.CrossAxisAlignment.start,
        children: [
          pw.Text(title, style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 11)),
          for (final step in steps)
            pw.Bullet(text: '${step.title}: ${step.reasoning}', style: const pw.TextStyle(fontSize: 9)),
          pw.Text('Answer: $answer', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 10)),
        ],
      ),
    );
  }

  static Future<pw.Document> buildDispersionQuestionPaper({
    required List<GeneratedDispersionProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
  }) async {
    final theme = await _loadTheme();
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel),
        footer: (ctx) => _buildFooter(ctx),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text('Q${i + 1}. Find the Range, Mean Deviation, Standard Deviation and Coefficient of Variation of the following data:',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
            pw.SizedBox(height: 4),
            _seriesTable(problems[i].series),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildDispersionAnswerKey({
    required List<GeneratedDispersionProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
  }) async {
    final theme = await _loadTheme();
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel),
        footer: (ctx) => _buildFooter(ctx),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final p = problems[i];
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. Measures of Dispersion',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(_measureSection('Range', p.result.range.steps, _fmt(p.result.range.range)));
            widgets.add(_measureSection('Mean Deviation', p.result.meanDeviation.steps, _fmt(p.result.meanDeviation.meanDeviation)));
            widgets.add(_measureSection(
                'Standard Deviation', p.result.standardDeviation.steps, _fmt(p.result.standardDeviation.standardDeviation)));
            widgets.add(_measureSection('Coefficient of Variation', p.result.coefficientOfVariation.steps,
                '${_fmt(p.result.coefficientOfVariation.coefficientOfVariation)}%'));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildCorrelationQuestionPaper({
    required List<GeneratedCorrelationProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
  }) async {
    final theme = await _loadTheme();
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel),
        footer: (ctx) => _buildFooter(ctx),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text("Q${i + 1}. Calculate Karl Pearson's Coefficient of Correlation between X and Y:",
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
            pw.SizedBox(height: 4),
            _xyTable(problems[i].pairs),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildCorrelationAnswerKey({
    required List<GeneratedCorrelationProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
  }) async {
    final theme = await _loadTheme();
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel),
        footer: (ctx) => _buildFooter(ctx),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final p = problems[i];
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. Coefficient of Correlation', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(_measureSection(
                'Karl Pearson\'s r', p.result.steps, '${_fmt(p.result.coefficient)} — ${p.result.interpretation}'));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildIndexNumberQuestionPaper({
    required List<GeneratedIndexNumberProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
  }) async {
    final theme = await _loadTheme();
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel),
        footer: (ctx) => _buildFooter(ctx),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text('Q${i + 1}. Construct the Price Index Number (base year = 100) from the following data:',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
            pw.SizedBox(height: 4),
            _commodityTable(problems[i].commodities, problems[i].includeQuantities),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildIndexNumberAnswerKey({
    required List<GeneratedIndexNumberProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
  }) async {
    final theme = await _loadTheme();
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel),
        footer: (ctx) => _buildFooter(ctx),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final p = problems[i];
            final r = p.result;
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. Index Numbers', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(_measureSection(
                'Simple Aggregative Method', r.simpleAggregativeSteps, r.simpleAggregativeIndex.toStringAsFixed(2)));
            widgets.add(_measureSection('Simple Average of Price Relatives', r.simpleAverageSteps,
                r.simpleAveragePriceRelativeIndex.toStringAsFixed(2)));
            if (r.laspeyresIndex != null) {
              widgets.add(_measureSection("Laspeyres' Method", r.laspeyresSteps, r.laspeyresIndex!.toStringAsFixed(2)));
            }
            if (r.paascheIndex != null) {
              widgets.add(_measureSection("Paasche's Method", r.paascheSteps, r.paascheIndex!.toStringAsFixed(2)));
            }
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildRegressionQuestionPaper({
    required List<GeneratedRegressionProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
  }) async {
    final theme = await _loadTheme();
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, paperTitle, setLabel),
        footer: (ctx) => _buildFooter(ctx),
        build: (ctx) => [
          for (var i = 0; i < problems.length; i++) ...[
            pw.SizedBox(height: 10),
            pw.Text('Q${i + 1}. Find the two regression equations (Y on X and X on Y) for the following data:',
                style: pw.TextStyle(fontWeight: pw.FontWeight.bold)),
            pw.SizedBox(height: 4),
            _xyTable(problems[i].pairs),
          ],
        ],
      ),
    );
    return doc;
  }

  static Future<pw.Document> buildRegressionAnswerKey({
    required List<GeneratedRegressionProblem> problems,
    required Board board,
    required int schoolClass,
    required String paperTitle,
    String setLabel = 'Set A',
  }) async {
    final theme = await _loadTheme();
    final doc = pw.Document(theme: theme);
    doc.addPage(
      pw.MultiPage(
        pageTheme: await PdfBrandingUtil.getPageTheme(pageFormat: PdfPageFormat.a4, theme: theme),
        header: (ctx) => _buildHeader(board, schoolClass, '$paperTitle — ANSWER KEY', setLabel),
        footer: (ctx) => _buildFooter(ctx),
        build: (ctx) {
          final widgets = <pw.Widget>[];
          for (var i = 0; i < problems.length; i++) {
            final r = problems[i].result;
            widgets.add(pw.SizedBox(height: 12));
            widgets.add(pw.Text('Q${i + 1}. Regression Analysis', style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 13)));
            widgets.add(_measureSection('Regression of Y on X', r.yOnX.steps, r.yOnX.equation));
            widgets.add(_measureSection('Regression of X on Y', r.xOnY.steps, r.xOnY.equation));
            widgets.add(pw.Text('Implied r = √(byx × bxy) = ${_fmt(r.impliedR)}', style: const pw.TextStyle(fontSize: 9, fontStyle: pw.FontStyle.italic)));
          }
          return widgets;
        },
      ),
    );
    return doc;
  }

  static pw.Widget _commodityTable(List<CommodityPrice> commodities, bool includeQuantities) {
    return pw.Table(
      border: pw.TableBorder.all(width: 0.5),
      children: [
        pw.TableRow(children: [
          _cell('Commodity'),
          _cell('P0'),
          _cell('P1'),
          if (includeQuantities) _cell('Q0'),
          if (includeQuantities) _cell('Q1'),
        ]),
        for (final c in commodities)
          pw.TableRow(children: [
            _cell(c.name),
            _cell(_fmt(c.basePrice)),
            _cell(_fmt(c.currentPrice)),
            if (includeQuantities) _cell(_fmt(c.baseQuantity)),
            if (includeQuantities) _cell(_fmt(c.currentQuantity)),
          ]),
      ],
    );
  }

  static pw.Widget _xyTable(List<XYPair> pairs) {
    return pw.Table(
      border: pw.TableBorder.all(width: 0.5),
      children: [
        pw.TableRow(children: [_cell('X'), _cell('Y')]),
        for (final p in pairs) pw.TableRow(children: [_cell(_fmt(p.x)), _cell(_fmt(p.y))]),
      ],
    );
  }

  static pw.Widget _seriesTable(DataSeries series) {
    switch (series.type) {
      case SeriesType.individual:
        return pw.Wrap(
          spacing: 8,
          children: [for (final v in series.individualValues) pw.Text(_fmt(v), style: const pw.TextStyle(fontSize: 10))],
        );
      case SeriesType.discrete:
        return pw.Table(
          border: pw.TableBorder.all(width: 0.5),
          children: [
            pw.TableRow(children: [_cell('Value (X)'), _cell('Frequency (f)')]),
            for (final d in series.discreteValues) pw.TableRow(children: [_cell(_fmt(d.value)), _cell('${d.frequency}')]),
          ],
        );
      case SeriesType.continuous:
        return pw.Table(
          border: pw.TableBorder.all(width: 0.5),
          children: [
            pw.TableRow(children: [_cell('Class Interval'), _cell('Frequency (f)')]),
            for (final c in series.classIntervals)
              pw.TableRow(children: [_cell('${_fmt(c.lowerBound)} - ${_fmt(c.upperBound)}'), _cell('${c.frequency}')]),
          ],
        );
    }
  }

  static pw.Widget _cell(String text) =>
      pw.Padding(padding: const pw.EdgeInsets.all(3), child: pw.Text(text, style: const pw.TextStyle(fontSize: 9)));

  static pw.Widget _buildHeader(Board board, int schoolClass, String title, String setLabel) {
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
        pw.Text(title, style: pw.TextStyle(fontWeight: pw.FontWeight.bold, fontSize: 16), textAlign: pw.TextAlign.center),
        pw.Text('$boardLabel — Class $schoolClass — Statistics', style: const pw.TextStyle(fontSize: 11), textAlign: pw.TextAlign.center),
        pw.Divider(),
      ],
    );
  }

  static pw.Widget _buildFooter(pw.Context ctx) {
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

  static String _fmt(double v) {
    final isWhole = v == v.roundToDouble();
    return isWhole ? v.toStringAsFixed(0) : v.toStringAsFixed(2);
  }
}
