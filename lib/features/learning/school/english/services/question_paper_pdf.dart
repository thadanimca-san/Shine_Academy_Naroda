import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';
import 'dart:typed_data';
import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';
import '../models/question_paper.dart';

Future<Uint8List> buildQuestionPaperPdf(QuestionPaper paper) async {
  List<Widget> widgets = [];
  widgets.add(_paperHeader(paper));
  widgets.add(const SizedBox(height: 16));
  for (final section in paper.sections) {
    widgets.add(_paperSection(section));
  }

  return await UniversalPdfEngine.generatePdfBytesFromWidgets(
    title: paper.title,
    widgets: widgets,
    isAnswerKey: false,
  );
}

Future<Uint8List> buildAnswerKeyPdf(QuestionPaper paper) async {
  List<Widget> widgets = [];
  widgets.add(
    Center(
      child: TtsInteractiveText(text: '${paper.title} - Answer Key', style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
    ),
  );
  widgets.add(const SizedBox(height: 16));
  for (final section in paper.sections) {
    widgets.add(_answerKeySection(section));
  }

  return await UniversalPdfEngine.generatePdfBytesFromWidgets(
    title: paper.title,
    widgets: widgets,
    isAnswerKey: true,
  );
}

Widget _paperHeader(QuestionPaper paper) {
  return Column(
    crossAxisAlignment: CrossAxisAlignment.center,
    children: [
      TtsInteractiveText(text: paper.title, style: const TextStyle(fontSize: 18, fontWeight: FontWeight.bold)),
      const SizedBox(height: 4),
      TtsInteractiveText(text: 
        '${paper.grade}  -  Total Marks: ${paper.totalMarks}  -  Questions: ${paper.totalQuestions}',
        style: TextStyle(fontSize: 14, color: Colors.grey[700]),
      ),
      const SizedBox(height: 8),
      const Divider(),
    ],
  );
}

Widget _paperSection(PaperSection section) {
  return Padding(
    padding: const EdgeInsets.only(bottom: 16),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        Row(
          mainAxisAlignment: MainAxisAlignment.spaceBetween,
          children: [
            TtsInteractiveText(text: section.heading, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
            TtsInteractiveText(text: '${section.totalMarks} marks', style: TextStyle(fontSize: 12, color: Colors.grey[700])),
          ],
        ),
        const SizedBox(height: 2),
        TtsInteractiveText(text: section.instructions, style: TextStyle(fontSize: 12, fontStyle: FontStyle.italic, color: Colors.grey[700])),
        if (section.passageText != null && section.passageText!.isNotEmpty) ...[
          const SizedBox(height: 8),
          Container(
            padding: const EdgeInsets.all(10),
            decoration: BoxDecoration(
              color: Colors.grey[100],
              border: Border.all(color: Colors.grey[300]!),
            ),
            child: TtsInteractiveText(text: section.passageText!, style: const TextStyle(fontSize: 14, height: 1.5)),
          ),
        ],
        const SizedBox(height: 6),
        for (var i = 0; i < section.questions.length; i++) _paperQuestion(i + 1, section.questions[i]),
      ],
    ),
  );
}

Widget _paperQuestion(int number, dynamic question) {
  return Padding(
    padding: const EdgeInsets.only(bottom: 8),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        TtsInteractiveText(text: '$number. ${question.prompt}', style: const TextStyle(fontSize: 14)),
        const SizedBox(height: 4),
        for (var i = 0; i < (question.options as List).length; i++)
          Padding(
            padding: const EdgeInsets.only(left: 14, bottom: 2),
            child: TtsInteractiveText(text: 
              '(${String.fromCharCode(97 + i)}) ${question.options[i]}',
              style: TextStyle(fontSize: 14, color: Colors.grey[800]),
            ),
          ),
      ],
    ),
  );
}

Widget _answerKeySection(PaperSection section) {
  return Padding(
    padding: const EdgeInsets.only(bottom: 14),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        TtsInteractiveText(text: section.heading, style: const TextStyle(fontSize: 16, fontWeight: FontWeight.bold)),
        const SizedBox(height: 4),
        for (var i = 0; i < section.questions.length; i++) _answerKeyQuestion(i + 1, section.questions[i]),
      ],
    ),
  );
}

Widget _answerKeyQuestion(int number, dynamic question) {
  final letter = String.fromCharCode(97 + (question.correctIndex as int));
  return Padding(
    padding: const EdgeInsets.only(bottom: 6),
    child: Column(
      crossAxisAlignment: CrossAxisAlignment.start,
      children: [
        TtsInteractiveText(text: '$number. ($letter) ${question.correctAnswer}',
            style: TextStyle(fontSize: 14, fontWeight: FontWeight.bold, color: Colors.green[800])),
        TtsInteractiveText(text: question.explanation as String, style: TextStyle(fontSize: 12, color: Colors.grey[800])),
      ],
    ),
  );
}
