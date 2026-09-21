import 'package:flutter/material.dart';
import '../../../../core/services/tts_service.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PhonicsBlenderWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const PhonicsBlenderWidget({super.key, required this.data});

  @override
  State<PhonicsBlenderWidget> createState() => _PhonicsBlenderWidgetState();
}

class _PhonicsBlenderWidgetState extends State<PhonicsBlenderWidget> {
  int _highlightIndex = -1;

  Future<void> _speak(String text, int index) async {
    setState(() => _highlightIndex = index);
    TTSService.instance.setSpeed(TTSSpeed.slow); // slow for phonics
    await TTSService.instance.speak(text);
    // Short delay so highlight doesn't instantly vanish
    await Future.delayed(const Duration(milliseconds: 500));
    if (mounted) setState(() => _highlightIndex = -1);
  }

  Future<void> _playSequence() async {
    final List<dynamic> parts = widget.data['parts'] ?? [];
    final String result = widget.data['result'] ?? '';

    // Speak parts
    for (int i = 0; i < parts.length; i++) {
      await _speak(parts[i].toString(), i);
      await Future.delayed(const Duration(milliseconds: 400));
    }

    // Speak result
    if (result.isNotEmpty) {
      await _speak(result, parts.length);
    }
  }

  Widget _buildTile(String text, int index, bool isResult) {
    bool isHighlighted = _highlightIndex == index;
    return GestureDetector(
      onTap: () => _speak(text, index),
      child: AnimatedContainer(
        duration: const Duration(milliseconds: 200),
        padding: const EdgeInsets.symmetric(horizontal: 16, vertical: 12),
        decoration: BoxDecoration(
          color: isHighlighted 
              ? (isResult ? Colors.green.shade100 : Colors.blue.shade100)
              : (isResult ? Colors.green.shade50 : Colors.blue.shade50),
          borderRadius: BorderRadius.circular(16),
          border: Border.all(
            color: isHighlighted 
                ? (isResult ? Colors.green : Colors.blue) 
                : Colors.transparent,
            width: 3,
          ),
          boxShadow: [BoxShadow(color: Theme.of(context).colorScheme.onSurface.withOpacity(0.12), blurRadius: 4)],
        ),
        child: Text(
          text,
          style: TextStyle(
            fontSize: 36,
            fontWeight: FontWeight.bold,
            color: isResult ? Colors.green.shade700 : Colors.blue.shade700,
          ),
        ),
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    final List<dynamic> parts = widget.data['parts'] ?? [];
    final String result = widget.data['result'] ?? '';

    List<Widget> wrapChildren = [];
    
    for (int i = 0; i < parts.length; i++) {
      wrapChildren.add(_buildTile(parts[i].toString(), i, false));
      if (i < parts.length - 1) {
        wrapChildren.add(Padding(
          padding: EdgeInsets.symmetric(horizontal: 8.0),
          child: Text(TrilingualService.instance.getUIText('+'), style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Colors.grey)),
        ));
      }
    }

    if (result.isNotEmpty && parts.isNotEmpty) {
      wrapChildren.add(Padding(
        padding: EdgeInsets.symmetric(horizontal: 8.0),
        child: Text(TrilingualService.instance.getUIText('='), style: TextStyle(fontSize: 28, fontWeight: FontWeight.bold, color: Colors.grey)),
      ));
      wrapChildren.add(_buildTile(result, parts.length, true));
    }

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      padding: const EdgeInsets.all(24),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(24),
        border: Border.all(color: Colors.grey.shade300, width: 2),
      ),
      child: Column(
        children: [
          Row(
            mainAxisAlignment: MainAxisAlignment.spaceBetween,
            children: [
              Text(TrilingualService.instance.getUIText('Let\'s Blend!'),
                style: TextStyle(fontSize: 24, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface),
              ),
              IconButton(
                icon: Icon(Icons.play_circle_fill, size: 36, color: Colors.orange),
                onPressed: _playSequence,
              )
            ],
          ),
          const SizedBox(height: 24),
          Wrap(
            alignment: WrapAlignment.center,
            crossAxisAlignment: WrapCrossAlignment.center,
            runSpacing: 16.0,
            children: wrapChildren,
          ),
          const SizedBox(height: 16),
          Text(TrilingualService.instance.getUIText('Tap any box to hear the sound'),
            style: TextStyle(color: Colors.grey, fontSize: 16, fontStyle: FontStyle.italic),
          )
        ],
      ),
    );
  }
}
