import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:go_router/go_router.dart';
import '../../../../core/engine/pedagogy_engine.dart';
import '../../../../core/engine/block_validator.dart';
import '../../../../core/engine/block_registry.dart';
import '../../../../core/engine/curriculum_database.dart';
import '../../../../core/engine/local_content_manager.dart';
import '../../../../foundation/theme/app_colors.dart';
import '../../../foundation/theme/brand_app_bar.dart';
import '../ai_tutor/ai_tutor_screen.dart';
import 'services/pdf_export_service.dart';
import 'widgets/universal_block_wrapper.dart';
import 'widgets/dictionary_term_widget.dart';
import '../../../core/services/presentation_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../core/engine/content_repository.dart';
import 'lesson_revision.dart';
import 'widgets/chapter_finish_card.dart';

class LearningEngineScreen extends StatefulWidget {
  final String moduleId;
  final String title;
  final bool isPremium;

  const LearningEngineScreen({
    super.key,
    required this.moduleId,
    required this.title,
    this.isPremium = false,
  });

  @override
  State<LearningEngineScreen> createState() => _LearningEngineScreenState();
}

class _LearningEngineScreenState extends State<LearningEngineScreen> {
  Map<String, dynamic>? _metadata;
  List<dynamic> _blocks = [];
  List<dynamic> _standardBlocks = [];
  List<dynamic> _boardBlocks = [];
  bool _isLoading = true;
  String _error = '';
  bool _showDictionaryHint = true;
  bool _showBoardQuestions = false;

  /// New-format chapters carry teacher-checked translations, so they are
  /// never machine-translated at runtime.
  bool _isNewFormat = false;

  /// Quick Revision shows only the summary-type blocks of the lesson.
  bool _revisionMode = false;

  void _setRevisionMode(bool on) {
    setState(() {
      _revisionMode = on;
      _blocks = on
          ? revisionBlocks(_standardBlocks)
          : (_showBoardQuestions ? [..._standardBlocks, ..._boardBlocks] : _standardBlocks);
    });
    if (_scrollController.hasClients) _scrollController.jumpTo(0);
  }
  late String _lastLang;

  // Phase 6: Smart Panel Remote Control Support
  final ScrollController _scrollController = ScrollController();
  final FocusNode _focusNode = FocusNode();

  @override
  void initState() {
    super.initState();
    _lastLang = TrilingualService.instance.activeViewLanguage;
    TrilingualService.instance.addListener(_onLanguageChanged);
    _loadModule();
    // Request focus automatically so the remote works instantly
    WidgetsBinding.instance.addPostFrameCallback((_) {
      _focusNode.requestFocus();
    });
  }

  @override
  void dispose() {
    _scrollController.dispose();
    _focusNode.dispose();
    TrilingualService.instance.removeListener(_onLanguageChanged);
    super.dispose();
  }

  void _onLanguageChanged() {
    final currentLang = TrilingualService.instance.activeViewLanguage;
    if (_lastLang != currentLang) {
      _lastLang = currentLang;
      if (currentLang != 'en') {
        _translateBlocks();
      } else {
        if (mounted) setState(() {});
      }
    }
  }

  Future<void> _translateBlocks() async {
    if (!mounted) return;
    if (_isNewFormat) {
      setState(() {});
      return;
    }
    await TrilingualService.instance.preTranslateBlocks(
      _blocks,
      isDictionary: widget.moduleId.contains('DICT'),
    );

    if (!mounted) return;
    setState(() {});
  }

  Future<void> _loadModule() async {
    try {
      await LocalContentManager.instance.init();

      if (widget.moduleId.contains('DICT')) {
        final termString = await rootBundle.loadString(
          'app_core/knowledge_graph/dictionary/${widget.moduleId}.json',
        );
        setState(() {
          _metadata = json.decode(termString);
          _blocks = [];
          _isLoading = false;
        });
      } else {
        Map<String, dynamic> _normalizeData(dynamic rawData) {
          if (rawData is List) {
            return {
              'metadata': {'title': 'Chapter'},
              'content': rawData,
              'blocks': rawData,
            };
          } else if (rawData is Map) {
            return rawData as Map<String, dynamic>;
          }
          return {};
        }

        // ── Priority 0: New content format (app_core/content/) ────────────────
        final newFormatChapter = await ContentRepository.instance.loadChapter(widget.moduleId);
        if (newFormatChapter != null) {
          final rawBlocks = newFormatChapter.blocks;
          setState(() {
            _isNewFormat = true;
            _metadata = newFormatChapter.metadata;
            _standardBlocks = rawBlocks.where((b) => b['is_board_challenge'] != true).toList();
            _boardBlocks = rawBlocks.where((b) => b['is_board_challenge'] == true).toList();
            _blocks = _showBoardQuestions ? rawBlocks : _standardBlocks;
            _isLoading = false;
          });
          return;
        }

        // ── Priority 1: Check LocalContentManager (catches editor-saved changes) ──
        final chapterAssetPath = 'app_core/chapters/${widget.moduleId}.json';
        dynamic rawFileData = await LocalContentManager.instance.readLocalJson(
          chapterAssetPath,
        );

        // ── Priority 2: Fall back to bundled asset ────────────────────────────
        if (rawFileData == null) {
          try {
            final String fileString = await rootBundle.loadString(
              chapterAssetPath,
            );
            rawFileData = jsonDecode(fileString);
          } catch (_) {
            // Chapter file doesn't exist at all
          }
        }

        Map<String, dynamic>? fileData = rawFileData != null
            ? _normalizeData(rawFileData)
            : null;

        if (fileData != null) {
          final metaData =
              (fileData['metadata'] as Map<String, dynamic>?) ?? {};
          final rawBlocks = (fileData['blocks'] as List<dynamic>?) ?? [];

          final pedagogyReport = PedagogyEngine.validateChapterFlow(rawBlocks);
          if (!pedagogyReport.isValid) {
            debugPrint(
              'PEDAGOGY WARNING: Chapter ${widget.moduleId} is missing: '
              '${pedagogyReport.missingComponents.join(', ')}',
            );
          }

          setState(() {
            _metadata = metaData;
            _standardBlocks = rawBlocks
                .where((b) => b['is_board_challenge'] != true)
                .toList();
            _boardBlocks = rawBlocks
                .where((b) => b['is_board_challenge'] == true)
                .toList();
            _blocks = _showBoardQuestions ? rawBlocks : _standardBlocks;
            _isLoading = false;
          });
          return; // Successfully loaded chapter!
        }

        // ── Priority 3: Fall back to in-memory CurriculumDatabase ─────────────
        if (CurriculumDatabase.instance.hasModule(widget.moduleId)) {
          final metaData = CurriculumDatabase.instance.getModuleMetadata(
            widget.moduleId,
          );
          final rawBlocks = CurriculumDatabase.instance.getModuleBlocks(
            widget.moduleId,
          );

          if (rawBlocks == null) {
            throw Exception('Module blocks not found in database.');
          }

          final pedagogyReport = PedagogyEngine.validateChapterFlow(rawBlocks);
          if (!pedagogyReport.isValid) {
            debugPrint(
              'PEDAGOGY WARNING: Chapter ${widget.moduleId} is missing: '
              '${pedagogyReport.missingComponents.join(', ')}',
            );
          }

          setState(() {
            _metadata = metaData ?? {};
            _standardBlocks = rawBlocks
                .where((b) => b['is_board_challenge'] != true)
                .toList();
            _boardBlocks = rawBlocks
                .where((b) => b['is_board_challenge'] == true)
                .toList();
            _blocks = _showBoardQuestions ? rawBlocks : _standardBlocks;
            _isLoading = false;
          });
        } else {
          throw Exception(
            'Module ${widget.moduleId} not found in LocalContentManager, assets, or CurriculumDatabase. Please ensure you have restarted the app (stop with q and flutter run) to bundle new JSON files.',
          );
        }
      }
    } catch (e, stack) {
      if (mounted) {
        setState(() {
          _error = 'Failed to load module data. Error: $e\n\nStack: $stack';
          _isLoading = false;
        });
      }
    }
  }

  bool get _showBoardGateway => _boardBlocks.isNotEmpty && !_showBoardQuestions && !_revisionMode;

  Widget _buildBlock(Map<String, dynamic> block) {
    try {
      BlockValidator.validateBlock(block);
      final childWidget = BlockRegistry.instance.build(block);
      if (childWidget != null) {
        return childWidget;
      } else {
        return _buildDiagnosticError(
          block,
          'Unknown block type: ${block['type']}',
        );
      }
    } catch (e, stack) {
      return _buildDiagnosticError(
        block,
        e.toString(),
        stackTrace: stack.toString(),
      );
    }
  }

  Widget _buildDiagnosticError(
    Map<String, dynamic> block,
    String error, {
    String? stackTrace,
  }) {
    String type = block['type'] ?? 'MISSING';
    String moduleTitle = _metadata?['title'] ?? 'Unknown Module';
    String fileInfo = '${widget.moduleId}/blocks.json';

    // Attempt to parse out expected/received from our custom FormatExceptions
    String expected = 'Valid Block Structure';
    String received = 'Malformed JSON';
    String valueInfo = block.containsKey('id') ? block['id'] : 'UNKNOWN_ID';

    if (error.contains("Expected key") && error.contains("to be")) {
      // Very basic parsing for demonstration of desired format
      try {
        final parts = error.split("to be ");
        final typePart = parts[1].split(",")[0];
        expected = typePart;
        received = error.split("but got ")[1];
      } catch (_) {}
    } else if (error.contains("Missing required key")) {
      expected = "Key Present";
      received = "Missing Key";
    }

    return Container(
      margin: const EdgeInsets.only(bottom: 16),
      padding: const EdgeInsets.all(16),
      decoration: BoxDecoration(
        color: Colors.red[50],
        border: Border.all(color: Colors.red[300]!, width: 2),
        borderRadius: BorderRadius.circular(12),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            children: [
              Icon(Icons.error_outline, color: Colors.red),
              const SizedBox(width: 8),
              Text(
                TrilingualService.instance.getUIText("Block Render Error"),
                style: TextStyle(
                  color: Colors.red[900],
                  fontWeight: FontWeight.bold,
                  fontSize: 16,
                ),
              ),
            ],
          ),
          const Divider(color: Colors.red),
          Text(
            "Chapter:\n$moduleTitle",
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          Text("Block:\n$type", style: TextStyle(fontWeight: FontWeight.bold)),
          const SizedBox(height: 8),
          Text("Expected:\n$expected"),
          const SizedBox(height: 8),
          Text("Received:\n$received"),
          const SizedBox(height: 8),
          Text("Value:\n$valueInfo"),
          const SizedBox(height: 8),
          Text("File:\n$fileInfo", style: TextStyle(color: Colors.blue)),
          const SizedBox(height: 16),
          Text(
            TrilingualService.instance.getUIText("Raw Data:"),
            style: TextStyle(fontWeight: FontWeight.bold),
          ),
          Container(
            padding: const EdgeInsets.all(8),
            color: Colors.white,
            width: double.infinity,
            child: Text(
              json.encode(block),
              style: TextStyle(fontFamily: 'monospace', fontSize: 12),
            ),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return const Scaffold(
        backgroundColor: AppColors.background,
        body: Center(child: CircularProgressIndicator()),
      );
    }

    if (_error.isNotEmpty) {
      return Scaffold(
        appBar: const BrandAppBar(title: 'Error'),
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Text(_error),
          ),
        ),
      );
    }

    final rawTitle =
        _metadata?['title'] ??
        _metadata?['term']?['english'] ??
        'Learning Module';
    final String title = rawTitle is String
        ? TrilingualService.instance.getLocalizedText(_metadata!, 'title')
        : (rawTitle is Map
              ? (rawTitle['en'] ?? rawTitle['english'] ?? 'Module')
              : 'Module');
    final isDictionary = widget.moduleId.contains('DICT');

    return ListenableBuilder(
      listenable: TrilingualService.instance,
      builder: (context, _) {
        return Scaffold(
          backgroundColor: Colors.grey[50],
          appBar: BrandAppBar(
            title: title,
            bottom: !isDictionary && hasRevisionContent(_standardBlocks)
                ? PreferredSize(
                    preferredSize: const Size.fromHeight(56),
                    child: Padding(
                      padding: const EdgeInsets.only(bottom: 8),
                      child: SegmentedButton<bool>(
                        style: SegmentedButton.styleFrom(
                          backgroundColor: Colors.white,
                          selectedBackgroundColor: Colors.amber.shade200,
                        ),
                        segments: [
                          ButtonSegment(value: false, icon: const Icon(Icons.menu_book), label: Text(TrilingualService.instance.getUIText('Full lesson'))),
                          ButtonSegment(value: true, icon: const Icon(Icons.bolt), label: Text(TrilingualService.instance.getUIText('Quick revision'))),
                        ],
                        selected: {_revisionMode},
                        onSelectionChanged: (selection) => _setRevisionMode(selection.first),
                      ),
                    ),
                  )
                : null,
            actions: isDictionary
                ? null
                : [
                    ValueListenableBuilder<bool>(
                      valueListenable: PresentationService.isPresentationMode,
                      builder: (context, isPresentation, child) {
                        return IconButton(
                          icon: Icon(
                            isPresentation
                                ? Icons.desktop_windows
                                : Icons.smartphone,
                            color: isPresentation
                                ? Colors.yellow
                                : Colors.white,
                          ),
                          tooltip: isPresentation
                              ? 'Presentation Mode: ON'
                              : 'Presentation Mode: OFF',
                          onPressed: () {
                            PresentationService.toggle();
                            ScaffoldMessenger.of(context).showSnackBar(
                              SnackBar(
                                content: Text(
                                  isPresentation
                                      ? "Standard Mode Activated"
                                      : "Presentation Mode Activated (Large Text)",
                                ),
                                duration: const Duration(seconds: 2),
                              ),
                            );
                          },
                        );
                      },
                    ),
                    IconButton(
                      icon: Icon(Icons.picture_as_pdf),
                      tooltip: 'Download as PDF',
                      onPressed: () {
                        if (_metadata != null) {
                          _showPdfMetadataDialog();
                        }
                      },
                    ),
                    IconButton(
                      icon: Icon(Icons.assignment),
                      tooltip: 'Generate Exam',
                      onPressed: () {
                        context.push('/assessment/bank/${widget.moduleId}');
                      },
                    ),
                  ],
          ),
          body: SafeArea(
            child: Focus(
              focusNode: _focusNode,
              autofocus: true,
              onKeyEvent: (FocusNode node, KeyEvent event) {
                if (event is KeyDownEvent || event is KeyRepeatEvent) {
                  const scrollAmount = 300.0; // Distance to jump per click

                  if (event.logicalKey == LogicalKeyboardKey.arrowDown ||
                      event.logicalKey == LogicalKeyboardKey.pageDown ||
                      event.logicalKey == LogicalKeyboardKey.space) {
                    _scrollController.animateTo(
                      (_scrollController.offset + scrollAmount).clamp(
                        0.0,
                        _scrollController.position.maxScrollExtent,
                      ),
                      duration: const Duration(milliseconds: 300),
                      curve: Curves.easeOut,
                    );
                    return KeyEventResult.handled;
                  }

                  if (event.logicalKey == LogicalKeyboardKey.arrowUp ||
                      event.logicalKey == LogicalKeyboardKey.pageUp) {
                    _scrollController.animateTo(
                      (_scrollController.offset - scrollAmount).clamp(
                        0.0,
                        _scrollController.position.maxScrollExtent,
                      ),
                      duration: const Duration(milliseconds: 300),
                      curve: Curves.easeOut,
                    );
                    return KeyEventResult.handled;
                  }
                }
                return KeyEventResult.ignored;
              },
              child: isDictionary
                  ? ListView(
                      key: ValueKey(
                        TrilingualService.instance.activeViewLanguage,
                      ),
                      controller: _scrollController,
                      padding: const EdgeInsets.all(20),
                      children: [DictionaryTermWidget(data: _metadata!)],
                    )
                  : ListView.builder(
                      key: ValueKey(
                        TrilingualService.instance.activeViewLanguage,
                      ),
                      controller: _scrollController,
                      padding: const EdgeInsets.all(20),
                      itemCount:
                          _blocks.length +
                          (_showDictionaryHint ? 1 : 0) +
                          (_showBoardGateway ? 1 : 0) +
                          1, // chapter finish card
                      itemBuilder: (context, index) {
                        final finishIndex = _blocks.length + (_showDictionaryHint ? 1 : 0) + (_showBoardGateway ? 1 : 0);
                        if (index == finishIndex) {
                          return ChapterFinishCard(
                            moduleId: widget.moduleId,
                            onPlayQuiz: () => context.push('/assessment/game/${widget.moduleId}'),
                            onQuickRevision: () => _setRevisionMode(true),
                          );
                        }
                        if (_showDictionaryHint && index == 0) {
                          return Container(
                            margin: const EdgeInsets.only(bottom: 24),
                            padding: const EdgeInsets.symmetric(
                              horizontal: 16,
                              vertical: 12,
                            ),
                            decoration: BoxDecoration(
                              color: Colors.blue.shade50,
                              borderRadius: BorderRadius.circular(12),
                              border: Border.all(color: Colors.blue.shade200),
                            ),
                            child: Row(
                              children: [
                                Icon(
                                  Icons.lightbulb_outline,
                                  color: Colors.blue,
                                ),
                                const SizedBox(width: 12),
                                Expanded(
                                  child: Text(
                                    TrilingualService.instance.getUIText(
                                      "Tip: Double-tap ANY word to start speaking from there!",
                                    ),
                                    style: TextStyle(
                                      color: Colors.blue.shade900,
                                      fontWeight: FontWeight.w500,
                                      fontSize: 15,
                                    ),
                                  ),
                                ),
                                IconButton(
                                  icon: Icon(
                                    Icons.close,
                                    size: 20,
                                    color: Colors.blue,
                                  ),
                                  onPressed: () => setState(
                                    () => _showDictionaryHint = false,
                                  ),
                                  padding: EdgeInsets.zero,
                                  constraints: const BoxConstraints(),
                                ),
                              ],
                            ),
                          );
                        }

                        int gatewayIndex =
                            _blocks.length + (_showDictionaryHint ? 1 : 0);
                        if (_showBoardGateway && index == gatewayIndex) {
                          return _buildBoardGateway(context);
                        }

                        final actualIndex = _showDictionaryHint
                            ? index - 1
                            : index;
                        final block = _blocks[actualIndex];
                        final childWidget = _buildBlock(block);
                        return UniversalBlockWrapper(
                          block: block,
                          child: childWidget,
                        );
                      },
                    ),
            ),
          ),
          floatingActionButton: (!_isLoading && _error.isEmpty && !isDictionary)
              ? FloatingActionButton.extended(
                  onPressed: () {
                    showModalBottomSheet(
                      context: context,
                      isScrollControlled: true,
                      backgroundColor: Colors.transparent,
                      builder: (context) => Padding(
                        padding: EdgeInsets.only(
                          top: MediaQuery.of(context).padding.top + 40,
                        ),
                        child: AiTutorScreen(
                          blockContext: _metadata ?? {'title': title},
                        ),
                      ),
                    );
                  },
                  icon: Icon(Icons.auto_awesome),
                  label: Text(
                    TrilingualService.instance.getUIText('Ask AI Tutor'),
                  ),
                  backgroundColor: Colors.purple,
                  foregroundColor: Colors.white,
                )
              : null,
        );
      },
    );
  }

  Widget _buildBoardGateway(BuildContext context) {
    return Container(
      margin: const EdgeInsets.symmetric(vertical: 32),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.indigo.shade50,
        borderRadius: BorderRadius.circular(20),
        border: Border.all(color: Colors.indigo.shade200, width: 2),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.center,
        children: [
          Icon(Icons.military_tech, size: 64, color: Colors.indigo.shade700),
          const SizedBox(height: 16),
          Text(
            TrilingualService.instance.getUIText(
              "Board Preparations (Solved Question Papers)",
            ),
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
              color: Colors.indigo.shade900,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            TrilingualService.instance.getUIText(
              "Ready for a challenge? You can play this as a timed gamified quiz to earn badges, or simply view them as standard practice questions at your own pace.",
            ),
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: 15,
              color: Colors.indigo.shade700,
              height: 1.5,
            ),
          ),
          const SizedBox(height: 24),
          Row(
            children: [
              Expanded(
                child: ElevatedButton.icon(
                  onPressed: () {
                    context.push('/assessment/bank/${widget.moduleId}');
                  },
                  icon: Icon(Icons.gamepad),
                  label: Text(
                    TrilingualService.instance.getUIText("Gamified Challenge"),
                  ),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.indigo.shade700,
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12),
                    ),
                  ),
                ),
              ),
              const SizedBox(width: 12),
              Expanded(
                child: OutlinedButton.icon(
                  onPressed: () {
                    setState(() {
                      _showBoardQuestions = true;
                      _blocks = [..._standardBlocks, ..._boardBlocks];
                    });
                  },
                  icon: Icon(Icons.menu_book),
                  label: Text(
                    TrilingualService.instance.getUIText("Standard Practice"),
                  ),
                  style: OutlinedButton.styleFrom(
                    foregroundColor: Colors.indigo.shade700,
                    side: BorderSide(color: Colors.indigo.shade300, width: 2),
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(12),
                    ),
                  ),
                ),
              ),
            ],
          ),
        ],
      ),
    );
  }

  void _showPdfMetadataDialog() {
    final studentNameCtrl = TextEditingController();

    showDialog(
      context: context,
      builder: (context) {
        return AlertDialog(
          title: Text(
            TrilingualService.instance.getUIText('PDF Details'),
            style: GoogleFonts.inter(fontWeight: FontWeight.bold),
          ),
          content: SingleChildScrollView(
            child: Column(
              mainAxisSize: MainAxisSize.min,
              children: [
                Text(
                  TrilingualService.instance.getUIText(
                    'Enter the student name for watermarking to protect material.',
                  ),
                  style: GoogleFonts.inter(
                    fontSize: 14,
                    color: Colors.grey.shade700,
                  ),
                ),
                const SizedBox(height: 12),
                TextFormField(
                  controller: studentNameCtrl,
                  decoration: InputDecoration(
                    labelText: TrilingualService.instance.getUIText(
                      'Student Name',
                    ),
                    border: OutlineInputBorder(),
                  ),
                ),
              ],
            ),
          ),
          actions: [
            TextButton(
              onPressed: () => Navigator.pop(context),
              child: Text(TrilingualService.instance.getUIText('Cancel')),
            ),
            ElevatedButton(
              style: ElevatedButton.styleFrom(
                backgroundColor: Colors.blue[700],
                foregroundColor: Colors.white,
              ),
              onPressed: () async {
                final name = studentNameCtrl.text.trim();
                if (name.isEmpty) {
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: Text(
                        TrilingualService.instance.getUIText(
                          'Please enter a valid name',
                        ),
                      ),
                    ),
                  );
                  return;
                }
                Navigator.pop(context);
                ScaffoldMessenger.of(context).showSnackBar(
                  SnackBar(
                    content: Text(
                      TrilingualService.instance.getUIText('Generating PDF...'),
                    ),
                  ),
                );
                try {
                  await PdfExportService.generateAndPrintChapter(
                    context,
                    _metadata!,
                    _blocks,
                    studentName: name,
                  );
                  if (context.mounted) {
                    ScaffoldMessenger.of(context).hideCurrentSnackBar();
                  }
                } catch (e) {
                  if (context.mounted) {
                    ScaffoldMessenger.of(context).hideCurrentSnackBar();
                    ScaffoldMessenger.of(context).showSnackBar(
                      SnackBar(
                        content: Text('Error generating PDF: $e'),
                        backgroundColor: Colors.red,
                      ),
                    );
                  }
                }
              },
              child: Text(TrilingualService.instance.getUIText('Generate')),
            ),
          ],
        );
      },
    );
  }
}
