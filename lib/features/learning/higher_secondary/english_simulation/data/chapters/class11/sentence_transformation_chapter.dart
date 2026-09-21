import '../../../models/chapter_model.dart';

final class11SentenceTransformationChapter = ChapterModel(
  standard: 11, subject: "English", chapterId: "cls11_eng_sentencetransformation", chapterName: "Transformation of Sentences",
  formulas: [],
  concepts: [
    "Sentence transformation changes the form of a sentence (affirmative, negative, interrogative, exclamatory, simple, complex, compound) while preserving its original meaning.",
    "A simple sentence has one finite verb; a complex sentence has a main clause and at least one subordinate clause; a compound sentence joins two independent clauses with a coordinating conjunction.",
    "Degree transformation converts between positive, comparative, and superlative forms without changing the comparison's meaning.",
    "Transforming between assertive and exclamatory sentences often involves 'What' or 'How' and reordering the sentence.",
    "Transforming voice (active to passive) shifts the object of the active sentence to the subject of the passive sentence.",
  ],
  fillInTheBlanks: [
    QuestionItem(id: 'q1', question: 'He is the tallest boy in the class. → He is taller than [ any other / all other ] boy in the class.', answer: 'any other'),
    QuestionItem(id: 'q2', question: 'As soon as the bell rang, the students left. → [ No sooner had the bell rung / Hardly had the bell rung ] than the students left.', answer: 'No sooner had the bell rung'),
    QuestionItem(id: 'q3', question: 'It is a very sad story. → [ What / How ] a sad story it is!', answer: 'What'),
    QuestionItem(id: 'q4', question: 'He is too weak to walk. → He is [ so weak that he cannot / such weak that he cannot ] walk.', answer: 'so weak that he cannot'),
    QuestionItem(id: 'q5', question: 'She is honest. She is hardworking. (join using a conjunction) → She is [ honest and hardworking / honest but hardworking ].', answer: 'honest and hardworking'),
    QuestionItem(id: 'q6', question: 'Unless you work hard, you will not succeed. → If you [ do not work / work ] hard, you will not succeed.', answer: 'do not work'),
    QuestionItem(id: 'q7', question: 'He is rich enough to buy a car. → He is [ so rich that he can / too rich that he can ] buy a car.', answer: 'so rich that he can'),
    QuestionItem(id: 'q8', question: 'Only Sunil can solve this problem. → No one [ except Sunil / but except Sunil ] can solve this problem.', answer: 'except Sunil'),
    QuestionItem(id: 'q9', question: 'Convert to complex: "Being tired, he went to bed." → [ As he was tired / Because tired ], he went to bed.', answer: 'As he was tired'),
    QuestionItem(id: 'q10', question: 'Convert to negative: "Everyone knows this fact." → [ There is no one who does not know / Someone does not know ] this fact.', answer: 'There is no one who does not know'),
  ],
);
