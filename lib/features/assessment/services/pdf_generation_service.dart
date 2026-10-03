import 'package:flutter/material.dart';
import 'package:shine_academy_naroda/core/engine/universal_pdf_engine.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import 'package:shine_academy_naroda/features/common/widgets/tts_interactive_text.dart';

class PdfGenerationService {
  Future<void> generateQuestionPaperPDF(String title, List<dynamic> questions) async {
    List<Widget> widgets = [];
    
    // Add title header manually since we're using widgets
    widgets.add(
      Center(
        child: TtsInteractiveText(
          text: title,
          style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
        ),
      ),
    );
    widgets.add(const SizedBox(height: 20));

    for (final q in questions) {
      widgets.add(
        Padding(
          padding: const EdgeInsets.only(bottom: 20),
          child: Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              TtsInteractiveText(text: 'Q${q['q_no']}. ', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
              Expanded(
                child: TtsInteractiveText(text: q['question'], style: const TextStyle(fontSize: 14)),
              ),
              const SizedBox(width: 10),
              TtsInteractiveText(text: '[${q['marks']}]', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
            ],
          ),
        ),
      );
    }

    await UniversalPdfEngine.generatePdfFromWidgets(
      title: title,
      widgets: widgets,
      isAnswerKey: false,
    );
  }

  Future<void> generateSolutionsPDF(String title, List<dynamic> questions) async {
    List<Widget> widgets = [];

    widgets.add(
      Center(
        child: TtsInteractiveText(
          text: '$title (Solutions)',
          style: const TextStyle(fontSize: 20, fontWeight: FontWeight.bold),
        ),
      ),
    );
    widgets.add(const SizedBox(height: 20));

    for (final q in questions) {
      widgets.add(
        Padding(
          padding: const EdgeInsets.only(bottom: 20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Row(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  TtsInteractiveText(text: 'Q${q['q_no']}. ', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
                  Expanded(
                    child: TtsInteractiveText(text: q['question'], style: const TextStyle(fontSize: 14)),
                  ),
                  const SizedBox(width: 10),
                  TtsInteractiveText(text: '[${q['marks']}]', style: const TextStyle(fontWeight: FontWeight.bold, fontSize: 14)),
                ],
              ),
              const SizedBox(height: 10),
              Container(
                padding: const EdgeInsets.all(10),
                decoration: BoxDecoration(
                  color: Colors.grey[100],
                  border: Border.all(color: Colors.grey[300]!),
                  borderRadius: const BorderRadius.all(Radius.circular(5)),
                ),
                child: TtsInteractiveText(text: 'Answer: \n${q['solution']}', style: const TextStyle(fontSize: 12)),
              ),
            ],
          ),
        ),
      );
    }

    await UniversalPdfEngine.generatePdfFromWidgets(
      title: title,
      widgets: widgets,
      isAnswerKey: true,
    );
  }
}

