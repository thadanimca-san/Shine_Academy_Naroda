import 'package:flutter/foundation.dart';
import 'package:shine_academy_naroda/core/engine/curriculum_database.dart';
import 'package:shine_academy_naroda/core/services/universal_dictionary_service.dart';
import 'models/knowledge_graph_models.dart';

class KnowledgeGraphService {
  static final KnowledgeGraphService instance = KnowledgeGraphService._internal();
  KnowledgeGraphService._internal();

  bool _isLoaded = false;
  final Map<String, KnowledgeNode> _nodes = {};
  final List<KnowledgeEdge> _edges = [];

  bool get isLoaded => _isLoaded;
  Map<String, KnowledgeNode> get nodes => _nodes;
  List<KnowledgeEdge> get edges => _edges;

  Future<void> buildGraph() async {
    if (_isLoaded) return;
    try {
      // 1. Add Chapter Nodes
      final chapterIds = CurriculumDatabase.instance.allModuleIds;
      for (final id in chapterIds) {
        final meta = CurriculumDatabase.instance.getModuleMetadata(id);
        if (meta != null) {
          final title = meta['title'] ?? id;
          final subtitle = '${meta['board'] ?? ''} Class ${meta['grade'] ?? ''} ${meta['subject'] ?? ''}'.trim();
          _nodes[id] = KnowledgeNode(
            id: id,
            title: title,
            subtitle: subtitle,
            type: NodeType.chapter,
          );
        }
      }

      // 2. Add Dictionary Nodes & Edges
      if (UniversalDictionaryService.instance.isInitialized) {
        final terms = await UniversalDictionaryService.instance.getAllTerms();
        for (final term in terms) {
          final id = term['id'] ?? '';
          if (id.isEmpty) continue;

          // Parse title (fallback to english term)
          String title = id;
          if (term['term'] != null && term['term']['english'] != null) {
            title = term['term']['english'];
          } else if (term['word_en'] != null) {
             title = term['word_en'];
          }

          _nodes[id] = KnowledgeNode(
            id: id,
            title: title,
            subtitle: 'Concept',
            type: NodeType.dictionaryTerm,
          );

          // Parse Edges
          if (term.containsKey('knowledge_graph_links')) {
            final links = term['knowledge_graph_links'];
            
            // Prerequisites
            if (links['prerequisites'] is List) {
              for (final target in links['prerequisites']) {
                _edges.add(KnowledgeEdge(sourceId: target.toString(), targetId: id, relationshipType: EdgeType.prerequisite));
              }
            }
            
            // Related
            if (links['related'] is List) {
              for (final target in links['related']) {
                _edges.add(KnowledgeEdge(sourceId: id, targetId: target.toString(), relationshipType: EdgeType.related));
              }
            }

            // Used In
            if (links['used_in'] is List) {
              for (final target in links['used_in']) {
                _edges.add(KnowledgeEdge(sourceId: id, targetId: target.toString(), relationshipType: EdgeType.usedIn));
              }
            }
          }
        }
      }

      _isLoaded = true;
      debugPrint("Knowledge Graph built with ${_nodes.length} nodes and ${_edges.length} edges.");
    } catch (e) {
      debugPrint("Error building knowledge graph: $e");
    }
  }

  /// Get prerequisites (edges pointing TO the node)
  List<KnowledgeNode> getPrerequisites(String nodeId) {
    final edgeList = _edges.where((e) => e.targetId == nodeId && e.relationshipType == EdgeType.prerequisite).toList();
    return edgeList.map((e) => _nodes[e.sourceId]).whereType<KnowledgeNode>().toList();
  }

  /// Get next topics (edges pointing FROM the node as prerequisite)
  List<KnowledgeNode> getNextTopics(String nodeId) {
    final edgeList = _edges.where((e) => e.sourceId == nodeId && e.relationshipType == EdgeType.prerequisite).toList();
    return edgeList.map((e) => _nodes[e.targetId]).whereType<KnowledgeNode>().toList();
  }

  /// Get chapters this concept is used in
  List<KnowledgeNode> getUsedInChapters(String nodeId) {
    final edgeList = _edges.where((e) => e.sourceId == nodeId && e.relationshipType == EdgeType.usedIn).toList();
    return edgeList.map((e) => _nodes[e.targetId]).whereType<KnowledgeNode>().toList();
  }
}
