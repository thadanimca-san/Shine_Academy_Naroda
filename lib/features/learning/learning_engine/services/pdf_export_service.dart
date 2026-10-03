import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:printing/printing.dart';
import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/core/utils/pdf_viewer_util.dart';
import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';

class PdfExportService {
  // ──────────────────────────────────────────────────────────────────────────
  // generateAndPrintSubject  (subject-level export — kept for compatibility)
  // ──────────────────────────────────────────────────────────────────────────
  static Future<void> generateAndPrintSubject(
      Map<String, dynamic> subjectData) async {
    final subjectName =
        subjectData['name'] ?? subjectData['title'] ?? 'Subject';
    final chapters = subjectData['chapters'] as List;

    List<Widget> allWidgets = [];

    for (var i = 0; i < chapters.length; i++) {
      final chapterMeta = chapters[i];
      final chapterId = chapterMeta['module_id'] ??
          chapterMeta['chapter_id'] ??
          chapterMeta['id'];
      if (chapterId == null) continue;

      try {
        final String jsonString =
            await rootBundle.loadString('app_core/chapters/$chapterId.json');
        final dynamic decoded = json.decode(jsonString);

        Map<String, dynamic> chapterData;
        if (decoded is List) {
          chapterData = {
            'metadata': {'title': 'Chapter Export'},
            'blocks': decoded,
          };
        } else {
          chapterData = decoded as Map<String, dynamic>;
        }

        final metadata = chapterData['metadata'] ?? {};
        final blocks = (chapterData['content'] ?? chapterData['blocks'])
                as List<dynamic>? ??
            [];
        final chapterTitle =
            metadata['title'] ?? chapterMeta['title'] ?? 'Chapter';

        // Chapter heading widget
        allWidgets.add(_chapterHeadingWidget(subjectName, chapterTitle));
        allWidgets.add(const SizedBox(height: 8));

        for (final block in blocks) {
          if (block is! Map) continue;
          final w = _buildFlutterBlock(block as Map<String, dynamic>);
          if (w != null) allWidgets.add(w);
        }

        allWidgets.add(const SizedBox(height: 32));
        allWidgets.add(const Divider());
        allWidgets.add(const SizedBox(height: 8));
      } catch (e) {
        debugPrint('Error loading chapter $chapterId for PDF: $e');
      }
    }

    final bytes = await UniversalPdfEngine.generatePdfBytesFromWidgets(
      title: subjectName,
      widgets: allWidgets,
    );
    await Printing.sharePdf(
      bytes: bytes,
      filename: '${subjectName.replaceAll(' ', '_')}_study_material.pdf',
    );
  }

  // ──────────────────────────────────────────────────────────────────────────
  // generateAndPrintChapter  (single chapter export — the one used in app)
  // ──────────────────────────────────────────────────────────────────────────
  static Future<void> generateAndPrintChapter(
    BuildContext context,
    Map<String, dynamic> metadata,
    List<dynamic> blocks, {
    String? studentName,
  }) async {
    final title = metadata['title'] ?? 'Chapter Study Material';
    ValueNotifier<int> progressNotifier = ValueNotifier<int>(0);
    BuildContext? dialogCtx;

    try {
      if (context.mounted) {
        showDialog(
          context: context,
          barrierDismissible: false,
          builder: (ctx) {
            dialogCtx = ctx;
            return AlertDialog(
              title: Text(
                  TrilingualService.instance.getUIText('Generating PDF')),
              content: ValueListenableBuilder<int>(
                valueListenable: progressNotifier,
                builder: (context, cur, _) {
                  final total = blocks.whereType<Map>().length;
                  return Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      const CircularProgressIndicator(),
                      const SizedBox(height: 16),
                      Text(
                          '${TrilingualService.instance.getUIText('Processing block')} $cur / $total'),
                      const SizedBox(height: 8),
                      Text(
                        TrilingualService.instance.getUIText(
                            'Please wait. Formatting document...'),
                        style: const TextStyle(
                            fontSize: 12, color: Colors.grey),
                        textAlign: TextAlign.center,
                      ),
                    ],
                  );
                },
              ),
            );
          },
        );
      }

      // Build Flutter widgets for each block
      List<Widget> flutterWidgets = [];
      final validBlocks = blocks.whereType<Map>().toList();

      for (int i = 0; i < validBlocks.length; i++) {
        progressNotifier.value = i + 1;
        await Future.delayed(const Duration(milliseconds: 2));

        final block = validBlocks[i] as Map<String, dynamic>;
        final w = _buildFlutterBlock(block);
        if (w != null) flutterWidgets.add(w);
      }

      if (dialogCtx != null && dialogCtx!.mounted) {
        Navigator.of(dialogCtx!).pop();
        dialogCtx = null;
      }

      final bytes = await UniversalPdfEngine.generatePdfBytesFromWidgets(
        title: title,
        widgets: flutterWidgets,
      );

      await PdfViewerUtil.openPdfBytes(
          bytes, '${metadata['id'] ?? 'chapter'}_study_material.pdf');
    } catch (e, stack) {
      if (dialogCtx != null && dialogCtx!.mounted) {
        Navigator.of(dialogCtx!).pop();
      }
      debugPrint('PDF Error: $e');
      debugPrint(stack.toString());
      rethrow;
    }
  }

  // ──────────────────────────────────────────────────────────────────────────
  // Flutter widget builders
  // All text goes through TtsInteractiveText which:
  //   • uses NotoSansGujarati (loaded via FontLoader in UniversalPdfEngine)
  //   • parses $...$ LaTeX markers and renders them via flutter_math_fork
  // ──────────────────────────────────────────────────────────────────────────

  static Widget _chapterHeadingWidget(String subject, String chapterTitle) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          TtsInteractiveText(
            text: 'Shine Academy Naroda — $subject',
            style: const TextStyle(
                fontSize: 13,
                color: Colors.grey,
                fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 6),
          TtsInteractiveText(
            text: chapterTitle,
            style: const TextStyle(
                fontSize: 24,
                fontWeight: FontWeight.bold,
                color: Color(0xFF1A237E)),
          ),
          const SizedBox(height: 10),
          const Divider(thickness: 2, color: Color(0xFF3949AB)),
          const SizedBox(height: 16),
        ],
      ),
    );
  }

  /// Returns a Flutter [Widget] that renders a single content block.
  /// Returns null for blocks that should be silently skipped.
  static Widget? _buildFlutterBlock(Map<String, dynamic> block) {
    final type = block['type']?.toString() ?? 'unknown';
    final payload = (block.containsKey('content') && block['content'] is Map)
        ? block['content'] as Map<String, dynamic>
        : block;

    final title = _getTitle(payload);
    final body = _getLoc(payload, ['body', 'content', 'text']);
    final question = _getLoc(payload, ['question']);
    final solution = _getLoc(payload, ['solution', 'answer', 'explanation']);
    final options = _getLocList(payload, ['options']);

    switch (type) {
      // ── Theory / reading blocks ────────────────────────────────────────
      case 'theory':
      case 'hook':
      case 'discovery':
      case 'short_note':
      case 'text':
      case 'reveal':
      case 'reflection':
      case 'connection':
      case 'mastery':
        return Padding(
          padding: const EdgeInsets.only(bottom: 14),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              if (title != null) ...[
                TtsInteractiveText(
                  text: title,
                  style: const TextStyle(
                      fontSize: 16,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFF0D47A1)),
                ),
                const SizedBox(height: 6),
              ],
              if (body.isNotEmpty)
                TtsInteractiveText(
                  text: body,
                  style: const TextStyle(fontSize: 13, color: Colors.black87),
                ),
            ],
          ),
        );

      // ── Question / MCQ blocks ──────────────────────────────────────────
      case 'socratic':
      case 'mcq':
      case 'numerical':
      case 'quiz':
      case 'practice_question':
      case 'board_questions':
      case 'knowledge_check':
        return Padding(
          padding: const EdgeInsets.only(bottom: 20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text('QUESTION',
                  style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.bold,
                      color: Colors.grey)),
              const SizedBox(height: 4),
              if (question.isNotEmpty)
                TtsInteractiveText(
                  text: question,
                  style: const TextStyle(
                      fontSize: 13, fontWeight: FontWeight.bold),
                ),
              const SizedBox(height: 6),
              ...options.map((opt) => Padding(
                    padding: const EdgeInsets.only(left: 12, bottom: 3),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        const Text('• ',
                            style: TextStyle(fontSize: 13)),
                        Expanded(
                          child: TtsInteractiveText(
                            text: opt.toString(),
                            style: const TextStyle(fontSize: 13),
                          ),
                        ),
                      ],
                    ),
                  )),
              if (solution.isNotEmpty) ...[
                const SizedBox(height: 10),
                const Text('SOLUTION / ANSWER',
                    style: TextStyle(
                        fontSize: 11,
                        fontWeight: FontWeight.bold,
                        color: Colors.green)),
                const SizedBox(height: 4),
                TtsInteractiveText(
                  text: solution,
                  style:
                      const TextStyle(fontSize: 13, color: Colors.black87),
                ),
              ],
            ],
          ),
        );

      // ── Teacher tip / Common mistakes ──────────────────────────────────
      case 'teacher_tip':
      case 'common_mistakes':
      case 'insight':
      case 'memory_trick':
        final isError = type == 'common_mistakes';
        final isTrick = type == 'memory_trick';
        final label = isError
            ? 'COMMON MISTAKE'
            : isTrick
                ? 'MEMORY TRICK'
                : 'TEACHER TIP';
        final bgColor = isError
            ? const Color(0xFFFFF3E0)
            : isTrick
                ? const Color(0xFFF3E5F5)
                : const Color(0xFFFFF8E1);
        final borderColor = isError
            ? const Color(0xFFF57C00)
            : isTrick
                ? const Color(0xFF7B1FA2)
                : const Color(0xFFF9A825);
        final textColor = isError
            ? const Color(0xFFE65100)
            : isTrick
                ? const Color(0xFF4A148C)
                : const Color(0xFF795548);

        final tipBody = _getLoc(payload, ['content', 'text', 'body']);

        return Container(
          margin: const EdgeInsets.only(bottom: 14),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: bgColor,
            border: Border.all(color: borderColor),
            borderRadius: BorderRadius.circular(6),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text(label,
                  style: TextStyle(
                      fontSize: 11,
                      fontWeight: FontWeight.bold,
                      color: borderColor)),
              const SizedBox(height: 4),
              if (tipBody.isNotEmpty)
                TtsInteractiveText(
                    text: tipBody,
                    style: TextStyle(fontSize: 13, color: textColor)),
            ],
          ),
        );

      // ── Flashcard ──────────────────────────────────────────────────────
      case 'flashcard':
        final front = _getLoc(payload, ['front', 'question']);
        final back = _getLoc(payload, ['back', 'answer']);
        return Container(
          margin: const EdgeInsets.only(bottom: 14),
          padding: const EdgeInsets.all(10),
          decoration: BoxDecoration(
            color: const Color(0xFFF5F5F5),
            border: Border.all(color: Colors.grey),
            borderRadius: BorderRadius.circular(6),
          ),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text('STUDY CARD',
                  style: TextStyle(
                      fontSize: 10,
                      fontWeight: FontWeight.bold,
                      color: Colors.grey)),
              const SizedBox(height: 6),
              if (front.isNotEmpty)
                TtsInteractiveText(
                    text: 'Q: $front',
                    style: const TextStyle(
                        fontSize: 13, fontWeight: FontWeight.bold)),
              const SizedBox(height: 8),
              if (back.isNotEmpty)
                TtsInteractiveText(
                    text: 'A: $back',
                    style: const TextStyle(
                        fontSize: 13, color: Color(0xFF1A237E))),
            ],
          ),
        );

      // ── Dictionary link ────────────────────────────────────────────────
      case 'dictionary_link':
        final preview =
            payload['preview'] ?? payload['term_id'] ?? 'Vocabulary Term';
        return Container(
          margin: const EdgeInsets.only(bottom: 10),
          padding: const EdgeInsets.symmetric(horizontal: 10, vertical: 6),
          decoration: BoxDecoration(
            color: const Color(0xFFE3F2FD),
            borderRadius: BorderRadius.circular(4),
            border: Border.all(color: const Color(0xFF90CAF9)),
          ),
          child: Row(
            children: [
              const Text('DICTIONARY: ',
                  style: TextStyle(
                      fontSize: 10,
                      fontWeight: FontWeight.bold,
                      color: Color(0xFF0D47A1))),
              TtsInteractiveText(
                text: preview.toString(),
                style: const TextStyle(
                    fontSize: 13,
                    fontWeight: FontWeight.bold,
                    color: Color(0xFF1565C0)),
              ),
            ],
          ),
        );

      // ── Animated diagram — show placeholder ───────────────────────────
      case 'animated_diagram':
      case 'media':
        final caption = payload['caption'] ?? payload['title'] ?? 'Diagram';
        return Container(
          margin: const EdgeInsets.only(bottom: 14),
          padding: const EdgeInsets.all(14),
          decoration: BoxDecoration(
            color: const Color(0xFFF5F5F5),
            border: Border.all(color: Colors.grey[300]!),
            borderRadius: BorderRadius.circular(6),
          ),
          child: Center(
            child: Text('[ Diagram: $caption ]',
                style: const TextStyle(
                    fontSize: 11, color: Colors.grey)),
          ),
        );

      default:
        final fallback =
            _getLoc(payload, ['body', 'content', 'text', 'question']);
        if (fallback.isEmpty) return null;
        return Padding(
          padding: const EdgeInsets.only(bottom: 12),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              if (title != null) ...[
                TtsInteractiveText(
                  text: title,
                  style: const TextStyle(
                      fontSize: 15, fontWeight: FontWeight.bold),
                ),
                const SizedBox(height: 4),
              ],
              TtsInteractiveText(
                text: fallback,
                style: const TextStyle(fontSize: 13),
              ),
            ],
          ),
        );
    }
  }

  // ──────────────────────────────────────────────────────────────────────────
  // Helpers
  // ──────────────────────────────────────────────────────────────────────────

  static String _getLoc(Map payload, List<String> baseKeys) {
    final lang = TrilingualService.instance.activeViewLanguage;
    for (final key in baseKeys) {
      if (lang != 'en') {
        final locKey = '${key}_$lang';
        if (payload[locKey] != null &&
            payload[locKey].toString().isNotEmpty) {
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
        if (payload[locKey] != null &&
            payload[locKey] is List &&
            (payload[locKey] as List).isNotEmpty) {
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
      if (payload[locKey] != null &&
          payload[locKey].toString().isNotEmpty) {
        return payload[locKey].toString();
      }
    }
    return payload['title']?.toString();
  }
}
