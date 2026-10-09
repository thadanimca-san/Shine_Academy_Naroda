import 'package:flutter/material.dart';

import '../../../core/engine/assessment_engine.dart';
import '../../../core/services/trilingual_service.dart';
import '../../../foundation/theme/app_typography.dart';
import '../../common/widgets/tts_interactive_text.dart';

/// Text of a question in the language the student or teacher has chosen.
extension LocalizedAssessmentQuestion on AssessmentQuestion {
  String get localizedQuestion {
    final lang = TrilingualService.instance.activeViewLanguage;
    if (lang == 'hi' && (questionHi?.isNotEmpty ?? false)) return questionHi!;
    if (lang == 'gu' && (questionGu?.isNotEmpty ?? false)) return questionGu!;
    return question;
  }

  String? get localizedExplanation {
    final lang = TrilingualService.instance.activeViewLanguage;
    if (lang == 'hi' && (explanationHi?.isNotEmpty ?? false)) return explanationHi!;
    if (lang == 'gu' && (explanationGu?.isNotEmpty ?? false)) return explanationGu!;
    return explanationEn;
  }

  List<String> get localizedOptions {
    final lang = TrilingualService.instance.activeViewLanguage;
    if (lang == 'hi' && (optionsHi?.isNotEmpty ?? false)) return optionsHi!;
    if (lang == 'gu' && (optionsGu?.isNotEmpty ?? false)) return optionsGu!;
    return options;
  }
}

String _optionLabel(int index) => '(${String.fromCharCode(97 + index)})';

/// One line of a question paper: a section header or a numbered question.
/// The same widget draws the on-screen paper and the PDF, so formulas and
/// Indian scripts print exactly as they appear on screen.
class PaperQuestionTile extends StatelessWidget {
  final AssessmentQuestion question;

  /// The question number, or null for a section header.
  final int? number;
  final bool showAnswer;

  /// True when drawn off-screen for a PDF (no read-aloud highlighting).
  final bool isPdfMode;

  const PaperQuestionTile({
    super.key,
    required this.question,
    required this.number,
    this.showAnswer = false,
    this.isPdfMode = false,
  });

  @override
  Widget build(BuildContext context) {
    final onSurface = Theme.of(context).colorScheme.onSurface;
    final body = AppTypography.body(context, color: onSurface);
    final bold = AppTypography.body(context, color: onSurface, fontWeight: FontWeight.w600);
    final small = AppTypography.bodySmall(context, color: onSurface);

    if (question.type == 'section_header') {
      return Padding(
        padding: const EdgeInsets.only(top: 20, bottom: 12),
        child: Center(
          child: Text(question.localizedQuestion, textAlign: TextAlign.center,
              style: AppTypography.body(context, color: Colors.blue.shade900, fontWeight: FontWeight.bold)),
        ),
      );
    }

    Widget text(String value, TextStyle style) =>
        TtsInteractiveText(text: value, style: style, isPdfMode: isPdfMode, enableWordTap: !isPdfMode);

    final options = question.localizedOptions;
    final isObjective = question.type == 'quiz' && options.isNotEmpty;

    return Padding(
      padding: const EdgeInsets.only(bottom: 18),
      child: Column(
        crossAxisAlignment: CrossAxisAlignment.start,
        children: [
          Row(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              Text('Q$number. ', style: bold.copyWith(color: Colors.blue.shade900)),
              Expanded(child: text(question.localizedQuestion, bold)),
              const SizedBox(width: 8),
              Text('[${question.marks}]', style: small.copyWith(color: Colors.grey.shade700)),
            ],
          ),
          if (isObjective)
            Padding(
              padding: const EdgeInsets.only(top: 6, left: 32),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: [
                  for (var i = 0; i < options.length; i++)
                    Padding(
                      padding: const EdgeInsets.only(bottom: 4),
                      child: Row(
                        crossAxisAlignment: CrossAxisAlignment.start,
                        children: [
                          Text('${_optionLabel(i)} ', style: body),
                          Expanded(child: text(options[i], body)),
                        ],
                      ),
                    ),
                ],
              ),
            ),
          if (showAnswer) _buildAnswer(context, text, options, isObjective, body, small),
        ],
      ),
    );
  }

  Widget _buildAnswer(BuildContext context, Widget Function(String, TextStyle) text, List<String> options,
      bool isObjective, TextStyle body, TextStyle small) {
    final answerStyle = body.copyWith(color: Colors.green.shade800, fontWeight: FontWeight.w600);
    final explanation = question.localizedExplanation;
    final answer = question.correctIndexOrAnswer;

    final lines = <Widget>[];
    if (isObjective && answer is int && answer >= 0 && answer < options.length) {
      lines.add(text('Answer: ${_optionLabel(answer)} ${options[answer]}', answerStyle));
    } else if (answer.toString().isNotEmpty) {
      lines.add(Text(TrilingualService.instance.getUIText('Model answer:'), style: answerStyle));
      lines.addAll(answer.toString().split('\n').map((step) => text(step, body)));
    }
    if (explanation != null && explanation.isNotEmpty) {
      final label = isObjective ? 'Explanation:' : 'Marking scheme:';
      lines.add(const SizedBox(height: 4));
      lines.add(Text(TrilingualService.instance.getUIText(label), style: small.copyWith(fontWeight: FontWeight.bold)));
      lines.addAll(explanation.split('\n').map((line) => text(line, small)));
    }

    return Container(
      width: double.infinity,
      margin: const EdgeInsets.only(top: 8, left: 32),
      padding: const EdgeInsets.all(10),
      decoration: BoxDecoration(
        color: Colors.green.shade50,
        borderRadius: BorderRadius.circular(8),
        border: Border.all(color: Colors.green.shade100),
      ),
      child: Column(crossAxisAlignment: CrossAxisAlignment.start, children: lines),
    );
  }
}

/// Numbers the questions of a paper (headers are not numbered) and builds one
/// tile per item.
List<Widget> buildPaperTiles(List<AssessmentQuestion> items, {bool showAnswers = false, bool isPdfMode = false}) {
  var nextNumber = 1;
  return [
    for (final item in items)
      PaperQuestionTile(
        question: item,
        number: item.type == 'section_header' ? null : nextNumber++,
        showAnswer: showAnswers,
        isPdfMode: isPdfMode,
      ),
  ];
}
