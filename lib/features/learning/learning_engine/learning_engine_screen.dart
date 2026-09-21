import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:go_router/go_router.dart';
import 'package:url_launcher/url_launcher.dart';
import '../../../../core/engine/pedagogy_engine.dart';
import '../../../../core/engine/block_validator.dart';
import '../../../../core/engine/block_registry.dart';
import '../../../../core/engine/curriculum_database.dart';
import '../../../../core/engine/local_content_manager.dart';
import '../../../../foundation/theme/app_colors.dart';
import 'widgets/dictionary_term_widget.dart';
import 'widgets/flashcard_widget.dart';
import 'widgets/teacher_tip_widget.dart';
import 'widgets/common_mistakes_widget.dart';
import 'widgets/dictionary_link_widget.dart';
import 'widgets/theory_widget.dart';
import 'widgets/trilingual_card_widget.dart';
import 'widgets/example_widget.dart';
import 'widgets/media_widget.dart';
import 'widgets/activity_widget.dart';
import 'widgets/quiz_widget.dart';
import 'widgets/nursery_rhyme_widget.dart';
import 'widgets/trace_alphabet_widget.dart';
import 'widgets/counting_game_widget.dart';
import 'widgets/color_canvas_widget.dart';
import '../../../foundation/theme/app_colors.dart';
import '../../../foundation/theme/brand_app_bar.dart';
import 'package:go_router/go_router.dart';
import '../ai_tutor/ai_tutor_screen.dart';
import '../../../core/engine/block_validator.dart';
import 'services/pdf_export_service.dart';
import 'package:flutter/services.dart';
import 'widgets/presentation_widget.dart';
import 'widgets/animated_diagram_widget.dart';
import 'widgets/universal_block_wrapper.dart';
import 'widgets/dialogue_widget.dart';
import '../../../core/engine/pedagogy_engine.dart';
import '../../../core/services/presentation_service.dart';

import 'widgets/worked_example_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

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
  bool _isComingSoon = false;
  bool _showDictionaryHint = true;
  bool _showBoardQuestions = false;
  
  // Phase 6: Smart Panel Remote Control Support
  final ScrollController _scrollController = ScrollController();
  final FocusNode _focusNode = FocusNode();

  @override
  void initState() {
    super.initState();
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
    super.dispose();
  }

  Future<void> _loadModule() async {
    try {
      await LocalContentManager.instance.init();

      if (widget.moduleId.contains('DICT')) {
        final termString = await rootBundle.loadString('app_core/knowledge_graph/dictionary/${widget.moduleId}.json');
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

        // ── Priority 1: Check LocalContentManager (catches editor-saved changes) ──
        final chapterAssetPath = 'app_core/chapters/${widget.moduleId}.json';
        dynamic rawFileData =
            await LocalContentManager.instance.readLocalJson(chapterAssetPath);

        // ── Priority 2: Fall back to bundled asset ────────────────────────────
        if (rawFileData == null) {
          try {
            final String fileString =
                await rootBundle.loadString(chapterAssetPath);
            rawFileData = jsonDecode(fileString);
          } catch (_) {
            // Chapter file doesn't exist at all
          }
        }
        
        Map<String, dynamic>? fileData = rawFileData != null ? _normalizeData(rawFileData) : null;


        if (fileData != null) {
          final metaData = (fileData['metadata'] as Map<String, dynamic>?) ?? {};
          final rawBlocks = (fileData['blocks'] as List<dynamic>?) ?? [];

          final pedagogyReport = PedagogyEngine.validateChapterFlow(rawBlocks);
          if (!pedagogyReport.isValid) {
            debugPrint(
                'PEDAGOGY WARNING: Chapter ${widget.moduleId} is missing: '
                '${pedagogyReport.missingComponents.join(', ')}');
          }

          setState(() {
            _metadata = metaData;
            _standardBlocks = rawBlocks.where((b) => b['is_board_challenge'] != true).toList();
            _boardBlocks = rawBlocks.where((b) => b['is_board_challenge'] == true).toList();
            _blocks = _showBoardQuestions ? rawBlocks : _standardBlocks;
            _isLoading = false;
          });
          return; // Successfully loaded chapter!
        }

        // ── Priority 3: Fall back to in-memory CurriculumDatabase ─────────────
        if (CurriculumDatabase.instance.hasModule(widget.moduleId)) {
          final metaData = CurriculumDatabase.instance.getModuleMetadata(widget.moduleId);
          final rawBlocks = CurriculumDatabase.instance.getModuleBlocks(widget.moduleId);

          if (rawBlocks == null) {
            throw Exception('Module blocks not found in database.');
          }

          final pedagogyReport = PedagogyEngine.validateChapterFlow(rawBlocks);
          if (!pedagogyReport.isValid) {
            debugPrint(
                'PEDAGOGY WARNING: Chapter ${widget.moduleId} is missing: '
                '${pedagogyReport.missingComponents.join(', ')}');
          }

          setState(() {
            _metadata = metaData ?? {};
            _standardBlocks = rawBlocks.where((b) => b['is_board_challenge'] != true).toList();
            _boardBlocks = rawBlocks.where((b) => b['is_board_challenge'] == true).toList();
            _blocks = _showBoardQuestions ? rawBlocks : _standardBlocks;
            _isLoading = false;
          });
        } else {
          // Module not found anywhere — show Coming Soon gracefully
          setState(() {
            _isComingSoon = true;
            _isLoading = false;
          });
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

  Widget _buildBlock(Map<String, dynamic> block) {
    try {
      BlockValidator.validateBlock(block);
      final childWidget = BlockRegistry.instance.build(block);
      if (childWidget != null) {
        return childWidget;
      } else {
        return _buildDiagnosticError(block, 'Unknown block type: ${block['type']}');
      }
    } catch (e, stack) {
      return _buildDiagnosticError(block, e.toString(), stackTrace: stack.toString());
    }
  }

  Widget _buildDiagnosticError(Map<String, dynamic> block, String error, {String? stackTrace}) {
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
              Text(TrilingualService.instance.getUIText("Block Render Error"), style: TextStyle(color: Colors.red[900], fontWeight: FontWeight.bold, fontSize: 16)),
            ],
          ),
          const Divider(color: Colors.red),
          Text("Chapter:\n$moduleTitle", style: TextStyle(fontWeight: FontWeight.bold)),
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
          Text(TrilingualService.instance.getUIText("Raw Data:"), style: TextStyle(fontWeight: FontWeight.bold)),
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
        body: Center(child: Padding(
          padding: const EdgeInsets.all(16.0),
          child: Text(_error),
        )),
      );
    }

    if (_isComingSoon) {
      return Scaffold(
        backgroundColor: Colors.white,
        appBar: BrandAppBar(title: widget.moduleId.split('_').join(' ').toUpperCase()),
        body: Center(
          child: Padding(
            padding: const EdgeInsets.all(32.0),
            child: Column(
              mainAxisAlignment: MainAxisAlignment.center,
              children: [
                Icon(Icons.construction, size: 80, color: Colors.orange[400]),
                const SizedBox(height: 24),
                Text(TrilingualService.instance.getUIText("Module Coming Soon"),
                  style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: AppColors.primary),
                ),
                const SizedBox(height: 16),
                Text(TrilingualService.instance.getUIText("Our Gold Standard Educators are currently crafting this chapter. It will be available in the next curriculum update!"),
                  textAlign: TextAlign.center,
                  style: TextStyle(fontSize: 16, color: Theme.of(context).colorScheme.onSurfaceVariant),
                ),
                const SizedBox(height: 32),
                ElevatedButton.icon(
                  onPressed: () => context.pop(),
                  icon: Icon(Icons.arrow_back),
                  label: Text(TrilingualService.instance.getUIText("Go Back")),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: AppColors.primary,
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 12),
                  ),
                )
              ],
            ),
          ),
        ),
      );
    }

    final rawTitle = _metadata?['title'] ?? _metadata?['term']?['english'] ?? 'Learning Module';
    final String title = rawTitle is String ? rawTitle : (rawTitle is Map ? (rawTitle['en'] ?? rawTitle['english'] ?? 'Module') : 'Module');
    final isDictionary = widget.moduleId.contains('DICT');

    return Scaffold(
      backgroundColor: Colors.grey[50],
      appBar: BrandAppBar(
        title: title,
        actions: isDictionary ? null : [
          ValueListenableBuilder<bool>(
            valueListenable: PresentationService.isPresentationMode,
            builder: (context, isPresentation, child) {
              return IconButton(
                icon: Icon(
                  isPresentation ? Icons.desktop_windows : Icons.smartphone,
                  color: isPresentation ? Colors.yellow : Colors.white,
                ),
                tooltip: isPresentation ? 'Presentation Mode: ON' : 'Presentation Mode: OFF',
                onPressed: () {
                  PresentationService.toggle();
                  ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(
                      content: Text(isPresentation ? "Standard Mode Activated" : "Presentation Mode Activated (Large Text)"),
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
            onPressed: () async {
              if (_metadata != null) {
                await PdfExportService.generateAndPrintChapter(_metadata!, _blocks);
              }
            },
          ),
          IconButton(
            icon: Icon(Icons.assignment),
            tooltip: 'Generate Exam',
            onPressed: () {
              context.push('/assessment/bank/${widget.moduleId}');
            },
          )
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
                    0.0, _scrollController.position.maxScrollExtent
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
                    0.0, _scrollController.position.maxScrollExtent
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
                  controller: _scrollController,
                  padding: const EdgeInsets.all(20),
                  children: [
                    DictionaryTermWidget(data: _metadata!),
                  ],
                )
              : ListView.builder(
                  controller: _scrollController,
                  padding: const EdgeInsets.all(20),
                  itemCount: _blocks.length + (_showDictionaryHint ? 1 : 0) + (_boardBlocks.isNotEmpty && !_showBoardQuestions ? 1 : 0),
                  itemBuilder: (context, index) {
                    if (_showDictionaryHint && index == 0) {
                      return Container(
                        margin: const EdgeInsets.only(bottom: 24),
                        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                        decoration: BoxDecoration(
                          color: Colors.blue.shade50,
                          borderRadius: BorderRadius.circular(12),
                          border: Border.all(color: Colors.blue.shade200),
                        ),
                        child: Row(
                          children: [
                            Icon(Icons.lightbulb_outline, color: Colors.blue),
                            const SizedBox(width: 12),
                            Expanded(
                              child: Text(TrilingualService.instance.getUIText("Tip: Double-tap ANY word to instantly look it up in the dictionary!"),
                                style: TextStyle(color: Colors.blue.shade900, fontWeight: FontWeight.w500, fontSize: 15),
                              ),
                            ),
                            IconButton(
                              icon: Icon(Icons.close, size: 20, color: Colors.blue),
                              onPressed: () => setState(() => _showDictionaryHint = false),
                              padding: EdgeInsets.zero,
                              constraints: const BoxConstraints(),
                            )
                          ],
                        ),
                      );
                    }

                    int gatewayIndex = _blocks.length + (_showDictionaryHint ? 1 : 0);
                    if (_boardBlocks.isNotEmpty && !_showBoardQuestions && index == gatewayIndex) {
                      return _buildBoardGateway(context);
                    }

                    final actualIndex = _showDictionaryHint ? index - 1 : index;
                    final block = _blocks[actualIndex];
                    final childWidget = _buildBlock(block);
                    return UniversalBlockWrapper(block: block, child: childWidget);
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
                    padding: EdgeInsets.only(top: MediaQuery.of(context).padding.top + 40),
                    child: AiTutorScreen(blockContext: _metadata ?? {'title': title}),
                  ),
                );
              },
              icon: Icon(Icons.auto_awesome),
              label: Text(TrilingualService.instance.getUIText('Ask AI Tutor')),
              backgroundColor: Colors.purple,
              foregroundColor: Colors.white,
            )
          : null,
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
          Text(TrilingualService.instance.getUIText("Board Preparations (Solved Question Papers)"),
            textAlign: TextAlign.center,
            style: TextStyle(
              fontSize: 22,
              fontWeight: FontWeight.bold,
              color: Colors.indigo.shade900,
            ),
          ),
          const SizedBox(height: 8),
          Text(TrilingualService.instance.getUIText("Ready for a challenge? You can play this as a timed gamified quiz to earn badges, or simply view them as standard practice questions at your own pace."),
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
                  label: Text(TrilingualService.instance.getUIText("Gamified Challenge")),
                  style: ElevatedButton.styleFrom(
                    backgroundColor: Colors.indigo.shade700,
                    foregroundColor: Colors.white,
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
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
                  label: Text(TrilingualService.instance.getUIText("Standard Practice")),
                  style: OutlinedButton.styleFrom(
                    foregroundColor: Colors.indigo.shade700,
                    side: BorderSide(color: Colors.indigo.shade300, width: 2),
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
                  ),
                ),
              ),
            ],
          )
        ],
      ),
    );
  }
}
