# Generate JSON (09_GENERATE_JSON)

**Purpose**: This prompt template is used when you need the AI to convert raw textbook text (from PDFs, docs, or web) into the exact structured JSON schema required by the Shine Academy Naroda `ChapterDetailScreen`.

**When to use**: Use this prompt whenever you want to add a new chapter to the complete course curriculum for any subject.

---

## The Prompt Template
*Copy and paste everything below this line to the AI when you want to generate a new chapter.*

---

**Role**: You are an expert instructional designer and data architect for Shine Academy Naroda.

**Task**: I am going to provide you with raw text from a textbook chapter. You must carefully read it, understand the pedagogical flow, and convert the entire chapter into a single, massive JSON file that strictly follows our `ChapterDetailScreen` schema.

**Instructions**:
1. Do not skip any topics. The final output must be comprehensive (The "Mahabharat/Ramayan" of the subject).
2. Extract all definitions into the `definitions` array.
3. Extract all step-by-step examples/illustrations into the `examples` array.
4. Create 3-5 multiple choice questions based on the text and place them in the `exercises` array.
5. If there are previous year board questions, place them in the `previous_year_questions` array.
6. Return the raw JSON wrapped in a code block.

**JSON Schema Template:**
```json
{
  "chapter_id": "gseb_class12_subject_chX",
  "board": "GSEB",
  "class": "Class 12",
  "subject": "Subject Name",
  "title": "Chapter Title",
  "header_image_url": "https://img.freepik.com/free-vector/example.jpg",
  "theory_sections": [
    {
      "section_title": "1. Main Topic",
      "content": "Full markdown-supported content explaining the topic in detail."
    }
  ],
  "definitions": [
    {
      "term": "Term Name",
      "meaning": "Clear definition of the term."
    }
  ],
  "examples": [
    {
      "title": "Example 1: Concept Application",
      "description": "Step by step breakdown of the illustration."
    }
  ],
  "exercises": [
    {
      "question": "Sample Question?",
      "options": ["A", "B", "C", "D"],
      "correct_answer": "B",
      "explanation": "Why B is correct."
    }
  ],
  "previous_year_questions": [
    {
      "year": "March 2023",
      "question": "Sample previous year question",
      "marks": 3,
      "answer_hint": "Key points to include in the answer."
    }
  ]
}
```

**Raw Textbook Text:**
[PASTE YOUR RAW TEXTBOOK TEXT HERE]
