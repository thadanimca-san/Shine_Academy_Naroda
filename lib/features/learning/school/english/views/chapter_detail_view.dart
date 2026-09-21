import 'package:flutter/material.dart';
import '../models/chapter_model.dart';
import '../simulations/class7/nouns_simulation_widget.dart';
import '../simulations/class7/pronouns_simulation_widget.dart';
import '../simulations/class7/verbs_simulation_widget.dart';
import '../simulations/class7/adjectives_simulation_widget.dart';
import '../simulations/class7/adverbs_simulation_widget.dart';
import '../simulations/class7/present_tense_simulation_widget.dart';
import '../simulations/class7/past_tense_simulation_widget.dart';
import '../simulations/class7/future_tense_simulation_widget.dart';
import '../simulations/class7/articles_simulation_widget.dart';
import '../simulations/class7/prepositions_simulation_widget.dart';
import '../simulations/class7/conjunctions_simulation_widget.dart';
import '../simulations/class7/punctuation_simulation_widget.dart';
import '../simulations/class7/subject_verb_agreement_simulation_widget.dart';
import '../simulations/class7/synonyms_antonyms_simulation_widget.dart';
import '../simulations/class7/kinds_of_sentences_simulation_widget.dart';
import '../simulations/class8/nouns_number_gender_simulation_widget.dart';
import '../simulations/class8/kinds_of_pronouns_simulation_widget.dart';
import '../simulations/class8/auxiliary_modal_verbs_simulation_widget.dart';
import '../simulations/class8/degrees_comparison_simulation_widget.dart';
import '../simulations/class8/perfect_tenses_simulation_widget.dart';
import '../simulations/class8/active_passive_voice_simulation_widget.dart';
import '../simulations/class8/direct_indirect_speech_simulation_widget.dart';
import '../simulations/class8/determiners_simulation_widget.dart';
import '../simulations/class8/clauses_simulation_widget.dart';
import '../simulations/class8/prepositions_simulation_widget.dart';
import '../simulations/class8/conjunctions_simulation_widget.dart';
import '../simulations/class8/homophones_homonyms_simulation_widget.dart';
import '../simulations/class8/idioms_phrases_simulation_widget.dart';
import '../simulations/class8/prefixes_suffixes_simulation_widget.dart';
import '../simulations/class8/question_tags_simulation_widget.dart';
import '../simulations/class8/punctuation_capitalisation_simulation_widget.dart';
import '../simulations/class9/modals_simulation_widget.dart';
import '../simulations/class9/subject_verb_concord_simulation_widget.dart';
import '../simulations/class9/reported_speech_statements_simulation_widget.dart';
import '../simulations/class9/reported_speech_questions_simulation_widget.dart';
import '../simulations/class9/reported_speech_commands_simulation_widget.dart';
import '../simulations/class9/active_passive_all_tenses_simulation_widget.dart';
import '../simulations/class9/noun_clauses_simulation_widget.dart';
import '../simulations/class9/adjective_clauses_simulation_widget.dart';
import '../simulations/class9/adverb_clauses_simulation_widget.dart';
import '../simulations/class9/determiners_advanced_simulation_widget.dart';
import '../simulations/class9/phrasal_verbs_simulation_widget.dart';
import '../simulations/class9/one_word_substitution_simulation_widget.dart';
import '../simulations/class9/editing_omission_simulation_widget.dart';
import '../simulations/class9/sentence_transformation_simulation_widget.dart';
import '../simulations/class9/advanced_punctuation_simulation_widget.dart';
import '../simulations/class10/integrated_grammar_simulation_widget.dart';
import '../simulations/class10/board_editing_omission_simulation_widget.dart';
import '../simulations/class10/sentence_reordering_simulation_widget.dart';
import '../simulations/class10/dialogue_completion_simulation_widget.dart';
import '../simulations/class10/reported_speech_mixed_simulation_widget.dart';
import '../simulations/class10/clauses_mixed_simulation_widget.dart';
import '../simulations/class10/determiners_prepositions_simulation_widget.dart';
import '../simulations/class10/modals_voice_simulation_widget.dart';
import '../simulations/class10/vocabulary_building_simulation_widget.dart';
import '../simulations/class10/idioms_phrasal_verbs_board_simulation_widget.dart';
import '../widgets/fill_in_blank_quiz.dart';
import '../widgets/numerical_problem_set.dart';
import '../widgets/formula_section.dart';
import 'package:shine_academy_naroda/core/services/trilingual_service.dart';
import '../../../../../foundation/theme/brand_app_bar.dart';

/// Maps each chapter to the interactive simulation widget(s) that best
/// teach its key topics.
final Map<String, List<Widget Function()>> _chapterSimulations = {
  'cls7_eng_nouns': [() => const NounsSimulationWidget()],
  'cls7_eng_pronouns': [() => const PronounsSimulationWidget()],
  'cls7_eng_verbs': [() => const VerbsSimulationWidget()],
  'cls7_eng_adjectives': [() => const AdjectivesSimulationWidget()],
  'cls7_eng_adverbs': [() => const AdverbsSimulationWidget()],
  'cls7_eng_presenttense': [() => const PresentTenseSimulationWidget()],
  'cls7_eng_pasttense': [() => const PastTenseSimulationWidget()],
  'cls7_eng_futuretense': [() => const FutureTenseSimulationWidget()],
  'cls7_eng_articles': [() => const ArticlesSimulationWidget()],
  'cls7_eng_prepositions': [() => const PrepositionsSimulationWidget()],
  'cls7_eng_conjunctions': [() => const ConjunctionsSimulationWidget()],
  'cls7_eng_punctuation': [() => const PunctuationSimulationWidget()],
  'cls7_eng_subjectverbagreement': [() => const SubjectVerbAgreementSimulationWidget()],
  'cls7_eng_synonymsantonyms': [() => const SynonymsAntonymsSimulationWidget()],
  'cls7_eng_kindsofsentences': [() => const KindsOfSentencesSimulationWidget()],
  'cls8_eng_nounsnumbergender': [() => const NounsNumberGenderSimulationWidget()],
  'cls8_eng_kindsofpronouns': [() => const KindsOfPronounsSimulationWidget()],
  'cls8_eng_auxiliarymodalverbs': [() => const AuxiliaryModalVerbsSimulationWidget()],
  'cls8_eng_degreescomparison': [() => const DegreesComparisonSimulationWidget()],
  'cls8_eng_perfecttenses': [() => const PerfectTensesSimulationWidget()],
  'cls8_eng_activepassivevoice': [() => const ActivePassiveVoiceSimulationWidget()],
  'cls8_eng_directindirectspeech': [() => const DirectIndirectSpeechSimulationWidget()],
  'cls8_eng_determiners': [() => const DeterminersSimulationWidget()],
  'cls8_eng_clauses': [() => const ClausesSimulationWidget()],
  'cls8_eng_prepositions': [() => const Class8PrepositionsSimulationWidget()],
  'cls8_eng_conjunctions': [() => const Class8ConjunctionsSimulationWidget()],
  'cls8_eng_homophoneshomonyms': [() => const HomophonesHomonymsSimulationWidget()],
  'cls8_eng_idiomsphrases': [() => const IdiomsPhrasesSimulationWidget()],
  'cls8_eng_prefixessuffixes': [() => const PrefixesSuffixesSimulationWidget()],
  'cls8_eng_questiontags': [() => const QuestionTagsSimulationWidget()],
  'cls8_eng_punctuationcapitalisation': [() => const PunctuationCapitalisationSimulationWidget()],
  'cls9_eng_modals': [() => const ModalsSimulationWidget()],
  'cls9_eng_subjectverbconcord': [() => const SubjectVerbConcordSimulationWidget()],
  'cls9_eng_reportedspeechstatements': [() => const ReportedSpeechStatementsSimulationWidget()],
  'cls9_eng_reportedspeechquestions': [() => const ReportedSpeechQuestionsSimulationWidget()],
  'cls9_eng_reportedspeechcommands': [() => const ReportedSpeechCommandsSimulationWidget()],
  'cls9_eng_activepassivealltenses': [() => const ActivePassiveAllTensesSimulationWidget()],
  'cls9_eng_nounclauses': [() => const NounClausesSimulationWidget()],
  'cls9_eng_adjectiveclauses': [() => const AdjectiveClausesSimulationWidget()],
  'cls9_eng_adverbclauses': [() => const AdverbClausesSimulationWidget()],
  'cls9_eng_determinersadvanced': [() => const DeterminersAdvancedSimulationWidget()],
  'cls9_eng_phrasalverbs': [() => const PhrasalVerbsSimulationWidget()],
  'cls9_eng_onewordsubstitution': [() => const OneWordSubstitutionSimulationWidget()],
  'cls9_eng_editingomission': [() => const EditingOmissionSimulationWidget()],
  'cls9_eng_sentencetransformation': [() => const SentenceTransformationSimulationWidget()],
  'cls9_eng_advancedpunctuation': [() => const AdvancedPunctuationSimulationWidget()],
  'cls10_eng_integratedgrammar': [() => const IntegratedGrammarSimulationWidget()],
  'cls10_eng_boardeditingomission': [() => const BoardEditingOmissionSimulationWidget()],
  'cls10_eng_sentencereordering': [() => const SentenceReorderingSimulationWidget()],
  'cls10_eng_dialoguecompletion': [() => const DialogueCompletionSimulationWidget()],
  'cls10_eng_reportedspeechmixed': [() => const ReportedSpeechMixedSimulationWidget()],
  'cls10_eng_clausesmixed': [() => const ClausesMixedSimulationWidget()],
  'cls10_eng_determinersprepositions': [() => const DeterminersPrepositionsSimulationWidget()],
  'cls10_eng_modalsvoice': [() => const ModalsVoiceSimulationWidget()],
  'cls10_eng_vocabularybuilding': [() => const VocabularyBuildingSimulationWidget()],
  'cls10_eng_idiomsphrasalverbsboard': [() => const IdiomsPhrasalVerbsBoardSimulationWidget()],
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
