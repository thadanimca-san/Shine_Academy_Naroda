enum NodeType {
  chapter,
  dictionaryTerm
}

class KnowledgeNode {
  final String id;
  final String title;
  final String subtitle;
  final NodeType type;

  KnowledgeNode({
    required this.id,
    required this.title,
    required this.subtitle,
    required this.type,
  });

  @override
  bool operator ==(Object other) =>
      identical(this, other) ||
      other is KnowledgeNode && runtimeType == other.runtimeType && id == other.id;

  @override
  int get hashCode => id.hashCode;
}

enum EdgeType {
  prerequisite,
  nextTopic,
  related,
  usedIn
}

class KnowledgeEdge {
  final String sourceId;
  final String targetId;
  final EdgeType relationshipType;

  KnowledgeEdge({
    required this.sourceId,
    required this.targetId,
    required this.relationshipType,
  });
}
