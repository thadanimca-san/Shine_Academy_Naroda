import 'package:flutter/material.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';
import '../models/chapter_model.dart';
import '../widgets/formula_section.dart';
import '../widgets/fill_in_blank_quiz.dart';
import '../widgets/numerical_problem_set.dart';
import '../simulations/class11/determiners_advanced_simulation_widget.dart';
import '../simulations/class11/tenses_integrated_simulation_widget.dart';
import '../simulations/class11/modals_advanced_simulation_widget.dart';
import '../simulations/class11/clauses_advanced_simulation_widget.dart';
import '../simulations/class11/sentence_transformation_simulation_widget.dart';
import '../simulations/class11/editing_omission_advanced_simulation_widget.dart';
import '../simulations/class11/notice_writing_simulation_widget.dart';
import '../simulations/class11/notice_writing_models_widget.dart';
import '../simulations/class11/letters_formal_informal_simulation_widget.dart';
import '../simulations/class11/letters_formal_informal_models_widget.dart';
import '../simulations/class11/business_letters_simulation_widget.dart';
import '../simulations/class11/business_letters_models_widget.dart';
import '../simulations/class11/advertisement_writing_simulation_widget.dart';
import '../simulations/class11/advertisement_writing_models_widget.dart';
import '../simulations/class11/email_writing_simulation_widget.dart';
import '../simulations/class11/dialogue_writing_simulation_widget.dart';
import '../simulations/class12/determiners_board_simulation_widget.dart';
import '../simulations/class12/modals_board_simulation_widget.dart';
import '../simulations/class12/clauses_board_simulation_widget.dart';
import '../simulations/class12/reported_speech_board_simulation_widget.dart';
import '../simulations/class12/editing_omission_board_simulation_widget.dart';
import '../simulations/class12/vocabulary_board_simulation_widget.dart';
import '../simulations/class12/article_writing_simulation_widget.dart';
import '../simulations/class12/article_writing_models_widget.dart';
import '../simulations/class12/report_writing_simulation_widget.dart';
import '../simulations/class12/report_writing_models_widget.dart';
import '../simulations/class12/speech_writing_simulation_widget.dart';
import '../simulations/class12/speech_writing_models_widget.dart';
import '../simulations/class12/letter_writing_simulation_widget.dart';
import '../simulations/class12/letter_writing_models_widget.dart';
import '../simulations/class12/essay_writing_simulation_widget.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';

/// Maps each chapter's unique ID to the interactive simulation widgets that
/// teach its key topics.
final Map<String, List<Widget Function()>> _chapterSimulations = {
  'cls11_eng_determinersadvanced': [() => const DeterminersAdvancedSimulationWidget()],
  'cls11_eng_tensesintegrated': [() => const TensesIntegratedSimulationWidget()],
  'cls11_eng_modalsadvanced': [() => const ModalsAdvancedSimulationWidget()],
  'cls11_eng_clausesadvanced': [() => const ClausesAdvancedSimulationWidget()],
  'cls11_eng_sentencetransformation': [() => const SentenceTransformationSimulationWidget()],
  'cls11_eng_editingomissionadvanced': [() => const EditingOmissionAdvancedSimulationWidget()],
  'cls11_eng_noticewriting': [() => const NoticeWritingModelsWidget(), () => const NoticeWritingSimulationWidget()],
  'cls11_eng_lettersformalinformal': [() => const LettersFormalInformalModelsWidget(), () => const LettersFormalInformalSimulationWidget()],
  'cls11_eng_businessletters': [() => const BusinessLettersModelsWidget(), () => const BusinessLettersSimulationWidget()],
  'cls11_eng_advertisementwriting': [() => const AdvertisementWritingModelsWidget(), () => const AdvertisementWritingSimulationWidget()],
  'cls11_eng_emailwriting': [() => const EmailWritingSimulationWidget()],
  'cls11_eng_dialoguewriting': [() => const DialogueWritingSimulationWidget()],
  'cls12_eng_determinersboard': [() => const DeterminersBoardSimulationWidget()],
  'cls12_eng_modalsboard': [() => const ModalsBoardSimulationWidget()],
  'cls12_eng_clausesboard': [() => const ClausesBoardSimulationWidget()],
  'cls12_eng_reportedspeechboard': [() => const ReportedSpeechBoardSimulationWidget()],
  'cls12_eng_editingomissionboard': [() => const EditingOmissionBoardSimulationWidget()],
  'cls12_eng_vocabularyboard': [() => const VocabularyBoardSimulationWidget()],
  'cls12_eng_articlewriting': [() => const ArticleWritingModelsWidget(), () => const ArticleWritingSimulationWidget()],
  'cls12_eng_reportwriting': [() => const ReportWritingModelsWidget(), () => const ReportWritingSimulationWidget()],
  'cls12_eng_speechwriting': [() => const SpeechWritingModelsWidget(), () => const SpeechWritingSimulationWidget()],
  'cls12_eng_letterwriting': [() => const LetterWritingModelsWidget(), () => const LetterWritingSimulationWidget()],
  'cls12_eng_essaywriting': [() => const EssayWritingSimulationWidget()],
};

class ChapterDetailView extends StatelessWidget {
  final ChapterModel chapter;

  const ChapterDetailView({super.key, required this.chapter});

  @override
  Widget build(BuildContext context) {
    final simulations = _chapterSimulations[chapter.chapterId] ?? const [];

    return Scaffold(
      appBar: BrandAppBar(
        title: chapter.chapterName,
      ),
      body: ListView(
        padding: const EdgeInsets.all(16.0),
        children: [
          if (simulations.isNotEmpty) ...[
            Text(TrilingualService.instance.getUIText('Interactive Simulation'),
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            for (final build in simulations) ...[
              build(),
              const SizedBox(height: 16),
            ],
            const SizedBox(height: 8),
          ],
          Text(TrilingualService.instance.getUIText('Core Concepts'),
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          ...chapter.concepts.map((concept) => Padding(
                padding: const EdgeInsets.only(bottom: 6.0),
                child: Row(
                  crossAxisAlignment: CrossAxisAlignment.start,
                  children: [
                    Text(TrilingualService.instance.getUIText('• ')),
                    Expanded(child: Text(concept)),
                  ],
                ),
              )),
          if (chapter.formulas.isNotEmpty) ...[
            const SizedBox(height: 24),
            Text(
              'Formulas & Derivations (${chapter.formulas.length})',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            FormulaSection(formulas: chapter.formulas),
          ],
          const SizedBox(height: 24),
          Text(
            'Practice Questions (${chapter.fillInTheBlanks.length})',
            style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
          ),
          const SizedBox(height: 8),
          FillInBlankQuiz(questions: chapter.fillInTheBlanks),
          if (chapter.numericalProblems.isNotEmpty) ...[
            const SizedBox(height: 24),
            Text(
              'Numerical Problems (${chapter.numericalProblems.length})',
              style: TextStyle(fontSize: 18, fontWeight: FontWeight.bold),
            ),
            const SizedBox(height: 8),
            NumericalProblemSet(problems: chapter.numericalProblems),
          ],
        ],
      ),
    );
  }
}
