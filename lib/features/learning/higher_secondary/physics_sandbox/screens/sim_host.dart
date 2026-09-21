import 'package:flutter/material.dart';
import '../models/syllabus.dart';
import '../services/progress_service.dart';
import '../theme/tokens.dart';

/// Hosts a simulator screen and fixes system-chrome issues in one place:
/// bottom controls are inset above the Android gesture / 3-button nav bar so
/// nothing hides behind it, and opening a topic records progress.
class SimHost extends StatefulWidget {
  final Topic topic;
  const SimHost({super.key, required this.topic});

  static Route<void> route(Topic topic) =>
      MaterialPageRoute(builder: (_) => SimHost(topic: topic));

  @override
  State<SimHost> createState() => _SimHostState();
}

class _SimHostState extends State<SimHost> {
  @override
  void initState() {
    super.initState();
    ProgressService.instance.markVisited(widget.topic.id);
  }

  @override
  Widget build(BuildContext context) {
    return ColoredBox(
      color: Palette.bg,
      child: SafeArea(
        top: false,
        left: false,
        right: false,
        child: widget.topic.builder!(context),
      ),
    );
  }
}
