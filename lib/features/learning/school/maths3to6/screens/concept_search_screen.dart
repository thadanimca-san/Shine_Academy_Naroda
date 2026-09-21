import 'package:flutter/material.dart';

import '../data/concept_topics.dart';
import '../models/concept.dart';
import '../theme/app_theme.dart';
import '../widgets/concept_widgets.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Searches every maths term across every grade (Class 3-6) at once —
/// unlike the per-grade search inside ConceptBrowseScreen, which only
/// searches within the one grade currently open.
class ConceptSearchScreen extends StatefulWidget {
  const ConceptSearchScreen({super.key});

  @override
  State<ConceptSearchScreen> createState() => _ConceptSearchScreenState();
}

class _MatchedConcept {
  final Concept concept;
  final String grade;

  const _MatchedConcept({required this.concept, required this.grade});
}

class _ConceptSearchScreenState extends State<ConceptSearchScreen> {
  final _searchController = TextEditingController();
  String _query = '';
  String? _gradeFilter;

  @override
  void dispose() {
    _searchController.dispose();
    super.dispose();
  }

  List<_MatchedConcept> get _allConceptsFlattened {
    final result = <_MatchedConcept>[];
    for (final entry in conceptTopicByGrade.entries) {
      for (final concept in entry.value.concepts) {
        result.add(_MatchedConcept(concept: concept, grade: entry.key));
      }
    }
    return result;
  }

  @override
  Widget build(BuildContext context) {
    final query = _query.trim().toLowerCase();
    final matches = query.isEmpty
        ? const <_MatchedConcept>[]
        : _allConceptsFlattened.where((m) {
            final matchesGrade = _gradeFilter == null || m.grade == _gradeFilter;
            final matchesQuery = m.concept.term.toLowerCase().contains(query) ||
                m.concept.meaningHi.contains(_query.trim()) ||
                m.concept.meaningEn.toLowerCase().contains(query);
            return matchesGrade && matchesQuery;
          }).toList();
          
    matches.sort((a, b) {
      return a.concept.term.toLowerCase().compareTo(b.concept.term.toLowerCase());
    });

    return Scaffold(
      appBar: AppBar(title: Text(TrilingualService.instance.getUIText('Search all terms'))),
      body: Column(
        children: [
          Padding(
            padding: const EdgeInsets.fromLTRB(16, 8, 16, 8),
            child: TextField(
              controller: _searchController,
              autofocus: true,
              onChanged: (v) => setState(() => _query = v),
              decoration: InputDecoration(
                hintText: 'Search any term, in English or Hindi...',
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
                _GradeChip(
                  label: 'All grades',
                  selected: _gradeFilter == null,
                  onTap: () => setState(() => _gradeFilter = null),
                ),
                ...conceptTopicByGrade.keys.map(
                  (g) => _GradeChip(
                    label: g,
                    selected: _gradeFilter == g,
                    onTap: () => setState(() => _gradeFilter = g),
                  ),
                ),
              ],
            ),
          ),
          const SizedBox(height: 4),
          Expanded(
            child: _buildResults(query, matches),
          ),
        ],
      ),
    );
  }

  Widget _buildResults(String query, List<_MatchedConcept> matches) {
    if (query.isEmpty) {
      return  Center(
        child: Padding(
          padding: EdgeInsets.all(24),
          child: Text(TrilingualService.instance.getUIText('Start typing to search every term across all grades.'),
            textAlign: TextAlign.center,
            style: TextStyle(color: AppColors.inkFaint),
          ),
        ),
      );
    }
    if (matches.isEmpty) {
      return Center(child: Text(TrilingualService.instance.getUIText('No terms found.'), style: TextStyle(color: AppColors.inkFaint)));
    }
    return GridView.builder(
      padding: const EdgeInsets.all(16),
      gridDelegate: const SliverGridDelegateWithMaxCrossAxisExtent(
        maxCrossAxisExtent: 320,
        mainAxisExtent: 150,
        crossAxisSpacing: 10,
        mainAxisSpacing: 10,
      ),
      itemCount: matches.length,
      itemBuilder: (context, index) {
        final m = matches[index];
        return ConceptCard(concept: m.concept, gradeLabel: m.grade);
      },
    );
  }
}

class _GradeChip extends StatelessWidget {
  final String label;
  final bool selected;
  final VoidCallback onTap;

  const _GradeChip({required this.label, required this.selected, required this.onTap});

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
