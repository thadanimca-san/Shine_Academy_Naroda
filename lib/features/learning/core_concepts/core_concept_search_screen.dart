import 'dart:convert';
import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';
import 'package:flutter/services.dart';
import 'package:google_fonts/google_fonts.dart';

import '../../../foundation/theme/app_colors.dart';
import '../../../foundation/theme/brand_app_bar.dart';
import '../../../foundation/theme/premium_card.dart';
import '../../../core/services/trilingual_service.dart';
import '../../../core/services/universal_dictionary_service.dart';
import '../../../core/engine/block_registry.dart';

class CoreConceptSearchScreen extends StatefulWidget {
  final String classId;
  final String subjectId;
  
  const CoreConceptSearchScreen({
    super.key,
    required this.classId,
    required this.subjectId,
  });

  @override
  State<CoreConceptSearchScreen> createState() => _CoreConceptSearchScreenState();
}

class _CoreConceptSearchScreenState extends State<CoreConceptSearchScreen> {
  final TextEditingController _searchController = TextEditingController();
  
  bool _isLoading = true;
  String _subjectName = 'Search Concepts';
  String _error = '';
  
  // Data for searching
  final List<Map<String, dynamic>> _allBlocks = [];
  
  // Search results
  List<Map<String, dynamic>> _dictionaryResults = [];
  List<Map<String, dynamic>> _blockResults = [];

  @override
  void initState() {
    super.initState();
    _loadSubjectData();
  }
  
  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _loadSubjectData() async {
    try {
      final jsonString = await rootBundle.loadString('app_core/curriculum/${widget.classId}.json');
      final curriculum = json.decode(jsonString);
      
      final subjects = curriculum['subjects'] as List;
      final subject = subjects.firstWhere(
        (s) => s['id'] == widget.subjectId, 
        orElse: () => null,
      );

      if (subject == null) {
        throw Exception('Subject not found');
      }

      _subjectName = subject['name'] ?? subject['title'] ?? 'Search Concepts';
      final chapters = subject['chapters'] as List;
      
      // Load all chapter blocks
      for (var chapter in chapters) {
        final moduleId = chapter['module_id'] ?? chapter['id'];
        if (moduleId != null && !moduleId.toString().startsWith('sci_sim:')) {
          try {
            final chapterJsonStr = await rootBundle.loadString('app_core/chapters/$moduleId.json');
            final chapterData = json.decode(chapterJsonStr);
            if (chapterData.containsKey('blocks')) {
              final blocks = chapterData['blocks'] as List;
              for (var block in blocks) {
                // We only care about educational content blocks
                final type = block['type'];
                if (type == 'theory' || type == 'definition' || type == 'concept' || type == 'dictionary_link') {
                  // Keep a reference to the chapter title for UI context
                  block['_chapter_context'] = chapter['title'] ?? 'Chapter';
                  _allBlocks.add(block as Map<String, dynamic>);
                }
              }
            }
          } catch (e) {
            // Ignore missing files or parsing errors for individual chapters
            debugPrint("Failed to load chapter $moduleId: $e");
          }
        }
      }

      setState(() {
        _isLoading = false;
      });
      
    } catch (e) {
      setState(() {
        _error = 'Failed to load subject data.';
        _isLoading = false;
      });
    }
  }

  void _onSearchChanged(String query) async {
    if (query.trim().isEmpty) {
      setState(() {
        _dictionaryResults.clear();
        _blockResults.clear();
      });
      return;
    }
    
    final lowerQuery = query.toLowerCase();
    
    // 1. Search Dictionary
    final dictResults = await UniversalDictionaryService.instance.searchTerms(lowerQuery);
    
    // 2. Search Chapter Blocks
    final List<Map<String, dynamic>> matchedBlocks = [];
    for (var block in _allBlocks) {
      bool matches = false;
      
      // Check titles
      if ((block['title']?.toString().toLowerCase().contains(lowerQuery) ?? false) ||
          (block['title_hi']?.toString().toLowerCase().contains(lowerQuery) ?? false) ||
          (block['title_gu']?.toString().toLowerCase().contains(lowerQuery) ?? false)) {
        matches = true;
      }
      
      // Check body
      if (!matches) {
        if ((block['body']?.toString().toLowerCase().contains(lowerQuery) ?? false) ||
            (block['body_hi']?.toString().toLowerCase().contains(lowerQuery) ?? false) ||
            (block['body_gu']?.toString().toLowerCase().contains(lowerQuery) ?? false)) {
          matches = true;
        }
      }
      
      // Check content object if it exists
      if (!matches && block.containsKey('content') && block['content'] != null) {
        final contentStr = block['content'].toString().toLowerCase();
        if (contentStr.contains(lowerQuery)) {
          matches = true;
        }
      }
      
      if (matches) {
        matchedBlocks.add(block);
      }
    }

    setState(() {
      _dictionaryResults = dictResults;
      _blockResults = matchedBlocks;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: AppColors.background,
      appBar: BrandAppBar(title: '$_subjectName Concepts'),
      body: _isLoading 
        ? const Center(child: CircularProgressIndicator())
        : _error.isNotEmpty 
          ? Center(child: Text(_error))
          : Column(
              children: [
                _buildSearchHeader(),
                Expanded(
                  child: _buildResults(),
                ),
              ],
            ),
    );
  }

  Widget _buildSearchHeader() {
    return Container(
      decoration: BoxDecoration(
        color: Colors.white,
        boxShadow: [
          BoxShadow(
            color: Colors.black.withValues(alpha: 0.05),
            blurRadius: 10,
            offset: const Offset(0, 4),
          ),
        ],
      ),
      padding: const EdgeInsets.all(24),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(
            TrilingualService.instance.getUIText('Search Core Concepts'),
            style: TextStyle(
              fontSize: 24,
              fontWeight: FontWeight.bold,
              color: AppColors.textPrimary,
            ),
          ),
          const SizedBox(height: 8),
          Text(
            TrilingualService.instance.getUIText('Search anything from dictionary terms to chapter theories.'),
            style: TextStyle(
              fontSize: 14,
              color: AppColors.textSecondary,
            ),
          ),
          const SizedBox(height: 20),
          TextField(
            controller: _searchController,
            onChanged: _onSearchChanged,
            style: TextStyle(fontSize: 16),
            decoration: InputDecoration(
              hintText: TrilingualService.instance.getUIText('Search... e.g. Force, Motion, Energy'),
              prefixIcon: const Icon(Icons.search, color: AppColors.primary),
              suffixIcon: _searchController.text.isNotEmpty 
                  ? IconButton(
                      icon: const Icon(Icons.clear),
                      onPressed: () {
                        _searchController.clear();
                        _onSearchChanged('');
                      },
                    )
                  : null,
              filled: true,
              fillColor: Colors.grey.shade50,
              contentPadding: const EdgeInsets.symmetric(vertical: 16, horizontal: 20),
              border: OutlineInputBorder(
                borderRadius: BorderRadius.circular(30),
                borderSide: BorderSide(color: Colors.grey.shade300),
              ),
              enabledBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(30),
                borderSide: BorderSide(color: Colors.grey.shade300),
              ),
              focusedBorder: OutlineInputBorder(
                borderRadius: BorderRadius.circular(30),
                borderSide: const BorderSide(color: AppColors.primary, width: 2),
              ),
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildResults() {
    if (_searchController.text.trim().isEmpty) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.manage_search, size: 64, color: Colors.grey.shade300),
            const SizedBox(height: 16),
            Text(
              TrilingualService.instance.getUIText('Start typing to find concepts.'),
              style: TextStyle(fontSize: 16, color: Colors.grey.shade500),
            ),
          ],
        ),
      );
    }

    if (_dictionaryResults.isEmpty && _blockResults.isEmpty) {
      return Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            Icon(Icons.search_off, size: 64, color: Colors.grey.shade300),
            const SizedBox(height: 16),
            Text(
              TrilingualService.instance.getUIText('No concepts found.'),
              style: TextStyle(fontSize: 16, color: Colors.grey.shade500),
            ),
          ],
        ),
      );
    }

    return ListView(
      padding: const EdgeInsets.all(16),
      children: [
        if (_dictionaryResults.isNotEmpty) ...[
          Padding(
            padding: const EdgeInsets.only(left: 8, bottom: 12, top: 8),
            child: Text(
              TrilingualService.instance.getUIText('Dictionary Definitions'),
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.primary),
            ),
          ),
          ..._dictionaryResults.map((term) => _buildDictionaryCard(term)),
        ],
        if (_blockResults.isNotEmpty) ...[
          Padding(
            padding: const EdgeInsets.only(left: 8, bottom: 12, top: 24),
            child: Text(
              TrilingualService.instance.getUIText('From Chapters'),
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.primary),
            ),
          ),
          ..._blockResults.map((block) => _buildChapterBlockCard(block)),
        ]
      ],
    );
  }

  Widget _buildDictionaryCard(Map<String, dynamic> termData) {
    final term = termData['term'] ?? {};
    final definition = termData['definition'] ?? {};
    
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: PremiumCard(
        padding: const EdgeInsets.all(20),
        color: Colors.white,
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
          Row(
            children: [
              Container(
                padding: const EdgeInsets.all(8),
                decoration: BoxDecoration(
                  color: AppColors.primary.withValues(alpha: 0.1),
                  borderRadius: BorderRadius.circular(8),
                ),
                child: const Icon(Icons.book, color: AppColors.primary),
              ),
              const SizedBox(width: 16),
              Expanded(
                child: Column(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(
                      term['english'] ?? 'Unknown Term',
                      style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold, color: AppColors.textPrimary),
                    ),
                    if (term['hindi'] != null || term['gujarati'] != null)
                      Text(
                        '${term['hindi'] ?? ''} • ${term['gujarati'] ?? ''}',
                        style: TextStyle(fontSize: 14, color: AppColors.textSecondary),
                      ),
                  ],
                ),
              ),
            ],
          ),
          const SizedBox(height: 16),
          const Divider(),
          const SizedBox(height: 12),
          TtsInteractiveText(
            text: (definition['simple'] is Map ? definition['simple']['en'] : definition['simple'])?.toString() ?? 
                  (definition['academic'] is Map ? definition['academic']['en'] : definition['academic'])?.toString() ?? '',
            style: const TextStyle(fontSize: 15, height: 1.5, color: Colors.black87),
          ),
          if (definition['simple'] is Map && definition['simple']['hi'] != null) ...[
            const SizedBox(height: 8),
            TtsInteractiveText(
              text: definition['simple']['hi'].toString(),
              style: const TextStyle(fontSize: 14, height: 1.5, color: Colors.black54),
            ),
          ],
          if (definition['simple'] is Map && definition['simple']['gu'] != null) ...[
            const SizedBox(height: 8),
            TtsInteractiveText(
              text: definition['simple']['gu'].toString(),
              style: const TextStyle(fontSize: 14, height: 1.5, color: Colors.black54),
            ),
          ],
        ],
      ),
      ),
    );
  }

  Widget _buildChapterBlockCard(Map<String, dynamic> block) {
    // For rendering, we will utilize the existing BlockRegistry to get the true UI
    // But we will wrap it in a card and add a chapter context header
    
    String chapterContext = block['_chapter_context'] ?? 'Chapter';
    
    return Card(
      elevation: 2,
      margin: const EdgeInsets.only(bottom: 16),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 10),
            decoration: BoxDecoration(
              color: Colors.blueGrey.shade50,
              borderRadius: const BorderRadius.only(topLeft: Radius.circular(16), topRight: Radius.circular(16)),
            ),
            child: Row(
              children: [
                const Icon(Icons.subject, size: 16, color: Colors.blueGrey),
                const SizedBox(width: 8),
                Expanded(
                  child: Text(
                    chapterContext,
                    style: TextStyle(fontSize: 12, fontWeight: FontWeight.bold, color: Colors.blueGrey.shade700),
                  ),
                ),
              ],
            ),
          ),
          Padding(
            padding: const EdgeInsets.all(16),
            child: BlockRegistry.instance.build(block) ?? const SizedBox.shrink(),
          ),
        ],
      ),
    );
  }
}
