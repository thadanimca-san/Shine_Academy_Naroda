# Application Architecture

## Folder Structure
```
Shine_Academy_Naroda/
├── app_core/                   # JSON data repository (Curriculum, Chapters, Languages, Dictionaries)
│   ├── chapters/               # Individual chapter data (e.g., gseb_class12_accounts_ch2.json)
│   ├── curriculum/             # Curriculum index files (e.g., gseb_class12_commerce.json)
│   └── languages/              # (Reserved for future localization definitions)
├── lib/                        # Main Dart Codebase
│   ├── core/                   # Utilities, global constants, and core services (ProfileService)
│   ├── features/               # Feature-based architectural breakdown
│   │   ├── chapter/            # ChapterDetailScreen and chapter parsing logic
│   │   ├── curriculum/         # Curriculum index screen (ChapterListScreen)
│   │   ├── dashboard/          # HomeScreen and app navigation
│   │   ├── learning/           # Subject-specific hubs and simulations
│   │   ├── profile/            # User profile selection and onboarding
│   │   └── settings/           # App settings (currently minimal)
│   └── foundation/             # Design System: AppColors, Themes, Typography
└── docs/                       # Project Documentation and AI continuity notes
```

## Navigation
Navigation is managed entirely by the `go_router` package.
- Routing logic is modular and centrally defined in `main.dart` or a dedicated router file.
- It leverages deep linking and parameterized routing (e.g., passing asset paths between screens).

## State Management
- Simple widget state is managed via `StatefulWidget` and `setState()`.
- User Profile data (Role, Stage, Class, Board) is persisted globally via `SharedPreferences` inside `ProfileService`.
- No heavy state management solution (Provider/Riverpod/Bloc) is used yet to keep the codebase simple, lightweight, and extremely fast on low-end hardware.

## Theme & UI
- Built on **Material 3**.
- Centralized color palette defined in `AppColors` (`lib/foundation/theme/app_colors.dart`).
- Uses `GoogleFonts` (Poppins for headers, Inter for body) to ensure a premium, modern aesthetic.

## Services
- `ProfileService`: Handles reading/writing user onboarding preferences.
- `PdfGeneratorService` / `PaperPdfService`: Handles exporting chapter data into branded PDF files.
- `PdfBrandingUtil`: Injects watermarks, headers, and ensures the custom `DejaVuSans` font is applied so the Rupee (₹) symbol renders successfully.

## JSON Structure
The app is entirely data-driven via local JSON files.
- **Curriculum JSONs:** Map subjects to an array of chapters, linking to their respective data files.
- **Chapter JSONs:** Highly structured files containing `theory_sections`, `definitions`, `examples`, `exercises`, and `previous_year_questions`.
- **Language Support:** Implemented via file naming convention (e.g., `_gu.json` for Gujarati). `ChapterDetailScreen` dynamically swaps the asset path based on a UI toggle.

## Future Expansion Strategy
- **Database Migration:** As the curriculum scales to hundreds of chapters, the flat JSON files in `app_core` should be migrated into an offline SQLite database for O(1) query time and full-text search capability.
- **State Management:** If we introduce real-time collaboration, quizzes, or complex user state, we should integrate Riverpod.
- **Cloud Sync:** Eventually syncing offline analytics (quiz scores) to a backend via REST/GraphQL.
