# Create New Feature (01_CREATE_NEW_FEATURE)

**Purpose**: This is the master prompt for implementing a new feature in the Shine Academy Naroda app. It establishes strict rules for architecture, code quality, and documentation to ensure the AI does not break existing functionality.

**When to use**: Use this whenever you want the AI to build a new screen, module, or core feature.

---

## The Prompt Template
*Copy and paste everything below this line to the AI when you request a new feature.*

---

**Context**: You are working on the Shine Academy Naroda project. I need you to implement a new feature: [DESCRIBE YOUR FEATURE HERE]

**Before writing any code, you MUST follow these directives:**
1. Read all existing related files.
2. Understand the current architecture.
3. Do not overwrite working code.
4. Improve the existing implementation.
5. Return COMPLETE files only.
6. Ensure the project compiles successfully.
7. Follow Material 3 design guidelines.
8. Follow feature-based architecture (`lib/features/`).
9. Reuse existing widgets and services wherever possible (check `lib/foundation/` and `lib/core/`).
10. Explain every file that you modify.

**After implementation, you must provide a summary containing:**
- Files modified
- Reason for each modification
- Any new folders created
- Any dependencies added
- Commands I should run (e.g., `flutter run -d linux`)
- Potential future improvements

Please acknowledge these rules and provide an Implementation Plan before proceeding.
