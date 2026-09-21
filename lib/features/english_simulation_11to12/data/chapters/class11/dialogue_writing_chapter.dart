import '../../../models/chapter_model.dart';

final class11DialogueWritingChapter = ChapterModel(
  standard: 11, subject: "English", chapterId: "cls11_eng_dialoguewriting", chapterName: "Dialogue Writing",
  formulas: [],
  concepts: [
    "A dialogue is a natural, realistic conversation between two (or more) speakers on a given situation, written the way people actually speak.",
    "Each speaker's name is written once per turn, followed by a colon, with their line immediately after (e.g. 'Aryan: Have you finished the assignment?').",
    "A good dialogue stays focused on the given situation and moves the conversation forward logically — each reply should genuinely respond to the previous line.",
    "Dialogues use natural conversational features: contractions ('I'm', 'don't'), short sentences, questions, and interruptions, rather than formal written English.",
    "A dialogue should have a clear beginning (context/greeting), middle (the actual exchange/discussion), and end (a resolution, decision, or natural close).",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'In a dialogue, each speaker\'s line is introduced by their [ name followed by a colon / full formal title ].', answer: 'name followed by a colon'),
    QuestionItem(id: 'q2', question: 'A dialogue should be written the way people [ actually speak / write formal essays ].', answer: 'actually speak'),
    QuestionItem(id: 'q3', question: 'Dialogues commonly use [ contractions like "I\'m" and "don\'t" / only full formal expressions ].', answer: 'contractions like "I\'m" and "don\'t"'),
    QuestionItem(id: 'q4', question: 'Each reply in a good dialogue should [ genuinely respond to the previous line / ignore what was just said ].', answer: 'genuinely respond to the previous line'),
    QuestionItem(id: 'q5', question: 'A dialogue should stay [ focused on the given situation / free to wander to unrelated topics ].', answer: 'focused on the given situation'),
    QuestionItem(id: 'q6', question: 'A well-written dialogue has a clear [ beginning, middle, and end / random, unstructured flow ].', answer: 'beginning, middle, and end'),
    QuestionItem(id: 'q7', question: 'Dialogues typically use [ short, natural sentences and questions / long, complex formal sentences ].', answer: 'short, natural sentences and questions'),
    QuestionItem(id: 'q8', question: 'A dialogue between a doctor and patient should end with a [ natural resolution, like advice given / abrupt, unrelated statement ].', answer: 'natural resolution, like advice given'),
    QuestionItem(id: 'q9', question: 'Unlike a report, a dialogue is written [ entirely in direct speech, turn by turn / entirely in reported speech ].', answer: 'entirely in direct speech, turn by turn'),
    QuestionItem(id: 'q10', question: 'A dialogue on a given situation (e.g. "booking an appointment") must include details [ relevant to that situation, like date and time / entirely unrelated to it ].', answer: 'relevant to that situation, like date and time'),
  ],
);
