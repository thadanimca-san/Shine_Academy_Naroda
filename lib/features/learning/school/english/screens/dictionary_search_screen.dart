import 'package:flutter/material.dart';

import '../theme/app_theme.dart';
import '../widgets/dictionary_word_widgets.dart';
import '../../../../../core/services/universal_dictionary_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

class DictionarySearchScreen extends StatefulWidget {
  const DictionarySearchScreen({super.key});

  @override
  State<DictionarySearchScreen> createState() => _DictionarySearchScreenState();
}

class _DictionarySearchScreenState extends State<DictionarySearchScreen> {
  final _searchController = TextEditingController();
  String _query = '';
  List<Map<String, dynamic>> _matches = [];
  bool _isSearching = false;

  @override
  void initState() {
    super.initState();
    TrilingualService.instance.addListener(_onLanguageChanged);
  }

  void _onLanguageChanged() {
    if (_matches.isNotEmpty) {
      TrilingualService.instance.preTranslateBlocks(_matches, isDictionary: true).then((_) {
        if (mounted) setState(() {});
      });
    }
  }

  @override
  void dispose() {
    TrilingualService.instance.removeListener(_onLanguageChanged);
    _searchController.dispose();
    super.dispose();
  }

  Future<void> _performSearch(String query) async {
    final queryLower = query.trim().toLowerCase();
    if (queryLower.isEmpty) {
      setState(() {
        _matches = [];
        _isSearching = false;
      });
      return;
    }
    
    setState(() => _isSearching = true);
    
    // Fetch terms matching query from the Universal Dictionary Service directly
    final matches = await UniversalDictionaryService.instance.searchTerms(queryLower);

    matches.sort((a, b) {
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
      
      bool aStarts = aText.startsWith(queryLower);
      bool bStarts = bText.startsWith(queryLower);
      
      if (aStarts && !bStarts) return -1;
      if (!aStarts && bStarts) return 1;
      
      return aText.compareTo(bText);
    });

    // Limit to 50 matches to prevent rate limit bans from Google Translate
    final limitedMatches = matches.take(50).toList();
    
    await TrilingualService.instance.preTranslateBlocks(limitedMatches, isDictionary: true);
    
    if (mounted) {
      setState(() {
        _matches = limitedMatches;
        _isSearching = false;
      });
    }
  }

  @override
  Widget build(BuildContext context) {
    final query = _query.trim().toLowerCase();

    return Scaffold(
      appBar: BrandAppBar(title: TrilingualService.instance.getUIText('Universal Dictionary Search')),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 16, 16, 8),
            child: TextField(
              controller: _searchController,
              autofocus: true,
              onChanged: (v) {
                _query = v;
                _performSearch(v);
              },
              decoration: InputDecoration(
                hintText: 'Search any word (English, Hindi, Gujarati)...',
                prefixIcon: Icon(Icons.search),
                filled: true,
                fillColor: AppColors.paperRaised,
                border: OutlineInputBorder(
                  borderRadius: BorderRadius.circular(12),
                  borderSide: BorderSide.none,
                ),
                contentPadding: EdgeInsets.zero,
              ),
            ),
          ),
          const SizedBox(height: 4),
          Expanded(
            child: _isSearching
                ? const Center(child: CircularProgressIndicator())
                : _buildResults(query, _matches),
          ),
        ],
      ),
    );
  }

  Widget _buildResults(String query, List<Map<String, dynamic>> matches) {
    if (query.isEmpty) {
      return  Center(
        child: Padding(
          padding: EdgeInsets.all(24),
          child: Text(TrilingualService.instance.getUIText('Start typing to search every word stored in the Universal Dictionary.'),
            textAlign: TextAlign.center,
            style: TextStyle(color: AppColors.inkFaint, fontSize: 16),
          ),
        ),
      );
    }
    if (matches.isEmpty) {
      return Center(child: Text(TrilingualService.instance.getUIText('No words found in dictionary.'), style: TextStyle(color: AppColors.inkFaint, fontSize: 16)));
    }
    return ListView.builder(
      padding: const EdgeInsets.all(16),
      itemCount: matches.length + 1,
      itemBuilder: (context, index) {
        if (index == 0) {
          return Padding(
            padding: EdgeInsets.only(bottom: 10),
            child: Text(TrilingualService.instance.getUIText('Tap any word or picture to see its meaning, pronunciation, and an example.'),
              style: TextStyle(fontSize: 12, color: AppColors.inkFaint, fontStyle: FontStyle.italic),
            ),
          );
        }
        final termMap = matches[index - 1];
        return Padding(
          padding: const EdgeInsets.only(bottom: 10),
          child: DictionaryWordCard(word: termMap),
        );
      },
    );
  }
}
