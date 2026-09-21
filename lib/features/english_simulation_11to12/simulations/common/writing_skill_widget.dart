import 'package:flutter/material.dart';
import 'sim_frame.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// One exam-style writing prompt paired with a complete, board-ready model
/// answer a student can study directly — not just a rule about the format.
class WritingPrompt {
  final String prompt;
  final String modelAnswer; // full text, using \n for line breaks
  final String? wordCount;

  const WritingPrompt({required this.prompt, required this.modelAnswer, this.wordCount});
}

/// Shows a quick format checklist followed by one or more [WritingPrompt]s,
/// each with a complete model answer a student can expand to study. Meant
/// to be the primary teaching content for a writing-skill chapter (Notice,
/// Letter, Report, Essay, Email, Dialogue, ...) so a student never needs to
/// look the format up in another book.
class WritingSkillWidget extends StatefulWidget {
  final String title;
  final IconData icon;
  final Color accent;
  final String description;
  final List<String> formatPoints;
  final List<WritingPrompt> prompts;

  const WritingSkillWidget({
    super.key,
    required this.title,
    required this.icon,
    required this.accent,
    required this.description,
    required this.formatPoints,
    required this.prompts,
  });

  @override
  State<WritingSkillWidget> createState() => _WritingSkillWidgetState();
}

class _WritingSkillWidgetState extends State<WritingSkillWidget> {
  @override
  Widget build(BuildContext context) {
    return SimFrame(
      title: widget.title,
      icon: widget.icon,
      accent: widget.accent,
      description: widget.description,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Container(
            width: double.infinity,
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: widget.accent.withValues(alpha: 0.07),
              borderRadius: BorderRadius.circular(10),
              border: Border.all(color: widget.accent.withValues(alpha: 0.25)),
            ),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Row(children: [
                  Icon(Icons.checklist_rtl, size: 18, color: widget.accent),
                  const SizedBox(width: 6),
                  Text(TrilingualService.instance.getUIText('Format at a Glance'), style: TextStyle(fontWeight: FontWeight.bold, fontSize: 13.5, color: widget.accent)),
                ]),
                const SizedBox(height: 8),
                ...widget.formatPoints.map((p) => Padding(
                      padding: const EdgeInsets.only(bottom: 5),
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Icon(Icons.check_circle, size: 14, color: widget.accent.withValues(alpha: 0.8)),
                          const SizedBox(width: 6),
                          Expanded(child: Text(p, style: TextStyle(fontSize: 12.5, height: 1.35))),
                        ],
                      ),
                    )),
              ],
            ),
          ),
          const SizedBox(height: 14),
          for (int i = 0; i < widget.prompts.length; i++) ...[
            _PromptCard(index: i, prompt: widget.prompts[i], accent: widget.accent, initiallyExpanded: i == 0),
            if (i != widget.prompts.length - 1) const SizedBox(height: 10),
          ],
        ],
      ),
    );
  }
}

class _PromptCard extends StatefulWidget {
  final int index;
  final WritingPrompt prompt;
  final Color accent;
  final bool initiallyExpanded;

  const _PromptCard({required this.index, required this.prompt, required this.accent, required this.initiallyExpanded});

  @override
  State<_PromptCard> createState() => _PromptCardState();
}

class _PromptCardState extends State<_PromptCard> {
  late bool _expanded = widget.initiallyExpanded;

  @override
  Widget build(BuildContext context) {
    return Container(
      width: double.infinity,
      decoration: BoxDecoration(
        borderRadius: BorderRadius.circular(10),
        border: Border.all(color: Colors.grey.shade300),
      ),
      clipBehavior: Clip.antiAlias,
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          InkWell(
            onTap: () => setState(() => _expanded = !_expanded),
            child: Container(
              width: double.infinity,
              padding: const EdgeInsets.all(12),
              color: Colors.grey.shade50,
              child: Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  CircleAvatar(
                    radius: 12,
                    backgroundColor: widget.accent,
                    child: Text('${widget.index + 1}', style: TextStyle(color: Colors.white, fontSize: 11, fontWeight: FontWeight.bold)),
                  ),
                  const SizedBox(width: 10),
                  Expanded(
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Text(widget.prompt.prompt, style: TextStyle(fontSize: 13, fontWeight: FontWeight.w600, height: 1.35)),
                        if (widget.prompt.wordCount != null) ...[
                          const SizedBox(height: 3),
                          Text(widget.prompt.wordCount!, style: TextStyle(fontSize: 11, color: widget.accent, fontWeight: FontWeight.w500)),
                        ],
                      ],
                    ),
                  ),
                  Icon(_expanded ? Icons.expand_less : Icons.expand_more, color: Theme.of(context).colorScheme.onSurface.withOpacity(0.45)),
                ],
              ),
            ),
          ),
          AnimatedCrossFade(
            duration: const Duration(milliseconds: 200),
            crossFadeState: _expanded ? CrossFadeState.showFirst : CrossFadeState.showSecond,
            firstChild: Container(
              width: double.infinity,
              padding: const EdgeInsets.all(14),
              color: const Color(0xFFFFFDF7),
              child: Text(
                widget.prompt.modelAnswer,
                style: TextStyle(fontSize: 13, height: 1.55, fontFamily: 'monospace'),
              ),
            ),
            secondChild: const SizedBox(width: double.infinity),
          ),
        ],
      ),
    );
  }
}
