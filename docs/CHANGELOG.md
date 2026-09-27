# Changelog

## 2026-08-04

**Completed**
- Built foundational documentation structure (`docs/` folder).
- Developed a dynamic EN/GU language toggle for the Chapter Detail Screen.
- Generated comprehensive ("Mahabharat" level) JSON content for GSEB Class 12 Accounts and Statistics.
- Completed Phase 2, 3, and 4: Generated Accounts Ch 4-7, Statistics Ch 3-5, English Ch 1-2, OC Ch 1-2, Eco Ch 1-2.
- Integrated `screen_protector` package to prevent screenshots and screen recording.

**Files Modified**
- `lib/features/chapter/chapter_detail_screen.dart`
- `app_core/curriculum/gseb_class12_commerce.json`
- `lib/main.dart`
- `lib/features/learning/higher_secondary/commerce_accounts/views/home_screen.dart`

**Files Created**
- `docs/PROJECT_STATUS.md`
- `docs/CHANGELOG.md`
- `docs/ROADMAP.md`
- `docs/AI_NOTES.md`
- `docs/ARCHITECTURE.md`
- `app_core/chapters/gseb_class12_accounts_ch4.json` to `ch7.json` (and `_gu.json`)
- `app_core/chapters/gseb_class12_stats_ch3.json` to `ch5.json` (and `_gu.json`)
- `app_core/chapters/gseb_class12_english_ch1.json` to `ch2.json`
- `app_core/chapters/gseb_class12_oc_ch1.json` to `ch2.json`
- `app_core/chapters/gseb_class12_eco_ch1.json` to `ch2.json`

**Reason for Changes**
- User requested absolute comprehensive coverage for the Commerce curriculum.
- User requested English-medium first, but immediate Gujarati availability for Accounts and Statistics.
- User requested standardizing AI-to-AI communication and project tracking via markdown documentation.

**Notes**
- The language toggle dynamically rewrites the asset path to point to `_gu.json` if Gujarati is selected. It gracefully falls back to English if the Gujarati file is missing, ensuring the app never crashes on missing language assets.
