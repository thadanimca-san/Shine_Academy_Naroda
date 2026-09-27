# AI Notes

## Date: 2026-08-04

**Task Completed**
Implemented dynamic language toggling for Accounts & Statistics (EN/GU) and established the core documentation framework.

**Files Modified**
- `lib/features/chapter/chapter_detail_screen.dart`
- Curriculum JSONs

**Architecture Decisions**
Instead of polluting the curriculum JSON with complex, nested language maps (which would break backwards compatibility with other single-language subjects), the language toggle was implemented directly in `ChapterDetailScreen.dart`. It intercepts the JSON file request and dynamically appends `_gu` to the filename if the user switches to Gujarati. 

**Important Notes**
- The app must never crash on missing files. The `rootBundle.loadString` call is wrapped in a `try/catch`. If `_gu.json` is missing, the UI triggers a SnackBar notification and safely falls back to the English default.
- PDF generation uses the `pdf` package and relies on `DejaVuSans` to properly render the Indian Rupee (₹) symbol. Ensure `pdf_branding_util.dart` correctly passes `pw.ThemeData.withFont(base: ttf)` to `pw.PageTheme` so that fonts aren't overridden by `MultiPage`.

**Future Recommendations**
- As the number of JSON files scales (potentially 100+ files per subject), consider migrating static JSONs to a local SQLite database (using `sqflite`) for faster queries, full-text search capabilities, and to lower the memory footprint.

**Known Risks**
- Storing hundreds of massive JSON files in `assets/` will increase the APK size significantly. If APK size becomes a constraint, consider delivering JSONs via an API backend or Firebase.

**Why this implementation was chosen**
JSON files allow rapid, structured generation of "Mahabharat" level comprehensive data without setting up a backend server during Phase 1/Phase 2. It keeps the app fully offline and self-contained, which is crucial for digital panel usage in classrooms with unreliable internet.
