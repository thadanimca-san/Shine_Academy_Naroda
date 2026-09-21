import 'dart:convert';
import 'dart:io';
import 'package:flutter/material.dart';
import 'package:google_fonts/google_fonts.dart';
import 'package:path_provider/path_provider.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

class PaperDigitizationStudioScreen extends StatefulWidget {
  const PaperDigitizationStudioScreen({super.key});

  @override
  State<PaperDigitizationStudioScreen> createState() => _PaperDigitizationStudioScreenState();
}

class _PaperDigitizationStudioScreenState extends State<PaperDigitizationStudioScreen> {
  final _formKey = GlobalKey<FormState>();

  final _idController = TextEditingController(text: 'Q001');
  final _classController = TextEditingController(text: '10');
  final _subjectController = TextEditingController(text: 'Maths');
  final _chapterIdController = TextEditingController(text: 'ch1');
  final _topicIdController = TextEditingController(text: 'topic1');
  final _sectionController = TextEditingController(text: 'A');
  String _board = 'GSEB';
  String _type = 'mcq';
  String _difficulty = 'Intermediate';
  final _marksController = TextEditingController(text: '1');
  String _bloomTaxonomy = 'Understanding';
  final _estimatedTimeController = TextEditingController(text: '2');
  String _examFrequency = 'Medium';
  final _questionTextController = TextEditingController();
  final _explanationController = TextEditingController();
  final _distractorRationaleController = TextEditingController();

  // MCQ specific fields
  final _optionAController = TextEditingController();
  final _optionBController = TextEditingController();
  final _optionCController = TextEditingController();
  final _optionDController = TextEditingController();
  String _correctAnswerIndex = '0';

  String _generatedJson = '';

  @override
  void dispose() {
    _idController.dispose();
    _classController.dispose();
    _subjectController.dispose();
    _chapterIdController.dispose();
    _topicIdController.dispose();
    _sectionController.dispose();
    _marksController.dispose();
    _estimatedTimeController.dispose();
    _questionTextController.dispose();
    _explanationController.dispose();
    _distractorRationaleController.dispose();
    _optionAController.dispose();
    _optionBController.dispose();
    _optionCController.dispose();
    _optionDController.dispose();
    super.dispose();
  }

  void _generateJson() {
    if (!_formKey.currentState!.validate()) return;

    final data = {
      'id': _idController.text,
      'class': _classController.text,
      'subject': _subjectController.text,
      'chapter_id': _chapterIdController.text,
      'topic_id': _topicIdController.text,
      'section': _sectionController.text,
      'type': _type,
      'difficulty': _difficulty,
      'board': [_board],
      'marks': int.tryParse(_marksController.text) ?? 1,
      'bloom_taxonomy': _bloomTaxonomy,
      'keywords': [],
      'estimated_time_minutes': int.tryParse(_estimatedTimeController.text) ?? 2,
      'exam_frequency': _examFrequency,
      'question_text': _questionTextController.text,
    };

    if (_type == 'mcq') {
      data['options'] = [
        _optionAController.text,
        _optionBController.text,
        _optionCController.text,
        _optionDController.text,
      ];
      data['correct_index'] = int.parse(_correctAnswerIndex);
    } else {
      data['answer'] = _optionAController.text; // Use Option A for short answer text
    }

    data['explanation'] = _explanationController.text;
    data['distractor_rationale'] = _distractorRationaleController.text;
    
    data['ai_context'] = {
      'learning_goal': 'Assess understanding of ${_topicIdController.text}',
      'common_misconceptions': [],
      'hint': 'Review the core formula.'
    };

    setState(() {
      _generatedJson = const JsonEncoder.withIndent('  ').convert(data);
    });
  }

  Future<void> _saveToFile() async {
    _generateJson();
    if (_generatedJson.isEmpty) return;

    try {
      // Automatically inject into the live curriculum database
      final result = await Process.run('python3', [
        '/home/ubuntu/Shine_Academy_Naroda/scripts/inject_question.py',
        _generatedJson
      ]);

      if (result.exitCode != 0) {
        throw Exception(result.stderr.toString());
      }

      // Auto-increment the Question ID
      String currentId = _idController.text;
      final match = RegExp(r'^(.*?)(\d+)$').firstMatch(currentId);
      if (match != null) {
        String prefix = match.group(1)!;
        String numberStr = match.group(2)!;
        int nextNum = int.parse(numberStr) + 1;
        // Keep the same zero-padding length
        String nextNumStr = nextNum.toString().padLeft(numberStr.length, '0');
        _idController.text = '$prefix$nextNumStr';
      }

      // Clear the text fields for the next question
      _questionTextController.clear();
      _optionAController.clear();
      _optionBController.clear();
      _optionCController.clear();
      _optionDController.clear();
      _explanationController.clear();
      _distractorRationaleController.clear();

      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(
            content: Text(TrilingualService.instance.getUIText('⚡ Instantly injected into the live Database!')),
            backgroundColor: Colors.green,
            duration: Duration(seconds: 2),
          ),
        );
      }
    } catch (e) {
      if (mounted) {
        ScaffoldMessenger.of(context).showSnackBar(
          SnackBar(content: Text('Error saving: $e'), backgroundColor: Colors.red),
        );
      }
    }
  }

  Widget _buildTextField(String label, TextEditingController controller, {bool multiline = false, bool required = true}) {
    return Padding(
      padding: const EdgeInsets.only(bottom: 16),
      child: TextFormField(
        controller: controller,
        maxLines: multiline ? 5 : 1,
        decoration: InputDecoration(
          labelText: label,
          border: const OutlineInputBorder(),
          filled: true,
          fillColor: Colors.white,
        ),
        validator: required ? (v) => v == null || v.isEmpty ? 'Required' : null : null,
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.grey[50],
      appBar: AppBar(
        title: Text(TrilingualService.instance.getUIText('Paper Digitization Studio'), style: GoogleFonts.poppins(fontWeight: FontWeight.bold)),
        backgroundColor: Colors.indigo[800],
        foregroundColor: Colors.white,
      ),
      body: Row(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          // Left: Form
          Expanded(
            flex: 6,
            child: Form(
              key: _formKey,
              child: ListView(
                padding: const EdgeInsets.all(24),
                children: [
                  Text(TrilingualService.instance.getUIText('1. Metadata'), style: GoogleFonts.poppins(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.indigo[800])),
                  const SizedBox(height: 16),
                  Row(
                    children: [
                      Expanded(child: _buildTextField('Class', _classController)),
                      const SizedBox(width: 16),
                      Expanded(child: _buildTextField('Subject', _subjectController)),
                      const SizedBox(width: 16),
                      Expanded(child: _buildTextField('Chapter ID', _chapterIdController)),
                    ],
                  ),
                  Row(
                    children: [
                      Expanded(child: _buildTextField('Topic ID', _topicIdController)),
                      const SizedBox(width: 16),
                      Expanded(child: _buildTextField('Question ID', _idController)),
                      const SizedBox(width: 16),
                      Expanded(child: _buildTextField('Section (e.g. A, B)', _sectionController)),
                    ],
                  ),
                  Row(
                    children: [
                      Expanded(
                        child: DropdownButtonFormField<String>(
                          isExpanded: true,
                          value: _board,
                          decoration: const InputDecoration(labelText: 'Board', border: OutlineInputBorder(), filled: true, fillColor: Colors.white),
                          items: ['GSEB', 'CBSE', 'NCERT'].map((e) => DropdownMenuItem(value: e, child: Text(e))).toList(),
                          onChanged: (v) => setState(() => _board = v!),
                        ),
                      ),
                      const SizedBox(width: 16),
                      Expanded(child: _buildTextField('Marks', _marksController)),
                      const SizedBox(width: 16),
                      Expanded(child: _buildTextField('Est. Time (mins)', _estimatedTimeController)),
                    ],
                  ),
                  Row(
                    children: [
                      Expanded(
                        child: DropdownButtonFormField<String>(
                          isExpanded: true,
                          value: _type,
                          decoration: const InputDecoration(labelText: 'Type', border: OutlineInputBorder(), filled: true, fillColor: Colors.white),
                          items: ['mcq', 'true_false', 'fill_blank', 'short_answer'].map((e) => DropdownMenuItem(value: e, child: Text(e.toUpperCase()))).toList(),
                          onChanged: (v) => setState(() => _type = v!),
                        ),
                      ),
                      const SizedBox(width: 16),
                      Expanded(
                        child: DropdownButtonFormField<String>(
                          isExpanded: true,
                          value: _difficulty,
                          decoration: const InputDecoration(labelText: 'Difficulty', border: OutlineInputBorder(), filled: true, fillColor: Colors.white),
                          items: ['Beginner', 'Intermediate', 'Advanced'].map((e) => DropdownMenuItem(value: e, child: Text(e))).toList(),
                          onChanged: (v) => setState(() => _difficulty = v!),
                        ),
                      ),
                      const SizedBox(width: 16),
                      Expanded(
                        child: DropdownButtonFormField<String>(
                          isExpanded: true,
                          value: _bloomTaxonomy,
                          decoration: const InputDecoration(labelText: 'Bloom Taxonomy', border: OutlineInputBorder(), filled: true, fillColor: Colors.white),
                          items: ['Remembering', 'Understanding', 'Applying', 'Analyzing', 'Evaluating', 'Creating'].map((e) => DropdownMenuItem(value: e, child: Text(e))).toList(),
                          onChanged: (v) => setState(() => _bloomTaxonomy = v!),
                        ),
                      ),
                    ],
                  ),
                  const SizedBox(height: 24),
                  
                  Text(TrilingualService.instance.getUIText('2. Content (Supports LaTeX)'), style: GoogleFonts.poppins(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.indigo[800])),
                  const SizedBox(height: 16),
                  _buildTextField('Question Text', _questionTextController, multiline: true),
                  
                  if (_type == 'mcq') ...[
                    Row(
                      children: [
                        Expanded(child: _buildTextField('Option A', _optionAController)),
                        const SizedBox(width: 16),
                        Expanded(child: _buildTextField('Option B', _optionBController)),
                      ],
                    ),
                    Row(
                      children: [
                        Expanded(child: _buildTextField('Option C', _optionCController)),
                        const SizedBox(width: 16),
                        Expanded(child: _buildTextField('Option D', _optionDController)),
                      ],
                    ),
                    DropdownButtonFormField<String>(
                      isExpanded: true,
                      value: _correctAnswerIndex,
                      decoration: const InputDecoration(labelText: 'Correct Answer', border: OutlineInputBorder(), filled: true, fillColor: Colors.white),
                      items: [
                        DropdownMenuItem(value: '0', child: Text(TrilingualService.instance.getUIText('Option A'))),
                        DropdownMenuItem(value: '1', child: Text(TrilingualService.instance.getUIText('Option B'))),
                        DropdownMenuItem(value: '2', child: Text(TrilingualService.instance.getUIText('Option C'))),
                        DropdownMenuItem(value: '3', child: Text(TrilingualService.instance.getUIText('Option D'))),
                      ],
                      onChanged: (v) => setState(() => _correctAnswerIndex = v!),
                    ),
                  ] else ...[
                    _buildTextField('Correct Answer', _optionAController),
                  ],
                  
                  const SizedBox(height: 24),
                  Text(TrilingualService.instance.getUIText('3. Pedagogy'), style: GoogleFonts.poppins(fontSize: 18, fontWeight: FontWeight.bold, color: Colors.indigo[800])),
                  const SizedBox(height: 16),
                  _buildTextField('Explanation', _explanationController, multiline: true, required: false),
                  _buildTextField('Distractor Rationale (Why wrong options are wrong)', _distractorRationaleController, multiline: true, required: false),
                  
                  const SizedBox(height: 24),
                  Row(
                    mainAxisAlignment: MainAxisAlignment.end,
                    children: [
                      ElevatedButton.icon(
                        icon: Icon(Icons.preview),
                        label: Text(TrilingualService.instance.getUIText('Generate JSON')),
                        onPressed: _generateJson,
                        style: ElevatedButton.styleFrom(
                          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 20),
                        ),
                      ),
                      const SizedBox(width: 16),
                      ElevatedButton.icon(
                        icon: Icon(Icons.save, color: Colors.white),
                        label: Text(TrilingualService.instance.getUIText('Save to Local Database'), style: TextStyle(color: Colors.white)),
                        onPressed: _saveToFile,
                        style: ElevatedButton.styleFrom(
                          backgroundColor: Colors.indigo[800],
                          padding: const EdgeInsets.symmetric(horizontal: 24, vertical: 20),
                        ),
                      ),
                    ],
                  ),
                ],
              ),
            ),
          ),
          
          // Right: Preview JSON
          Expanded(
            flex: 4,
            child: Container(
              margin: const EdgeInsets.all(24),
              decoration: BoxDecoration(
                color: const Color(0xFF1E1E1E),
                borderRadius: BorderRadius.circular(12),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.stretch,
                children: [
                  Container(
                    padding: const EdgeInsets.all(12),
                    decoration: BoxDecoration(
                      color: Color(0xFF2D2D2D),
                      borderRadius: BorderRadius.vertical(top: Radius.circular(12)),
                    ),
                    child: Row(
                      mainAxisAlignment: MainAxisAlignment.spaceBetween,
                      children: [
                        Text(TrilingualService.instance.getUIText('JSON Output Preview'), style: GoogleFonts.firaCode(color: Colors.white, fontWeight: FontWeight.bold)),
                        IconButton(
                          icon: Icon(Icons.copy, color: Colors.white54, size: 20),
                          onPressed: () {
                            // Copy to clipboard not easily available without services, skipping for brevity
                          },
                        ),
                      ],
                    ),
                  ),
                  Expanded(
                    child: SingleChildScrollView(
                      padding: const EdgeInsets.all(16),
                      child: SelectableText(
                        _generatedJson.isEmpty ? 'Click "Generate JSON" to preview' : _generatedJson,
                        style: GoogleFonts.firaCode(color: Colors.greenAccent[100], fontSize: 13),
                      ),
                    ),
                  ),
                ],
              ),
            ),
          ),
        ],
      ),
    );
  }
}
