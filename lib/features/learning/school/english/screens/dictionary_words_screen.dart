import 'package:flutter/material.dart';

import '../models/dictionary_word.dart';
import '../theme/app_theme.dart';
import '../widgets/admin_edit_button.dart';
import '../widgets/dictionary_word_widgets.dart';
import '../../../../../core/services/universal_dictionary_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

class DictionaryWordsScreen extends StatefulWidget {
  final DictionaryTopic topic;

  const DictionaryWordsScreen({super.key, required this.topic});

  @override
  State<DictionaryWordsScreen> createState() => _DictionaryWordsScreenState();
}

class _DictionaryWordsScreenState extends State<DictionaryWordsScreen> {
  String? _selectedCategory;
  final _searchController = TextEditingController();
  String _query = '';
  List<Map<String, dynamic>> _allWords = [];
  bool _isLoading = true;

  @override
  void initState() {
    super.initState();
    _loadWords();
    TrilingualService.instance.addListener(_onLanguageChanged);
  }

  void _onLanguageChanged() {
    if (_allWords.isNotEmpty) {
      TrilingualService.instance.preTranslateBlocks(_allWords, isDictionary: true).then((_) {
        if (mounted) setState(() {});
      });
    }
  }

  Future<void> _loadWords() async {
    List<Map<String, dynamic>> words = [];
    
    // Legacy support
    if (widget.topic.words.isNotEmpty) {
      words = widget.topic.words.map((w) => {
        'term': {'english': w.word, 'hindi': w.meaningHi, 'gujarati': w.meaningGu ?? ''},
        'definition': {'simple': {'en': w.meaningEn, 'hi': w.meaningHi, 'gu': w.meaningGu ?? ''}},
        'examples': [
          {'en': w.exampleEn, 'hi': w.exampleHi ?? '', 'gu': w.exampleGu ?? ''}
        ],
        'media': {'emoji': w.emoji, 'imagePath': w.imagePath},
        'part_of_speech': w.partOfSpeech,
        'category': w.category,
      }).toList();
    } 
    // New JSON support
    else if (widget.topic.wordIds != null) {
      final service = UniversalDictionaryService.instance;
      for (String id in widget.topic.wordIds!) {
        final term = await service.getTermById(id);
        if (term != null) {
          words.add(term);
        }
      }
    }

    await TrilingualService.instance.preTranslateBlocks(words, isDictionary: true);

    if (mounted) {
      setState(() {
        _allWords = words;
        _isLoading = false;
      });
    }
  }

  @override
  void dispose() {
    TrilingualService.instance.removeListener(_onLanguageChanged);
    _searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    if (_isLoading) {
      return Scaffold(
        appBar: BrandAppBar(title: widget.topic.title),
        body: const Center(child: CircularProgressIndicator()),
      );
    }

    List<Map<String, dynamic>> words = _allWords.where((w) {
      final category = w['category'] as String?;
      final termEn = w['term']?['english']?.toString().toLowerCase() ?? '';
      final termHi = (w['term']?['hindi'] ?? w['term']?['hi'])?.toString() ?? '';
      final termGu = (w['term']?['gujarati'] ?? w['term']?['gu'])?.toString() ?? '';
      
      final matchesCategory = _selectedCategory == null || category == _selectedCategory;
      final matchesQuery = _query.trim().isEmpty ||
          termEn.contains(_query.trim().toLowerCase()) ||
          termHi.contains(_query.trim()) ||
          termGu.contains(_query.trim());
      return matchesCategory && matchesQuery;
    }).toList();

    words.sort((a, b) {
      final lang = TrilingualService.instance.activeViewLanguage;
      String aText = '';
      String bText = '';
      
      if (lang == 'gu') {
        aText = (a['term']?['gujarati'] ?? a['term']?['gu'] ?? a['term']?['english'] ?? '').toString().toLowerCase();
        bText = (b['term']?['gujarati'] ?? b['term']?['gu'] ?? b['term']?['english'] ?? '').toString().toLowerCase();
      } else if (lang == 'hi') {
        aText = (a['term']?['hindi'] ?? a['term']?['hi'] ?? a['term']?['english'] ?? '').toString().toLowerCase();
        bText = (b['term']?['hindi'] ?? b['term']?['hi'] ?? b['term']?['english'] ?? '').toString().toLowerCase();
      } else {
        aText = (a['term']?['english'] ?? '').toString().toLowerCase();
        bText = (b['term']?['english'] ?? '').toString().toLowerCase();
      }
      return aText.compareTo(bText);
    });

    return Scaffold(
      appBar: BrandAppBar(
        title: widget.topic.title,
        actions: [
          AdminEditButton(
            jsonPath: 'app_core/english/dictionary/${widget.topic.id}.json',
            data: {
              'id': widget.topic.id,
              'title': widget.topic.title,
              'grade': widget.topic.grade,
              'word_ids': widget.topic.wordIds ?? [],
            },
          ),
        ],
      ),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
            child: TextField(
              controller: _searchController,
              onChanged: (v) => setState(() => _query = v),
              decoration: InputDecoration(
                hintText: 'Search within ${widget.topic.title}...',
                prefixIcon: Icon(Icons.search),
                filled: true,
                fillColor: AppColors.paperRaised,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(10),
                  borderSide: const BorderSide(color: AppColors.rule),
                ),
                contentPadding: const EdgeInsets.symmetric(vertical: 0, horizontal: 14),
              ),
            ),
          ),
          SizedBox(
            height: 40,
            child: ListView(
              scrollDirection: Axis.horizontal,
              padding: const EdgeInsets.symmetric(horizontal: 12),
              children: [
                _CategoryChip(
                  label: 'All',
                  selected: _selectedCategory == null,
                  onTap: () => setState(() => _selectedCategory = null),
                ),
                ...words.map((w) => w['category'] as String?).where((c) => c != null).toSet().cast<String>().map(
                  (c) => _CategoryChip(
                    label: c,
                    selected: _selectedCategory == c,
                    onTap: () => setState(() => _selectedCategory = c),
                  ),
                ),
              ],
            ),
          ),
          Padding(
            padding: EdgeInsets.fromLTRB(16, 0, 16, 8),
            child: Text(TrilingualService.instance.getUIText('Tap any word or picture to see its meaning, pronunciation, and an example.'),
              style: TextStyle(fontSize: 11.5, color: AppColors.inkFaint, fontStyle: FontStyle.italic),
            ),
          ),
          Expanded(
            child: words.isEmpty
                ? Center(child: Text(TrilingualService.instance.getUIText('No words found.'), style: TextStyle(color: AppColors.inkFaint)))
                : GridView.builder(
                    padding: const EdgeInsets.all(16),
                    gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
                      maxCrossAxisExtent: 320,
                      mainAxisExtent: 150,
                      crossAxisSpacing: 10,
                      mainAxisSpacing: 10,
                    ),
                    itemCount: words.length,
                    itemBuilder: (context, index) => DictionaryWordCard(word: words[index]),
                  ),
          ),
        ],
      ),
    );
  }
}

class _CategoryChip extends StatelessWidget {
  final String label;
  final bool selected;
  final VoidCallback onTap;

  const _CategoryChip({required this.label, required this.selected, required this.onTap});

  @override
  Widget build(BuildContext context) {
    return Padding(
      padding: const EdgeInsets.only(right: 8),
      child: ChoiceChip(
        label: Text(label),
        selected: selected,
        onSelected: (_) => onTap(),
        selectedColor: AppColors.saffronTint,
        labelStyle: TextStyle(
          color: selected ? AppColors.saffronDeep : AppColors.inkSoft,
          fontWeight: selected ? FontWeight.w600 : FontWeight.w400,
        ),
        side: const BorderSide(color: AppColors.rule),
        backgroundColor: AppColors.paper,
      ),
    );
  }
}
