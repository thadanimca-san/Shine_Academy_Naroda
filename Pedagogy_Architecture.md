# Pedagogy Architecture

The Pedagogy Engine dictates *how* students learn, not just *what* they learn.

## The Standard Educational Sequence
Every chapter MUST follow this verified pedagogical flow to be accepted by the validation engine:

1. **Learning Objectives:** What will the student achieve?
2. **Theory:** The core concept (culturally integrated, using The Shine Academy Method).
3. **Example:** A worked out or real-world example.
4. **Interactive Activity:** A diagram, slider, or presentation.
5. **Teacher Tip / Common Mistake:** Pre-emptive error correction.
6. **Dictionary Link:** Tying the concept into the Knowledge Graph.
7. **Quiz:** Immediate micro-assessment.
8. **Flashcard:** Rote memorization anchor.
9. **Summary / Revision:** Final wrap-up.
10. **Final Assessment:** Bloom's Taxonomy driven testing.

## Validation Rule
If a generated JSON chapter lacks an Assessment or a Summary, the Pedagogy Engine will **REJECT** the build. Quality over quantity.
