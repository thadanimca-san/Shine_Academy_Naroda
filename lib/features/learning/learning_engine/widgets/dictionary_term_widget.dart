import 'dart:io';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import '../../school/english/services/speech_service.dart';
import 'package:shine_academy_naroda/core/services/tts_service.dart';
import '../../../common/widgets/tts_interactive_text.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class DictionaryTermWidget extends StatefulWidget {
  final Map<String, dynamic> data;

  const DictionaryTermWidget({super.key, required this.data});

  @override
  State<DictionaryTermWidget> createState() => _DictionaryTermWidgetState();
}

class _DictionaryTermWidgetState extends State<DictionaryTermWidget> with SingleTickerProviderStateMixin {
  late TabController _tabController;
  double _currentSpeechRate = 0.4;
  bool _isSpeaking = false;

  @override
  void initState() {
    super.initState();
    _tabController = TabController(length: 3, vsync: this);
  }

  void _changeSpeechRate(double rate) async {
    setState(() {
      _currentSpeechRate = rate;
    });
  }

  Future<void> _speak(String text) async {
    if (text.trim().isEmpty || text.trim() == ".") return;
    
    setState(() { _isSpeaking = true; });
    try {
      await TTSService.instance.speak(text);
      if (mounted) setState(() { _isSpeaking = false; });
    } catch (e) {
      debugPrint("Failed to run TTS: $e");
      if (mounted) setState(() { _isSpeaking = false; });
    }
  }

  Future<void> _stopSpeaking() async {
    setState(() { _isSpeaking = false; });
    await TTSService.instance.stop();
  }

  @override
  void dispose() {
    _tabController.dispose();
    TTSService.instance.stop();
    super.dispose();
  }
  
  // Helper to safely get definition based on keys, handling String or Map
  String _getDefinitionText(dynamic definitionData, List<String> keys) {
    if (definitionData == null) return '';
    if (definitionData is String) return definitionData; // If it's just a raw string
    
    if (definitionData is Map) {
      for (String key in keys) {
        if (definitionData[key] != null && definitionData[key].toString().isNotEmpty) {
          return definitionData[key].toString();
        }
      }
    }
    return '';
  }

  @override
  Widget build(BuildContext context) {
    final term = widget.data['term']?['english'] ?? 'Concept';
    final hindi = widget.data['term']?['hindi'] ?? '';
    final definition = widget.data['definition'] ?? widget.data['definitions'] ?? {};
    final realLifeExamples = widget.data['real_life_examples'] as List<dynamic>? ?? [];
    final importance = widget.data['importance']?['accounting'] as List<dynamic>? ?? [];
    final teacherNotes = widget.data['teacher_notes'] ?? {};
    final imageUrl = widget.data['media']?['image'];
    
    String simpleDef = _getDefinitionText(definition, ['simple', 'beginner']);
    String standardDef = _getDefinitionText(definition, ['standard', 'academic', 'intermediate']);
    String advancedDef = _getDefinitionText(definition, ['scientific', 'advanced']);

    return Container(
      margin: const EdgeInsets.only(bottom: 24),
      decoration: BoxDecoration(
        color: Colors.white,
        borderRadius: BorderRadius.circular(20),
        boxShadow: [
          BoxShadow(
            color: Colors.blue.withValues(alpha: 0.1),
            blurRadius: 15,
            offset: const Offset(0, 8),
          )
        ],
        border: Border.all(color: Colors.blue[50]!, width: 2),
      ),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.stretch,
        children: [
          // Header
          Container(
            padding: const EdgeInsets.all(20),
            decoration: BoxDecoration(
              gradient: LinearGradient(
                colors: [Colors.blue[700]!, Colors.blue[500]!],
                begin: Alignment.topLeft,
                end: Alignment.bottomRight,
              ),
              borderRadius: const BorderRadius.vertical(top: Radius.circular(18)),
            ),
            child: Row(
              children: [
                Icon(Icons.menu_book, color: Colors.white, size: 28),
                const SizedBox(width: 12),
                Expanded(
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      Text(
                        term,
                        style: GoogleFonts.poppins(
                          fontSize: 24,
                          fontWeight: FontWeight.bold,
                          color: Colors.white,
                        ),
                      ),
                      if (hindi.isNotEmpty)
                        Text(
                          hindi,
                          style: GoogleFonts.inter(fontSize: 14, color: Colors.white70),
                        ),
                    ],
                  ),
                ),
                if (widget.data['voice']?['pronunciation'] == true || widget.data['voice'] == null) ...[
                  PopupMenuButton<double>(
                    icon: Icon(Icons.speed, color: Colors.white70, size: 24),
                    tooltip: 'Change Reading Speed',
                    onSelected: _changeSpeechRate,
                    itemBuilder: (context) => [
                      PopupMenuItem(value: 0.2, child: Text(TrilingualService.instance.getUIText('Slow'))),
                      PopupMenuItem(value: 0.4, child: Text(TrilingualService.instance.getUIText('Normal'))),
                      PopupMenuItem(value: 0.6, child: Text(TrilingualService.instance.getUIText('Fast'))),
                    ],
                  ),
                  IconButton(
                    icon: Icon(_isSpeaking ? Icons.stop_circle : Icons.volume_up, color: _isSpeaking ? Colors.redAccent : Colors.white, size: 32),
                    tooltip: _isSpeaking ? 'Stop reading' : 'Listen to pronunciation',
                    onPressed: () {
                      if (_isSpeaking) {
                        _stopSpeaking();
                      } else {
                        String defToSpeak = '';
                        if (_tabController.index == 0) defToSpeak = simpleDef;
                        else if (_tabController.index == 1) defToSpeak = standardDef;
                        else if (_tabController.index == 2) defToSpeak = advancedDef;
                        
                        // Fallback if the tab is empty but another tab has content
                        if (defToSpeak.isEmpty) {
                            if (simpleDef.isNotEmpty) defToSpeak = simpleDef;
                            else if (standardDef.isNotEmpty) defToSpeak = standardDef;
                            else if (advancedDef.isNotEmpty) defToSpeak = advancedDef;
                        }
                        
                        _speak("$term. $defToSpeak");
                      }
                    },
                  ),
                ],
              ],
            ),
          ),
          
          if (imageUrl != null)
            GestureDetector(
              onTap: () {
                showDialog(
                  context: context,
                  builder: (context) => Dialog(
                    backgroundColor: Colors.transparent,
                    insetPadding: const EdgeInsets.all(16),
                    child: Stack(
                      alignment: Alignment.center,
                      children: [
                        ClipRRect(
                          borderRadius: BorderRadius.circular(16),
                          child: Image.asset(imageUrl, fit: BoxFit.contain),
                        ),
                        Positioned(
                          top: 16,
                          right: 16,
                          child: IconButton(
                            icon: Icon(Icons.close, color: Colors.white, size: 32),
                            onPressed: () => Navigator.pop(context),
                          ),
                        ),
                      ],
                    ),
                  ),
                );
              },
              child: Container(
                width: double.infinity,
                height: 220,
                color: Colors.white,
                padding: const EdgeInsets.all(16),
                child: Hero(
                  tag: 'dictionary_img_$term',
                  child: Image.asset(imageUrl, fit: BoxFit.contain),
                ),
              ),
            ),
          
          // Definitions TabBar
          TabBar(
            controller: _tabController,
            labelColor: Colors.blue[800],
            unselectedLabelColor: Colors.grey,
            indicatorColor: Colors.blue[800],
            tabs: const [
              Tab(text: "Simple"),
              Tab(text: "Standard"),
              Tab(text: "Advanced"),
            ],
          ),
          
          // Definitions Content
          SizedBox(
            height: 140,
            child: TabBarView(
              controller: _tabController,
              children: [
                _buildDefinitionText(simpleDef.isNotEmpty ? simpleDef : 'No simple definition available.'),
                _buildDefinitionText(standardDef.isNotEmpty ? standardDef : 'No standard definition available.'),
                _buildDefinitionText(advancedDef.isNotEmpty ? advancedDef : 'No advanced definition available.'),
              ],
            ),
          ),
          
          const Divider(height: 1),
          
          // Content Sections
          Padding(
            padding: const EdgeInsets.all(20),
            child: Column(
              crossAxisAlignment: CrossAxisAlignment.start,
              children: [
                if (realLifeExamples.isNotEmpty) ...[
                  _buildSectionHeader(Icons.lightbulb, "Real Life Examples", Colors.orange),
                  ...realLifeExamples.map((ex) => _buildBulletPoint(ex.toString())),
                  const SizedBox(height: 16),
                ],
                
                if (importance.isNotEmpty) ...[
                  _buildSectionHeader(Icons.star, "Why It Matters", Colors.purple),
                  ...importance.map((imp) => _buildBulletPoint(imp.toString())),
                  const SizedBox(height: 16),
                ],
                
                if (teacherNotes.containsKey('misconception')) ...[
                  Container(
                    padding: const EdgeInsets.all(16),
                    decoration: BoxDecoration(
                      color: Colors.red[50],
                      borderRadius: BorderRadius.circular(12),
                      border: Border.all(color: Colors.red[200]!),
                    ),
                    child: Row(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: [
                        Icon(Icons.warning_amber_rounded, color: Colors.red),
                        const SizedBox(width: 12),
                        Expanded(
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: [
                              Text(TrilingualService.instance.getUIText("Common Misconception"), style: GoogleFonts.poppins(fontWeight: FontWeight.bold, color: Colors.red[800])),
                              const SizedBox(height: 4),
                              Text(teacherNotes['misconception'], style: GoogleFonts.inter(color: Theme.of(context).colorScheme.onSurface)),
                            ],
                          ),
                        ),
                      ],
                    ),
                  ),
                ],
              ],
            ),
          ),
        ],
      ),
    );
  }

  Widget _buildDefinitionText(String text) {
    return Padding(
      padding: const EdgeInsets.all(20),
      child: Center(
        child: TtsInteractiveText(
          text: text,
          style: GoogleFonts.inter(fontSize: 16, height: 1.5, color: Theme.of(context).colorScheme.onSurface),
          highlightColor: Colors.amber.withValues(alpha: 0.5),
          textAlign: TextAlign.center,
        ),
      ),
    );
  }

  Widget _buildSectionHeader(IconData icon, String title, Color color) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 12),
      child: Row(
        children: [
          Icon(icon, color: color, size: 20),
          const SizedBox(width: 8),
          Text(
            title,
            style: GoogleFonts.poppins(fontSize: 18, fontWeight: FontWeight.bold, color: Theme.of(context).colorScheme.onSurface),
          ),
        ],
      ),
    );
  }

  Widget _buildBulletPoint(String text) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 8, left: 4),
      child: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Text(TrilingualService.instance.getUIText("• "), style: TextStyle(fontSize: 16, fontWeight: FontWeight.bold, color: Colors.blue)),
          Expanded(child: Text(text, style: GoogleFonts.inter(fontSize: 15, height: 1.4, color: Theme.of(context).colorScheme.onSurface))),
        ],
      ),
    );
  }
}
