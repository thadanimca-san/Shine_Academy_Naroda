import '../../../models/chapter_model.dart';

final class9SentenceTransformationChapter = ChapterModel(
  standard: 9, subject: "English", chapterId: "cls9_eng_sentencetransformation", chapterName: "Sentence Transformation",
  formulas: [],
  concepts: [
    "Sentence transformation changes a sentence's form (affirmative, negative, interrogative, exclamatory) while keeping its meaning.",
    "Simple sentences can be transformed into compound sentences by joining with coordinating conjunctions.",
    "Simple sentences can be transformed into complex sentences by adding a subordinate clause.",
    "Degrees of comparison can be transformed between positive, comparative and superlative while keeping the meaning.",
    "Affirmative and negative sentences can express the same meaning using structures like 'no one but'/'only'.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'Positive: "He is the tallest boy in class." Comparative: "He is taller than [ any other / all other ] boy in class."', answer: 'any other'),
    QuestionItem(id: 'q2', question: 'Simple: "Despite his illness, he came to work." Complex: "[ Though / Because ] he was ill, he came to work."', answer: 'Though'),
    QuestionItem(id: 'q3', question: 'Simple: "He is too weak to walk." Complex: "He is so weak [ that / because ] he cannot walk."', answer: 'that'),
    QuestionItem(id: 'q4', question: 'Affirmative: "Only he can solve this." Negative: "No one [ but / except of ] he can solve this."', answer: 'but'),
    QuestionItem(id: 'q5', question: 'Simple: "On hearing the news, she wept." Complex: "[ When / Because ] she heard the news, she wept."', answer: 'When'),
    QuestionItem(id: 'q6', question: 'Compound: "He was tired, but he kept working." Simple: "[ In spite of / Because of ] being tired, he kept working."', answer: 'In spite of'),
    QuestionItem(id: 'q7', question: 'Assertive: "It is a difficult task." Exclamatory: "[ What / How ] a difficult task it is!"', answer: 'What'),
    QuestionItem(id: 'q8', question: 'Assertive: "She sings very sweetly." Exclamatory: "[ How / What ] sweetly she sings!"', answer: 'How'),
    QuestionItem(id: 'q9', question: 'Simple: "I know the reason for his absence." Complex: "I know [ why / what ] he was absent."', answer: 'why'),
    QuestionItem(id: 'q10', question: 'Positive: "Gold is a precious metal." Comparative: "Gold is [ more precious / precious ] than most other metals."', answer: 'more precious'),
    QuestionItem(id: 'q11', question: 'Simple: "He worked hard to succeed." Complex: "He worked hard [ so that / because ] he might succeed."', answer: 'so that'),
    QuestionItem(id: 'q12', question: 'Interrogative: "Isn\'t it a beautiful morning?" Assertive: "It [ is / isn\'t ] a beautiful morning."', answer: 'is'),
    QuestionItem(id: 'q13', question: 'Complex: "As soon as he arrived, we left." Simple: "[ On his arrival / During his arrival ], we left."', answer: 'On his arrival'),
    QuestionItem(id: 'q14', question: 'Compound: "He is poor but honest." Simple: "[ In spite of / Because of ] being poor, he is honest."', answer: 'In spite of'),
    QuestionItem(id: 'q15', question: 'Superlative: "He is the wisest man in the village." Positive: "[ No other / Every other ] man in the village is as wise as him."', answer: 'No other'),
  ],
);
