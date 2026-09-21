import 'package:flutter/widgets.dart';

/// Content availability for a syllabus topic.
enum TopicStatus { available, comingSoon }

/// A single learnable topic. `id` is a stable key — progress storage and the
/// future backend both reference it, so never rename ids once shipped.
class Topic {
  final String id;
  final String title;
  final String tagline;
  final IconData icon;
  final TopicStatus status;
  final WidgetBuilder? builder;
  final bool highYield;

  const Topic({
    required this.id,
    required this.title,
    required this.tagline,
    required this.icon,
    this.status = TopicStatus.comingSoon,
    this.builder,
    this.highYield = false,
  });

  bool get isAvailable => status == TopicStatus.available && builder != null;
}

/// A chapter groups topics the way JEE/NEET students revise them.
class Chapter {
  final String id;
  final String title;
  final String unit;
  final IconData icon;
  final Color tint;
  final List<Topic> topics;

  const Chapter({
    required this.id,
    required this.title,
    required this.unit,
    required this.icon,
    required this.tint,
    required this.topics,
  });

  int get availableCount => topics.where((t) => t.isAvailable).length;
}
