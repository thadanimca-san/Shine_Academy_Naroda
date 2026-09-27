# Shine Academy Naroda - Universal Content Standards

=========================================================
PERMANENT DIRECTIVE — NOTED BY USER ON 2026-09-05
=========================================================
**THIS IS NOT A SMALL PROJECT. EVERY EXERCISE QUESTION FROM EVERY TEXTBOOK CHAPTER
MUST BE INCLUDED. NO SHORTCUTS. NO LAZY SUMMARIES. NO "DONE" WITHOUT PROOF.**

- If a chapter has 4 exercise sections with 65 questions → all 65 must be in the JSON.
- If a chapter has 3 sections with 47 questions → all 47 must be there.
- Every question must appear in English, Hindi, AND Gujarati.
- Every option must appear in English, Hindi, AND Gujarati.
- Every explanation must appear in English, Hindi, AND Gujarati.
- Never claim a chapter is "complete" unless EVERY exercise question from the textbook is present.
- Never generate a token chapter with 8-10 blocks and call it done. That is cheating.
- The student's time and the user's money are both valuable. Do not waste either.

=========================================================

=========================================================
TOP PRIORITY: HINDI TRANSLATION IS MANDATORY EVERYWHERE
=========================================================
**CRITICAL DIRECTIVE FOR ALL AGENTS:**
This application is mainly for Indian students. The average student does not know English well, as it is a foreign language to them. Therefore, giving the world's best knowledge ONLY in English will fail them. 
*   **HINDI TRANSLATION IS A MUST EVERYWHERE.**
*   Every single block of content (titles, bodies, questions, options, explanations, teacher tips) MUST include its Hindi equivalent (e.g., `body_hi`, `title_hi`, `question_hi`, `options_hi`, `explanation_hi`).
*   Never generate a JSON payload that contains only English text.
*   This rule supersedes all other content generation rules. Do not forget it ever.

**CRITICAL DIRECTIVE FOR ALL AGENTS:**

Before you generate **ANY** educational content for this platform (including JSON definitions, curriculum files, modules, chapters, quiz questions, or dictionary entries), you MUST parse and strictly adhere to the 5 Master Standards located in the `standards/` directory.

### The 5 Master Standards:
1. `standards/MASTER_CONTENT_STANDARD.yaml` - Governs the overarching educational philosophy.
2. `standards/DICTIONARY_STANDARD.yaml` - Governs the structure of every single definition/concept.
3. `standards/CHAPTER_STANDARD.yaml` - Governs the sequential flow of a learning module.
4. `standards/QUESTION_STANDARD.yaml` - Governs the structure of all assessments.
5. `standards/MEDIA_STANDARD.yaml` - Governs the asset requirements (visuals, voice, animations).

### Execution Rule:
If a user requests the generation of a new subject, chapter, or dictionary entry, you must construct the JSON payload such that it perfectly maps to the keys and data types specified in these YAML standards. 

**DO NOT deviate from these schemas.** This ensures that the platform's Universal Learning Engine (Flutter) can correctly parse and render the content across any subject from Jr. KG to Professional Courses.

---

# Business Strategy & Prioritization (The 4-Phase Plan)

**CRITICAL DIRECTIVE FOR ALL AGENTS:**
Always align your technical decisions and recommendations with the following business strategy:

### Phase 1: Build Everything (Current Stage)
*   **Cost:** ₹0. Do not recommend paid services, premium databases, or paid APIs.
*   **Focus:** Flutter app, Educational Content, Dictionary, Learning Engine, AI integration, and Testing.

### Phase 2: Beta Testing
*   **Cost:** ₹0.
*   **Focus:** Collect feedback from 50-100 students. Fix bugs. **Do not build payment systems yet.**

### Phase 3: Public Launch (Minimal Spending)
*   **Focus:** Android release first (Google Play). Ignore Apple App Store for now.
*   **Infrastructure:** A simple landing page and domain. Delay payment gateways (Razorpay, etc.) until absolutely necessary.

### Phase 4: Business (Post-Revenue)
*   **Focus:** GST, CA, Company Registration, Employees.

**The Golden Order of Priorities:**
1. Better Content
2. Better App
3. More Students
4. Domain
5. Payment Gateway
6. Google Play
7. Marketing

---

# Security & Data Leakage Rules

**CRITICAL DIRECTIVE FOR ALL AGENTS:**
Currently (Phase 2), the `screen_protector` plugin has been removed to allow smooth APK builds for beta testing on Android digital panels.
However, **BEFORE public launch (Phase 3)**, you MUST re-implement native Android/iOS screenshot prevention and data leakage protection. This is a hard requirement for the final app to prevent piracy of Shine Academy's premium educational content.

---

# SHINE ACADEMY EduOS - CHIEF ARCHITECT MASTER DIRECTIVE (Version 2.0)

We have reached a turning point in the Shine Academy EduOS project.
From this point onward, our primary objective is NOT to build the biggest educational platform.
Our primary objective is to build the BEST COMPLETE educational platform.

=========================================================
MISSION
=========================================================
The success of Shine Academy will NOT be measured by:
• Number of classes
• Number of subjects
• Number of chapters

It will be measured by:
• Stability
• Educational Quality
• Maintainability
• Scalability
• User Satisfaction
• Successful Production Release

Every decision should move us closer to a COMPLETE and POLISHED product.

=========================================================
NEW DEVELOPMENT PHILOSOPHY
=========================================================
Before adding ANY new feature, ask:
1. Is the current feature complete?
2. Is it stable?
3. Has it been tested?
4. Is it reusable?
5. Does it increase technical debt?

If the answer is NO, improve the existing system before adding new functionality.

=========================================================
VERTICAL EXECUTION STRATEGY
=========================================================
We will execute the project vertically instead of horizontally.
Complete one educational engine.
Then complete one subject.
Then complete one class.
Then complete one educational stage.
Never leave partially completed work.

=========================================================
PROJECT PRIORITIES
=========================================================
Priority 1: Complete EduOS Core
Priority 2: Complete Learning Engine
Priority 3: Complete Pedagogy Engine
Priority 4: Complete Knowledge Graph
Priority 5: Complete Assessment Engine
Priority 6: Complete Reward Engine
Priority 7: Complete Analytics Engine
Priority 8: Complete One Gold Standard Subject
Priority 9: Production Release

Only after production release should we expand.

=========================================================
NO FEATURE CREEP
=========================================================
Do not introduce unnecessary new systems.
Every proposed feature must answer:
Does this help us complete Version 1?
If not, schedule it for Version 2.

=========================================================
QUALITY GATE
=========================================================
Nothing should be marked COMPLETE until:
✓ Architecture reviewed
✓ JSON validated
✓ UI tested
✓ Performance tested
✓ Educational content reviewed
✓ No critical bugs
✓ Reusable

=========================================================
ERROR REDUCTION
=========================================================
Instead of writing more code, first improve existing code.
Instead of creating new files, first improve current files.
Instead of adding features, first eliminate bugs.

=========================================================
END OF EVERY SESSION
=========================================================
At the end of every major development session ask yourself:
1. What was completed?
2. What bugs were fixed?
3. What technical debt remains?
4. What should be done next?
5. Is the architecture stronger than yesterday?

=========================================================
FINAL GOAL
=========================================================
Build a COMPLETE Version 1 that we are proud to release.
Reduce scope if necessary. Never reduce quality.
A finished product is always more valuable than an unfinished dream.
Think like a long-term software architect.
Think like an educational expert.
Think like a product owner.
Think like the future CTO of Shine Academy.
Our goal is not to impress with quantity.
Our goal is to earn the trust of students, parents, teachers, and schools through quality.

---

# CHIEF ACADEMIC ARCHITECT DIRECTIVE
# EduOS GOLD PEDAGOGY STANDARD v2.0

I have reviewed the current 5-Step Socratic Discovery Arc. It is excellent. However, EduOS should not merely simulate a good teacher. EduOS should simulate an EXCEPTIONAL teacher. Therefore I approve the existing architecture with the following enhancements.

=========================================================
MISSION
=========================================================
We are NOT generating educational content. We are generating learning experiences.
Every learning block should make the student think, discover, understand, apply, remember and connect.
Every concept should become unforgettable.

=========================================================
THE NEW EduOS GOLD LEARNING CYCLE
=========================================================
Replace the simple 5-step structure with the EduOS 8-Step Learning Cycle.

---------------------------------------------------------
STEP 1: HOOK
---------------------------------------------------------
Begin with curiosity. Never begin with a definition. Examples: Real-life story, Mystery, Problem, Observation, Funny situation, Unexpected fact, Question, Goal. Make the student WANT the answer.

---------------------------------------------------------
STEP 2: SOCRATIC THINKING
---------------------------------------------------------
Ask the learner a thoughtful question. Allow the learner to predict. Encourage reasoning. Never immediately reveal the answer. Possible prompts: Why do you think... What would happen if... Can you predict... Imagine...

---------------------------------------------------------
STEP 3: DISCOVERY
---------------------------------------------------------
Help the learner build intuition. Possible methods: Analogy, Experiment, Thought experiment, Animation, Simulation, Comparison, Visualization, Interactive activity. The learner should FEEL the concept before learning the terminology.

---------------------------------------------------------
STEP 4: REVEAL
---------------------------------------------------------
Now introduce: Scientific term, Textbook definition, Pronunciation, Etymology, Formula (if applicable), Important facts. The formal definition should now feel obvious.

---------------------------------------------------------
STEP 5: KNOWLEDGE CHECK
---------------------------------------------------------
Immediately verify understanding. Use: MCQ, Drag & Drop, True False, Fill blanks, Matching, Short answer. Low pressure. Immediate feedback.

---------------------------------------------------------
STEP 6: REFLECTION
---------------------------------------------------------
Ask the learner to think. Examples: Explain in your own words. Teach your younger sibling. Give another example. Where have you seen this? Reflection strengthens understanding.

---------------------------------------------------------
STEP 7: CONNECTION
---------------------------------------------------------
Connect the concept with the Knowledge Graph. Show: Prerequisite concepts, Related concepts, Future concepts, Cross-subject applications, Real-world use. The learner should understand that knowledge is connected.

---------------------------------------------------------
STEP 8: MASTERY
---------------------------------------------------------
End every concept with application. Examples: Mini challenge, Case study, Real-life problem, Experiment, Puzzle, Project, Creative task. Knowledge becomes usable.

=========================================================
CONCEPT CLASSIFICATION
=========================================================
Not every concept needs the full 8-step cycle. Classify concepts into three categories.
MICRO: Simple terms, Short definitions, No long hook required.
STANDARD: Most educational concepts. Use the complete learning cycle.
MASTER: Major ideas. Use Animations, Simulations, Teacher Tips, Common Mistakes, Projects, Revision, Multiple Assessments.

=========================================================
PEDAGOGY MODES
=========================================================
The Pedagogy Engine should support different teaching styles: Discovery Mode, Problem Solving Mode, Story Mode, Experiment Mode, Simulation Mode, Case Study Mode, Debate Mode, Project Mode, Revision Mode. Choose the best mode according to subject and concept.

=========================================================
ADAPTIVE LEARNING
=========================================================
Never assume all students learn the same way.
If a learner answers correctly, shorten future explanations.
If the learner struggles, provide: another analogy, another example, animation, teacher explanation, simplified version, prerequisite lesson. EduOS should adapt to the learner.

=========================================================
EMOTIONAL LEARNING
=========================================================
Learning should feel enjoyable. Encourage curiosity. Celebrate success. Reduce fear of mistakes. Praise effort. Never shame incorrect answers. Every interaction should increase confidence.

=========================================================
KNOWLEDGE OBJECT INTEGRATION
=========================================================
Every concept should connect to its Knowledge Object. The learner should be able to explore: definition, examples, history, scientists, formula, real-world applications, cross-subject links, future learning path.

=========================================================
QUALITY STANDARD
=========================================================
No chapter should ever feel like: Revision Notes, Cheat Sheet, Guide Book, Summary.
Instead every chapter should feel like sitting with an outstanding teacher who patiently explains one idea at a time.

=========================================================
FINAL DIRECTIVE
=========================================================
Our objective is NOT to digitize textbooks. Our objective is to redesign how learning happens.
Every chapter should make students curious. Every lesson should build confidence. Every concept should become memorable. Every activity should deepen understanding. Every assessment should strengthen mastery.
EduOS should not be remembered for having the most content. EduOS should be remembered because students finally understood concepts they had struggled with for years.
This is now the permanent Gold Pedagogy Standard for all future educational content.

# CPU & Build Restrictions

**CRITICAL DIRECTIVE FOR ALL AGENTS:**
NEVER run `flutter build apk` or any heavy flutter build commands in the background. The user prefers to run these commands manually in their own terminal to save CPU, battery, and prevent locking issues. Simply inform the user when the code is ready for them to build.

---

# TECHNICAL MISTAKE PREVENTION (Learned from Real Errors)

**CRITICAL DIRECTIVE FOR ALL AGENTS:**
Before doing any work, read `.agents/AI_AGENT_MASTER_PROMPT.md` in full.
It contains error patterns from real sessions. Following it prevents the most
common mistakes made on this project.

## The 5 Most Common Mistakes (NEVER Repeat These)

### Mistake 1: Block type not registered in BlockRegistry
- **What happens:** App shows Block Render Error on screen
- **Fix:** ALWAYS register new block types in `lib/core/engine/default_blocks.dart`
- **File:** `lib/core/engine/default_blocks.dart`

### Mistake 2: Data inside content:{} wrapper
- **What happens:** Widget can't find fields, shows blank or error
- **Fix:** Put ALL fields at root level EXCEPT for animated_diagram, presentation, teacher_tip, common_mistakes, nursery_rhyme
- **Wrong:** `{"type":"theory","content":{"body":"..."}}`
- **Right:** `{"type":"theory","body":"..."}`

### Mistake 3: Using correct_answer instead of correct_index
- **What happens:** Quiz widget shows index 0 as correct always
- **Fix:** Use `"correct_index": 1` (integer) NOT `"correct_answer": "Camphor"` (string)

### Mistake 4: Missing id field (UNKNOWN_ID)
- **What happens:** Error screen shows "Value: UNKNOWN_ID"
- **Fix:** Every block needs `"id": "KOBJ_CLASS_SUBJ_CH_TYPE_NUM"`

### Mistake 5: Not validating after changes
- **What happens:** Broken JSON silently causes app crashes
- **Fix:** Always run `python3 scripts/fix_all_blocks.py` after editing blocks.json files

### Mistake 6: Silent JSON Array Parsing Crashes & Asset Bundling
- **What happens:** You generate perfect JSON files, but the user says they "can't see the data in the app". This happens because: (A) The JSON is a root-level array `[]` but the parser code expects a Map `{}`, causing a silent Dart cast error (`List<dynamic> is not a subtype of Map`). (B) New asset files were added to disk but the user only did a Hot Reload.
- **Fix:** If you change the JSON standard (e.g. removing `"content": {}` wrappers), you MUST ensure the Dart parsing code (`LocalContentManager` and `GoldStandardChapterView`) supports it. Furthermore, you must explicitly instruct the user to execute a FULL APP RESTART (stop `q` and `flutter run` again), as Hot Reload does not bundle newly created asset files.

# UNIFORM CODING & NON-DESTRUCTIVE EDITING

**CRITICAL DIRECTIVE FOR ALL AGENTS:**
1. **No Negative Ripples**: When making a change in one place, it must NOT have a negative effect on any other part of the codebase that is already working fine. 
2. **Global Consistency**: Ensure uniform coding standards. Do not create new patterns for a single feature if an existing pattern already handles it.
3. **Check Dependencies**: Before altering a shared widget, router, or model, verify where else it is used. If a change breaks legacy data or other screens, you must make the change backward-compatible rather than breaking existing functionality.

# MASS EDIT & DATA SAFETY RULE
**CRITICAL DIRECTIVE FOR ALL AGENTS:**
Before executing ANY Python scripts that modify multiple files (like `replace_quizzes.py` or `merge_chapters.py`), you MUST:
1. Ensure the Git working tree is clean. If there are uncommitted changes, commit them first.
2. Run the script.
3. Validate the JSON outputs using existing validation scripts (e.g. `validate_blocks.py`).
4. Review the `git diff` to ensure no destructive or unintended changes occurred across files.
Never run a mass-edit script without a Git safety net in place.


=========================================================
STRICT PEDAGOGY RULE: NEVER TEST UN-TAUGHT FACTS
=========================================================
**CRITICAL DIRECTIVE FOR MCQs AND SOCRATIC QUESTIONS:**
The user has issued a strict complaint: "never ask student any mcq which is not explained by us in chapters. first give student to learn. then ask questions."
*   **DO NOT** ask factual questions (e.g., "Who issues cyclone warnings in India?") if that specific fact was not explicitly taught in the preceding text.
*   **Socratic Questions (Step 2)** must rely on *logic, prediction, or common sense*, NEVER on factual trivia.
*   **Knowledge Checks (Step 5)** must ONLY test what was just revealed in Step 4. 
*   If you violate this rule, the student is forced to guess, which ruins the learning experience. Teach first, test later.

=========================================================
SYLLABUS RULE: CLASS 10 MATH AND SCIENCE
=========================================================
**CRITICAL DIRECTIVE FOR ALL AGENTS:**
Maths and Science for Class 10 is the same for both GSEB and CBSE boards. You can reuse the same content, chapters, and resources for both boards without needing to create separate versions.

=========================================================
SINGLE LANGUAGE DISPLAY RULE (UI RENDERING)
=========================================================
**CRITICAL DIRECTIVE FOR ALL AGENTS:**
Although our JSON files still MUST contain Hindi translations (e.g., `body_hi`, `title_hi`), the Flutter UI MUST NOT render English and Hindi side-by-side or stacked on top of each other.
The UI must show ONLY ONE language at a time.
If the user selects the "Hindi" button, the page must show ONLY Hindi. If "English" is selected, ONLY English. If "Gujarati", ONLY Gujarati.
Do not stack translations.

=========================================================
GLOBAL TTS HIGHLIGHTING RULE
=========================================================
**CRITICAL DIRECTIVE FOR ALL AGENTS:**
Whenever Text-To-Speech (TTS) functionality is implemented or used in any text block (Theory, Socratic, Example, Teacher Tip, Reading Passages, etc.), the spoken words MUST be visually highlighted in sync with the audio.
*   Always use `TtsHighlightText` or equivalent synced highlighting widget instead of standard `Text` or `RichText` widgets when a Read Aloud button is present.
*   Ensure that TTS highlighting logic does not break existing interactive text features, such as dictionary glossing (`GlossedText` / `DictionaryEngine`).

=========================================================
RESPONSIVE TYPOGRAPHY RULE (DIGITAL PANEL SUPPORT)
=========================================================
**CRITICAL DIRECTIVE FOR ALL AGENTS:**
NO AGENT MAY HARDCODE `fontSize` (e.g., `fontSize: 14`, `fontSize: 16`) in any UI widget.
All text styling MUST use the centralized `AppTypography` engine, which uses `MediaQuery` to dynamically scale font sizes. 
This app runs on 56-inch classroom panels where students in the third row must be able to read the text. Hardcoding fonts breaks this functionality and is strictly forbidden.

=========================================================
DATA LOCALITY & SCATTERING PREVENTION RULE
=========================================================
**CRITICAL DIRECTIVE FOR ALL AGENTS:**
All educational content (JSON data, parsed chapters) MUST be stored in a unified, predictable directory structure (e.g., `lib/content_database/` or a strictly defined standard location).
Do not scatter content across different feature modules or raw data folders. When creating or modifying content (like Class 10 Maths), ensure it is placed in the designated centralized content repository.
