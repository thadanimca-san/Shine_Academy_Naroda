import 'package:flutter/material.dart';

import '../data/concept_topics.dart';
import '../models/concept.dart';
import '../theme/app_theme.dart';
import '../widgets/concept_widgets.dart';
import 'concept_search_screen.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Grade picker for the Maths Glossary — the maths equivalent of the
/// sister English app's Picture Dictionary.
class ConceptGradeListScreen extends StatelessWidget {
  const ConceptGradeListScreen({super.key});

  @override
  Widget build(BuildContext context) {
    final grades = conceptTopicByGrade.keys.toList();
    final totalTerms = conceptTopicByGrade.values.fold<int>(0, (sum, t) => sum + t.concepts.length);

    return Scaffold(
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Maths Glossary')),
        actions: [
          IconButton(
            icon: Icon(Icons.search),
            tooltip: 'Search all terms',
            onPressed: () => Navigator.of(context).push(
              MaterialPageRoute(builder: (_) => const ConceptSearchScreen()),
            ),
          ),
        ],
      ),
      body: ListView(
        padding: const EdgeInsets.all(16),
        children: [
          InkWell(
            borderRadius: BorderRadius.circular(12),
            onTap: () => Navigator.of(context).push(
              MaterialPageRoute(builder: (_) => const ConceptSearchScreen()),
            ),
            child: Container(
              padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 14),
              margin: const EdgeInsets.only(bottom: 16),
              decoration: BoxDecoration(
                color: AppColors.tealTint,
                borderRadius: BorderRadius.circular(12),
                border: Border.all(color: AppColors.rule),
              ),
              child: Row(
                children: [
                  Icon(Icons.search, color: AppColors.tealDeep),
                  const SizedBox(width: 12),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(TrilingualService.instance.getUIText('Search all terms'), style: TextStyle(fontWeight: FontWeight.w700, color: AppColors.tealDeep)),
                        Text('Across every grade · $totalTerms terms',
                            style: TextStyle(fontSize: 12, color: AppColors.inkSoft)),
                      ],
                    ),
                  ),
                  Icon(Icons.chevron_right, color: AppColors.inkFaint),
                ],
              ),
            ),
          ),
          ...grades.map((grade) {
            final topic = conceptTopicByGrade[grade]!;
            return Padding(
              padding: const EdgeInsets.only(bottom: 10),
              child: Card(
                child: ListTile(
                  contentPadding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
                  leading: CircleAvatar(
                    backgroundColor: AppColors.indigoTint,
                    child: Text(TrilingualService.instance.getUIText('📘'), style: TextStyle(fontSize: 18)),
                  ),
                  title: Text(grade, style: Theme.of(context).textTheme.titleMedium),
                  subtitle: Text('${topic.concepts.length} terms'),
                  trailing: Icon(Icons.chevron_right, color: AppColors.inkFaint),
                  onTap: () => Navigator.of(context).push(
                    MaterialPageRoute(builder: (_) => ConceptBrowseScreen(topic: topic)),
                  ),
                ),
              ),
            );
          }),
        ],
      ),
    );
  }
}

class ConceptBrowseScreen extends StatefulWidget {
  final ConceptTopic topic;

  const ConceptBrowseScreen({super.key, required this.topic});

  @override
  State<ConceptBrowseScreen> createState() => _ConceptBrowseScreenState();
}

class _ConceptBrowseScreenState extends State<ConceptBrowseScreen> {
  String? _selectedCategory;
  final _searchController = TextEditingController();
  String _query = '';

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    final terms = widget.topic.concepts.where((c) {
      final matchesCategory = _selectedCategory == null || c.category == _selectedCategory;
      final matchesQuery = _query.isEmpty ||
          c.term.toLowerCase().contains(_query.toLowerCase()) ||
          c.meaningHi.contains(_query);
      return matchesCategory && matchesQuery;
    }).toList();

    return Scaffold(
      appBar: AppBar(title: Text('${widget.topic.grade} Glossary')),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
            child: TextField(
              controller: _searchController,
              onChanged: (v) => setState(() => _query = v),
              decoration: InputDecoration(
                hintText: 'Search within this glossary...',
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
                ...widget.topic.categories.map(
                  (c) => _CategoryChip(
                    label: c,
                    selected: _selectedCategory == c,
                    onTap: () => setState(() => _selectedCategory = c),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 4),
          Expanded(
            child: terms.isEmpty
                ? Center(child: Text(TrilingualService.instance.getUIText('No terms found.'), style: TextStyle(color: AppColors.inkFaint)))
                : GridView.builder(
                    padding: const EdgeInsets.all(16),
                    gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
                      maxCrossAxisExtent: 320,
                      mainAxisExtent: 150,
                      crossAxisSpacing: 10,
                      mainAxisSpacing: 10,
                    ),
                    itemCount: terms.length,
                    itemBuilder: (context, index) => ConceptCard(concept: terms[index]),
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
        selectedColor: AppColors.indigoTint,
        labelStyle: TextStyle(
          color: selected ? AppColors.indigoDeep : AppColors.inkSoft,
          fontWeight: selected ? FontWeight.w600 : FontWeight.w400,
        ),
        side: const BorderSide(color: AppColors.rule),
        backgroundColor: AppColors.paper,
      ),
    );
  }
}
