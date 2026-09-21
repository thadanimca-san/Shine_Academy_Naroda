import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class UniversalBlockWrapper extends StatefulWidget {
  final Map<String, dynamic> block;
  final Widget child;

  const UniversalBlockWrapper({super.key, required this.block, required this.child});

  @override
  State<UniversalBlockWrapper> createState() => _UniversalBlockWrapperState();
}

class _UniversalBlockWrapperState extends State<UniversalBlockWrapper> {
  bool _isRevealed = false;
  
  @override
  void initState() {
    super.initState();
    if (widget.block['presentation']?['reveal_mode'] == true) {
      _isRevealed = false;
    } else {
      _isRevealed = true;
    }
  }

  void _reveal() {
    setState(() => _isRevealed = true);
  }

  @override
  Widget build(BuildContext context) {
    final presentation = widget.block['presentation'] ?? {};
    final bool hasReveal = presentation['reveal_mode'] == true;
    final bool isHighlighted = presentation['highlight'] == true;
    final String? teacherNotes = presentation['teacher_notes'];

    Widget content = widget.child;

    if (hasReveal && !_isRevealed) {
      return InkWell(
        onTap: _reveal,
        child: Container(
          width: double.infinity,
          padding: const EdgeInsets.all(24),
          margin: const EdgeInsets.symmetric(vertical: 8),
          decoration: BoxDecoration(
            color: Colors.grey.shade200,
            borderRadius: BorderRadius.circular(12),
          ),
          child: Center(
            child: Text(TrilingualService.instance.getUIText("Click to Reveal"), style: TextStyle(color: Colors.grey, fontSize: 18, fontWeight: FontWeight.bold)),
          ),
        ),
      );
    }

    if (isHighlighted) {
      content = Container(
        padding: const EdgeInsets.all(4),
        decoration: BoxDecoration(
          border: Border.all(color: Colors.amber, width: 3),
          borderRadius: BorderRadius.circular(12),
          boxShadow: [
            BoxShadow(color: Colors.amber.withValues(alpha: 0.2), blurRadius: 10, spreadRadius: 2)
          ]
        ),
        child: content,
      );
    }

    if (teacherNotes != null && _isRevealed) {
      content = Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          content,
          Container(
            margin: const EdgeInsets.only(top: 8, bottom: 8),
            padding: const EdgeInsets.all(12),
            decoration: BoxDecoration(
              color: Colors.blue.shade50,
              borderRadius: BorderRadius.circular(8),
              border: Border.all(color: Colors.blue.shade200),
            ),
            child: Row(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                Icon(Icons.lightbulb, color: Colors.blue),
                const SizedBox(width: 8),
                Expanded(child: Text(teacherNotes, style: TextStyle(color: Colors.blueGrey, fontStyle: FontStyle.italic))),
              ],
            ),
          )
        ],
      );
    }

    if (presentation['animation'] == 'fade_in') {
      content = TweenAnimationBuilder(
        tween: Tween<double>(begin: 0, end: 1),
        duration: const Duration(milliseconds: 800),
        builder: (context, double val, child) {
          return Opacity(opacity: val, child: child);
        },
        child: content,
      );
    }

    return content;
  }
}
