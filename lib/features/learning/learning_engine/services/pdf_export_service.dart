import 'dart:io';
import 'dart:convert';
import 'package:flutter/foundation.dart';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:pdf/pdf.dart';
import 'package:pdf/widgets.dart' as pw;
import 'package:printing/printing.dart';
import 'package:shine_academy_naroda/core/utils/pdf_branding_util.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/core/utils/pdf_viewer_util.dart';
import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';
import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';

class PdfExportService {
  static Future<void> generateAndPrintSubject(Map<String, dynamic> subjectData) async {
    final pdf = pw.Document();

final baseData = await rootBundle.load('assets/fonts/DejaVuSans.ttf');
    final fontBase = pw.Font.ttf(baseData);
    final boldData = await rootBundle.load('assets/fonts/DejaVuSans-Bold.ttf');
    final fontBold = pw.Font.ttf(boldData);
    
    final gujData = await rootBundle.load('assets/fonts/NotoSansGujarati-Regular.ttf');
    final gujFont = pw.Font.ttf(gujData);
    final hinData = await rootBundle.load('assets/fonts/NotoSansDevanagari-Regular.ttf');
    final hinFont = pw.Font.ttf(hinData);

    final fontTheme = pw.ThemeData.withFont(
      base: fontBase, 
      bold: fontBold,
      fontFallback: [gujFont, hinFont]
    );

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
                ...blocks.map((block) => _buildPdfBlock(block)),
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
      }
    }

    final bytes = await pdf.save();
    await Printing.sharePdf(
      bytes: bytes,
      filename: '${subjectName.replaceAll(' ', '_')}_study_material.pdf',
    );
  }


  static Future<void> generateAndPrintChapter(
      BuildContext context,
      Map<String, dynamic> metadata,
      List<dynamic> blocks,
      {String? studentName}) async {
    ValueNotifier<int> progressNotifier = ValueNotifier<int>(0);
    BuildContext? dialogCtx;

    try {
      final title = metadata['title'] ?? 'Chapter Study Material';
      final validBlocks = blocks.whereType<Map>().toList();
      
      if (context.mounted) {
        showDialog(
          context: context,
          barrierDismissible: false,
          builder: (ctx) {
            dialogCtx = ctx;
            return AlertDialog(
              title: Text(TrilingualService.instance.getUIText('Generating PDF')),
              content: ValueListenableBuilder<int>(
                valueListenable: progressNotifier,
                builder: (context, currentBlock, child) {
                  return Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      const CircularProgressIndicator(),
                      const SizedBox(height: 16),
                      Text('${TrilingualService.instance.getUIText('Processing component')} $currentBlock'),
                      const SizedBox(height: 8),
                      Text(TrilingualService.instance.getUIText('Please wait. High quality rendering takes time...'),
                        style: const TextStyle(fontSize: 12, color: Colors.grey),
                        textAlign: TextAlign.center,
                      ),
                    ],
                  );
                }
              ),
            );
          }
        );
      }

      List<Widget> flutterWidgets = [];
      for (int i = 0; i < validBlocks.length; i++) {
        final block = validBlocks[i];
        progressNotifier.value = i + 1;
        
        await Future.delayed(const Duration(milliseconds: 2));
        flutterWidgets.addAll(await _buildFlutterWidgets(block));
      }

      final bytes = await UniversalPdfEngine.generatePdfBytesFromWidgets(
        title: title,
        widgets: flutterWidgets,
        isAnswerKey: false,
        onProgress: (current, total) {
           progressNotifier.value = (validBlocks.length) + current;
        }
      );

      if (dialogCtx != null && dialogCtx!.mounted) {
        Navigator.of(dialogCtx!).pop();
        dialogCtx = null;
      }

      await PdfViewerUtil.openPdfBytes(bytes, '${metadata['id'] ?? 'chapter'}_study_material.pdf');
    } catch (e, stack) {
      if (dialogCtx != null && dialogCtx!.mounted) {
        Navigator.of(dialogCtx!).pop();
      }
      debugPrint('PDF Error: $e');
      debugPrint(stack.toString());
      rethrow;
    }
  }

  static Future<List<Widget>> _buildFlutterWidgets(Map block) async {
    final type = block['type']?.toString() ?? 'unknown';
    final payload = block.containsKey('content') && block['content'] is Map 
        ? block['content'] as Map 
        : block;

    final title = _getTitle(payload);
    List<Widget> widgets = [];

    switch (type) {
      case 'theory':
      case 'hook':
      case 'discovery':
      case 'short_note':
      case 'text':
        if (title != null) {
          widgets.add(
            Padding(
              padding: const EdgeInsets.only(bottom: 8, top: 12),
              child: Text(
                title,
                style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: Color(0xFF0D47A1)),
              ),
            )
          );
        }
        final body = _getLoc(payload, ['body', 'content', 'text']);
        widgets.addAll(_buildParagraphs(body));
        
        final imageWidget = await _buildFlutterImage(payload);
        if (imageWidget != null) {
          widgets.add(const SizedBox(height: 8));
          widgets.add(imageWidget);
        }
        
        widgets.add(const SizedBox(height: 16));
        return widgets;

      case 'socratic':
      case 'mcq':
      case 'numerical':
      case 'quiz':
      case 'practice_question':
      case 'board_questions':
      case 'knowledge_check':
        widgets.add(const SizedBox(height: 12));
        widgets.add(
          const Text('QUESTION', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.grey))
        );
        widgets.add(const SizedBox(height: 4));
        widgets.add(
          TtsInteractiveText(text: _getLoc(payload, ['question']), style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14))
        );
        widgets.add(const SizedBox(height: 8));

        final options = _getLocList(payload, ['options']);
        if (options.isNotEmpty) {
          for (var opt in options) {
            widgets.add(
              Padding(
                padding: const EdgeInsets.only(left: 16, bottom: 4),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    const Text('• ', style: TextStyle(fontSize: 12)),
                    Expanded(child: TtsInteractiveText(text: opt.toString(), style: const TextStyle(fontSize: 14))),
                  ],
                ),
              )
            );
          }
        }

        final solution = _getLoc(payload, ['solution', 'answer', 'explanation']);
        if (solution.isNotEmpty) {
          widgets.add(const SizedBox(height: 12));
          widgets.add(
            const Text('SOLUTION / ANSWER', style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.green))
          );
          widgets.add(const SizedBox(height: 4));
          widgets.addAll(_buildParagraphs(solution));
        }
        widgets.add(const SizedBox(height: 24));
        return widgets;

      case 'common_mistakes':
      case 'teacher_tip':
      case 'insight':
      case 'memory_trick':
        final label = type == 'common_mistakes' ? 'COMMON MISTAKE' : (type == 'memory_trick' ? 'MEMORY TRICK' : 'TEACHER TIP');
        final color = type == 'memory_trick' ? Colors.purple[900]! : Colors.amber[900]!;
        
        widgets.add(const SizedBox(height: 12));
        widgets.add(
          Text(label, style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: color))
        );
        widgets.add(const SizedBox(height: 4));
        widgets.addAll(_buildParagraphs(_getLoc(payload, ['content', 'text']), textColor: color));
        widgets.add(const SizedBox(height: 24));
        return widgets;

      default:
        final fallbackContent = _getLoc(payload, ['body', 'content', 'text', 'question']);
        if (fallbackContent.isNotEmpty) {
          if (title != null) {
            widgets.add(
              Padding(
                padding: const EdgeInsets.only(bottom: 8, top: 12),
                child: Text(
                  title,
                  style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.black87),
                ),
              )
            );
          }
          widgets.addAll(_buildParagraphs(fallbackContent));
        }
        
        final defImageWidget = await _buildFlutterImage(payload);
        if (defImageWidget != null) {
          widgets.add(const SizedBox(height: 8));
          widgets.add(defImageWidget);
        }
        
        if (fallbackContent.isNotEmpty || defImageWidget != null) {
          widgets.add(const SizedBox(height: 16));
        }
        return widgets;
    }
  }

  static List<Widget> _buildParagraphs(String text, {Color? textColor}) {
    final paragraphs = text.split('\n\n');
    List<Widget> widgets = [];
    for (var p in paragraphs) {
      if (p.trim().isEmpty) continue;
      final lines = p.split('\n');
      for (var line in lines) {
         if(line.trim().isEmpty) continue;
         widgets.add(
           Padding(
             padding: const EdgeInsets.only(bottom: 4),
             child: TtsInteractiveText(text: line, style: TextStyle(fontSize: 14, color: textColor ?? Colors.black87)),
           )
         );
      }
      widgets.add(const SizedBox(height: 8));
    }
    return widgets;
  }

  static Future<Widget?> _buildFlutterImage(Map payload) async {
    final imageUrl = payload['image_url'] ?? (payload['visuals'] != null ? payload['visuals']['image_url'] : null) ?? payload['path'];
    if (imageUrl != null && imageUrl.toString().isNotEmpty) {
      try {
        Uint8List imageBytes;
        if (imageUrl.toString().startsWith('/')) {
           imageBytes = File(imageUrl.toString()).readAsBytesSync();
        } else {
           final ByteData data = await rootBundle.load(imageUrl.toString());
           imageBytes = data.buffer.asUint8List();
        }
        final imageWidget = Center(child: Image.memory(imageBytes, height: 200, fit: BoxFit.contain));
        
        final caption = _getLoc(payload, ['caption']);
        if (caption.isNotEmpty) {
          return Column(
            children: [
              imageWidget,
              const SizedBox(height: 4),
              Center(
                child: Text(caption, style: const TextStyle(fontSize: 10, color: Colors.grey, fontStyle: FontStyle.italic))
              ),
            ]
          );
        }
        return imageWidget;
      } catch (e) {
        debugPrint('Error loading image $imageUrl for PDF: $e');
      }
    }
    return null;
  }

  
  static String _getLoc(Map payload, List<String> baseKeys) {
    final lang = TrilingualService.instance.activeViewLanguage;
    for (final key in baseKeys) {
      if (lang != 'en') {
        final locKey = '${key}_$lang';
        if (payload[locKey] != null && payload[locKey].toString().isNotEmpty) {
          return payload[locKey].toString();
        }
      }
      if (payload[key] != null && payload[key].toString().isNotEmpty) {
        return payload[key].toString();
      }
    }
    return '';
  }

  static List<dynamic> _getLocList(Map payload, List<String> baseKeys) {
    final lang = TrilingualService.instance.activeViewLanguage;
    for (final key in baseKeys) {
      if (lang != 'en') {
        final locKey = '${key}_$lang';
        if (payload[locKey] != null && payload[locKey] is List && (payload[locKey] as List).isNotEmpty) {
          return payload[locKey] as List;
        }
      }
      if (payload[key] != null && payload[key] is List) {
        return payload[key] as List;
      }
    }
    return [];
  }

  static String? _getTitle(Map payload) {
    final lang = TrilingualService.instance.activeViewLanguage;
    if (lang != 'en') {
      final locKey = 'title_$lang';
      if (payload[locKey] != null && payload[locKey].toString().isNotEmpty) {
        return payload[locKey].toString();
      }
    }
    return payload['title']?.toString();
  }

  // Kept for backward compatibility with generateAndPrintSubject
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
              )),
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
