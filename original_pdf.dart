import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:flutter/services.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:printing/printing.dart';
import 'package:shine_academy_naroda/core/utils/pdf_branding_util.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PdfExportService {
  static Future<void> generateAndPrintSubject(Map<String, dynamic> subjectData) async {
    final pdf = pw.Document();

    final fontBase = await PdfGoogleFonts.notoSansRegular();
    final fontBold = await PdfGoogleFonts.notoSansBold();
    final fontTheme = pw.ThemeData.withFont(base: fontBase, bold: fontBold);

    final pageTheme = await PdfBrandingUtil.getPageTheme(
      pageFormat: PdfPageFormat.a4,
      theme: fontTheme,
    );

    final subjectName = subjectData['name'] ?? subjectData['title'] ?? 'Subject';
    final chapters = subjectData['chapters'] as List;

    for (var i = 0; i < chapters.length; i++) {
      final chapterMeta = chapters[i];
      final chapterId = chapterMeta['module_id'] ?? chapterMeta['chapter_id'] ?? chapterMeta['id'];
      
      if (chapterId == null) continue;

      try {
        final String jsonString = await rootBundle.loadString('app_core/chapters/$chapterId.json');
        final dynamic decoded = json.decode(jsonString);
        
        Map<String, dynamic> chapterData;
        if (decoded is List) {
          chapterData = {
            'metadata': {'title': 'Chapter Export'},
            'content': decoded,
            'blocks': decoded,
          };
        } else {
          chapterData = decoded as Map<String, dynamic>;
        }
        
        final metadata = chapterData['metadata'] ?? {};
        final blocks = (chapterData['content'] ?? chapterData['blocks']) as List<dynamic>? ?? [];

        pdf.addPage(
          pw.MultiPage(
            pageTheme: pageTheme,
            build: (pw.Context context) {
              return [
                // Chapter Title Header
                pw.Header(
                  level: 0,
                  child: pw.Column(
                    crossAxisAlignment: pw.CrossAxisAlignment.start,
                    children: [
                      pw.Text(
                        'Shine Academy Naroda - $subjectName',
                        style: pw.TextStyle(
                          fontSize: 14,
                          color: PdfColors.grey700,
                          fontWeight: pw.FontWeight.bold,
                        ),
                      ),
                      pw.SizedBox(height: 8),
                      pw.Text(
                        metadata['title'] ?? chapterMeta['title'] ?? 'Chapter',
                        style: pw.TextStyle(
                          fontSize: 28,
                          fontWeight: pw.FontWeight.bold,
                          color: PdfColors.indigo900,
                        ),
                      ),
                      if (metadata['subtitle'] != null) ...[
                        pw.SizedBox(height: 4),
                        pw.Text(
                          metadata['subtitle'],
                          style: pw.TextStyle(
                            fontSize: 16,
                            color: PdfColors.grey600,
                            fontStyle: pw.FontStyle.italic,
                          ),
                        ),
                      ],
                      pw.SizedBox(height: 16),
                      pw.Divider(color: PdfColors.indigo, thickness: 2),
                      pw.SizedBox(height: 24),
                    ],
                  ),
                ),
                
                // Generate content blocks
                ...blocks.map((block) => _buildPdfBlock(block)).toList(),
                
                // Footer
                pw.SizedBox(height: 40),
                pw.Divider(color: PdfColors.grey300),
                pw.SizedBox(height: 8),
                pw.Row(
                  mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
                  children: [
                    pw.Text(TrilingualService.instance.getUIText('Contact: 9408721039 | 9408154333'),
                      style: const pw.TextStyle(fontSize: 10, color: PdfColors.grey700),
                    ),
                    pw.Text(TrilingualService.instance.getUIText('Shine Academy Naroda'),
                      style: pw.TextStyle(fontSize: 10, color: PdfColors.grey500, fontStyle: pw.FontStyle.italic),
                    ),
                    pw.UrlLink(
                      destination: 'https://sites.google.com/view/shine-academy-naroda/home',
                      child: pw.Text(TrilingualService.instance.getUIText('Website: shine-academy-naroda'),
                        style: const pw.TextStyle(
                          fontSize: 10,
                          color: PdfColors.blue,
                          decoration: pw.TextDecoration.underline,
                        ),
                      ),
                    ),
                  ],
                ),
              ];
            },
          ),
        );
      } catch (e) {
        debugPrint('Error loading chapter $chapterId for PDF: $e');
        // Continue to next chapter, failing silently is acceptable as it just skips missing files
      }
    }

    final bytes = await pdf.save();
    await Printing.sharePdf(
      bytes: bytes,
      filename: '${subjectName.replaceAll(' ', '_')}_study_material.pdf',
    );
  }
  static Future<void> generateAndPrintChapter(Map<String, dynamic> metadata, List<dynamic> blocks) async {
    final pdf = pw.Document();

    // Load high-quality Unicode fonts to prevent crossed-boxes in math/science
    final fontBase = await PdfGoogleFonts.notoSansRegular();
    final fontBold = await PdfGoogleFonts.notoSansBold();
    final fontTheme = pw.ThemeData.withFont(base: fontBase, bold: fontBold);

    // Get branded page theme (logo watermark) and inject the custom font theme
    final pageTheme = await PdfBrandingUtil.getPageTheme(
      pageFormat: PdfPageFormat.a4,
      theme: fontTheme,
    );

    pdf.addPage(
      pw.MultiPage(
        pageTheme: pageTheme,
        build: (pw.Context context) {
          return [
            // Chapter Title Header
            pw.Header(
              level: 0,
              child: pw.Column(
                crossAxisAlignment: pw.CrossAxisAlignment.start,
                children: [
                  pw.Text(TrilingualService.instance.getUIText('Shine Academy Naroda'),
                    style: pw.TextStyle(
                      fontSize: 14,
                      color: PdfColors.grey700,
                      fontWeight: pw.FontWeight.bold,
                    ),
                  ),
                  pw.SizedBox(height: 8),
                  pw.Text(
                    metadata['title'] ?? 'Chapter',
                    style: pw.TextStyle(
                      fontSize: 28,
                      fontWeight: pw.FontWeight.bold,
                      color: PdfColors.indigo900,
                    ),
                  ),
                  if (metadata['subtitle'] != null) ...[
                    pw.SizedBox(height: 4),
                    pw.Text(
                      metadata['subtitle'],
                      style: pw.TextStyle(
                        fontSize: 16,
                        color: PdfColors.grey600,
                        fontStyle: pw.FontStyle.italic,
                      ),
                    ),
                  ],
                  pw.SizedBox(height: 16),
                  pw.Divider(color: PdfColors.indigo, thickness: 2),
                  pw.SizedBox(height: 24),
                ],
              ),
            ),
            
            // Generate content blocks
            ...blocks.map((block) => _buildPdfBlock(block)).toList(),
            
            // Footer
            pw.SizedBox(height: 40),
            pw.Divider(color: PdfColors.grey300),
            pw.SizedBox(height: 8),
            pw.Row(
              mainAxisAlignment: pw.MainAxisAlignment.spaceBetween,
              children: [
                pw.Text(TrilingualService.instance.getUIText('Contact: 9408721039 | 9408154333'),
                  style: const pw.TextStyle(fontSize: 10, color: PdfColors.grey700),
                ),
                pw.Text(TrilingualService.instance.getUIText('Shine Academy Naroda'),
                  style: pw.TextStyle(fontSize: 10, color: PdfColors.grey500, fontStyle: pw.FontStyle.italic),
                ),
                pw.UrlLink(
                  destination: 'https://sites.google.com/view/shine-academy-naroda/home',
                  child: pw.Text(TrilingualService.instance.getUIText('Website: shine-academy-naroda'),
                    style: const pw.TextStyle(
                      fontSize: 10,
                      color: PdfColors.blue,
                      decoration: pw.TextDecoration.underline,
                    ),
                  ),
                ),
              ],
            ),
          ];
        },
      ),
    );

    // Trigger the native share/save dialog
    final bytes = await pdf.save();
    await Printing.sharePdf(
      bytes: bytes,
      filename: '${metadata['id'] ?? 'chapter'}_study_material.pdf',
    );
  }

  static pw.Widget _buildPdfBlock(dynamic block) {
    if (block == null || block is! Map) return pw.SizedBox();
    
    final type = block['type'] ?? 'theory';
    final payload = block['data'] ?? block;
    
    switch (type) {
      case 'theory':
        return pw.Container(
          margin: const pw.EdgeInsets.only(bottom: 20),
          child: pw.Column(
            crossAxisAlignment: pw.CrossAxisAlignment.start,
            children: [
              if (payload['title'] != null)
                pw.Text(
                  payload['title'],
                  style: pw.TextStyle(
                    fontSize: 18,
                    fontWeight: pw.FontWeight.bold,
                    color: PdfColors.indigo800,
                  ),
                ),
              if (payload['title'] != null) pw.SizedBox(height: 8),
              pw.Text(
                payload['content'] ?? payload['text'] ?? '',
                style: const pw.TextStyle(
                  fontSize: 12,
                  lineSpacing: 1.5,
                ),
              ),
            ],
          ),
        );

      case 'media':
        // For media we just output the caption or a placeholder in PDF since downloading the image is tricky in this pure PDF generator.
        return pw.Container(
          margin: const pw.EdgeInsets.only(bottom: 20),
          padding: const pw.EdgeInsets.all(16),
          decoration: pw.BoxDecoration(
            color: PdfColors.grey100,
            border: pw.Border.all(color: PdfColors.grey300),
          ),
          child: pw.Center(
            child: pw.Text(
              "[ Image: ${payload['caption'] ?? 'Visual Aid'} ]",
              style: pw.TextStyle(fontSize: 10, color: PdfColors.grey600, fontStyle: pw.FontStyle.italic),
            )
          )
        );

      case 'flashcard':
        return pw.Container(
          margin: const pw.EdgeInsets.only(bottom: 20),
          padding: const pw.EdgeInsets.all(16),
          decoration: pw.BoxDecoration(
            color: PdfColors.grey100,
            border: pw.Border.all(color: PdfColors.grey400),
            borderRadius: const pw.BorderRadius.all(pw.Radius.circular(8)),
          ),
          child: pw.Column(
            crossAxisAlignment: pw.CrossAxisAlignment.start,
            children: [
              pw.Text(TrilingualService.instance.getUIText('STUDY CARD'),
                style: pw.TextStyle(
                  fontSize: 10,
                  fontWeight: pw.FontWeight.bold,
                  color: PdfColors.grey600,
                ),
              ),
              pw.SizedBox(height: 8),
              pw.Text(
                'Q: ${payload['front'] ?? ''}',
                style: pw.TextStyle(
                  fontSize: 14,
                  fontWeight: pw.FontWeight.bold,
                ),
              ),
              pw.SizedBox(height: 12),
              pw.Text(
                'A: ${payload['back'] ?? ''}',
                style: const pw.TextStyle(
                  fontSize: 12,
                  color: PdfColors.indigo900,
                ),
              ),
            ],
          ),
        );

      case 'quiz':
      case 'mcq':
        final options = payload['options'] as List<dynamic>? ?? [];
        return pw.Container(
          margin: const pw.EdgeInsets.only(bottom: 24),
          child: pw.Column(
            crossAxisAlignment: pw.CrossAxisAlignment.start,
            children: [
              pw.Text(TrilingualService.instance.getUIText('QUESTION'),
                style: pw.TextStyle(
                  fontSize: 10,
                  fontWeight: pw.FontWeight.bold,
                  color: PdfColors.grey600,
                ),
              ),
              pw.SizedBox(height: 4),
              pw.Text(
                payload['question'] ?? '',
                style: pw.TextStyle(
                  fontSize: 14,
                  fontWeight: pw.FontWeight.bold,
                ),
              ),
              pw.SizedBox(height: 8),
              ...options.map((opt) => pw.Padding(
                padding: const pw.EdgeInsets.only(bottom: 4, left: 16),
                child: pw.Text('• $opt', style: const pw.TextStyle(fontSize: 12)),
              )).toList(),
            ],
          ),
        );
        
      case 'common_mistakes':
      case 'teacher_tip':
      case 'insight':
        return pw.Container(
          margin: const pw.EdgeInsets.only(bottom: 20),
          padding: const pw.EdgeInsets.all(12),
          decoration: pw.BoxDecoration(
            color: PdfColors.amber50,
            border: pw.Border.all(color: PdfColors.amber400),
            borderRadius: const pw.BorderRadius.all(pw.Radius.circular(8)),
          ),
          child: pw.Row(
            crossAxisAlignment: pw.CrossAxisAlignment.start,
            children: [
              pw.Expanded(
                child: pw.Column(
                  crossAxisAlignment: pw.CrossAxisAlignment.start,
                  children: [
                    pw.Text(
                      type == 'common_mistakes' ? 'COMMON MISTAKE' : 'TEACHER TIP',
                      style: pw.TextStyle(
                        fontSize: 10,
                        fontWeight: pw.FontWeight.bold,
                        color: PdfColors.amber900,
                      ),
                    ),
                    pw.SizedBox(height: 4),
                    pw.Text(
                      payload['content'] ?? payload['text'] ?? '',
                      style: pw.TextStyle(
                        fontSize: 12,
                        color: PdfColors.amber900,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        );

      case 'animated_diagram':
        final paths = payload['paths'] as List<dynamic>? ?? [];
        final strokeColor = payload['stroke_color'] ?? '#000000';
        
        // Construct a standard SVG string from the path data
        String svgPaths = '';
        for (var p in paths) {
          svgPaths += '<path d="$p" stroke="$strokeColor" fill="none" stroke-width="2"/>';
        }
        
        final svgString = '''
          <svg viewBox="0 0 400 300" xmlns="http://www.w3.org/2000/svg">
            $svgPaths
          </svg>
        ''';

        return pw.Container(
          margin: const pw.EdgeInsets.only(bottom: 20),
          padding: const pw.EdgeInsets.all(16),
          decoration: pw.BoxDecoration(
            border: pw.Border.all(color: PdfColors.grey300),
            borderRadius: const pw.BorderRadius.all(pw.Radius.circular(8)),
          ),
          child: pw.Column(
            crossAxisAlignment: pw.CrossAxisAlignment.center,
            children: [
              if (payload['title'] != null)
                pw.Text(
                  payload['title'],
                  style: pw.TextStyle(
                    fontSize: 14,
                    fontWeight: pw.FontWeight.bold,
                    color: PdfColors.indigo,
                  ),
                ),
              pw.SizedBox(height: 16),
              pw.SizedBox(
                height: 200,
                child: pw.SvgImage(svg: svgString),
              ),
              if (payload['description'] != null) ...[
                pw.SizedBox(height: 16),
                pw.Text(
                  payload['description'],
                  style: pw.TextStyle(fontSize: 10, color: PdfColors.grey600),
                  textAlign: pw.TextAlign.center,
                ),
              ]
            ],
          ),
        );

      case 'dictionary_link':
        final preview = payload['preview'] ?? payload['term_id'] ?? 'Vocabulary Term';
        return pw.Container(
          margin: const pw.EdgeInsets.only(bottom: 16),
          padding: const pw.EdgeInsets.all(8),
          decoration: pw.BoxDecoration(
            color: PdfColors.blue50,
            borderRadius: const pw.BorderRadius.all(pw.Radius.circular(4)),
            border: pw.Border.all(color: PdfColors.blue200),
          ),
          child: pw.Row(
            children: [
              pw.Text(TrilingualService.instance.getUIText('DICTIONARY: '),
                style: pw.TextStyle(
                  fontSize: 10,
                  fontWeight: pw.FontWeight.bold,
                  color: PdfColors.blue900,
                ),
              ),
              pw.Text(
                preview,
                style: pw.TextStyle(
                  fontSize: 12,
                  fontWeight: pw.FontWeight.bold,
                  color: PdfColors.blue700,
                ),
              ),
            ]
          )
        );

      case 'memory_trick':
        return pw.Container(
          margin: const pw.EdgeInsets.only(bottom: 20),
          padding: const pw.EdgeInsets.all(12),
          decoration: pw.BoxDecoration(
            color: PdfColors.purple50,
            border: pw.Border.all(color: PdfColors.purple400),
            borderRadius: const pw.BorderRadius.all(pw.Radius.circular(8)),
          ),
          child: pw.Row(
            crossAxisAlignment: pw.CrossAxisAlignment.start,
            children: [
              pw.Expanded(
                child: pw.Column(
                  crossAxisAlignment: pw.CrossAxisAlignment.start,
                  children: [
                    pw.Text(TrilingualService.instance.getUIText('MEMORY TRICK'),
                      style: pw.TextStyle(
                        fontSize: 10,
                        fontWeight: pw.FontWeight.bold,
                        color: PdfColors.purple900,
                      ),
                    ),
                    pw.SizedBox(height: 4),
                    pw.Text(
                      payload['content'] ?? payload['text'] ?? '',
                      style: pw.TextStyle(
                        fontSize: 12,
                        color: PdfColors.purple900,
                      ),
                    ),
                  ],
                ),
              ),
            ],
          ),
        );

      default:
        // Fallback for unknown block types
        final fallbackContent = payload['content'] ?? payload['text'];
        if (fallbackContent != null) {
          return pw.Container(
            margin: const pw.EdgeInsets.only(bottom: 16),
            child: pw.Text(
              fallbackContent.toString(),
              style: const pw.TextStyle(fontSize: 12),
            ),
          );
        }
        return pw.SizedBox();
    }
  }
}
